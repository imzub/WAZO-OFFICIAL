# WAZO-OFFICIAL Website Agent Guide

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
- Microsoft Store should be positioned as the recommended public install path once available. Keep the Store card unlinked and marked pending until the WAZO listing is published and verified; direct `.exe` installers are the current website channel for offline setup and controlled installation.
- Do not recreate or use the old `Site/` folder.
- Do not link to the private WAZO source repository.
- Do not copy private WAZO application source, dependencies, credentials, browser sessions, or user data into this public repository. Record only the exact private source commit required for authorized reproduction.
- The website may link to LinkedIn, support email, public release files, and public documentation.

## Product Messaging

- WAZO is a Windows desktop personal wealth organizer.
- WAZO `1.1.6` and later are permanently offline-only: no cloud portfolio service or synchronization, market-data or financial API, cloud AI, telemetry, advertising request, or background portfolio upload. Prices and rates are user-maintained locally. Explicit website, Store, LinkedIn, policy, and email links are user-initiated handoffs and never attach the local portfolio.
- The current public installer is WAZO `1.1.6`. It protects app-managed Windows data as authenticated encrypted envelopes; do not describe those active records as plaintext JSON.
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
- Keep video recording versions explicit. The featured tour now shows WAZO `v1.1.6`; the earlier v1.1.4 tour remains retained as historical media and must not be relabeled as current-version evidence.
- Keep download sections version-aware: recommended Microsoft Store install, latest published direct installer, and the major baseline installer, with release notes and known fixes.
- Keep SmartScreen/Chrome warning guidance visible near direct installer links until standalone installers are code-signed and have download reputation.
- Do not publish `latest.yml`, blockmaps, or other automatic-update metadata unless WAZO first ships and verifies a compatible automatic-update client and URL layout. WAZO v1.1.6 uses a direct installer link only.
- Current corrective direct installer is WAZO `v1.1.6`, 102,429,605 bytes, SHA-256 `A4BAB97F8D252FA95F586B98CB59BF123FE1F91C3BFA3CA52B7B6DCD807DE6F7`, from private product source commit `56399c120c644c1d80485b368370e630c58f6ac7`. Website commit `5db6957ae8e7d91a060db0fee2f37cbc5e4f807e` deployed through successful Pages run `30125432522`; cache-busted public verification passed at `2026-07-24T20:53:53Z`. The previously published v1.1.6 bytes (102,427,430 bytes, SHA-256 `E641AB23BBFBC49A15E37C78EB62515E195D68C54815D6B1FFE533D50DC3E077`) remain historical deployment evidence. Physical human workflow validation is not recorded, and publication must not be described as a human test pass. WAZO v1.1.5 is superseded historical evidence.
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
