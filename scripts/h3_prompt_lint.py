#!/usr/bin/env python3
"""Lint paired MiniMax H3 Chinese storyboard and English six-section prompts."""

from __future__ import annotations

import argparse
import html
import pathlib
import re
import sys


CONTAINER = re.compile(
    r"<(?P<tag>pre|div)\b(?P<attrs>[^>]*)>(?P<prompt>.*?)</(?P=tag)>",
    re.IGNORECASE | re.DOTALL,
)
ATTRIBUTE = re.compile(r"([\w-]+)\s*=\s*(['\"])(.*?)\2", re.DOTALL)
TITLE = re.compile(r"^中文(?:审稿|分镜)版｜H3-[\w-]+｜\d+(?:\.\d+)?秒\s*$", re.MULTILINE)
ZH_SHOT = re.compile(
    r"^【镜头\s*(?P<number>\d+)\s*｜\s*"
    r"(?P<start>\d+(?:\.\d+)?)—(?P<end>\d+(?:\.\d+)?)秒】",
    re.MULTILINE,
)
EN_SHOT = re.compile(
    r"\[Shot\s+(?P<number>\d+)\]"
    r"(?:\s+At\s+(?P<minute>\d{2}):(?P<second>\d{2}(?:\.\d{3})),)?",
    re.IGNORECASE,
)
REFERENCE_LABEL = re.compile(r"<(?:Subject|Picture|Video|Audio)\s+\d+>", re.IGNORECASE)
AUDIO_LABEL = re.compile(r"<Audio\s+\d+>", re.IGNORECASE)
AUDIO_FILENAME_IN_PROMPT = re.compile(
    r"(?<![\w.-])[^\s,；;<>]+\.(?:wav|mp3|m4a|flac|aac|ogg|opus)(?![\w.-])",
    re.IGNORECASE,
)
EN_AUDIO_DEFINITION = re.compile(
    r"^(?P<label><Audio\s+\d+>)\s+is\s+(?P<description>.+?)\s*$",
    re.MULTILINE | re.IGNORECASE,
)
EN_AUDIO_RETENTION = re.compile(
    r"^(?P<label><Audio\s+\d+>)\s*:\s*"
    r"(?P<marker>fully_copy|partially_copy|reference|weak_reference)\s*-\s*"
    r"(?P<scope>.+?)\s*$",
    re.MULTILINE | re.IGNORECASE,
)
ZH_AUDIO_BINDING = re.compile(
    r"^(?P<label><Audio\s+\d+>)\s*：\s*(?P<body>.+?)\s*$",
    re.MULTILINE | re.IGNORECASE,
)
DIALOGUE_TAG = re.compile(r"<d>\[(?P<language>[^\]]+)\]\s*(?P<text>.*?)</d>", re.DOTALL)
ZH_DIALOGUE = re.compile(
    r"[^\n]{1,240}(?:说|问|答|回应|低声|开口|画外音|实际说出|使用(?!角色图中的形象))"
    r"[^：:\n]{0,220}[：:]\s*(?P<line>[^\n]+)"
)
LEGACY_IN_CHINESE = re.compile(
    r"<\s*/?d\s*>|<\s*(?:Subject|Picture|Video)\s+\d+\s*>|\(S\d+\)|"
    r"integrated_multimodal_description\s*:|overall_soundscape\s*:|non_diegetic_music\s*:",
    re.IGNORECASE,
)
BOUNDARY_TAG = re.compile(
    r"<[^>]+\bdata-h3-boundary\s*=\s*(['\"])[^'\"]+\1[^>]*>", re.IGNORECASE
)
VALID_BOUNDARY_STRATEGIES = {
    "exact_match_continuation", "contrast_cut", "neutral_bridge", "scene_transition"
}
EN_SECTIONS = [
    "subject_definitions:", "summary:", "retention_analysis:",
    "detailed_description:", "overall_soundscape:", "non_diegetic_music:",
]
# 中文机读六段式法定核心段落与起始正则
ZH_MACHINE_SECTIONS = [
    "主体定义：", "任务摘要：", "保留分析：",
    "镜头详述：", "环境音响：", "非剧情音乐：",
]
ZH_MACHINE_START = re.compile(r"^主体定义：\s*$", re.MULTILINE)

