# WAZO Website and Media Decisions

## 2026-07-21 narrated-tour publication

1. Keep the website, installer, privacy policy, and release index on WAZO `1.1.5`. Adding a video does not justify a product version bump.
2. Label the accepted tour as recorded from WAZO `1.1.4`. Add an explicit note that 1.1.5 preserves the shown core workflows and adds guided privacy setup and protected Windows storage.
3. Place the tour after the compact capability summary and before the 1.1.5 changes. This explains the product before presenting release-specific improvements.
4. Use native video controls with no autoplay, a 16:9 responsive container, poster, default English captions, fallback download, and a full transcript.
5. Keep the 25 MB web review MP4 in ordinary Git under `docs/`; GitHub Pages cannot serve an LFS pointer as a playable video.
6. Preserve the exact 165 MB master, narration, original music bed, voice segments, scripts, manifests, artwork, and all 731 capture frames under versioned `project-data/`, using Git LFS for the largest/editable binary groups.
7. Retain older release material. Do not overwrite a prior version when a later video or installer is produced.
8. Do not publish the private WAZO application source or dependencies. Record the exact source commit and require a separate authorized checkout for reproduction.
9. Treat the current explainer as accepted, not final forever. Future visual and narration polish belongs in a new revision or versioned media folder after review.
10. Always use the `imzub` GitHub account for WAZO operations without asking the user to select between saved accounts.

## 2026-07-23 offline-only policy publication

1. WAZO `1.1.6` and later are permanently offline-only. Do not plan or advertise cloud storage, synchronization, market-data or financial APIs, cloud AI, telemetry, advertising requests, or background portfolio uploads.
2. Keep prices, rates, guidance, analysis, and the WAZO Guide local. External website, Store, LinkedIn, policy, and email links remain explicit user-initiated handoffs and do not attach portfolio data.
3. Publish the reviewed policy revision `WAZO-PP-1.1.6-2026-07-23-R2` at the stable `/privacy/` route with canonical source SHA-256 `0f792e634eec910e6c248575a2497301544ce8e85b9bd45a16827b2ec7a43150`.
4. This policy publication does not promote a product binary. Keep the public website release, release index, and direct installer at verified WAZO `1.1.5` until the separate `1.1.6` release is approved.

## 2026-07-23 WAZO 1.1.6 website publication

1. The July 21 narrated-tour and July 23 policy-only entries above are preserved as dated historical decisions; their temporary v1.1.5 current-release boundary was superseded when v1.1.6 publication was explicitly authorized.
2. Promote WAZO `1.1.6` / build `1.1.6.0` to the current website release and direct installer while retaining all v1.1.5 artifacts and identities as historical evidence.
3. Publish only the exact 102,427,430-byte installer with SHA-256 `E641AB23BBFBC49A15E37C78EB62515E195D68C54815D6B1FFE533D50DC3E077` from private product source commit `68562c0af607f5c73bd1b948beb95f5517243523`.
4. Keep the v1.1.6 installer, 16-page manual, release notes, release manifest, release index, and privacy revision synchronized. Website artifact-publication commit `41b359e4e306dacb090da69b82e2e3de1eab2e7b` deployed through GitHub Pages run `30037802828`.
5. Continue to label automated validation separately from physical human validation; `humanValidated=false` remains the recorded state.

## 2026-07-24 Organized W website identity

1. Use `docs/site-data/shared/branding/wazo-logo-organized-w-r2.png` as the current header, footer, favicon, release-manifest, and privacy-page identity.
2. Preserve `wazo-logo.png` only as a legacy asset; do not restore it to current public pages.
3. Logo correction commit `ab4a65f06656940f3da92b02d0a9e2cc182dd769` deployed successfully through GitHub Pages run `30062852367`. The live homepage, privacy page, and 57,329-byte, 256 x 256 logo asset returned HTTP 200; the asset SHA-256 is `4F897AF777A8ADEB4782848E04F934B05D40F8F2A92979D75D75380E6BAC4B55`.

## 2026-07-24 Microsoft Store trailer direction

1. Keep the accepted 121.72-second WAZO v1.1.4 narrated explainer available on the website as explicitly labeled historical visual evidence.
2. Do not attach that recording to the v1.1.6 Microsoft Store draft: it exceeds Microsoft's recommended 60-second trailer length and shows older UI, branding, and the removed optional-rates workflow.
3. A future Store trailer should be a fresh 45-60 second v1.1.6-specific production using the current Organized W identity, current offline-only UI and claims, a 1920 x 1080 Store-compliant video and PNG thumbnail, an accurate title, and English WebVTT captions.
4. Trailer production and upload are separate future media work. Submission 4 remains intentionally trailer-free unless the current release-specific trailer is created, validated, and explicitly approved.
