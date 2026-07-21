from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import wave
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


WIDTH = 1920
HEIGHT = 1080
CAPTURE_FPS = 6
OUTPUT_FPS = "30000/1001"
OUTPUT_FPS_FLOAT = 30000 / 1001
VERSION = "1.1.4"
SOURCE_COMMIT = "7c63be818372307dc08ff6551b7296fca863d3e7"

SOURCE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SOURCE_DIR.parent
TIMELINE_PATH = SOURCE_DIR / "timeline.json"
NARRATION_PATH = PROJECT_ROOT / "audio" / "WAZO-English-Narration.wav"
SOURCE_SUBTITLES_PATH = PROJECT_ROOT / "delivery" / f"WAZO-Narrated-Explainer-v{VERSION}-English.srt"
CAPTURE_DIR = PROJECT_ROOT / "capture-frames"
CAPTURE_MANIFEST_PATH = PROJECT_ROOT / "manifests" / "capture-manifest.json"
CAPTURE_PATTERN = "frame-%06d.jpg"
LOGO_PATH = PROJECT_ROOT / "artwork" / "wazo-logo.png"
GENERATED_DIR = PROJECT_ROOT / "artwork"

INTRO_PATH = GENERATED_DIR / "wazo-narrated-intro.png"
OUTRO_PATH = GENERATED_DIR / "wazo-narrated-outro.png"
MUSIC_PATH = PROJECT_ROOT / "audio" / "wazo-narrated-original-bed.wav"
DELIVERY_DIR = PROJECT_ROOT / "delivery"
MANIFEST_DIR = PROJECT_ROOT / "manifests"
POSTER_PATH = DELIVERY_DIR / f"WAZO-Narrated-Explainer-v{VERSION}-Poster.png"
SUBTITLES_PATH = DELIVERY_DIR / f"WAZO-Narrated-Explainer-v{VERSION}-English.srt"
MASTER_PATH = DELIVERY_DIR / f"WAZO-Narrated-Explainer-v{VERSION}-Master.mp4"
REVIEW_PATH = DELIVERY_DIR / f"WAZO-Narrated-Explainer-v{VERSION}-Review.mp4"
MANIFEST_PATH = MANIFEST_DIR / "production-manifest.json"

FONT_REGULAR = Path(r"C:\Windows\Fonts\segoeui.ttf")
FONT_SEMIBOLD = Path(r"C:\Windows\Fonts\seguisb.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\segoeuib.ttf")


def load_timeline() -> dict[str, Any]:
    if not TIMELINE_PATH.exists():
        raise FileNotFoundError(f"Narration timeline was not found: {TIMELINE_PATH}")
    timeline = json.loads(TIMELINE_PATH.read_text(encoding="utf-8"))
    duration = float(timeline.get("videoDuration", 0))
    if duration <= 0 or not timeline.get("scenes"):
        raise ValueError("timeline.json does not contain a usable videoDuration and scene list")
    return timeline


def find_ffmpeg() -> Path:
    candidates: list[Path] = []
    if configured := os.environ.get("WAZO_FFMPEG"):
        candidates.append(Path(configured))
    if system_ffmpeg := shutil.which("ffmpeg"):
        candidates.append(Path(system_ffmpeg))
    try:
        import imageio_ffmpeg

        candidates.append(Path(imageio_ffmpeg.get_ffmpeg_exe()))
    except ImportError:
        pass
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError(
        "FFmpeg was not found. Set WAZO_FFMPEG, install ffmpeg on PATH, "
        "or install the imageio-ffmpeg Python package."
    )


def ffmpeg_supports_required_filters(ffmpeg: Path) -> None:
    result = subprocess.run(
        [str(ffmpeg), "-hide_banner", "-filters"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    filters = result.stdout + result.stderr
    missing = [name for name in ("framerate", "sidechaincompress", "overlay") if name not in filters]
    if missing:
        raise RuntimeError(f"This FFmpeg build is missing required filters: {', '.join(missing)}")


def image_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    if not path.exists():
        raise FileNotFoundError(f"Required Windows font was not found: {path}")
    return ImageFont.truetype(str(path), size=size)


def centered_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: int,
    text_font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int],
) -> None:
    box = draw.textbbox((0, 0), text, font=text_font)
    draw.text(((WIDTH - (box[2] - box[0])) / 2, y), text, font=text_font, fill=fill)


