# Current WAZO Website State

Checkpoint date: 2026-07-23

## Published product state

- The website product release remains WAZO `1.1.5`; the policy-only R2 publication does not change the installer, Store state, release index, or product-tour version.
- The stable website privacy route is prepared for policy revision `WAZO-PP-1.1.6-2026-07-23-R2` (effective `2026-07-23`, canonical source SHA-256 `0f792e634eec910e6c248575a2497301544ce8e85b9bd45a16827b2ec7a43150`). This is a policy-only publication for the WAZO `1.1.6` offline-only boundary; it does not promote or replace the current public `1.1.5` installer.
- The current public direct installer is `docs/site-data/releases/v1.1.5/installer/WAZO-Setup-1.1.5.exe`: 102,285,721 bytes, SHA-256 `94EF7F7C3456FE025689A44C228E4D8759F2AD153C12AD22B0ED81CC328D86AB`, from private product source commit `0f03c6084ab023cd14841158bd369461163ac319`.
- Website artifact-publication commit `94f6cff4868814ee3bc0fd40903e025a72c6331c` deployed successfully as GitHub Pages deployment `5538627778`. Cache-busted live verification at `2026-07-21T12:59:13Z` returned HTTP 200 for the homepage, release index, release manifest, release notes, privacy page, installer, and manual. The downloaded installer and manual matched their recorded byte sizes and SHA-256 hashes exactly.
- Publication was explicitly authorized on 2026-07-21 after the recorded automated release gates passed. Physical human workflow validation is not recorded; website publication is not a human-validation pass.
- The earlier 102,284,642-byte installer with SHA-256 `955F00602E1FE632F5F429963E396A535359907D80520A45C7DE9B23AC09A13E` is rejected, superseded historical evidence only.
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

The next requested media task is to improve the explainer later, not to change it now. Begin from the accepted master and `NEXT_IMPROVEMENTS.md`. If a future installer or app version is supplied, update the site only after validating that release, and keep prior versioned files retained in Git.

Before making new changes, run:

```powershell
git switch Master
git pull --ff-only origin Master
git lfs pull
git status --short
```

Use the `imzub` GitHub account for all WAZO repository work without asking the user to choose an account.
