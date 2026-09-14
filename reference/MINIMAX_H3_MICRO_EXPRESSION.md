# MiniMax H3 Micro-Expression and Restrained Performance

Use this reference when a MiniMax H3 shot keeps a human face or upper body readable and the screenplay depends on concealed, contradictory, delayed, or restrained emotion. It converts subtext into small chronological actions that H3 can render. It does not create a separate prompt, choose an H3 mode, change unit boundaries, or override the approved shot plan.

## 1. Parent-workflow authority

The JMCAI Shotlist Builder remains authoritative for:

- source truth, dialogue, blocking, prop state, and relationship turns;
- H3 unit duration, internal cuts, and cross-clip continuity;
- I2VA, FL2VA, L2VA, or Ref2VA routing;
- `VOICE_BIBLE`, speaker IDs, `<d>` payloads, field order, and reference indexing;
- the paired Chinese director storyboard and English six-section companion compiled from one approved timeline.

Use this reference only to compile the acting layer inside an already approved shot window. Ignore the source skill's standalone defaults of six seconds, one close-up, one continuous shot, Chinese-only prose, mode recommendation, and final-prompt delivery.

## 2. Trigger and skip rules

Compile a `MICRO_PERFORMANCE_SCORE` when all of these are true:

1. a face, profile, throat, breath, hand, posture, or prop interaction is readable in the chosen framing;
2. the current source beat contains a hidden need, social mask, interrupted intention, delayed reaction, or pressure to suppress emotion;
3. a small visible change materially clarifies the relationship turn or after-state.

Typical triggers include restrained grief, held-back tears, suppressed anger, hesitation, longing, shame, guilt, disbelief, social politeness under pressure, fear disguised as calm, emotional numbness, and a meaningful silent reaction.

Skip the micro-expression layer when:

- the face is unreadable, occluded, too distant, or intentionally withheld;
- the unit is driven by locomotion, spectacle, physical causality, or environment rather than an acting turn;
- the source asks for direct, open emotion with no concealment or contradiction;
- the same meaning is already carried by a stronger scripted action and another facial chain would become decorative;
- the required action would contradict the reference image's baseline, approved blocking, or the screenplay.

Do not diagnose deception, personality, trauma, or mental state from facial movement. These are directing choices, not medical, psychological, or FACS claims.

## 3. Compile one internal score

Before writing final shot prose, resolve:

```text
MICRO_PERFORMANCE_SCORE
shot_and_window: exact shot and usable time window
outward_mask: what the character is trying to show
hidden_emotion: what must not be openly revealed
trigger: exact word, look, sound, touch, fact, or listener reaction
baseline: source-consistent starting face, gaze, breath, posture, and prop state
first_leak: the smallest involuntary readable cue
suppression: the deliberate attempt to hide or repair that cue
escalation_or_reset: optional second leak, interrupted intention, or reset beat
after_state: what remains visibly changed at the end
polarity_lock: emotional readings the ending must preserve and the likely wrong reading to exclude
selected_chains: 1-5 chronological observable action chains
```

This score is planning metadata. Do not add it as a new H3 output field. Serialize only its directly filmable consequences inside the chosen shot description.

## 4. Mask-versus-leak construction

Build restrained acting as a causal sequence:

1. **Baseline** — preserve the approved identity, expression baseline, eyeline, posture, hands, wardrobe, props, and framing.
2. **Leak** — allow one brief involuntary cue after the actual trigger.
3. **Suppression** — show the character actively containing or disguising the cue.
4. **Escalation or reset** — only when the relationship turn needs a second pressure change.
5. **After-state** — return toward control, but do not erase what happened. The face, gaze, breath, posture, or prop grip remains subtly changed.

Protect emotional polarity. Grief must not drift into relief, restraint into confidence, longing into cheerful flirtation, or shock into horror unless the source supports that change.

## 5. Action-selection discipline

