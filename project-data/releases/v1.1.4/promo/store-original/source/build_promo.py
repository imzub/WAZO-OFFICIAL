from __future__ import annotations

import math
import os
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont


WIDTH = 1920
HEIGHT = 1080
FPS = 30000 / 1001
VERSION = "1.1.4"
TRANSITION = 0.8
DURATIONS = [5.0, 8.0, 8.0, 8.0, 8.0, 8.0, 6.0]
TOTAL_DURATION = sum(DURATIONS) - TRANSITION * (len(DURATIONS) - 1)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FRAMES_DIR = PROJECT_ROOT / "frames"
ASSET_ROOT = Path(r"G:\iZ\WAZO-OFFICIAL\docs\site-data")
IMAGE_ROOT = ASSET_ROOT / "releases" / f"v{VERSION}" / "images"
LOGO_PATH = ASSET_ROOT / "shared" / "branding" / "wazo-logo.png"
FFMPEG = Path(
    os.environ.get(
        "WAZO_FFMPEG",
        r"G:\iZ\WAZO-PROMO\.tools\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe",
    )
)

REGULAR = Path(r"C:\Windows\Fonts\segoeui.ttf")
SEMIBOLD = Path(r"C:\Windows\Fonts\seguisb.ttf")
BOLD = Path(r"C:\Windows\Fonts\segoeuib.ttf")


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size=size)


def gradient_background() -> Image.Image:
    y, x = np.mgrid[0:HEIGHT, 0:WIDTH]
    nx = x / WIDTH
    ny = y / HEIGHT
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    base[..., 0] = 7 + 10 * nx + 8 * (1 - ny)
    base[..., 1] = 8 + 16 * nx + 8 * (1 - ny)
    base[..., 2] = 37 + 42 * nx + 27 * (1 - ny)

    for cx, cy, radius, color, strength in [
        (0.24, 0.34, 0.46, (88, 44, 255), 0.78),
        (0.76, 0.68, 0.50, (0, 144, 255), 0.52),
        (0.54, 0.08, 0.28, (174, 78, 255), 0.36),
    ]:
        dist = ((nx - cx) ** 2 + (ny - cy) ** 2) ** 0.5
        glow = np.clip(1 - dist / radius, 0, 1) ** 2 * strength
        for channel, value in enumerate(color):
            base[..., channel] += glow * value

    vignette = np.clip(1 - 0.78 * (((nx - 0.5) / 0.72) ** 2 + ((ny - 0.5) / 0.72) ** 2), 0.36, 1)
    base *= vignette[..., None]
    return Image.fromarray(np.uint8(np.clip(base, 0, 255)), "RGB")


def add_brand_texture(image: Image.Image) -> None:
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for x in range(0, WIDTH, 96):
        draw.line((x, 0, x, HEIGHT), fill=(136, 149, 255, 13), width=1)
    for y in range(0, HEIGHT, 96):
        draw.line((0, y, WIDTH, y), fill=(136, 149, 255, 13), width=1)

    points = [
        (0, 810),
        (180, 762),
        (342, 824),
        (530, 686),
        (724, 734),
        (918, 590),
        (1110, 640),
        (1326, 472),
        (1515, 518),
        (1730, 336),
        (1920, 386),
    ]
    draw.line(points, fill=(119, 109, 255, 52), width=4, joint="curve")
    for x, y in points[1:-1]:
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=(185, 179, 255, 90))

    for radius, alpha in [(330, 16), (245, 22), (160, 28)]:
        draw.ellipse(
            (WIDTH - 340 - radius, -160 - radius, WIDTH - 340 + radius, -160 + radius),
            outline=(112, 174, 255, alpha),
            width=2,
        )
    image.paste(overlay, (0, 0), overlay)


