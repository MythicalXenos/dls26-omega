#!/usr/bin/env python3
"""tools/checkpoint.py — durable turn transactions (OMEGA-CHECKPOINT-001).

Separation of concerns:
  prepare  1) serialize writers with a repository lock
           2) run tools/protocol.py contract checks
           3) reject unrelated dirty work (only expected omega artifacts may change)
           4) reserve the logical turn in the local Git metadata journal
              (.omega/journal/turns.jsonl), BEFORE the commit
           5) write logs/turn_manifest.json from the reserved meta +
              computed artifact path/hash manifest (manifest never contains
              its own enclosing commit hash and never lists itself)
           6) stage + commit the complete checkpoint; verify staged blob bytes
           7) journal the commit hash; install git ref refs/omega/turns/<turn_id>

  publish  1) verify HEAD equals the journaled commit for the turn
           2) ordinary push of the fixed branch (no force, no rebase, no merge)
           3) verify remote branch points at that exact commit (ls-remote)
           4) write the publication receipt OUTSIDE the immutable commit it
              describes (.omega/receipts/<turn_id>.json)
           5) journal the publication

Crash recovery: a reserved journal entry without a commit hash whose manifest
hash matches a later commit by the same parent is reconciled; a divergent HEAD
or changed working tree requires explicit reconciliation — never force.

Usage:
  python3 tools/checkpoint.py prepare --meta .omega/journal/turn_meta.json
  python3 tools/checkpoint.py publish --turn-id turn-xxxx
"""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import subprocess
import sys
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRANCH = "arena/a7e23a6b-dls26-omega"
JOURNAL_DIR = os.path.join(REPO_ROOT, ".omega", "journal")
RECEIPT_DIR = os.path.join(REPO_ROOT, ".omega", "receipts")
LOCK_PATH = os.path.join(REPO_ROOT, ".omega", "lock")
JOURNAL_PATH = os.path.join(JOURNAL_DIR, "turns.jsonl")
MANIFEST_PATH = os.path.join(REPO_ROOT, "logs", "turn_manifest.json")

# Paths that are allowed to appear dirty during an omega checkpoint.
ALLOWED_DIRTY_PREFIXES = (
    "DLS26_OMEGA_PROMPT.md",
    "OPERATIONAL_RULES.md",
    "HANDOFF.md",
    ".gitignore",
    "README.md",
    "docs/",
    "logs/",
    "handoff/",
    "evidence/",
    "kb/",
    "profile/",
    "plans/",
    "audits/",
    "config/",
    "schemas/",
    "tools/",
    "exits/",
    "research/",
)


def sh(args, check=True, capture=True):
    proc = subprocess.run(args, cwd=REPO_ROOT, text=True,
                          capture_output=capture, check=False)
    if check and proc.returncode != 0:
        raise RuntimeError("command failed: %s\n%s\n%s" % (args, proc.stderr, proc.stdout))
    return proc


def journal_append(entry):
    os.makedirs(JOURNAL_DIR, exist_ok=True)
    entry = dict(entry)
    entry["journal_time"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(JOURNAL_PATH, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, sort_keys=True) + "\n")