CHINESE_AUTHORING_LEAKS = {
    "第一决定动作占位": re.compile(r"第一个决定性动作"),
    "下一条原文信息占位": re.compile(r"新增下一条原文信息|下一条原文信息"),
    "信息落地占位": re.compile(r"信息落地或动作结果"),
    "未完成镜头选择": re.compile(
        r"(?:远景|中景|近景|背面三分之四|道具主导|过肩)[^。\n]{0,80}或[^。\n]{0,80}"
        r"(?:远景|中景|近景|背面三分之四|道具主导|过肩)"
    ),
    "承接占位": re.compile(r"承接上一段|保持同前|根据需要选择镜头"),
    "跨单元音色依赖": re.compile(
        r"(?:以|使用)?与\s*H3-\d+\s*(?:完全)?一致[^。\n]{0,80}(?:声线|音色|嗓音|高音|中音|低音)"
        r"|沿用\s*(?:H3-\d+|上一段|前一单元)[^。\n]{0,80}(?:声线|音色|嗓音|高音|中音|低音)"
    ),
}
EN_AUTHORING_LEAK = re.compile(
    r"same as (?:the )?(?:previous|prior) (?:clip|unit|prompt)|choose (?:a|the) (?:shot|framing)|"
    r"add the next source fact|first decisive action",
    re.IGNORECASE,
)

MODE_MARKERS = {
    "audio reuse": {"fully_copy", "partially_copy"},
    "audio reference": {"reference", "weak_reference"},
}


def canonical_audio_label(label: str) -> str:
    number = re.search(r"\d+", label)
    return f"<audio {number.group(0)}>" if number else label.lower()


def parse_english_audio(fields: dict[str, str]) -> tuple[dict[str, dict[str, str]], str | None, dict[str, str]]:
    definitions: dict[str, dict[str, str]] = {}
    for match in EN_AUDIO_DEFINITION.finditer(fields.get("subject_definitions:", "")):
        label = canonical_audio_label(match.group("label"))
        definitions[label] = {
            "description": match.group("description").strip(),
            "speaker": (re.search(r"\(S\d+\)", match.group("description"), re.IGNORECASE) or [""])[0],
        }
    summary = fields.get("summary:", "").lower()
    modes = [mode for mode in MODE_MARKERS if mode in summary]
    mode = modes[0] if len(modes) == 1 else None
    retention = {
        canonical_audio_label(match.group("label")): match.group("marker").lower()
        for match in EN_AUDIO_RETENTION.finditer(fields.get("retention_analysis:", ""))
    }
    return definitions, mode, retention


def parse_chinese_audio(prompt: str) -> dict[str, dict[str, str]]:
    role_start = prompt.find("角色与场景：")
    shot_start = prompt.find("镜头设计：")
    if role_start < 0 or shot_start < 0 or shot_start <= role_start:
        return {}
    role_prose = prompt[role_start + len("角色与场景："):shot_start]
    bindings: dict[str, dict[str, str]] = {}
    for match in ZH_AUDIO_BINDING.finditer(role_prose):
        body = match.group("body").strip()
        mode_match = re.search(r"Audio mode\s*:\s*(audio reuse|audio reference)", body, re.IGNORECASE)
        retention_match = re.search(
            r"Retention\s*:\s*(fully_copy|partially_copy|reference|weak_reference)",
            body,
            re.IGNORECASE,
        )
        bindings[canonical_audio_label(match.group("label"))] = {
            "body": body,
            "mode": mode_match.group(1).lower() if mode_match else "",
            "retention": retention_match.group(1).lower() if retention_match else "",
        }
    return bindings


def attrs(raw: str) -> dict[str, str]:
    return {name.lower(): html.unescape(value) for name, _q, value in ATTRIBUTE.findall(raw)}


def prompt_blocks(source: str) -> list[str]:
    blocks: list[str] = []
    for match in CONTAINER.finditer(source):
        classes = attrs(match.group("attrs")).get("class", "").split()
        if "prompt-block" in classes:
            blocks.append(html.unescape(match.group("prompt")).strip())
    return blocks


