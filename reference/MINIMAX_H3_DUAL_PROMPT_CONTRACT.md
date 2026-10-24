# MiniMax H3 中英双版提示词契约 (Dual-Prompt Contract)

本契约约束 MiniMax H3 单元的提示词交付形态：**中英双版**。

**交付标准 = 两个可直接粘贴的提示词块**：

1. **中文版 (Chinese Prompt)**：对齐底层模型能力的中文六段式，含 `<主体 N>`、任务摘要、保留分析、`<镜头 N>` 与 `<d>` 台词容器，供国内模型直投生成；
2. **英文版 (English Prompt)**：官方标准英文六段式，供官方／国际通道精准生成。

两个版本均非随意翻译，而是从**同一个单元真相账本（One Approved Unit Truth）**编译出的两种语言形态。

**分镜视图 (Storyboard View) 不是第三种提示词模态。** 它是工单里给人读的审阅层：纯中文自然语言，禁止机器标签，不可直接粘贴给模型。它必须与双版同源同事实，但不参与双版 parity 的硬校验。

> 早期版本曾把审阅层称作「三模态」之一。现按上游参考规范收敛为**中英双版**，审阅层降为展示层——对外只承诺两版提示词。

---

## 1. 核心铁律：单核多序列化 (One Truth, Multiple Serializations)

在动笔撰写任何版本之前，必须首先确立该单元的底层事实账本：
`CLIP_TRUTH_LEDGER`、`OPENING_STATE`、`SHOT_SCORE`、时间轴毫秒切点、对白台词原文、音响设计与结束定格（`exit_state`）。

中文版与英文版必须在以下物理事实和戏剧因果上**绝对对称（100% Parity）**：
- 单元编号（Unit ID）、目标时长、场景、天气与光照；
- 登场角色身份、服装款式、左右站位与道具状态；
- 镜头总数量、镜头顺序、起止切点时间、景别、运镜位移与最终定格帧；
- 说话人身份、台词原文内容与标点符号（字节级相同）；
- 环境底噪、物理碰撞拟音与配乐决策（`无配乐。` 严格对应 `non_diegetic_music: N/A`）。

---

## 2. 分镜视图：中文审阅层 (Storyboard View, review-only)

供导演、编剧、演员、制片对戏与审稿使用。保持五段式自然语言规范，杜绝一切机器噪音：

```text
中文分镜视图｜H3-XXX｜N秒

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

- **严禁包含机器标签**：不出现 `<Subject N>`、`<Picture N>`、`(S1)`、`<d>` 或英文六段式字段名，也不夹带英文短语；
- **台词呈现**：采用「冒号 + 换行孤行」输出纯净台词；
- **唯一例外**：在 `角色与场景：` 中保留一行紧凑纯中文的 `<Audio N>` 槽位说明，并在说话人处以自然语言引用；
- **不可直接用于生成**：这一层是给人看的，粘贴给模型会因缺少主体绑定与保留策略而退化。工单中须标注「仅供审阅」。

---

## 3. 中文版 (Chinese Prompt)

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

## 4. 英文版 (English Prompt)

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

## 5. 双版一致性与视图同源审查 (Pair-Parity & View-Consistency Audit)

交付前，校验工具将执行全量一致性审查：

1. **镜头数量与时钟切点必须 1:1 绝对重合**；
2. **台词原文在双版中字节级 100% 相同**；
3. **主体编号 `<主体 N>` 与英文版 `<Subject N>` 语义完全一致**；
4. **配乐决策严格一致**；
5. **分镜视图若存在**，其镜头数、切点、台词与配乐必须与双版一致；不一致时以双版为准并修正视图。视图缺失不构成交付缺陷，视图与双版矛盾则构成缺陷。

---

## 6. 必含项与写法细则 (Mandatory Elements)

前五节管「双版怎么对齐」；本节管「每一版里必须写进去、否则必然翻车的几件事」。**这些不是可选优化项**，缺一项就是交付缺陷。

### 6.1 取脸来源声明（双版都必含）

角色设定图采用「左侧面部特写 + 正面全身平涂遮脸」版式，因此提示词必须显式声明取脸来源，否则模型可能从被涂灰的正面视图「补」出一张脸，或把人物理解成戴面罩的人。

- 中文版：写在 `<主体 N>` 定义行内，`人物外观只取自角色设定图左侧的面部特写，正面全身视图的面部已作遮罩，不得据此还原五官。`
- 英文版：`<Subject N> is the four-view character sheet; take facial identity only from the left-hand facial close-up. The front body view's face is masked — do not reconstruct features from it.`
- 分镜视图（自然语言）：`人物外观只取自角色设定图左侧的面部特写，正面全身视图的面部已作遮罩，不得据此还原五官。`

