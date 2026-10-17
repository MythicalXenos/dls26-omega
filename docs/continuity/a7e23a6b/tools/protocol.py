#!/usr/bin/env python3
"""tools/protocol.py — executable field contract for DLS26 Omega protocol version 2.

Defines and validates the on-disk contracts referenced by OMEGA-STATE-001 and
OMEGA-CHECKPOINT-001:

  * logs/control.json            (state / operation binding)
  * logs/turn_manifest.json      (immutable checkpoint envelope)
  * logs/exits/*.exit.json       (predecessor exit proofs)
  * logs/sources_visited.json    (frontier / epoch contract)   [structural subset]
  * DLS26_OMEGA_PROMPT.md        (OMEGA-RULE block linker)

This module checks SYNTAX, required fields, JSON strictness (duplicate keys,
non-finite numbers), path safety (no symlinks / repo escape) and reference
resolution. It cannot and does not judge whether evidence is true or adequate
(OMEGA-STATE-001: "a validator does not infer that an arbitrary text file is
adequate evidence").

CLI:
  python3 tools/protocol.py check-all
  python3 tools/protocol.py check-master [path]
  python3 tools/protocol.py check-control
  python3 tools/protocol.py check-manifest
  python3 tools/protocol.py check-exits
"""

from __future__ import annotations

import json
import math
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCHEMA_CONTROL = "control-1.0"
SCHEMA_TURN_MANIFEST = "turn_manifest-1.0"
SCHEMA_EXIT = "exit_proof-1.0"
SCHEMA_SOURCES = "sources_visited-1.0"

PROTOCOL_VERSION = 2

PHASES = {"WORKING", "COMPLETED", "WAITING_USER", "BLOCKED"}
STEPS = {0, 1, 2, 3, 4, 5}
DEVICE_DISPOSITIONS = {"UNASSESSED", "READY", "DECLINED", "UNAVAILABLE"}
TERMINAL_CLASSES = {
    "BOOTSTRAP_START",
    "CONTINUE",
    "ATTENTION_REQUIRED",
    "PUBLICATION_PENDING",
    "PROTOCOL_ERROR",
    "COMPLETE",
    "RESEARCH_CONTINUE",
    "RESEARCH_PAUSED",
    "RESEARCH_COMPLETE",
}
TERMINAL_LINES = {
    "BOOTSTRAP_START": "Bootstrap started. Send > to continue background research.",
    "ATTENTION_REQUIRED": "Bootstrap paused [ATTENTION_REQUIRED]. Do not send >.",
    "PUBLICATION_PENDING": "Bootstrap paused [PUBLICATION_PENDING]. Do not send >.",
    "PROTOCOL_ERROR": "Bootstrap paused [PROTOCOL_ERROR]. Do not send >.",
    "COMPLETE": "Bootstrap complete. Do not send >; answer the questions above.",
    "RESEARCH_CONTINUE": "Research in progress. Send > to continue.",
    "RESEARCH_PAUSED": "Research paused. Do not send >.",
    "RESEARCH_COMPLETE": "Research complete. Do not send >.",
}
CONTINUE_PATTERN = re.compile(r"^Bootstrap in progress \[Step [0-4]\]\. Send > to continue\.$")

CONTROL_REQUIRED_FIELDS = [
    "schema", "protocol_version", "session_id", "operation_id",
    "operation_request_ref", "conversation_binding", "mode", "step", "phase",
    "next_step", "device_disposition", "predecessor_exits", "physical_evidence",
    "resumption_point", "updated_at",
]

MANIFEST_REQUIRED_FIELDS = [
    "schema", "protocol_version", "session_id", "turn_id", "sequence",
    "checkpoint_nonce", "mode", "step", "phase", "next_step",
    "terminal_line_class", "terminal_line", "parent_commit", "prompt_sha256",
    "artifact_manifest", "created_at",
]

MANIFEST_FORBIDDEN_KEYS = {
    "enclosing_commit", "own_commit", "checkpoint_commit", "commit_hash",
    "self_commit", "this_commit",
}

