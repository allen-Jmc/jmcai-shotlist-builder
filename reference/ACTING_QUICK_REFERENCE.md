# Acting Quick Reference (A1–A6)

**这一层是查表用的，不是读的。** 先在这里选词、过判断清单；需要理解"为什么"时再回下面四份方法文件：

| 方法层 | 管什么 |
| --- | --- |
| `MINIMAX_H3_ACTOR_DIALOGUE_CRAFT.md` | 一个说话人怎么出声、怎么分思维单元、怎么防念稿 |
| `MINIMAX_H3_EMOTION_PERFORMANCE.md` | 情绪从哪来（意图而非形容词）、六种情绪原型 |
| `MINIMAX_H3_MICRO_EXPRESSION.md` | 脸和身体漏什么（M001–M070 动作链库） |
| `SCENE_ACTING_CRAFT.md` | 两个人怎么接戏（听者、接话、地位、停顿、类型语法） |

**总原则：表是选词库，不是必填清单。** 每一项都要说得出「输入依据 → 表演目的 → 可见/可听证据 → 触发时机」。说不出依据的，不写。

---

## A1 语气与声音标签

标签是**写作约定**，不是已验证的平台接口语法。保持拼写原样，成对标签必须闭合。

| 标签 | 作用 |
| --- | --- |
| `<pause>` | 短暂停顿 |
| `<long pause>` | 长停顿，留出沉默 |
| `<i>词语</i>` | 重读包裹的词 |
| `<whisper>台词</whisper>` | 耳语说出 |
| `<softer>` | 降低后续音量 |
| `<humming>音节</humming>` | 哼唱音节 |
| `<breath>` | 插入呼吸声 |
| `<inhale>` / `<exhale>` | 吸气 / 呼气 |
| `<deep breath>` | 深呼吸，准备开口或平复 |
| `<catches breath>` | 停下来缓一口气 |
| `<pant>` / `<pants>` | 急促喘气 |
| `<laughs>` / `<chuckle>` | 笑出声 / 短促轻笑 |
| `<sighs>` | 叹气 |
| `<gasp>` | 突然倒吸气 |
| `<mhm>` | 认同的"嗯哼" |
| `<phew>` | 松一口气 |
| `<groan>` | 低沉呻吟或抱怨 |
| `<uh>` / `<hmm>` | 犹豫 / 思考声 |
| `<stutter>` | 结巴、重复、断续 |
| `<coughs>` / `<clears throat>` | 咳嗽 / 清嗓 |
| `<sniff>` | 吸鼻子 |
| `<smacks lips></smacks lips>` | 咂嘴 |
| `[Chinese]` / `[English]` | 指定对白语言 |
| `[Chinese, crying]` | 带哭腔 |
| `[Chinese, singing]` | 演唱台词 |
| `[Hum]` | 哼唱旋律 |

规则：标签写在 `<d>` 内；停顿与呼吸**占用时长**，不能把长台词+长停顿+细密动作挤进短窗口；语言与演唱标记是声音指令，不生成字幕。

---

## A2 微表情控制短语

单点动作用这里；需要时序组合时用 `MICRO_EXPRESSION` 的 M001–M070 动作链。**链优先，点其次，一拍一个点。**