配套的 `retention_analysis` / `保留分析` 仍标 `fully_preserved`（整张四视图作为一个主体），但取脸来源必须在定义行说清。

### 6.2 开场镜头声明（双版都必含）

在 `任务摘要` / `summary` 中写明本单元**第一个镜头拍的是谁**，以及开场直接呈现谁。

- 中文版：`本段第一个镜头是<Sx>的镜头，开场直接是<Sx>的画面。`
- 英文版：`The first shot of this unit belongs to <Subject N>; the clip opens directly on <Subject N>.`

作用：防止生成结果用空镜、环境镜头或错误角色起幅。尤其是多人正反打单元，开场错人等于整段作废。

### 6.3 调色与场景锁定句（双版都必含）

参考场景图一旦上传，模型倾向于把画面「美化」成干净高对比的商业调色，并顺手重新设计场景。必须在全局视觉锁定里加一句锁定：

- 中文：`画面的调色、雾感与颗粒以场景图为准，不得画成干净、高对比的普通商业调色，不得重新设计场景陈设。`
- 英文：`Grading, haze and grain follow the supplied scene plate. Do not normalise it into a clean high-contrast commercial grade, and do not redesign the set.`

### 6.4 左右禁令（双版都必含）

正反打单元必须把「人物不得互换画面左右」写进禁止项。这是镜像错误里最高频、最难事后发现的一种——单独看每一帧都正常，剪起来才发现两人位置反了。

- 中文：`人物不得互换画面左右位置。`
- 英文：`Characters must not swap screen-left and screen-right positions.`

### 6.5 中文版的微表情写法

**仅适用于中文版。分镜视图严禁任何英文短语与机器标签，不要混用。**

中文版里，微表情写成「中文描述（英文原文控制短语）」：

```text
她轻微眯眼（narrows the eyes slightly），下颌缓慢放松（the jaw slowly relaxes）。
```

并在全局视觉锁定处注明一次：`括号内英文为微表情控制短语，与中文同义。`

好处：中文读者可读，同时保留模型侧精确匹配的控制短语，避免中文转述在语义上漂移。

### 6.6 数字与易误读台词的读法

台词原文**一个字都不能改**。数字、缩写、多音字、英文混读等容易被念错的写法，在声音段说明读法，不写进台词本体。

- 中文版：写在 `环境音响：` 段内，例如 `「28」读作「二十八」。`
- 英文版：写在 `overall_soundscape:` 内，例如 `The numeral "28" is read aloud as "er shi ba" in Mandarin.`
- 分镜视图：写在 `声音：` 段内，同义表述。

### 6.7 交付与试跑建议

交付时除双版提示词外，必须一并写明：

- **总生成时长**与**预计成片时长**（两者不是一回事，后者含剪辑损耗）；
- **每个单元上传的参考图编号**（与上传清单一致，不写文件名）；
- **先试跑一两段的建议**，并说明这几段要重点看什么（例：脸是否漂、口型是否对上、场景是否被重新设计）。效果确认后再批量生成，避免一次性消耗全部额度。

---

## 7. 双版语言分工 (Language Division)

双版不是互译关系，是同一事实的两种语言序列化。以下分工必须逐条执行。

### 7.1 中文版

- 说明文字、镜头描述、表演指令：**全部中文**；
- 台词：**中文原文**，包在 `<d>[中文] … </d>`；
- 标签拼写：`<主体 N>`、`<图片 N>`、`<音频 N>`、`<d>`、`(S1)` 按规范原样，不译不改；
- 微表情：按 6.5 写「中文（英文控制短语）」。

### 7.2 英文版

- 说明文字、镜头描述、表演指令：**必须全部译成英文**，不得保留中文散文；
- 台词：**保留中文原文不翻译**，写成 `<Subject N> (SN): <d>[Chinese] 原文</d>`；
- 声音标签：拼写原样（`<pause>`、`<whisper>` 等），不译；
- 微表情：直接用英文控制短语，不再加中文括号；
- 数字读法：写在 `overall_soundscape:` 内；
- **美学提示词保留中文原文**，不译成英文——它是与出图侧共用的锁定串，翻译会破坏两侧一致性。

### 7.3 分镜视图

- 全部中文自然语言；
- 无标签、无英文短语、无六段式字段名；
- 台词同样逐字保留原文。

### 7.4 三处必须保持原样，永不翻译

