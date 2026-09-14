# MiniMax H3 Actor and Dialogue Craft

Use this reference together with `MINIMAX_H3_EMOTION_PERFORMANCE.md` for every MiniMax H3 unit containing dialogue, voice-over, lyrics, cries, laughter, or other human vocal performance. Inherit the stable speaker identity from the project `VOICE_BIBLE`; direct only the current playable action and pressure-state change. Its job is to turn correct script analysis into concise, playable actor direction that H3 can prioritize. The target is not “more emotional adjectives”; it is a visibly and audibly different take without voice drift between independently generated units.

## 1. Protect the performance hierarchy

When a prompt becomes dense, preserve information in this order:

1. exact speaker, original words, language, and lip/voice-over relationship
2. the playable action and hidden need driving the line
3. the phrase where control changes and the line's ending contour
4. the few voice mechanics that make the change audible
5. pre-line thought, one useful physical action, and post-line residue
6. supporting camera, environment, and continuity detail

Do not let character-rate math, lens specifications, lighting inventories, or psychological exposition displace the actor-facing delivery cue. Reduce redundant technical or decorative prose before reducing the performance score.

## 2. Convert analysis into a playable acting score

Analyze the scene internally, but give the actor an action they can perform. Resolve:

- **Given circumstance:** what has just happened and what fact is active now?
- **Immediate objective:** what response or protection does the speaker want in this moment?
- **Playable action:** what is the speaker doing to the listener or to themself—testing, concealing, dismissing, cornering, calming, seducing, warning, bargaining, confessing, or retreating?
- **Unspoken truth:** what must not be admitted directly?
- **Resistance:** what holds the emotion back or pushes it outward?
- **Turn:** on which original phrase, pause, breath, look, or reaction does control change?
- **After-state:** what remains once the words are finished?

Write an internal score before serialization:

```text
The speaker [playable action] to achieve [immediate objective] while hiding [unspoken truth]; on [exact phrase/pause], control [tightens / breaks / reverses / collapses], leaving [after-state].
```

Do not paste this analysis wholesale into the prompt. Translate it into one concise dominant delivery instruction and observable phrase-level behavior.

## 3. Exclude the most likely wrong take

H3 can satisfy the words while choosing the wrong acting convention: neutral recital, generic sadness, theatrical anger, open sarcasm, horror-story narration, commercial voice-over, or exaggerated crying. When one or two wrong readings are genuinely likely, exclude them immediately beside the spoken line.

Pair every negative with the correct playable alternative:

- Weak: `Do not sound neutral or sarcastic.`
- Playable: `Do not read this neutrally or as open sarcasm; she is trying to ridicule a hope that has already frightened her.`

Do not stack long prohibition lists. Name only the failure modes that would materially change this scene, then state what the actor is doing instead.

## 4. Shape the line into thought units

Actors speak thoughts, not character counts. Divide the original line only at existing punctuation or natural semantic boundaries. For each thought unit, choose one dominant function:

- **Entry impulse:** the thought or sensation that makes the first words escape
- **Operative phrase:** the original word or phrase carrying the speaker's immediate action
- **Turn:** the point where the hidden need leaks out or is forced back under control
- **Exit:** how the final word lands—attacks, falls, fades, hardens, breaks, or remains unfinished

For a short line, two contrasting thought units are usually stronger than instructions on every word. For a long voice-over, choose three to five emotional waypoints across the full passage; do not assign a new emotion to every comma.

Treat punctuation as active thought. An ellipsis may be shock, concealment, expectation, or loss of nerve; a comma may hold back a confession; a sentence ending may close a door or fail to do so. Direct the reason for the pause, not metronomic counting.

## 5. Direct actor-grade vocal technique

Choose only the vocal parameters that carry this specific dramatic action:

- **Register and placement:** chest-led, throat-held, head-light, low, mid, briefly lifting, dropping
- **Intensity versus volume:** quiet can still be forceful; loud can still be frightened
- **Breath support:** held, shallow, opened, swallowed, caught, leaking, released after the line
- **Articulation:** clipped consonants, softened consonants, words squeezed out, precision used as control
- **Operative stress:** identify the exact original phrase that receives force, softness, delay, or loss of support
- **Cadence:** whether thoughts connect, hesitate, rush and stop, or arrive as separate decisions
- **Ending contour:** falling, brittle, fading into breath, cut short, held flat, unexpectedly softened

