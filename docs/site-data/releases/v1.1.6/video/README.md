# WAZO v1.1.6 Product Tour

Public, browser-ready assets for the current English WAZO product tour.

- `WAZO-Product-Tour-v1.1.6.mp4`: 1920 × 1080 H.264/AAC web encode with Fast Start.
- `WAZO-Product-Tour-v1.1.6-Poster.png`: 1920 × 1080 playback poster.
- `WAZO-Product-Tour-v1.1.6-Thumbnail.png`: matching 1920 × 1080 thumbnail.
- `WAZO-Product-Tour-v1.1.6-English.vtt`: default English browser captions.
- `WAZO-Product-Tour-v1.1.6-Transcript.md`: accessible English transcript.
- `video.json`: exact hashes, sizes, timing, recording version, and source provenance.

The website encode was derived from the validated 364,239,785-byte Microsoft Store trailer master. The high-bitrate Store master remains preserved in the private WAZO release repository; the browser copy is kept below 100 MB and remains ordinary Git content so GitHub Pages can serve playable media rather than an LFS pointer.

The tour uses WAZO v1.1.6 with an isolated anonymous demo profile. Privacy Mode is intentionally off for clarity. It contains no real user or financial data, and its claims stay within the implemented fully offline-only v1.1.6 boundary.

The browser encode passed a complete audio/video decode and Fast Start check. Frame-by-frame comparison with the Store master measured all-plane SSIM `0.999938` and average PSNR `71.668123 dB`. These are automated media checks (`humanValidated=false`).
