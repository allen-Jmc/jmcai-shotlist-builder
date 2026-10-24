# H3 unit directing rules

These rules govern **both** serializations of a unit — the Chinese six-section prompt and
its English companion. They were previously inlined in `SKILL.md`; they live here so the
entry file stays loadable. Read this file before writing the first unit of a project and
whenever a take fails for a directing reason rather than a syntax reason.

They are not style advice. Each one corresponds to a specific failure that shows up in
generated footage: a shot that reaches its pose and idles, a reaction with no trigger, a
cut that adds no information, dialogue buried under unrelated action, a speaker whose
mouth is unreadable at the line's start.

---

# H3 unit directing rules

Every unit ships exactly **two** copyable prompts: a Chinese six-section prompt and an English six-section companion, both compiled from one unit truth. The Chinese prompt follows [MINIMAX_H3_CHINESE_MACHINE_PROMPT_SPEC.md](MINIMAX_H3_CHINESE_MACHINE_PROMPT_SPEC.md); the English companion follows [MINIMAX_H3_FULL_REFERENCE_EN.md](MINIMAX_H3_FULL_REFERENCE_EN.md).

The six Chinese top-level sections are `主体定义：`, `任务摘要：`, `保留分析：`, `镜头详述：`, `环境音响：`, `非剧情音乐：`. The six English fields are `subject_definitions:`, `summary:`, `retention_analysis:`, `detailed_description:`, `overall_soundscape:`, `non_diegetic_music:`. **There is no third prompt and no review-only storyboard block.**

The directing rules below apply to both serializations.

- The official Base Mode guide informs the internal timeline, keyframe routing, camera, dialogue, and sound design, but its English field names are not copied into the Chinese prompt.
- The Chinese prompt keeps the six top-level sections above and binds subjects through `<Subject N>` slots. When `AUDIO_REFERENCE_MAP` is active, keep the filename/slot rows in a separate operator upload checklist, use the confirmed `<Audio N>` label at the subject definition and again at the owning vocal event, and carry the target character/source, `Audio mode`, `Retention`, referenced scope, and exclusions there. Express the full written voice baseline and playable delivery naturally in Chinese as well; the audio token reinforces rather than replaces them.
- Use one strong submitted keyframe per unit whenever possible. Treat prior clips, character sheets, scene images, props, and style boards as production references for building that keyframe and define their actual roles in the English companion.
- Every independent unit is self-contained. Never write `承接上一段`, `承接 H3-001`, `同前`, `沿用上一条`, or any equivalent relative instruction inside the copyable prompt. Replace it with the complete opening geometry: location/time, light/weather, active identity and wardrobe, left/right/depth positions, eyelines, significant prop holder/location/state, and current sound bed.
- Every shot has a continuous Chinese time range. The ranges must cover the requested duration without overlap or gaps.
- State lens, framing, angle, screen geography, movement pace, current light, action onset/change/result, and visible performance chronologically in each shot.
- Allocate each shot's time from its actual screen event, not from an even division of the unit duration. Before prose, give every internal shot a timing chain: `entry trigger → visible development → information/dialogue landing → cut trigger or stable exit`. A character walking toward a prop, noticing it, bending down, opening it, and lifting it are separate playable phases; keep them in one shot only while the camera can follow the changing action without losing clarity.
- Cut when the current shot's promised action or information lands: a gaze reaches the discovered prop, a hand completes a pickup, a body crosses into a new posture, a line finishes, a listener receives its meaning, or a new action begins. Do not let a character reach the intended pose and then remain visibly idle merely to consume assigned seconds. Reassign that time to an earlier action, a source-grounded reaction, the following action, or a stable final handle; if none is justified, shorten the shot or repack the unit.
- A quiet hold is valid only when it carries a readable ongoing process—listening, deciding, an unfolding micro-expression, environmental pressure, or the final 0.8–1.0-second edit handle. Describe what remains alive in that hold. “Camera holds after she stops” without new observable information is a timing failure.
- When a user supplies an exact dialogue start time, test it against the locked words at the approved natural speech rate plus a stable tail handle. If it would force rushed speech or leave less than a safe tail, explain the conflict and move the cue to the nearest viable time, split the unit, or request a user decision; never silently accelerate the line or extend a unit beyond 15 seconds.
- Give every audible line an explicit absolute in-shot start and end time before serializing its text. Reserve a named pre-line window for the visible thought/breath/action, place the dialogue itself inside its timed window, and reserve its consequence separately. Never state only a shot range and leave the model to decide when the speaker begins. When spoken words are the shot's primary new information, begin them promptly after the necessary pre-line beat rather than letting preparatory acting consume the shot; for visible speech, keep the speaker's mouth readable at the line's exact start.
- Direct every significant visible action as `onset → change → readable result`. Do not cut before the audience can understand its result, and do not reserve a whole shot for the result after it has become static unless the resulting state itself changes the relationship or carries the final handle.
- Every reaction has a named trigger and a chronological route: receive the sound/image → gaze or body registers it → visible change. A reaction shot may not be a generic facial pause. Give it the time it needs to alter meaning, then cut when that alteration lands.
- Protect attention around dialogue. Do not put a line that carries new information on top of an unrelated complex manipulation or rapid reframing. Let the crucial action become readable before the line, or let the line land over a simple, controlled action; reserve the post-line shot or tail for the listener's consequence.
- Each camera move needs an arrival condition: reveal a prop, close a relationship distance, transfer focus, expose a reaction, or land on an exit image. Each cut needs a new fact, changed point of view, action handoff, eye-line handoff, sound handoff, or emotional turn. A new focal length or a closer crop alone does not earn a cut.
- Assign shot size by information function: wide for spatial orientation or entrance, medium for action and relationship geometry, close for a detail, line landing, or readable performance. Avoid consecutive scale changes that repeat the same information. When several adjacent shots share the same scale, tempo, and emotional temperature, vary the shot only when the screenplay supplies a new action or perception.
- Design every edit as an action handoff: the outgoing shot supplies the trigger (`notice`, `reach`, `finish line`, `turn`); the incoming shot begins with its physical or perceptual consequence (`bend`, `open`, `listen`, `answer`, `move closer`). Preserve the relevant body, eyeline, prop, and sound state across that handoff.
- Write the delivery cue outside the dialogue container, then place the verbatim line inside `<d>`: `甲以低中音、偏冷偏干的声线和短促命令感说：` followed by `<Subject 1> (S1): <d>[Chinese]请把门打开。</d>`. Keep facial actions and camera directions outside `<d>`. The line itself stays word-for-word; only the delivery prose may change.
- Put post-line reactions in the next silent shot whenever possible. Do not append a long acting instruction immediately after the closing quotation mark.

