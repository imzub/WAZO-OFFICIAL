# WAZO Official Website Context

The WAZO-OFFICIAL repository is the public marketing and support website for WAZO. It is separate from the private WAZO application source repository.

## Publishing

- GitHub Pages URL: `https://imzub.github.io/WAZO-OFFICIAL/`
- Reserved Microsoft Store product ID: `9NKLT8DKJ1QX`. Do not expose its web or app link until the WAZO listing is published and verified as available.
- Publish source: `docs/`
- Keep `.nojekyll` in `docs/` so GitHub Pages serves static assets directly.

## Content Goals

- Explain what WAZO does.
- Present the complete WAZO `v1.1.6` Windows product experience, major improvements, and current direct installer.
- Help users understand the app workflow.
- Provide version-aware download areas.
- Position Microsoft Store as the recommended public install channel once available; until then, show it as pending without an outbound link.
- Host public Windows installer downloads in versioned folders under `docs/site-data/releases/` with version, size, notes, and SHA-256 hashes.
- Explain that direct `.exe` installers may trigger SmartScreen/Chrome warnings until they are code-signed and gain reputation.
- Provide support paths for bugs, issues, feature requests, and queries.
- The downloads section should show only three cards: the recommended-when-available Microsoft Store channel, latest published direct installer, and the current major baseline installer such as `1.0.0`, `1.1.0`, or `2.0.0`.
- Showcase privacy, protected local storage, multiple currencies, reports, backups, reversible records, local guidance, and the optional zakat module. For v1.1.6, describe app-managed Windows records as authenticated encrypted envelopes protected by a Windows-bound key rather than plaintext local JSON.
- Keep the downloads section visually light: one short warning panel, three release cards, and concise version metadata.
- Add beginner-friendly FAQ items for initial setup, freeware, offline mode, backups, and core workflows whenever the site is updated.

## Current Public Downloads

- Prepared corrective direct installer: `v1.1.6` / `docs/site-data/releases/v1.1.6/installer/WAZO-Setup-1.1.6.exe`.
- The prepared Windows x64 installer is 102,429,605 bytes with SHA-256 `A4BAB97F8D252FA95F586B98CB59BF123FE1F91C3BFA3CA52B7B6DCD807DE6F7`; its product source commit is `56399c120c644c1d80485b368370e630c58f6ac7`.
- The replacement has not yet been committed, deployed, or publicly byte/hash verified. After publication, replace this preparation checkpoint with the exact website commit, GitHub Pages deployment, HTTP results, and fresh installer/video download hashes.
- The previous live v1.1.6 installer remains historical deployment evidence: 102,427,430 bytes, SHA-256 `E641AB23BBFBC49A15E37C78EB62515E195D68C54815D6B1FFE533D50DC3E077`, source commit `68562c0af607f5c73bd1b948beb95f5517243523`, website artifact commit `41b359e4e306dacb090da69b82e2e3de1eab2e7b`, and successful Pages run `30037802828`.
- Final corrective-source validation passed syntax for 78 files, static analysis, brand and Trust Center checks, `726/726` tests, package matrices `54/54`, native-current-display matrices `9/9` at DPR `1.5`, UI-humanity `166/166`, and runtime workflows `14/14`. This remains automated evidence (`humanValidated=false`); physical packaged human validation is not recorded.
- The superseded published v1.1.5 installer remains historical evidence: 102,285,721 bytes, SHA-256 `94EF7F7C3456FE025689A44C228E4D8759F2AD153C12AD22B0ED81CC328D86AB`, product source commit `0f03c6084ab023cd14841158bd369461163ac319`, and website publication commit `94f6cff4868814ee3bc0fd40903e025a72c6331c`.
- The rejected v1.1.5 predecessor also remains historical evidence: 102,284,642 bytes, SHA-256 `955F00602E1FE632F5F429963E396A535359907D80520A45C7DE9B23AC09A13E`, product source commit `232210ba29904c9f3badf54d0650edc6c721a1b1`, and website publication commit `1630edadb907cce834886ded65b7190ecbe6205a`.
- The matching 16-page v1.1.6 manual is 112,431 bytes with SHA-256 `028C0233B47B44AB32C655E0F1133512CF8118E164032D700B706FB5FF66CE30`.
- Authenticode status is `NotSigned`, so keep the direct-installer warning visible and never claim code signing.
- Major baseline installer: `v1.0.0` / `docs/site-data/releases/v1.0.0/installer/WAZO-Setup-1.0.0.exe`.
- Older installers retained for rollback/testing: `v1.0.1`, `v1.0.2`, and `v1.0.4`.
- Keep older installers available unless Zubair explicitly asks to remove them.
- The Store card is recommended-when-available but remains unlinked until availability is verified. The corrected direct installer is the current usable public download; it remains unsigned and separate from the pending Store channel.

## Versioned Website Data

- Shared branding lives in `docs/site-data/shared/branding/`.
- Release data lives in `docs/site-data/releases/v<version>/`.
- Each release keeps a machine-readable `release.json` and human-readable notes under `updates/`.
- Release-specific product graphics live under that release's `images/` folder.
- Release-specific public video assets live under that release's optional `video/` folder with a machine-readable manifest, web MP4, poster, captions, and transcript.
- Installer binaries live under that release's `installer/` folder.
- `docs/site-data/releases/index.json` records the product version, current published installer, major baseline, and archived versions.
- Archived installers remain tracked in GitHub for GitHub Pages and rollback use. This working clone may omit their binary files through Git sparse checkout; their manifests and notes remain local.
- WAZO does not currently integrate Electron's automatic updater. Do not publish `latest.yml`, blockmaps, or other auto-update-feed metadata for v1.1.6; website delivery is the direct installer link only.

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
- Active revision: `WAZO-PP-1.1.6-2026-07-23-R2`; effective date: `2026-07-23`.
- Canonical bundled-policy SHA-256: `0f792e634eec910e6c248575a2497301544ce8e85b9bd45a16827b2ec7a43150`.
- This policy applies to the live WAZO `1.1.6` Windows release and the WAZO Official website. The policy, installer, 16-page manual, release manifest, and release index are published together as the current v1.1.6 public release.
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
