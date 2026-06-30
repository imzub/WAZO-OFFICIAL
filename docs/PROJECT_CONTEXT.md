# WAZO Official Website Context

The WAZO-OFFICIAL repository is the public marketing and support website for WAZO. It is separate from the private WAZO application source repository.

## Publishing

- GitHub Pages URL: `https://imzub.github.io/WAZO-OFFICIAL/`
- Microsoft Store web URL: `https://apps.microsoft.com/detail/9NKLT8DKJ1QX`
- Microsoft Store app deep link: `ms-windows-store://pdp/?productid=9NKLT8DKJ1QX`
- Publish source: `docs/`
- Keep `.nojekyll` in `docs/` so GitHub Pages serves static assets directly.

## Content Goals

- Explain what WAZO does.
- Help users understand the app workflow.
- Provide version-aware download areas.
- Position Microsoft Store as the recommended public install channel.
- Host public Windows installer downloads from `docs/downloads/` with version, size, notes, and SHA-256 hashes.
- Explain that direct `.exe` installers may trigger SmartScreen/Chrome warnings until they are code-signed and gain reputation.
- Provide support paths for bugs, issues, feature requests, and queries.
- Showcase privacy, local JSON storage, multiple currencies, reports, backups, and optional zakat module.

## Current Public Downloads

- Stable direct installer: `v1.0.0` / `docs/downloads/WAZO-Setup-1.0.0.exe`.
- Latest fix direct installer: `v1.0.2` / `docs/downloads/WAZO-Setup-1.0.2.exe`.
- Previous testing installer retained for rollback testing: `v1.0.1` / `docs/downloads/WAZO-Setup-1.0.1.exe`.
- Keep older installers available unless Zubair explicitly asks to remove them.
- Direct installers remain available, but the Store link should be the primary public install path.

## Public Safety

- Do not link to the private WAZO source repo.
- Do not publish real user financial data.
- Use only public-safe screenshots, generated visuals, or anonymized demo data.

## Change Rule

Update `AGENTS.md` or this context file when future website work changes publishing source, support flow, release/download strategy, or core product positioning.