def brand_background() -> Image.Image:
    y, x = np.mgrid[0:HEIGHT, 0:WIDTH]
    nx = x / WIDTH
    ny = y / HEIGHT
    pixels = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    pixels[..., 0] = 9 + 13 * nx + 8 * (1 - ny)
    pixels[..., 1] = 11 + 16 * nx + 8 * (1 - ny)
    pixels[..., 2] = 39 + 42 * nx + 22 * (1 - ny)

    glows = [
        (0.20, 0.32, 0.50, (98, 55, 255), 0.72),
        (0.78, 0.70, 0.54, (0, 142, 255), 0.48),
        (0.56, 0.04, 0.34, (183, 73, 255), 0.30),
    ]
    for cx, cy, radius, color, strength in glows:
        distance = np.sqrt((nx - cx) ** 2 + (ny - cy) ** 2)
        glow = np.clip(1 - distance / radius, 0, 1) ** 2 * strength
        for channel, value in enumerate(color):
            pixels[..., channel] += glow * value

    vignette = np.clip(
        1 - 0.72 * (((nx - 0.5) / 0.72) ** 2 + ((ny - 0.5) / 0.76) ** 2),
        0.43,
        1,
    )
    pixels *= vignette[..., None]
    canvas = Image.fromarray(np.uint8(np.clip(pixels, 0, 255)), "RGB").convert("RGBA")

    texture = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(texture)
    for gx in range(0, WIDTH, 96):
        draw.line((gx, 0, gx, HEIGHT), fill=(154, 164, 255, 12), width=1)
    for gy in range(0, HEIGHT, 96):
        draw.line((0, gy, WIDTH, gy), fill=(154, 164, 255, 12), width=1)
    wealth_line = [
        (0, 846),
        (182, 790),
        (356, 825),
        (548, 692),
        (745, 735),
        (941, 574),
        (1138, 618),
        (1340, 452),
        (1533, 505),
        (1742, 320),
        (1920, 374),
    ]
    draw.line(wealth_line, fill=(144, 126, 255, 48), width=4, joint="curve")
    for px, py in wealth_line[1:-1]:
        draw.ellipse((px - 5, py - 5, px + 5, py + 5), fill=(209, 204, 255, 82))
    canvas.alpha_composite(texture)
    return canvas


def paste_logo(canvas: Image.Image, max_size: tuple[int, int], y: int) -> None:
    if not LOGO_PATH.exists():
        raise FileNotFoundError(f"WAZO logo was not found: {LOGO_PATH}")
    logo = Image.open(LOGO_PATH).convert("RGBA")
    logo.thumbnail(max_size, Image.Resampling.LANCZOS)
    x = (WIDTH - logo.width) // 2
    shadow_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow = Image.new("RGBA", logo.size, (40, 18, 108, 210))
    shadow.putalpha(logo.getchannel("A"))
    shadow_layer.paste(shadow, (x, y + 18), shadow)
    canvas.alpha_composite(shadow_layer.filter(ImageFilter.GaussianBlur(34)))
    canvas.alpha_composite(logo, (x, y))


def rounded_pill(
    draw: ImageDraw.ImageDraw,
    text: str,
    center_y: int,
    text_font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int] = (102, 79, 226, 232),
    center_x: int = WIDTH // 2,
) -> None:
    box = draw.textbbox((0, 0), text, font=text_font)
    text_width = box[2] - box[0]
    text_height = box[3] - box[1]
    pill_width = text_width + 64
    pill_height = text_height + 30
    left = center_x - pill_width // 2
    top = center_y - pill_height // 2
    draw.rounded_rectangle(
        (left, top, left + pill_width, top + pill_height),
        radius=pill_height // 2,
        fill=fill,
        outline=(190, 199, 255, 145),
        width=2,
    )
    draw.text((left + 32, top + 11 - box[1]), text, font=text_font, fill=(255, 255, 255, 255))


