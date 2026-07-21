# Narrated Explainer Production Handoff

This guide rebuilds or extends the accepted WAZO 1.1.4 English explainer without relying on the original `G:` drive layout.

## Prerequisites

- Windows 10 or 11 with Segoe UI fonts.
- Python 3.12 or a compatible current Python.
- Node.js 24 or a compatible release with a built-in WebSocket client.
- FFmpeg 7.x with `framerate`, `sidechaincompress`, and `overlay` filters.
- An authorized checkout of the private WAZO application at commit `7c63be818372307dc08ff6551b7296fca863d3e7`.
- The private app's Node dependencies installed so its Electron executable is available.
- At least 450 MiB of free working space before a full render; more is recommended.

Install Python requirements from the narrated workspace:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Configure machine-specific locations

Run these commands from `project-data/releases/v1.1.4/promo/narrated/`, replacing the example private-app path:

```powershell
$env:WAZO_APP_SOURCE = "D:\Work\WAZO"
$env:WAZO_ELECTRON_PATH = "$env:WAZO_APP_SOURCE\node_modules\electron\dist\electron.exe"
```

`build_narrated.py` and `generate_voice.py` locate FFmpeg in this order: `WAZO_FFMPEG`, `ffmpeg` on `PATH`, then the `imageio-ffmpeg` package. Set an override only when needed:

```powershell
$env:WAZO_FFMPEG = "D:\Tools\ffmpeg.exe"
```

## Rebuild order

The accepted generated narration, capture frames, and outputs are already preserved. Run only the phases you intend to replace.

1. Regenerate English voice, subtitles, and timeline. This uses Microsoft Edge TTS and therefore needs an internet connection.

   ```powershell
   python scripts/generate_voice.py
   ```

2. Recapture the app interface from the separately authorized private source checkout.

   ```powershell
   node scripts/capture_walkthrough.js
   ```

3. Validate inputs and FFmpeg capabilities.

   ```powershell
   python scripts/build_narrated.py --check
   ```

4. Render the high-quality master, review copy, poster, soundtrack, subtitles, and production manifest.

   ```powershell
   python scripts/build_narrated.py
   ```

## Publication workflow

Do not replace the public website MP4 until the new review copy has been watched end-to-end and its claims match the application version shown.

After acceptance:

1. Copy the accepted review MP4, poster, SRT, and derived VTT/transcript into the matching version under `docs/site-data/releases/`.
2. Update the version's `release.json`, `docs/site-data/releases/index.json`, the public `video.json`, checksums, and this context together.
3. Keep the web MP4 as ordinary Git data. Keep the master, WAV/MP3 files, and capture frames under Git LFS.
4. Validate local links, captions, aspect ratio, JSON, media hashes, full video decoding, and Git LFS attributes.
5. Commit and push with the `imzub` account, then verify the deployed Pages HTML and video response.

## Security and product-claim guardrails

- Never copy the private app source into this public repository.
- Never use installed user profiles or real financial data for capture.
- WAZO 1.1.4 Privacy Mode is shown as concealment/redaction; the video must not be described as demonstrating WAZO 1.1.5 protected-storage internals.
- Keep optional online rates represented as opt-in.
- Keep zakat represented as optional, not as the sole purpose of WAZO.
- Do not expose local storage paths, credentials, browser sessions, native file dialogs, or destructive actions.

The original production manifest is retained as historical evidence and uses the old workspace layout. Map its root delivery filenames to `delivery/`, narration to `audio/`, `source/generated/wazo-narrated-original-bed.wav` to `audio/wazo-narrated-original-bed.wav`, and `source/timeline.json` to `scripts/timeline.json`. Its absolute FFmpeg path is also historical. The portable scripts and `handoff-manifest.json` do not depend on those old paths.
