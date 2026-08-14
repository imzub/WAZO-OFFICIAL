# WAZO Website Project Data

This directory preserves the public-safe working material needed to continue WAZO website, media, release, and update work on another computer.

## Current checkpoint

- GitHub owner/account: `imzub`
- Repository: `WAZO-OFFICIAL`
- Publishing branch: `Master`
- GitHub Pages source: `docs/`
- Live site: `https://imzub.github.io/WAZO-OFFICIAL/`
- Current stable website and direct-installer version: `2.0.0` / build `2.0.0.0`
- The former v1.1.7 website release is removed from current website metadata; older releases remain historical repository evidence.
- Current privacy policy: `WAZO-PP-2.0.0-2026-08-07`
- Current website identity: Organized W revision `organized-w-r2`
- Current narrated product-tour recording: `1.1.6` historical media

The historical 58.17-second tour was recorded from WAZO 1.1.6 using anonymous demo data. Its browser-ready media, captions, poster, thumbnail, transcript, and manifest are versioned with the release. The earlier v1.1.4 narrated tour remains retained as historical media.

The stable v2.0.0 installer is 99,450,391 bytes with SHA-256 `31F44DAF38D26CDB69A42AFFE46FE473060CA239262871FA7B5A6F4BB9E44FE4`, anchored to WAZO `Dev/QA` source commit `28b0522`. Local hash, payload, and 18/18 startup verification passed; website commit `2a7a67f4c9f3071a4635aa4ea558a0538f27ec24` deployed through Pages deployment `5886802524`, and public HTTP/size/hash verification passed at `2026-08-13T11:11:41Z`. The v1.1.6 tour remains historical media. Microsoft Store Submission 5 is now published and available with `WAZO-Store-2.0.0-x64.appx` v2.0.0.0 for X64 Windows.Desktop devices.

## Directory map

- `context/` contains the durable state, decisions, handoff instructions, and improvement backlog.
- `releases/v1.1.4/promo/narrated/` contains the retained historical v1.1.4 narrated-video workspace.
- `docs/site-data/releases/v1.1.4/video/` contains the retained historical v1.1.4 browser delivery assets.
- `docs/site-data/releases/v1.1.6/video/` contains the historical lightweight browser delivery copy, poster, thumbnail, captions, transcript, and public manifest.

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

Browser-ready MP4 files under `docs/` deliberately stay in ordinary Git because GitHub Pages must serve the actual media bytes, not an LFS pointer. The historical v1.1.6 Store master remains preserved in the private WAZO release repository and is not duplicated here.

## Public/private boundary

This public repository does not contain the private WAZO application source, application dependencies, credentials, browser sessions, or personal WAZO data. The production notes record the exact source commit needed to reproduce the tour. Reproduction requires a separate authorized checkout of the private WAZO application repository.

Start future work with `context/CURRENT_STATE.md`, then read `context/PRODUCTION_HANDOFF.md` before rebuilding or replacing the video.
