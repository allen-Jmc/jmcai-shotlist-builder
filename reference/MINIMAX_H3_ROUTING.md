# MiniMax H3 Routing for JMCAI Shotlist Builder

Use this file only after the user has selected **MiniMax H3** at the platform gate. The default delivery is a paired prompt for every unit: the Chinese director storyboard defined in `SKILL.md`, followed by the English six-section companion defined in `MINIMAX_H3_DUAL_PROMPT_CONTRACT.md` and `MINIMAX_H3_FULL_REFERENCE_EN.md`. `MINIMAX_H3_BASE_EN.md` remains the timing, keyframe, camera, dialogue, and sound source for both serializations.

## 1. Choose the H3 mode by asset role

Choose by how an asset is used in the target generation, not by file extension or by the mere presence of an uploaded file.

| Actual target-video input | H3 mode | Canonical output |
| --- | --- | --- |
| One image used only as the exact first frame | I2VA | Paired Chinese storyboard + English six-section companion; define the concrete first-frame picture role in English |
| Two images used only as exact first and last frames | FL2VA | Paired Chinese storyboard + English six-section companion; define both frame anchors in English |
| One image used only as the exact last frame | L2VA | Paired Chinese storyboard + English six-section companion; define the landing-frame role in English |
| Any image/video/audio supplies reusable identity, setting, costume, prop, style, pose, action, camera, timing, or voice guidance | Ref2VA | Paired Chinese storyboard + English six-section companion |
| A concrete keyframe plus any additional reusable reference | Ref2VA | Include `keyframe completion` plus the other applicable task types |
| A source video is directly edited | Ref2VA | `video editing`; add `audio reuse` only if its signal remains audible |
| New content continues a source video | Ref2VA | `video continuation`; add the true audio relationship if any |
| A video supplies only motion, cuts, rhythm, or temporal structure | Ref2VA | `reference generation`, not editing or continuation |
| An audio signal is copied in full or in part | Ref2VA | `audio reuse` |
| Only timbre, vocal performance, scripted diegetic rhythm, dialogue content, or sound texture is followed | Ref2VA | `audio reference` |

Internal concept art or blocking diagrams that are not actually submitted to H3 do not create H3 reference inputs.

Text-only generation is outside this skill. If the user will not submit at least one valid reference input to H3, stop at the asset gate and request one rather than selecting a fallback mode.

If an image or video role is ambiguous, ask whether it is a concrete frame anchor, a reusable reference, an edit source, or a continuation source. Never infer this silently.

## 2. Read the right canonical guides

- Before all mode-specific work, read `MINIMAX_H3_LONG_SCRIPT_UNITS.md` and `MINIMAX_H3_SCENE_GROUNDING_AND_RUNTIME.md`; establish the complete requested-scope unit blueprint, document-authority map, project runtime contract, voice bible, post nodes, and per-unit truth-ledger requirement.
- Before packing more than one independent H3 clip, read `MINIMAX_H3_CROSS_CLIP_EDIT_CONTINUITY.md` and build the full-scene shot ladder plus pairwise boundary ledgers.
- For every H3 mode, read `MINIMAX_H3_BASE_EN.md`, `MINIMAX_H3_DUAL_PROMPT_CONTRACT.md`, and `MINIMAX_H3_FULL_REFERENCE_EN.md` completely. The English companion always uses the six-section container while truthfully stating the actual I2VA, FL2VA, L2VA, or Ref2VA reference relationship.
- Every H3 clip with a human vocal event: read both `MINIMAX_H3_EMOTION_PERFORMANCE.md` and `MINIMAX_H3_ACTOR_DIALOGUE_CRAFT.md` completely.
- Always resolve `AUDIO_REFERENCE_INTENT` using `MINIMAX_H3_AUDIO_REFERENCE_BINDING.md`: ask once if unknown; only explicit refusal skips binding. If requested, confirm the operator-side filename → clip-local upload slot → character `AUDIO_REFERENCE_MAP`. Pending intent/files/bindings prevent final sound-bearing prompt delivery, not independent visual planning. Never invent audio-routing syntax for unbound inputs.

Do not translate, rename, reorder, merge, or embellish either schema. The five Chinese director-storyboard sections remain isolated in their block; the six English fields remain isolated in the companion block.

