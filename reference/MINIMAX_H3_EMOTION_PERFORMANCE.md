# MiniMax H3 Emotion and Vocal Performance

Use this reference together with `MINIMAX_H3_ACTOR_DIALOGUE_CRAFT.md` for every MiniMax H3 unit containing dialogue, voice-over, lyrics, crying, laughter, breathing, or another human vocal event. First inherit the speaker's exact baseline from the project `VOICE_BIBLE` in `MINIMAX_H3_LONG_SCRIPT_UNITS.md`; this file may direct the current pressure-state and phrase-level change, but it must not silently replace that baseline. The companion file converts the diagnosis into concise, playable actor direction. Together they prevent technically correct speech from sounding like a neutral read-through. When the chosen framing keeps the face or upper body readable and the scene depends on concealed, contradictory, delayed, or restrained emotion, also use `MINIMAX_H3_MICRO_EXPRESSION.md` to compile a shot-local `MICRO_PERFORMANCE_SCORE`; it adds observable acting detail but never changes dialogue, voice identity, timing ownership, shot structure, H3 routing, or output fields.

The source examples behind this method demonstrate that the same line can become teasing feigned anger, restrained anger, explosive rage, stifled hurt, wounded longing, or quiet grief when the subtext, vocal mechanics, physical resistance, and post-line behavior change. Do not copy an example label mechanically. Diagnose the dramatic situation from the script.

## 1. Emotion comes from dramatic intention

Before writing the prompt, resolve five questions for each vocal event:

1. **Literal action:** What is the speaker doing with the words—warning, testing, dismissing, confessing, bargaining, hiding, comforting, provoking, or letting go?
2. **Hidden need:** What does the speaker actually want from the listener, including the opposite of the literal sentence?
3. **Obstacle:** What prevents the need from being stated directly—pride, fear, shame, grief, duty, disbelief, physical weakness, or social restraint?
4. **Energy direction:** Does emotion move outward, stay compressed, collapse inward, or change direction during the line?
5. **Turn:** Which exact word, pause, look, breath, or listener reaction changes the emotional state?

Write a one-sentence `EMOTION_INTENT` internally before serialization:

```text
Surface action + hidden need + resistance + turn.
```

Example pattern: `She dismisses the rumor as absurd, but the exhaustion beneath the sarcasm reveals that she desperately wants it to be true; her certainty weakens on the final phrase.`

The prompt must communicate this conflict through observable voice and body behavior. Do not paste the internal label into `<d>`.

## 2. Build a voice profile, not an adjective

For every speaker and every emotionally distinct phase, begin from the verbatim `VOICE_BIBLE` entry and specify only the applicable current changes:

- **Pitch/register:** low, mid, high, dropping, briefly lifting
- **Volume:** near-whisper, quiet, conversational, firm, raised, shouted
- **Timbre/resonance:** dry, breathy, tight, warm, nasal, hoarse, chest-led, throat-held
- **Articulation:** clipped, precise, softened consonants, words squeezed out, consonants hardening
- **Tempo:** use the approved speech-rate calculation only in the internal timing manifest; in the copyable H3 prompt, direct the actual time window, pauses, stress, and phrasing rather than numerical characters-per-second
- **Breath:** short nasal inhale, held breath, swallowed breath, controlled exhale, breath catching, heavy recovery
- **Stress:** name the exact original word or phrase receiving extra force or softness
- **Pause behavior:** comma pause, hesitation, delayed reply, swallowed pause, sentence-end hold
- **Ending contour:** rising, falling, cut off, fading into breath, held flat, suddenly softened

Generic instructions such as `sad voice`, `angrily`, `emotional`, or `speaks naturally` are insufficient unless the prompt also defines these audible mechanics.

Because every H3 unit is independently generated, a relative instruction such as `same voice as H3-001`, `match the previous clip`, or `与 H3-002 完全一致` is also insufficient and forbidden. Repeat the speaker's baseline profile in that unit, then direct only the current pressure-state change. An actual submitted voice reference can support the repeatability, but does not replace the written profile.

## 3. Give every line an acting envelope

Each vocal event needs a chronological envelope with real timeline space:

### Pre-line beat

Define what the actor does before the first word: eye focus, inhale, swallow, jaw set, lip compression, posture change, hand tension, or weight shift. This creates thought before speech.

### During-line progression

Divide the line by its existing punctuation or semantic phrases. For each phase, specify:

- gaze and listener relationship
- brow, eyelid, jaw, mouth-corner, or chin behavior
- breath and vocal shift
- one restrained hand or posture action when useful
- the exact word or phrase where the emotional turn occurs

### Post-line residue

Reserve a hold after the last word. Define whether the actor maintains eye contact, looks away, fails to leave, loosens a clenched hand, suppresses a smile, lets a tear remain, or releases a breath. The residue reveals whether the words were believed.

Do not finish a vocal event on the last phoneme and cut immediately unless the script intentionally demands interruption.

## 4. Dialogue and voice-over are directed differently

### On-screen dialogue

- Keep lip synchronization precise.
- Keep the eyes, mouth, jaw, breath, hands, and listener reaction synchronized with the vocal turn.
- Limit the actor to one clear major gesture per short line unless the script requires action; several competing gestures make the result theatrical and unstable.

### Off-screen voice-over

- Use the exact H3 phrase `says in an off-screen voiceover`.
- Immediately state that the corresponding visible character's lips remain completely closed.
- The visible performance still carries emotion through gaze, breathing, pace, shoulders, hands, and interaction with the environment.
- Direct the narration as active thinking, not reading. Tie subtle vocal shifts to exact phrases while preserving the transcript verbatim.
- A reflective voice-over may begin as factual recitation, tighten around a painful fact, hesitate at a feared word, and soften after an admission. Derive the curve from the script rather than applying this example universally.

