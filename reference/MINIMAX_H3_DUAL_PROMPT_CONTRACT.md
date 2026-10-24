# MiniMax H3 多模态提示词契约 (Dual & Tri-Modal Prompt Contract)

本契约用于约束 MiniMax H3 生成的提示词工单。为解决“国内用户直接使用中文提示词生成时缺乏强主体与保留控制”的痛点，支持**三模态（Tri-Modal）独立序列化体系**：

1. **中文审稿版 (Chinese Director Storyboard)**：专供导演、编剧、演员、制片对戏与审稿的纯自然语言故事板；
2. **中文生成机读版 (Chinese Machine-Aligned Six-Section Prompt) [NEW]**：对齐底层大模型能力的结构化六段式，包含 `<主体 N>`、任务摘要、保留分析与 `<d>` 台词容器，专供直接复制生成；
3. **英文执行版 (English Six-Section Full-Reference Prompt)**：官方标准英文机读六段式，用于底层精准 Attention 路由。

所有的提示词版本均非随意翻译，而是从**同一个单元真相账本（One Approved Unit Truth）编译出的三种不同形态**。

---

## 1. 核心铁律：单核多序列化 (One Truth, Multiple Serializations)

在动笔撰写任何版本的提示词之前，必须首先确立该单元的底层事实账本：
`CLIP_TRUTH_LEDGER`、`OPENING_STATE`、`SHOT_SCORE`、时间轴毫秒切点、对白台词原文、音响设计与结束定格（`exit_state`）。

无论输出两版还是三版，各版本之间必须在以下物理事实和戏剧因果上**绝对对称（100% Parity）**：
- 单元编号（Unit ID）、目标时长、场景、天气与光照；
- 登场角色身份、服装款式、左右站位与道具状态；
- 镜头总数量、镜头顺序、起止切点时间、景别、运镜位移与最终定格帧；
- 说话人身份、台词原文内容与标点符号（字字节级相同）；
- 环境底噪、物理碰撞拟音与配乐决策（`无配乐。` 严格对应 `non_diegetic_music: N/A`）。

---

## 2. 模态一：中文审稿版 (Human Storyboard)

保持五段式自然语言规范，杜绝一切机器噪音：

```text
中文审稿版｜H3-XXX｜N秒

角色与场景：
...

镜头设计：
【镜头1｜0.0—2.0秒】
...

声音：
...

音乐：
...
```

- **严禁包含机器标签**：不出现 `<Subject N>`、`<Picture N>`、`(S1)`、`<d>` 或英文六段式字段名；
- **台词呈现**：采用“冒号 + 换行孤行”输出纯净台词；
- **唯一例外**：在 `角色与场景：` 中保留一行紧凑纯中文的 `<Audio N>` 槽位说明，并在说话人处以自然语言引用。

---

## 3. 模态二：中文生成机读版 (Machine-Aligned Chinese Prompt)

详见 [`MINIMAX_H3_CHINESE_MACHINE_PROMPT_SPEC.md`](MINIMAX_H3_CHINESE_MACHINE_PROMPT_SPEC.md)。严格执行中文六段式结构：

```text
主体定义：
<主体 1>：...
<图片 1>：...
<音频 1>：...

任务摘要：
[参考生成] ...

保留分析：
<主体 1>：reference, 继承五官服装，排除原背景...

镜头详述：
[镜头 1] 0.0—3.5秒。中景正打...
[镜头 2] 00:03.500 起。(S2) 说：
<d>[中文]台词原文</d>

环境音响：
...

非剧情音乐：
无配乐。
```

- **三大控制力**：
  1. 显式主体槽位绑定（`<主体 N>`）；
  2. 显式保留与排除策略（`reference`、`weak_reference` 等）；
  3. 专用口型容器（`<d>[中文] ... </d>`）与发音人编号（`(S1)`）。

---

## 4. 模态三：英文执行版 (English Six-Section Block)

详见 [`MINIMAX_H3_FULL_REFERENCE_EN.md`](MINIMAX_H3_FULL_REFERENCE_EN.md)。维持官方标准英文六段式：

```text
subject_definitions:
<Subject 1>: ...

summary:
[reference generation] ...

retention_analysis:
<Subject 1>: reference, ...

detailed_description:
[Shot 1] ...
[Shot 2] At 00:03.500, ...
<d>[Chinese]台词原文</d>

overall_soundscape:
...

non_diegetic_music:
N/A
```

---

