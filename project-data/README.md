# WAZO Website Project Data

This directory preserves the public-safe working material needed to continue WAZO website, media, release, and update work on another computer.

## Current checkpoint

- GitHub owner/account: `imzub`
- Repository: `WAZO-OFFICIAL`
- Publishing branch: `Master`
- GitHub Pages source: `docs/`
- Live site: `https://imzub.github.io/WAZO-OFFICIAL/`
- Current website and direct-installer version: `1.1.7` / build `1.1.7.0`
- Current privacy policy: `WAZO-PP-1.1.7-2026-07-25`
- Current website identity: Organized W revision `organized-w-r2`
- Current narrated product-tour recording: `1.1.6` historical media

The historical 58.17-second tour was recorded from WAZO 1.1.6 using anonymous demo data. Its browser-ready media, captions, poster, thumbnail, transcript, and manifest are versioned with the release. The earlier v1.1.4 narrated tour remains retained as historical media.

The v1.1.7 installer-only website release was published from website commit `19dc0f51899a730955e11327b53a6577a9b4013e` through Pages deployment `30834371474`; the live installer matched 103,181,264 bytes and SHA-256 `2DDEADC0D06E171DD7DB95B4D5038DAEB9CABE4BC7849A450EF9EEB2CEB906E1`. The v1.1.6 tour remains historical media.

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
