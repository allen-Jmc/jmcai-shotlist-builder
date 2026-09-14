# Spatial Blocking — Top-Down Schema

**Rule:** before writing any prompt with 2+ characters, key props on a specific surface, or complex camera geometry — produce a top-down (bird's-eye) SVG schema and get user approval. AI video models hallucinate spatial relationships unless they're declared in absolute terms; the schema is how you lock blocking before the prompt is written.

## 1. When to draw a schema

Draw it for:
- Any scene with 2+ characters in the same location
- Any scene with a key prop on a specific surface (device, artifact, weapon, photo)
- Any scene where camera geometry matters (which shot from where)
- Any time the user requests a position change — redraw immediately

Skip it for:
- Single-character close-ups in a generic location
- Inserts/cutaways with no character relationship
- Pure environmental shots

## 2. What goes on the schema

- **Room/location outline** with labeled walls, tables, screens, bridges, etc.
- **Each character** as a colored circle with their initial (G, R, J, Re, etc.)
- **Eyeline arrow** from each character (where they're looking)
- **Props** as distinct icons (e.g., 📡 for the device, 📷 for camera-in-scene, 📄 for paper)
- **Distances** between key objects (~Xm)
- **Surface labels** (FL/FR/BL/BR — front-left, front-right, back-left, back-right, relative to a stated main view)
- **Main axis** (e.g., "north–south = entrance to screen") for orientation
- **Camera position(s)** for each shot in the scene — separate icon, labeled

## 3. How to render

Use `visualize:show_widget` with module `diagram`. Default viewBox: 900×720 (desktop). Use the dark theme tokens. Show character circles in the production palette (Roko = red, Gandelfina = gold, etc. — pick consistent colors and stick to them across scenes).

After rendering, ask: **"Positions correct? Edits?"** Iterate until approved before writing any prompt.

## 4. After approval — translating the schema into the selected platform

For **Seedance 2.0**, every prompt for that scene includes the original `⚠️空间布局` block that mirrors the approved schema:

```
⚠️空间布局（MAIN VIEW=从 [direction]，俯视图布局）：
位置A：[Character1]靠/站在 [exact location]——[detail, e.g. height, angle]
位置B：[Character2]站在 [exact location]——[detail]
位置C：[Prop]放置在 [exact location]——[detail]
⚠️[Critical alignment rules: distances, axes, mirroring, occlusion]
```

Example:
```
⚠️空间布局（MAIN VIEW=从天桥入口看向巨型屏幕）：
位置A：@image4站在中央通道最前方靠近屏幕，面朝三人。
位置B：@image1和@image2在通道中间并肩站立，距@image4约3米，面朝@image4方向。
位置C：@image3站在@image1和@image2正后方1.5米处——不在他们旁边，严格在他们背后，被他们的身体部分遮挡——也面朝@image4方向。
⚠️@image1左肩与@image2右肩间距约40厘米。@image3的头顶高度严格低于@image1和@image2的肩部连线（站位较远造成的视觉缩小）。
```

For **MiniMax H3**, do not insert this warning block or `@imageN` handles. Serialize the approved geometry naturally in Chinese `角色与场景` / `镜头设计` and English `detailed_description`, following the parent SKILL's current paired-prompt contract. Do not reintroduce retired `integrated_multimodal_description` fields.

For both platforms, preserve all of these facts:
- Distances in meters
- Cardinal directions or "north/south/east/west" relative to the declared main view
- Who occludes whom
- Which direction each character faces
- Any heights or eyelines that the model might get wrong

## 5. Position changes

If the user revises a position after approval — **redraw the schema first**, get re-approval, then update the prompt. Do not edit the prompt's `空间布局` block from memory; always work from the latest approved schema.
