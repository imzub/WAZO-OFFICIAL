# WAZO Official Website Context

The WAZO-OFFICIAL repository is the public marketing and support website for WAZO. It is separate from the private WAZO application source repository.

## Publishing

- GitHub Pages URL: `https://imzub.github.io/WAZO-OFFICIAL/`
- Publish source: `docs/`
- Keep `.nojekyll` in `docs/` so GitHub Pages serves static assets directly.

## Content Goals

- Explain what WAZO does.
- Help users understand the app workflow.
- Provide version-aware download areas.
- Position Microsoft Store as the recommended public install channel after approval.
- Host public Windows installer downloads from `docs/downloads/` with version, size, notes, and SHA-256 hashes.
- Explain that direct `.exe` installers may trigger SmartScreen/Chrome warnings until they are code-signed and gain reputation.
- Provide support paths for bugs, issues, feature requests, and queries.
- Showcase privacy, local JSON storage, multiple currencies, reports, backups, and optional zakat module.

## Public Safety

- Do not link to the private WAZO source repo.
- Do not publish real user financial data.
- Use only public-safe screenshots, generated visuals, or anonymized demo data.

## Change Rule

Update `AGENTS.md` or this context file when future website work changes publishing source, support flow, release/download strategy, or core product positioning.
