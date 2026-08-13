# WAZO-OFFICIAL Website Agent Guide

## Current synchronization checkpoint - 2026-08-13

- The optional v2.0.0 testing installer has been replaced locally with the
  verified artifact from WAZO `Dev/QA` source commit `3e92050`: 99,450,391
  bytes, SHA-256
  `94CE4DD7C73739468A7525BEC8747BA5060DB74CFC626C5E589A5F260B4AA77E`.
  Website publication and public HTTP/hash verification are pending this
  synchronization; do not mark it live until Pages serves the exact file.
- Source evidence for this candidate is 1,675/1,675 root tests, 536/536
  focused hardening tests, and an 8/8 ultra-scale run covering 10 profiles,
  150 members, 50,000 assets, 5,000 definitions, 400 periods, and 10 repeated
  imports. v1.1.7 remains stable and unchanged.
- The Store AppX is prepared locally for Store submission and is not published
  to this website. Android remains archived/out of scope.

## Current synchronization checkpoint - 2026-08-11

- The approved premium v2 screen-led product tour is live in website media
  commit `8f8a27c` and Pages deployment `31497574428`. It is 166.467 seconds,
  1920x1080, English narrated/captioned, and its MP4 is 8,278,367 bytes with
  SHA-256 `6D37BD32A456D27657366A5F602632DC5AC5252C1A36EE5D1E3B2FEB6F9B4DCE`.
  Public HTTP 200 and exact hashes were verified at `2026-08-11T13:45:29Z`.
  The homepage features it; the earlier short v2 promo and historical v1.1.6
  tour remain retained.
- The premium media is sourced from private WAZO `Dev/QA` commit
  `c821aab73f865081603786944ad62a9bcde1c858`. Only public-safe synthetic Demo
  media and exact reproducibility metadata are present here; no user data,
  credentials, browser state, or private application source was copied.

- Website checkout is `Master`; the refreshed v2 installer replacement is
  published in website commit `b4da2ae` after local hash and payload
  verification. GitHub Pages deployment `31465805369` completed successfully;
  public HTTP 200/size/hash verification passed at `2026-08-11T06:41:05Z`.
- The v2.0.0.0 testing installer replacement is sourced from private WAZO
  `Dev/QA` commit `c990cc3`: 99,434,227 bytes, SHA-256
  `F2C4808064438E863E1FD065BDA1CDD8D016332C981484E16FCEF5F5E5078130`.
  GitHub Pages live verification follows publication.
- Stable v1.1.7 remains unchanged. The Store AppX is local-only, the Store
  listing is not independently verified, and Android is out of scope.

This repository hosts the public WAZO product website through GitHub Pages.

## Purpose

- Showcase WAZO as a private personal wealth organizer.
- Explain app features, workflows, downloads, support, and release notes.
- Help users understand the app without exposing the private application source code.

## Repository Rules

- For all WAZO GitHub authentication and repository operations, always select and use the `imzub` account without asking the user to make the account choice.
- GitHub Pages publishes from `docs/`.
- Keep public website content in `docs/`.
- Keep the stable public privacy policy at `docs/privacy/index.html`, published as `/privacy/`.
- Store website-managed data under `docs/site-data/`.
- Keep shared brand files in `docs/site-data/shared/`.
- Store every release under `docs/site-data/releases/v<version>/` with `release.json`, `updates/`, and optional `images/` and `installer/` folders.
- Store public product-tour delivery assets in the matching release's optional `video/` folder. Keep its manifest, captions, transcript, poster, and web MP4 together.
- Store public-safe editable media sources and continuation notes under `project-data/releases/v<version>/`; never place production-only material under `docs/`.
- Large production media under `project-data/` may use Git LFS. The actual MP4 served by GitHub Pages must remain ordinary Git content, because Pages cannot serve an LFS pointer as playable media.
- Public installer downloads are stored in the matching version's `installer/` folder and linked from the Downloads section.
- Keep older releases and installers tracked in the GitHub repository. The local clone may use sparse checkout to omit archived installer binaries while keeping their metadata and release notes locally.
- Do not remove an older release artifact from GitHub unless Zubair explicitly asks for its deletion.
- Microsoft Store is the recommended install path through `ms-windows-store://pdp/?productid=9NKLT8DKJ1QX`; the website link is present but listing availability is not independently live-verified. The direct `.exe` installer remains the current website download channel.
- Do not recreate or use the old `Site/` folder.
- Do not link to the private WAZO source repository.
- Do not copy private WAZO application source, dependencies, credentials, browser sessions, or user data into this public repository. Record only the exact private source commit required for authorized reproduction.
- The website may link to LinkedIn, support email, public release files, and public documentation.

## Portable cross-system continuation

- Treat repository files as the durable source of truth; never depend on a particular Codex account, browser profile, saved GitHub session, local path, or hidden task memory.
- On a new system or with a new AI/tool, read this file, `docs/PROJECT_CONTEXT.md`, `docs/WAZO_CODEX_HANDOFF_POINTER.md`, `project-data/context/CURRENT_STATE.md`, and the matching `docs/site-data/releases/v<version>/release.json` before editing.
- Re-verify `origin` and the active branch, fetch the named source repositories, and use the exact source commit, artifact size, and SHA-256 recorded in the release manifest. Authentication is an environment prerequisite, not project state; never store tokens or session data in context.
- Keep `Master` as the website publishing branch, preserve v1.1.7 as stable, and label v2.0.0 as testing until a separately recorded publication and live byte/hash verification exists. Retain v1.1.9 as historical testing evidence.

## Product Messaging