For creative decisions inside those fields, apply this priority order: explicit user direction and submitted style/content references → screenplay facts and approved blocking → `MINIMAX_H3_DIRECTORIAL_NATURAL_LANGUAGE.md` → this routing/timing layer → general camera or house-style libraries. Canonical guides control protocol syntax; they do not override the user's content, the script's reality, or a motivated director decision.

## 3. Build director-led H3 clip groups

First read `MINIMAX_H3_SOURCE_COVERAGE.md`. Receive the ordered `SOURCE_BEATS`, recurring `PROP_STATE_CHAIN` records, `VOICE_BIBLE`, `POST_NODES`, and platform-neutral `SHOT_BEATS` manifest produced before either renderer: approved shot rows, order, scene boundaries, actions, transcript placement, emotional progression, and cinematography. Confirm that every atomic source beat has one owning shot beat before packing. Preserve that directing core, then build the complete MiniMax-specific `H3_UNIT_BLUEPRINT` using `MINIMAX_H3_LONG_SCRIPT_UNITS.md` and `PROMPT_DENSITY.md`.

H3 packing is allowed to differ from Seedance because a fixed envelope can force intact speech, visible action, or performance into an unnatural pace. Prefer the fewest independently generated `H3_UNIT` objects that each preserve one scene/time/reality layer, one micro relationship change, one main action chain, full source-beat coverage, intact performance, readable shot grammar, reference continuity, and valid timing. Dialogue-led narrative units normally last 10–15 seconds and obey the 40-effective-character hard ceiling; shorter units require a documented exception. A lens change, insert, cutaway, camera reposition, or dialogue line ending may remain an internal shot when it belongs to the same unit, but the underlying environment establish, character action, visible-text/post-node decision, or prop-state transition must remain explicit. Split, merge, or resize units only when timing capacity, scene/reality layer, reference mode, action objective, relationship turn, performance arc, continuity, or platform limits genuinely require a new generation. Never delete, reorder, rewrite, summarize away, or reinterpret a source beat. When the user later switches platforms, reuse `SOURCE_BEATS`, `PROP_STATE_CHAIN`, `VOICE_BIBLE`, and `SHOT_BEATS` and repack for that platform; do not reuse another platform's boundaries as creative authority.

Before writing any prompt in a multi-clip scene, lay all internal shots onto one `SCENE_SHOT_LADDER`. Then design both sides of every adjacent boundary together in a `CLIP_BOUNDARY_LEDGER`; choose exactly one of `exact_match_continuation`, `contrast_cut`, `neutral_bridge`, or `scene_transition`. A new H3 clip is not permission to reset to a frontal medium shot, repeat the same push-in, change an unseen prop state, or start after an unshown action. If two boundary frames share the same subject and axis at a near scale but are not an exact action/frame match, redesign the incoming composition or use a neutral bridge before prompt serialization.

Translate the internal cuts inside each `H3_UNIT` into `【镜头1｜0.0—N秒】`, `【镜头2｜N—M秒】`, and later continuous timed shots. A unit with multiple internal shots remains one workflow execution. A unit with one continuous shot remains one shot.

- Derive the clip's effective duration from the combined speech timeline and `visual_action_minimum`: environment establish, action onset, state change, visible result, performance reaction, and transition. Allow overlap only when both speech and action remain clearly readable. Do not treat 15.00 seconds as a creative target.
- Keep the shotlist's default 21:9 aspect ratio as generation metadata in the HTML prompt header unless the user requests another ratio. Do not append duration or aspect-ratio prose to the canonical H3 prompt body.
- If H3 accepts the required exact duration, use it. If only discrete durations are available, select the nearest longer supported duration and fill the surplus with a motivated visual hold, reaction, environmental beat, or transition.
- Record requested, platform-supported, and observed rendered durations separately. Reserve a stable 0.5-second head handle and 0.8–1.0-second tail handle where possible; extra platform frames count only when their content is stable.
- Prefer keeping a complete sentence or emotionally indivisible line inside one clip. If a long passage must span clips, split only at existing sentence, clause, or breath boundaries and preserve every character and punctuation mark in order.
- Design an explicit continuity handoff between independently generated clips: lock the outgoing and incoming pose or gait phase, eyeline, screen direction, camera side, lens and distance, significant-prop holder/location/state from the approved `PROP_STATE_CHAIN`, costume wetness/damage, practical-light state, weather, and ambience. Use continuous diegetic ambience or a motivated hard cut to hide the generation boundary.
- Start `镜头1` at 0.0 seconds. Use consecutive Chinese shot headers with start/end ranges; the ranges must be continuous and end exactly at the unit duration.
- For I2VA, FL2VA, and L2VA, replace every placeholder `N` and `S.SS` with the real final-shot index and exact two-decimal duration.
- FL2VA normally uses a single continuous shot. Add cuts only when the user explicitly requires them and the last shot still lands exactly on the final frame.
- Use the long-script density references: 10 seconds usually 2–3 shots, 12 seconds 3–4, and 15 seconds 3–5. These are not quotas. Preserve a motivated continuous take when cutting would weaken the unit, and permit a necessary 0.5–2.5-second establishment, insert, reaction detail, or match image inside a multi-shot unit when it adds essential information. Record the dramatic reason.