Avoid voice-parameter inventories. A baseline voice plus one audible change at the turn and one ending behavior is usually enough. Contradictory adjective piles produce generic acting.

## 6. Bind voice and body to the same inner event

The physical performance must reveal the same struggle as the voice:

- Before the line, give one thought-producing action: a delayed look, swallow, inhale, jaw set, failed smile, hand tension, or weight shift.
- During the line, use one main physical behavior tied to the turn. Do not pantomime every word.
- After the line, reserve a residue: held breath, eyes that do not rise, a hand that fails to release, shoulders that drop late, an incomplete exit, or a look the speaker cannot sustain.
- If a listener is visible, their reaction should occur at the turn or after-state, not randomly during the words.

Choose framing and cuts that protect the performance. Keep the face, profile, hands, or gait readable at the emotional turn, and do not cut away on the exact beat that must be seen unless the script deliberately hides it.

## 7. Dialogue and voice-over require different acting

### On-screen dialogue

- Preserve exact lip synchronization and keep the mouth visible enough when the line matters.
- Let gaze, jaw, breath, and one physical action change with the operative phrase.
- Direct the speaker toward a listener, absent person, object, or private thought; never leave the line without an eyeline relationship.

### Off-screen voice-over

- Use the exact phrase `says in an off-screen voiceover` and keep the visible character's lips completely closed.
- Treat narration as active thinking occurring now, not as a polished read recorded later.
- Give the passage a dramatic task: remembering against resistance, rationalizing, testing a belief, avoiding a name, or admitting what the image cannot say.
- Let visible pace, gaze, shoulders, hands, and interaction with the environment carry the same turns without illustrating every noun.

## 8. Serialize one compact performance paragraph

Follow the parent SKILL's paired-prompt contract. In Chinese, put the full voice baseline and playable delivery before a colon, followed by the exact line alone; no `<d>` or visual reference tags. In the English companion, bind the same delivery immediately before `<d>`. The following is an internal score outline, not a literal output shell:

```text
At [start/end window], [real vocal source], in [full baseline voice],
[playable delivery, entry behavior, exact-phrase turn, ending contour], says:
[exact approved speech; English companion wraps only this payload in <d>]
[Reserve the aftermath in a separate timed action/silent shot.]
```

Adapt the grammar to the scene; do not output this as a literal fill-in form. Keep the original words only inside `<d>`. Never put numerical characters-per-second instructions in the copyable prompt. Start/end windows and meaningful pauses are allowed, but they must support natural thought and performance.

## 9. Keep direction selective enough to execute

More instructions do not automatically create more acting. For each short line, prefer:

- one playable action
- one hidden contradiction
- one likely wrong reading to exclude when necessary
- two thought units or one clear turn
- one baseline voice and one audible change
- one pre-line impulse, one main physical action, and one residue

For a long passage, preserve one overall task and a small number of waypoints. If the prompt asks the actor to display many unrelated emotions, gestures, facial changes, and voice qualities at once, simplify until the take can be performed coherently in one pass.

## 10. Actor-quality audit

Before delivery, verify every vocal event:

- **Playable-action test:** an actor can answer “What am I doing with these words?”
- **Distinct-take test:** following the direction produces a recognizably different take from neutral reading.
- **Thought-unit test:** the entry, turn, and ending attach to exact original phrases or punctuation.
- **Wrong-reading test:** any excluded reading is paired with a clear alternative, not only a prohibition.
- **Vocal-craft test:** selected voice mechanics support the dramatic action and do not contradict one another.
- **Body-voice test:** breath, gaze, face, hands, posture, and listener reaction arise from the same inner event.
- **Residue test:** the performance continues briefly after the last phoneme unless interruption is intentional.
- **Priority test:** the dominant performance cue sits beside `<d>` and is not buried by technical prose.
- **Timing test:** numerical character rate appears only in internal shotlist notes, never in the copyable H3 prompt.
- **Transcript test:** every source word and punctuation mark remains unchanged.
- **Voice-bible test:** the baseline age, range, timbre, habitual pace, sentence ending, and prohibited readings remain identical across units.

If a competent actor could follow the prompt and still reasonably deliver a flat, generic recital, the performance direction is not finished.