- WAZO is a Windows desktop personal wealth organizer.
- WAZO `1.1.6` and later are permanently offline-only: no cloud portfolio service or synchronization, market-data or financial API, cloud AI, telemetry, advertising request, or background portfolio upload. Prices and rates are user-maintained locally. Explicit website, Store, LinkedIn, policy, and email links are user-initiated handoffs and never attach the local portfolio.
- The current public installer is WAZO `1.1.7`. It protects app-managed Windows data as authenticated encrypted envelopes; do not describe those active records as plaintext JSON.
- It supports family/profile setup, members, assets, allocation targets, financial goals, reports, backups, privacy mode, themes, multiple currencies, and optional zakat planning.
- Zakat is optional. The website should not position WAZO as only a zakat app.
- Source code is private.

## Website Maintenance Rules

- Update this context file when website structure, public messaging, download/release process, support process, or GitHub Pages publishing rules change.
- The current website identity uses `docs/site-data/shared/branding/wazo-logo-organized-w-r2.png` (57,329 bytes, 256 x 256, SHA-256 `4F897AF777A8ADEB4782848E04F934B05D40F8F2A92979D75D75380E6BAC4B55`). Use this cache-busted asset for public header, footer, favicon, and Privacy Policy branding. Retain `wazo-logo.png` only as a legacy asset; do not restore it to current public pages.
- Keep the website privacy-policy revision, effective date, and substantive text synchronized with the reviewed offline policy bundled with the matching WAZO release. Do not publish protected-storage or Store-readiness claims before the corresponding release behavior is verified.
- `docs/privacy/policy-manifest.json` and the `wazo-policy-*` metadata in `docs/privacy/index.html` must match the authoritative UTF-8/LF bytes of the sibling WAZO repository's `docs/PRIVACY_POLICY.md`. This static site has no package/build validation runner, so before publication deterministically verify: the canonical file has no UTF-8 BOM or CR bytes; `Get-FileHash -Algorithm SHA256` matches both website hash fields; revision, effective date, and canonical URL match; and the twelve numbered policy sections plus the local-processing summary are substantively present in both copies.
- Update `docs/site-data/releases/index.json`, the version's `release.json`, and its release notes whenever release status, installer metadata, product graphics, or public update details change.
- When publishing or replacing a product tour, update its public `video.json`, the version `release.json`, the release index featured-video pointer, `docs/PROJECT_CONTEXT.md`, and the matching `project-data/context/` checkpoint together.
- Keep video recording versions explicit. The featured tour now shows the
  WAZO `v2.0.0` testing promo; the v1.1.6 narrated tour remains retained as
  historical media and must not be relabeled as current-version evidence.
- Keep the Downloads section's two stable/public channel cards: recommended Microsoft Store install and the v1.1.7 stable direct installer. When an explicitly approved testing build is published, add one clearly labeled Testing card without changing or removing the stable cards. Retain older releases and the major baseline in repository history, but do not surface them as current download cards.
- Keep SmartScreen/Chrome warning guidance visible near direct installer links until standalone installers are code-signed and have download reputation.
- Do not publish `latest.yml`, blockmaps, or other automatic-update metadata unless WAZO first ships and verifies a compatible automatic-update client and URL layout. WAZO v1.1.7 uses a direct installer link only.
- Current direct installer is WAZO `v1.1.7`, 103,200,128 bytes, SHA-256 `489D6775D55E5F3FC7965C357263B5BA452B6BE073DE60CC8B9EC33AF31EF5F5`, from WAZO `Dev/QA` source commit `c13bbb973c8866876f527685e52d1875b1de2ad7`; the website release manifest records Pages deployment `30905719455` and live verification on `2026-08-04T11:41:14Z`. The Store AppX was generated and tested locally and is not a website artifact. Physical human workflow validation is not recorded.
- The current optional testing installer is WAZO `v2.0.0` / build `2.0.0.0`, 99,434,227 bytes, SHA-256 `F2C4808064438E863E1FD065BDA1CDD8D016332C981484E16FCEF5F5E5078130`, from WAZO `Dev/QA` source commit `c990cc3`. Source evidence is 1,661/1,661 tests, 100,000/460,000 deep-audit probes/assertions, 496/496 full UI Humanity cases with zero severe contrast findings, 21/21 runtime workflows, 1,000/1,000 scenarios, and 7/7 package-compatibility cases. Packaged installer payload verification and 12/12 isolated startup journeys pass; v1.1.7 remains stable and the package is unsigned.
- Support actions should use email templates for bugs, feature requests, and queries.
- Use public-safe screenshots or app-style visuals only. Do not include personal financial data.

## Testing Checklist

- Open `docs/index.html` locally after UI changes.
- Confirm no private source-code links are present.
- Confirm GitHub Pages can publish from `docs/`.
- Confirm support email links open with useful templates.
- Confirm every local page, image, manual, release-note, and installer link resolves, and verify public installer size/hash against the current release manifest.
- Confirm product-tour playback uses the correct poster, unsqueezed 16:9 dimensions, native controls, English WebVTT captions, a transcript, and a byte-identical published MP4 hash.
- Confirm `git check-attr` marks production master/audio/capture frames as LFS while leaving the Pages MP4 as ordinary Git data.
- Confirm the `/privacy/` page, canonical URL, policy metadata, and sitemap entry are valid.
- Check desktop and mobile responsiveness.

## Cross-System Handoff And Media Preservation

- Never leave a unique WAZO website visual, photo, audio, video, caption, thumbnail, frame, or editable production asset only in a temporary/non-repository workspace. Preserve it under `project-data/releases/v<version>/`; large production video/audio uses Git LFS.
- Keep the public repository free of private application source, credentials, browser/session data, real financial records, and user-specific task screenshots.
- Keep `docs/WAZO_CODEX_HANDOFF_POINTER.md` synchronized with the private application repository’s living handoff and current website task/repository state after substantive website scope, asset, release, deployment, or external-gate changes.
