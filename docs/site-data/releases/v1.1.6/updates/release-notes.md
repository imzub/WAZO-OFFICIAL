# WAZO 1.1.6 Official Website Release

Version/build: `1.1.6` / `1.1.6.0`

Platform: Windows x64
Channel: WAZO Official website direct installer

Corrective refresh prepared: `2026-07-25`.

The previous v1.1.6 website binary was published and byte/hash verified on
`2026-07-23T19:28:34Z` through GitHub Pages deployment `30037802828`. The
corrective build below supersedes those binary bytes without changing the
`1.1.6` product version or `1.1.6.0` build version. Its public deployment and
download verification are recorded separately after GitHub Pages publishes the
replacement.

Website branding correction: the public header, footer, favicon, and Privacy
Policy page now use the current Organized W logo through a cache-busted
website asset. This presentation-only correction does not change the WAZO
`1.1.6` product version or `1.1.6.0` build version.

Corrective reliability refresh: source commit
`56399c120c644c1d80485b368370e630c58f6ac7` improves transient status cleanup,
form alignment and responsive behavior, theme legibility, Privacy Mode
redaction, regional-format display, valuation preservation, and human-scale
runtime validation without deferring an agreed item to a later release.

WAZO 1.1.6 is a permanently offline personal wealth organizer. Portfolio
records, calculations, guidance, prices, and rates remain on the user's
computer. The app has no cloud portfolio service, synchronization, market-data
or financial API, cloud AI, telemetry, advertising request, or background
portfolio upload.

## Highlights

- Adds a ten-step, scroll-safe first setup with privacy acknowledgement, live
  theme preview, one or more family members, optional dates of birth,
  configurable financial year and currency, an optional first goal, optional
  local English audio guidance, optional Zakat, and a final review.
- Adds configurable financial-year boundaries for global use, including
  January-to-December, April-to-March, and custom recurring start dates.
- Adds optional member-specific risk assessments with educational,
  evidence-linked observations and a clear reminder to consult a qualified
  financial professional before acting.
- Adds the deterministic local WAZO Guide for page-aware help and navigation.
  It does not use cloud AI, upload prompts, or change financial records without
  an explicit preview and confirmation.
- Adds local English audio guidance using installed Windows voices. It is off
  by default, has no microphone or cloud-speech path, does not speak entered
  personal or financial values, and stops in Privacy Mode.
- Makes ordinary record removal recoverable through Data Lifecycle & Trash.
  Confirmed financial history remains auditable through corrections, voids,
  and reversals rather than destructive edits.
- Supports reversible sale, redemption, theft, loss, destruction, company
  collapse/total loss, disposal, and later reacquisition workflows.
- Lets users review, confirm, or delete multiple Pending Investment Reviews.
- Adds compact importable `.wz` backups with optional password protection,
  privacy-safe restore preview, integrity validation, and a protected recovery
  point before replacement. Legacy `.wazo-backup` files remain readable.
- Adds Trust Center & Data Health, protected recovery verification, local CSV
  reconciliation preview, calculation details, ownership completeness, and
  household resilience observations.
- Keeps prices, rates, valuations, and FX evidence user-maintained locally.
  Missing evidence fails closed for review instead of triggering a network
  fallback.
- Uses `Fees, Taxes & Handling Charges` consistently and adds `Other` to the
  Record Sale or Asset Loss outcome list.
- Expands the anonymous demo with an active monthly SIP, confirmed
  transactions, pending occurrences, and additional investment activity.

## Privacy And Local Protection

- The in-app privacy acknowledgement is not selected in advance. If it is not
  selected, WAZO shows one local message, makes no data change, and allows a
  clean retry.
- App-managed active Windows data is protected with authenticated encryption
  and a key bound to the current Windows user through Windows protection.
- Privacy Mode structurally redacts sensitive screen, report, print, export,
  accessibility, Guide, CSV, calculation, and audio surfaces.
- Explicit website, Store, LinkedIn, policy, and support-email actions are
  user-initiated operating-system handoffs and do not attach portfolio data.
