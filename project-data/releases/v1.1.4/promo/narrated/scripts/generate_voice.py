from __future__ import annotations

import asyncio
import json
import os
import shutil
import subprocess
import wave
from pathlib import Path

import edge_tts


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(__file__).resolve().parent
AUDIO_DIR = ROOT / "audio"
DELIVERY_DIR = ROOT / "delivery"
SEGMENT_DIR = AUDIO_DIR / "voice-segments"
SCRIPT_PATH = SOURCE / "narration.json"
SILENCE_SECONDS = 0.58


def find_ffmpeg() -> Path:
    configured = os.environ.get("WAZO_FFMPEG", "").strip()
    if configured:
        return Path(configured).expanduser().resolve()

    local_candidates = (
        ROOT / "tools" / "ffmpeg.exe",
        ROOT / "tools" / "ffmpeg",
        ROOT / "ffmpeg.exe",
        ROOT / "ffmpeg",
    )
    for candidate in local_candidates:
        if candidate.is_file():
            return candidate.resolve()

    executable = shutil.which("ffmpeg")
    if executable:
        return Path(executable).resolve()

    try:
        import imageio_ffmpeg

        executable = imageio_ffmpeg.get_ffmpeg_exe()
        if executable:
            return Path(executable).resolve()
    except (ImportError, RuntimeError):
        pass

    raise FileNotFoundError(
        "FFmpeg was not found. Set WAZO_FFMPEG, add ffmpeg to PATH, "
        "place it in the narrated archive's tools directory, or install imageio-ffmpeg."
    )


FFMPEG = find_ffmpeg()


async def synthesize_segment(text: str, output: Path, voice: str, rate: str, pitch: str) -> None:
    communicator = edge_tts.Communicate(
        text,
        voice,
        rate=rate,
        pitch=pitch,
        boundary="SentenceBoundary",
    )
    await communicator.save(str(output))


def convert_to_wav(source: Path, target: Path) -> None:
    subprocess.run(
        [
            str(FFMPEG),
            "-y",
            "-v",
            "error",
            "-i",
            str(source),
            "-ar",
            "48000",
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(target),
        ],
        check=True,
    )


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as audio:
        return audio.getnframes() / audio.getframerate()


def srt_time(seconds: float) -> str:
    milliseconds = int(round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    whole_seconds, milliseconds = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{whole_seconds:02d},{milliseconds:03d}"


def write_concat_file(paths: list[Path], silence: Path, output: Path) -> None:
    lines: list[str] = []
    for index, path in enumerate(paths):
        lines.append(f"file '{path.as_posix()}'")
        if index < len(paths) - 1:
            lines.append(f"file '{silence.as_posix()}'")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def create_silence(path: Path) -> None:
    subprocess.run(
        [
            str(FFMPEG),
            "-y",
            "-v",
            "error",
            "-f",
            "lavfi",
            "-i",
            "anullsrc=r=48000:cl=mono",
            "-t",
            f"{SILENCE_SECONDS:.3f}",
            "-c:a",
            "pcm_s16le",
            str(path),
        ],
        check=True,
    )


async def main() -> None:
    if not FFMPEG.exists():
        raise FileNotFoundError(f"FFmpeg executable not found: {FFMPEG}")
    config = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    DELIVERY_DIR.mkdir(parents=True, exist_ok=True)
    SEGMENT_DIR.mkdir(parents=True, exist_ok=True)

    wav_paths: list[Path] = []
    timeline: list[dict[str, object]] = []
    cursor = 0.0
    for index, scene in enumerate(config["scenes"], start=1):
        stem = f"{index:02d}-{scene['id']}"
        mp3 = SEGMENT_DIR / f"{stem}.mp3"
        wav = SEGMENT_DIR / f"{stem}.wav"
        await synthesize_segment(scene["spoken"], mp3, config["voice"], config["rate"], config["pitch"])
        convert_to_wav(mp3, wav)
        duration = wav_duration(wav)
        timeline.append(
            {
                "index": index,
                "id": scene["id"],
                "view": scene["view"],
                "start": round(cursor, 3),
                "voiceDuration": round(duration, 3),
                "end": round(cursor + duration, 3),
                "sceneEnd": round(cursor + duration + (SILENCE_SECONDS if index < len(config["scenes"]) else 1.2), 3),
                "caption": scene["caption"],
            }
        )
        cursor += duration
        if index < len(config["scenes"]):
            cursor += SILENCE_SECONDS
        wav_paths.append(wav)

    silence = SEGMENT_DIR / "silence.wav"
    create_silence(silence)
    concat_file = SEGMENT_DIR / "concat.txt"
    write_concat_file(wav_paths, silence, concat_file)
    narration_wav = AUDIO_DIR / "WAZO-English-Narration.wav"
    narration_mp3 = AUDIO_DIR / "WAZO-English-Narration.mp3"
    subprocess.run(
        [str(FFMPEG), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat_file), "-c", "copy", str(narration_wav)],
        check=True,
    )
    subprocess.run(
        [
            str(FFMPEG),
            "-y",
            "-v",
            "error",
            "-i",
            str(narration_wav),
            "-af",
            "loudnorm=I=-16:TP=-2:LRA=7",
            "-c:a",
            "libmp3lame",
            "-b:a",
            "256k",
            str(narration_mp3),
        ],
        check=True,
    )

    total_duration = wav_duration(narration_wav)
    timeline[-1]["sceneEnd"] = round(total_duration + 1.2, 3)
    timeline_path = SOURCE / "timeline.json"
    timeline_path.write_text(
        json.dumps(
            {
                "title": config["title"],
                "voice": config["voice"],
                "rate": config["rate"],
                "pitch": config["pitch"],
                "silenceBetweenScenes": SILENCE_SECONDS,
                "narrationDuration": round(total_duration, 3),
                "videoDuration": round(total_duration + 1.2, 3),
                "scenes": timeline,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    subtitles: list[str] = []
    for scene in timeline:
        subtitles.extend(
            [
                str(scene["index"]),
                f"{srt_time(float(scene['start']))} --> {srt_time(float(scene['end']))}",
                str(scene["caption"]),
                "",
            ]
        )
    (DELIVERY_DIR / "WAZO-Narrated-Explainer-v1.1.4-English.srt").write_text(
        "\n".join(subtitles),
        encoding="utf-8",
    )
    print(json.dumps({"narrationDuration": total_duration, "videoDuration": total_duration + 1.2, "scenes": len(timeline)}, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
