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
- Public installer downloads are stored in the matching version's `installer/` folder and linked from the Downloads section.
- Keep older releases and installers tracked in the GitHub repository. The local clone may use sparse checkout to omit archived installer binaries while keeping their metadata and release notes locally.
- Do not remove an older release artifact from GitHub unless Zubair explicitly asks for its deletion.
- Microsoft Store should be positioned as the recommended public install path once available. Keep the Store card unlinked and marked pending until the WAZO listing is published and verified; direct `.exe` installers are the current website channel for offline setup and controlled installation.
- Do not recreate or use the old `Site/` folder.
- Do not link to the private WAZO source repository.
- The website may link to LinkedIn, support email, public release files, and public documentation.

## Product Messaging

- WAZO is a Windows desktop personal wealth organizer.
- It is offline-first and stores core data locally. WAZO v1.1.5 protects app-managed Windows data as authenticated encrypted envelopes; do not describe those active records as plaintext JSON.
- It supports family/profile setup, members, assets, allocation targets, financial goals, reports, backups, privacy mode, themes, multiple currencies, and optional zakat planning.
- Zakat is optional. The website should not position WAZO as only a zakat app.
- Source code is private.

## Website Maintenance Rules

- Update this context file when website structure, public messaging, download/release process, support process, or GitHub Pages publishing rules change.
- Keep the website privacy-policy revision, effective date, and substantive text synchronized with the reviewed offline policy bundled with the matching WAZO release. Do not publish protected-storage or Store-readiness claims before the corresponding release behavior is verified.
- `docs/privacy/policy-manifest.json` and the `wazo-policy-*` metadata in `docs/privacy/index.html` must match the authoritative UTF-8/LF bytes of the sibling WAZO repository's `docs/PRIVACY_POLICY.md`. This static site has no package/build validation runner, so before publication deterministically verify: the canonical file has no UTF-8 BOM or CR bytes; `Get-FileHash -Algorithm SHA256` matches both website hash fields; revision, effective date, and canonical URL match; and the twelve numbered policy sections plus the local-processing summary are substantively present in both copies.
- Update `docs/site-data/releases/index.json`, the version's `release.json`, and its release notes whenever release status, installer metadata, product graphics, or public update details change.
- Keep download sections version-aware: recommended Microsoft Store install, latest published direct installer, and the major baseline installer, with release notes and known fixes.
- Keep SmartScreen/Chrome warning guidance visible near direct installer links until standalone installers are code-signed and have download reputation.
- Do not publish `latest.yml`, blockmaps, or other automatic-update metadata unless WAZO first ships and verifies a compatible automatic-update client and URL layout. WAZO v1.1.5 uses a direct installer link only.
- Current stable direct installer should track the latest validated build (currently `v1.1.5`).
- Support actions should use email templates for bugs, feature requests, and queries.
- Use public-safe screenshots or app-style visuals only. Do not include personal financial data.

## Testing Checklist

- Open `docs/index.html` locally after UI changes.
- Confirm no private source-code links are present.
- Confirm GitHub Pages can publish from `docs/`.
- Confirm support email links open with useful templates.
- Confirm every local page, image, manual, release-note, and installer link resolves, and verify public installer size/hash against the current release manifest.
- Confirm the `/privacy/` page, canonical URL, policy metadata, and sitemap entry are valid.
- Check desktop and mobile responsiveness.