| 部位 | 短语 | 中文 |
| --- | --- | --- |
| 眉 | `raises one eyebrow slightly` | 轻挑一侧眉 |
| 眉 | `briefly raises both eyebrows` | 短暂抬双眉 |
| 眉 | `draws the eyebrows slightly together` | 双眉向眉心靠拢 |
| 眉 | `slightly raises the inner corners of the eyebrows` | 轻微抬眉头 |
| 眉 | `the brow tension gradually releases` | 眉间紧张渐松 |
| 眼 | `narrows the eyes slightly` | 轻微眯眼 |
| 眼 | `the eyes widen briefly, then settle` | 短暂睁大再恢复 |
| 眼 | `blinks once, slowly` | 缓慢眨眼一次 |
| 眼 | `the lower eyelids tighten slightly` | 下眼睑轻收紧 |
| 眼 | `the eyes become moist without tears falling` | 眼湿不落泪 |
| 视线 | `glances sideways without turning the head` | 头不动眼神侧瞥 |
| 视线 | `briefly lowers the gaze, then restores eye contact` | 垂眸再恢复 |
| 视线 | `the gaze flicks toward the door, then returns` | 扫向门口再移回 |
| 视线 | `holds steady eye contact` | 稳定注视 |
| 嘴角 | `one corner of the mouth lifts slightly` | 单侧嘴角轻扬 |
| 嘴角 | `a faint, closed-mouth smile appears` | 轻微闭嘴笑 |
| 嘴角 | `the smile gradually fades` | 笑容渐消 |
| 嘴角 | `suppresses a smile by pressing the lips together` | 抿嘴压笑意 |
| 嘴角 | `the corners of the mouth turn down slightly` | 两侧嘴角轻垂 |
| 唇 | `presses the lips together briefly` | 短暂抿紧 |
| 唇 | `the lips part slightly before speaking` | 开口前轻启 |
| 唇 | `the lower lip trembles faintly` | 下唇轻颤 |
| 颌 | `the jaw tightens subtly` | 下颌轻绷 |
| 颌 | `the jaw slowly relaxes` | 下颌缓松 |
| 颊 | `the cheeks lift slightly as the eyes gently narrow` | 颊抬同时眼眯 |
| 鼻 | `the nostrils flare slightly` | 鼻翼轻张 |
| 鼻 | `briefly wrinkles the nose` | 短暂皱鼻 |
| 喉 | `swallows softly, with a small movement in the throat` | 轻吞咽、喉部微动 |

---

## A3 微表情修饰词

短语不给幅度、时长和触发点，模型只能猜。**只挂这一段需要的修饰词。**

| 修饰词 | 作用 |
| --- | --- |
| `slightly` / `subtly` | 缩小幅度 |
| `briefly` / `for a split second` | 缩短时长 |
| `gradually` / `slowly` | 放慢变化 |
| `only on the left side` | 限制单侧——**必须说明是角色自身左侧还是画面左侧** |
| `just before speaking` | 卡在开口前 |
| `on hearing the word "X"` | 绑定到台词里的真实词，X 必须真的出现过 |
| `then returns to a neutral expression` | 指定回落 |
| `while the rest of the face remains relaxed` | 隔离单通道 |

---

## A4 从表演意图到连续过程

三条判断，逐条过：

**1. 用行为呈现情绪，不用表情清单。** 先定人物目标与阻力，再决定需不需要变化、变化怎么被看见。想靠近却害羞 = 对视后回避、又试探看回；想说却克制 = 准备开口后中断、再决定说不说。**不能只看到"害羞"就加偷看，只看到"克制"就加吞咽。**

**2. 声音、口型、身体按同一事件配合。** 先定台词与演法，再选音量、音色、语速、停顿、重音。吸气准备 → 说话 → 停顿吞咽 → 说后呼气，按生理顺序排。低声、清晰、迟疑可以同时成立；"平淡"不等于没有口型。

**3. 景别决定能看见什么。** 胸部以上拍不到手部指节；面部近景不能同时承诺全身动作。写之前先问：这个构图真的看得见吗？看不见的改用肩颈、呼吸、视线表达，不改用户的景别。

**收尾必须延续刚才的行为**——继续回避、等待、松弛、喘息都可以，但**不默认恢复中性或微笑**。

---

## A5 多情绪转换与对白递进

先写一条可检验的**情绪弧线**，再排表情。不是"依次做几种表情"。

编排五步（可压缩合并，不要机械填满）：