Reference and speaker numbering is local to one target clip. Renumber from 1 in each copyable prompt, while mapping the same source asset and person consistently whenever they recur in later clips. Never rely on a previous prompt block to define a label used in the current one.

Before writing the canonical fields, copy the unit's full `OPENING_STATE`, `relationship_turn`, `action_chain`, `exit_state`, and applicable `VOICE_BIBLE` entries into the production manifest. Then read `MINIMAX_H3_DIRECTORIAL_NATURAL_LANGUAGE.md` and create two internal layers:

1. `DIRECTOR_INTENT` for the full clip: dramatic question, point-of-view ownership, emotional movement, visual reveal, and stable final image.
2. `SHOT_SCORE` for each internal shot: narrative purpose, time window, framing and crop, camera height and angle, screen geography, focal plane, motivated motion or stillness, action onset/change/result, performance turn, editorial trigger, and landing state.

Do not expose these names as another top-level H3 field. Translate their decisions into chronological prose inside `镜头设计：`.

## 4. Preserve the shotlist's direction without polluting H3 syntax

Compile each prompt from the complete approved `SOURCE_BEATS`, `PROP_STATE_CHAIN`, `POST_NODES`, and `SHOT_BEAT`, not merely its visible-action cell or a shortened scene summary. Environment-only establishes, entrances/exits, visible-text reveal timing and either exact model-rendered text or the approved clean-plate/post-node plan, significant wardrobe/body reveals, recurring-prop opening states and state-changing actions, lens/shot-size, crop, camera height and angle, left/right and depth positions, focus, camera behavior, performance beats, dialogue, listener reaction, synchronized sound, and landing frame must all survive into the authoritative natural-language description. If a source field disappears during serialization, the prompt fails even if the HTML table still displays it or the asset appears in `subject_definitions`.

Translate the approved cinematography into the single authoritative Chinese `镜头设计：` section:

- State composition, focal length, subject position, practical lighting, action, state change, and background activity where visible.
- State the shot size and crop together, plus camera height/angle, screen-left/right placement, foreground/middle/background layers, and the intended first visual focus.
- For a two-person shot or reverse angle, identify which face is sharp, which figure remains recognizably soft, the eyeline, distance, occlusion, and preserved 180-degree axis.
- Express camera motion as a natural sentence with motion type plus meaningful amplitude and speed.
- Explain the visible or emotional reason for the motion. When no motivated change exists, use a stable camera; never add motion merely to signal “cinematic.”
- Translate numbered performance beats into an observable chronological progression of eyes, jaw, breath, hands, weight, and reaction.
- Let gaze precede head motion and isolate delicate facial changes into separate time windows. End on a readable stable pose for 0.8–1.0 seconds when possible.
- Encode approved distances, facing directions, eyelines, and occlusion in prose.
- Give every cut an editorial trigger—action, gaze, operative phrase, listener reaction, information reveal, matched composition, or sound bridge—and state the incoming composition that the cut reveals.
- Give each shot one primary attention target: a person, prop, or relationship. A two-shot or over-the-shoulder composition is valid when distance, power balance, or listener reaction is the subject; do not force relationship coverage into alternating isolated close-ups.
- Do not insert Seedance-only `@imageN` handles, `⚠️` warning blocks, or the `15秒。21:9。` suffix into an H3 prompt. Chinese `【镜头N｜起始—结束秒】` headers are required.
- If production warnings are useful, place them in the HTML outside the copyable H3 prompt.

