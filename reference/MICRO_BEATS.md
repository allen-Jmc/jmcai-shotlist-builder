# Micro-Beats — Actor Performance Catalog

**Never leave a generic emotion in a prompt.** Every emotional direction must decompose into specific muscle movements, breath, eyes, and skin. This is the single biggest difference between a Seedance prompt that produces "AI video" and one that produces a performance.

## 1. The base rule

When the user (or the script) says "the character looks [generic emotion]" — stop. Decompose it. If you can't decompose it confidently, ask the user to choose a variant.

Example of the clarification you should offer when the user writes "surprised":

> *Which kind of surprise?*
> *(a) Light positive surprise — eyebrows lift, lips slightly part, pupils dilate for 0.3 sec, soft inhale through nose. No extra movement.*
> *(b) Shock surprise — sharp inhale through mouth, eyes wide, freezes in place, hand involuntarily lifts to chest.*
> *(c) Disbelief surprise — slow blink, head tilts slightly, lips press together, only one eyebrow lifts.*
> *(d) Surprise-with-joy — eyes light up (catchlight), smile builds gradually, shoulders relax.*
> *Which one fits?*

Same approach for "tense", "sad", "angry", "scared", "thoughtful", "in love" — every general adjective has 3–5 distinct physical realizations.

## 2. Catalog by emotion

### Anger / determination / rage

```
- 颊部咬肌（masseter）通过皮肤可见地搏动
- 颈部颈动脉脉搏可见
- 太阳穴血管浮起
- 鼻翼在重音词上扩张
- 瞳孔收缩（focus tightening）
- 眼角外缘收紧（genuine intensity，非廉价眯眼）
- 高潮时刻不眨眼
- 眉骨/鼻翼处微汗珠
```

### Anxiety / nervousness

```
- 一次喉结上下吞咽（visible swallow）
- 台词前一次短促浅吸气（短促鼻吸）
- 用舌头舔润干燥的下唇
- 下唇轻微内收
- 脸颊毛细血管充血泛红
- 关键词上瞳孔扩张
- ⚠️除非明确说明，否则不哭
```

### Sadness / vulnerability (without tears)

```
- 眼角外缘下垂
- 眼睛湿润带眼神光（wet with catchlight）——但⚠️不流、不淌、不闪烁泪光
- 眉头中央皱起（corrugator muscle）
- 嘴唇轻微颤抖
- 头部微微低垂
```

### Control / calm / superiority

```
- 平稳均匀的呼吸（与紧张的对手形成对比）
- 手指/手臂放松
- 缓慢均匀的眨眼（slow blink）
- 下颌微抬（chin lift）
- Duchenne微笑——眼角外侧出现细纹。⚠️逐渐建立，不是从已完成的状态开始
```

### Heaviness / weighed-down

```
- 双肩下沉（heavy shoulders）
- 头部微微下垂
- 深而缓慢的呼吸
- 声音比平时更低沉、更闷
- 回答时头部轻微侧倾（5–15°）
```

### Shock / freeze

```
- 镜头开始瞬间——身体冻结0.3-0.5秒，无任何移动
- 瞳孔在冻结瞬间扩张
- 嘴唇微微张开（lips part）但无声
- 一次延迟的、急促的鼻吸气在freeze结束后
- 眼睛锁定在触发源上——无眨眼、无视线偏移
```

### Suppressed emotion (the hardest — physical resistance)

```
- 他在试图忍住——每一块面部肌肉都在对抗涌上来的情绪
- 颧骨处咬肌慢慢收缩
- 喉结一次延迟的、用力的吞咽
- 眼睛逐渐湿润，眼眶积聚泪水使眼球开始泛光——但泪不落下
- 一次缓慢、深、控制的吸气——胸腔可见起伏
- 下颌微抖一次——立刻被收紧
```

### Surprise variants

**Light positive:**
```
- 眉毛轻微上扬
- 嘴唇微张
- 瞳孔扩张约0.3秒
- 一次柔和的鼻吸气
- 无其他多余动作
```

**Shock:**
```
- 急促的口吸气（sharp mouth inhale）
- 双眼睁大，瞳孔扩张
- 身体冻结在原地
- 一只手不自主抬至胸前
- 嘴唇微微张开但无声
```

**Disbelief:**
```
- 一次缓慢的眨眼
- 头部微微侧倾
- 嘴唇收紧
- 只有一侧眉毛抬起
- 视线锁定在触发源上
```

**Surprise + joy:**
```
- 眼睛点亮（catchlight强化）
- 笑容逐步建立——⚠️不是瞬间出现的完整笑容
- 双肩放松下沉
- 一次轻松的呼气
```

## 3. Emotional arc within a single shot

When emotion changes inside one continuous take, write it as a numbered sequence of beats with explicit muscle/breath/eye changes per beat:

```
①开始——[emotion A]——[specific muscular indicators]
②过渡——[trigger event]——[which muscles release / tense]
③下一阶段——[emotion B]——[new indicators]
④...
⑦结尾——[final emotion]——[final indicators]
```

Also state explicitly **what must remain visible on the face** through the arc (eyebrows, jaw, breath, eyes).

Tie each numbered beat to a corresponding camera phase (see CAMERA_EMOTION.md §2).

## 4. Dialogue and timing

Every spoken line gets:
- **Pre-line beat** (what happens before the first word): swallow, inhale, lip lick, posture shift
- **During the line**: which words are emphasized via nostrils, intonation, pupils
- **Post-line beat**: ~0.5 sec held breath before the next movement, then release

Example:
```
台词前：一次短促鼻吸气，喉结一次吞咽。
台词："Don't ask me again."——重音落在"again"，鼻翼在该词上扩张。
台词后：保持视线锁定在对手身上0.5秒——然后微微移开。
```

## 5. Listeners in bokeh

If the focal character is in focus and others are blurred — **they are not static**. Write:
- Where their head and gaze are pointed
- Micro-movements of shoulders and head
- Reaction to key moments (even in bokeh)
- Clear timing offset (e.g., "Roko turns his head first; 0.4 sec later, Rein; another 0.4 sec, Jax")

Three characters never sync perfectly — always stagger by 0.3–0.5 sec.

## 6. Forbidden in performance

- ❌ "Just stands there talking" — there is always a micro-movement
- ❌ Cartoony grimaces / over-mugging
- ❌ "Eyes to the ceiling" for thinking — name a specific gaze direction
- ❌ Tears by default — only if the script explicitly calls for them
- ❌ Perfect synchronization across multiple characters — always stagger timing
- ❌ Generic "looks tense" / "looks happy" — always decompose into muscles, breath, eyes

## 7. The anti-AI test

Before delivering any prompt, read the performance section and ask:
> *Could this come from an AI prompt template? Or does it read like notes from a director who watched the actor rehearse?*

If it reads templated, rewrite. The micro-beats should feel like they came from a specific performance, not a checklist.