def lint_boundaries(source: str, unit_count: int) -> list[str]:
    errors: list[str] = []
    tags = list(BOUNDARY_TAG.finditer(source))
    expected = max(0, unit_count - 1)
    if len(tags) != expected:
        errors.append(f"HTML: expected {expected} data-h3-boundary record(s) for {unit_count} ordered H3 units, found {len(tags)}")
    seen: set[str] = set()
    for index, match in enumerate(tags, start=1):
        values = {name.lower(): html.unescape(value).strip() for name, _q, value in ATTRIBUTE.findall(match.group(0))}
        boundary_id = values.get("data-h3-boundary", "")
        if not boundary_id or boundary_id in seen:
            errors.append(f"boundary {index}: data-h3-boundary is missing or duplicated")
        seen.add(boundary_id)
        if values.get("data-boundary-strategy", "") not in VALID_BOUNDARY_STRATEGIES:
            errors.append(f"boundary {index}: invalid or missing boundary strategy")
        for key in ("data-outgoing-frame", "data-incoming-frame", "data-cut-trigger"):
            if not values.get(key, ""):
                errors.append(f"boundary {index}: {key} is missing or empty")
    return errors


def lint_chinese(prompt: str, index: int) -> tuple[list[str], list[re.Match[str]]]:
    errors: list[str] = []
    if TITLE.search(prompt) is None:
        errors.append("missing title in the form ‘中文分镜版（或审稿版）｜H3-XXX｜N秒’")
    sections = ["角色与场景：", "镜头设计：", "声音：", "音乐："]
    offsets = [prompt.find(label) for label in sections]
    if any(offset < 0 for offset in offsets) or offsets != sorted(offsets):
        errors.append("sections must be ordered: 角色与场景 → 镜头设计 → 声音 → 音乐")
        role_prose = prompt
        shot_prose = prompt
    else:
        role_prose = prompt[offsets[0] + len(sections[0]): offsets[1]]
        shot_prose = prompt[offsets[1] + len(sections[1]): offsets[2]]
    shots = list(ZH_SHOT.finditer(shot_prose))
    if not shots:
        errors.append("镜头设计 contains no timed shot entries")
    else:
        numbers = [int(m.group("number")) for m in shots]
        if numbers != list(range(1, len(numbers) + 1)):
            errors.append(f"shot numbers are not consecutive from 1: {numbers}")
        previous_end: float | None = None
        for match in shots:
            start, end = float(match.group("start")), float(match.group("end"))
            if end <= start:
                errors.append(f"镜头{match.group('number')} has a non-positive duration")
            if previous_end is None and abs(start) > 1e-6:
                errors.append("镜头1 must start at 0.0 seconds")
            if previous_end is not None and abs(start - previous_end) > 1e-6:
                errors.append(f"镜头{match.group('number')} starts at {start:g}s but previous shot ends at {previous_end:g}s")
            previous_end = end
    if LEGACY_IN_CHINESE.search(prompt):
        errors.append("Chinese storyboard must not contain English fields, visual H3 reference labels, <d>, or (Sx)")
    audio_labels = {canonical_audio_label(label) for label in AUDIO_LABEL.findall(prompt)}
    binding_matches = list(ZH_AUDIO_BINDING.finditer(role_prose))
    binding_counts: dict[str, int] = {}
    for match in binding_matches:
        label = canonical_audio_label(match.group("label"))
        binding_counts[label] = binding_counts.get(label, 0) + 1
        body = match.group("body")
        if re.search(r"目标(?:角色|来源)\s+[^；;]+", body) is None:
            errors.append(f"{label} Chinese binding must name one 目标角色 or 目标来源")
        modes = re.findall(r"Audio mode\s*:\s*(audio reuse|audio reference)", body, re.IGNORECASE)
        if len(modes) != 1:
            errors.append(f"{label} Chinese binding requires exactly one Audio mode")
        markers = re.findall(
            r"Retention\s*:\s*(fully_copy|partially_copy|reference|weak_reference)",
            body,
            re.IGNORECASE,
        )
        if len(markers) != 1:
            errors.append(f"{label} Chinese binding requires exactly one Retention marker")
        elif len(modes) == 1 and markers[0].lower() not in MODE_MARKERS[modes[0].lower()]:
            errors.append(f"{label} Chinese marker {markers[0].lower()} is incompatible with {modes[0].lower()}")
        if "作用范围：" not in body:
            errors.append(f"{label} Chinese binding is missing 作用范围")
        if "排除：" not in body:
            errors.append(f"{label} Chinese binding is missing 排除")
    if audio_labels:
        for label in sorted(audio_labels):
            if binding_counts.get(label, 0) != 1:
                errors.append(f"{label} must have exactly one filename-free Chinese binding under 角色与场景")
            if len(re.findall(re.escape(label), shot_prose, re.IGNORECASE)) < 1:
                errors.append(f"{label} must be cited at its actual Chinese vocal/audio event in 镜头设计")
        if set(binding_counts) != audio_labels:
            errors.append("Chinese audio labels must match exactly across 角色与场景 bindings and 镜头设计 events")
    elif re.search(
        r"音频参考｜Ref2VA|Audio mode\s*:|Retention\s*:|作用范围：[^\n]*(?:音色|波形|声音)",
        prompt,
        re.IGNORECASE,
    ):
        errors.append("Chinese audio-routing language is present without any approved <Audio N> label")
    if AUDIO_FILENAME_IN_PROMPT.search(prompt):
        errors.append("audio filenames are operator metadata and must not appear in a copyable prompt")
    if "|" in shot_prose:
        errors.append("镜头设计 contains ASCII table delimiter ‘|’")
    for name, pattern in CHINESE_AUTHORING_LEAKS.items():
        if pattern.search(shot_prose):
            errors.append(f"authoring-template leakage ({name})")
    return [f"Chinese block {index}: {e}" for e in errors], shots


