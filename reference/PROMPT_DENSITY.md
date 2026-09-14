# Prompt Density

How to preserve one platform-neutral directing plan while packing it into platform-appropriate generation clips. Build `SHOT_BEATS` once; Seedance uses 15-second envelopes, while MiniMax H3 uses director-led dynamic durations and may require different clip boundaries.

## The rule, derived from the source shotlist

Across the canonical shotlist (scenes 13–29 + 61–66), the average is **~1 prompt per 4–5 shot rows**, but this varies wildly by scene:
- Scene 21: 7 rows / 5 prompts (1:1.4) — dense, prompt-per-beat
- Scene 23: 3 rows / 1 prompt (3:1) — collapsed into one continuous emotional unit
- Scene 28: 42 rows / ~9 prompts (4.7:1) — typical action coverage

**There is no fixed ratio. Decide per scene.**

## Shared directing heuristic

Group shot rows into one prompt when ALL of these are true:
1. They share the same **character set** in frame
2. They share the same **location/subset of location**
3. They form a **continuous emotional/temporal unit** (no time skip, no major mood pivot)
4. They fit the selected platform's practical duration and prompt limits without rushing speech, action, or reaction
5. The combined prompt remains operationally clear

Split into separate prompts when one of these materially changes the generation contract:
1. **Hard cut between locations, times, or reality layers** (apartment → flashback)
2. **Major character entrance/exit** changes the independently controlled references or scene objective
3. **Performance or action objective** changes enough to require a new complete envelope
4. **Timing or platform capacity** cannot preserve intact speech, reaction, and readable action in one generation
5. **Reference mode or continuity handoff** genuinely requires a separate generation

A new physical action, camera move, angle, lens, shot size, insert, or cutaway does not automatically create a new prompt. When it belongs to the same dramatic unit, keep it as an internal shot and give its cut a clear information or emotion function.

Prompt grouping never changes source coverage. Before packing, map every atomic screenplay `SOURCE_BEAT`—including environment-only establishes, visible actions, exact visible text, and significant-prop state changes—to one owning `SHOT_BEAT`. A physical action may stay inside an existing dramatic beat, but it may not disappear merely because it does not justify a new prompt. Use [MINIMAX_H3_SOURCE_COVERAGE.md](MINIMAX_H3_SOURCE_COVERAGE.md) for H3 source authority, the coverage ledger, and recurring-prop state chains.

## Seedance 2.0 packing

A single 15-second Seedance prompt CAN contain internal `【镜头1】 / 【镜头2】 / 【镜头3】` cuts when the cuts share location and characters. This is the "multi-shot prompt" pattern. See [PROMPT_PATTERNS.md](PROMPT_PATTERNS.md) §3 for the syntax.

Use multi-shot when:
- 2–3 fast cuts inside one continuous emotional moment (e.g., wide establish → tight reaction → low-angle finish, all in 15s)
- A montage that's tonally one unit (the polaroid scan in scene 21 — slide across photos, land on NOV 14, hand reaches in — one prompt, three internal beats)

Use one-shot when:
- A single continuous performance moment with one camera move (the dolly across the bridge in scene 18)
- Anything where the emotional weight needs to land without cuts

## MiniMax H3 packing — full-script units first

Read [MINIMAX_H3_LONG_SCRIPT_UNITS.md](MINIMAX_H3_LONG_SCRIPT_UNITS.md), [MINIMAX_H3_SCENE_GROUNDING_AND_RUNTIME.md](MINIMAX_H3_SCENE_GROUNDING_AND_RUNTIME.md), and [MINIMAX_H3_TIMING_ENGINEERING.md](MINIMAX_H3_TIMING_ENGINEERING.md) before applying this section. Build the complete requested-scope `H3_UNIT_BLUEPRINT` before any final prompt. This section explains how the shared shot-beat manifest is packed into those independently generated units.

Do not mechanically fill a 15-second template. Direct the beat first, calculate how long the intact scripted speech, performance, visible actions, information reveals, and prop-state transitions need, then choose 10, 12, or 15 seconds for dialogue-led narrative units. Use a documented 5–9.99-second exception only where the long-script-unit guide permits it.

For each Chinese vocal event:

1. Preserve the original words, punctuation, language, and order.
2. Count audible Han characters; punctuation is excluded from the character count.
3. Use 4.0–4.5 characters per second for ordinary dialogue unless the user sets another rate; default to 4.25. Use 2.5–3.0 characters per second for slow emotional voice-over, suppressed monologue, or memory narration; default to 3.0.
4. Compute `speech_time = character_count / rate`.
5. Add 0.3–0.5 seconds to establish the shot and 0.3–0.8 seconds for the post-line hold, listener reaction, action residue, camera transition, and environmental afterglow.