Immediately after the Chinese block, output an English full-reference companion with exactly these six fields in this order:

```text
subject_definitions:
...

summary:
...

retention_analysis:
...

detailed_description:
...

overall_soundscape:
...

non_diegetic_music:
...
```

- Write all explanatory prose in English. Preserve dialogue, lyrics, and approved model-rendered visible text in their original language.
- Define only the real reference units used by the current clip and keep `<Subject N>`, `<Picture N>`, `<Video N>`, and `<Audio N>` meanings stable across all six sections.
- When `AUDIO_REFERENCE_MAP` is active, every English `<Audio N>` definition names the semantic role and the same locked character/source, without any filename. Its number must equal the operator checklist's actual upload slot; the `summary`, `retention_analysis`, and owning vocal event must preserve the same mode and scope. When inactive, do not invent an audio label merely because a character speaks.
- Use `[Shot 1]` without a timestamp, then `[Shot N] At MM:SS.mmm, ...` for later cuts. These cut times, shot count, shot order, action phases, and exit state must match the Chinese prompt exactly.
- Assign `(S1)`, `(S2)`, and later IDs by first audible-event order inside the unit. Bind every `<d>` event to the real speaking character or explicit off-screen source in the immediately preceding vocal clause.
- Preserve every approved spoken line inside `<d>[Language] ...</d>` without translating or paraphrasing it. The Chinese block keeps its colon-plus-next-line boundary and contains none of these tags.
- Translate the Chinese `音乐：` decision faithfully: `无配乐。` becomes `non_diegetic_music: N/A`; a concrete score cue keeps the same instrumentation/texture, pulse, entry, and exit.
- Preserve the anti-subtitle intent in both blocks. Dialogue exists as character audio; do not generate subtitles, translations, dialogue text, captions, titles, speech bubbles, or unintended readable screen text unless a model-rendered text event is explicitly approved.
- Treat [MINIMAX_H3_DUAL_PROMPT_CONTRACT.md](MINIMAX_H3_DUAL_PROMPT_CONTRACT.md) as the parity authority. An edit to timing, blocking, dialogue, sound, props, or exit state is incomplete until both blocks are synchronized.

Each `H3_UNIT` is one independently generated, self-contained file. Dialogue-led narrative units normally last 10–15 seconds, carry one relationship turn and one action chain, obey the recommended speech budget and 40-effective-character hard ceiling, and end on a stable state that is fully restated at the next unit's opening. Use 5–9.99 seconds only for a documented exception allowed by the long-script reference. Never exceed 15 seconds.

Before prose, compile for every unit:

- owned `SOURCE_BEATS`, `CLIP_TRUTH_LEDGER`, and relevant `PROP_STATE_CHAIN` entries;
- `OPENING_STATE`, `relationship_turn`, `action_chain`, and `exit_state`;
- `DIRECTOR_INTENT` and one `SHOT_SCORE` per internal shot;
- one internal `EMOTIONAL_RHYTHM_MAP` with opening pressure, exact trigger, turn, release-or-withholding, afterimage, source-grounded visual motif, sonic pulse, and a time-specific tempo curve. Each shot must express an audiovisual cause-and-effect link from that map rather than merely restating plot;
- one internal `SCENE_RHYTHM_MAP` for every multi-shot unit and full requested scope: mark each shot's primary event, trigger, cut reason, information function, dialogue/action load, shot-size progression, hold justification, and the local tempo rise/fall. Across any run of three to five shots, flag repeated scale, camera speed, or emotional intensity that does not add new information. This is a directing check, not a user-facing H3 field;
- the current speakers' verbatim `VOICE_BIBLE` entries and exact speech map;
- the recorded `AUDIO_REFERENCE_INTENT` decision and approved `AUDIO_REFERENCE_MAP` rows used by the current unit, or an explicit `declined` decision for the no-reference workflow; `unknown` is unresolved, not inactive approval;
- when the micro-expression trigger applies, one `MICRO_PERFORMANCE_SCORE` bound to an exact shot and time window, containing the outward mask, hidden emotion, trigger, baseline, first leak, suppression, optional reset, after-state, polarity lock, and 1-5 chronological observable action chains;
- a full-scene `SCENE_SHOT_LADDER` and exactly one `CLIP_BOUNDARY_LEDGER` for each adjacent unit pair.

Design both sides of every boundary together. Use exactly one strategy: `exact_match_continuation`, `contrast_cut`, `neutral_bridge`, or `scene_transition`. Reject accidental same-axis near-scale resets, unseen action/prop changes, generic frontal restarts, and text-only continuity claims.

Compile chronological, directly filmable natural language. State motivated framing and crop, camera height/angle, screen geography, focus, action onset/change/result, performance before/during/after speech, cut trigger, synchronized sound, prop opening/exit state, and the final 0.8–1.0-second stable pose. When a `MICRO_PERFORMANCE_SCORE` applies, serialize its visible cues only inside the owning shot, at normal physical speed and in causal order; do not add a new output field. Every cut must add information or change viewpoint. Long voice-over uses composition that makes the mouth unreadable, not only a closed-lips sentence.

Treat the final `镜头设计` as an executable shooting description, never as advice to the prompt writer. Commit to one frame for every shot. Phrases that offer alternatives or describe a future authoring decision—such as “use a wide, rear three-quarter, or object-led view,” “cut on the first decisive action,” “add the next source fact,” “switch scale when the information lands,” or their equivalents—are build failures. Replace them with the chosen shot size, side, height, lens/field of view, screen position, exact action or spoken-word trigger, and visible result. A generic template may help organize metadata, but it may not generate or supply final shot prose.

Bind every vocal event to its real visible or off-screen source before serialization. In the Chinese prompt, name the source in natural Chinese prose and state that character's full locked `VOICE_BIBLE` baseline at its first vocal event in the unit: identity where relevant, register, resonance, timbre, usual volume, articulation, habitual breath/cadence, and the one or two wrong readings to avoid. Keep the exact same baseline string for that character in every independent unit. A real submitted audio reference reinforces that written baseline and is cited through its confirmed `<Audio N>` in both the Chinese vocal event and the English companion; it does not remove the Chinese self-contained textual definition.

Write line-specific pressure, operative phrase, pace, pause, breath timing, and sentence ending immediately before the dialogue line. Keep only the exact approved line on that next line. Do not append bracketed “non-spoken” notes, translations, negative-prompt blocks, or long acting notes immediately after it. Put the reaction or hold into the following silent shot whenever possible. For VO, say `以画外音说` and choose a composition where unintended lip movement is not readable.

After calibration approval, preserve the approved calibration unit byte-for-byte unless the user explicitly revises it. Bulk expansion must author every remaining unit from its own `SHOT_SCORE`; do not replace the approved unit or the remaining units with a shared prose generator.

Output one authoritative prompt pair per unit: the Chinese six-section prompt first and the English six-section companion second. Keep original-language dialogue and visible text verbatim in both. Resolve the user's score policy first: a no-background-music instruction locks “无配乐。” / `non_diegetic_music: N/A` throughout the requested scope. Otherwise use the source or approved directing decision to choose silence or a concrete cue with instrumentation/texture, pulse, entry, and exit. Diegetic music stays inside the matching shot timeline in both serializations, only when supported by the source and not excluded by the user.
