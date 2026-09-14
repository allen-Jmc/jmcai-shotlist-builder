# MiniMax H3 Audio Reference Binding

Read this reference for every MiniMax H3 production intake to resolve audio-reference intent. Build an upload map only for requested references. Its purpose is to avoid silently skipping the user's choice or attaching audio to the wrong character. The upload map is operator metadata; both copyable prompts carry the same model-facing `<Audio N>` relationship, while exact filenames remain outside them.

## 1. Conditional trigger

First record `AUDIO_REFERENCE_INTENT` with status, user's answer, and project/scene scope:

- `unknown`: the user has not decided. Ask once: “本项目是否使用音频参考，例如角色音色或原声复用？” No attachment, silence, or a no-background-music instruction does not mean refusal. Continue independent assets, blocking drafts, and timing work, but label sound-bearing prompts provisional and do not release them as ready for generation.
- `declined`: the user explicitly declines. Skip upload mapping and use the locked textual `VOICE_BIBLE`; do not ask again in later units unless the user changes this decision.
- `requested`: the user wants reference audio, including when files are not ready. Collect exact files, source/character, scope and reuse/reference mode. Pending files are not confirmed bindings; never invent upload tokens. Continue independent work while resolving them.

Ask the intent question separately from the later exact-file binding question. A skill-maintenance-only request does not trigger production intake. No-background-music remains an independent constraint in every state; reference music must not leak into a no-score project.

Activate `AUDIO_REFERENCE_MAP` when at least one of these is true:

- the user uploads a standalone audio file and intends H3 to copy or reference it;
- the user names an audio filename, planned filename, or enabled video-audio track as a voice source;
- the user asks to preserve original dialogue audio, match a voice, reference timbre, cadence, delivery, breath, beat, or another audible characteristic.

An uploaded but unexplained audio file is ambiguous. Ask what it should control and stop before prompt generation. A textual request for rain, footsteps, room tone, newly generated dialogue, or another target-video sound does not activate this map unless the user also identifies a real reference audio input.

Only after explicit refusal (`declined`), do not ask an audio-mapping question or create `AUDIO_REFERENCE_MAP`. Emit no `<Audio N>`, `Audio mode`, `Retention`, `audio reuse`, or `audio reference` routing syntax in either prompt. Preserve the no-reference `VOICE_BIBLE` workflow. Lack of a map alone is never evidence that the intent question was answered.

## 2. Confirm the operator upload map

Before blocking or prompts, present one row per proposed voice reference and obtain explicit confirmation. Record:

| Field | Required value |
| --- | --- |
| `audio_label` | Clip-local `<Audio N>` label determined by the real upload/input order |
| `filename` | Exact uploaded filename, or exact planned filename if upload is still pending |
| `target_character` | One named character or explicit narrator/off-screen source |
| `vocal_role` | On-screen dialogue, off-screen voice-over, singing, or another concrete vocal role |
| `audio_mode` | `audio reuse` or `audio reference` |
| `retention_marker` | `fully_copy`, `partially_copy`, `reference`, or `weak_reference` |
| `copied_or_referenced_scope` | Exact time range/layer for reuse, or exact timbre/delivery traits for reference |
| `excluded_content` | Words, ambience, music, noise, or other layers that must not transfer |

Use the exact filename only in the operator-facing `AUDIO_UPLOAD_MAP`, asset table, or per-unit upload checklist; do not copy it into either model-facing prompt. Default to a one-to-one lock: one uploaded slot maps to one character, and one character maps to one active voice-reference slot. If filenames, slot order, or target characters are missing, duplicated, or ambiguous, ask the user to resolve the rows and stop. A mixed track containing multiple character voices should be split into separate files. Allow a shared or mixed-track exception only after the user explicitly approves the non-one-to-one mapping and the map records each speaker/time range unambiguously.

