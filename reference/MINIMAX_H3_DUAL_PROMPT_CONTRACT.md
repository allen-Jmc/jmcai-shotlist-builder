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