Choose only cues that are visible at the planned scale. Prefer 1-5 chains across two or three channels rather than an inventory covering every facial region.

- Extreme close-up: eyelids, gaze focus, brow, lip pressure, jaw, nostril breath, swallow.
- Close-up: add head angle, throat, shoulders, and one readable hand or prop cue.
- Medium close-up: prioritize posture, weight, hands, prop pressure, eyeline, and one facial cue.
- Wider framing: use hesitation, reach interruption, weight shift, body orientation, and prop behavior; do not claim tiny eyelid changes the audience cannot see.

Use asymmetry sparingly for involuntary leakage. Use one dominant physical behavior per spoken thought unit. Every action needs an onset, change, or result; avoid static adjective stacks.

## 6. Observable action-chain library

Select and rewrite only what the source supports. Do not dump IDs or library wording into the final prompt.

### Eyelids and gaze

- M001: lower eyelids tighten slightly → gaze turns aside → returns half a beat later
- M002: upper eyelids become heavy → blink arrives late → focus briefly empties
- M003: gaze moves closer first → head stays still → outer eye line retreats
- M004: eyes moisten → blink is withheld → gaze drops quickly
- M005: one eyelid narrows → focus locks → the character deliberately releases it
- M006: eyes scan an exit → return to the listener → the social mask resumes
- M007: a pupil-like freeze → rapid refocus → one small nod

### Brow and forehead

- M008: inner brows pull upward briefly → flatten immediately
- M009: brow gathers → is deliberately smoothed → a faint residual crease remains
- M010: one brow tail falls → the mouth tries to repair the social mask
- M011: brows release → eyes remain tense
- M012: one brow peak lifts → doubt is pressed back down
- M013: forehead stays controlled → eyelids carry the leak
- M014: brow reaction arrives only after the spoken phrase ends

### Mouth and jaw

- M015: mouth corner tries to lift → one side fails first
- M016: lip line flattens → jaw locks → breath escapes through the nose
- M017: lips part → inhale catches → lips close again without speech
- M018: maintained smile lasts too long → corners lose support
- M019: inner lip is caught → released only before a swallow
- M020: jaw tightens to one side → answer becomes shorter
- M021: mouth smiles while the eyes do not join it, only when the source requires a false smile

### Throat and breath

- M022: swallow appears first → gaze evades afterward
- M023: inhale is held → chest barely moves → air leaks through the nose
- M024: broken exhale → shoulders drop half a beat late
- M025: throat moves before speech → voice enters lighter
- M026: breathing quickens while the face stays controlled
- M027: a complete exhale passes before eye contact becomes possible
- M028: an extra breath arrives only after the sentence ends

### Head, neck, and shoulders

- M029: chin lowers slightly → neck remains rigid
- M030: head begins to turn away → stops midway
- M031: shoulders brace first → face remains outwardly calm
- M032: torso recoils slightly → feet or seated base remain fixed
- M033: eyes move before the head follows
- M034: shoulders release late → mouth tension releases afterward
- M035: a swallow shifts the neck → posture is immediately repaired

### Hands and props

- M036: fingertips press a cup rim → release → grip again
- M037: hand reaches halfway → stops → redirects into adjusting clothing
- M038: thumb rubs fingertip → gaze avoids the listener
- M039: prop nearly slips → is caught and stabilized immediately
- M040: hand moves behind the back → shoulder stays rigid
- M041: paper is smoothed repeatedly → speech fails to begin
- M042: fist starts to form → becomes a controlled fingertip tap

### Timing and interruption

- M043: reply arrives half a beat late → blink precedes the first word
- M044: action begins → emotion interrupts it → a smaller substitute action completes
- M045: smile arrives first → true emotion catches up → smile loses support
- M046: expression collapses only after the line ends
- M047: eye contact holds for two beats → breaks on the third
- M048: a trigger word causes one missed breath
- M049: facial repair happens too quickly → over-control becomes the leak

