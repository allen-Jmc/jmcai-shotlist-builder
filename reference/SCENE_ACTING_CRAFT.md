# MiniMax H3 Scene Acting Craft

Use this reference together with `MINIMAX_H3_ACTOR_DIALOGUE_CRAFT.md` and `MINIMAX_H3_EMOTION_PERFORMANCE.md` for any H3 unit containing dialogue between characters, a confrontation, a negotiation, a comic beat, or any request about acting quality ("文戏", "演技", "台词", "表演").

Division of labour:

- `ACTOR_DIALOGUE_CRAFT` and `EMOTION_PERFORMANCE` control **how one speaker sounds and moves** — voice mechanics, thought units, emotional arc, anti-recital.
- `MICRO_EXPRESSION` controls **what the face and body leak**.
- This file controls **who listens, how lines are picked up, what each line does to the other person, who holds status, where stress and pauses sit, and whether the lines physically fit the time**.

Selection discipline applies to every rule below. For each item you write, be able to state four things: **input basis → performance purpose → visible/audible evidence → trigger timing**. If you cannot name the basis, do not write it. This is a menu, not a checklist to fill.

## 1. The listener track

Half of screen drama sits on the person not talking. For every line in a multi-character unit, direct the listener as well as the speaker.

For each line, resolve:

- **The landing word** — the exact word in the supplied dialogue that hits the listener. Bind to real text ("on hearing 败将"), never to an invented word.
- **The first reacting channel** — eyes, gaze, jaw, breath, or hand. Pick one; do not open three channels at once.
- **Reaction delay** — normally 0.2–0.4 s after the line lands. When the listener is stung or shocked, hold a 0.3–0.6 s freeze first, then react. A listener who expected it may barely react; not reacting is itself a performance and must be stated as such.
- **Suppressed interruption** — lips part and close again, an inhale that never becomes a word, half an inch of forward lean withdrawn.

Do not invent dialogue, footsteps, door sounds, or any audible action for an off-screen listener. An unseen partner exists only through the on-screen character's gaze, reaction, and information the user has already established.

## 2. Cue pickup

Four pickup types. Choose by relationship and stakes, not by habit.

| Type | Timing | Use for |
| --- | --- | --- |
| Normal pickup | opens 0.3–0.6 s after the previous line lands | steady exchange, ordinary conversation |
| Overlap / cut-in | opens while the last one or two characters of the previous line are still being spoken (0.1–0.3 s of overlap) | quarrels, urgency, dominating, familiar bickering |
| Interruption | previous line cut off mid-phrase; the interrupted speaker's line must be written as a fragment ending in "——" | loss of patience, status suppression, stopping the other from saying it |
| Delayed reply | 1–2 s of visible silence before speaking, with the listener's reaction written inside that silence | being stung, weighing, refusing to cooperate, residue after an emotional peak |

Rules:

- Without a reason, never let two characters alternate at an even pace. That even alternation is the single most common "recital" failure in generated dialogue.
- Overlap and interruption must be visible **in the dialogue text itself** (fragment, dash). Writing "she interrupts" in the description does not produce an interruption.
- Keep the pickup type consistent with the `EMOTIONAL_RHYTHM_MAP` beat; a delayed reply is a beat, not padding.

## 3. Playable action verbs

A professional actor plays a **verb** — what they are doing to the other person. Emotion is the by-product of that verb meeting resistance. Give each line one action verb, written as "to whom + doing what".

- **Attack:** 逼问 press, 揭穿 expose, 羞辱 shame, 威胁 threaten, 施压 pressure, 挑衅 provoke, 刺痛 sting, 激将 goad
- **Defend:** 搪塞 stall, 回避 evade, 否认 deny, 拖延 delay, 稳住 steady, 装傻 play dumb, 掩饰 cover
- **Draw close:** 试探 test, 讨好 please, 安抚 soothe, 示弱 yield, 求 plead, 哄 coax, 引诱 lure
- **Push away:** 拒绝 refuse, 打发 dismiss, 冷落 cold-shoulder, 警告 warn, 划清界限 draw a line
- **Reveal:** 坦白 confess, 认输 concede, 承认 admit, 交底 come clean

Strategy change:

- A character changes verb only when the previous verb fails — the other does not take it, counterattacks, or stays silent. Write the turn as "this did not work → try another", not as "anger becomes grievance".
- Before the new verb, give one visible moment of realization: gaze stops, breath breaks, the hand pauses mid-motion.
- The same line under a different verb is a different take. For "你走吧。": as 打发 — flat pace, no eye contact, returns to the task immediately; as 试探 — looks up to watch the reaction, tail of the line softens; as 求 said backwards — voice tightens, does not look away, waits for the other to stay.
- When the user has already specified the reading, the user wins; the verb exists only to give that reading a cause.

Keep verbs internal unless the user wants them shown. Serialize them through gaze, timing, stress, and delivery — never as an acting note inside the copyable prompt.

## 4. Status and power flow

For a two-hander, decide first **who holds the higher position and whether it flips**. "坐下" spoken from above and from below are two different scenes.

- **Higher position, pick 1–2:** steady gaze that does not rush away; speaks first or decides when the conversation ends; slower pace, does not hurry to fill silence; occupies space, few but complete movements; may decline to answer.
- **Lower position:** breaks eye contact first or keeps checking the other's reaction; faster pace, rising line-ends, self-correction; body drawn in, small self-soothing movements (touching an object, adjusting a hem); rushes to explain.