def section_slices(prompt: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    matches: list[tuple[str, int, int]] = []
    for label in EN_SECTIONS:
        found = list(re.finditer(rf"^{re.escape(label)}\s*$", prompt, re.MULTILINE | re.IGNORECASE))
        if len(found) != 1:
            errors.append(f"field {label} must appear exactly once")
        elif found:
            matches.append((label, found[0].start(), found[0].end()))
    if len(matches) != len(EN_SECTIONS) or [m[0].lower() for m in sorted(matches, key=lambda x: x[1])] != [s.lower() for s in EN_SECTIONS]:
        errors.append("six fields must appear in canonical order")
        return {}, errors
    ordered = sorted(matches, key=lambda x: x[1])
    values: dict[str, str] = {}
    for i, (label, _start, end) in enumerate(ordered):
        next_start = ordered[i + 1][1] if i + 1 < len(ordered) else len(prompt)
        values[label] = prompt[end:next_start].strip()
        if not values[label]:
            errors.append(f"field {label} is empty")
    return values, errors


def lint_english(prompt: str, index: int) -> tuple[list[str], list[re.Match[str]]]:
    fields, errors = section_slices(prompt)
    shots: list[re.Match[str]] = []
    if fields:
        defined = REFERENCE_LABEL.findall(fields["subject_definitions:"])
        if not defined:
            errors.append("subject_definitions must define at least one real reference label")
        normalized_defined = {label.lower() for label in defined}
        used = {label.lower() for label in REFERENCE_LABEL.findall(prompt)}
        unresolved = sorted(used - normalized_defined)
        if unresolved:
            errors.append(f"unresolved reference labels: {unresolved}")
        retention = fields["retention_analysis:"]
        for label in normalized_defined:
            entries = re.findall(
                rf"^\s*{re.escape(label)}(?=\s*(?:\(|:|-))",
                retention,
                re.IGNORECASE | re.MULTILINE,
            )
            if len(entries) != 1:
                errors.append(f"{label} must have exactly one retention_analysis entry")
        if not re.match(r"^\[[^\]\n]+\]\s+", fields["summary:"]):
            errors.append("summary must start with a square-bracketed task-type prefix")
        audio_labels = {canonical_audio_label(label) for label in AUDIO_LABEL.findall(prompt)}
        audio_definition_matches = list(EN_AUDIO_DEFINITION.finditer(fields["subject_definitions:"]))
        audio_retention_matches = list(EN_AUDIO_RETENTION.finditer(retention))
        summary_modes = [mode for mode in MODE_MARKERS if mode in fields["summary:"].lower()]
        if AUDIO_FILENAME_IN_PROMPT.search(prompt):
            errors.append("audio filenames are operator metadata and must not appear in a copyable prompt")
        if audio_labels:
            definition_counts: dict[str, int] = {}
            for match in audio_definition_matches:
                label = canonical_audio_label(match.group("label"))
                definition_counts[label] = definition_counts.get(label, 0) + 1
                description = match.group("description")
                if re.search(r"voice|timbre|vocal|speaker|dialogue|narrat", description, re.IGNORECASE) and re.search(r"\(S\d+\)", description) is None:
                    errors.append(f"{label} is a character voice but is not bound to the target (Sx) source")
            retention_counts: dict[str, int] = {}
            for match in audio_retention_matches:
                label = canonical_audio_label(match.group("label"))
                retention_counts[label] = retention_counts.get(label, 0) + 1
            for label in sorted(audio_labels):
                if definition_counts.get(label, 0) != 1:
                    errors.append(f"{label} must have exactly one English semantic source definition")
                if retention_counts.get(label, 0) != 1:
                    errors.append(f"{label} must have exactly one compatible English retention entry")
                if len(re.findall(re.escape(label), fields["detailed_description:"], re.IGNORECASE)) < 1:
                    errors.append(f"{label} must be cited at its actual English vocal/audio event")
            defined_audio = {canonical_audio_label(match.group("label")) for match in audio_definition_matches}
            retained_audio = {canonical_audio_label(match.group("label")) for match in audio_retention_matches}
            if defined_audio != audio_labels or retained_audio != audio_labels:
                errors.append("English audio labels must match exactly across definitions, retention, and detailed_description")
            voice_speakers = [
                speaker.group(0).casefold()
                for match in audio_definition_matches
                if re.search(r"voice|timbre|vocal|speaker|dialogue|narrat", match.group("description"), re.IGNORECASE)
                for speaker in [re.search(r"\(S\d+\)", match.group("description"), re.IGNORECASE)]
                if speaker is not None
            ]
            if len(voice_speakers) != len(set(voice_speakers)):
                errors.append("English audio map assigns more than one active slot to the same target (Sx) source")
            if len(summary_modes) != 1:
                errors.append("an active English audio map requires exactly one audio reuse|audio reference task type")
            else:
                mode = summary_modes[0]
                for match in audio_retention_matches:
                    marker = match.group("marker").lower()
                    if marker not in MODE_MARKERS[mode]:
                        errors.append(f"{canonical_audio_label(match.group('label'))} marker {marker} is incompatible with {mode}")
        elif summary_modes or re.search(r"audio reuse|audio reference", retention, re.IGNORECASE):
            errors.append("English audio-routing language is present without any approved <Audio N> label")
        shots = list(EN_SHOT.finditer(fields["detailed_description:"]))
        if not shots:
            errors.append("detailed_description contains no [Shot N] entries")
        else:
            numbers = [int(m.group("number")) for m in shots]
            if numbers != list(range(1, len(numbers) + 1)):
                errors.append(f"English shot numbers are not consecutive from 1: {numbers}")
            if shots[0].group("minute") is not None:
                errors.append("[Shot 1] must not carry a timestamp")
            for match in shots[1:]:
                if match.group("minute") is None:
                    errors.append(f"[Shot {match.group('number')}] lacks an At MM:SS.mmm cut time")
        if EN_AUTHORING_LEAK.search(fields["detailed_description:"]):
            errors.append("English detailed_description contains relative or authoring-template language")
        previous_end = 0
        for event in DIALOGUE_TAG.finditer(fields["detailed_description:"]):
            preceding = fields["detailed_description:"][previous_end:event.start()]
            if re.search(r"\(S\d+\)", preceding[-700:]) is None:
                errors.append("every <d> event must have an immediately preceding real (Sx) vocal source")
            previous_end = event.end()
        music = fields["non_diegetic_music:"]
        if re.search(r"^\s*N/A\s*$", music, re.IGNORECASE) is None and len(music.split()) < 4:
            errors.append("non_diegetic_music must be N/A or a concrete English score cue")
    return [f"English block {index}: {e}" for e in errors], shots


def shot_cut_seconds(match: re.Match[str]) -> float:
    return int(match.group("minute")) * 60 + float(match.group("second"))


def clean_zh_dialogue(prompt: str) -> list[str]:
    shot_start = prompt.find("镜头设计：")
    sound_start = prompt.find("声音：")
    prose = (
        prompt[shot_start + len("镜头设计："):sound_start]
        if shot_start >= 0 and sound_start > shot_start
        else prompt
    )
    return [m.group("line").strip().strip("“”") for m in ZH_DIALOGUE.finditer(prose)]


def clean_en_dialogue(prompt: str) -> list[str]:
    return [m.group("text").strip() for m in DIALOGUE_TAG.finditer(prompt)]


def zh_machine_section_slices(prompt: str) -> tuple[dict[str, str], list[str]]:
    """切片并校验中文机读六段式的六大顶层字段顺序与非空性。"""
    errors: list[str] = []
    matches: list[tuple[str, int, int]] = []
    for label in ZH_MACHINE_SECTIONS:
        found = list(re.finditer(rf"^{re.escape(label)}\s*$", prompt, re.MULTILINE))
        if len(found) != 1:
            errors.append(f"字段 {label} 必须且只能出现一次")
        elif found:
            matches.append((label, found[0].start(), found[0].end()))
    if len(matches) != len(ZH_MACHINE_SECTIONS) or [m[0] for m in sorted(matches, key=lambda x: x[1])] != ZH_MACHINE_SECTIONS:
        errors.append("中文机读六段式必须按标准顺序出现")
        return {}, errors
    ordered = sorted(matches, key=lambda x: x[1])
    values: dict[str, str] = {}
    for i, (label, _start, end) in enumerate(ordered):
        next_start = ordered[i + 1][1] if i + 1 < len(ordered) else len(prompt)
        values[label] = prompt[end:next_start].strip()
        if not values[label]:
            errors.append(f"字段 {label} 不能为空")
    return values, errors


def lint_chinese_machine(prompt: str, index: int) -> tuple[list[str], list[re.Match[str]]]:
    """校验单个中文机读六段式提示词块的结构、任务类型与镜头标记。"""
    fields, errors = zh_machine_section_slices(prompt)
    shots: list[re.Match[str]] = []
    if fields:
        desc = fields["镜头详述："]
        shots = list(EN_SHOT.finditer(desc))
        if not shots:
            shots = list(re.finditer(r"\[镜头\s*(?P<number>\d+)\](?:\s+(?:At\s+)?(?P<minute>\d{2}):(?P<second>\d{2}(?:\.\d{3})))?", desc, re.IGNORECASE))
        if not shots:
            errors.append("镜头详述 中未找到合规的 [镜头 N] 标记")
        if not re.match(r"^\[[^\]\n]+\]\s+", fields["任务摘要："]):
            errors.append("任务摘要 必须以方括号开头的任务类型前缀开始，例如 [参考生成]")
    return [f"Chinese machine block {index}: {e}" for e in errors], shots


def lint_pair(zh: str, en: str, index: int, zh_shots: list[re.Match[str]], en_shots: list[re.Match[str]]) -> list[str]:
    errors: list[str] = []
    if len(zh_shots) != len(en_shots):
        errors.append(f"shot-count mismatch: Chinese {len(zh_shots)} vs English {len(en_shots)}")
    else:
        zh_cuts = [float(m.group("start")) for m in zh_shots[1:]]
        en_cuts = [shot_cut_seconds(m) for m in en_shots[1:] if m.group("minute") is not None]
        if len(zh_cuts) != len(en_cuts) or any(abs(a - b) > 1e-3 for a, b in zip(zh_cuts, en_cuts)):
            errors.append(f"cut-time mismatch: Chinese {zh_cuts} vs English {en_cuts}")
    zh_lines, en_lines = clean_zh_dialogue(zh), clean_en_dialogue(en)
    if zh_lines != en_lines:
        errors.append(f"dialogue mismatch: Chinese {zh_lines!r} vs English {en_lines!r}")
    zh_no_music = re.search(r"^音乐：\s*\n\s*无配乐。?\s*$", zh, re.MULTILINE) is not None
    en_na = re.search(r"^non_diegetic_music:\s*\n\s*N/A\s*$", en, re.MULTILINE | re.IGNORECASE) is not None
    if zh_no_music != en_na:
        errors.append("music mismatch: Chinese 无配乐 and English N/A must map one-to-one")
    zh_audio = parse_chinese_audio(zh)
    en_fields, _field_errors = section_slices(en)
    en_definitions, en_mode, en_retention = parse_english_audio(en_fields) if en_fields else ({}, None, {})
    zh_audio_labels = {canonical_audio_label(label) for label in AUDIO_LABEL.findall(zh)}
    en_audio_labels = {canonical_audio_label(label) for label in AUDIO_LABEL.findall(en)}
    if zh_audio_labels != en_audio_labels:
        errors.append(f"audio-label mismatch: Chinese {sorted(zh_audio_labels)} vs English {sorted(en_audio_labels)}")
    for label in sorted(zh_audio_labels & en_audio_labels):
        zh_entry = zh_audio.get(label, {})
        if zh_entry.get("mode") and en_mode and zh_entry["mode"] != en_mode:
            errors.append(f"{label} audio-mode mismatch: Chinese {zh_entry['mode']} vs English {en_mode}")
        en_marker = en_retention.get(label, "")
        if zh_entry.get("retention") and en_marker and zh_entry["retention"] != en_marker:
            errors.append(
                f"{label} retention mismatch: Chinese {zh_entry['retention']} vs English {en_marker}"
            )
    return [f"pair {index}: {e}" for e in errors]


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint paired MiniMax H3 prompt blocks embedded in HTML.")
    parser.add_argument("html_file", type=pathlib.Path)
    args = parser.parse_args()
    source = args.html_file.read_text(encoding="utf-8")
    blocks = prompt_blocks(source)
    chinese = [p for p in blocks if TITLE.search(p)]
    chinese_machine = [p for p in blocks if ZH_MACHINE_START.search(p)]
    english = [p for p in blocks if re.search(r"^subject_definitions:\s*$", p, re.MULTILINE | re.IGNORECASE)]
    errors: list[str] = []
    if not chinese:
        errors.append("HTML: no Chinese director-storyboard prompt blocks found")
    if len(chinese) != len(english):
        errors.append(f"HTML: expected one English companion per Chinese block, found {len(chinese)} Chinese and {len(english)} English")
    has_tri_modal = len(chinese_machine) > 0
    if has_tri_modal:
        if len(chinese_machine) != len(chinese):
            errors.append(f"HTML: expected {len(chinese)} Chinese machine prompts, found {len(chinese_machine)}")
        expected_total = len(chinese) + len(chinese_machine) + len(english)
    else:
        expected_total = len(chinese) + len(english)
    if len(blocks) != expected_total:
        errors.append("HTML: one or more prompt-block containers are neither canonical Chinese, Chinese machine, nor canonical English")
    zh_results: list[list[re.Match[str]]] = []
    en_results: list[list[re.Match[str]]] = []
    for i, prompt in enumerate(chinese, 1):
        block_errors, shots = lint_chinese(prompt, i)
        errors.extend(block_errors)
        zh_results.append(shots)
    if has_tri_modal:
        for i, prompt in enumerate(chinese_machine, 1):
            block_errors, _shots = lint_chinese_machine(prompt, i)
            errors.extend(block_errors)
    for i, prompt in enumerate(english, 1):
        block_errors, shots = lint_english(prompt, i)
        errors.extend(block_errors)
        en_results.append(shots)
    for i, (zh, en, zh_shots, en_shots) in enumerate(zip(chinese, english, zh_results, en_results), 1):
        errors.extend(lint_pair(zh, en, i, zh_shots, en_shots))
    if has_tri_modal:
        for i, (zh_m, en) in enumerate(zip(chinese_machine, english), 1):
            zh_m_lines, en_lines = clean_en_dialogue(zh_m), clean_en_dialogue(en)
            if zh_m_lines != en_lines:
                errors.append(f"pair {i}: Chinese machine dialogue {zh_m_lines!r} vs English {en_lines!r} mismatch")
    errors.extend(lint_boundaries(source, len(chinese)))
    if errors:
        print(f"FAIL: {len(errors)} issue(s) across {len(chinese)} H3 prompt pair(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    mode_text = "tri-modal (storyboard + Chinese execution + English execution)" if has_tri_modal else "paired H3 Chinese storyboard + English six-section"
    print(f"PASS: {len(chinese)} {mode_text} prompt(s) satisfy structural and parity lint checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
