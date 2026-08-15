# WAZO Official Website Context

## 2026-08-15 v2.0.0 stable baseline and v2.0.1 update

- WAZO v2.0.0 / build 2.0.0.0 remains the stable baseline. WAZO v2.0.1 /
  build 2.0.1.0 is the latest bug-fix and enhancement update on that stable
  line. It is sourced from private WAZO `Dev/QA` commit
  `ced9761`; the refreshed installer is 99,453,603 bytes with SHA-256
  `AF00F8966E48B87CA876954B8D09863F383EA166F8C694D44772E76A2AA2E564`.
- Website publication and public HTTP/size/hash verification for this refreshed
  artifact are pending the GitHub Pages deployment. The v2.0.0 baseline remains
  live and byte-preserved.
- v2.0.0 remains the stable baseline with its original 99,450,391-byte hash.
  Microsoft Store remains published at v2.0.0.0; the v2.0.1 publication is a
  website direct-installer update only. Android remains archived/out of scope.

## Current synchronization checkpoint - 2026-08-14

- WAZO v2.0.0 is the stable public website release. The direct installer
  artifact was built from private WAZO `Dev/QA` commit `28b0522`; the current
  synchronized private source checkout is `Dev/QA` commit `42a0477`. The
  installer is 99,450,391 bytes with
  SHA-256 `31F44DAF38D26CDB69A42AFFE46FE473060CA239262871FA7B5A6F4BB9E44FE4`.
- Source evidence is 1,675/1,675 root tests, Import Studio 46/46, focused
  hardening 536/536, packaged startup 18/18, launch media 44/44, package
  compatibility 7/7, deep audit 100,000 probes / 460,000 assertions,
  scenario register 1,000/1,000, and 8/8 ultra-scale cases using 10 profiles,
  150 members, 50,000 assets, 5,000 definitions, 400 periods, and 10 repeated
  imports. Public HTTP/size/hash verification is recorded after Pages deploy.
- The former v1.1.7 current website release has been removed from current
  cards and release metadata. Microsoft Store Submission 5 is published and
  available; the local unsigned AppX is retained only as reproducibility
  evidence. Android work is archived and out of scope.
- The WAZO v2.0 LinkedIn article and article-share post are drafted and saved
  but unpublished. The article contains the cover video and three captioned
  visuals; do not claim social publication until the owner publishes it.

The WAZO-OFFICIAL repository is the public marketing and support website for WAZO. It is separate from the private WAZO application source repository.

## 2026-08-11 premium v2 screen-led promotion publication

- The homepage now features the approved WAZO v2.0.0 premium screen-led tour.
  It is 166.467 seconds, 1920x1080, H.264/AAC, professionally narrated in
  English, captioned, and built from isolated anonymous synthetic Demo screens.
- The source anchor is private WAZO `Dev/QA` commit
  `c821aab73f865081603786944ad62a9bcde1c858`. Website media commit `8f8a27c`
  deployed successfully through Pages deployment `31497574428`; public HTTP
  200 and exact hashes for the video and supporting files were verified at
  `2026-08-11T13:45:29Z`.
- Premium MP4: 8,278,367 bytes, SHA-256
  `6D37BD32A456D27657366A5F602632DC5AC5252C1A36EE5D1E3B2FEB6F9B4DCE`.
  The website manifest records the served LF-normalized caption and transcript
  hashes. The previous short v2 review cut and historical v1.1.6 narrated tour
  remain in the repository and are not deleted or overwritten.
- The v2.0.0 installer is the stable website build. Microsoft Store
  verification completed on 2026-08-14: Partner Center shows the latest
  product available on Store, with Submission 5 carrying
  `WAZO-Store-2.0.0-x64.appx` v2.0.0.0 for X64 Windows.Desktop devices. Android
  is archived, and no real user or financial data is present in public media.

## 2026-08-11 v2 promo media checkpoint

- A new v2.0.0 testing promo is staged under
  docs/site-data/releases/v2.0.0/video/ from private WAZO source commit
  4bf939b. It is a 52-second 1,920x1,080 H.264/AAC video with English
  captions, transcript, no-audio variant, poster, thumbnail, and machine-
  readable manifest.
- The MP4 is 7,196,381 bytes with SHA-256
  DC3ED9DE1BE546885F76D6E1B0C2C069A305A9AD3AB7F460EB91114CA6946BF6.
  Website artifact commit 26f6904 and Pages deployment 31484600128 are live;
  public HTTP 200 and exact MP4/poster hashes were verified at
  2026-08-11T11:02:17Z.
- The old v1.1.6 narrated tour remains in its historical release folder and is
  not deleted or overwritten. The promo uses synthetic Demo data only and is
  not professional financial, tax, Zakat, legal, or investment advice.