## 5. Dialogue and voice consistency

For the default Chinese director storyboard, do not use speaker IDs or visual H3 tags. The only conditional H3 reference token allowed is an approved `<Audio N>` from `AUDIO_REFERENCE_MAP`, embedded exactly as specified in `MINIMAX_H3_AUDIO_REFERENCE_BINDING.md`: once in a compact binding line under `角色与场景：` and again at the owning vocal event. Bind each vocal event to the real visible or explicit off-screen source in prose. State the locked voice baseline, visible action, emotional delivery, pace, pause, breath, and ending before a colon; put the exact approved spoken line alone on the following line. This line break is the only speech boundary.
- Treat all scripted speech as locked source text: dialogue, voice-over, lyrics, announcements, and spoken on-screen text must remain word-for-word, punctuation-for-punctuation, in their original language and original order. Do not abridge, paraphrase, euphemize, combine, or rewrite it to hit a clip duration. A textual change is allowed only after explicit user approval.
- For Chinese speech, count audible Han characters and schedule each vocal event at 4.0–4.5 characters per second unless the user explicitly supplies another rate; use 4.25 as the default directing rate. Punctuation does not count as a spoken character, but commas, ellipses, sentence endings, hesitation, breath, and emotional recovery require additional time outside the character-rate calculation. This is internal timing math, not a performance command to paste into the copyable H3 prompt.
- Compute `minimum_speech_time = audible_Han_character_count / selected_rate`. Then add the pre-line acting beat, punctuation pauses, post-line hold, listener reaction, and any camera transition to derive the unit duration. If the result does not fit the current envelope, lengthen the unit or create another `H3_UNIT` at a natural boundary. Never solve an overfull timeline by changing the words or accelerating above 4.5 characters per second. In the H3 prompt, state the real start/end window and meaningful pauses, then direct natural phrasing rather than saying “X characters per second.”
- For voice-over, write `以画外音说：` before the dialogue and choose framing where the visible character's mouth is unreadable or fully closed.
- Treat that lip-closure phrase as necessary but insufficient. During a long voice-over, avoid a centered frontal shot with the corresponding visible character's readable mouth; use rear/over-shoulder/profile-occluded coverage, hands/props, the eyeline target, or environment coverage so composition reduces auto-lip-sync risk.
- For a line that continues across a cut, place the visual cut at a natural breath boundary and state uninterrupted audio continuity in ordinary Chinese. Do not use `<scenetrans>` or `<cutoff>`.

For every human vocal event, apply `MINIMAX_H3_EMOTION_PERFORMANCE.md` and `MINIMAX_H3_ACTOR_DIALOGUE_CRAFT.md` before serialization:

- Infer emotion from the dramatic objective and subtext, not from isolated words.
- Define the speaker's surface action, hidden need, obstacle, energy direction, and exact turn.
- Specify audible pitch/register, volume, timbre/resonance, articulation, breath, stress, pause behavior, and ending contour as applicable.
- Give the line a pre-line thought/breath beat, chronological during-line progression tied to exact phrases, and a post-line residue or intentional interruption.
- For voice-over, keep visible lips completely closed while directing emotion through the voice, gaze, breathing, body rhythm, and environment interaction.
- Avoid generic delivery labels and excessive gestures. One clear major gesture per short line is normally enough unless the script requires more.
- Place the dominant delivery cue immediately before the dialogue line: name what the line must not sound like when needed, then give the single strongest phrase-level turn. Do not let a character-rate instruction, an abstract subtext explanation, or a long technical list displace that cue.
- Convert the internal scene analysis into a playable objective and action rather than pasting psychology into the prompt. Shape short lines as no more than two strong thought units unless the text itself requires more; shape long narration around one overall task and three to five emotional waypoints.
- If a neutral or stereotyped take remains plausible, exclude the likely wrong reading and pair it with the correct playable alternative. Preserve one baseline voice, one audible change at the turn, and a post-line residue.

For Ref2VA voice or audio references:

- Before assigning labels, confirm one operator row per asset with the exact filename, real clip-local upload position, one locked target character/source, vocal role, `audio reuse` or `audio reference`, compatible retention marker, scope, and excluded layers. Never infer the character mapping from filename similarity, gender, or character order; `<Audio N>` itself follows the confirmed upload position.
- Default to one filename ↔ one target character. Mixed/shared exceptions require explicit user approval and unambiguous speaker/time ranges.
- Define `<Audio N>` only for an explicit standalone audio asset or an enabled audio track that is actually copied or referenced. A reference video does not automatically create an audio label.
- Keep the exact confirmed filename outside both prompt blocks. In the English companion, bind the real upload slot to the target speaker ID without a filename, for example: `<Audio 1> is the voice-timbre and speaking-delivery reference for <Subject 1> (S1).` Keep the Chinese storyboard free of H3 reference tags.
- Repeat that mapping naturally at the speaker's actual vocal event in both the Chinese `镜头设计：` and English `detailed_description`.
- Do not put `(Sx)` in `retention_analysis`.
- If only timbre, rhythm, emotion, or delivery is referenced, do not import the source audio's words.
- If dialogue from reference audio is reused or explicitly reperformed, preserve its words and language; write `[unclear]` rather than guessing unintelligible spans, and normalize only decorative punctuation.
- A verbal cue contained only inside a directly reused soundtrack uses `<Audio N>` as its source and does not create a fictional speaker ID.

## 6. Sound-layer separation

- Keep dialogue, singing, diegetic music, and shot-synchronized sound events in their owning timed shot. Summarize current ambience, physical actions, and non-verbal human sounds in one scene-specific `声音：` section after the final shot. Do not repeat dialogue there or reuse a generic sound list.
- When no audience-only score is intended, write exactly `音乐：` followed by `无配乐。` Do not invent score. When score is approved, `音乐：` names its concrete texture, pulse, entry, and exit.
- Radio, television, phone playback, and live instruments heard by characters are diegetic and belong in the relevant shot, not in `音乐：`.

## 7. Preflight validation

Before placing an H3 prompt in the HTML, verify all applicable checks:

### Long-script unit audit

- The complete requested-scope `H3_UNIT_BLUEPRINT` exists before prompt expansion.
- Every unit has one scene/time/reality layer, one `relationship_turn`, one `action_chain`, a complete `OPENING_STATE`, and a stable `exit_state`.
- Dialogue-led narrative units use 10–15 seconds; a 5–9.99-second unit has a permitted `duration_exception_reason`; no unit exceeds 15 seconds.
- Chinese effective speech stays within the 10/12/15-second recommendations where possible and never exceeds 40 characters.
- The project `VOICE_BIBLE` is stable across units; scene-specific delivery changes do not rewrite its baseline.
- Titles, timestamps, chats, forums, and complex UI are explicit `POST_NODES` by default, with exact wording, timing, placement, clean plate, and reaction evidence.
- A same-scene next unit fully restates the prior unit's visible exit state instead of relying on “same as before.”
- The final HTML contains one machine-readable `article.h3-unit` record per English/Chinese prompt pair and passes `scripts/h3_unit_lint.py`.

### Chinese director storyboard (default)

- The title and sections appear exactly once and in this order: `中文审稿版｜H3-XXX｜N秒`, `角色与场景：`, `镜头设计：`, `声音：`, `音乐：`.
- I2VA, FL2VA, or L2VA keyframe alignment is described by the opening/landing states inside the relevant shot; do not emit a separate Base-Mode preamble.
- Shot numbers are consecutive, ranges are continuous, and the last range ends at the declared clip duration.
- Dialogue has no `<d>` tags: its delivery ends in a colon and the verbatim line occupies the next line alone.
- If `AUDIO_REFERENCE_MAP` is active, show the exact filename, upload slot, and locked character in an operator checklist outside both copyable prompts. `角色与场景：` contains one filename-free compact binding line per active `<Audio N>`, with target source, `Audio mode`, `Retention`, scope, and exclusions; it contains no `<Subject N>`, `<Picture N>`, `<Video N>`, or `(Sx)`. Each label recurs at its owning Chinese vocal event. If the map is inactive, neither prompt contains audio-routing fields.

### Ref2VA

