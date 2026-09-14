# 好莱坞工业级摄影机与专业灯光词典 (Camera & Lighting Vocabulary)

本词典作为 `jmcai-shotlist-builder-beta` 的专业视听词库层，用于指导中文审稿版分镜与英文执行版提示词（特别是 `detailed_description:`）中的摄影机运动与光影质感描述。**“‘电影感’不是指令，‘35mm 镜头，慢速推进，画面左侧切入温暖的窗户主光，右侧深沉阴影’才是专业指令。”**

---

## 一、 经典影视灯光与光质谱系 (Lighting Quality & Direction)

在描述光线时，禁止使用“光线很好”、“唯美打光”，必须明确指定**光源类型、入射方向与明暗对比度**：

| 专业灯光术语 (英文) | 中文标准称谓 | 视觉特征与戏剧功能 | 实战提示词描写示例 |
| :--- | :--- | :--- | :--- |
| **Rembrandt Lighting** | **伦勃朗光** | 人物阴影侧面颊上呈现经典的三角形光斑，塑造深沉、威严与立体感。 | `Rembrandt lighting with a distinct illuminated triangle on the shadow cheek.` |
| **Rim Light / Kicker** | **轮廓光 / 侧逆发丝光** | 从被摄体斜后方照射，在发丝、肩膀或轮廓边缘勾勒出一道高光细线，将被摄体与暗黑背景强力剥离。 | `Sharp cold rim light tracing the outer edge of her navy blazer against the dark marble.` |
| **Chiaroscuro** | **高反差明暗对比 (强光影)** | 亮部极亮、暗部极深，大光比戏剧阴影，强调道德撕裂或权力压迫。 | `High-contrast chiaroscuro lighting, deep cavernous shadows contrasting with bright directional beam.` |
| **Practical Light** | **场景实用光源** | 画面中真实可见的物理灯具（如床头台灯、蜡烛、老旧荧光灯管、车队大灯），光照自然衰减。 | `Lit primarily by practical lights: a single swaying warm bulb overhead casting swinging shadows.` |
| **Volumetric Light / God Rays** | **体积光 / 丁达尔效应** | 光束穿透空气中的微尘、薄雾、暴雨或茶汽，形成清晰可见的光柱。 | `Volumetric light beams slicing through airborne tea steam in the dim room.` |
| **Soft Diffused Light** | **柔漫射光 (阴天/窗光)** | 大面积柔和漫反射，阴影柔和渐变，用于内敛从容的情感交流。 | `Gentle diffused north-facing window light, soft shadow roll-off with no harsh hot spots.` |

---

## 二、 工业级运镜全谱系 (Camera Movement & Dynamic Presets)

在描述镜头运动时，**绝对禁止使用 `zoom`（光学变焦）**，强制使用真实的机械物理机位位移术语：

| 运镜术语 (英文) | 中文标准称谓 | 机械运动方式与戏剧节拍 |
| :--- | :--- | :--- |
| **Static Camera** | **固定机位** | 摄像机锁死在重型三脚架上，绝对静止，全靠被摄者微表情与空间自身施压。 |
| **Slow Push-in** | **慢速推进 (Dolly-in)** | 轨道物理向前推近，视线收窄，压力骤增，距离通常控制在 10~25 厘米内。 |
| **Pull-back / Dolly-out** | **慢速拉出** | 摄像机物理后退，揭示角色周围原本不可见的危险环境或第三者。 |
| **Lateral Tracking** | **横向平移跟拍** | 摄像机平行于被摄者移动路线同步滑轨平移，保持被摄者在画面同等比例。 |
| **Handheld Micro-shake** | **受控手持微晃** | 模仿摄影师贴身持机的自然呼吸起伏与心跳微颤，带有人性体温，禁用电子稳定器。 |
| **Whip Pan** | **快速甩镜 (闪光转场)** | 摄影机以极高角速度瞬间甩向侧面，产生强烈的水平动态模糊，常用于激烈动作或换场。 |
| **Dolly-Zoom (Hitchcock Zoom)** | **滑动变焦 (希区柯克变焦)** | 摄影机物理后退同时镜头拉焦（或反之），人物大小不变，但背景空间剧烈扭曲扩张，呈现顿悟或极度眩晕。 |
| **Rack Focus** | **移焦 / 焦点转换** | 机位不动，焦平面在 0.5 秒内从前景道具平滑切换至后景人物眼睛。 |
| **Orbit** | **环绕镜头** | 摄像机沿弧形轨道围绕对峙中的两人或核心道具进行 45°~90° 的慢速圆周旋转。 |
| **Crane / Aerial Shot** | **升降臂 / 俯瞰航拍** | 摄像机从低空垂直抬升至 10 米高空，展现百辆车队或宏大建筑空间。 |
| **Bounce Speed Ramp** | **弹跳变速 (快慢快)** | 动作启动时正常 $\rightarrow$ 核心碰撞或交锋瞬间骤降至慢动作 $\rightarrow$ 动作落地瞬间恢复原速。 |