def journal_entries():
    if not os.path.isfile(JOURNAL_PATH):
        return []
    out = []
    with open(JOURNAL_PATH, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def acquire_lock():
    os.makedirs(os.path.dirname(LOCK_PATH), exist_ok=True)
    fh = open(LOCK_PATH, "a+")
    try:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        raise RuntimeError("repository lock is held by another writer")
    return fh


def git_head():
    return sh(["git", "rev-parse", "HEAD"]).stdout.strip()


def git_parent():
    return sh(["git", "rev-parse", "HEAD^"]).stdout.strip()


def dirty_files():
    proc = sh(["git", "status", "--porcelain"])
    out = []
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        out.append(line[3:].strip().strip('"'))
    return out


def check_dirty_allowed():
    bad = []
    for rel in dirty_files():
        if rel.startswith(".omega/") or rel == "logs/turn_manifest.json":
            continue
        if not any(rel.startswith(p) or rel == p.rstrip("/") for p in ALLOWED_DIRTY_PREFIXES):
            bad.append(rel)
    if bad:
        raise RuntimeError("unrelated dirty work present, refusing checkpoint: %s" % bad)


def artifact_manifest():
    """Exact path/hash/bytes for every tracked artifact except the manifest itself."""
    sh(["git", "add", "-A"])
    proc = sh(["git", "diff", "--cached", "--name-only"])
    items = []
    for rel in sorted(proc.stdout.splitlines()):
        rel = rel.strip()
        if not rel or rel == "logs/turn_manifest.json" or rel.startswith(".omega/"):
            continue
        if os.path.islink(os.path.join(REPO_ROOT, rel)):
            raise RuntimeError("symlink in staged tree: %s" % rel)
        full = os.path.join(REPO_ROOT, rel)
        h = hashlib.sha256()
        with open(full, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 16), b""):
                h.update(chunk)
        items.append({"path": rel, "sha256": h.hexdigest(),
                      "bytes": os.path.getsize(full)})
    return items


def verify_staged_blobs(items):
    for it in items:
        proc = subprocess.run(["git", "cat-file", "blob", ":%s" % it["path"]],
                              cwd=REPO_ROOT, capture_output=True, check=True)
        got = hashlib.sha256(proc.stdout).hexdigest()
        if got != it["sha256"]:
            raise RuntimeError("staged blob hash mismatch for %s" % it["path"])


def run_protocol_checks():
    sys.path.insert(0, os.path.join(REPO_ROOT, "tools"))
    import protocol
    return protocol.check_all()


def prepare(meta_path):
    lock = acquire_lock()
    try:
        with open(meta_path, "r", encoding="utf-8") as fh:
            meta = json.load(fh)
        for field in ("turn_id", "sequence", "checkpoint_nonce", "session_id",
                      "mode", "step", "phase", "next_step", "terminal_line_class",
                      "terminal_line", "prompt_sha256", "created_at"):
            if field not in meta:
                raise RuntimeError("turn meta missing field: %s" % field)

        prior = [e for e in journal_entries()
                 if e.get("turn_id") == meta["turn_id"] and e.get("event") == "reserved"]
        if prior:
            raise RuntimeError("turn %s already reserved; retry with publish" % meta["turn_id"])

        check_dirty_allowed()

        parent = git_head()
        items = artifact_manifest()
        verify_staged_blobs(items)

        manifest = {
            "schema": "turn_manifest-1.0",
            "protocol_version": 2,
            "session_id": meta["session_id"],
            "turn_id": meta["turn_id"],
            "sequence": meta["sequence"],
            "checkpoint_nonce": meta["checkpoint_nonce"],
            "mode": meta["mode"],
            "step": meta["step"],
            "phase": meta["phase"],
            "next_step": meta["next_step"],
            "terminal_line_class": meta["terminal_line_class"],
            "terminal_line": meta["terminal_line"],
            "parent_commit": parent,
            "prompt_sha256": meta["prompt_sha256"],
            "conversation_binding": meta.get("conversation_binding", {
                "id": None, "source": "local-generated", "observed_from_host": False}),
            "host_message_ids": {"observed": False, "value": None},
            "tool_call_counts": meta.get("tool_call_counts", {}),
            "wrap_checks": meta.get("wrap_checks", {}),
            "artifact_manifest": items,
            "created_at": meta["created_at"],
        }
        with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, indent=2, sort_keys=True)
            fh.write("\n")

        sys.path.insert(0, os.path.join(REPO_ROOT, "tools"))
        import protocol
        protocol.check_manifest(MANIFEST_PATH)

        manifest_sha = hashlib.sha256(open(MANIFEST_PATH, "rb").read()).hexdigest()
        journal_append({
            "event": "reserved",
            "turn_id": meta["turn_id"],
            "sequence": meta["sequence"],
            "checkpoint_nonce": meta["checkpoint_nonce"],
            "session_id": meta["session_id"],
            "parent_commit": parent,
            "manifest_sha256": manifest_sha,
        })

        sh(["git", "add", "logs/turn_manifest.json"])
        sh(["git", "commit", "-m",
            "checkpoint: %s seq=%s step=%s" % (meta["turn_id"], meta["sequence"], meta["step"])])
        commit = git_head()
        journal_append({
            "event": "committed",
            "turn_id": meta["turn_id"],
            "checkpoint_nonce": meta["checkpoint_nonce"],
            "commit": commit,
            "parent_commit": parent,
            "manifest_sha256": manifest_sha,
        })
        sh(["git", "update-ref", "refs/omega/turns/%s" % meta["turn_id"], commit])
        print(json.dumps({"status": "prepared", "turn_id": meta["turn_id"],
                          "commit": commit, "parent": parent,
                          "manifest_sha256": manifest_sha,
                          "artifacts": len(items)}, indent=2))
    finally:
        lock.close()