- The six sections appear exactly once and in canonical order.
- Every reference label is defined before use and keeps one meaning throughout the prompt.
- `summary` introduces no new labels and begins with valid, non-duplicated task types.
- Every defined label receives exactly one `retention_analysis` line using a marker valid for its label type.
- `retention_analysis` contains no speaker IDs.
- The six-section protocol is not a word-count target. Use the shortest complete description that remains storyboardable, playable, temporally clear, and reference-safe. Treat 350-500 English words as a normal detail band for a genuinely complex multi-shot Ref2VA generation, never as a minimum or quota; simple clips may be shorter and dense dialogue or action may be longer. Keep `subject_definitions`, `summary`, and `retention_analysis` compact and non-duplicative, reserve useful detail for chronological directing, and never repeat identity, costume, setting, or style to inflate length.
- One or two English style sentences appear before `[Shot 1]`.

### Platform isolation

- The copyable block contains no Seedance handles, Chinese prompt scaffolding, or Seedance duration suffix.
- The authoritative submission block uses English H3 rewrite prose; only dialogue, lyrics, and visible scene text retain their original language. The separately labeled Chinese editing mirror is allowed and required, but it is never mixed into the English block.
- The first shot is exactly `[Shot 1]` without a timestamp. Later shots alone use `[Shot N] At MM:SS.mmm,`.
- Outside original-language `<d>` payloads and exact quoted visible text, the English block contains no CJK, Chinese plan labels, bilingual fragments, `【镜头N】`, or table delimiters such as `|`.
- `overall_soundscape` and `non_diegetic_music` contain no `<d>` blocks.
- The H3 output preserves every approved `SOURCE_BEAT`, `SHOT_BEAT`, recurring-prop state transition, scene boundary, spoken line, and internal shot order. Its prompt count, clip boundaries, and effective durations may differ from Seedance when source fidelity or director-led timing requires it.

### Source coverage and stateful-prop audit

- The full screenplay scene text and current user corrections outrank synopsis, old shotlists, keyframe lists, and previous prompt sections.
- Every `source_beat_id` maps to exactly one owning `SHOT_BEAT`, one H3 clip, and explicit prompt evidence in both languages.
- Environment-only establishing frames remain distinct from later character entrances when the screenplay orders them separately.
- Exact visible values and text—times, messages, notes, signs, screens—either appear verbatim at the correct reveal or are preserved as an explicit `POST_NODE` with exact wording, timing, placement, clean plate, and reaction evidence.
- Each recurring significant prop has a closed `PROP_STATE_CHAIN`: holder, location, opening state, state-changing action, and exit state connect across every appearance and clip boundary.
- A prop reference label or HTML scene-text cell does not count as action coverage; `detailed_description` must state the prop's current state and any manipulation at the moment it occurs.
- Compression preserves action onset, change, and readable result. If all owned source beats do not fit alongside intact speech and performance, split the clip instead of summarizing actions.
- Every concrete prompt noun, event, setting condition, light and sound traces to the current `CLIP_TRUTH_LEDGER`; no hospital, street, rain, monitor, paper, prop, ambience, or style content is imported merely because it exists elsewhere in the project.
- Every `retention_analysis` line identifies the exact asset and concrete traits or relationships to retain; generic placeholder prose fails.

### Directorial natural-language audit

- Every shot specifies framing plus crop, camera height/angle, screen geography, focus/depth relationship, a motivated camera behavior or explicit stillness, one readable action progression, and a stable landing state.
- Every cut changes information or emotional point of view and names its action, gaze, line, sound, reveal, or matching-visual trigger.
- Two-person coverage preserves left/right positions, eyelines, distance, foreground occlusion, focus priority, and the 180-degree axis.
- Micro-expression changes are chronological and isolated; gaze moves before the head, and the final readable pose is held for 0.8–1.0 seconds where possible.
- The prose is directly storyboardable. Replacing the character names must not leave a generic prompt that could fit any unrelated scene.
- Every prompt passes three craft tests: a storyboard artist can draw the opening, motion, focus, and landing frame; an actor can identify the pre-line thought, playable action, phrase-level turn, and after-state; an editor can identify why each cut occurs, what the incoming shot adds, and how picture or sound bridges the boundary.
- Style-only references control photography and grading only. Extraction-only composition/action sources are absent from final labels and uploads, with only their abstract geometry translated into prose.