### Asymmetry

- M050: left mouth corner falls → right side still carries the mask
- M051: one side of the brow tightens → the other remains level
- M052: one hand tightens → the other performs normality
- M053: one shoulder rises → is pressed down immediately
- M054: one eyelid grows heavy → gaze retreats diagonally
- M055: one nostril shifts → jaw contains the reaction
- M056: body weight shifts → head holds its original position

### Posture and space

- M057: body moves forward a fraction → stops before closing distance
- M058: body steps back → gaze remains with the other person
- M059: torso faces the exit → eyes remain on the listener
- M060: chest contracts → arms stop short of a full defensive fold
- M061: seated posture straightens → voice drops lower
- M062: body moves closer to a prop instead of the person
- M063: the character begins to turn → hears the cue → stops

### Mask repair

- M064: expression cracks → a social expression is rebuilt, only if the scene supports it
- M065: tears threaten → one blink contains them
- M066: anger rises → becomes a quiet counter-question
- M067: fear appears → one nod attempts to cover it
- M068: shame is exposed → a short laugh fills the gap, only if scripted or strongly supported
- M069: grief pulls the face down → an inhale rebuilds control
- M070: control nears failure → sleeves or another approved prop are straightened to recover

## 7. Emotion routing library

Use these as search routes, not predetermined readings. Derive the actual mask, leak, and after-state from scene context.

- Love and loss: unreturned love; wanting to ask someone to stay; private desire inside a blessing; uncertain reunion; retreat before confession; hearing that someone will leave; seeing the other person happy; old lovers turned strangers; wanting closeness while blaming oneself; final tenderness.
- Grief and restraint: holding back tears; breaking only after comfort; delayed response to bad news; saying “I am fine” as a mask; holding together until alone; swallowing tears; grief interrupted by work; emptiness after goodbye; hearing regret; admitting loss.
- Suppressed anger: polite anger; being unable to react to an insult; controlled questioning; threat behind a smile; anger turning into silence; stopping an impulse to throw something; the second before an argument; self-reproach after anger; protective anger; calm after betrayal.
- Fear and disguise: fear of being seen through; smiling while danger approaches; searching for an exit; hearing a threat; inability to ask for help; performing calm; body reacting first; numbness after fear; vigilance in a crowd; freezing after touch.
- Guilt and avoidance: inability to explain; late apology; seeing consequences; forgiveness making guilt worse; avoiding a name; trying to compensate; silence under questioning; guilt becoming tenderness; self-blame becoming numbness; accepting responsibility.
- Jealousy and pride: pretending to bless; gaze sticking to the other person; hearing an intimate name; losing a comparison; shame after jealousy; possessiveness under restraint; acidity hidden in humor; deliberate coldness; protectiveness crossing a boundary; withdrawing from a triangle.
- Joy and disbelief: delayed good news; smile afraid to expand; fear after happiness; freezing when chosen; reunion after separation; finally being understood; joy close to tears; blankness after victory; disbelief after praise; relief that may or may not include a smile.
- Shame and exposure: feelings seen through; repairing a verbal mistake; awkward social mask; shame turning to anger; avoiding eye contact; wanting to disappear; discomfort under praise; a secret exposed; body retreating first; forced composure.
- Resolve and attachment: saying goodbye; pause before turning; regret after harsh words; cutting a relationship; returning an object; final embrace; refusing to turn while still listening; choosing to release; shutting emotion down; softening only after leaving.
- Hope and hesitation: wanting to believe; tentative approach; hearing an opportunity; trying to speak again; fear of disappointed hope; careful confirmation; an unsaid wish; eyes brightening first; reaching then stopping; warmth returning after numbness.
- Disgust and politeness: disgust contained; sensory discomfort; forced touch; surface courtesy; disgust turning to ridicule; stopping a retreat; smile becoming rigid; wanting to wipe a hand; recognizing hypocrisy; polite refusal.
- Fatigue and persistence: delayed reactions from exhaustion; forcing alertness; being depleted while comforting another; actions becoming smaller; brief loss of focus; heavy breath; holding through the last task; tired social expression; refusing further explanation; finally lowering defenses.
- Surprise and understanding: initial disbelief; a brief freeze; smile disappearing; information landing in stages; sudden comprehension; reaction arriving late; surprise concealed; inability to speak; gaze moving to evidence; rebuilding the face.
- Numbness and return: emotional absence; mechanical response; pain arriving late; a name restoring focus; repeated action interrupted; gaze refocusing; delayed breath; voice emptying first; touch restoring presence; collapse only after the task ends.
- Power and vulnerability: authority showing fear; a crack inside dominance; hesitation before an order; being seen through by a subordinate; controlling a room; releasing only in private; authority becoming fatigue; apology without lowering posture; protecting a weakness; joyless victory.

