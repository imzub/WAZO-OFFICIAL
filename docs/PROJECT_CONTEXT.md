# WAZO Official Website Context

The WAZO-OFFICIAL repository is the public marketing and support website for WAZO. It is separate from the private WAZO application source repository.

## Current synchronization checkpoint - 2026-08-11

- Website `Master` contains the refreshed v2 installer; publication commit and
  Pages verification are recorded below.
- The refreshed v2.0.0.0 testing installer is sourced from private WAZO
  `Dev/QA` commit `c990cc3`: 99,434,227 bytes, SHA-256
  `F2C4808064438E863E1FD065BDA1CDD8D016332C981484E16FCEF5F5E5078130`.
  Local installer hash and payload verification passed before publication.
  Stable v1.1.7 remains unchanged and the Store AppX remains local-only.

## Publishing

- GitHub Pages URL: `https://imzub.github.io/WAZO-OFFICIAL/`
- Microsoft Store product ID: `9NKLT8DKJ1QX`; the public Store button uses `ms-windows-store://pdp/?productid=9NKLT8DKJ1QX`. Listing availability remains unverified.
- Publish source: `docs/`
- Keep `.nojekyll` in `docs/` so GitHub Pages serves static assets directly.

## Content Goals

- Explain what WAZO does.
- Present the current WAZO `v1.1.7` Windows direct installer while retaining the v1.1.6 product tour as explicitly versioned historical media.
- Help users understand the app workflow.
- Provide version-aware download areas.
- Position Microsoft Store as the recommended public install channel using the supplied deep link; do not claim listing availability until it is independently verified.
- Host public Windows installer downloads in versioned folders under `docs/site-data/releases/` with version, size, notes, and SHA-256 hashes.
- Explain that direct `.exe` installers may trigger SmartScreen/Chrome warnings until they are code-signed and gain reputation.
- Provide support paths for bugs, issues, feature requests, and queries.
- The downloads section keeps two stable/public cards: the recommended Microsoft Store channel and the v1.1.7 stable direct installer. An explicitly approved testing build may appear as a separate clearly labeled third card without changing the stable cards. Older releases and the major baseline remain repository history, not current download cards.
- Showcase privacy, protected local storage, multiple currencies, reports, backups, reversible records, local guidance, and the optional zakat module. For v1.1.7, describe app-managed Windows records and encrypted Import Studio drafts as authenticated encrypted envelopes protected by a Windows-bound key rather than plaintext local JSON.
- Keep the downloads section visually light: one short warning panel, two stable/public cards, an optional testing card, and concise version metadata.
- Add beginner-friendly FAQ items for initial setup, freeware, offline mode, backups, and core workflows whenever the site is updated.

## Portable cross-system continuation

- Repository state must be recoverable without a particular AI account, browser session, local path, or hidden conversation. The durable handoff is this file plus `AGENTS.md`, `docs/WAZO_CODEX_HANDOFF_POINTER.md`, `project-data/context/CURRENT_STATE.md`, and each release's `release.json`.
- A new system should authenticate independently, verify `origin`, check out `Master`, and validate the exact release manifest before changing website files. Never copy credentials, real financial data, browser profiles, or private application source into this repository.
- The private application repository remains authoritative for product implementation context; the website records only public-safe release state, exact source commit references, artifact hashes, deployment IDs, and explicit external gates.

## Current Public Downloads

