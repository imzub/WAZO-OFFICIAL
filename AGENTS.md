# WAZO-OFFICIAL Website Agent Guide

This repository hosts the public WAZO product website through GitHub Pages.

## Purpose

- Showcase WAZO as a private personal wealth organizer.
- Explain app features, workflows, downloads, support, and release notes.
- Help users understand the app without exposing the private application source code.

## Repository Rules

- GitHub Pages publishes from `docs/`.
- Keep public website content in `docs/`.
- Do not recreate or use the old `Site/` folder.
- Do not link to the private WAZO source repository.
- The website may link to LinkedIn, support email, public release files, and public documentation.

## Product Messaging

- WAZO is a Windows desktop personal wealth organizer.
- It is offline-first and stores core data locally as JSON.
- It supports family/profile setup, members, assets, allocation targets, financial goals, reports, backups, privacy mode, themes, multiple currencies, and optional zakat planning.
- Zakat is optional. The website should not position WAZO as only a zakat app.
- Source code is private.

## Website Maintenance Rules

- Update this context file when website structure, public messaging, download/release process, support process, or GitHub Pages publishing rules change.
- Keep download sections version-aware: stable version, latest fix/testing version, release notes, and known fixes.
- Support actions should use email templates for bugs, feature requests, and queries.
- Use public-safe screenshots or app-style visuals only. Do not include personal financial data.

## Testing Checklist

- Open `docs/index.html` locally after UI changes.
- Confirm no private source-code links are present.
- Confirm GitHub Pages can publish from `docs/`.
- Confirm support email links open with useful templates.
- Check desktop and mobile responsiveness.