1. **台词原文**（含标点）——双版都是原文，只有语言标记不同；
2. **标签拼写**——`<Subject N>` / `<主体 N>` / `<d>` / `(S1)` / 声音标签；
3. **美学提示词**——中文原文原样嵌入英文版，它是跨资产复用的锁定串。

翻译这三样中的任何一样，都会导致双版漂移或资产生成不一致。

---

## 8. 输出格式硬规则 (Format Hard Rules)

以下规则不分平台、不分环境、不分智能体，**每一次输出都适用**。它们防的不是创意问题，是"交付物看起来对、实际不可用"。

### 8.1 一个代码块，块外不写东西

每个提示词必须装在**一个**围栏代码块里（` ```text `）。块内除提示词本身不写任何东西；块外不写前言、总结、说明或第二备选——除非用户明确要求解释。

工单 HTML 中，可复制的提示词块必须是独立的 `<pre class="prompt-block">` 容器，与说明文字物理分离，确保"复制"按钮拿到的就是纯提示词。

### 8.2 六段标题的格式禁令

六个顶层字段必须以**精确小写、原样拼写、独立成行、行尾带冒号**的形式出现，顺序固定：

```text
subject_definitions:
summary:
retention_analysis:
detailed_description:
overall_soundscape:
non_diegetic_music:
```

**禁止**：翻译标题、改名、加编号（`1.`）、加粗（`**summary:**`）、包进 Markdown 表格、转成无序列表、写成标题层级（`# summary`）。中文版的六个字段同理。

标题被格式破坏后，模型会把它们当成正文，主体绑定与保留策略全部失效。

### 8.3 空段落必须写显式声明

任何一个字段没有内容要写时，**写一句简短的显式声明，不能留空，也不能整段删除**。

- `non_diegetic_music: N/A` / `非剧情音乐：无配乐。`
- `overall_soundscape: quiet room tone, no added effects.` / `环境音响：仅有室内底噪，无额外音效。`

留空会让模型自行发挥，删除会让字段缺失、linter 直接判不合格。

### 8.4 不加前言、解释、第二备选

提示词正文里不出现：开场铺垫语、目的说明、创作思路、"以下是…"、备选方案 A/B、对操作员的提示。这些放在工单的说明区，不放在可复制提示词里。

一个单元只交付一套确定的选择，不交付"也可以这样"。

### 8.5 不得发明平台参数

**绝不编造**模型不支持的分辨率、帧率、时长上限、采样参数、API 字段或平台开关。

- 需要平台上限时，查 [MINIMAX_H3_PLATFORM_LIMITS.md](MINIMAX_H3_PLATFORM_LIMITS.md) 或项目已确认的规格；
- 规格未知就不写，不要用"看起来合理"的数值填充；
- 用户未指定画幅时，除剧本已声明外，不擅自写死画幅。

编造参数比留空更危险：它会让操作员以为该设置可用，实际在平台上无法执行。

### 8.6 防题材偏见清单

不得因为题材未明确就默认套用以下任何一类：日式设定、冬季场景、恋爱氛围、祈祷/宗教意象、超写实照片质感、音乐录影带式剪辑。

默认值必须来自剧本、用户指令或项目已批准的风格块。剧本没写的，按人物与情境做最少假设，并在 `retention_analysis` 里标明这是推断。

### 8.7 风格参考与连续性锁定的固定模板

当上传图只作视觉风格参考时，英文版必须使用以下定义（把 `<Subject N>` 换成实际编号）：

```text
<Subject N> is reference image N used solely as a visual-style reference. Transfer only its artistic direction, cinematography, lens character, color palette, saturation, color-temperature relationship, exposure, contrast, lighting logic, material rendering, depth of field, bokeh texture, grain, highlight roll-off, shadow density, atmospheric perspective, and overall mood. Do not transfer any recognizable people, faces, hairstyle, wardrobe, objects, architecture, text, composition, camera angle, pose, or action from <Subject N>.
```

并在 `detailed_description` 开头加连续性锁定：

```text
All shots must continuously retain <Subject N>'s overall color system, color-temperature relationship, luminance distribution, contrast, key-light direction, light softness, environmental bounce logic, material detail, focal-length feel, depth-of-field relationship, bokeh behavior, grain scale, highlight roll-off, shadow density, atmospheric perspective, and artistic mood. Cuts must not cause a jump in grading, lighting ratio, skin tone, sharpness, grain, bokeh, or lens texture.
```

中文版用同义自然语言表述，语义必须与英文版逐项对应；不得因为"中文不好写"就省略其中的技术维度。

风格参考是可选项。没有风格参考时，按用户书面风格指令或项目已批准的风格块执行，从内容参考中推导克制的连续性约束，不发明题材化方向。