def make_intro() -> None:
    canvas = brand_background()
    paste_logo(canvas, (212, 212), 154)
    draw = ImageDraw.Draw(canvas)
    centered_text(draw, "WAZO", 405, image_font(FONT_BOLD, 138), (255, 255, 255, 255))
    centered_text(
        draw,
        "Your personalized wealth organizer",
        570,
        image_font(FONT_REGULAR, 46),
        (226, 231, 255, 255),
    )
    rounded_pill(draw, "PRIVATE   •   OFFLINE-FIRST   •   FOR WINDOWS", 720, image_font(FONT_SEMIBOLD, 25))
    centered_text(
        draw,
        "See your complete financial picture.",
        836,
        image_font(FONT_SEMIBOLD, 42),
        (255, 255, 255, 255),
    )
    canvas.convert("RGB").save(INTRO_PATH, optimize=True)


def make_outro() -> None:
    canvas = brand_background()
    paste_logo(canvas, (178, 178), 122)
    draw = ImageDraw.Draw(canvas)
    centered_text(draw, "Take control of your financial picture.", 354, image_font(FONT_BOLD, 61), (255, 255, 255, 255))
    centered_text(draw, "Private wealth organization", 474, image_font(FONT_SEMIBOLD, 47), (226, 232, 255, 255))
    rounded_pill(draw, "DISCOVER WAZO FOR WINDOWS", 625, image_font(FONT_SEMIBOLD, 26))
    centered_text(
        draw,
        "imzub.github.io/WAZO-OFFICIAL",
        760,
        image_font(FONT_REGULAR, 33),
        (190, 210, 255, 255),
    )
    centered_text(draw, f"Version {VERSION}", 848, image_font(FONT_REGULAR, 25), (173, 181, 220, 255))
    canvas.convert("RGB").save(OUTRO_PATH, optimize=True)


def fit_frame(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def make_poster(frame_path: Path) -> None:
    canvas = brand_background()
    draw = ImageDraw.Draw(canvas)
    screenshot = fit_frame(Image.open(frame_path), (1160, 653)).convert("RGBA")
    mask = Image.new("L", screenshot.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, screenshot.width, screenshot.height), radius=28, fill=255)
    screenshot.putalpha(mask)

    sx, sy = 665, 226
    shadow_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow = Image.new("RGBA", screenshot.size, (9, 6, 40, 230))
    shadow.putalpha(mask)
    shadow_layer.paste(shadow, (sx, sy + 22), shadow)
    canvas.alpha_composite(shadow_layer.filter(ImageFilter.GaussianBlur(32)))
    canvas.alpha_composite(screenshot, (sx, sy))
    draw.rounded_rectangle((sx, sy, sx + screenshot.width, sy + screenshot.height), radius=28, outline=(185, 190, 255, 140), width=3)

    logo = Image.open(LOGO_PATH).convert("RGBA")
    logo.thumbnail((116, 116), Image.Resampling.LANCZOS)
    canvas.alpha_composite(logo, (112, 118))
    draw.text((112, 275), "Meet", font=image_font(FONT_SEMIBOLD, 46), fill=(215, 222, 255, 255))
    draw.text((104, 326), "WAZO", font=image_font(FONT_BOLD, 103), fill=(255, 255, 255, 255))
    draw.multiline_text(
        (112, 475),
        "Your wealth.\nOrganized privately.",
        font=image_font(FONT_SEMIBOLD, 41),
        fill=(233, 236, 255, 255),
        spacing=14,
    )
    rounded_pill(
        draw,
        "INTRODUCTION VIDEO",
        844,
        image_font(FONT_SEMIBOLD, 23),
        (89, 69, 207, 238),
        center_x=326,
    )
    canvas.convert("RGB").save(POSTER_PATH, optimize=True)


