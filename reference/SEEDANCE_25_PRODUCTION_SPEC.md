# 字节跳动 Seedance 2.5 / 2.0 官方生产规约 (ByteDance Production Spec)

本规约作为 `jmcai-shotlist-builder-beta` 的字节跳动（即梦 Dreamina / 剪映小云雀）视频大模型专项指导层。Seedance 是目前业界**唯一具备单次生成输出多机位蒙太奇（Multi-shot in ONE generation）能力的顶级模型**。2.5 版本更带来了原生 30 秒长叙事与 50 槽位多模态资产支持。

---

## 一、 Seedance 2.5 核心规格与硬性限制

| 参数维度 | Seedance 2.0 规格 | **Seedance 2.5 官方生产规格 (2026 最新)** |
| :--- | :--- | :--- |
| **单通生成时长** | 5~15 秒 | **原生单次支持长达 30 秒**（支持连续拓展至 60s / 180s） |
| **图片参考槽位** | 最多 9 张 | **多达 30 张图片**（支持超高清 4K、≤30MB） |
| **视频参考槽位** | 最多 3 段（≤15s） | **多达 10 段视频**（单段 2~30s，总计 ≤30s） |
| **音频参考槽位** | 最多 3 段（伴随视频） | **多达 10 段音频**（支持独立纯音频参考，总计 ≤30s） |
| **时间戳解析能力** | 粗略排序参考 | **秒级严格锚定**（`[0-4s]`、`[4-10s]` 被作为真实时钟执行） |
| **人物写实度** | 略带磨皮感 | **真人毛孔漫反射与 11 种语言精准原生对白口型** |

---

## 二、 🌟 Seedance 2.5 官方四大专用语法标记 (Syntax Markers)

Seedance 2.5 废弃了散文式的声音描述，**正式推出了官方专用的四大括号标记符号系统**。模型对以下 4 种标记符号赋予最高级别的指令解析权重：

| 元素分类 | 官方专用标记 | 语法功能与规范 | 实战写法示例 |
| :--- | :---: | :--- | :--- |
| **配乐 (Music)** | **`( )` 英文圆括号** | 仅用于非剧情背景音乐、情绪伴奏。严禁用散文描述。 | `(低沉克制的传统潮汕古琴声在背景低回，无多余电音)` |
| **音效 (SFX)** | **`< >` 尖括号** | 用于画面内的物理撞击声、脚步、雷雨、茶具摩擦。 | `<粗布包袱落在石案上的沉闷钝响>` |
| **对白台词 (Dialogue)** | **`{ }` 大花括号** | **严禁丢掉花括号！**模型依据花括号直接绑定演员唇形。 | `{让让，你挡路了。}` |
| **标题/字幕 (Titles)** | **`【 】` 粗方括号** | 用于片头时间、地点印章、章节字幕。 | `【第一幕：顾景舟底槽清】` |

---

## 三、 原生对白口型强化公式 (Dialogue & Lip-sync Protocol)

为了确保 11 种语言对白能够 100% 严丝合缝对齐演员面部与口型，强制执行以下强化声明模板：

$$\text{对白指令} = \text{Dialogue language: 语言} + \text{发音腔调/语速} + \text{说话者与情绪} + \text{\{台词内容\}}$$

### 实战示例：
```text
Dialogue language: authentic Mandarin. delivery style: calm, low-mid pitch, unhurried and cold.
Lin Qingning gaze fixed forward, visible lips open and close in precise sync as she says:
{手滑赔得起，眼瞎没得医。}
```

---

## 四、 🌟 剪辑防粘连硬切守卫块 (Anti-mush Guard Block)

### 痛点：
Seedance 在处理多镜头提示词时，有时会错误地把“镜头1切到镜头2”渲染成一道诡异融化的长镜头（Mushy transition），导致画面扭曲形变。

### 必填防御咒语（放在多镜头时间轴开头）：
```text
This must be a multi-shot sequence with visible hard cuts.
Do not generate a single continuous take. Each beat uses a different angle and framing.
No blurry morphing, no dissolve transitions between shots.
```
**中文对应指令**：
`本视频严格由多个不同机位的硬切镜头组成（Multi-shot sequence）。严禁渲染为单个连续长镜头，镜头之间严禁任何融化过渡或画面形变，切点处必须是清晰直接的硬切（Hard cuts）。`

---

## 五、 Seedance 2.5 生产级宏观提示词模板 (30 秒全剧短片级)

```text
[参考资产声明]
@img1: 主角林青柠（身份与校服基底）
@img2: 对手崔秀雅（奢华定制造型）
@img3: 老紫砂小品壶（道具特写）
@audio1: 林青柠冷静低音声线参考

[全局戏剧意图]
Master intent: 学院长廊对峙，老紫砂真迹现世压制全场，暴雨将至。

[防粘连守卫]
This must be a multi-shot sequence with visible hard cuts. Do not generate a single continuous take.

[多镜头时间轴流水线]
[0-5s] 镜头1（全景交代）：35mm平视。@img1沿着大理石长廊行走，@img2带跟班挡住去路。<急促高跟鞋踩踏回音>，@img2冷笑抱胸。
[5-12s] 镜头2（反打台词）：50mm中近景过肩。@img2下颌微抬，嘲讽说道：{穿同款西装却一件首饰没有，二手淘来的吧？}，(背景无配乐)。
[12-20s] 镜头3（碰撞与特写）：50mm微距。@img2伸手推搡，粗布滑落，@img1单手稳稳托出@img3紫砂壶，壶身温润无贼光。<茶壶脱落摩擦声>。
[20-30s] 镜头4（决胜反应与反击）：正面特写。跟班脸色惨白失声喊道：{三亿的顾景舟底槽清？！}。@img1双眸清澈冰冷，稳定开合口型说道：{手滑赔得起，眼瞎没得医。}，说完捧壶迈步离开。

[环境与光影尾注]
Environment: 挑高石柱长廊，阴天暴雨前夕冷蓝光。
Audio globals: 真实长廊混响，脚步与衣料摩擦声，无背景配乐。
```
