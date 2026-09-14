# 快手可灵 Kling 3.0 / 2.6 专项提示词规约 (Kuaishou Kling Contract)

本规约作为 `jmcai-shotlist-builder-beta` 的快手可灵（Kling）视频大模型专项指导层。可灵在物理真实度、角色动画与多镜头原生对白上具备极强表现力，3.0 版本更支持多达 6 个镜头的单次连续生成与原生口型同步。

---

## 一、 可灵 3.0 五层提示词核心结构 (Five-layer Structure)

可灵 3.0 具备理解完整导演意图的上下文能力。提示词必须按照以下标准流水线层级编写，严禁乱序堆砌：

$$\text{Scene (全局场景)} \rightarrow \text{Characters (角色锚定)} \rightarrow \text{Action (多镜头动作)} \rightarrow \text{Camera (运镜参数)} \rightarrow \text{Audio (原生音效与对白)}$$

---

## 二、 角色提前锚定协议 (Subject Anchoring Protocol)

### 痛点：
在多人对手戏中，如果每句分镜都反复写角色的外貌长相，可灵极容易将两个角色的服装、脸型甚至性别混淆“窜台”。

### 解决方案：
**在提示词最顶部，且在任何分镜展开之前，使用带方括号的强标识声明角色：**

```text
[Character A: 林青柠 — 19岁中国女生，东亚清冷素颜，黑色垂直长发披肩，身穿宽松藏青色学院西装校服，无任何首饰]
[Character B: 崔秀雅 — 19岁财阀千金，冷艳浓妆，波浪黑卷发，同款藏青色西装外套但内搭真丝衬衫，佩戴水滴钻石耳钉]
```

**在后续的所有分镜描写中，直接统一使用 `Character A` / `Character B`**，严禁重新更换称呼。这能极大降低可灵底层的注意力混淆。

---

## 三、 可灵 3.0 多镜头原生时序语法 (Multi-Shot Syntax)

可灵单次生成最高支持 6 个分镜连续硬切。每个镜头必须明确回答三要素：**景别构图 (Framing) + 核心主体 (Subject) + 物理动作 (Motion)**：

```text
Master intent: 学院长廊内的阶层对峙与打脸反转。

Shot 1 (0-3s). 35mm wide tracking shot. Character A enters frame from left, walking calmly. Character B steps into path to block her.
Shot 2 (3-6s). Over-the-shoulder medium shot. Camera frames Character B sneering as her diamond earrings catch the light.
Shot 3 (6-10s). Extreme close-up. Character B shoves the bundle; Character A firmly braces and steadies the antique teapot.
Shot 4 (10-15s). Frontal medium close-up. Character A looks up calmly and speaks, holding her ground as Character B freezes.
```

> **警示**：空洞的镜头描述（如 `Shot 2: static frame, atmospheric mood`）会被可灵直接忽略，并坍缩为毫无动作的长镜头。必须写明具体的物理运动。

---

## 四、 P1–P4 对白与口型协议 (Dialogue Protocol)

在可灵中生成人物说话时，严格遵循以下四步准则：

1. **P1 结构化命名 (Structured Naming)**：
   - 必须使用唯一的角色标签对应台词：`Character A says: "..."`。
2. **P2 显式对白标记 (Explicit Quotations)**：
   - 台词必须使用双引号包裹，并在前面明确声明语言和语速：
     `Character A speaks in calm, clear Mandarin: "手滑赔得起，眼瞎没得医。"`
3. **P3 说话时机视线绑定 (Camera on Speaker)**：
   - 说话期间，摄像机必须保持该角色的面部或嘴唇在画面内可读，禁止在说话瞬间把机位切到无嘴唇的环境空镜。
4. **P4 画外音保护 (Voiceover Silence)**：
   - 当为内心独白或旁白时，必须显式声明：`Character A's lips remain firmly closed throughout the voiceover line.`

---

## 五、 常见形变与专属防崩负面词库 (Negative Constraints)

针对可灵在剧烈运动时容易出现的手指熔化、身体扭曲或突然抽搐，在负面词中强制固定：

```text
Negative: extra fingers, fused hands, deformed limbs, floating objects, jerky motion, blurry transitions between shots, sudden camera shake, morphing face, distorted pupils, unnatural smile, animated style, 3D render.
```
