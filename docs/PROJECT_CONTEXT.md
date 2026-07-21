# WAZO Official Website Context

The WAZO-OFFICIAL repository is the public marketing and support website for WAZO. It is separate from the private WAZO application source repository.

## Publishing

- GitHub Pages URL: `https://imzub.github.io/WAZO-OFFICIAL/`
- Reserved Microsoft Store product ID: `9NKLT8DKJ1QX`. Do not expose its web or app link until the WAZO listing is published and verified as available.
- Publish source: `docs/`
- Keep `.nojekyll` in `docs/` so GitHub Pages serves static assets directly.

## Content Goals

- Explain what WAZO does.
- Present the complete WAZO `v1.1.5` Windows product experience, major improvements, and current direct installer.
- Help users understand the app workflow.
- Provide version-aware download areas.
- Position Microsoft Store as the recommended public install channel once available; until then, show it as pending without an outbound link.
- Host public Windows installer downloads in versioned folders under `docs/site-data/releases/` with version, size, notes, and SHA-256 hashes.
- Explain that direct `.exe` installers may trigger SmartScreen/Chrome warnings until they are code-signed and gain reputation.
- Provide support paths for bugs, issues, feature requests, and queries.
- The downloads section should show only three cards: the recommended-when-available Microsoft Store channel, latest published direct installer, and the current major baseline installer such as `1.0.0`, `1.1.0`, or `2.0.0`.
- Showcase privacy, local storage, multiple currencies, reports, backups, and the optional zakat module. For v1.1.5, describe app-managed Windows records as authenticated protected storage rather than plaintext local JSON.
- Keep the downloads section visually light: one short warning panel, three release cards, and concise version metadata.
- Add beginner-friendly FAQ items for initial setup, freeware, offline mode, backups, and core workflows whenever the site is updated.

## Current Public Downloads

- Stable direct installer: `v1.1.5` / `docs/site-data/releases/v1.1.5/installer/WAZO-Setup-1.1.5.exe`.
- The corrected published Windows x64 installer is 102,285,721 bytes with SHA-256 `94EF7F7C3456FE025689A44C228E4D8759F2AD153C12AD22B0ED81CC328D86AB`; its product source commit is `0f03c6084ab023cd14841158bd369461163ac319`.
- Final source verification passed syntax, static analysis, and brand checks; the full suite passed `245/245` in `25.9s`, and the clean rerun of the default source-startup gate passed `12/12` in `148.5s`.
- The exact corrected NSIS/website-installer payload matrix passed `18/18`. Native-current-display browser/CDP interaction against that exact payload passed `3/3` fresh, legacy, and lifecycle scenarios at DPR `1.5` (CSS screen `1280 x 800`, work area `1280 x 752`, physical display `1920 x 1200`) in `104.4s`; Windows `IsZoomed` separately attested maximized state at flow endpoints and all five lifecycle checkpoints. This remains automated evidence (`humanValidated=false`); physical packaged human validation is not recorded. Publication was explicitly authorized by the user on July 21, 2026 and must not be described as a human test pass.
- Historical predecessor: the rejected and superseded 102,284,642-byte v1.1.5 installer had SHA-256 `955F00602E1FE632F5F429963E396A535359907D80520A45C7DE9B23AC09A13E`, product source `232210ba29904c9f3badf54d0650edc6c721a1b1`, and website publication commit `1630edadb907cce834886ded65b7190ecbe6205a`. Preserve that identity only as historical traceability.
- The matching 12-page manual is 96,715 bytes with SHA-256 `F21FCF29713F10AA8BEB934A21AF08112B16055C0EA66A51D5CEB877B1055E59`.
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
- WAZO does not currently integrate Electron's automatic updater. Do not publish `latest.yml`, blockmaps, or other auto-update-feed metadata for v1.1.5; website delivery is the direct installer link only.

## Public Safety

- Do not link to the private WAZO source repo.
- Do not publish real user financial data.
- Use only public-safe screenshots, generated visuals, or anonymized demo data.

## Current Product Tour

- The home page includes a narrated product tour at `#tour`, placed before the release-specific v1.1.5 changes.
- The accepted interface recording is WAZO `v1.1.4`, built from private application commit `7c63be818372307dc08ff6551b7296fca863d3e7`; the website and current installer remain `v1.1.5`.
- The tour is approximately 2 minutes 2 seconds, 1920 x 1080, with English narration, default English WebVTT captions, anonymous demo data, a poster, and a complete transcript.
- Public delivery files are under `docs/site-data/releases/v1.1.4/video/`. The Pages MP4 must remain ordinary Git content.
- The complete public-safe editable workspace and durable continuation notes are under `project-data/`. The master, production audio, voice segments, and 731 capture frames use Git LFS and require `git lfs pull` after cloning.
- Private WAZO application source and dependencies are intentionally excluded. Authorized reproduction requires a separate checkout of the recorded source commit.
- Do not describe the v1.1.4 recording as demonstrating v1.1.5 protected-storage internals. Its on-page disclosure explains the version boundary.

## Stable Privacy Policy

- Public route: `https://imzub.github.io/WAZO-OFFICIAL/privacy/`, sourced from `docs/privacy/index.html`.
- Active revision: `WAZO-PP-1.1.5-2026-07-20`; effective date: `2026-07-20`.
- Canonical bundled-policy SHA-256: `345782b97fb5c6e530658415a4ba8b1a2589f03068e2238b03a588a1b9a442af`.
- `docs/privacy/policy-manifest.json` and the `wazo-policy-*` metadata in the policy HTML must retain the same revision, effective date, URL, and canonical hash as the exact UTF-8/LF `docs/PRIVACY_POLICY.md` bundled by the matching WAZO release.
- Any substantive privacy-policy edit requires a new reviewed revision and synchronized app, website, manifest, Help/About, manual, and Store-listing metadata. Do not silently edit one copy.

## Change Rule

Update `AGENTS.md` or this context file when future website work changes publishing source, support flow, release/download strategy, or core product positioning.

## Current Website Presentation

- Product graphics for the `v1.1.5` experience live in `docs/site-data/releases/v1.1.5/images/`; all five website images are genuine 1920 x 1080 app captures with anonymous/demo data.
- The public feature story highlights seven-step initial setup, non-preselected in-app privacy acknowledgement, protected Windows storage, backup-first v1.1.4 migration, password-protected portable backups, protected automatic recovery, readable-export warnings, opt-in online rates, the Asset Library, Assets and investment review, and performance reports.
- Current-installer confidence messaging may cite only confirmed evidence: syntax, static analysis, and brand checks passed; the full suite passed `245/245` in `25.9s`; the clean default source-startup rerun passed `12/12` in `148.5s`; the corrected NSIS/website-installer payload matrix passed `18/18`; and native-current-display browser/CDP interaction against the exact payload passed `3/3` in `104.4s`, with Windows `IsZoomed` attestation at flow endpoints and all five lifecycle checkpoints and `humanValidated=false`. Publication is confirmed separately and must not be presented as physical human validation.
- Existing-user messaging must explain the one-time privacy review, that exiting before acknowledgement leaves the v1.1.4 store unchanged, and that successful migration preserves supported data without re-entry.
- Windows protection claims apply only to the Windows desktop release. Do not imply Android protection parity.
