# WAZO Website Project Data

This directory preserves the public-safe working material needed to continue WAZO website, media, release, and update work on another computer.

## Current checkpoint

- GitHub owner/account: `imzub`
- Repository: `WAZO-OFFICIAL`
- Publishing branch: `Master`
- GitHub Pages source: `docs/`
- Live site: `https://imzub.github.io/WAZO-OFFICIAL/`
- Current stable website and direct-installer version: `1.1.7` / build `1.1.7.0`
- Current optional deep-audit testing installer: `1.1.9` / build `1.1.9.0`; v1.1.8 remains historical testing evidence.
- Current privacy policy: `WAZO-PP-1.1.7-2026-07-25`
- Current website identity: Organized W revision `organized-w-r2`
- Current narrated product-tour recording: `1.1.6` historical media

The historical 58.17-second tour was recorded from WAZO 1.1.6 using anonymous demo data. Its browser-ready media, captions, poster, thumbnail, transcript, and manifest are versioned with the release. The earlier v1.1.4 narrated tour remains retained as historical media.

The stable v1.1.7 installer remains 103,200,128 bytes with SHA-256 `489D6775D55E5F3FC7965C357263B5BA452B6BE073DE60CC8B9EC33AF31EF5F5`. The optional v1.1.9 deep-audit testing installer is 103,209,860 bytes with SHA-256 `D8097C2BC4CDCF63B80E5A2FCA6F9A79593AFE1ED8A45D371FB81A6A82F0AA01`, anchored to WAZO source commit `d6533f1`; live byte/hash verification passed at website commit `f976331ac0b0047eea4176c8b8c5047e18528dd5` through Pages deployment `31074581797` at `2026-08-06T05:37:21Z`. The v1.1.6 tour remains historical media.

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
