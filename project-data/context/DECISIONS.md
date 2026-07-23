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
