# WAZO Website Project Data

This directory preserves the public-safe working material needed to continue WAZO website, media, release, and update work on another computer.

## Current checkpoint

- GitHub owner/account: `imzub`
- Repository: `WAZO-OFFICIAL`
- Publishing branch: `Master`
- GitHub Pages source: `docs/`
- Live site: `https://imzub.github.io/WAZO-OFFICIAL/`
- Current website and direct-installer version: `1.1.6` / build `1.1.6.0`
- Current privacy policy: `WAZO-PP-1.1.6-2026-07-23-R2`
- Current public manual: 16-page WAZO `1.1.6` user manual
- Current website identity: Organized W revision `organized-w-r2`
- Current narrated product-tour recording: `1.1.4`

The version difference is intentional. The accepted tour was recorded from WAZO 1.1.4. The website is on 1.1.6 and clearly explains that the recording demonstrates earlier core workflows, not the current protected-storage, reversible-history, financial-year, risk, or local-guidance internals.

## Directory map

- `context/` contains the durable state, decisions, handoff instructions, and improvement backlog.
- `releases/v1.1.4/promo/narrated/` contains the accepted narrated-video workspace.
- `docs/site-data/releases/v1.1.4/video/` contains the lightweight browser delivery copy, poster, captions, transcript, and public manifest.

## Clone and restore

Large production assets are tracked with Git LFS. On a new computer:

```powershell
git lfs install
git lfs pull
```

If the clone uses sparse checkout, include this directory before pulling its LFS objects:

```powershell
git sparse-checkout add project-data
git lfs pull --include="project-data/releases/v1.1.4/promo/narrated/**"
```

The browser-ready MP4 under `docs/` deliberately stays in ordinary Git because GitHub Pages must serve the actual media bytes, not an LFS pointer.

## Public/private boundary

This public repository does not contain the private WAZO application source, application dependencies, credentials, browser sessions, or personal WAZO data. The production notes record the exact source commit needed to reproduce the tour. Reproduction requires a separate authorized checkout of the private WAZO application repository.

Start future work with `context/CURRENT_STATE.md`, then read `context/PRODUCTION_HANDOFF.md` before rebuilding or replacing the video.
