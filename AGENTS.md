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
- Microsoft Store is the recommended install path through `ms-windows-store://pdp/?productid=9NKLT8DKJ1QX`; the website link is present but listing availability is not independently live-verified. The direct `.exe` installer remains the current website download channel.
- Do not recreate or use the old `Site/` folder.
- Do not link to the private WAZO source repository.
- Do not copy private WAZO application source, dependencies, credentials, browser sessions, or user data into this public repository. Record only the exact private source commit required for authorized reproduction.
- The website may link to LinkedIn, support email, public release files, and public documentation.

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
- Keep video recording versions explicit. The featured tour now shows WAZO `v1.1.6`; the earlier v1.1.4 tour remains retained as historical media and must not be relabeled as current-version evidence.
- Keep the Downloads section's two stable/public channel cards: recommended Microsoft Store install and the v1.1.7 stable direct installer. When an explicitly approved testing build is published, add one clearly labeled Testing card without changing or removing the stable cards. Retain older releases and the major baseline in repository history, but do not surface them as current download cards.
- Keep SmartScreen/Chrome warning guidance visible near direct installer links until standalone installers are code-signed and have download reputation.
- Do not publish `latest.yml`, blockmaps, or other automatic-update metadata unless WAZO first ships and verifies a compatible automatic-update client and URL layout. WAZO v1.1.7 uses a direct installer link only.
- Current direct installer candidate is WAZO `v1.1.7`, 103,200,128 bytes, SHA-256 `489D6775D55E5F3FC7965C357263B5BA452B6BE073DE60CC8B9EC33AF31EF5F5`, from WAZO `Dev/QA` source commit `c13bbb973c8866876f527685e52d1875b1de2ad7`. Source tests passed 889/889, focused financial/SIP/source/renderer 77/77, Demo seed/SIP 8/8, UI-humanity 198/198, packaged startup 12/12, and complete isolated runtime 19/19. The current website update is pending Pages deployment and live byte/hash verification. The Store AppX was generated and tested locally and is not a website artifact. Physical human workflow validation is not recorded, and publication must not be described as a human test pass. Earlier releases remain historical evidence.
- The optional testing installer is WAZO `v1.1.8`, 103,205,840 bytes, SHA-256 `BA99682DA105D0FC52EB6C371C43B7C960FC77417C58FC2700F963FDBD014850`, from WAZO audit-hardening commit `14c3a3d640c36c44e38e63de44ebc2eb4ca68b9a`. It remains labeled Testing; v1.1.7 remains the stable public installer. The v1.1.8 source evidence is 143/143 focused regression tests, 72/72 source/privacy/demo/import subset, Trust Foundation PASS, UI-humanity 198/198, static/syntax checks PASS, and corrected NSIS payload/installed-startup verification. The exact installer was live-verified at website commit `d1dfb61e07cbd77b97c8b0f5f46f05c3466766c8` through Pages deployment `30927906679` on `2026-08-04T16:16:26Z`; intermittent DevTools mouse-dispatch transport timeouts mean complete startup/runtime automation and physical human validation remain unclaimed. The Store AppX is local-only and is not a website artifact.
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
