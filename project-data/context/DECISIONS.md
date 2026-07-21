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