def make_soundtrack(path: Path, duration: float) -> None:
    sample_rate = 48_000
    sample_count = int(math.ceil(duration * sample_rate))
    left = np.zeros(sample_count, dtype=np.float32)
    right = np.zeros(sample_count, dtype=np.float32)
    section_length = 8.0
    roots = [146.83, 110.00, 123.47, 98.00, 146.83, 110.00, 164.81, 98.00]
    chord_ratios = [0.5, 1.0, 1.25, 1.5, 2.0]

    for section, start in enumerate(np.arange(0.0, duration, section_length)):
        root = roots[section % len(roots)]
        start_index = int(start * sample_rate)
        end_index = min(sample_count, int((start + section_length + 1.4) * sample_rate))
        local_t = np.arange(end_index - start_index, dtype=np.float32) / sample_rate
        attack = np.clip(local_t / 1.6, 0, 1)
        release = np.clip((section_length + 1.4 - local_t) / 1.8, 0, 1)
        envelope = np.sin(np.minimum(attack, release) * np.pi / 2) ** 2
        pad_l = np.zeros_like(local_t)
        pad_r = np.zeros_like(local_t)
        for harmonic_index, ratio in enumerate(chord_ratios):
            frequency = root * ratio
            level = [0.26, 0.24, 0.17, 0.12, 0.07][harmonic_index]
            vibrato = 0.0018 * np.sin(2 * np.pi * (0.055 + harmonic_index * 0.009) * local_t)
            pad_l += level * np.sin(2 * np.pi * frequency * (1 + vibrato) * local_t + harmonic_index * 0.63)
            pad_r += level * np.sin(2 * np.pi * frequency * (1 - vibrato) * local_t + harmonic_index * 0.63 + 0.16)
        left[start_index:end_index] += 0.16 * envelope * pad_l
        right[start_index:end_index] += 0.16 * envelope * pad_r

    melody = [293.66, 369.99, 440.00, 554.37, 440.00, 369.99, 329.63, 246.94]
    for beat, start in enumerate(np.arange(1.4, duration - 0.5, 0.75)):
        frequency = melody[beat % len(melody)]
        start_index = int(start * sample_rate)
        length = min(sample_count - start_index, int(0.58 * sample_rate))
        local_t = np.arange(length, dtype=np.float32) / sample_rate
        envelope = np.exp(-5.2 * local_t) * np.sin(np.clip(local_t / 0.055, 0, 1) * np.pi / 2)
        tone = np.sin(2 * np.pi * frequency * local_t) + 0.18 * np.sin(2 * np.pi * frequency * 2 * local_t)
        pan = 0.22 + 0.56 * ((beat % 7) / 6)
        left[start_index : start_index + length] += 0.036 * (1.0 - 0.52 * pan) * envelope * tone
        right[start_index : start_index + length] += 0.036 * (0.48 + 0.52 * pan) * envelope * tone

    for start in np.arange(0.0, duration, 2.0):
        start_index = int(start * sample_rate)
        length = min(sample_count - start_index, int(0.48 * sample_rate))
        local_t = np.arange(length, dtype=np.float32) / sample_rate
        phase = 2 * np.pi * (54 * local_t - 10 * local_t**2)
        pulse = np.sin(phase) * np.exp(-10.5 * local_t)
        left[start_index : start_index + length] += 0.034 * pulse
        right[start_index : start_index + length] += 0.034 * pulse

    master = np.stack([left, right], axis=1)
    fade_samples = min(int(2.0 * sample_rate), sample_count // 4)
    master[:fade_samples] *= np.linspace(0, 1, fade_samples, dtype=np.float32)[:, None]
    master[-fade_samples:] *= np.linspace(1, 0, fade_samples, dtype=np.float32)[:, None]
    peak = max(float(np.max(np.abs(master))), 1e-8)
    master = np.clip(master * (0.42 / peak), -1, 1)
    pcm = np.int16(master * 32767)

    with wave.open(str(path), "wb") as output:
        output.setnchannels(2)
        output.setsampwidth(2)
        output.setframerate(sample_rate)
        output.writeframes(pcm.tobytes())


def frame_number(path: Path) -> int:
    try:
        return int(path.stem.rsplit("-", 1)[1])
    except (IndexError, ValueError) as exc:
        raise ValueError(f"Unexpected capture frame name: {path.name}") from exc


def validate_capture(duration: float) -> list[Path]:
    frames = sorted(CAPTURE_DIR.glob("frame-*.jpg"), key=frame_number)
    if not frames:
        raise FileNotFoundError(
            f"No live capture frames were found in {CAPTURE_DIR}. "
            f"Expected {CAPTURE_PATTERN} at {CAPTURE_FPS} fps."
        )
    numbers = [frame_number(frame) for frame in frames]
    expected_numbers = list(range(numbers[0], numbers[0] + len(numbers)))
    if numbers[0] != 1 or numbers != expected_numbers:
        raise ValueError("Capture frames must be a complete sequence beginning with frame-000001.jpg")
    minimum_frames = math.floor(duration * CAPTURE_FPS) - 1
    if len(frames) < minimum_frames:
        captured_seconds = len(frames) / CAPTURE_FPS
        raise ValueError(
            f"Capture is too short: {len(frames)} frames ({captured_seconds:.3f}s); "
            f"at least {minimum_frames} frames are required for {duration:.3f}s."
        )
    with Image.open(frames[0]) as first:
        first.verify()
    with Image.open(frames[-1]) as last:
        last.verify()
    return frames


def validate_audio(duration: float) -> None:
    if not NARRATION_PATH.exists():
        raise FileNotFoundError(f"Narration WAV was not found: {NARRATION_PATH}")
    with wave.open(str(NARRATION_PATH), "rb") as narration:
        narration_duration = narration.getnframes() / narration.getframerate()
    if narration_duration < duration - 2.0:
        raise ValueError(
            f"Narration is unexpectedly short ({narration_duration:.3f}s for a {duration:.3f}s video)."
        )
    if not SOURCE_SUBTITLES_PATH.exists():
        raise FileNotFoundError(f"English subtitles were not found: {SOURCE_SUBTITLES_PATH}")


def require_render_space(minimum_mib: int = 450) -> None:
    free = shutil.disk_usage(PROJECT_ROOT).free
    required = minimum_mib * 1024 * 1024
    if free < required:
        raise OSError(
            f"Only {free / (1024**2):.0f} MiB is free on {PROJECT_ROOT.drive}; "
            f"at least {minimum_mib} MiB is required for the two compressed outputs."
        )


def prepare_assets(timeline: dict[str, Any], frames: list[Path]) -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    DELIVERY_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    make_intro()
    make_outro()
    make_soundtrack(MUSIC_PATH, float(timeline["videoDuration"]))
    if SOURCE_SUBTITLES_PATH.resolve() != SUBTITLES_PATH.resolve():
        shutil.copy2(SOURCE_SUBTITLES_PATH, SUBTITLES_PATH)
    poster_index = min(len(frames) - 1, round(8.0 * CAPTURE_FPS))
    make_poster(frames[poster_index])


def build_filter(duration: float) -> str:
    intro_duration = 3.4
    intro_fade_start = 2.4
    outro_duration = 6.2
    outro_start = duration - outro_duration
    return ";".join(
        [
            "[0:v]"
            f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=decrease,"
            f"pad={WIDTH}:{HEIGHT}:(ow-iw)/2:(oh-ih)/2:color=0x070923,"
            "setsar=1,"
            f"framerate=fps={OUTPUT_FPS}:interp_start=0:interp_end=255:scene=8.2,"
            "tpad=stop_mode=clone:stop_duration=1,"
            f"trim=duration={duration:.3f},setpts=PTS-STARTPTS,format=yuv420p[app]",
            "[1:v]"
            f"scale={WIDTH}:{HEIGHT},setsar=1,format=rgba,"
            f"trim=duration={intro_duration:.3f},setpts=PTS-STARTPTS,"
            f"fade=t=out:st={intro_fade_start:.3f}:d={intro_duration - intro_fade_start:.3f}:alpha=1[intro]",
            "[app][intro]"
            f"overlay=0:0:enable='between(t,0,{intro_duration:.3f})':eof_action=pass:shortest=0[withintro]",
            "[2:v]"
            f"scale={WIDTH}:{HEIGHT},setsar=1,format=rgba,"
            f"trim=duration={outro_duration:.3f},setpts=PTS-STARTPTS,"
            "fade=t=in:st=0:d=1.0:alpha=1,"
            f"setpts=PTS+{outro_start:.3f}/TB[outro]",
            "[withintro][outro]"
            f"overlay=0:0:enable='gte(t,{outro_start:.3f})':eof_action=pass:shortest=0,format=yuv420p[vout]",
            "[3:a]"
            f"aresample=48000,atrim=0:{duration:.3f},asetpts=PTS-STARTPTS,"
            "loudnorm=I=-16:TP=-1.5:LRA=7[narration0]",
            "[narration0]asplit=2[narration][sidechain]",
            "[4:a]"
            f"aresample=48000,atrim=0:{duration:.3f},asetpts=PTS-STARTPTS,"
            f"afade=t=in:st=0:d=1.5,afade=t=out:st={duration - 2.0:.3f}:d=2.0,volume=0.26[music]",
            "[music][sidechain]"
            "sidechaincompress=threshold=0.012:ratio=10:attack=18:release=520:makeup=1[ducked]",
            "[narration][ducked]"
            "amix=inputs=2:duration=longest:weights='1 0.62':normalize=0,"
            "alimiter=limit=0.94:attack=5:release=80,"
            "loudnorm=I=-16:TP=-1.2:LRA=8[aout]",
        ]
    )


def run(command: list[str], label: str) -> None:
    print(f"\n{label}")
    print(" ".join(f'\"{part}\"' if " " in part else part for part in command))
    subprocess.run(command, check=True)


def render_master(ffmpeg: Path, duration: float) -> None:
    filter_complex = build_filter(duration)
    command = [
        str(ffmpeg),
        "-y",
        "-hide_banner",
        "-loglevel",
        "warning",
        "-framerate",
        str(CAPTURE_FPS),
        "-start_number",
        "1",
        "-i",
        str(CAPTURE_DIR / CAPTURE_PATTERN),
        "-loop",
        "1",
        "-framerate",
        OUTPUT_FPS,
        "-i",
        str(INTRO_PATH),
        "-loop",
        "1",
        "-framerate",
        OUTPUT_FPS,
        "-i",
        str(OUTRO_PATH),
        "-i",
        str(NARRATION_PATH),
        "-i",
        str(MUSIC_PATH),
        "-i",
        str(SUBTITLES_PATH),
        "-filter_complex",
        filter_complex,
        "-map",
        "[vout]",
        "-map",
        "[aout]",
        "-map",
        "5:0",
        "-t",
        f"{duration:.3f}",
        "-c:v",
        "libx264",
        "-profile:v",
        "high",
        "-level:v",
        "4.2",
        "-preset",
        "slow",
        "-b:v",
        "15M",
        "-maxrate",
        "16M",
        "-bufsize",
        "32M",
        "-pix_fmt",
        "yuv420p",
        "-r",
        OUTPUT_FPS,
        "-g",
        "60",
        "-keyint_min",
        "30",
        "-sc_threshold",
        "0",
        "-c:a",
        "aac",
        "-profile:a",
        "aac_low",
        "-b:a",
        "256k",
        "-ar",
        "48000",
        "-ac",
        "2",
        "-c:s",
        "mov_text",
        "-metadata:s:s:0",
        "language=eng",
        "-metadata:s:s:0",
        "handler_name=English subtitles",
        "-disposition:s:0",
        "default",
        "-movflags",
        "+faststart",
        "-metadata",
        f"title=WAZO {VERSION} - Narrated introduction",
        "-metadata",
        "artist=Zubair Shaikh",
        "-metadata",
        "comment=Official WAZO English-language feature explainer",
        str(MASTER_PATH),
    ]
    run(command, "Rendering high-quality narrated master...")


def render_review(ffmpeg: Path) -> None:
    command = [
        str(ffmpeg),
        "-y",
        "-hide_banner",
        "-loglevel",
        "warning",
        "-i",
        str(MASTER_PATH),
        "-map",
        "0:v:0",
        "-map",
        "0:a:0",
        "-map",
        "0:s?",
        "-c:v",
        "libx264",
        "-profile:v",
        "high",
        "-preset",
        "medium",
        "-crf",
        "23",
        "-maxrate",
        "6M",
        "-bufsize",
        "12M",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-c:s",
        "copy",
        "-movflags",
        "+faststart",
        str(REVIEW_PATH),
    ]
    run(command, "Creating compact review copy...")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_record(path: Path) -> dict[str, Any]:
    return {
        "path": path.relative_to(PROJECT_ROOT).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def write_manifest(timeline: dict[str, Any], frames: list[Path], ffmpeg: Path) -> None:
    capture_manifest: dict[str, Any] | None = None
    if CAPTURE_MANIFEST_PATH.exists():
        capture_manifest = json.loads(CAPTURE_MANIFEST_PATH.read_text(encoding="utf-8"))
    outputs = [MASTER_PATH, REVIEW_PATH, POSTER_PATH, SUBTITLES_PATH]
    manifest = {
        "schemaVersion": 1,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "project": "WAZO narrated English introduction",
        "appVersion": VERSION,
        "sourceCommit": SOURCE_COMMIT,
        "durationSeconds": float(timeline["videoDuration"]),
        "video": {
            "resolution": f"{WIDTH}x{HEIGHT}",
            "captureFps": CAPTURE_FPS,
            "outputFps": OUTPUT_FPS,
            "captureFramePattern": f"capture-frames/{CAPTURE_PATTERN}",
            "captureFrameCount": len(frames),
            "motionInterpolation": "FFmpeg scene-aware linear frame interpolation",
            "masterVideoRate": "15 Mbps target, 16 Mbps maximum",
            "reviewVideoRate": "CRF 23, 6 Mbps maximum",
        },
        "audio": {
            "voice": timeline.get("voice"),
            "language": "en-US",
            "narration": file_record(NARRATION_PATH),
            "music": {
                **file_record(MUSIC_PATH),
                "description": "Original procedurally generated ambient instrumental; ducked under narration",
            },
            "masterTarget": "-16 LUFS, true peak below -1.2 dB",
        },
        "subtitles": {
            "language": "English",
            "embeddedCodec": "mov_text",
            "sidecar": file_record(SUBTITLES_PATH),
        },
        "timeline": file_record(TIMELINE_PATH),
        "captureManifest": capture_manifest,
        "ffmpeg": str(ffmpeg),
        "outputs": [file_record(path) for path in outputs],
        "privacy": "Live capture uses the isolated anonymous WAZO demo profile only.",
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def static_check(ffmpeg: Path, timeline: dict[str, Any]) -> None:
    required = [NARRATION_PATH, SOURCE_SUBTITLES_PATH, LOGO_PATH, FONT_REGULAR, FONT_SEMIBOLD, FONT_BOLD]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required inputs:\n" + "\n".join(missing))
    ffmpeg_supports_required_filters(ffmpeg)
    validate_audio(float(timeline["videoDuration"]))
    print("Static inputs and FFmpeg capabilities are ready.")
    if CAPTURE_DIR.exists() and any(CAPTURE_DIR.glob("frame-*.jpg")):
        frames = validate_capture(float(timeline["videoDuration"]))
        print(f"Live capture is ready: {len(frames)} frames at {CAPTURE_FPS} fps.")
    else:
        print(f"Live capture is pending: {CAPTURE_DIR / CAPTURE_PATTERN}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the WAZO 1.1.4 English narrated introduction from live capture frames."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate static dependencies and report capture readiness without generating or rendering.",
    )
    parser.add_argument(
        "--prepare-only",
        action="store_true",
        help="Validate capture and generate cards, poster, soundtrack, and subtitle copy without rendering video.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    timeline = load_timeline()
    duration = float(timeline["videoDuration"])
    ffmpeg = find_ffmpeg()
    if args.check:
        static_check(ffmpeg, timeline)
        return

    static_check(ffmpeg, timeline)
    frames = validate_capture(duration)
    prepare_assets(timeline, frames)
    if args.prepare_only:
        print(f"Prepared narrated-video assets in {GENERATED_DIR}")
        print(f"Poster: {POSTER_PATH}")
        return

    require_render_space()
    render_master(ffmpeg, duration)
    render_review(ffmpeg)
    write_manifest(timeline, frames, ffmpeg)
    print("\nWAZO narrated explainer package created:")
    for path in (MASTER_PATH, REVIEW_PATH, POSTER_PATH, SUBTITLES_PATH, MANIFEST_PATH):
        print(f"  {path}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"FFmpeg failed with exit code {exc.returncode}.", file=sys.stderr)
        raise
