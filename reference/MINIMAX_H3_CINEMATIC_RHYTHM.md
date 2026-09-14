# MiniMax H3 Cinematic Rhythm, Emotion, and Image Presence

This reference prevents technically complete H3 prompts from becoming flat coverage notes. Use it for every H3 unit alongside the canonical H3 format guides. It governs *how the moment lands*; it never changes source truth, dialogue, reference routing, duration, or continuity requirements.

## 1. The unit must have a felt temporal shape

Before writing any final prompt, compile this internal `EMOTIONAL_RHYTHM_MAP` for each H3 unit:

```text
opening_pressure: the visible baseline and what is already under tension
trigger: the exact look, action, sound, object change, or source phrase that disturbs it
turn: the single point at which the relationship, knowledge, or self-control changes
release_or_withholding: whether the unit expands, arrests, breaks, or deliberately refuses release
afterimage: the stable final visual residue the audience is left with
visual_motif: one source-grounded image or material event that carries the pressure
sonic_pulse: the scene-specific physical sound, silence, breath, or score change that marks time
tempo_curve: hold / gather / accelerate / arrest / release, with actual shot or action windows
```

This is planning material, not a seventh H3 output field. A unit without a trigger, turn, and afterimage is coverage, not a dramatic beat: revise the unit boundary or shot score before writing prose.

Do not assign a named emotion to every second. Give the audience a readable baseline, one disturbance, and a changed residue. “Sad,” “tense,” “cinematic,” “beautiful,” “natural performance,” and “slow push” are not substitutes for this map.

## 2. Write an audiovisual cause-and-effect chain

Every internal shot must contribute at least one link in this sequence:

```text
what is seen or heard → what changes in attention/body/space → what the camera or sound reveals → what remains
```

For dialogue, the line must be an action on someone, not an isolated transcript. Bind one pre-line impulse, one operative phrase or punctuation turn, and one post-line residue to visible behavior. For silent units, let a look, touch, blocked movement, prop state change, or environmental interruption carry the turn.

Use one dominant image at a time. A rain bead stretching across a train window, a thumb flattening a letter crease, the gap left by a pulled-out chair, or a bulb failing to stop swaying can carry more feeling than an adjective pile. The image must come from current scene truth and must visibly change or acquire meaning during the unit; never bolt on generic rain, tear, smoke, neon, or dust merely to make a shot “cinematic.”

## 3. Build rhythm with contrast, not constant motion

Map the chosen tempo to specific time in the shot plan:

- **Hold:** allow 0.3–1.0 seconds for the audience to register a look, object state, or spatial imbalance before the decisive action. A hold is active only if the frame has pressure.
- **Gather:** narrow attention through a gaze shift, hand tension, sound arriving, rack focus, or a motivated move. Do not add multiple competing camera motions.
- **Turn:** place the cut, focus change, action completion, or vocal pressure on an exact word, breath, impact, or glance—not on a vague “emotional moment.”
- **Arrest:** after a reveal, use stillness, an interrupted action, or a sound drop when the image needs to be absorbed. Do not immediately explain the meaning with a new gesture.
- **Release:** let a completed action, exhale, exit, sound decay, or musical resolution move the scene forward only when the source supports release. Withholding is also a valid ending.

Vary distance and motion because perception changes, not because a cut quota exists. An unbroken static close shot can be more rhythmic than three cuts if the eyes, breath, voice, and sound have a controlled progression. Conversely, a reaction insert or sound-led cut earns its place when it changes what the audience understands.

## 4. Make camera, performance, and sound agree

The same dramatic turn should be legible in three compatible channels whenever the scene permits:

| Channel | A specific, executable choice |
| --- | --- |
| Frame | Whose experience owns the shot; crop, screen position, depth, and the first thing seen |
| Performance | One physical or vocal pressure change with a start, turn, and residue |
| Sound | A physical sound, breath, silence, dialogue cadence, or score shift that happens at the same moment |

Do not describe all three channels as separate decoration. Write their causal relation in playback order: the key turns in the lock, her held breath breaks, then the camera leaves the listener only after the sound has died. If score is used, it must support rather than duplicate the action.

`overall_soundscape` must describe the actual sound rhythm of this unit: which bed persists, what sound enters or stops, and where a physical sound or breath punctuates the turn. Do not reuse an atmospheric sound list across scenes.

## 5. Non-diegetic music is a creative choice, not a default ban

Use `non_diegetic_music: N/A` only when the source, user, or directing decision calls for no audience-only score. Otherwise write a compact, filmable score cue in the canonical H3 field: instrumentation or texture, tempo/pulse, when it enters, and how it changes or ends. Never use abstract function labels such as “emotional music” or “sad score.”

Examples of adequate specificity:

```text
non_diegetic_music: One muted piano note repeats at a slow, uneven interval under the held look. A low cello harmonic enters only when the key turns, then stops before the final breath.
```

```text
non_diegetic_music: N/A
```

Diegetic music remains in `detailed_description`; do not mislabel a radio, phone, television, street performer, or audible instrument as score.

## 6. Prompt-level rhythm audit

Before delivery, read the final `detailed_description` aloud at the intended duration and check:

1. Can a viewer identify the opening pressure without being told an abstract emotion?
2. Is there one exact trigger and one irreducible turn, tied to an observable time, word, sound, or action?
3. Does every camera move, cut, rack focus, sound entry, or silence change attention rather than decorate the prose?
4. Does at least one scene-specific image change meaning across the unit?
5. Can an actor play the line with a pre-line impulse, a turn, and a post-line residue?
6. Does the soundscape have an onset, change, or decay that supports the tempo curve?
7. Does the final 0.8–1.0-second pose preserve a changed afterimage rather than merely stopping the action?
8. If the words “cinematic,” “emotional,” “beautiful,” “tense,” and “slow” are deleted, are the image, rhythm, and feeling still directly filmable?

If any answer is no, return to the `EMOTIONAL_RHYTHM_MAP` and rewrite the owning `SHOT_SCORE`; never patch the final prompt by adding more mood adjectives.