---

## 三、 单镜头一主一副运镜克制律 (The Dominant Move Rule)

> **铁律**：一个 5~15 秒的镜头内，**只能确立 1 个主导运镜动作（Dominant Move）**。至多允许叠加 1 个极轻微的次级修饰（如微弱呼吸手持），严禁乱晃。

- **错误写法（贪多嚼不烂）**：
  ❌ *“摄影机快速前推，同时向左旋转，接着向下俯冲并变焦拉远。”*（AI 模型必崩，画面产生严重撕裂与几何形变）。
- **正确写法（主导克制）**：
  ✅ *“摄影机保持 35mm 固定平移跟拍（主导），全程带有极细微规律的手持呼吸感（次级微动）。”*

---

## 四、 景别与构图裁切标准对照表 (Framing & Composition)

| 简写代号 | 英文全称 | 中文标准景别 | 裁切基准线与应用场景 |
| :---: | :--- | :--- | :--- |
| **EWS** | Extreme Wide Shot | **大远景 / 极景** | 百辆迈巴赫车队、暴雨中的整个码头港口，人物仅占画面 5% 以下。 |
| **WS** | Wide Shot | **全景** | 从头到脚完整全身，包含地平线接触点与周围环境建筑。 |
| **MS** | Medium Shot | **中景** | 腰部以上截切，标准双人对手戏与常规肢体交流。 |
| **MCU** | Medium Close-Up | **中近景** | 胸口以上截切，能清晰兼顾手部小动作与面部神态。 |
| **CU** | Close-Up | **特写** | 锁骨到头顶，清晰读取眼神光、嘴角肌肉与发丝。 |
| **ECU** | Extreme Close-Up | **大特写** | 额头到下巴填满画面，极浅景深，专用于核心微表情冲突。 |
| **OTS** | Over-the-Shoulder | **过肩镜头** | 前景为听者虚化的肩背，后景焦点清晰锁死说话者。 |
| **POV** | Point of View | **主观视点镜头** | 摄像机完全模拟主角双眼看到的视线目标。 |
| **Dutch Angle** | Dutch Tilt | **荷兰角 (倾斜机位)** | 地平线倾斜 15°~25°，表现心理失衡、危机降临或狂妄挑衅。 |

---

## 五、 中英双语落地写作范式

在编写 H3 六段式 `detailed_description:` 时，直接调用本词典的精准组合：

```text
[Shot 1] A 35 mm eye-level medium tracking shot (F2.8) follows <Subject 1> along the marble hallway. Key illumination comes from low-angle morning sunlight slicing through archways, casting sharp diagonal shadows, complemented by a subtle cold rim light defining her navy silhouette.

[Shot 2] At 00:05.000, cut to an extreme close-up (85 mm, F1.4) of <Subject 2> under Rembrandt lighting. The camera performs a slow, barely perceptible 10 cm dolly-in as her jaw clenches and knuckles whiten against the handrail.
```