1. **建立状态** — 观众先读懂此刻的关注点、期待、戒备或回避
2. **触发转折** — 用已知事件、对方沉默、角色观察到的动作，或意识到自己失态
3. **台词或行动推进** — 每句台词承担一个明确作用：确认、试探、追问、阻止、掩饰、坦白
4. **余波与下一次选择** — 说完可以等待、追随、收回、平复、重新决定；下一句由这份余波引出
5. **结局状态** — 保留这次过程的结果，不默认回到笑容或中性

**每句对白必须回答四件事：**

| 问题 | 答不出来会怎样 |
| --- | --- |
| **为什么现在说** | 台词变成平铺陈述，没有压力 |
| **说给谁** | 失去视线关系，变成自言自语 |
| **语气怎样** | 所有句子同一个音高，像念稿 |
| **说完发生什么** | 没有余波，下一句接不上 |

弧线规则：每次转换都要有可见或可听的触发；强度可以上升、下降或反转，但不能无依据地从耳语跳到嘶吼；未入画的对象不能替他补台词或制造声音。

---

## A6 输入冲突与时间预算

交付前五条检查，任何一条过不去就不要交付：

**1. 台词唯一。** 正文与声音控制里的台词必须完全一致。用户明确说"只说 X"时，按 X 清理其他位置，不能把两个版本拼起来。

**2. 时间可行。** 台词时长 ≈ 字数 ÷ 语速 + 停顿合计 + 开口准备（0.2–0.5 s）+ 余波（≥0.5 s）。不够时按顺序处理：① 删可选表情与铺垫；② 重新分配未锁定时间；③ 仍不够就问用户改哪一项（台词、语速还是时长）。**不交付说不完的时间轴，也不擅自删改台词。**

语速档位：普通对白 **4.0–4.5 字/秒**（默认 4.25），慢速旁白 / 压抑独白 **2.5–3.0 字/秒**。**即使剧情激动，也不超过 4.5 字/秒**——超了就延长单元或拆分，不靠加速硬塞。这一点比部分外部规范更严：现实中争吵能说到 5–6 字/秒，但生成模型在这个速度下吞字概率显著上升，宁可多一个单元。

**3. 声音范围明确。** 五类分别判断，不要一概而论：

| 类别 | 默认 | 注意 |
| --- | --- | --- |
| 对白 | 允许 | — |
| 其他人物发声 | 需依据 | 未入画者不得替他发声 |
| 环境声 | 允许 | "无额外音效"不等于静音 |
| 外界音效（敲门、鸟鸣） | 需依据 | 禁止外界声音的片段里不得突然加入 |
| 配乐 | 默认无 | "无背景音乐"≠ 全片静音 |

**4. 刺激与可闻性一致。** 在禁止外界声音的片段里，不写敲门声、鸟鸣或画外台词。只能写成片段开始前的刺激，或已有视觉刺激。

**5. 约束针对误演。** 按本段最可能出的错来写禁止项（2–4 条），不复制覆盖所有情绪的负面清单，也不禁止用户明确要的激烈动作。

---

## B11 文戏自检（输出前逐条过）

每条规则的做法见 `SCENE_ACTING_CRAFT.md`。这里只列"过没过"。

- [ ] 每句台词都有说话人、行动动词、听者反应、接话方式
- [ ] 每次情绪或策略转换都有触发，并有"意识到"的瞬间
- [ ] 地位关系清楚；若有翻转，翻转点落在具体台词或动作上
- [ ] 调度（如有）对应关系变化，且景别看得见
- [ ] 每句只有一个主重音；心理停顿的位置与停顿期间的表情写清
- [ ] 每个时间窗按字数与语速核算过，说得完，留有反应时间
- [ ] 表演尺度符合类型（生活流 / 史诗正剧 / 喜剧）
- [ ] 分段生成时已继承上一段的情绪当前状态
- [ ] 视线方向跨镜头一致；除非要求，否则不看镜头
- [ ] 禁止项写了本段最可能的 2–4 种误演

**任一条打不了勾，就不要交付。**
