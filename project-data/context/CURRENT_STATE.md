# Current WAZO Website State

Checkpoint date: 2026-07-24

## Published product state

- The current website and direct-installer release is WAZO `1.1.6` / build `1.1.6.0`.
- The stable website privacy route publishes policy revision `WAZO-PP-1.1.6-2026-07-23-R2` (effective `2026-07-23`, canonical source SHA-256 `0f792e634eec910e6c248575a2497301544ce8e85b9bd45a16827b2ec7a43150`). Policy commit `02b985126843180a6f68e3fac1aa1469642405bc` deployed successfully through GitHub Pages run `30020443537`.
- The current public direct installer is `docs/site-data/releases/v1.1.6/installer/WAZO-Setup-1.1.6.exe`: 102,427,430 bytes, SHA-256 `E641AB23BBFBC49A15E37C78EB62515E195D68C54815D6B1FFE533D50DC3E077`, from private product source commit `68562c0af607f5c73bd1b948beb95f5517243523`.
- Website artifact-publication commit `41b359e4e306dacb090da69b82e2e3de1eab2e7b` deployed successfully through GitHub Pages run `30037802828`. Cache-busted live verification at `2026-07-23T19:28:34Z` returned HTTP 200 for the homepage, release index, release manifest, release notes, privacy page, installer, and manual. The 102,427,430-byte installer and 112,431-byte, 16-page manual matched their recorded SHA-256 hashes exactly.
- Publication was explicitly authorized on 2026-07-23 after the recorded automated release gates passed. Physical human workflow validation is not recorded; website publication is not a human-validation pass.
- The current Organized W identity is `docs/site-data/shared/branding/wazo-logo-organized-w-r2.png`: 57,329 bytes, 256 x 256, SHA-256 `4F897AF777A8ADEB4782848E04F934B05D40F8F2A92979D75D75380E6BAC4B55`. Logo correction commit `ab4a65f06656940f3da92b02d0a9e2cc182dd769` deployed successfully through GitHub Pages run `30062852367`; live verification found HTTP 200 on the homepage, privacy page, and logo asset, with both pages referencing that asset.
- The previously published v1.1.5 installer (102,285,721 bytes, SHA-256 `94EF7F7C3456FE025689A44C228E4D8759F2AD153C12AD22B0ED81CC328D86AB`) and its rejected predecessor (102,284,642 bytes, SHA-256 `955F00602E1FE632F5F429963E396A535359907D80520A45C7DE9B23AC09A13E`) are superseded historical evidence only.
- The Microsoft Store card remains pending until the listing is published and independently verified.
- GitHub Pages continues to publish from `docs/` on branch `Master` under the `imzub` account.

## Product-tour state

- Status: accepted for the current website; future polish is deferred.
- Recording version: WAZO `1.1.4`.
- Private application source commit: `7c63be818372307dc08ff6551b7296fca863d3e7`.
- Runtime: 121.692 seconds on the production timeline; approximately 2 minutes 2 seconds in browser playback.
- Format: 1920 x 1080 H.264 video, AAC English audio, 30000/1001 fps.
- Voice: `en-US-AndrewNeural`, rate `-4%`, pitch `-1Hz`.
- Safety: captured from a fresh isolated Electron profile using anonymous demo data; installed user data was not used.

The home page now has a dedicated `#tour` section after the capability strip. It includes native playback controls, a non-squeezed 16:9 layout, poster image, default English WebVTT captions, visible version disclosure, downloadable transcript, and inline transcript.

## Asset locations

Public GitHub Pages delivery:

```text
docs/site-data/releases/v1.1.4/video/
```

Complete public-safe production workspace:

```text
project-data/releases/v1.1.4/promo/narrated/
```

Large production assets use Git LFS; the Pages MP4 does not.

## Resume point

The next requested media task is to improve the explainer later, not to change it now. Begin from the accepted master and `NEXT_IMPROVEMENTS.md`. The current product release remains v1.1.6 while that v1.1.4 recording is retained as explicitly labeled historical visual evidence. If a future installer or app version is supplied, update the site only after validating that release, and keep prior versioned files retained in Git.

Before making new changes, run:

```powershell
git switch Master
git pull --ff-only origin Master
git lfs pull
git status --short
```

Use the `imzub` GitHub account for all WAZO repository work without asking the user to choose an account.
