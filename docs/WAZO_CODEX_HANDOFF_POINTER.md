# WAZO Cross-System Handoff Pointer

Last updated: 2026-08-06

The canonical complete substantive WAZO/Codex handoff is stored in the private application repository:

```text
Repository: https://github.com/imzub/WAZO.git
Branch: `codex/v1.1.9-deep-audit` for the latest synchronized work; `Dev/QA` is the product baseline.
File: docs/WAZO_CODEX_CONVERSATION_HANDOFF.md
```

This public website repository is:

```text
Repository: https://github.com/imzub/WAZO-OFFICIAL.git
Branch: Master
Codex website task: 019f7ed2-a4e9-79b0-8dda-15c0773061fa
```

Read this repository’s `AGENTS.md` and `docs/PROJECT_CONTEXT.md` before website work. Use `imzub` and Firefox for WAZO authentication.

## Current Website State

- GitHub Pages publishes from `docs/`.
- Current stable website installer line is v1.1.7; the v1.1.6 product tour remains explicitly versioned historical media.
- An optional v1.1.9 deep-audit testing installer is listed separately and does not replace or relabel v1.1.7. The synchronized candidate is 103,209,860 bytes / SHA-256 `D8097C2BC4CDCF63B80E5A2FCA6F9A79593AFE1ED8A45D371FB81A6A82F0AA01`, from WAZO `codex/v1.1.9-deep-audit` commit `d6533f1` based on `Dev/QA`; its packaged payload passed local readiness verification and its live bytes matched at website commit `f976331ac0b0047eea4176c8b8c5047e18528dd5` / Pages deployment `31074581797` at `2026-08-06T05:37:21Z`. v1.1.8 remains historical testing evidence.
- The website publication scope includes the v1.1.7 stable installer and the explicitly labeled v1.1.9 testing installer; the v1.1.9 Store AppX remains local for user testing.
- The Microsoft Store button uses `ms-windows-store://pdp/?productid=9NKLT8DKJ1QX`; listing availability remains unverified. The current installer candidate is 103,200,128 bytes / SHA-256 `489D6775D55E5F3FC7965C357263B5BA452B6BE073DE60CC8B9EC33AF31EF5F5`, from WAZO `Dev/QA` commit `c13bbb973c8866876f527685e52d1875b1de2ad7`; Pages deployment and live byte/hash verification are pending.
- Do not claim v1.1.7 Store upload, certification, or publication without direct evidence.
- Public browser media under `docs/` remains ordinary Git content.
- Large editable production video/audio under `project-data/` uses Git LFS.
- Never publish private application source, real financial records, credentials, browser/session data, or user-specific task screenshots.

## Preserved Original Promo

The previously local-only original/silent v1.1.4 Store-promo workspace is retained at:

```text
project-data/releases/v1.1.4/promo/store-original/
```

It includes master/review MP4s, original WAV, captions, storyboard, manifest, source script, audio analysis, thumbnail, frames, eight Store screenshots, and a hash manifest. These assets use anonymous/demo content; production MP4/WAV bytes are LFS-backed.

Update this pointer whenever substantive website scope, assets, public release, deployment, repository state, or an external gate changes. The application handoff remains authoritative for the combined project history.

## Account-independent resume rules

- The repositories and their tracked context files are the source of truth; do not depend on this Codex thread, a saved Firefox profile, a particular account, or local-only task memory.
- On a new system, independently authenticate as an authorized collaborator, verify `origin`, check out the recorded branch, and read both repositories' `AGENTS.md`, `docs/PROJECT_CONTEXT.md`, and current release manifests before changing files.
- Never persist credentials, browser/session data, real financial data, private application source, or generated temporary profiles in either repository. Record exact commits, hashes, deployment IDs, and pending external gates instead.