- Current direct installer: `v1.1.7` / `docs/site-data/releases/v1.1.7/installer/WAZO-Setup-1.1.7.exe`.
- Optional testing installer: `v2.0.0` / `docs/site-data/releases/v2.0.0/installer/WAZO-Setup-2.0.0.exe`; status `testing`, stable public release remains `v1.1.7`.
- The refreshed v2.0.0 testing installer is 99,434,227 bytes with SHA-256 `F2C4808064438E863E1FD065BDA1CDD8D016332C981484E16FCEF5F5E5078130`, sourced from WAZO `Dev/QA` commit `c990cc3`. Current source evidence is 1,661/1,661 tests, 100,000/460,000 deep-audit probes/assertions, 496/496 full UI Humanity cases with zero severe contrast findings, 21/21 runtime workflows, 1,000/1,000 scenarios, and 7/7 package-compatibility cases. Installer payload verification and 12/12 isolated startup journeys pass; v1.1.7 remains stable.
- The stable v1.1.7 installer is 103,200,128 bytes with SHA-256 `489D6775D55E5F3FC7965C357263B5BA452B6BE073DE60CC8B9EC33AF31EF5F5`, sourced from WAZO `Dev/QA` commit `c13bbb973c8866876f527685e52d1875b1de2ad7`; its release manifest records Pages deployment `30905719455` and live verification on `2026-08-04T11:41:14Z`.
- Website commit `5db6957ae8e7d91a060db0fee2f37cbc5e4f807e` deployed successfully through GitHub Pages run `30125432522`. Cache-busted verification at `2026-07-24T20:53:53Z` returned HTTP 200 and exact expected hashes for the installer, video, captions, poster, thumbnail, transcript, and manual. Live desktop and 390 x 844 responsive checks had no browser-console errors; the 1920 x 1080 video decoded with one caption track.
- The previous same-version v1.1.6 installer remains historical deployment evidence: 102,427,430 bytes, SHA-256 `E641AB23BBFBC49A15E37C78EB62515E195D68C54815D6B1FFE533D50DC3E077`, source commit `68562c0af607f5c73bd1b948beb95f5517243523`, website artifact commit `41b359e4e306dacb090da69b82e2e3de1eab2e7b`, and successful Pages run `30037802828`.
- Final corrective-source validation passed syntax for 78 files, static analysis, brand and Trust Center checks, `726/726` tests, package matrices `54/54`, native-current-display matrices `9/9` at DPR `1.5`, UI-humanity `166/166`, and runtime workflows `14/14`. This remains automated evidence (`humanValidated=false`); physical packaged human validation is not recorded.
- The superseded published v1.1.5 installer remains historical evidence: 102,285,721 bytes, SHA-256 `94EF7F7C3456FE025689A44C228E4D8759F2AD153C12AD22B0ED81CC328D86AB`, product source commit `0f03c6084ab023cd14841158bd369461163ac319`, and website publication commit `94f6cff4868814ee3bc0fd40903e025a72c6331c`.
- The rejected v1.1.5 predecessor also remains historical evidence: 102,284,642 bytes, SHA-256 `955F00602E1FE632F5F429963E396A535359907D80520A45C7DE9B23AC09A13E`, product source commit `232210ba29904c9f3badf54d0650edc6c721a1b1`, and website publication commit `1630edadb907cce834886ded65b7190ecbe6205a`.
- The 16-page v1.1.6 manual remains historical website evidence; the v1.1.7 public website scope is intentionally installer-only.
- Authenticode status is `NotSigned`, so keep the direct-installer warning visible and never claim code signing.
- The major baseline installer and other older binaries remain archived in the repository but are intentionally not shown in the Downloads section.
- Older installers retained for rollback/testing: `v1.0.1`, `v1.0.2`, and `v1.0.4`.
- Keep older installers available unless Zubair explicitly asks to remove them.
- The Store card is linked through the Windows Store deep link but remains availability-unverified. The v1.1.7 direct installer is the current usable public download; it remains unsigned and separate from the local-only Store AppX candidate.

## Versioned Website Data

- Shared branding lives in `docs/site-data/shared/branding/`.
- Release data lives in `docs/site-data/releases/v<version>/`.
- Each release keeps a machine-readable `release.json` and human-readable notes under `updates/`.
- Release-specific product graphics live under that release's `images/` folder.
- Release-specific public video assets live under that release's optional `video/` folder with a machine-readable manifest, web MP4, poster, captions, and transcript.
- Installer binaries live under that release's `installer/` folder.
- `docs/site-data/releases/index.json` records the current installer, Store deep link, and archived versions; the major baseline is retained in history rather than surfaced as a current card.
- Archived installers remain tracked in GitHub for GitHub Pages and rollback use. This working clone may omit their binary files through Git sparse checkout; their manifests and notes remain local.
- WAZO does not currently integrate Electron's automatic updater. Do not publish `latest.yml`, blockmaps, or other auto-update-feed metadata for v1.1.7; website delivery is the direct installer link only.

## Public Safety

- Do not link to the private WAZO source repo.
- Do not publish real user financial data.
- Use only public-safe screenshots, generated visuals, or anonymized demo data.

## Current Product Tour

- The home page includes a narrated product tour at `#tour`, placed before the release-specific v1.1.6 changes.
- The featured interface recording is WAZO `v1.1.6`, built from private application commit `56399c120c644c1d80485b368370e630c58f6ac7`.
- The tour is 58.17 seconds at 1920 x 1080, with English narration, original music, default English WebVTT captions, anonymous demo data, a poster, a thumbnail, and a complete transcript.
- Public delivery files are under `docs/site-data/releases/v1.1.6/video/`. The 24,372,012-byte Pages MP4 has SHA-256 `6B79ED9EC177C0182AD7FF44641EEDE55898A9D228F0A921ED796C853E3F1533` and must remain ordinary Git content.
- The browser MP4 was derived from the validated 364,239,785-byte Store master with SHA-256 `3C0D867D007FF20607DDB7209A9EA9DFB78631C5959BC7B4992FDFAA50AD584F`, which remains preserved in the private WAZO release repository.
- The prior v1.1.4 narrated explainer and its complete editable workspace remain retained as historical media under their existing versioned folders; do not delete or overwrite them.
- Private WAZO application source and dependencies are intentionally excluded. Authorized reproduction requires a separate checkout of the recorded source commit.

