# WAZO Website Data

This folder contains the public data and large assets used by the WAZO website.

## Structure

- `shared/branding/`: brand assets that are not tied to one release.
- `releases/index.json`: the public release index and current-version pointers.
- `releases/v<version>/release.json`: machine-readable metadata for one version.
- `releases/v<version>/updates/`: human-readable public release notes.
- `releases/v<version>/images/`: graphics that present that version.
- `releases/v<version>/installer/`: published installer binaries for that version.

## Retention

Published releases remain tracked in GitHub. Archived installer binaries may be
excluded from an individual local clone with Git sparse checkout, but their
metadata and release notes remain available locally.

When an installer is published, update its version manifest, release notes,
`releases/index.json`, and the website download section together.