## 5. 多模态一致性与防退化审查 (Pair & Tri-Parity Audit)

交付前，校验工具将执行全量一致性审查：
1. **镜头数量与时钟切点必须 1:1 绝对重合**；
2. **台词原文在所有版本中字号标点 100% 相同**；
3. **主体编号 `<主体 N>` 与英文版 `<Subject N>` 语义完全一致**；
4. **配乐决策严格一致**。

---

## 6. 必含项与写法细则 (Mandatory Elements)

前五节管"三版怎么对齐"；本节管"每一版里必须写进去、否则必然翻车的几件事"。**这些不是可选优化项**，缺一项就是交付缺陷。

### 6.1 取脸来源声明（三模态都必含）

角色设定图采用「左侧面部特写 + 正面全身平涂遮脸」版式，因此提示词必须显式声明取脸来源，否则模型可能从被涂灰的正面视图"补"出一张脸，或把人物理解成戴面罩的人。

- 中文审稿版（自然语言）：`人物外观只取自角色设定图左侧的面部特写，正面全身视图的面部已作遮罩，不得据此还原五官。`
- 中文机读版：写在 `<主体 N>` 定义行内，同义表述。
- 英文版：`<Subject N> is the four-view character sheet; take facial identity only from the left-hand facial close-up. The front body view's face is masked — do not reconstruct features from it.`

配套的 `retention_analysis` / `保留分析` 仍标 `fully_preserved`（整张四视图作为一个主体），但取脸来源必须在定义行说清。

### 6.2 开场镜头声明（机读版与英文版必含）

在 `任务摘要` / `summary` 中写明本单元**第一个镜头拍的是谁**，以及开场直接呈现谁。

- 中文机读版：`本段第一个镜头是<Sx>的镜头，开场直接是<Sx>的画面。`
- 英文版：`The first shot of this unit belongs to <Subject N>; the clip opens directly on <Subject N>.`

作用：防止生成结果用空镜、环境镜头或错误角色起幅。尤其是多人正反打单元，开场错人等于整段作废。

### 6.3 调色与场景锁定句（三模态都必含）

参考场景图一旦上传，模型倾向于把画面"美化"成干净高对比的商业调色，并顺手重新设计场景。必须在全局视觉锁定里加一句锁定：

- 中文：`画面的调色、雾感与颗粒以场景图为准，不得画成干净、高对比的普通商业调色，不得重新设计场景陈设。`
- 英文：`Grading, haze and grain follow the supplied scene plate. Do not normalise it into a clean high-contrast commercial grade, and do not redesign the set.`

### 6.4 左右禁令（三模态都必含）

正反打单元必须把"人物不得互换画面左右"写进禁止项。这是镜像错误里最高频、最难事后发现的一种——单独看每一帧都正常，剪起来才发现两人位置反了。

- 中文：`人物不得互换画面左右位置。`
- 英文：`Characters must not swap screen-left and screen-right positions.`

### 6.5 中文机读版的微表情写法

**仅适用于模态二（中文生成机读版）。模态一中文审稿版严禁任何英文短语与机器标签，不要混用。**

中文机读版里，微表情写成「中文描述（英文原文控制短语）」：

```text
她轻微眯眼（narrows the eyes slightly），下颌缓慢放松（the jaw slowly relaxes）。
```

并在全局视觉锁定处注明一次：`括号内英文为微表情控制短语，与中文同义。`

好处：中文读者可读，同时保留模型侧精确匹配的控制短语，避免中文转述在语义上漂移。

### 6.6 数字与易误读台词的读法

台词原文**一个字都不能改**。数字、缩写、多音字、英文混读等容易被念错的写法，在声音段说明读法，不写进台词本体。

- 中文机读版：写在 `环境音响：` 段内，例如 `“28”读作“二十八”。`
- 英文版：写在 `overall_soundscape:` 内，例如 `The numeral “28” is read aloud as “er shi ba” in Mandarin.`
- 中文审稿版：写在 `声音：` 段内，同义表述。

### 6.7 交付与试跑建议

交付时除三版提示词外，必须一并写明：

- **总生成时长**与**预计成片时长**（两者不是一回事，后者含剪辑损耗）；
- **每个单元上传的参考图编号**（与上传清单一致，不写文件名）；
- **先试跑一两段的建议**，并说明这几段要重点看什么（例：脸是否漂、口型是否对上、场景是否被重新设计）。效果确认后再批量生成，避免一次性消耗全部额度。