def paste_with_shadow(canvas: Image.Image, asset: Image.Image, xy: tuple[int, int], blur: int = 28) -> None:
    x, y = xy
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    alpha = asset.getchannel("A") if asset.mode == "RGBA" else Image.new("L", asset.size, 255)
    shadow_shape = Image.new("RGBA", asset.size, (34, 13, 96, 205))
    shadow_shape.putalpha(alpha)
    shadow.paste(shadow_shape, (x, y + 18), shadow_shape)
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    canvas.paste(shadow, (0, 0), shadow)
    canvas.paste(asset, (x, y), asset)


def centered_text(draw: ImageDraw.ImageDraw, text: str, y: int, text_font: ImageFont.FreeTypeFont, fill: tuple[int, ...]) -> None:
    box = draw.textbbox((0, 0), text, font=text_font)
    width = box[2] - box[0]
    draw.text(((WIDTH - width) // 2, y), text, font=text_font, fill=fill)


def make_opener() -> Image.Image:
    canvas = gradient_background().convert("RGBA")
    add_brand_texture(canvas)
    draw = ImageDraw.Draw(canvas)

    logo = Image.open(LOGO_PATH).convert("RGBA")
    logo.thumbnail((230, 230), Image.Resampling.LANCZOS)
    paste_with_shadow(canvas, logo, ((WIDTH - logo.width) // 2, 172), blur=38)

    centered_text(draw, "WAZO", 430, font(BOLD, 142), (255, 255, 255, 255))
    centered_text(draw, "Your personalized wealth organizer", 592, font(REGULAR, 44), (220, 225, 255, 255))

    pill_text = f"INTRODUCING {VERSION}"
    pill_font = font(SEMIBOLD, 26)
    pill_box = draw.textbbox((0, 0), pill_text, font=pill_font)
    pill_width = pill_box[2] - pill_box[0] + 58
    pill_x = (WIDTH - pill_width) // 2
    draw.rounded_rectangle((pill_x, 690, pill_x + pill_width, 748), radius=29, fill=(111, 86, 232, 210), outline=(174, 190, 255, 150), width=2)
    draw.text((pill_x + 29, 703), pill_text, font=pill_font, fill=(255, 255, 255, 255))

    centered_text(draw, "Your wealth. Organized privately.", 814, font(SEMIBOLD, 48), (255, 255, 255, 255))
    return canvas.convert("RGB")


def make_end_card() -> Image.Image:
    canvas = gradient_background().convert("RGBA")
    add_brand_texture(canvas)
    draw = ImageDraw.Draw(canvas)

    logo = Image.open(LOGO_PATH).convert("RGBA")
    logo.thumbnail((184, 184), Image.Resampling.LANCZOS)
    paste_with_shadow(canvas, logo, ((WIDTH - logo.width) // 2, 132), blur=34)

    centered_text(draw, "WAZO 1.1.4", 350, font(BOLD, 106), (255, 255, 255, 255))
    centered_text(draw, "Private. Offline-first. Built for Windows.", 500, font(SEMIBOLD, 50), (231, 235, 255, 255))

    cta = "GET WAZO ON MICROSOFT STORE"
    cta_font = font(SEMIBOLD, 29)
    box = draw.textbbox((0, 0), cta, font=cta_font)
    cta_width = box[2] - box[0] + 74
    cta_x = (WIDTH - cta_width) // 2
    cta_y = 642
    draw.rounded_rectangle((cta_x, cta_y, cta_x + cta_width, cta_y + 72), radius=18, fill=(87, 66, 213, 245), outline=(169, 184, 255, 190), width=2)
    draw.text((cta_x + 37, cta_y + 17), cta, font=cta_font, fill=(255, 255, 255, 255))

    centered_text(draw, "imzub.github.io/WAZO-OFFICIAL", 782, font(REGULAR, 32), (184, 204, 255, 255))
    centered_text(draw, "Organize clearly. Stay in control.", 898, font(REGULAR, 28), (183, 189, 225, 255))
    return canvas.convert("RGB")


def fit_1080(image: Image.Image) -> Image.Image:
    image = image.convert("RGB")
    scale = max(WIDTH / image.width, HEIGHT / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - WIDTH) // 2
    top = (resized.height - HEIGHT) // 2
    return resized.crop((left, top, left + WIDTH, top + HEIGHT))


def make_soundtrack(path: Path) -> None:
    sample_rate = 48_000
    sample_count = int(round(TOTAL_DURATION * sample_rate))
    t = np.arange(sample_count, dtype=np.float64) / sample_rate
    left = np.zeros(sample_count, dtype=np.float64)
    right = np.zeros(sample_count, dtype=np.float64)

    chord_roots = [146.83, 174.61, 130.81, 196.00, 146.83, 174.61, 130.81]
    starts = [0.0]
    for index in range(1, len(DURATIONS)):
        starts.append(starts[-1] + DURATIONS[index - 1] - TRANSITION)

    for index, (start, duration, root) in enumerate(zip(starts, DURATIONS, chord_roots)):
        start_i = int(start * sample_rate)
        end_i = min(sample_count, int((start + duration) * sample_rate))
        local_t = np.arange(end_i - start_i, dtype=np.float64) / sample_rate
        attack = np.clip(local_t / 1.4, 0, 1)
        release = np.clip((duration - local_t) / 1.6, 0, 1)
        envelope = np.sin(np.minimum(attack, release) * math.pi / 2) ** 2
        chord = [root / 2, root, root * 1.5, root * 2.0]
        pad_l = np.zeros_like(local_t)
        pad_r = np.zeros_like(local_t)
        for harmonic_index, frequency in enumerate(chord):
            level = [0.32, 0.23, 0.15, 0.10][harmonic_index]
            drift = 0.0025 * np.sin(2 * math.pi * (0.07 + harmonic_index * 0.013) * local_t)
            pad_l += level * np.sin(2 * math.pi * frequency * (1 + drift) * local_t + harmonic_index * 0.7)
            pad_r += level * np.sin(2 * math.pi * frequency * (1 - drift) * local_t + harmonic_index * 0.7 + 0.18)
        left[start_i:end_i] += 0.17 * envelope * pad_l
        right[start_i:end_i] += 0.17 * envelope * pad_r

    notes = [293.66, 349.23, 440.00, 523.25, 440.00, 349.23, 293.66, 392.00]
    for beat, start in enumerate(np.arange(1.2, TOTAL_DURATION - 0.5, 0.75)):
        frequency = notes[beat % len(notes)]
        start_i = int(start * sample_rate)
        length = min(sample_count - start_i, int(0.52 * sample_rate))
        local_t = np.arange(length, dtype=np.float64) / sample_rate
        envelope = np.exp(-5.8 * local_t) * np.sin(np.clip(local_t / 0.045, 0, 1) * math.pi / 2)
        tone = np.sin(2 * math.pi * frequency * local_t) + 0.22 * np.sin(2 * math.pi * frequency * 2 * local_t)
        pan = 0.30 + 0.40 * ((beat % 5) / 4)
        left[start_i:start_i + length] += 0.055 * (1 - pan / 2) * envelope * tone
        right[start_i:start_i + length] += 0.055 * (0.5 + pan / 2) * envelope * tone

    for start in np.arange(0.0, TOTAL_DURATION, 2.0):
        start_i = int(start * sample_rate)
        length = min(sample_count - start_i, int(0.44 * sample_rate))
        local_t = np.arange(length, dtype=np.float64) / sample_rate
        thump = np.sin(2 * math.pi * (56 - 22 * local_t) * local_t) * np.exp(-10 * local_t)
        left[start_i:start_i + length] += 0.065 * thump
        right[start_i:start_i + length] += 0.065 * thump

    rng = np.random.default_rng(114)
    for start in starts[1:]:
        start_i = max(0, int((start - 0.45) * sample_rate))
        length = min(sample_count - start_i, int(0.9 * sample_rate))
        local_t = np.arange(length, dtype=np.float64) / sample_rate
        envelope = np.sin(np.pi * np.clip(local_t / 0.9, 0, 1)) ** 2
        noise = rng.normal(0, 1, length)
        smooth = np.convolve(noise, np.ones(28) / 28, mode="same")
        sweep = smooth * envelope * (0.4 + 0.6 * local_t / 0.9)
        left[start_i:start_i + length] += 0.055 * sweep
        right[start_i:start_i + length] += 0.055 * sweep[::-1]

    master = np.stack([left, right], axis=1)
    fade = int(1.4 * sample_rate)
    master[:fade] *= np.linspace(0, 1, fade)[:, None]
    master[-fade:] *= np.linspace(1, 0, fade)[:, None]
    peak = max(1e-9, float(np.max(np.abs(master))))
    master = np.clip(master * (0.48 / peak), -1, 1)
    pcm = np.int16(master * 32767)

    with wave.open(str(path), "wb") as output:
        output.setnchannels(2)
        output.setsampwidth(2)
        output.setframerate(sample_rate)
        output.writeframes(pcm.tobytes())


def timestamp(seconds: float) -> str:
    milliseconds = int(round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, milliseconds = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{milliseconds:03d}"


def make_captions(path: Path) -> None:
    cues = [
        (0.0, 4.2, "WAZO. Your wealth, organized privately."),
        (4.2, 11.4, "See your whole financial life clearly."),
        (11.4, 18.6, "One workspace for every asset."),
        (18.6, 25.8, "Define once. Organize everything."),
        (25.8, 33.0, "See what your wealth is doing."),
        (33.0, 40.2, "Private by design. Powerful by choice."),
        (40.2, TOTAL_DURATION, "WAZO 1.1.4. Private, offline-first, and built for Windows."),
    ]
    lines = ["WEBVTT", ""]
    for index, (start, end, text) in enumerate(cues, start=1):
        lines.extend([str(index), f"{timestamp(start)} --> {timestamp(end)}", text, ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def create_assets() -> list[Path]:
    FRAMES_DIR.mkdir(parents=True, exist_ok=True)
    opener = FRAMES_DIR / "00-opener.png"
    ender = FRAMES_DIR / "06-end-card.png"
    thumbnail = PROJECT_ROOT / f"WAZO-Promo-Thumbnail-v{VERSION}.png"
    soundtrack = PROJECT_ROOT / "source" / "wazo-original-ambient.wav"
    captions = PROJECT_ROOT / f"WAZO-Promo-Captions-v{VERSION}.vtt"

    make_opener().save(opener, optimize=True)
    make_end_card().save(ender, optimize=True)
    fit_1080(Image.open(IMAGE_ROOT / f"wazo-hero-v{VERSION.replace('.', '')}.png")).save(thumbnail, optimize=True)
    make_soundtrack(soundtrack)
    make_captions(captions)

    source_images = [
        opener,
        IMAGE_ROOT / f"wazo-hero-v{VERSION.replace('.', '')}.png",
        IMAGE_ROOT / f"wazo-assets-investments-v{VERSION.replace('.', '')}.png",
        IMAGE_ROOT / f"wazo-asset-library-v{VERSION.replace('.', '')}.png",
        IMAGE_ROOT / f"wazo-performance-reports-v{VERSION.replace('.', '')}.png",
        IMAGE_ROOT / f"wazo-privacy-backup-v{VERSION.replace('.', '')}.png",
        ender,
    ]
    for source in source_images:
        if not source.exists():
            raise FileNotFoundError(source)
    return source_images


def build_filter() -> tuple[str, str]:
    filters: list[str] = []
    zoom_rates = [0.00013, 0.00010, 0.00012, 0.00011, 0.00012, 0.00010, 0.00013]
    pans = [0.50, 0.48, 0.54, 0.46, 0.52, 0.48, 0.50]
    for index, (duration, zoom_rate, pan) in enumerate(zip(DURATIONS, zoom_rates, pans)):
        frames = int(math.ceil(duration * FPS))
        x_expr = f"(iw-iw/zoom)*{pan}"
        filters.append(
            f"[{index}:v]scale=2304:1296:force_original_aspect_ratio=increase,"
            f"crop=2304:1296,setsar=1,"
            f"zoompan=z='min(1+on*{zoom_rate},1.045)':x='{x_expr}':y='(ih-ih/zoom)/2':"
            f"d={frames}:s={WIDTH}x{HEIGHT}:fps=30000/1001,format=yuv420p[v{index}]"
        )

    previous = "v0"
    cumulative = DURATIONS[0]
    for index in range(1, len(DURATIONS)):
        offset = cumulative - TRANSITION * index
        output = f"x{index}"
        filters.append(
            f"[{previous}][v{index}]xfade=transition=fade:duration={TRANSITION}:offset={offset:.3f}[{output}]"
        )
        previous = output
        cumulative += DURATIONS[index]

    filters.append(
        f"[{len(DURATIONS)}:a]atrim=0:{TOTAL_DURATION:.3f},"
        "afade=t=in:st=0:d=1.2,"
        f"afade=t=out:st={TOTAL_DURATION - 1.4:.3f}:d=1.4,"
        "loudnorm=I=-16:TP=-1.5:LRA=8[aout]"
    )
    return ";".join(filters), previous


def render(source_images: list[Path]) -> None:
    if not FFMPEG.exists():
        raise FileNotFoundError(f"FFmpeg was not found at {FFMPEG}")

    soundtrack = PROJECT_ROOT / "source" / "wazo-original-ambient.wav"
    master = PROJECT_ROOT / f"WAZO-Promo-v{VERSION}-Store-Master.mp4"
    review = PROJECT_ROOT / f"WAZO-Promo-v{VERSION}-Review.mp4"
    filter_complex, final_label = build_filter()

    command = [str(FFMPEG), "-y"]
    for source in source_images:
        command.extend(["-i", str(source)])
    command.extend(["-i", str(soundtrack)])
    command.extend(
        [
            "-filter_complex",
            filter_complex,
            "-map",
            f"[{final_label}]",
            "-map",
            "[aout]",
            "-t",
            f"{TOTAL_DURATION:.3f}",
            "-c:v",
            "libx264",
            "-profile:v",
            "high",
            "-level:v",
            "4.2",
            "-preset",
            "slow",
            "-b:v",
            "50M",
            "-maxrate",
            "50M",
            "-bufsize",
            "100M",
            "-pix_fmt",
            "yuv420p",
            "-r",
            "30000/1001",
            "-g",
            "15",
            "-keyint_min",
            "15",
            "-bf",
            "2",
            "-sc_threshold",
            "0",
            "-c:a",
            "aac",
            "-profile:a",
            "aac_low",
            "-b:a",
            "384k",
            "-ar",
            "48000",
            "-ac",
            "2",
            "-movflags",
            "+faststart",
            "-metadata",
            f"title=WAZO {VERSION} — Your personalized wealth organizer",
            "-metadata",
            "artist=Zubair Shaikh",
            "-metadata",
            "comment=Original WAZO promotional video and soundtrack",
            str(master),
        ]
    )
    subprocess.run(command, check=True)

    review_command = [
        str(FFMPEG),
        "-y",
        "-i",
        str(master),
        "-c:v",
        "libx264",
        "-profile:v",
        "high",
        "-preset",
        "medium",
        "-crf",
        "20",
        "-maxrate",
        "14M",
        "-bufsize",
        "28M",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-movflags",
        "+faststart",
        str(review),
    ]
    subprocess.run(review_command, check=True)


def main() -> None:
    source_images = create_assets()
    render(source_images)
    print(f"Created WAZO promo package at {PROJECT_ROOT}")
    print(f"Duration: {TOTAL_DURATION:.3f} seconds")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"FFmpeg failed with exit code {exc.returncode}", file=sys.stderr)
        raise