EXIT_REQUIRED_FIELDS = [
    "schema", "protocol_version", "session_id", "step", "reviewer",
    "accepted_disposition", "evidence", "limitations", "created_at",
]


class ProtocolError(Exception):
    pass


# ---------------------------------------------------------------- JSON strict

def _no_dupes(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ProtocolError("duplicate key in JSON object: %r" % k)
        out[k] = v
    return out


def _no_nonfinite(x):
    raise ProtocolError("non-finite JSON number: %r" % (x,))


def load_json_strict(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            raw = fh.read()
    except FileNotFoundError:
        raise ProtocolError("missing file: %s" % path)
    return json.loads(raw, object_pairs_hook=_no_dupes, parse_constant=_no_nonfinite)


# ---------------------------------------------------------------- path safety

def safe_repo_path(relpath):
    """Reject absolute paths, '..' escapes and symlinks; return repo-relative path."""
    if not isinstance(relpath, str) or not relpath:
        raise ProtocolError("empty artifact path")
    if relpath.startswith("/") or relpath.startswith("~"):
        raise ProtocolError("unsafe absolute path: %r" % relpath)
    if relpath.startswith(".omega/"):
        raise ProtocolError("journal/receipt area must stay outside committed manifests: %r" % relpath)
    full = os.path.realpath(os.path.join(REPO_ROOT, relpath))
    root = os.path.realpath(REPO_ROOT)
    if full != root and not full.startswith(root + os.sep):
        raise ProtocolError("path escapes repository: %r" % relpath)
    if os.path.islink(os.path.join(REPO_ROOT, relpath)):
        raise ProtocolError("symlink rejected: %r" % relpath)
    return relpath.replace(os.sep, "/")


def sha256_file(path):
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------- master linker

RULE_OPEN = re.compile(r"^<!--\s*OMEGA-RULE\s+(\{.*\})\s*-->\s*$")
RULE_CLOSE = "<!-- /OMEGA-RULE -->"


def parse_rule_blocks(text):
    """Return list of (meta_dict, body_text, line_no). Validates balanced/unnested blocks."""
    lines = text.splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        m = RULE_OPEN.match(lines[i].strip()) if lines[i].strip().startswith("<!-- OMEGA-RULE") else None
        if m is None:
            if lines[i].strip().startswith("<!-- OMEGA-RULE"):
                raise ProtocolError("malformed OMEGA-RULE open tag at line %d" % (i + 1))
            i += 1
            continue
        try:
            meta = json.loads(m.group(1), object_pairs_hook=_no_dupes, parse_constant=_no_nonfinite)
        except json.JSONDecodeError as exc:
            raise ProtocolError("invalid rule JSON at line %d: %s" % (i + 1, exc))
        if not isinstance(meta, dict) or not meta.get("id"):
            raise ProtocolError("rule meta missing id at line %d" % (i + 1))
        body = []
        j = i + 1
        closed = False
        while j < len(lines):
            s = lines[j].strip()
            if s.startswith("<!-- OMEGA-RULE"):
                raise ProtocolError("nested OMEGA-RULE block at line %d" % (j + 1))
            if s == RULE_CLOSE:
                closed = True
                break
            body.append(lines[j])
            j += 1
        if not closed:
            raise ProtocolError("unclosed OMEGA-RULE block starting line %d" % (i + 1))
        body_text = "\n".join(body).strip()
        if not body_text:
            raise ProtocolError("empty rule body for %s" % meta["id"])
        blocks.append((meta, body_text, i + 1))
        i = j + 1
    return blocks


def check_master(path=None):
    path = path or os.path.join(REPO_ROOT, "DLS26_OMEGA_PROMPT.md")
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if "END DLS26 OMEGA PROMPT" not in text:
        raise ProtocolError("master missing END marker")
    blocks = parse_rule_blocks(text)
    if not blocks:
        raise ProtocolError("no OMEGA-RULE blocks found")
    ids = [meta["id"] for meta, _, _ in blocks]
    if len(ids) != len(set(ids)):
        raise ProtocolError("duplicate rule ids")
    idset = set(ids)
    for meta, _, line_no in blocks:
        for ref in meta.get("refs", []):
            if ref not in idset:
                raise ProtocolError("unresolved ref %r in %s (line %d)" % (ref, meta["id"], line_no))
        if meta.get("list_mode") not in {"open", "fixed"}:
            raise ProtocolError("bad list_mode in %s" % meta["id"])
        if meta.get("data_mode") != "framework":
            raise ProtocolError("bad data_mode in %s" % meta["id"])
    return {"rules": len(blocks), "ids": ids, "sha256": sha256_file(path)}


# ---------------------------------------------------------------- control.json

def check_control(path=None):
    path = path or os.path.join(REPO_ROOT, "logs", "control.json")
    doc = load_json_strict(path)
    missing = [f for f in CONTROL_REQUIRED_FIELDS if f not in doc]
    if missing:
        raise ProtocolError("control.json missing fields: %s" % missing)
    if doc["schema"] != SCHEMA_CONTROL:
        raise ProtocolError("control.json schema mismatch: %r" % doc["schema"])
    if doc["protocol_version"] != PROTOCOL_VERSION:
        raise ProtocolError("protocol_version mismatch")
    if doc["phase"] not in PHASES:
        raise ProtocolError("bad phase %r" % doc["phase"])
    if doc["step"] not in STEPS or doc["next_step"] not in STEPS:
        raise ProtocolError("bad step/next_step")
    if doc["device_disposition"] not in DEVICE_DISPOSITIONS:
        raise ProtocolError("bad device_disposition %r" % doc["device_disposition"])
    binding = doc["conversation_binding"]
    if not isinstance(binding, dict) or "observed_from_host" not in binding:
        raise ProtocolError("conversation_binding must record observed_from_host")
    for ex in doc["predecessor_exits"]:
        safe_repo_path(ex["exit_file"]) if "exit_file" in ex else None
        if "exit_file" in ex and not os.path.isfile(os.path.join(REPO_ROOT, ex["exit_file"])):
            raise ProtocolError("predecessor exit file missing: %s" % ex.get("exit_file"))
    for p in doc["physical_evidence"]:
        rel = p if isinstance(p, str) else p.get("path")
        safe_repo_path(rel)
        if not os.path.exists(os.path.join(REPO_ROOT, rel)):
            raise ProtocolError("physical evidence missing: %s" % rel)
    return {"step": doc["step"], "phase": doc["phase"]}


# ---------------------------------------------------------------- exits

def check_exits():
    exit_dir = os.path.join(REPO_ROOT, "logs", "exits")
    results = []
    if not os.path.isdir(exit_dir):
        raise ProtocolError("logs/exits missing")
    for name in sorted(os.listdir(exit_dir)):
        if not name.endswith(".exit.json"):
            continue
        path = os.path.join(exit_dir, name)
        doc = load_json_strict(path)
        missing = [f for f in EXIT_REQUIRED_FIELDS if f not in doc]
        if missing:
            raise ProtocolError("%s missing fields: %s" % (name, missing))
        if doc["schema"] != SCHEMA_EXIT or doc["protocol_version"] != PROTOCOL_VERSION:
            raise ProtocolError("%s schema/protocol mismatch" % name)
        if doc["step"] not in STEPS:
            raise ProtocolError("%s bad step" % name)
        for ev in doc.get("evidence", []):
            if "sha256" in ev and not re.fullmatch(r"[0-9a-f]{64}", ev["sha256"]):
                raise ProtocolError("%s bad evidence hash" % name)
        results.append({"file": name, "step": doc["step"]})
    return results


# ---------------------------------------------------------------- turn manifest

def check_manifest(path=None):
    path = path or os.path.join(REPO_ROOT, "logs", "turn_manifest.json")
    doc = load_json_strict(path)
    missing = [f for f in MANIFEST_REQUIRED_FIELDS if f not in doc]
    if missing:
        raise ProtocolError("turn_manifest.json missing fields: %s" % missing)
    if doc["schema"] != SCHEMA_TURN_MANIFEST:
        raise ProtocolError("turn_manifest schema mismatch")
    if doc["protocol_version"] != PROTOCOL_VERSION:
        raise ProtocolError("protocol_version mismatch")
    bad = MANIFEST_FORBIDDEN_KEYS.intersection(doc.keys())
    if bad:
        raise ProtocolError("turn manifest must not contain its enclosing commit hash; forbidden keys: %s" % sorted(bad))
    if not re.fullmatch(r"[0-9a-f]{40}", doc["parent_commit"]):
        raise ProtocolError("parent_commit must be a full 40-char git sha")
    if not re.fullmatch(r"[0-9a-f]{64}", doc["prompt_sha256"]):
        raise ProtocolError("prompt_sha256 malformed")
    if doc["terminal_line_class"] not in TERMINAL_CLASSES:
        raise ProtocolError("bad terminal_line_class")
    cls = doc["terminal_line_class"]
    if cls == "CONTINUE":
        if not CONTINUE_PATTERN.match(doc["terminal_line"]):
            raise ProtocolError("bad CONTINUE line: %r" % doc["terminal_line"])
    elif doc["terminal_line"] != TERMINAL_LINES[cls]:
        raise ProtocolError("terminal_line does not match class %s" % cls)
    if doc["phase"] not in PHASES or doc["step"] not in STEPS:
        raise ProtocolError("bad phase/step in manifest")
    if not doc["artifact_manifest"]:
        raise ProtocolError("artifact_manifest must be nonempty")
    seen = set()
    for item in doc["artifact_manifest"]:
        rel = safe_repo_path(item["path"])
        if rel in seen:
            raise ProtocolError("duplicate artifact path: %s" % rel)
        seen.add(rel)
        full = os.path.join(REPO_ROOT, rel)
        if not os.path.isfile(full):
            raise ProtocolError("artifact missing: %s" % rel)
        if sha256_file(full) != item["sha256"]:
            raise ProtocolError("artifact hash mismatch: %s" % rel)
        if os.path.getsize(full) != item["bytes"]:
            raise ProtocolError("artifact size mismatch: %s" % rel)
        if rel == "logs/turn_manifest.json":
            raise ProtocolError("manifest must not include itself")
    return {"artifacts": len(doc["artifact_manifest"]), "turn_id": doc["turn_id"]}


# ---------------------------------------------------------------- sources (subset)

def check_sources():
    path = os.path.join(REPO_ROOT, "logs", "sources_visited.json")
    doc = load_json_strict(path)
    if doc.get("schema") != SCHEMA_SOURCES:
        raise ProtocolError("sources_visited schema mismatch")
    if not doc.get("epochs"):
        raise ProtocolError("sources_visited.json must carry at least the sealed epoch contract")
    for ep in doc["epochs"]:
        for field in ("epoch_id", "scope_trigger", "as_of", "required_dimensions",
                      "discovery_procedure", "status"):
            if field not in ep:
                raise ProtocolError("epoch missing %s" % field)
    statuses = {r.get("status") for r in doc.get("references", [])}
    allowed = {"UNVISITED", "IN_PROGRESS", "RETRYABLE_FAILURE", "VISITED",
               "ACCESS_BOUNDARY", "REPRESENTATION_DUPLICATE", "NON_CONNECTED"}
    bad = statuses - allowed
    if bad:
        raise ProtocolError("unknown reference dispositions: %s" % sorted(bad))
    return {"epochs": len(doc["epochs"]), "references": len(doc.get("references", []))}


# ---------------------------------------------------------------- orchestrator

def check_all():
    report = {}
    report["master"] = check_master()
    report["control"] = check_control()
    report["exits"] = check_exits()
    report["manifest"] = check_manifest()
    report["sources"] = check_sources()
    return report


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "check-all"
    try:
        if cmd == "check-master":
            out = check_master(argv[2] if len(argv) > 2 else None)
        elif cmd == "check-control":
            out = check_control()
        elif cmd == "check-manifest":
            out = check_manifest()
        elif cmd == "check-exits":
            out = check_exits()
        elif cmd == "check-sources":
            out = check_sources()
        elif cmd == "check-all":
            out = check_all()
        else:
            print("unknown command: %s" % cmd, file=sys.stderr)
            return 2
    except ProtocolError as exc:
        print("FAIL: %s" % exc, file=sys.stderr)
        return 1
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
