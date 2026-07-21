# Current WAZO Website State

Checkpoint date: 2026-07-21

## Published product state

- The website remains WAZO `1.1.5`; no product, installer, Store, or policy version was changed for this media update.
- The validated direct installer remains `docs/site-data/releases/v1.1.5/installer/WAZO-Setup-1.1.5.exe`.
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
