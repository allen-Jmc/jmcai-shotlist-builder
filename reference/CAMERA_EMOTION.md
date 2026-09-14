# Camera–Emotion Sync

The camera can become the emotional double of the focal character, but emotion is not a mechanical lookup table. Choose movement, lens, and duration from dramatic purpose, point of view, spatial pressure, action, and what the audience must learn. The mappings below are candidate expressions, not compulsory formulas. For MiniMax H3, `MINIMAX_H3_DIRECTORIAL_NATURAL_LANGUAGE.md` overrides any template here: rage may be static, panic may use controlled tracking, grief may remain wide, and no ending automatically requires a top-shot freeze.

## 1. Candidate movement-to-emotion vocabulary

| Focal character emotion | Camera type | How to write it in Chinese |
|---|---|---|
| **Anger / rage / tension / on edge** | Handheld breathing, **jittery, unstable** — broken breath rhythm, visible vertical/horizontal twitches. Small amplitude, irregular rhythm. | `摄影机不安、紧张——画面有较明显的呼吸式漂移、上下微抖、左右轻摆。手持摄影，画面带有不规则的呼吸节奏。禁稳定器。` |
| **Calm / control / confidence** | Handheld breathing, **smooth** — steady breath, regular micro-amplitude. | `摄影机平稳、流畅、克制——只剩下极细微的、规律的呼吸式微动。手持摄影但呼吸感极微。禁稳定器。` |
| **Sadness / vulnerability** | Handheld, **slow, low** — lower breath frequency, slight downward camera drift. | `摄影机缓慢、低位手持——呼吸节奏放慢，画面有极轻微的下沉感。` |
| **Shock / revelation** | Static + slow push-in or pull-out — sharp freeze at start, then very slow movement. | `镜头开始严格静止——0.5秒后开始极缓慢推进/拉远（push-in/pull-out），整段移动距离不超过15厘米。` |
| **Action** | 60fps, 180° shutter — clear motion, motion blur within shutter range only. | `60fps流畅运动，180°快门运动模糊，禁止超出快门范围的拖影。` |
| **Final beat / verdict, when explicitly motivated** | A brief top-shot freeze can create formal judgment, but it is one option among stable holds, negative space, reactions, or action residue. | `仅当俯拍本身承担审判、命运或空间揭示功能时，使用短暂正上方停顿；否则选择与本场落点一致的稳定画面。` |

## 2. Emotional arcs within a single shot

If emotion **changes** across one continuous take (e.g., Roko goes from rage → controlled), the camera changes synchronously. Write it explicitly in phases:

```
⚠️镜头开始（步骤①②阶段，Roko怒气）：摄影机⚠️明显手持、不安、紧张——画面有明显的呼吸式漂移、上下微抖、左右轻摆。

⚠️随Roko情绪逐步缓和（步骤③④⑤）：摄影机的不安⚠️逐渐减弱——呼吸式漂移幅度变小，左右晃动减少，画面开始稳定。

⚠️镜头结尾（步骤⑥⑦，Roko稳定）：摄影机⚠️变得平稳、流畅、克制——只剩下极细微的、规律的呼吸式微动。
```

Tie each camera phase to a numbered acting beat (① ② ③ ...) so the model knows when in the take to transition.

## 3. Lens selection

| Use | Lens | Aperture |
|---|---|---|
| Extreme tight emotional close-up (forehead-to-chin fills frame) | **85mm** or **100mm** | F1.4 |
| Mid dialogue, two-shot | **50mm** | F2.0 – F2.8 |
| Wide / establishing | **35mm** | F4 – F5.6 |
| Insert / detail of object | **50mm** or **85mm** with focus lock on object | F1.4 |
| Macro (pores, droplets, fabric) | **45mm macro** | F2.8 |

**Forbid optical distortion** in every prompt that uses a wide or fast lens:
```
禁桶形畸变、禁枕形畸变、禁鱼眼效果、禁广角变形，画面线条必须笔直，构图平整。
```

**Bokeh / shallow DOF** for tight inserts and emotional close-ups — use F1.4 and lock focus:
```
⚠️焦平面严格锁定在 [object/character] 上——绝对禁止焦点漂移、绝对禁止 rack focus、绝对禁止 autofocus 跳变。
```

