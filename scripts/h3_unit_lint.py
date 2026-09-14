#!/usr/bin/env python3
"""Lint MiniMax H3 dual-prompt unit metadata and speech budgets in HTML."""

from __future__ import annotations

import argparse
import html
import pathlib
import re
import sys


ARTICLE_RE = re.compile(
    r"<article\b(?P<attrs>[^>]*\bclass\s*=\s*(['\"])[^'\"]*\bh3-unit\b[^'\"]*\2[^>]*)>"
    r"(?P<body>.*?)</article>",
    re.IGNORECASE | re.DOTALL,
)
ATTRIBUTE_RE = re.compile(r"([\w-]+)\s*=\s*(['\"])(.*?)\2", re.DOTALL)
PROMPT_CONTAINER_RE = re.compile(
    r"<(?:pre\b[^>]*|div\b[^>]*\bclass\s*=\s*(['\"])[^'\"]*\bprompt-block\b[^'\"]*\1[^>]*)>"
    r"(?P<prompt>.*?)</(?:pre|div)>",
    re.IGNORECASE | re.DOTALL,
)
CHINESE_DIALOGUE_RE = re.compile(
    r"[^\n]{1,120}(?:说|问|答|回应|低声|开口|画外音|使用(?!角色图中的形象))[^：:\n]{0,160}"
    r"[：:]\s*(?:“(?P<quoted>[^”]+)”|(?P<plain>[^\n]+))"
)
EFFECTIVE_CHAR_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaffA-Za-z0-9]")
SHOT_TIME_RE = re.compile(
    r"【镜头\s*(?P<number>\d+)\s*｜\s*(?P<start>\d+(?:\.\d+)?)—"
    r"(?P<end>\d+(?:\.\d+)?)秒】"
)
CHINESE_TITLE_RE = re.compile(r"^中文(?:审稿|分镜)版｜H3-[\w-]+｜\d+(?:\.\d+)?秒\s*$", re.MULTILINE)
ZH_MACHINE_START_RE = re.compile(r"^主体定义：\s*$", re.MULTILINE)
ENGLISH_SIX_SECTION_RE = re.compile(r"^subject_definitions:\s*$", re.MULTILINE | re.IGNORECASE)
PACKED_RUNTIME_RE = re.compile(
    r"<(?P<tag>[A-Za-z][\w:-]*)\b(?P<attrs>[^>]*\bdata-h3-packed-runtime-seconds\s*=\s*"
    r"(?P<quote>['\"])(?P<declared>[^'\"]+)(?P=quote)[^>]*)>"
    r"(?P<body>.*?)</(?P=tag)>",
    re.IGNORECASE | re.DOTALL,
)
VISIBLE_RUNTIME_RE = re.compile(r"(?P<value>\d+(?:\.\d+)?)\s*s\b", re.IGNORECASE)


def parse_attributes(raw: str) -> dict[str, str]:
    return {
        name.lower(): html.unescape(value).strip()
        for name, _quote, value in ATTRIBUTE_RE.findall(raw)
    }


def extract_prompt_blocks(body: str) -> list[str]:
    return [html.unescape(match.group("prompt")) for match in PROMPT_CONTAINER_RE.finditer(body)]


def effective_dialogue_chars(prompt: str) -> int:
    spoken = "".join(
        match.group("quoted") or match.group("plain") or ""
        for match in CHINESE_DIALOGUE_RE.finditer(prompt)
    )
    return len(EFFECTIVE_CHAR_RE.findall(spoken))


