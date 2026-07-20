# WAZO 1.1.5 Official Website Release

Status: current validated direct website installer.

WAZO 1.1.5 adds explicit in-app privacy acknowledgement, Windows-protected
app storage, safer migration for existing v1.1.4 users, and portable recovery
controls while retaining the complete personal-wealth workflow.

## Highlights

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
- Includes the 11-page WAZO 1.1.5 Windows user manual and the current privacy
  policy revision `WAZO-PP-1.1.5-2026-07-20`.

## Validation

- Automated tests: 204 passed, 0 failed.
- Installer size: 102,277,651 bytes (97.5 MiB).
- SHA-256:
  `4CD10928FB07886CE114A6029B9070B85D2BFF98D89228835CD2EBD2DD34865B`.
- Archive integrity, installer metadata, and isolated launch checks passed.
- Fresh install, same-version reinstall, existing-profile preservation, and
  uninstall checks passed.
- Authenticode status: `NotSigned`. Windows or the browser may show an unknown-
  publisher warning for the direct installer.

## Installation And Upgrade Notes

- Privacy acknowledgement is collected inside WAZO, not by the Windows
  installer.
- Existing v1.1.4 profiles, members, assets, goals, supported settings, and
  financial values do not require re-entry after successful migration.
- WAZO 1.1.4 cannot read the new v1.1.5 protected store. Create a
  password-protected portable backup before moving to another Windows account
  or computer.
- The website provides this direct installer and does not publish an automatic-
  update feed for v1.1.5. The Microsoft Store release is not yet available from
  this page.

## Platform Scope

The protection, migration, portable-backup, permanent-deletion, and online-rate
behaviors described above apply to the WAZO 1.1.5 Windows desktop release. They
do not claim equivalent Android protection.
