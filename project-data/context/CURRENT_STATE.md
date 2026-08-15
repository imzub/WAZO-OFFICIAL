# Current WAZO Website State

## 2026-08-15 v2.0.1 stable website promotion

- Current website direct installer: WAZO v2.0.1 / build 2.0.1.0, sourced from
  private WAZO `Dev/QA` commit `5b82ddf`.
- Installer size/hash: 99,453,083 bytes / SHA-256
  `F2F04955A46EB2AC0DED9C29D44D0E93D4DA9FFCAE039CE104398171ED123EF8`.
- Website commit `018a987` deployed through Pages run `31884767262`; public
  HTTP 200, exact size, and exact hash verification passed at
  `2026-08-15T12:37:17Z`.
- v2.0.0 remains retained and byte-preserved as the previous stable website
  installer. Microsoft Store remains published as v2.0.0.0; no Store update
  was claimed or submitted in this website-only promotion.

## 2026-08-14 Microsoft Store v2.0.0 publication verification

- Current repository synchronization: private WAZO `Dev/QA` is at `42a0477`
  and WAZO Official `Master` is at `ade2795`. The stable installer’s artifact
  provenance remains private source commit `28b0522`; its public bytes/hash are
  unchanged.
- The LinkedIn article and article-share post are drafted and saved but remain
  unpublished. The article includes the approved cover video and three
  captioned WAZO visuals.

- Partner Center direct verification shows: “Your latest product is now
  available on Microsoft Store” and the Store presence is available.
- Submission 5 contains `WAZO-Store-2.0.0-x64.appx`, version `2.0.0.0`,
  architecture `X64`, device family `Windows.Desktop`, minimum version
  `10.0.17763.0`. The submission was last modified on 2026-08-14.
- Verified product links: Store deep link
  `ms-windows-store://pdp/?productid=9NKLT8DKJ1QX`; browser listing
  `https://apps.microsoft.com/detail/9NKLT8DKJ1QX`.
- The live Store listing metadata still contains stale v1.1.6 wording in its
  “What’s new” field. Do not repeat that text in public WAZO messaging; it is a
  separate Store listing correction item for the next editable submission.

## 2026-08-13 v2.0.0 stable website promotion

- WAZO v2.0.0 is the stable website release, sourced from private WAZO
  `Dev/QA` commit `28b0522`. The direct installer is 99,450,391 bytes with
  SHA-256 `31F44DAF38D26CDB69A42AFFE46FE473060CA239262871FA7B5A6F4BB9E44FE4`.
- Validation evidence is root 1,675/1,675, Import Studio 46/46, focused
  536/536, packaged startup 18/18, launch media 44/44, compatibility 7/7,
  deep audit 100,000 probes / 460,000 assertions, scenario register 1,000/1,000,
  and ultra-scale 8/8. Website commit `2a7a67f4c9f3071a4635aa4ea558a0538f27ec24`
  deployed through Pages deployment `5886802524`; public HTTP/size/hash
  verification passed at `2026-08-13T11:11:41Z`. Microsoft Store publication
  is recorded separately in the 2026-08-14 checkpoint above.

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
  v2.0.0 is now the stable website release. Public media uses synthetic Demo data only,
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

## Historical 2026-08-11 refreshed v2 testing package

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
- This package is historical; the v2.0.0 stable website package is recorded in
  the 2026-08-13 checkpoint above. The Store AppX remains local-only, and
  Android remains archived.

## Current published product state

- The current stable website and direct-installer release is WAZO `2.0.0` / build `2.0.0.0`, sourced from WAZO `Dev/QA` commit `28b0522`. The installer is `docs/site-data/releases/v2.0.0/installer/WAZO-Setup-2.0.0-stable-20260813.exe`: 99,450,391 bytes, SHA-256 `31F44DAF38D26CDB69A42AFFE46FE473060CA239262871FA7B5A6F4BB9E44FE4`.
- The stable website privacy route publishes policy revision `WAZO-PP-2.0.0-2026-08-07` (effective `2026-08-07`, canonical source SHA-256 `a2775340dcf179e8f68b33cfa73b9d722f4787ba351999b793f893f152564f79`). Microsoft Store publication is verified in the current 2026-08-14 checkpoint.
- Website commit `5db6957ae8e7d91a060db0fee2f37cbc5e4f807e` deployed through successful GitHub Pages run `30125432522`. Cache-busted verification at `2026-07-24T20:53:53Z` returned HTTP 200 and exact expected byte counts and SHA-256 hashes for the installer, video, captions, poster, thumbnail, transcript, and manual.
- Live desktop and 390 x 844 responsive browser checks passed with no console errors. The public video decoded at 1920 x 1080, duration 58.179 seconds, ready state 4, with one English caption track.
- The previous same-version v1.1.6 website bytes remain historical evidence: artifact-publication commit `41b359e4e306dacb090da69b82e2e3de1eab2e7b`, successful Pages run `30037802828`, verification at `2026-07-23T19:28:34Z`, installer size 102,427,430 bytes, and SHA-256 `E641AB23BBFBC49A15E37C78EB62515E195D68C54815D6B1FFE533D50DC3E077`.
- Corrective validation passed `726/726` source tests, `54/54` exact-package checks, `9/9` current-display checks, `166/166` UI-humanity checks, and `14/14` runtime workflows. Physical human workflow validation is not recorded; website publication is not a human-validation pass.
- The current Organized W identity is `docs/site-data/shared/branding/wazo-logo-organized-w-r2.png`: 57,329 bytes, 256 x 256, SHA-256 `4F897AF777A8ADEB4782848E04F934B05D40F8F2A92979D75D75380E6BAC4B55`. Logo correction commit `ab4a65f06656940f3da92b02d0a9e2cc182dd769` deployed successfully through GitHub Pages run `30062852367`; live verification found HTTP 200 on the homepage, privacy page, and logo asset, with both pages referencing that asset.
- The previously published v1.1.5 installer (102,285,721 bytes, SHA-256 `94EF7F7C3456FE025689A44C228E4D8759F2AD153C12AD22B0ED81CC328D86AB`) and its rejected predecessor (102,284,642 bytes, SHA-256 `955F00602E1FE632F5F429963E396A535359907D80520A45C7DE9B23AC09A13E`) are superseded historical evidence only.
- The Microsoft Store card uses `ms-windows-store://pdp/?productid=9NKLT8DKJ1QX` and the browser fallback `https://apps.microsoft.com/detail/9NKLT8DKJ1QX`. The Store package is published; the local package hash remains historical build evidence and is not used as the public Store artifact identity.
- GitHub Pages continues to publish from `docs/` on branch `Master` under the `imzub` account.

## Product-tour state

- Status: v1.1.6 tour remains published and live-verified as historical versioned media; the current downloadable installer is v2.0.0.
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

The v2.0.0 stable installer is sourced from WAZO `Dev/QA` commit `28b0522`: 99,450,391 bytes, SHA-256 `31F44DAF38D26CDB69A42AFFE46FE473060CA239262871FA7B5A6F4BB9E44FE4`. Public HTTP/size/hash verification passed through Pages deployment `5886802524` at `2026-08-13T11:11:41Z`. Keep historical media and release evidence retained in Git; do not add the local-only Store AppX to this website repository.

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