def suggested_max(duration: float) -> int | None:
    if duration < 10:
        return None
    if duration <= 10.5:
        return 24
    if duration <= 13.5:
        return 30
    return 36


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check H3 unit duration, dialogue budget, relationship/action/state metadata, "
            "and internal shot times in a Chinese director-storyboard shotlist HTML."
        )
    )
    parser.add_argument("html_file", type=pathlib.Path)
    args = parser.parse_args()

    source = args.html_file.read_text(encoding="utf-8")
    units = list(ARTICLE_RE.finditer(source))
    if not units:
        print("FAIL: no <article class=\"h3-unit\"> records found", file=sys.stderr)
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    seen_ids: set[str] = set()
    packed_duration = 0.0

    print("unit\tduration\tdialogue_chars\tstatus")
    for index, unit in enumerate(units, start=1):
        attrs = parse_attributes(unit.group("attrs"))
        unit_id = attrs.get("data-h3-unit", "") or f"unit-{index}"
        unit_errors: list[str] = []

        if unit_id in seen_ids:
            unit_errors.append("duplicate unit id")
        seen_ids.add(unit_id)

        for required in (
            "data-h3-unit",
            "data-unit-kind",
            "data-duration-seconds",
            "data-dialogue-effective-chars",
            "data-relationship-turn",
            "data-action-chain",
            "data-opening-state",
            "data-exit-state",
        ):
            if not attrs.get(required, ""):
                unit_errors.append(f"{required} is missing or empty")

        try:
            duration = float(attrs.get("data-duration-seconds", ""))
        except ValueError:
            duration = -1.0
            unit_errors.append("data-duration-seconds is not numeric")
        if duration >= 0:
            packed_duration += duration

        exception_reason = attrs.get("data-duration-exception-reason", "")
        if duration > 15:
            unit_errors.append("duration exceeds the 15-second H3 ceiling")
        elif 0 <= duration < 5:
            unit_errors.append("duration is below the 5-second exception floor")
        elif 5 <= duration < 10 and not exception_reason:
            unit_errors.append("sub-10-second unit lacks data-duration-exception-reason")

        blocks = extract_prompt_blocks(unit.group("body"))
        chinese_blocks = [block for block in blocks if CHINESE_TITLE_RE.search(block)]
        english_blocks = [block for block in blocks if ENGLISH_SIX_SECTION_RE.search(block)]
        chinese_machine_blocks = [block for block in blocks if ZH_MACHINE_START_RE.search(block)]

        has_machine = len(chinese_machine_blocks) > 0
        valid_counts = (
            (len(blocks) == 3 and len(chinese_blocks) == 1 and len(english_blocks) == 1 and len(chinese_machine_blocks) == 1)
            if has_machine
            else (len(blocks) == 2 and len(chinese_blocks) == 1 and len(english_blocks) == 1)
        )
        if not valid_counts:
            computed_chars = -1
            unit_errors.append(
                "expected exactly one Chinese director-storyboard block and one English "
                f"six-section block (optional one Chinese machine block), found {len(chinese_blocks)} Chinese / "
                f"{len(chinese_machine_blocks)} Chinese machine / {len(english_blocks)} English / {len(blocks)} total"
            )
        else:
            prompt = chinese_blocks[0]
            computed_chars = effective_dialogue_chars(prompt)
            shot_times = list(SHOT_TIME_RE.finditer(prompt))
            if not shot_times:
                unit_errors.append("prompt contains no Chinese timed shot headers")
            elif duration >= 0 and abs(float(shot_times[-1].group("end")) - duration) > 1e-6:
                unit_errors.append(
                    f"last shot ends at {float(shot_times[-1].group('end')):g}s, not declared {duration:g}s"
                )
            for shot_match in shot_times:
                cut_time = float(shot_match.group("end"))
                if duration >= 0 and cut_time > duration + 1e-6:
                    unit_errors.append(
                        f"镜头{shot_match.group('number')} ends at {cut_time:.3f}s "
                        f"is outside {duration:.3f}s"
                    )

        try:
            declared_chars = int(attrs.get("data-dialogue-effective-chars", ""))
        except ValueError:
            declared_chars = -1
            unit_errors.append("data-dialogue-effective-chars is not an integer")

        if computed_chars >= 0 and declared_chars >= 0 and computed_chars != declared_chars:
            unit_errors.append(
                f"declared dialogue count {declared_chars} != computed {computed_chars}"
            )
        if computed_chars > 40:
            unit_errors.append("Chinese dialogue exceeds the 40-effective-character hard limit")

        recommended = suggested_max(duration)
        if recommended is not None and computed_chars > recommended:
            warnings.append(
                f"{unit_id}: {computed_chars} effective characters exceed the normal "
                f"{duration:g}s recommendation ({recommended}); verify comedy pace or split"
            )

        status = "FAIL" if unit_errors else "PASS"
        print(f"{unit_id}\t{duration:g}\t{computed_chars}\t{status}")
        errors.extend(f"{unit_id}: {message}" for message in unit_errors)

    runtime_markers = list(PACKED_RUNTIME_RE.finditer(source))
    if len(runtime_markers) != 1:
        errors.append(
            "HTML: expected exactly one visible element with "
            f"data-h3-packed-runtime-seconds, found {len(runtime_markers)}"
        )
    else:
        marker = runtime_markers[0]
        try:
            declared_runtime = float(html.unescape(marker.group("declared")).strip())
        except ValueError:
            declared_runtime = -1.0
            errors.append("HTML: data-h3-packed-runtime-seconds is not numeric")
        if declared_runtime >= 0 and abs(declared_runtime - packed_duration) > 1e-6:
            errors.append(
                f"HTML: packed runtime attribute {declared_runtime:g}s != summed unit duration "
                f"{packed_duration:g}s"
            )
        visible = VISIBLE_RUNTIME_RE.search(html.unescape(marker.group("body")))
        if visible is None:
            errors.append(
                "HTML: packed-runtime element does not visibly print the runtime with an 's' suffix"
            )
        else:
            visible_runtime = float(visible.group("value"))
            if abs(visible_runtime - packed_duration) > 1e-6:
                errors.append(
                    f"HTML: visible packed runtime {visible_runtime:g}s != summed unit duration "
                    f"{packed_duration:g}s"
                )

    if warnings:
        print(f"WARN: {len(warnings)} density warning(s)")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print(f"FAIL: {len(errors)} issue(s) in {len(units)} H3 unit(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {len(units)} H3 dual-prompt unit(s) satisfy unit and dialogue-budget checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
