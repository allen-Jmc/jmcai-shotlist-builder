#!/usr/bin/env python3
"""Regression tests for paired Chinese/English MiniMax H3 delivery."""

from __future__ import annotations

import pathlib
import subprocess
import sys
import tempfile


SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
PROMPT_LINT = SCRIPT_DIR / "h3_prompt_lint.py"
UNIT_LINT = SCRIPT_DIR / "h3_unit_lint.py"


def storyboard_prompt(
    *,
    leaked: bool = False,
    tagged: bool = False,
    dependency: bool = False,
    scored: bool = False,
    audio: bool = False,
) -> str:
    dialogue = "苏晚使用年轻中国女性的低中音、清晰咬字和稳定语速：\n我会回来。"
    audio_binding = ""
    if audio:
        audio_binding = (
            "\n<Audio 1>：目标角色 苏晚；Audio mode: audio reference；Retention: reference；"
            "作用范围：音色、共鸣、咬字、呼吸与说话节奏；"
            "排除：原音频台词、环境声、音乐、噪声与原始波形。"
        )
        dialogue = "苏晚使用 <Audio 1> 的音色与说话方式参考，以年轻中国女性的低中音、清晰咬字和稳定语速说：\n我会回来。"
    if dependency:
        dialogue = "苏晚使用与H3-001完全一致的低中音：\n我会回来。"
    if tagged:
        dialogue = "<Subject 1> (S1) <d>[Chinese] 我会回来。</d>"
    shot_two = "\n【镜头2｜5.0—12.0秒】\n切至苏晚正面近景，她闭口看向窗外，保持稳定姿势至结束。"
    if leaked:
        shot_two = "\n【镜头2｜5.0—12.0秒】\n在第一个决定性动作上切至中景或近景，新增下一条原文信息。"
    music = "稀疏钢琴单音在最后一个呼吸前进入，停在尾态前。" if scored else "无配乐。"
    return f"""中文审稿版｜H3-001｜12秒

角色与场景：
苏晚站在安静室内的窗边，穿深色针织衫，夜色透过玻璃落在她左侧脸颊。{audio_binding}

镜头设计：
【镜头1｜0.0—5.0秒】
50毫米固定侧面中景，苏晚位于画面左侧，先看向窗外再收回视线。{dialogue}{shot_two}

声音：
安静室内底噪与轻微衣料摩擦声持续存在；台词近而清楚。

音乐：
{music}"""


def six_section_prompt(
    *,
    cut: str = "00:05.000",
    dialogue: str = "我会回来。",
    bound: bool = True,
    scored: bool = False,
    bad_order: bool = False,
    audio: bool = False,
    audio_mode: str = "audio reference",
    audio_marker: str = "reference",
) -> str:
    vocal = "<Subject 1> (S1)" if bound else "<Subject 1>"
    audio_definition = ""
    audio_retention = ""
    audio_event = ""
    task_types = "reference generation"
    if audio:
        audio_definition = "\n<Audio 1> is the voice-timbre and speaking-delivery reference for <Subject 1> (S1)."
        audio_retention = f"\n<Audio 1>: {audio_marker} - its vocal timbre guides <Subject 1> without copying the source words or waveform."
        audio_event = ", using the voice-timbre reference from <Audio 1>,"
        task_types += f" + {audio_mode}"
    music = "A sparse solo-piano note enters before the final breath and stops before the landing frame." if scored else "N/A"
    summary = f"summary:\n[{task_types}] The target video shows <Subject 1> making a quiet promise beside a window."
    retention = f"retention_analysis:\n<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - identity, wardrobe, and screen position are retained.{audio_retention}"
    if bad_order:
        summary, retention = retention, summary
    return f"""subject_definitions:
<Subject 1> is Su Wan from character_suwan_fourview.png, a young Chinese woman wearing a dark knitted top.{audio_definition}

{summary}

{retention}

detailed_description:
The target video uses restrained live-action photography and contains no subtitles, captions, translations, or dialogue text.
[Shot 1] A locked 50 mm eye-level side medium shot places <Subject 1> at frame left beside a dark window. She looks outside, brings her gaze back, and {vocal}{audio_event} says in a clear young female low-mid register at a steady pace, <d>[Chinese] {dialogue}</d>
[Shot 2] At {cut}, the video cuts to a frontal close-up. She closes her lips, returns her gaze to the window, and holds the stable final pose through 00:12.000.

overall_soundscape:
Quiet indoor room tone and faint fabric movement continue throughout.

non_diegetic_music:
{music}"""