Keep this calculation in the shotlist timing notes. In the copyable H3 prompt, use the resulting start/end window and natural punctuation holds; never instruct a performer to speak at a numeric characters-per-second rate.

For H3, prefer the fewest `H3_UNIT` objects that preserve single-scene integrity, one micro relationship change, one main action chain, intact performance, readable shot grammar, reference continuity, and valid timing. More prompts are not inherently safer. If one 10–15-second unit is too dense, split at an existing sentence, clause, breath, action handoff, relationship turn, information landing, or scene boundary. Chinese dialogue also follows the 10/12/15-second suggested budgets and the 40-effective-character hard ceiling in the long-script guide. Treat 10-second 2–3 shots, 12-second 3–4 shots, and 15-second 3–5 shots as density references, while preserving a motivated continuous take or a necessary 0.5–2.5-second insert when the director intent requires it. Do not shorten a locked line, accelerate it unnaturally, or create a new unit merely because a dialogue line ends.

Calculate a `visual_action_minimum` alongside speech time. Sequence every owned source beat with enough time to read its onset, change, and result; allow overlap with dialogue only when both remain legible. The final clip duration must satisfy the complete combined timeline, not only the spoken line. Compression may shorten redundant holds or simplify unmotivated camera motion, but it may not merge an empty establishing image into a later entrance, replace several actions with a vague summary, omit a prop interaction, skip a before-to-after state transition, or leave a source fact only in the HTML scene-text column. If full coverage is unclear at the proposed duration, split the clip.

After clip packing, sum every scene and every clip against `DECLARED_RUNTIME`. If the source-faithful minimum or packed total exceeds the declared film duration by more than 5%, stop and obtain an explicit user choice; never silently add clips, lengthen the film, accelerate performance outside the approved range, or rewrite the transcript.

Every split requires a continuity bridge. Specify the same outgoing/incoming pose or gait phase, screen direction, camera side, focal length and distance, eyeline, significant-prop holder/location/state, costume wetness/damage, weather, practical-light state, and diegetic ambience. Validate the relevant `PROP_STATE_CHAIN` before and after the boundary; a reference label does not make a separate generation inherit whether a prop is open, closed, carried, parked, dropped, damaged, empty, or full. Fully restate the previous exit state as the next unit's opening state instead of writing “same as before.” Each unit contains only one location/time/reality layer and one relationship/action unit. MiniMax H3 uses no non-diegetic music bed. Restart H3 reference and speaker numbering in each unit, and redefine only recurring assets that are actually visible and necessary, within the current Ref2VA modality limits in `MINIMAX_H3_PLATFORM_LIMITS.md`.

## Examples from the source

**Scene 23, 3 rows → 1 prompt (collapsed)**
- Row 11.1: Roko in apartment, dark atmosphere
- Row 11.2: Tear falls
- Row 11.3: Closes eyes, breaks into sobs

All three are one continuous emotional collapse on the kitchen floor. In the Seedance branch this may use `【镜头1】【镜头2】`; in H3 it becomes either one motivated continuous take or natural-language `[Shot N]` entries in one dynamic-duration group. **Don't fragment grief.**

**Scene 21, 7 rows → 5 prompts (split)**
- Prompt 1: door open + boots crossing threshold (rows 9.1 partial)
- Prompt 2: hallway walk to living room (own envelope — needs its own breath)
- Prompt 3: living room scan + window + turn toward fridge (one-er, 50mm)
- Prompt 4: fridge ECU — polaroid slide + hand reaches in
- Prompt 5: photo close-up + Roko's face + turn

These may earn separate prompts only when the distinct performance envelopes or generation-continuity requirements demand them. Camera setup and focal length alone do not decide the boundary.

## When in doubt

For Seedance, err toward clear 15-second envelopes rather than overpacking. For MiniMax H3, use the **fewest independently generated clips that remain complete and reliable**; do not treat prompt count as a quality metric. “Fewest” is subordinate to coverage: both branches must preserve the approved `SOURCE_BEATS`, `SHOT_BEATS`, scene order, visible action and prop-state chains, transcript, and cinematic intent.

## Tagging

Each prompt gets a short bracketed tag for the HTML header — describes what the prompt shows at a glance. Examples:
- `[MS-CU · door open + boots]`
- `[ECU · fridge photo slide + take photo]`
- `[CU · Roko face + turn]`
- `[Wide → MCU · spatial establish + reaction]`
- `[Multi-shot · 3 reactions + dialogue]`

Use the team's existing shot-plan abbreviations (see [PLAN_TYPES.md](PLAN_TYPES.md)).