## 8. Performance prototype families

Select one to three families only when they help clarify the acting design:

- restrained inner injury: hold tears, swallow a confession, hear bad news, remain misunderstood, perform “fine,” pause before departure, begin but fail to speak;
- intimacy under tension: approach then retreat, stop a touch, flee after eye contact, half-confession, adjust the other person's clothing, use a prop as cover, freeze after farewell;
- social mask: maintain politeness too long, nod after being hurt, public congratulations, suppress embarrassment, contain anger in a meeting, recover after being exposed;
- alert fear: hear an unexplained sound, discover a lie, avoid looking back, search for an exit, voice catches, body freezes first, attempt a controlled escape;
- guilt and regret: avoid eye contact, late apology, slow hand movement, listen without defending, erase evidence, accept responsibility, apologize before leaving;
- anger control: jaw lock, shortened answer, nostril flare, fingertips press a surface, silence as resistance, anger interrupted, attack withdrawn;
- jealousy and possession: observe intimacy, pretend indifference, compare oneself, follow too long with the eyes, use too much pressure on a glass, ask too softly, retreat to the edge;
- edge of collapse: social expression fails, breath breaks, line stops halfway, hands lose their task, shoulders release suddenly, delayed tear, repeated self-repair;
- relief or returning warmth: complete exhale, shoulders release late, eye contact finally returns, hand unclenches, quiet after an embrace, truth leaves a changed stillness;
- numb withdrawal: slow blink, delayed response, mechanical nod, voice-face mismatch, action continues by routine, emotion arrives later, collapse only after completion.

## 9. Timing and density

Assign micro-actions inside the time already owned by the shot. Timestamps mark acting beats, not cuts. Normal physical speed is the default.

- Under 2 seconds: one leak and one immediate containment or residue.
- 2-4 seconds: baseline, one leak, one suppression or after-state; usually 2-3 beats.
- 4-7 seconds: 4-6 beats, including baseline, leak, suppression, optional second leak/reset, and after-state.
- 8-10 seconds: 6-9 beats only when the whole shot genuinely holds a readable performance; otherwise divide actions across the existing shot score.
- 10-15-second H3 unit: never stretch one micro-expression over the full unit by default. Assign dense micro-beats only to the relevant internal shot or reaction window.

Prefer verbs such as `briefly`, `half a beat later`, `for less than half a second`, `immediately contains`, `refocuses`, `misses one breath`, and `tightens momentarily`. Avoid repeated `slowly`, `gradually`, `lingering`, `frozen`, or continuous slow camera drift unless the approved direction is intentionally lyrical.

Micro-actions should be sequential, not simultaneous. The actor cannot plausibly perform six separate leaks at the same instant, and H3 is more stable when each cue has a clear order and result.

## 10. High-tension reset pattern

For a sustained close-up with strong pressure and little macro action, use only the stages supported by the source:

```text
compressed baseline → first crack → interrupted intention → physical leakage → brief reset → aftershock suppression
```

