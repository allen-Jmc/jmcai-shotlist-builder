# Default Style Block

This Chinese style paragraph is appended to **every** prompt unless the user uploads a custom style override. Drop it in verbatim, then layer the scene-type-specific lighting clause on top.

## Universal lighting rules (always present)

These rules go into **every** prompt's style block, regardless of scene:

```
灯光：⚠️严格仅使用场景内实际存在的光源（practicals）——屏幕、显示器、办公舱内部灯光、窗户、实用吊灯/台灯等。
禁止一切电影补光——禁正面光、禁侧面补光、禁顶光、禁底光、禁反光板、禁柔光箱、禁LED灯带、禁霓虹、禁任何画面外光源。
摄影机始终在人物的阴影侧（shadow side）拍摄——面部自然受光但从较暗的一侧取景，practicals环境光照亮脸部轮廓和眼神光（catchlight）。
全程大气薄雾haze增加空气质感——禁止可见光束（god rays）。
```

If the scene has a screen/monitor in frame, also append:
```
⚠️禁止屏幕/显示器向环境投射可见蓝色光芒——屏幕仅作为背景元素发光，不作为主光源。
⚠️禁止蓝色色溢（blue spill）打在人物皮肤和服装上。
```

## Universal color rule (always present)

Default palette declared in every prompt:
```
色彩：60:30:10——主色/辅色/点缀色。
```

Pick the proportions to match the scene's **mood**:

| Mood | Proportion |
|---|---|
| **Cold conflict / tension** | 60% cool blue + 30% concrete grey + 10% red accent |
| **Warmth / intimacy** | 60% warm tungsten + 30% deep brown + 10% amber |
| **Danger / panic** | 60% deep red + 30% black + 10% sodium orange |
| **Sci-fi / tech** | 60% black + 30% cool grey + 10% accent (purple / cyan) |

State the proportion explicitly in the prompt, e.g.:
```
色彩：60:30:10——冷蓝/混凝土灰/红色点缀。
```

**Default forbidden:**
```
禁3D渲染，禁游戏引擎，禁游戏CG过场质感，禁霓虹，禁过饱和色，禁HDR感。
```

## The full block (canonical)

```
风格：8K IMAX。超写实——禁3D渲染，禁游戏引擎，禁游戏CG过场质感。摄影：Emmanuel Lubezki × Roger Deakins。灯光：⚠️严格仅使用场景内实际存在的光源（practicals）。禁止一切电影补光——禁正面光、禁侧面补光、禁顶光、禁底光、禁反光板、禁柔光箱、禁LED灯带、禁霓虹、禁任何画面外光源。摄影机始终在人物的阴影侧（shadow side）拍摄。全程大气薄雾haze——禁止可见光束（god rays）。色彩：60:30:10——主色/辅色/点缀色。镜头：物理电影镜头。180°快门运动模糊。皮肤：毛孔级写实——汗毛、不对称痣、毛细血管潮红、毛孔阴影匹配现场光源。表演：好莱坞级——反应前微停顿、精准视线、湿润活眼带眼神光、可见呼吸和胸腔起伏。物理：重力惯性真实——质量有真实重量、正确接触阴影。禁漂浮道具。构图：三分法+黄金比例。每人从第一帧开始运动。连续性：角色、道具、环境每个镜头完全一致。禁身份漂移。技术：60fps流畅运动。8K细节。禁抖动（除手持呼吸感）。音频：仅环境SFX。禁音乐。禁字幕。
```

## Scene-type lighting variants

Layer these specific clauses into the lighting section above based on the scene:

### Night interior — natural light only (e.g., dark apartment, no lamps on)
```
灯光：夜景——室内全部灯光关闭，禁任何室内光源（禁灯、禁台灯、禁屏幕光），整个空间唯一的光来自窗外城市夜景透过窗户洒入的冷蓝光。摄影机始终在人物的阴影侧拍摄。
```

### Underground base / sci-fi interior with practicals
```
灯光：⚠️严格仅使用场景内实际存在的光源（practicals）——屏幕、工作站显示器、玻璃办公舱内部灯光。禁止一切电影补光。⚠️禁止屏幕/显示器向环境投射可见蓝色光芒——屏幕仅作为背景元素发光。主要照明来自玻璃办公舱内暖白灯光和工作台台灯的漫反射。摄影机始终在人物的阴影侧（shadow side）拍摄。⚠️禁止蓝色色溢（blue spill）打在人物皮肤和服装上。
```

### Day exterior
```
灯光：仅自然日光——硬阳光+大气散射，摄影机始终在人物的阴影侧（shadow side）拍摄，contre-jour逆光从天空方向，禁反光板、禁补光、禁柔光箱。全程大气haze增加深度。
```

### Night exterior
```
灯光：仅实际街灯、车头灯、店铺霓虹反射、路灯。无任何摄影补光。摄影机在人物阴影侧。全程城市haze。
```

### Warm interior (kitchen, bedroom with lamps on)
```
灯光：仅室内实际灯光——温白色台灯、吊灯、暖色practicals。摄影机始终在阴影侧。无任何外部补光。haze轻微。
```

## Closing footer (always)

Every prompt ends with:
```
15秒。21:9。
```

For multi-shot prompts (one prompt with internal `【镜头1】【镜头2】【镜头3】` cuts), still 15 seconds total — divide internally per shot duration rules in CAMERA_EMOTION.md.

## Aspect ratio override

If user specifies a different aspect ratio (e.g., 9:16 for shorts, 4:3 for retro), swap `21:9` in the footer.

## Camera/composition rule (append for wide shots)

For wide shots and any shot using a lens 35mm or wider, append:
```
禁光学畸变——禁桶形畸变、禁枕形畸变、禁鱼眼效果、禁广角变形，画面线条必须笔直，构图平整。
```

## Multi-shot prompt header

When a prompt contains internal cuts (`【镜头1】【镜头2】` etc.), prepend:
```
多机位剪辑（multi-shot）。
```

When a prompt is a continuous one-er, prepend:
```
单镜头（one-shot，无剪辑）。
```