Rules:

- Status comes from the dramatic relationship, never from volume. A loud character can be the low-status one (bluffing); a quiet one can hold the room.
- Tension usually comes from a **flip**. State which line or action carries it — for example, the lower-status character not looking away for the first time.
- When no flip is called for, hold status steady. Do not let it wobble line by line.

## 5. Stress and pause

**Stress.** Ask what this line most needs the other person to hear. "我没说他偷了钱" changes meaning with each stressed word — 我 (someone else said it), 没 (denial), 偷 (borrowed, not stolen), 钱 (not money that was taken). One main stress per line, at most one secondary. Stress everywhere is stress nowhere. For irony, place the stress on the word being mocked; the tone turns one corner past the literal meaning.

**Pause.** Two kinds, and they are not interchangeable:

- **Logical pause** — grammatical, 0.2–0.4 s, no emotion, exists so the line is audible.
- **Psychological pause** — 0.5–1.5 s. The line is at the lips while the character thinks, restrains, searches for the word, or waits for the other. This is where the scene lives. Always state which word the pause precedes and what the face does during it.

Silence longer than 1.5 s needs visible content — an exchanged look, an avoidance, breath, a hand movement — or it renders as a stall.

## 6. Genre register

"Restrained vs expressive" is not enough; the genre grammar must also be right.

- **Slice-of-life / contemporary drama:** small movements, colloquial, incomplete sentences and particles allowed; few stresses, more pauses; avoid stage diction.
- **Period / epic / mythic drama:** breath low, consonants complete, line-ends do not rise; longer and steadier pauses; few but weighted movements — stillness carries more than motion; declarative lines land one word at a time on chest resonance, not on shouting.
- **Comedy:** setup → beat → punchline, with 0.3–0.6 s of air before the punchline and a clean, unlaughed delivery; delayed reaction (double take) where the character responds normally first and registers it 0.5–1 s later; deadpan where the flatter the face against absurd content the funnier it reads; confident scheme → collapse, where the collapse must be fast and total. Comedy comes from rhythm and contrast, not from facial amplitude — never squeeze a grin onto every line.
- **Dialect / accent:** only on request, and state the dialect and its degree (slight accent / full dialect).

## 7. Cross-unit emotional carryover

When a scene is generated as separate H3 units, no unit may start from zero.

At the head of each unit's opening state, include the **emotional current state**:

- the emotional quality and intensity the previous unit ended on (for example, anger at 7/10, not yet discharged);
- physiological residue — breath not yet settled, voice still rough, eyes still rimmed;
- where the gaze rests and which way the body faces;
- the echo of the previous unit's last line: this unit's first reaction must answer it — listener response, rebuttal, or silence.

Spend the first 1–2 seconds of the unit on that residue before the new objective begins. This is a state, not a recap: do not restate the previous unit's action in prose.

## 8. Camera and acting coordination

- **Eyeline match.** In shot-reverse-shot, if A looks screen-left, B must look screen-right, and this must hold across every cut. When a character looks at an off-screen partner, state screen-left or screen-right and high or low.
- **No lens contact.** Unless the user asks for it (monologue, breaking the fourth wall, direct address), the character does not look into the lens.
- **Edit handles.** Every dialogue shot keeps 0.3–0.5 s of preparation before the first word and 0.5 s of reaction after the last, so an editor can find the cut.
- **Framing versus amplitude.** A close-up carries one micro change. A medium shot can carry gaze plus body. A wide shot must work through blocking and posture — facial detail that the framing cannot resolve must not be written.

## 9. Likely AI mis-performance bans

Select the 2–4 that this beat would most plausibly produce, and exclude them beside the affected line. Never paste the whole list.

- permanent smiling, or a smile attached to every line;
- over-acting, every emotion rendered as a large facial event;
- dead eyes while speaking, no fixed target, or unprovoked lens contact;
- lip-sync drift, or speaking with the mouth closed;
- several emotions smeared into one vague "faintly sad" face with no readable change;
- every line at the same pitch and the same speed — recital;
- two characters alternating at an even pace with no reaction and no pickup rhythm;
- crying that produces tears without any change in breath or voice;
- anger expressed only as shouting, with no compression or build;
- hair and clothing drifting with no wind;
- the body freezing completely while speaking, or hands fidgeting nonstop.

## 10. Pre-delivery scene-acting audit

- [ ] Every line has a speaker, an action verb, a listener reaction, and a pickup type.
- [ ] Every emotional or tactical turn has a trigger and a visible moment of realization.
- [ ] Status is clear; if it flips, the flip lands on a specific line or action.
- [ ] Blocking, if used, corresponds to a relationship change and is visible in the framing.
- [ ] One main stress per line; every psychological pause states its position and what the face does.
- [ ] Every time window passes the speech-rate check in `MINIMAX_H3_TIMING_ENGINEERING.md` and leaves reaction time.
- [ ] Performance scale matches the genre register.
- [ ] Multi-unit scenes inherit the previous unit's emotional current state.
- [ ] Eyelines are consistent across cuts; no lens contact unless requested.
- [ ] The restriction list names this beat's 2–4 most likely mis-performances.
