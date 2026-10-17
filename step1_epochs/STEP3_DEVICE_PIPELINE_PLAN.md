# STEP 3 — DEVICE PIPELINE PLAN (DRAFT, not entered)

Status at time of writing (2026-10-17, turn 11): **STATE_3 is not entered.** Step 1 is still open and this sandbox has no device, no `adb`, no root and no network path to a phone. This document is the delivery *plan* required by `STATE_3_DEVICE_PIPELINE` ("delivery of state extraction scripts and risk assessments") so that when a device exists the work is a matter of consent and execution, not design under pressure. It commits to nothing that requires a device today.

## 1. Purpose and non-purpose
**Purpose:** keep a trustworthy record of the *user's* game state — build, division/points, squad, currency, season and event status — so coaching is computed from observed state rather than from memory of a conversation.
**Non-purpose:** it is not a cheat pipeline, not a data-mining route, and not a way to see anything the game does not show on screen. Every method below reads what the user could photograph.

## 2. Hard boundaries (each mapped to a verified claim)

| Boundary | Rule |
| --- | --- |
| No root, no unlocked bootloader, no Magisk/LSPosed, no Xposed | The only authorised builds are store builds (CLAIM-075); modifying the device to read app-private data is the "external software" class named in the sanctions article (CLAIM-075, CLAIM-043 §2.1.2) |
| No patched/modded APK, no repackaging, no signature tricks | Explicitly bannable (CLAIM-075) |
| No memory reading, no debugger attach, no hooking | Reverse engineering / derivation prohibited (CLAIM-043 §2.1.1) and would be indistinguishable from cheat tooling to FTG |
| No synthetic input into a live match (no `adb shell input` macro, no auto-play, no scripted farming) | Automation software and bots are prohibited (CLAIM-043 §2.1.2); DLL is human-vs-human by design (CLAIM-080) and fairness is explicitly protected (CLAIM-075) |
| No packet capture / MITM / proxy of game traffic | "Access only via the user interface provided by First Touch" (CLAIM-043 §2.1.3); and it would expose credentials |
| No editing of saves or profiles | Would be a progression-circumvention act (CLAIM-075) |
| No screen recording of opponents or public sharing of match footage that identifies another player | Fair-play and naming policy (CLAIM-075) plus ordinary privacy |

**Consequence of a boundary violation:** the user's account may be permanently lost, and the loss is not reversible by appeal unless FTG agrees the flag was wrong (CLAIM-075). A pipeline that risks that is worth less than no pipeline.

## 3. What the pipeline will actually do (three tiers of intrusiveness)

### Tier A — zero-permission capture (default, always available)
The user takes screenshots and drops them in `raw_game_data/`. A script renames them by capture time, records what surface each shows, and asks the user to confirm a short typed state block. No device connection at all.
- **Trust:** highest. Nothing to detect; nothing to break.
- **Cost:** user effort, ~2 minutes per session.

### Tier B — USB debugging, capture only
With the user's explicit consent per session, `adb` is used **only** for `screencap` and `shell dumpsys` of OS-level facts (battery, thermal, display refresh rate, build fingerprint). No input injection, no `pm`/`am` of the game, no file pull from app-private storage.
- **Why it is acceptable:** reading a screenshot the user could take by hand is not automating the game; it is automating the *file transfer*.
- **Caveat:** even this must be turned off outside capture sessions; a permanently connected debugger is a risk the user is not being asked to take for convenience.
- **Not yet available here:** no `adb` binary and no device in this sandbox.

### Tier C — user-initiated exports the OS already supports
Android's own backup/export or iOS Files app, only where the OS offers it without root. Treated as **raw input** (`RAW GAME DATA DIRECTORY`), never written back. If the export format is undocumented: read it, describe it, never modify it.

## 4. Scripts to deliver (written to run offline; none executed here)

| Script | Function | Status |
| --- | --- | --- |
| `scripts/state_capture.py` | Take a directory of screenshots, hash them, read EXIF/mtime, emit `raw_game_data/captures.jsonl` with a capture ID and a surface label the user supplies | planned; depends on Tier A only |
| `scripts/state_record.py` | Apply a typed state block (`build`, `division`, `season_points`, `coins`, `gems`, `squad_ovr`, `formation`, `pass_state`, `event`) to `user_profile.md` with a timestamp and a source-capture reference | planned; no device dependency |
| `scripts/state_diff.py` | Diff two state records, flag every changed field, mark staleness by age and by build change | planned |
| `scripts/adb_capture.sh` | **Tier B only:** loop of `adb exec-out screencap -p` with consent banner and a hard kill-switch | planned; requires `adb` + consent |
| `scripts/verify_no_mutation.sh` | Assert the pipeline never writes into `raw_game_data/` and never invokes `input`, `pm`, `am`, `monkey` | planned; runs in CI-style pre-commit |

Design rules: every script is read-only with respect to the game and the device; every script refuses to run if the build number differs from the epoch's reference build without an explicit override; every output records the capture time, the build, and the surface shown.

## 5. State schema (the minimum that makes coaching possible)

```
build           string   e.g. 13.430          (CLAIM-087/054)
platform        enum     android | ios
division        int 1-8  career division       (CLAIM-045/010)
season_points   int                            (CLAIM-071)
dll_tier        string   nullable              (CLAIM-081)
coins, gems     int                            (CLAIM-015/019)
squad_ovr       int      nullable until the OVR test resolves (CLAIM-104)
formation       string   must be checked against the season pool (CLAIM-077)
pass_state      enum     none | free | premium (CLAIM-040)
event_state     string   nullable              (CLAIM-016/063)
captured_at     ISO-8601 utc
witness         path     screenshot or typed block
```

Anything not shown on screen is `UNOBSERVABLE`, never inferred. A missing field is a gap, not a zero.

## 6. Risk assessment (what can go wrong, and the mitigation)

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| User follows Tier B and leaves USB debugging on with a rogue host | low | high | consent per session; revoke after capture; never ask for "always allow" |
| Pipeline is mistaken for cheat tooling (it never is, but appears so) | low | high | no input injection, no memory access, no patching; all code public in this repo |
| Screenshot metadata leaks personal data | medium | medium | strip EXIF GPS before commit; store only screen content |
| State drift between captures misleads coaching | high | medium | hard staleness rules: state older than 7 days or a different build is treated as unverified |
| Over-collection (capturing opponents' names) | medium | low | crop/redact opponent identifiers in stored images |
| Plan is mistaken for completed work | — | **high** | this file is marked DRAFT; no script has been executed; Step 3 remains unentered |

## 7. Preconditions before Step 3 can begin (all user-side)
1. Step 2 resolved (OBS-013) and Step 1 sealed — the sequence is binding.
2. A device the user owns and is willing to connect; platform + OS version recorded.
3. Explicit consent to one capture method (A, B or C).
4. Confirmation that the account is signed in with a provider the user controls (CLAIM-083 sign-out hazard).
5. Agreement that no match will be played differently because a capture is running (no scripting, no "just this one automation").

## 8. What this plan deliberately does not include
No save editing, no roster injection, no unlocked-everything tooling, no "safe" mod, no APK extraction, no packet tooling. Every one of those is prohibited by CLAIM-043/075 and would put the user's account — the asset the whole mission depends on — at risk for information the screen already shows.
