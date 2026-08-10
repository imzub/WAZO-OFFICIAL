# Current WAZO Website State

Checkpoint date: 2026-08-10

## Published product state

- The current stable website and direct-installer release is WAZO `1.1.7` / build `1.1.7.0`; the optional v2 testing installer is v2.0.0 / build 2.0.0.0. v1.1.9 is historical testing evidence.
- The stable website privacy route publishes policy revision `WAZO-PP-1.1.7-2026-07-25` (effective `2026-07-25`, canonical source SHA-256 `4d2e8f1076573679d5653bf63c12e3c08752ea7f261e2e820fd92a5e6f232dea`). It is synchronized with the current WAZO 1.1.7 application policy.
- The current installer candidate is `docs/site-data/releases/v1.1.7/installer/WAZO-Setup-1.1.7.exe`: 103,200,128 bytes, SHA-256 `489D6775D55E5F3FC7965C357263B5BA452B6BE073DE60CC8B9EC33AF31EF5F5`, from WAZO `Dev/QA` commit `c13bbb973c8866876f527685e52d1875b1de2ad7`. Source tests passed 889/889, focused 77/77, Demo seed/SIP 8/8, UI-humanity 198/198, packaged startup 12/12, and complete isolated runtime 19/19. Pages deployment and live byte/hash verification are pending for this update.
- Website commit `5db6957ae8e7d91a060db0fee2f37cbc5e4f807e` deployed through successful GitHub Pages run `30125432522`. Cache-busted verification at `2026-07-24T20:53:53Z` returned HTTP 200 and exact expected byte counts and SHA-256 hashes for the installer, video, captions, poster, thumbnail, transcript, and manual.
- Live desktop and 390 x 844 responsive browser checks passed with no console errors. The public video decoded at 1920 x 1080, duration 58.179 seconds, ready state 4, with one English caption track.
- The previous same-version v1.1.6 website bytes remain historical evidence: artifact-publication commit `41b359e4e306dacb090da69b82e2e3de1eab2e7b`, successful Pages run `30037802828`, verification at `2026-07-23T19:28:34Z`, installer size 102,427,430 bytes, and SHA-256 `E641AB23BBFBC49A15E37C78EB62515E195D68C54815D6B1FFE533D50DC3E077`.
- Corrective validation passed `726/726` source tests, `54/54` exact-package checks, `9/9` current-display checks, `166/166` UI-humanity checks, and `14/14` runtime workflows. Physical human workflow validation is not recorded; website publication is not a human-validation pass.
- The current Organized W identity is `docs/site-data/shared/branding/wazo-logo-organized-w-r2.png`: 57,329 bytes, 256 x 256, SHA-256 `4F897AF777A8ADEB4782848E04F934B05D40F8F2A92979D75D75380E6BAC4B55`. Logo correction commit `ab4a65f06656940f3da92b02d0a9e2cc182dd769` deployed successfully through GitHub Pages run `30062852367`; live verification found HTTP 200 on the homepage, privacy page, and logo asset, with both pages referencing that asset.
- The previously published v1.1.5 installer (102,285,721 bytes, SHA-256 `94EF7F7C3456FE025689A44C228E4D8759F2AD153C12AD22B0ED81CC328D86AB`) and its rejected predecessor (102,284,642 bytes, SHA-256 `955F00602E1FE632F5F429963E396A535359907D80520A45C7DE9B23AC09A13E`) are superseded historical evidence only.
- The Microsoft Store card uses `ms-windows-store://pdp/?productid=9NKLT8DKJ1QX`; listing availability remains independently unverified. The current Store AppX is 155,281,564 bytes / SHA-256 `46795AB01FB66B331F2C51107060EC2C4DB0C2C37A9C2A2EF26A1157744F575D`, local-only, and was not added to the website.
- GitHub Pages continues to publish from `docs/` on branch `Master` under the `imzub` account.

## Product-tour state

- Status: v1.1.6 tour remains published and live-verified as historical versioned media; the current downloadable installer is v1.1.7.
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

The v2.0.0 testing installer-only website release is sourced from WAZO commit `4284642`: 99,438,888 bytes, SHA-256 `5C6783D145FB3C3A5B83B1721B10F6D902F881455C7C3BD36C7F08156D2F753E`. It contains the existing-user migration repair that preserves legacy append-only investment facts across migration saves. It remains testing while v1.1.7 remains stable; live byte/size verification passed at website commit `e8cdc6a` through Pages deployment `31372833271` at `2026-08-10T09:09:00Z`. Keep the v1.1.9, v1.1.8, v1.1.6 tour, v1.1.4 tour, and all older release files retained in Git; do not add the local-only Store AppX to this website repository.

Before making new changes, run:

```powershell
git switch Master
git pull --ff-only origin Master
git lfs pull
git status --short
```

Use the `imzub` GitHub account for all WAZO repository work without asking the user to choose an account.

## Portable resume contract

Any new machine, AI, or account can resume from the repository state without hidden session data: read `AGENTS.md`, this file, `docs/WAZO_CODEX_HANDOFF_POINTER.md`, and the matching release manifest; verify the remote and branch; then compare the recorded source commit, artifact size, and SHA-256 before publishing. GitHub/Firefox authentication is never treated as project memory, and no token, browser profile, user data, or private application source belongs in this repository.
