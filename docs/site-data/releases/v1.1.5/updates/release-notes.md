# WAZO 1.1.5 Official Website Release

Status: current official-website direct installer, published July 21, 2026. Automated release validation passed; physical human workflow validation has not been recorded.

WAZO 1.1.5 adds explicit in-app privacy acknowledgement, Windows-protected
app storage, safer migration for existing v1.1.4 users, and portable recovery
controls while retaining the complete personal-wealth workflow. This corrected
same-version installer also includes the completed calculation and full-app
reliability work and is the current website download.

## Highlights

- Adds a deterministic financial-calculation test matrix and corrects edge
  cases in SIP/SWP, FIRE, Zakat projection and allocation, date arithmetic,
  explicit zero values, CAGR/XIRR eligibility, and transferred-asset history.
- Strengthens recurring-plan review, household compatibility recovery,
  backup/delete containment, privacy-safe charts, and sortable-table
  accessibility without changing the data schema or release version.
- Adds a seven-step first setup. The privacy acknowledgement is not selected in
  advance and is required before WAZO stores real personal or financial data.
  Users can continue later with anonymous demo data.
- Protects app-managed active Windows data, settings, logs, transaction
  generations, and recovery points with authenticated encryption and a key
  bound through Windows DPAPI.
- Gives existing v1.1.4 users a one-time privacy review before a validated,
  backup-first migration. Exiting before acknowledgement leaves the earlier
  store unchanged.
- Adds password-protected portable `.wazo-backup` files for transfer or device
  recovery, plus protected automatic recovery, reset-to-demo, and an explicit
  permanent local-deletion control.
- Warns before creating readable exports outside WAZO. Optional online rates
  remain off by default and require a separate disclosure.
- Includes the 12-page WAZO 1.1.5 Windows user manual and the current privacy
  policy revision `WAZO-PP-1.1.5-2026-07-20`.

## Current Installer Identity And Validation

- Product source commit:
  `0f03c6084ab023cd14841158bd369461163ac319`.
- Installer size: 102,285,721 bytes (97.5 MiB).
- SHA-256:
  `94EF7F7C3456FE025689A44C228E4D8759F2AD153C12AD22B0ED81CC328D86AB`.
- Final source syntax, static-analysis, and brand checks passed.
- The full automated test suite passed `245/245` in `25.9s`.
- The clean rerun of the default source-startup gate passed `12/12` in
  `148.5s`.
- The exact corrected NSIS/website-installer payload matrix passed `18/18`;
  its detailed evidence is retained in the private product-release handoff.
- Native-current-display browser/CDP interaction against the exact corrected
  NSIS/website-installer payload passed `3/3` fresh, legacy, and lifecycle
  scenarios at DPR `1.5` (CSS screen `1280 x 800`, work area `1280 x 752`,
  physical display `1920 x 1200`) in `104.4s`. Windows `IsZoomed` separately
  attested maximized state at the flow endpoints and all five lifecycle
  checkpoints.
- That native-display result is automated evidence only: `humanValidated=false`.
- Automated evidence does not substitute for physical human workflow testing.
- Physical packaged human-interaction validation: `not recorded`.
- Official-website publication was explicitly authorized on July 21, 2026;
  publication is not recorded as a physical human-validation pass.
- Authenticode status: `NotSigned`. Windows or the browser may show an unknown-
  publisher warning when downloading or installing this direct release.

## Previously Published Candidate — Historical Evidence

- The previously published remote installer was the rejected and superseded
  102,284,642-byte candidate with SHA-256
  `955F00602E1FE632F5F429963E396A535359907D80520A45C7DE9B23AC09A13E`.
- Its product source commit was
  `232210ba29904c9f3badf54d0650edc6c721a1b1`.
- Those facts remain documented for traceability only; they are not validation
  evidence for the corrected candidate.

## Installation And Upgrade Notes

- Privacy acknowledgement is collected inside WAZO, not by the Windows
  installer.
- Download the current installer from the official WAZO website. Because the
  installer is not code-signed, Windows or the browser may display an unknown-
  publisher warning; verify the SHA-256 above if needed.
- Existing v1.1.4 profiles, members, assets, goals, supported settings, and
  financial values do not require re-entry after successful migration.
- WAZO 1.1.4 cannot read the new v1.1.5 protected store. Create a
  password-protected portable backup before moving to another Windows account
  or computer.
- This website release provides only the direct installer; it does not publish
  `latest.yml`, a blockmap, or another automatic-update feed. The Microsoft
  Store release is not yet available from this page.

## Platform Scope

The protection, migration, portable-backup, permanent-deletion, and online-rate
behaviors described above apply to the WAZO 1.1.5 Windows desktop release. They
do not claim equivalent Android protection.