def chinese_machine_prompt(
    *,
    dialogue: str = "我会回来。",
    scored: bool = False,
    bad_order: bool = False,
) -> str:
    """构造合规的中文机读六段式测试夹具提示词。"""
    music = "稀疏钢琴单音在最后一个呼吸前进入，停在尾态前。" if scored else "无配乐。"
    summary = "任务摘要：\n[参考生成] 目标视频展示 <主体 1> 在窗边许下安静承诺。"
    retention = "保留分析：\n<主体 1>：reference, 保留角色身份五官与服装，窗边站位与动作由本场景生成。"
    if bad_order:
        summary, retention = retention, summary
    return f"""主体定义：
<主体 1>：苏晚，年轻中国女性，穿深色针织衫。

{summary}

{retention}

镜头详述：
[镜头 1] 0.0—5.0秒。50毫米固定侧面中景，<主体 1> 位于画面左侧，先看向窗外再收回视线。(S1) 以低中音语速说：
<d>[中文]{dialogue}</d>
[镜头 2] 00:05.000至00:12.000。正面近景，她闭口看向窗外，保持稳定姿势至结束。

环境音响：
安静室内底噪与轻微衣料摩擦声持续存在。

非剧情音乐：
{music}"""


def escape(prompt: str) -> str:
    return prompt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def html_document(
    *,
    zh: str,
    en: str | None,
    zh_machine: str | None = None,
    displayed_runtime: int = 12,
    dialogue_chars: int = 4,
) -> str:
    en_block = "" if en is None else f'<pre class="prompt-block h3-prompt-en">{escape(en)}</pre>'
    zh_machine_block = (
        "" if zh_machine is None else f'<pre class="prompt-block prompt-zh-machine">{escape(zh_machine)}</pre>'
    )
    return f"""<!doctype html><html><body>
<div data-h3-packed-runtime-seconds="{displayed_runtime}"><b>{displayed_runtime}s</b> packed runtime</div>
<article class="h3-unit" data-h3-unit="H3-001" data-unit-kind="dialogue"
 data-duration-seconds="12" data-dialogue-effective-chars="{dialogue_chars}"
 data-relationship-turn="承诺" data-action-chain="开口到闭口"
 data-opening-state="人物静止" data-exit-state="人物闭口" data-duration-exception-reason="">
<b>中文审稿版｜H3-001｜12秒</b><pre class="prompt-block">{escape(zh)}</pre>
{zh_machine_block}
{en_block}
</article></body></html>"""