def publish(turn_id):
    lock = acquire_lock()
    try:
        entries = [e for e in journal_entries()
                   if e.get("turn_id") == turn_id and e.get("event") == "committed"]
        if not entries:
            raise RuntimeError("no committed journal entry for %s" % turn_id)
        entry = entries[-1]
        head = git_head()
        if head != entry["commit"]:
            raise RuntimeError("HEAD %s diverged from journaled commit %s; reconcile explicitly"
                               % (head, entry["commit"]))
        branch = sh(["git", "rev-parse", "--abbrev-ref", "HEAD"]).stdout.strip()
        if branch != BRANCH:
            raise RuntimeError("on branch %s, expected %s" % (branch, BRANCH))
        sh(["git", "push", "origin", "HEAD:%s" % BRANCH], check=True, capture=True)
        remote = sh(["git", "ls-remote", "origin", "refs/heads/%s" % BRANCH]).stdout.split()
        if not remote:
            raise RuntimeError("remote branch missing after push")
        remote_sha = remote[0]
        if remote_sha != entry["commit"]:
            raise RuntimeError("remote branch at %s, expected %s" % (remote_sha, entry["commit"]))
        os.makedirs(RECEIPT_DIR, exist_ok=True)
        receipt = {
            "turn_id": turn_id,
            "checkpoint_nonce": entry["checkpoint_nonce"],
            "commit": entry["commit"],
            "parent_commit": entry["parent_commit"],
            "remote": "origin",
            "branch": BRANCH,
            "remote_ref": "refs/heads/%s" % BRANCH,
            "remote_sha_observed": remote_sha,
            "verified_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "method": "git push + git ls-remote byte-identity check",
            "scope_note": "hash proves byte identity at the verified repository endpoint only",
        }
        receipt_path = os.path.join(RECEIPT_DIR, "%s.json" % turn_id)
        with open(receipt_path, "w", encoding="utf-8") as fh:
            json.dump(receipt, fh, indent=2, sort_keys=True)
            fh.write("\n")
        journal_append({"event": "published", "turn_id": turn_id,
                        "commit": entry["commit"], "remote_sha": remote_sha,
                        "receipt": os.path.relpath(receipt_path, REPO_ROOT)})
        print(json.dumps({"status": "published", "receipt": os.path.relpath(receipt_path, REPO_ROOT),
                          "remote_sha": remote_sha}, indent=2))
    finally:
        lock.close()


def main(argv):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("prepare")
    p1.add_argument("--meta", required=True)
    p2 = sub.add_parser("publish")
    p2.add_argument("--turn-id", required=True)
    args = ap.parse_args(argv[1:])
    if args.cmd == "prepare":
        prepare(args.meta)
    else:
        publish(args.turn_id)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as exc:  # noqa: BLE001 — CLI boundary
        print("FAIL: %s" % exc, file=sys.stderr)
        sys.exit(1)