Once approved, freeze the filename-to-character relationship across the requested scope. Compile a clip-local upload checklist before each independent H3 unit: the first attached audio becomes `<Audio 1>`, the second becomes `<Audio 2>`, and so on. The same character may use a different clip-local number only when the operator checklist explicitly changes the attachment order; the underlying source file and target character remain unchanged.

## 3. Choose reuse versus reference truthfully

- Use `audio reuse` when the source signal itself is copied. Use `fully_copy` only when it becomes the complete final audio track. Use `partially_copy` for selected time ranges or layers, or when newly generated ambience/dialogue/effects are mixed around copied audio.
- Use `audio reference` when the source signal is not copied. Use `reference` for specific timbre, resonance, articulation, cadence, delivery, rhythm, or texture. Use `weak_reference` only for broad category or atmosphere.
- Do not use `fully_copy` for a voice clip when the prompt also creates new rain, effects, dialogue, or music around it; that is normally `partially_copy`.
- When only voice timbre or delivery is referenced, keep the target script's exact dialogue and explicitly exclude the reference file's original words and waveform.

## 4. Chinese director storyboard

Keep the five existing top-level sections unchanged and keep this block independently readable. When the current unit uses approved reference audio, add one compact binding line per active audio inside `角色与场景：` using this shape:

```text
<Audio 1>：目标角色 FLICK；Audio mode: audio reference；Retention: reference；作用范围：音色、共鸣、咬字、呼吸与说话节奏；排除：原音频台词、环境声、音乐与噪声。
```

Use the exact approved slot number, target character/source, mode, compatible retention marker, scope, and exclusions. Never include the source filename. At the actual vocal event in `镜头设计：`, cite the same token naturally, for example `FLICK使用 <Audio 1> 的音色与说话方式参考，并以……说：`. The label must therefore appear at least once in the binding area and once at its owning vocal event.

At each vocal event, name the real character in natural Chinese and keep the complete written voice baseline, line-specific emotion, pace, breath, pause, and intention before the exact dialogue. The audio reference strengthens acoustic identity but does not replace playable vocal direction.

## 5. English six-section binding

For the paired English prompt, mirror the approved map in all applicable locations:

1. `subject_definitions`: define `<Audio N>` by its semantic role, target character/source, and speaker ID when it is a character voice. Do not include the source filename.
2. `summary`: include `audio reuse` or `audio reference` in the task-type prefix and describe the relationship.
3. `retention_analysis`: use exactly one compatible audio marker per label and do not include `(Sx)`.
4. `detailed_description`: cite `<Audio N>` at the actual vocal/audio event and bind it to the same real `(Sx)` source used by the dialogue.
5. `overall_soundscape` or `non_diegetic_music`: mention copy/reference behavior only when that audio actually supplies the corresponding ambience/effect or audience-only music layer.

Example definition:

```text
<Audio 1> is the voice-timbre and speaking-delivery reference for <Subject 1> (S1).
```

Do not bind the label to a different speaker or import the reference audio's original words when only timbre/delivery is referenced. If the upload order changes, update both the operator checklist and every model-facing `<Audio N>` occurrence before delivery.

## 6. Pair parity and review

Before delivery, compare the approved `AUDIO_REFERENCE_MAP`, per-unit upload checklist, and English prompt:

- each `<Audio N>` label resolves to the same upload position, exact operator-side filename, and target character/source;
- the English summary task type matches the map's `audio reuse` or `audio reference` mode;
- English `retention_analysis` uses the compatible marker and scope;
- every voice-reference label appears at its target character's actual vocal event in the English prompt;
- the Chinese storyboard contains the same confirmed `<Audio N>` at its compact binding line and owning vocal event, with matching mode, retention, scope, and target character, but no filename or visual H3 reference tag;
- no unrequested audio label, file, character mapping, source words, ambience, or music has been added;
- when the map is inactive, the English prompt contains no audio-reference routing language.

Any missing upload slot, unresolved character, duplicate one-to-one assignment, mode mismatch, filename leakage into a prompt, or slot-label drift blocks prompt generation or delivery.