def run(script: pathlib.Path, source: str) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as tmp:
        fixture = pathlib.Path(tmp) / "fixture.html"
        fixture.write_text(source, encoding="utf-8")
        return subprocess.run([sys.executable, str(script), str(fixture)], text=True, capture_output=True, check=False)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    valid = html_document(zh=storyboard_prompt(), en=six_section_prompt())
    valid_prompt = run(PROMPT_LINT, valid)
    valid_unit = run(UNIT_LINT, valid)
    require(valid_prompt.returncode == 0, valid_prompt.stdout + valid_prompt.stderr)
    require(valid_unit.returncode == 0, valid_unit.stdout + valid_unit.stderr)
    require("<Audio " not in storyboard_prompt() and "Audio mode" not in storyboard_prompt(), "no-audio Chinese branch leaked audio syntax")
    require("<Audio " not in six_section_prompt() and "audio reference" not in six_section_prompt(), "no-audio English branch leaked audio syntax")

    valid_tri_modal = html_document(
        zh=storyboard_prompt(),
        zh_machine=chinese_machine_prompt(),
        en=six_section_prompt(),
    )
    valid_tri_result = run(PROMPT_LINT, valid_tri_modal)
    require(valid_tri_result.returncode == 0, valid_tri_result.stdout + valid_tri_result.stderr)
    require("tri-modal" in valid_tri_result.stdout, f"expected tri-modal PASS message, got {valid_tri_result.stdout}")

    bad_tri_dialogue = run(
        PROMPT_LINT,
        html_document(
            zh=storyboard_prompt(),
            zh_machine=chinese_machine_prompt(dialogue="我绝不回来。"),
            en=six_section_prompt(),
        ),
    )
    require(bad_tri_dialogue.returncode != 0 and "Chinese machine dialogue" in bad_tri_dialogue.stdout, bad_tri_dialogue.stdout)

    valid_audio = html_document(zh=storyboard_prompt(audio=True), en=six_section_prompt(audio=True))
    valid_audio_result = run(PROMPT_LINT, valid_audio)
    require(valid_audio_result.returncode == 0, valid_audio_result.stdout + valid_audio_result.stderr)

    leaked_audio_filename = run(
        PROMPT_LINT,
        html_document(
            zh=storyboard_prompt(audio=True),
            en=six_section_prompt(audio=True).replace(
                "<Audio 1> is the voice-timbre",
                "<Audio 1> is suwan_voice.wav, the voice-timbre",
            ),
        ),
    )
    require(leaked_audio_filename.returncode != 0 and "operator metadata" in leaked_audio_filename.stdout, leaked_audio_filename.stdout)

    incompatible_audio_mode = run(
        PROMPT_LINT,
        html_document(
            zh=storyboard_prompt(audio=True),
            en=six_section_prompt(audio=True, audio_mode="audio reference", audio_marker="fully_copy"),
        ),
    )
    require(incompatible_audio_mode.returncode != 0 and "incompatible" in incompatible_audio_mode.stdout, incompatible_audio_mode.stdout)

    one_sided_audio = run(
        PROMPT_LINT,
        html_document(zh=storyboard_prompt(), en=six_section_prompt(audio=True)),
    )
    require(one_sided_audio.returncode != 0 and "audio-label mismatch" in one_sided_audio.stdout, one_sided_audio.stdout)

    chinese_only_audio = run(
        PROMPT_LINT,
        html_document(zh=storyboard_prompt(audio=True), en=six_section_prompt()),
    )
    require(chinese_only_audio.returncode != 0 and "audio-label mismatch" in chinese_only_audio.stdout, chinese_only_audio.stdout)

    missing_chinese_audio_event = run(
        PROMPT_LINT,
        html_document(
            zh=storyboard_prompt(audio=True).replace("使用 <Audio 1> 的音色与说话方式参考，以", "使用该音色与说话方式参考，以"),
            en=six_section_prompt(audio=True),
        ),
    )
    require(
        missing_chinese_audio_event.returncode != 0 and "actual Chinese vocal/audio event" in missing_chinese_audio_event.stdout,
        missing_chinese_audio_event.stdout,
    )

    duplicate_character_zh = storyboard_prompt(audio=True)
    duplicate_character_en = six_section_prompt(audio=True)
    duplicate_character_en = duplicate_character_en.replace(
        "\n\nsummary:",
        "\n<Audio 2> is the voice-timbre reference for <Subject 1> (S1).\n\nsummary:",
    ).replace(
        "\n\ndetailed_description:",
        "\n<Audio 2>: reference - its vocal timbre guides <Subject 1> without copying the source words or waveform.\n\ndetailed_description:",
    ).replace("from <Audio 1>", "from <Audio 1> and <Audio 2>")
    duplicate_character = run(
        PROMPT_LINT,
        html_document(zh=duplicate_character_zh, en=duplicate_character_en),
    )
    require(duplicate_character.returncode != 0 and "same target" in duplicate_character.stdout, duplicate_character.stdout)

    scored = html_document(zh=storyboard_prompt(scored=True), en=six_section_prompt(scored=True))
    require(run(PROMPT_LINT, scored).returncode == 0, "matched score cues should pass")

    leaked = run(PROMPT_LINT, html_document(zh=storyboard_prompt(leaked=True), en=six_section_prompt()))
    require(leaked.returncode != 0 and "authoring-template leakage" in leaked.stdout, leaked.stdout)

    tagged = run(PROMPT_LINT, html_document(zh=storyboard_prompt(tagged=True), en=six_section_prompt()))
    require(tagged.returncode != 0 and "must not contain" in tagged.stdout, tagged.stdout)

    dependency = run(PROMPT_LINT, html_document(zh=storyboard_prompt(dependency=True), en=six_section_prompt()))
    require(dependency.returncode != 0 and "跨单元音色依赖" in dependency.stdout, dependency.stdout)

    missing_en = html_document(zh=storyboard_prompt(), en=None)
    require(run(PROMPT_LINT, missing_en).returncode != 0, "missing English companion was not rejected by prompt lint")
    require(run(UNIT_LINT, missing_en).returncode != 0, "missing English companion was not rejected by unit lint")

    bad_order = run(PROMPT_LINT, html_document(zh=storyboard_prompt(), en=six_section_prompt(bad_order=True)))
    require(bad_order.returncode != 0 and "canonical order" in bad_order.stdout, bad_order.stdout)

    bad_cut = run(PROMPT_LINT, html_document(zh=storyboard_prompt(), en=six_section_prompt(cut="00:06.000")))
    require(bad_cut.returncode != 0 and "cut-time mismatch" in bad_cut.stdout, bad_cut.stdout)

    bad_dialogue = run(PROMPT_LINT, html_document(zh=storyboard_prompt(), en=six_section_prompt(dialogue="我不会回来。")))
    require(bad_dialogue.returncode != 0 and "dialogue mismatch" in bad_dialogue.stdout, bad_dialogue.stdout)

    unbound = run(PROMPT_LINT, html_document(zh=storyboard_prompt(), en=six_section_prompt(bound=False)))
    require(unbound.returncode != 0 and "vocal source" in unbound.stdout, unbound.stdout)

    bad_runtime = run(UNIT_LINT, html_document(zh=storyboard_prompt(), en=six_section_prompt(), displayed_runtime=405))
    require(bad_runtime.returncode != 0 and "405s != summed unit duration 12s" in bad_runtime.stdout, bad_runtime.stdout)

    print("PASS: H3 dual-prompt regression tests enforce external filename maps plus paired Chinese/English <Audio N> bindings, event citations, filename isolation, compatible audio modes, timing/dialogue parity, speaker binding, and runtime truth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
