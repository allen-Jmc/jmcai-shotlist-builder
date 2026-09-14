# 视频穿帮修复与 14 项连续性终审清单 (Continuity & Fixes Checklist)

本规约作为 `jmcai-shotlist-builder-beta` 的防穿帮终审工具箱。用于在最终交付工单或生成提示词前，排查所有跨镜头、跨片段的时空穿帮与逻辑破绽，并为常见的 AI 视频翻车提供即插即用的修复咒语。

---

## 一、 14 项连续性终审自检表 (Pre-Delivery Checklist)

在分镜工单输出或提交生成前，逐项核对以下 14 项指标。**只要有 1 项不符，立即修正：**

- [ ] **1. 人脸绝对一致**：同一角色在不同分镜中，脸型、骨相、眼珠颜色、发型长短完全一致。
- [ ] **2. 服装细节锁死**：服装款式、纽扣颜色、领口开合状态在相邻镜头中未发生突变。
- [ ] **3. 空间地理连续**：角色的左右站位、背后背景建筑与门窗光源位置逻辑自洽。
- [ ] **4. 道具状态流转合规**：道具的物理移动符合因果律（如：老紫砂在包袱内 $\rightarrow$ 露出一角 $\rightarrow$ 单手托起 $\rightarrow$ 稳稳捧直，绝不凭空瞬移）。
- [ ] **5. 杜绝幽灵多余人物**：画面中没有未在剧本中声明的模糊路人或突兀多余脸孔。
- [ ] **6. 画面零杂乱字幕**：提示词中显式禁止任何未经授权的英文字幕、乱码水印、片名字样。
- [ ] **7. 年龄与体态锁定**：角色体型比例与年龄感稳定，不忽大忽小、忽老忽少。
- [ ] **8. 物理真实动作**：手部持握、迈步动作符合人体解剖学，无反关节或手指黏连。
- [ ] **9. 运镜拒绝空洞**：严禁出现 `cinematic camera` 等泛词，必须有具体焦段与物理位移。
- [ ] **10. 灯光拒绝抽象**：严禁出现 `beautiful light`，必须有明确的主光与辅助光来源。
- [ ] **11. 导演风格不杂糅**：单场戏严格遵循单一导演/胶片视听基调，不胡乱拼贴冲突流派。
- [ ] **12. 色彩饱和度受控**：色调必须由具体的 2~3 种环境主色统领，不出现调色盘失控。
- [ ] **13. 尾态画面稳定定格**：每个片段结尾必须有明确的稳定终态帧（Afterimage），无悬空半截动作。
- [ ] **14. 逻辑零前后矛盾**：如前一秒是暴雨，后一秒地面绝不能干透无水渍。

---

## 二、 关键道具状态迁移追踪链 (Object Progression Chain)

对于短剧核心道具（如三亿紫砂小品壶、钛合金卫星电话），必须建立一条线性的物理迁移链，防止道具凭空消失或状态打架：

```text
[初始状态] 粗棉布包袱紧紧包裹，斜挎在林青柠身侧
    ↓ (H3-001 碰撞触发)
[解体状态] 崔秀雅跟班撞击，布料松脱滑开约一半，露出深红紫泥壶钮
    ↓ (H3-002 现世状态)
[持握状态] 林青柠单手稳稳托住壶底，壶身温润无损，段砂颗粒在晨光下显露
    ↓ (H3-003 收回状态)
[带走状态] 青柠将小壶重新捧于双手中，贴近胸前，转身迈步带出画外
```

---

## 三、 五大高频翻车模式的现成修复模板 (Failure Modes & Fixes)

当遇到模型生成翻车时，直接将以下针对性防崩修复句式追加进提示词：

### 翻车 1：镜头融化粘连成一条长镜头（One continuous take instead of montage）
- **修复咒语**：
  ```text
  This must be a multi-shot sequence with visible hard cuts. Do not generate a single continuous take. Each beat uses a completely different angle and framing with crisp cut transitions.
  ```

### 翻车 2：角色在相邻镜头中换脸或换衣（Character face/outfit changes）
- **修复咒语**：
  ```text
  Preserve the exact same character in every shot: identical bone structure, same eyes, identical navy tailored blazer with brass buttons, identical hair length. Do not alter identity or costume.
  ```

### 翻车 3：核心道具中途凭空消失（Object disappears mid-scene）
- **修复咒语**：
  ```text
  Track the object continuously. The dark purple-clay teapot remains physically present and firmly held in her right hand across all frames; it must never vanish or morph.
  ```

### 翻车 4：戏剧张力不足、表演像木偶（Weak drama, flat scene）
- **修复咒语**：
  ```text
  Play the scene with intense, quiet dramatic gravity. Every actor exhibits subtle physical tension: clenched jaw, restrained breathing, and piercing direct eye contact. No relaxed or neutral drifting.
  ```

### 翻车 5：多镜头快切时画面混乱狂晃（Messy random cuts）
- **修复咒语**：
  ```text
  Maintain strict 180-degree axis continuity. The camera remains strictly on the west side of the characters. Every cut lands cleanly on a decisive glance or physical impact.
  ```
