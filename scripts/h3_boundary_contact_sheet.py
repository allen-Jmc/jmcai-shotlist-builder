#!/usr/bin/env python3
"""Build adjacent MiniMax H3 clip-boundary contact sheets with ffmpeg."""

from __future__ import annotations

import argparse
import json
import pathlib
import shutil
import subprocess
import sys


WINDOW = 0.625
SAMPLE_FPS = 8


def run(command: list[str]) -> str:
    completed = subprocess.run(
        command,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return completed.stdout


def probe(path: pathlib.Path) -> dict[str, object]:
    raw = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height,r_frame_rate",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(path),
        ]
    )
    data = json.loads(raw)
    stream = data["streams"][0]
    return {
        "path": str(path.resolve()),
        "duration": round(float(data["format"]["duration"]), 6),
        "width": int(stream["width"]),
        "height": int(stream["height"]),
        "frame_rate": stream["r_frame_rate"],
    }


def build_sheet(
    previous: pathlib.Path,
    current: pathlib.Path,
    previous_duration: float,
    output: pathlib.Path,
) -> None:
    tail_start = max(0.0, previous_duration - WINDOW)
    filter_graph = (
        f"[0:v]trim=start={tail_start:.6f},setpts=PTS-STARTPTS,"
        f"fps={SAMPLE_FPS},scale=320:-2,tile=5x1:padding=4:margin=4:color=black[top];"
        f"[1:v]trim=start=0:end={WINDOW},setpts=PTS-STARTPTS,"
        f"fps={SAMPLE_FPS},scale=320:-2,tile=5x1:padding=4:margin=4:color=black[bottom];"
        "[top][bottom]vstack=inputs=2[out]"
    )
    run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-i",
            str(previous),
            "-i",
            str(current),
            "-filter_complex",
            filter_graph,
            "-map",
            "[out]",
            "-frames:v",
            "1",
            str(output),
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Create a two-row contact sheet for every adjacent H3 clip: "
            "previous tail above, next head below."
        )
    )
    parser.add_argument("clips", nargs="+", type=pathlib.Path)
    parser.add_argument("--output-dir", required=True, type=pathlib.Path)
    args = parser.parse_args()

    if len(args.clips) < 2:
        parser.error("at least two ordered clips are required")
    for tool in ("ffmpeg", "ffprobe"):
        if shutil.which(tool) is None:
            print(f"FAIL: {tool} is not available", file=sys.stderr)
            return 2
    for clip in args.clips:
        if not clip.is_file():
            print(f"FAIL: clip not found: {clip}", file=sys.stderr)
            return 2

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    clips = [clip.resolve() for clip in args.clips]
    clip_records = [probe(clip) for clip in clips]
    durations = {
        pathlib.Path(str(record["path"])): float(record["duration"])
        for record in clip_records
    }
    manifest: dict[str, object] = {
        "window_seconds": WINDOW,
        "sample_fps": SAMPLE_FPS,
        "clips": clip_records,
        "boundaries": [],
    }

    boundaries = manifest["boundaries"]
    assert isinstance(boundaries, list)
    for previous, current in zip(clips, clips[1:]):
        boundary_id = f"{previous.stem}__{current.stem}"
        sheet = output_dir / f"boundary_{boundary_id}.png"
        build_sheet(previous, current, durations[previous], sheet)
        boundaries.append(
            {
                "boundary_id": boundary_id,
                "from_clip": str(previous),
                "to_clip": str(current),
                "contact_sheet": str(sheet),
                "status": "pending_visual_review",
            }
        )

    manifest_path = output_dir / "boundary_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"PASS: wrote {len(boundaries)} boundary sheet(s) and {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