### Transcript and duration audit

- Compare every H3 `<d>` payload against the source script before delivery. Except for the required `[Language]` tag and HTML escaping, the spoken text and punctuation match exactly; no source line is missing, shortened, paraphrased, reordered, or duplicated.
- For each Chinese vocal event, record the audible Han-character count, selected rate, calculated speech time, scheduled start, and scheduled end. Confirm the effective rate remains within 4.0–4.5 characters per second.
- Confirm punctuation pauses, pre-line micro-beats, post-line holds, and listener reactions have real timeline space rather than being squeezed into the speech-rate allowance.
- Record `visual_action_minimum` for environment establishes, visible information reveals, character actions, and prop-state transitions. Confirm the combined timeline leaves each onset, change, and result readable rather than assuming all visuals fit inside speech time.
- Confirm the clip duration is derived from the finished beat timing. If it is longer or shorter than 15.00 seconds, that is valid and should be visible in the HTML metadata.
- For every H3 split, verify an explicit outgoing/incoming continuity handoff and make each prompt self-contained by redefining all recurring references and speakers.
- For every adjacent pair, verify one complete `CLIP_BOUNDARY_LEDGER`, a unique boundary strategy, a cut trigger, outgoing/incoming frame geometry, edit handles, and English/Chinese prompt evidence. Reject accidental same-axis near-scale resets and any incoming state reached through an unshown action.
- Distinguish requested, supported, and observed durations. If generated clips are supplied, inspect actual internal cuts plus the previous tail and next head before declaring the boundary edit-safe.

### Emotion and anti-recital audit

- Every vocal event has a script-derived surface action, hidden need, obstacle, energy direction, and emotional turn.
- Every vocal event has an audible voice profile, a pre-line beat, phrase-level progression, and post-line residue or intentional interruption.
- Emotion is expressed through synchronized voice, breath, gaze, facial muscles, hands, posture, listener reaction, and camera behavior as relevant; a generic emotion adjective never carries the direction alone.
- Dialogue remains intelligible and lip-synchronized. Voice-over uses the exact off-screen phrase and keeps visible lips completely closed.
- Sound design supports performance without masking breath, articulation, or line endings.

### Actor and dialogue-craft audit

- The performer has an immediate objective, a playable action, a hidden contradiction, and an after-state; the prompt does not stop at abstract psychology.
- Entry, turn, and ending behavior attach to exact original phrases or punctuation, with one operative phrase carrying the main change.
- Any excluded wrong reading is paired with the correct acting alternative.
- Vocal parameters are selective and coherent: a baseline, a turn, and an ending contour rather than an adjective inventory.
- Body, breath, gaze, gesture, listener reaction, and camera all protect the same inner event.
- The dominant acting cue sits immediately beside `<d>`; numerical character rate and internal timing math never appear in the copyable prompt.
- A competent actor following the instruction could not reasonably default to a flat recital without violating the prompt.

### Music-layer audit

- Confirm every English companion contains `non_diegetic_music` exactly once and every Chinese block contains `音乐：` exactly once.
- When the Chinese block says `无配乐。`, require the English value `N/A`. When the Chinese block specifies a score, require the same instrumentation/texture, pulse, entry, and exit in English.
- Keep script-required radio, television, phone, live-instrument, or other music heard by the characters as diegetic action in the timed shot description only.

### Chinese/English pair parity audit

- Each H3 unit contains two separately labeled and independently copyable blocks in this order: `中文审稿版` first, `English six-section prompt` second.
- The Chinese block remains natural Chinese director prose with no H3 visual/dialogue tags; only confirmed `<Audio N>` tokens and their compact mixed-language routing block are conditionally allowed. The English block keeps the canonical six field names and H3 reference/dialogue tokens.
- Both blocks encode the same unit truth: reference roles, audio mode/retention scope when active, shot count/order, cut times, speaker identities, exact original-language dialogue payloads, emotional turns, action/prop states, sound events, music decision, and exit state. The operator checklist separately locks each audio filename to the English `<Audio N>` upload slot and target character.
- Any edit to one block is synchronized into the other before delivery. Resolve discrepancies by returning to the approved `CLIP_TRUTH_LEDGER` and `SHOT_SCORE`, not by silently treating either serialization as expendable.
