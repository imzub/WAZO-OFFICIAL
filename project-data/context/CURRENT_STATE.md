# Current WAZO Website State

## 2026-08-13 v2 testing installer synchronization

- The v2.0.0 testing installer is locally replaced with the artifact from
  private WAZO `Dev/QA` commit `3e92050`: 99,450,391 bytes, SHA-256
  `94CE4DD7C73739468A7525BEC8747BA5060DB74CFC626C5E589A5F260B4AA77E`.
- Validation evidence is root 1,675/1,675, focused 536/536, and ultra-scale
  8/8. Pages publication and public hash verification are pending the website
  push. Stable v1.1.7 remains unchanged; the Store AppX is local-only.

## 2026-08-11 premium v2 screen-led promotion publication

- Premium v2 media is live from website `Master` commit `8f8a27c` through
  successful Pages deployment `31497574428`. The public homepage points to
  the 166.467-second, 1920x1080 English-narrated/captioned product tour.
- Source anchor: private WAZO `Dev/QA` commit
  `c821aab73f865081603786944ad62a9bcde1c858`. The final MP4 is 8,278,367
  bytes with SHA-256
  `6D37BD32A456D27657366A5F602632DC5AC5252C1A36EE5D1E3B2FEB6F9B4DCE`.
  Public HTTP 200 and exact hashes for all supporting assets were verified at
  `2026-08-11T13:45:29Z`.
- The older short v2 review cut and historical v1.1.6 tour remain retained;
  stable v1.1.7 is unchanged. Public media uses synthetic Demo data only,
  with no user data or credentials. Website MP4 delivery remains ordinary Git;
  private source MP4s use Git LFS and render intermediates remain ignored.

Checkpoint date: 2026-08-11

## v2 dynamic promo media

- Private WAZO source commit 4bf939b produced the v2 testing promo:
  52 seconds, 1,920x1,080, H.264/AAC, 7,196,381 bytes,
  SHA-256 DC3ED9DE1BE546885F76D6E1B0C2C069A305A9AD3AB7F460EB91114CA6946BF6.
- The public v2 release now includes the video manifest, MP4, captions,
  transcript, no-audio variant, poster, and thumbnail. Website artifact commit
  26f6904 and Pages deployment 31484600128 are live; public HTTP 200 and exact
  MP4/poster hashes were verified at 2026-08-11T11:02:17Z.
- The v1.1.6 narrated tour remains historical and unchanged.

## 2026-08-11 refreshed v2 testing package

- The optional v2.0.0 / build 2.0.0.0 testing installer is rebuilt from WAZO
  `Dev/QA` source commit `c990cc3`: 99,434,227 bytes, SHA-256
  `F2C4808064438E863E1FD065BDA1CDD8D016332C981484E16FCEF5F5E5078130`.
- Source evidence is 1,661/1,661 tests, 100,000/460,000 deep-audit
  probes/assertions, 496/496 full UI Humanity cases with zero severe contrast
  findings, 21/21 runtime workflows, 1,000/1,000 scenarios, and 7/7 package
  compatibility cases. Installer payload verification and 12/12 isolated
  startup journeys passed. GitHub Pages deployment `31465805369` completed
  successfully; public HTTP 200/size/hash verification passed at
  `2026-08-11T06:41:05Z`.
- Stable v1.1.7 is unchanged; the Store AppX remains local-only, and Android
  remains archived.

## Published product state

- The current stable website and direct-installer release is WAZO `1.1.7` / build `1.1.7.0`; the optional v2 testing installer is v2.0.0 / build 2.0.0.0. v1.1.9 is historical testing evidence.
- The stable website privacy route publishes policy revision `WAZO-PP-1.1.7-2026-07-25` (effective `2026-07-25`, canonical source SHA-256 `4d2e8f1076573679d5653bf63c12e3c08752ea7f261e2e820fd92a5e6f232dea`). It is synchronized with the current WAZO 1.1.7 application policy.
- The stable installer is `docs/site-data/releases/v1.1.7/installer/WAZO-Setup-1.1.7.exe`: 103,200,128 bytes, SHA-256 `489D6775D55E5F3FC7965C357263B5BA452B6BE073DE60CC8B9EC33AF31EF5F5`, from WAZO `Dev/QA` commit `c13bbb973c8866876f527685e52d1875b1de2ad7`. Its release manifest records verified Pages deployment `30905719455` on `2026-08-04T11:41:14Z`.
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

The refreshed v2.0.0 testing installer-only website release is sourced from WAZO `Dev/QA` commit `c990cc3`: 99,434,227 bytes, SHA-256 `F2C4808064438E863E1FD065BDA1CDD8D016332C981484E16FCEF5F5E5078130`. It remains testing while v1.1.7 remains stable; public HTTP 200/size/hash verification passed through Pages deployment `31465805369` at `2026-08-11T06:41:05Z`. Keep the v1.1.9, v1.1.8, v1.1.6 tour, v1.1.4 tour, and all older release files retained in Git; do not add the local-only Store AppX to this website repository.

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