A reset can be a short eye closure, blink, inhale, swallow, refocus, or prop-straightening action. It is not emotional erasure. After reopening or recovering, the character must remain changed. A climax need not become screaming, collapse, or tears.

## 11. Dialogue and voice integration

Preserve exact dialogue. Under the parent SKILL's current contract, put line-specific performance and full voice direction before the speech event. Chinese uses a colon followed by the original line alone; English wraps only the original payload in `<d>`. Put the aftermath in its separately timed action or silent shot rather than stacking instructions after the line. For each vocal event:

- use one pre-line cue that produces the thought;
- bind the main leak or containment action to an exact source word, phrase, punctuation mark, or listener reaction;
- preserve one post-line residue unless the source requires interruption;
- keep the locked `VOICE_BIBLE` unchanged and modify only line-level pressure, breath, stress, pause, or ending contour;
- do not let mouth-corner or jaw direction interfere with intelligible lip sync.

For voice-over, keep the visible character's lips fully closed and carry the same emotional route through gaze, breath, posture, hands, pace, and environment interaction.

## 12. Camera and continuity integration

Do not force a close-up or forbid a cut. The approved `SHOT_SCORE`, `SCENE_SHOT_LADDER`, and boundary ledger decide framing and edits. When a micro-beat carries the relationship turn, keep its relevant body channel readable and avoid cutting away at the exact leak unless hiding it is the chosen dramatic decision.

Every cut must still add information. A micro-expression is not justification for an otherwise unmotivated insert or scale reset. At a clip boundary, preserve the final gaze, breath phase, hand/prop pressure, posture, and emotional after-state whenever they remain visible in the next unit.

## 13. Risk-specific guardrails

Use only constraints needed for the current source and likely H3 failure mode.

- Accidental smile: for grief or restraint, prefer `the lip line remains level` or `the mouth corners do not lift`; avoid ambiguous phrases such as `gentle smile`, `bittersweet smile`, or `soft warmth` unless requested.
- Overacting: exclude large brow distortion, repeated shaking, pantomimed gestures, instant sobbing, or a dramatic head drop when unsupported.
- Unwanted tears: distinguish eyes moistening, one held tear, one released tear, and active crying. Do not add or forbid tears without source support.
- Emotion drift: name the one likely wrong after-state, then state the correct visible residue.
- Identity and scene drift: preserve approved face, hair, wardrobe, posture base, props, background, and light; do not repeat generic bans that the parent prompt already covers.
- Camera drift: lock a static camera only when the approved shot score calls for it. Do not import the standalone skill's default no-cut rule.

## 14. Bilingual serialization

Compile the Chinese director storyboard and English six-section companion using their distinct syntax but exactly the same:

- shot numbers and timestamps;
- action order and degree;
- mask, leak, suppression, reset, and after-state;
- dialogue payload, speaker binding, and operative phrase;
- emotional polarity and risk-specific exclusions.

Do not add a `MICRO_PERFORMANCE_SCORE` field to either prompt. Do not add mode recommendations or commentary after the copyable prompt. Restart no numbering because of this layer; it owns no H3 reference or speaker IDs.

## 15. Final micro-performance audit

Before delivery, verify:

- every micro-beat is caused by current scene truth rather than an emotion keyword alone;
- the chosen framing can actually show the directed cue;
- actions are chronological, physiologically plausible, and normal-speed;
- there are enough beats to remain alive but not enough to compete with dialogue, blocking, or prop causality;
- the first leak, suppression attempt, and after-state are distinct when the window allows them;
- emotional polarity does not drift during the final beat;
- mouth behavior remains compatible with lip sync and the intended emotion;
- tears, smiles, asymmetry, and prop manipulators appear only when supported;
- English and Chinese prompts preserve identical performance logic;
- the layer has not changed H3 routing, prompt schema, unit duration, reference indexing, or source dialogue.