- Privacy policy revision:
  `WAZO-PP-1.1.6-2026-07-23-R2`, effective July 23, 2026.

## Verified Installer

- Product source commit:
  `56399c120c644c1d80485b368370e630c58f6ac7`
- File: `WAZO-Setup-1.1.6.exe`
- Size: `102,429,605` bytes (`97.7 MiB`)
- SHA-256:
  `A4BAB97F8D252FA95F586B98CB59BF123FE1F91C3BFA3CA52B7B6DCD807DE6F7`
- Authenticode: `NotSigned`
- Manual: 16 pages, `112,431` bytes, SHA-256
  `028C0233B47B44AB32C655E0F1133512CF8118E164032D700B706FB5FF66CE30`

Because the direct installer is not code-signed, Windows SmartScreen or the
browser may show an unknown-publisher warning. Download only from the WAZO
Official website and verify the file name, size, and SHA-256 above.

## Validation Record

- Closing standalone Node suite: `726/726` passed with no failures,
  cancellations, skips, or todo tests in `52.533` seconds.
- Closing coverage suite: `726/726` passed; `76.23%` lines, `75.90%` branches,
  and `86.16%` functions.
- Syntax passed for 78 source files; static analysis, brand validation, and
  Trust Center validation
  passed.
- UI-humanity validation passed `166/166`; runtime workflow validation passed
  `14/14`; calculator/settings Electron validation passed `30/30`; focused
  calculator/settings tests passed `86/86`; lifecycle/recovery passed `20/20`;
  and deterministic file workflows passed `21/21`.
- The exact standalone, installer payload, and Store package payload each
  passed `18/18` package checks (`54/54` total).
- Native current-display validation passed `3/3` for each exact payload
  (`9/9` total) at DPR `1.5`, CSS screen `1280 x 720`, and CSS work area
  `1280 x 672`.
- The installer was extracted directly and its 76-file application payload was
  byte-for-byte identical to the validated standalone payload. A clean full
  rerun passed `18/18`.
- Native Print cancellation cannot be concluded from automation because the
  operating-system dialog is intentionally outside the app harness.

The results above are automated evidence. Physical human workflow validation
is not recorded. A physical install/repair/uninstall lifecycle was not rerun for
this replacement candidate because it uses the same per-user product identity;
the exact extracted payload was validated instead. The installer is unsigned.
Windows App Certification Kit, signed/sideload validation, Microsoft Partner
Center upload, and Store certification are separate external gates and are not
claimed here.

## Current Product Tour

- Recording version: WAZO `1.1.6`, source commit
  `56399c120c644c1d80485b368370e630c58f6ac7`.
- Runtime: `58.17` seconds at `1920 x 1080`, with English narration, original
  music, and nine English WebVTT caption cues.
- Browser MP4: `24,372,012` bytes, SHA-256
  `6B79ED9EC177C0182AD7FF44641EEDE55898A9D228F0A921ED796C853E3F1533`.
- The website copy was transcoded from the validated 364,239,785-byte Store
  master with SHA-256
  `3C0D867D007FF20607DDB7209A9EA9DFB78631C5959BC7B4992FDFAA50AD584F`.
- The video uses an isolated anonymous demo profile. Privacy Mode is
  intentionally off for presentation clarity; no real user or financial data
  appears.

## Installation And Upgrade Notes

- Privacy acknowledgement is collected inside WAZO, not by the Windows
  installer.
- Existing supported v1.1.5 profiles, members, assets, definitions, plans,
  transactions, goals, optional Zakat data/settings, themes, presets, backups,
  and logs are intended to remain available without re-entry.
- Create a portable `.wz` backup before moving data to another Windows account
  or computer. Windows-bound protected recovery is not a portable backup.
- This website channel provides a direct installer only. WAZO does not include
  an automatic-update client, so this release does not publish `latest.yml`, a
  blockmap, or another automatic-update feed.
- Microsoft Store availability is not claimed until its listing is separately
  published and verified.
