# Current WAZO Website State

Checkpoint date: 2026-07-25

## Published product state

- The current website and direct-installer release is WAZO `1.1.6` / build `1.1.6.0`.
- The stable website privacy route publishes policy revision `WAZO-PP-1.1.6-2026-07-23-R2` (effective `2026-07-23`, canonical source SHA-256 `0f792e634eec910e6c248575a2497301544ce8e85b9bd45a16827b2ec7a43150`). Policy commit `02b985126843180a6f68e3fac1aa1469642405bc` deployed successfully through GitHub Pages run `30020443537`.
- A corrective replacement is prepared at `docs/site-data/releases/v1.1.6/installer/WAZO-Setup-1.1.6.exe`: 102,429,605 bytes, SHA-256 `A4BAB97F8D252FA95F586B98CB59BF123FE1F91C3BFA3CA52B7B6DCD807DE6F7`, from private product source commit `56399c120c644c1d80485b368370e630c58f6ac7`.
- The replacement has not yet been committed, deployed, or publicly byte/hash verified. After publication, record the exact website commit, Pages deployment, HTTP checks, and fresh installer/video download hashes here.
- The previous v1.1.6 website bytes remain historical live evidence: artifact-publication commit `41b359e4e306dacb090da69b82e2e3de1eab2e7b`, successful Pages run `30037802828`, verification at `2026-07-23T19:28:34Z`, installer size 102,427,430 bytes, and SHA-256 `E641AB23BBFBC49A15E37C78EB62515E195D68C54815D6B1FFE533D50DC3E077`.
- Corrective validation passed `726/726` source tests, `54/54` exact-package checks, `9/9` current-display checks, `166/166` UI-humanity checks, and `14/14` runtime workflows. Physical human workflow validation is not recorded; website publication is not a human-validation pass.
- The current Organized W identity is `docs/site-data/shared/branding/wazo-logo-organized-w-r2.png`: 57,329 bytes, 256 x 256, SHA-256 `4F897AF777A8ADEB4782848E04F934B05D40F8F2A92979D75D75380E6BAC4B55`. Logo correction commit `ab4a65f06656940f3da92b02d0a9e2cc182dd769` deployed successfully through GitHub Pages run `30062852367`; live verification found HTTP 200 on the homepage, privacy page, and logo asset, with both pages referencing that asset.
- The previously published v1.1.5 installer (102,285,721 bytes, SHA-256 `94EF7F7C3456FE025689A44C228E4D8759F2AD153C12AD22B0ED81CC328D86AB`) and its rejected predecessor (102,284,642 bytes, SHA-256 `955F00602E1FE632F5F429963E396A535359907D80520A45C7DE9B23AC09A13E`) are superseded historical evidence only.
- The Microsoft Store card remains pending until the listing is published and independently verified.
- GitHub Pages continues to publish from `docs/` on branch `Master` under the `imzub` account.

## Product-tour state

- Status: current v1.1.6 tour prepared for website publication.
- Recording version: WAZO `1.1.6`.
- Private application source commit: `56399c120c644c1d80485b368370e630c58f6ac7`.
- Runtime: 58.17 seconds.
- Format: 1920 x 1080 H.264 video, AAC English audio, 30000/1001 fps.
- Audio: English narration with an original deterministic music score.
- Safety: captured from a fresh isolated Electron profile using anonymous demo data; installed user data was not used.

The home page's `#tour` section includes native playback controls, a non-squeezed 16:9 layout, poster image, default English WebVTT captions, current-version disclosure, downloadable transcript, and inline transcript. Privacy Mode is intentionally off in the recording so the app remains understandable; no real user or financial data appears.

## Asset locations

Public GitHub Pages delivery:

```text
docs/site-data/releases/v1.1.6/video/
```

Validated high-bitrate production master:

```text
WAZO private release repository: releases/windows-store/v1.1.6/promo/
```

The 24,372,012-byte Pages MP4 has SHA-256 `6B79ED9EC177C0182AD7FF44641EEDE55898A9D228F0A921ED796C853E3F1533` and remains ordinary Git. It was derived from the 364,239,785-byte Store master with SHA-256 `3C0D867D007FF20607DDB7209A9EA9DFB78631C5959BC7B4992FDFAA50AD584F`. The older v1.1.4 public tour and editable production workspace remain retained as historical media.

## Resume point

The immediate resume point is publication: commit the prepared v1.1.6 installer and website tour, deploy GitHub Pages, then replace all pending-publication markers with the exact commit, deployment ID, HTTP status, and cache-busted installer/video hashes. Keep the prior v1.1.4 tour and all older release files retained in Git.

Before making new changes, run:

```powershell
git switch Master
git pull --ff-only origin Master
git lfs pull
git status --short
```

Use the `imzub` GitHub account for all WAZO repository work without asking the user to choose an account.