## Stable Privacy Policy

- Public route: `https://imzub.github.io/WAZO-OFFICIAL/privacy/`, sourced from `docs/privacy/index.html`.
- Active revision: `WAZO-PP-1.1.7-2026-07-25`; effective date: `2026-07-25`; document SHA-256 `4D2E8F1076573679D5653BF63C12E3C08752EA7F261E2E820FD92A5E6F232DEA`.
- Canonical bundled-policy SHA-256: `0f792e634eec910e6c248575a2497301544ce8e85b9bd45a16827b2ec7a43150`.
- This policy applies to the live WAZO `1.1.7` Windows release and the WAZO Official website. The policy page, installer, release manifest, and release index are synchronized as the current v1.1.7 public release; the v1.1.6 tour remains historical media.
- The R2 policy records the permanent offline-only product boundary: no WAZO cloud portfolio service, synchronization, market-data or financial API, cloud AI, telemetry, advertising request, or background portfolio upload. User-selected website, Store, LinkedIn, policy, and email links are explicit handoffs to external applications and do not attach the local portfolio.
- Policy publication commit `02b985126843180a6f68e3fac1aa1469642405bc` deployed successfully through GitHub Pages run `30020443537`. Cache-busted verification at `2026-07-23T15:27:22Z` returned HTTP 200 for both policy and manifest; the public policy was byte-identical to `docs/privacy/index.html` (28,953 bytes, SHA-256 `1DDE5582371B480965B5FEC219492D3D1AE494DB94883A20C9CA164C11EBC3E9`), and the public manifest was byte-identical to its repository source.
- `docs/privacy/policy-manifest.json` and the `wazo-policy-*` metadata in the policy HTML must retain the same revision, effective date, URL, and canonical hash as the exact UTF-8/LF `docs/PRIVACY_POLICY.md` bundled by the matching WAZO release.
- Any substantive privacy-policy edit requires a new reviewed revision and synchronized app, website, manifest, Help/About, manual, and Store-listing metadata. Do not silently edit one copy.

## Change Rule

Update `AGENTS.md` or this context file when future website work changes publishing source, support flow, release/download strategy, or core product positioning.

## Current Website Presentation

- Product graphics for the `v1.1.6` experience live in `docs/site-data/releases/v1.1.6/images/`; the current website uses five release-specific graphics plus the shared Organized W logo.
- Public branding uses `docs/site-data/shared/branding/wazo-logo-organized-w-r2.png`. Logo correction commit `ab4a65f06656940f3da92b02d0a9e2cc182dd769` deployed successfully through GitHub Pages run `30062852367`; the live homepage and privacy page each return HTTP 200 and reference the current logo.
- The public feature story highlights ten-step scroll-safe setup, explicit privacy acknowledgement, permanently offline operation, Windows-bound protected storage, reversible records, configurable financial years, local guidance, password-optional `.wz` backups, Asset Library, investments, goals, reports, and optional Zakat.
- Current-installer confidence messaging may cite only confirmed evidence: syntax for 78 files, static analysis, brand and Trust Center checks, `726/726` source tests, `54/54` exact-package matrix checks, `9/9` native-current-display scenarios, `166/166` UI-humanity checks, and `14/14` runtime workflows passed, with `humanValidated=false`. Publication must be confirmed separately and must not be presented as physical human validation.
- Existing-user messaging must explain the one-time current-policy review, that exiting before acknowledgement leaves supported existing data unchanged, and that successful v1.1.5-to-v1.1.6 upgrade preserves supported data without re-entry.
- Windows protection claims apply only to the Windows desktop release. Do not imply Android protection parity.

## Cross-System Handoff And Media Preservation

The private WAZO application repository owns the canonical living Codex handoff at `docs/WAZO_CODEX_CONVERSATION_HANDOFF.md`. This public repository keeps a sanitized pointer in `docs/WAZO_CODEX_HANDOFF_POINTER.md` and updates it after substantive website scope, media, release, deployment, repository-state, or external-gate changes.

Historical v1.1.4 original Store-promo production media previously found only in `G:\iZ\WAZO-PROMO` is preserved under `project-data/releases/v1.1.4/promo/store-original/`. Master/review video and original WAV use Git LFS; source script, storyboard, manifest, captions, thumbnails, frames, and Store screenshots remain versioned alongside them. The workspace contains anonymous demo content.

Private application source, credentials, browser/session profiles, real financial data, and task feedback screenshots must never enter this public repository. Reproducible toolchains, dependency caches, pycache, and duplicate source-app checkouts remain excluded.
