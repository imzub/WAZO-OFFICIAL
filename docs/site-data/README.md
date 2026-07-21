# WAZO Website Data

This folder contains the public data and large assets used by the WAZO website.

## Structure

- `shared/branding/`: brand assets that are not tied to one release.
- `releases/index.json`: the public release index and current-version pointers.
- `releases/v<version>/release.json`: machine-readable metadata for one version.
- `releases/v<version>/updates/`: public release notes, manuals, and updater metadata for that version.
- `releases/v<version>/images/`: graphics that present that version.
- `releases/v<version>/video/`: browser-ready video, poster, captions, transcript, and media manifest for that version.
- `releases/v<version>/installer/`: published installer binaries for that version.

## Retention

Published releases remain tracked in GitHub. Archived installer binaries may be
excluded from an individual local clone with Git sparse checkout, but their
metadata and release notes remain available locally.

Large editable video-production assets stay outside the GitHub Pages source in
`project-data/releases/v<version>/promo/`. Public MP4 files under `docs/` must
remain ordinary Git objects so GitHub Pages can serve them. Production masters,
audio, and capture frames may use Git LFS and require `git lfs pull` after a
fresh clone.

When an installer is published, update its version manifest, release notes,
manual and updater files when supplied, `releases/index.json`, and the website
download section together. Verify published installer hashes and sizes against
the approved app-release handoff before promoting the version to `current`.
