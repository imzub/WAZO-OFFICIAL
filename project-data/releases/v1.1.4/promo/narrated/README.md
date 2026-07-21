# WAZO Narrated Explainer — v1.1.4

This is the complete public-safe editable workspace for the accepted two-minute English WAZO product tour. It was produced from the real WAZO 1.1.4 interface at private source commit `7c63be818372307dc08ff6551b7296fca863d3e7` using an isolated anonymous demo profile.

## Layout

```text
artwork/         Logo, intro/outro cards, opener/closing checks, and QA contact sheets
audio/           Final narration, original music bed, and voice segments
capture-frames/  731 original 1920 x 1080 JPEG capture frames at 6 fps
delivery/        Accepted master, review copy, poster, and English SRT
manifests/       Original capture and production records
scripts/         Voice, live-capture, and video-build sources
```

`CHECKPOINT.md` records the accepted status and validation. `requirements.txt` pins the Python packages used by the portable scripts. The broader rebuild and publication procedure is in `../../../../context/PRODUCTION_HANDOFF.md`.

## Accepted delivery files

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `delivery/WAZO-Narrated-Explainer-v1.1.4-Master.mp4` | 164,609,325 | `A29C156218B245021B1F99E1DD4B132757032770229E888FA0D583F19DB5EE2A` |
| `delivery/WAZO-Narrated-Explainer-v1.1.4-Review.mp4` | 25,540,813 | `639D090D6C730BD583FD5FD87EA92DF3D98C6DA69C78CE53D3C090AEAC9A2723` |
| `delivery/WAZO-Narrated-Explainer-v1.1.4-Poster.png` | 520,766 | `3E5D4BD45B995AC98E02EC9017335BBDC398A2F7BAFD52393317A65D3F325379` |
| `delivery/WAZO-Narrated-Explainer-v1.1.4-English.srt` | 2,028 | `75B5FE7F969A1F8B8309FCE2AB0E6D7730F15A61267D3FA05555C40FF3B228A7` |

The public site uses the byte-identical review copy and poster under `docs/site-data/releases/v1.1.4/video/`, plus WebVTT captions and a readable transcript.

## Git LFS

The master, WAV/MP3 production audio, voice-segment audio, and all capture frames are Git LFS objects. After cloning:

```powershell
git lfs install
git lfs pull --include="project-data/releases/v1.1.4/promo/narrated/**"
```

If any of those files contains a short text pointer instead of media bytes, the LFS pull has not completed.

## Reproduction boundary

The private WAZO application source is intentionally excluded. Set `WAZO_APP_SOURCE` to an authorized checkout of commit `7c63be818372307dc08ff6551b7296fca863d3e7` before recapturing. Optional environment overrides are `WAZO_ELECTRON_PATH` and `WAZO_FFMPEG`.

The manifests in `manifests/` describe the accepted historical render and preserve its old directory layout. Their root-level delivery paths now map to `delivery/`; `WAZO-English-Narration.wav` maps to `audio/`; `source/generated/wazo-narrated-original-bed.wav` maps to `audio/wazo-narrated-original-bed.wav`; and `source/timeline.json` maps to `scripts/timeline.json`. The original FFmpeg machine path is also historical. Use `handoff-manifest.json` and the portable scripts for the current layout.