## 5. Six evidence-backed emotional patterns

These are reusable patterns, not automatic labels.

### Teasing feigned anger

- Surface: dismiss or chase the listener away.
- Hidden need: wants the listener to stay or respond.
- Voice: playful emphasis, slight nasal color, softened second phrase, lightly rising tail.
- Body: pretend glare with relaxed shoulders; suppressed smile leaks through one mouth corner; a small dismissive gesture retracts instead of completing the rejection.
- Forbid: genuine hatred, shouting, cartoon pouting, repeated waving.

### Restrained anger

- Surface: controlled rejection or warning.
- Hidden need: preserve dignity and avoid an uncontrolled outburst.
- Voice: low, slow, throat-held, consonants firm; volume drops rather than rises after the pause.
- Body: fixed eye contact, lips gradually tighten, jaw hardens, fingers slowly clench, one deliberate swallow.
- Forbid: lunging, screaming, crying by default, exaggerated glare.

### Explosive rage

- Surface: force the listener away immediately.
- Hidden need: regain control after restraint breaks.
- Voice: compressed opening that rapidly expands; a sharp replenishing inhale; stronger second phrase while remaining intelligible.
- Body: shoulders rise with the held breath, torso drives forward once, one decisive gesture, heavy recovery afterward.
- Forbid: repeated lunges, flailing, grotesque facial distortion, unclear words.

### Stifled hurt

- Surface: pushes the listener away because arguing feels impossible.
- Hidden need: wants the injury acknowledged.
- Voice: low, tight, slightly nasal; first phrase squeezed out, second phrase softer and broken by controlled breath.
- Body: gaze drops, shoulders close inward, fingers grip fabric, eyes redden without automatic tears, chin tremor is small and immediately restrained.
- Forbid: melodramatic sobbing, shouting, large dismissive gesture.

### Wounded longing

- Surface: tells the listener to leave.
- Hidden need: hopes to be stopped or reassured.
- Voice: soft, low, fragile nasal resonance; pause carries expectation; ending falls gently rather than attacking.
- Body: eye contact is attempted then abandoned, hands twist fabric, torso turns slightly while weight stays planted, the final look-back remains incomplete.
- Forbid: childish cuteness, exaggerated pout, actual exit unless scripted.

### Quiet grief / silent tear

- Surface: completes a restrained farewell.
- Hidden need: maintain composure long enough to finish.
- Voice: low, light, controlled, nearly breath on the last phrase; breath catches at existing punctuation.
- Body: eye focus softens then briefly returns; moisture gathers before one blink releases one tear; no wiping unless scripted; body settles downward after the line.
- Forbid: instant streams of tears, repeated wiping, sobbing, anger leakage not supported by the scene.

## 6. Select emotion from the scene, not the vocabulary

The same words may carry opposite intentions. Use the surrounding action, preceding beat, relationship history, scene objective, and aftermath to choose the performance. Never infer emotion from a single keyword such as `恨`, `走`, `对不起`, or `没事`.

When the script supports more than one plausible interpretation and the choice would materially change the scene, present concise options and ask. When context is sufficient, choose the interpretation and state it in the HTML's director note.

## 7. Sound supports performance

- Keep dialogue intelligible above ambience and physical sound effects.
- Include synchronized breath, swallow, cloth tension, footsteps, or another physical sound only when it belongs to the acting beat.
- Use no non-diegetic score. Let dialogue, breath, movement, weather, room tone, and other diegetic sound carry the performance; always serialize `non_diegetic_music: N/A` when the H3 format requires that field.
- Do not repeat dialogue in `overall_soundscape`.

## 8. H3 serialization

- Keep the original words and punctuation only inside `<d>[Language] ...</d>`.
- Put emotion intent, voice profile, delivery, physical action, and timing outside `<d>`.
- Put the one dominant delivery cue immediately adjacent to `<d>`; do not bury it after camera setup or character-rate math. When helpful, state the unwanted reading explicitly, such as “not neutral,” “not contemptuous,” or “not a recital.”
- In the canonical English prompt, write the performance as natural chronological English.
- In the Chinese director storyboard, use the parent SKILL's natural Chinese sections and colon-plus-next-line speech boundary, without `<d>` or visual reference tags. The English companion alone uses its six-section syntax. Both serialize the same shot times, exact spoken words, vocal source, emotional turn, sound design, and constraints; syntax is not mirrored literally.

## 9. Anti-recital audit

Before delivery, verify every vocal event:

- has a script-derived surface action and hidden need
- converts that analysis into an immediate objective and playable action
- has an audible voice profile beyond a generic emotion word
- has a pre-line thought/breath beat
- changes or develops during the line
- ties its entry, operative phrase, turn, and ending to exact original words or punctuation
- reserves a post-line residue or intentional interruption
- synchronizes facial and body micro-beats with exact phrases
- keeps all source words and punctuation unchanged
- keeps Chinese speech within the approved character-rate range
- keeps the numerical character-rate calculation outside the copyable H3 prompt
- avoids excessive gesture, melodrama, and emotion unsupported by the scene
- preserves the character's `VOICE_BIBLE` baseline exactly and changes only the scene-specific pressure state

If removing the emotional adjectives would leave the delivery unchanged, the direction is still too generic. Rewrite it as observable vocal and physical behavior.