## Historical synchronization checkpoint - 2026-08-11

- Website `Master` contains the refreshed v2 installer; publication commit
  `b4da2ae` is recorded in the release manifest. Pages deployment
  `31465805369` completed successfully, and public HTTP 200/size/hash
  verification passed at `2026-08-11T06:41:05Z`.
- This section records the superseded v2 testing artifact from the prior
  publication cycle. It is retained as historical evidence only; the current
  stable package is recorded in the 2026-08-13 checkpoint above.

## Publishing

- GitHub Pages URL: `https://imzub.github.io/WAZO-OFFICIAL/`
- Microsoft Store product ID: `9NKLT8DKJ1QX`; the public Store button uses
  `ms-windows-store://pdp/?productid=9NKLT8DKJ1QX`, with browser fallback
  `https://apps.microsoft.com/detail/9NKLT8DKJ1QX`. The v2.0.0 listing is
  published and live-verified through Partner Center.
- Publish source: `docs/`
- Keep `.nojekyll` in `docs/` so GitHub Pages serves static assets directly.

## Content Goals

- Explain what WAZO does.
- Present the current WAZO `v2.0.0` Windows direct installer while retaining the v1.1.6 product tour as explicitly versioned historical media.
- Help users understand the app workflow.
- Provide version-aware download areas.
- Position Microsoft Store as the recommended public install channel using the
  supplied deep link and browser fallback. The v2.0.0 listing is now verified
  as published and available; preserve the direct installer as a fallback for
  regional or device-specific Store availability differences.
- Host public Windows installer downloads in versioned folders under `docs/site-data/releases/` with version, size, notes, and SHA-256 hashes.
- Explain that direct `.exe` installers may trigger SmartScreen/Chrome warnings until they are code-signed and gain reputation.
- Provide support paths for bugs, issues, feature requests, and queries.
- The downloads section keeps the Microsoft Store v2.0.0 stable baseline, the
  v2.0.0 baseline direct installer, and the latest v2.0.1 stable-line update.
  The removed v1.1.7 card and stale testing card must not return. Older
  releases remain repository history, not current download cards.
- Showcase privacy, protected local storage, multiple currencies, reports, backups, reversible records, local guidance, and the optional zakat module. For v2.0.0, describe app-managed Windows records and encrypted Import Studio drafts as authenticated encrypted envelopes protected by a Windows-bound key rather than plaintext local JSON.
- Keep the downloads section visually light: one short warning panel, two stable/public cards, an optional testing card, and concise version metadata.
- Add beginner-friendly FAQ items for initial setup, freeware, offline mode, backups, and core workflows whenever the site is updated.

## Portable cross-system continuation

- Repository state must be recoverable without a particular AI account, browser session, local path, or hidden conversation. The durable handoff is this file plus `AGENTS.md`, `docs/WAZO_CODEX_HANDOFF_POINTER.md`, `project-data/context/CURRENT_STATE.md`, and each release's `release.json`.
- A new system should authenticate independently, verify `origin`, check out `Master`, and validate the exact release manifest before changing website files. Never copy credentials, real financial data, browser profiles, or private application source into this repository.
- The private application repository remains authoritative for product implementation context; the website records only public-safe release state, exact source commit references, artifact hashes, deployment IDs, and explicit external gates.

## Current Public Downloads

- Current direct installer: `v2.0.0` / `docs/site-data/releases/v2.0.0/installer/WAZO-Setup-2.0.0-stable-20260813.exe`; status `stable`.
 - The prior v2 testing installer record is historical evidence only. The current
   stable installer is v2.0.0 and is recorded in the 2026-08-13 checkpoint.
- The prior v1.1.7 installer record is historical evidence only and is not a
  current website download.