## 4. Dolly / track moves

For very slow dolly (insert / device close-up), specify **exact distance and time**:
```
整个7秒内摄影机后移总距离仅约10-15厘米。速度慢到几乎察觉不到。禁zoom变焦，禁突然推拉。
```

Never write `zoom`. Always write physical camera movement (`dolly`, `track`, `crane`, `push-in`, `pull-out`).

## 5. Seedance planning examples and H3 exceptions

| Shot type | Duration |
|---|---|
| Hard cut intro / flash establishing (split-second wide) | **0.3 – 0.5 sec** (a fraction of a second, NOT 1 second) |
| One dialogue line, mid-length | **3 – 7 sec** |
| Reaction without words (with emotional arc) | **5 – 10 sec** |
| Insert / wide / freeze | **0.3 – 2 sec** |
| Emotional close-up with full arc (5–7 numbered beats) | **8 – 15 sec** |

The table is a Seedance-oriented planning library, not an H3 compliance gate. H3 dialogue-led narrative units normally use 10–15 seconds and the density guidance in `MINIMAX_H3_LONG_SCRIPT_UNITS.md`, while allowing a motivated continuous take or a necessary 0.5–2.5-second insert inside a multi-shot unit. Never create a cut solely to satisfy this table.

## 6. Seedance pattern vocabulary — adapt, do not copy into H3

### 6.1 Extreme tight close-up of dialogue (85mm, F1.4)

```
机位：⚠️85mm（或100mm）长焦，⚠️F1.4极浅景深，⚠️[Character]⚠️严格的极致大特写（strictly extreme tight close-up）——构图严格"额头到下巴填满画幅"，[Character]的脸⚠️必须占据画面绝大部分。
⚠️⚠️⚠️摄影机⚠️严格手持，全程明显的呼吸式漂移和微动——⚠️真实摄影师贴身跟拍的呼吸感、心跳感。⚠️摄影机⚠️主动跟随[Character]的脸部运动——头部任何细微的转动、抬起、下沉、目光移动，摄影机都微微跟随调整构图。
摄影机位置：[east/west/south/north of character].
背景：⚠️完全虚化为模糊色块和柔光斑——所有细节都强烈散焦。
动作：[step-by-step micro-beats].
⚠️⚠️⚠️微表演细节（actor performance micro-beats）：
- ...
```

### 6.2 Insert on prop (focus-locked)

```
机位：50mm/85mm 大光圈定焦，⚠️F1.4极浅景深，⚠️焦平面从镜头第1帧到最后1帧严格锁定在[object]上——绝对禁止焦点漂移、rack focus、autofocus跳变。
⚠️清晰度规则：画面中⚠️只有[object]绝对清晰锐利，所有其他元素强烈散焦虚化为模糊色块和柔光斑（heavy bokeh）——背景永远模糊。
摄影机[angle].⚠️⚠️⚠️dolly out运动幅度极小：整个X秒内总位移仅约10-15厘米——速度慢到几乎察觉不到。禁zoom，禁突然推拉。
```

### 6.3 Wide / establishing flash (split-second)

```
机位：35mm广角，全景/远景（wide shot / establishing shot）。⚠️持续时间⚠️严格约0.3-0.5秒（split-second flash establishing shot——只是瞬间空间定位的闪现，不是完整构图镜头）。整体空间构图——[positions of all key elements].
动作：[moment]——⚠️0.3-0.5秒后⚠️立刻硬切（hard cut）到镜头2——无过渡、无淡出、无停留。
```

### 6.4 Optional top-shot freeze finale — only with explicit dramatic reason

```
【镜头 N (last)】
机位：严格正上方俯拍（top-shot）。0.3-0.5秒freeze frame。
背景：严格匹配[location].
动作：所有人物位置冻结。时间静止。
```

## 7. Forbidden moves

- `禁zoom变焦` — physical camera movement only
- `禁稳定器` (no stabilizer) — handheld means handheld breathing must be visible
- `禁抖动（除手持呼吸感）` — no shake outside of intentional handheld breathing
- `禁过度运动` — don't oversell the camera move; if the script is intimate, the camera is intimate
