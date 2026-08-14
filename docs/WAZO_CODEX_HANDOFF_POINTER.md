# WAZO Cross-System Handoff Pointer

## Current synchronization checkpoint - 2026-08-14

- Private application source: `Dev/QA` commit `42a0477` (latest synchronized
  context/documentation state; the stable installer artifact provenance is
  source commit `28b0522`).
- WAZO v2.0.0 stable installer: 99,450,391 bytes, SHA-256
  `31F44DAF38D26CDB69A42AFFE46FE473060CA239262871FA7B5A6F4BB9E44FE4`.
- Automated evidence: root 1,675/1,675, Import Studio 46/46, focused 536/536,
  packaged startup 18/18, ultra-scale 8/8, and deep audit 100,000 probes /
  460,000 assertions. Stable website commit
  `2a7a67f4c9f3071a4635aa4ea558a0538f27ec24`; latest Store-availability
  synchronization commit `ade2795`
  deployed through Pages deployment `5886802524`; public HTTP 200, exact size,
  and exact hash were verified at `2026-08-13T11:11:41Z`.
- v2.0.0 is the current stable website release. The v1.1.7 current release
  card and folder were removed from the website tree. Microsoft Store
  Submission 5 is published and available with
  `WAZO-Store-2.0.0-x64.appx` v2.0.0.0 for X64 Windows.Desktop devices;
  Android is archived/out of scope.

Last updated: 2026-08-14

The canonical complete substantive WAZO/Codex handoff is stored in the private application repository:

```text
Repository: https://github.com/imzub/WAZO.git
Branch: `Dev/QA` at source commit `42a0477` for the latest synchronized work;
the v2.0.0 installer artifact remains reproducible from `28b0522`; older audit
branches are historical lineage only.
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
- Current stable website installer line is v2.0.0; the v1.1.6 product tour remains explicitly versioned historical media.
- The v2.0.0 stable installer is 99,450,391 bytes / SHA-256 `31F44DAF38D26CDB69A42AFFE46FE473060CA239262871FA7B5A6F4BB9E44FE4`, from WAZO `Dev/QA` commit `28b0522`. Installer payload verification and 18/18 isolated startup journeys pass; public HTTP/size/hash verification is recorded in the current checkpoint above.
- The website publication scope includes the v2.0.0 stable installer and approved v2 promo media. The v2.0.0 Store package is published through Submission 5 and available on Microsoft Store.
- The former v1.1.7 release record below is historical only and must not be
  presented as a current website download or Store submission.
- The Microsoft Store button uses `ms-windows-store://pdp/?productid=9NKLT8DKJ1QX`; browser fallback is `https://apps.microsoft.com/detail/9NKLT8DKJ1QX`.
- Partner Center direct evidence verifies the latest product is available on Store and Submission 5 contains the v2.0.0.0 X64 package.
- The WAZO v2.0 LinkedIn article and article-share post are drafted and saved
  but intentionally unpublished. The article includes the approved cover
  video and three captioned WAZO visuals.
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