- Website commit `5db6957ae8e7d91a060db0fee2f37cbc5e4f807e` deployed successfully through GitHub Pages run `30125432522`. Cache-busted verification at `2026-07-24T20:53:53Z` returned HTTP 200 and exact expected hashes for the installer, video, captions, poster, thumbnail, transcript, and manual. Live desktop and 390 x 844 responsive checks had no browser-console errors; the 1920 x 1080 video decoded with one caption track.
- The previous same-version v1.1.6 installer remains historical deployment evidence: 102,427,430 bytes, SHA-256 `E641AB23BBFBC49A15E37C78EB62515E195D68C54815D6B1FFE533D50DC3E077`, source commit `68562c0af607f5c73bd1b948beb95f5517243523`, website artifact commit `41b359e4e306dacb090da69b82e2e3de1eab2e7b`, and successful Pages run `30037802828`.
- Final corrective-source validation passed syntax for 78 files, static analysis, brand and Trust Center checks, `726/726` tests, package matrices `54/54`, native-current-display matrices `9/9` at DPR `1.5`, UI-humanity `166/166`, and runtime workflows `14/14`. This remains automated evidence (`humanValidated=false`); physical packaged human validation is not recorded.
- The superseded published v1.1.5 installer remains historical evidence: 102,285,721 bytes, SHA-256 `94EF7F7C3456FE025689A44C228E4D8759F2AD153C12AD22B0ED81CC328D86AB`, product source commit `0f03c6084ab023cd14841158bd369461163ac319`, and website publication commit `94f6cff4868814ee3bc0fd40903e025a72c6331c`.
- The rejected v1.1.5 predecessor also remains historical evidence: 102,284,642 bytes, SHA-256 `955F00602E1FE632F5F429963E396A535359907D80520A45C7DE9B23AC09A13E`, product source commit `232210ba29904c9f3badf54d0650edc6c721a1b1`, and website publication commit `1630edadb907cce834886ded65b7190ecbe6205a`.
- The 16-page v1.1.6 manual remains historical website evidence; the v2.0.0 public website scope is intentionally installer-only plus approved v2 promo media.
- Authenticode status is `NotSigned`, so keep the direct-installer warning visible and never claim code signing.
- The major baseline installer and other older binaries remain archived in the repository but are intentionally not shown in the Downloads section.
- Older installers retained for rollback/testing: `v1.0.1`, `v1.0.2`, and `v1.0.4`.
- Keep older installers available unless Zubair explicitly asks to remove them.
- The Store card is linked through the Windows Store deep link and browser
  listing URL. Microsoft Store v2.0.0 is published and available; the direct
  v2.0.0 installer remains a usable fallback and is unsigned.

## Versioned Website Data

- Shared branding lives in `docs/site-data/shared/branding/`.
- Release data lives in `docs/site-data/releases/v<version>/`.
- Each release keeps a machine-readable `release.json` and human-readable notes under `updates/`.
- Release-specific product graphics live under that release's `images/` folder.
- Release-specific public video assets live under that release's optional `video/` folder with a machine-readable manifest, web MP4, poster, captions, and transcript.
- Installer binaries live under that release's `installer/` folder.
- `docs/site-data/releases/index.json` records the current installer, Store deep link, and archived versions; the major baseline is retained in history rather than surfaced as a current card.
- Archived installers remain tracked in GitHub for GitHub Pages and rollback use. This working clone may omit their binary files through Git sparse checkout; their manifests and notes remain local.
- WAZO does not currently integrate Electron's automatic updater. Do not publish `latest.yml`, blockmaps, or other auto-update-feed metadata for v2.0.0; website delivery is the direct installer link only.

## Public Safety

- Do not link to the private WAZO source repo.
- Do not publish real user financial data.
- Use only public-safe screenshots, generated visuals, or anonymized demo data.

## Current Product Tour

- The home page features the v2.0.0 stable promo at `#tour`; the narrated
  v1.1.6 tour remains available at `#historical-tour` as versioned historical
  media.
- The featured interface recording is WAZO `v1.1.6`, built from private application commit `56399c120c644c1d80485b368370e630c58f6ac7`.
- The tour is 58.17 seconds at 1920 x 1080, with English narration, original music, default English WebVTT captions, anonymous demo data, a poster, a thumbnail, and a complete transcript.
- Public delivery files are under `docs/site-data/releases/v1.1.6/video/`. The 24,372,012-byte Pages MP4 has SHA-256 `6B79ED9EC177C0182AD7FF44641EEDE55898A9D228F0A921ED796C853E3F1533` and must remain ordinary Git content.
- The browser MP4 was derived from the validated 364,239,785-byte Store master with SHA-256 `3C0D867D007FF20607DDB7209A9EA9DFB78631C5959BC7B4992FDFAA50AD584F`, which remains preserved in the private WAZO release repository.
- The prior v1.1.4 narrated explainer and its complete editable workspace remain retained as historical media under their existing versioned folders; do not delete or overwrite them.
- Private WAZO application source and dependencies are intentionally excluded. Authorized reproduction requires a separate checkout of the recorded source commit.

## Stable Privacy Policy

- Public route: `https://imzub.github.io/WAZO-OFFICIAL/privacy/`, sourced from `docs/privacy/index.html`.
- Active revision: `WAZO-PP-2.0.0-2026-08-07`; effective date: `2026-08-07`; document SHA-256 `A2775340DCF179E8F68B33CFA73B9D722F4787BA351999B793F893F152564F79`.
- Canonical bundled-policy SHA-256: `0f792e634eec910e6c248575a2497301544ce8e85b9bd45a16827b2ec7a43150`.
- This policy applies to the live WAZO `2.0.0` Windows release and the WAZO Official website. The policy page, installer, release manifest, and release index are synchronized as the current v2.0.0 public release; the v1.1.6 tour remains historical media.
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
