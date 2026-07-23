# WAZO 1.1.6 Official Website Release

Version/build: `1.1.6` / `1.1.6.0`

Platform: Windows x64
Channel: WAZO Official website direct installer

Publication: live and byte/hash verified on `2026-07-23T19:28:34Z` through
GitHub Pages deployment `30037802828` from artifact commit
`41b359e4e306dacb090da69b82e2e3de1eab2e7b`.

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
  `68562c0af607f5c73bd1b948beb95f5517243523`
- File: `WAZO-Setup-1.1.6.exe`
- Size: `102,427,430` bytes (`97.7 MiB`)
- SHA-256:
  `E641AB23BBFBC49A15E37C78EB62515E195D68C54815D6B1FFE533D50DC3E077`
- Authenticode: `NotSigned`
- Manual: 16 pages, `112,431` bytes, SHA-256
  `028C0233B47B44AB32C655E0F1133512CF8118E164032D700B706FB5FF66CE30`

Because the direct installer is not code-signed, Windows SmartScreen or the
browser may show an unknown-publisher warning. Download only from the WAZO
Official website and verify the file name, size, and SHA-256 above.

## Validation Record

- Closing standalone Node `v24.14.0` suite: `716/716` passed with no failures,
  cancellations, skips, or todo tests in `57.060` seconds.
- Closing coverage suite: `716/716` passed; `76.22%` lines, `75.86%` branches,
  and `86.16%` functions.
- Syntax passed for 75 source files; static analysis and brand validation
  passed.
- Focused release-hardening verification passed `35/35`; focused
  offline/storage/privacy verification passed `97/97`.
- `npm audit` reported zero known vulnerabilities across 384 dependencies.
- The exact standalone, installer payload, and Store package payload each
  passed `18/18` package checks (`54/54` total).
- Native current-display validation passed `3/3` for each exact payload
  (`9/9` total) at DPR `1.5`, CSS screen `1280 x 800`, and CSS work area
  `1280 x 752`.
- Fresh install, unchecked-policy rejection, checked retry, configured
  workspace creation, restart, same-version repair, post-repair launch, and
  uninstall passed.
- A graceful v1.1.5-to-v1.1.6 upgrade preserved 2 families, 5 members, and 11
  assets, showed the current-policy review, accepted a clean retry, and
  remained stable after restart.
- The test user data and protected-store sentinel were preserved byte-for-byte
  through repair and uninstall, with no plaintext portfolio record found.

The results above are automated evidence. Physical human workflow validation
is not recorded. The installer is unsigned. Windows App Certification Kit,
signed/sideload validation, Microsoft Partner Center upload, and Store
certification are separate external gates and are not claimed here.

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
