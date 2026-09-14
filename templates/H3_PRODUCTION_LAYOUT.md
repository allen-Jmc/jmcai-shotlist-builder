# H3 production HTML — default delivery layout

Use this layout for H3 shotlist and prompt deliveries. It captures the user's approved production-card format, not the characters, runtime, unit count, source script, filenames or music decisions of any particular film. Do not request a new format confirmation on each project. Current explicit user layout changes take precedence.

## Page hierarchy

1. Project title, calculated runtime, unit count, effective spoken-character count, and truthful production status (planning / prompts ready / media generated).
2. Compact navigation: units, upload instructions, boundary ledger, postproduction text; print/PDF and optional search. Search does not change authoritative runtime totals.
3. For each unit: heading with ID, local duration and project time interval; scene/relationship turn; expanded **本段上传顺序**; shot timing/ladder; independently copyable Chinese review, Machine-aligned Chinese generation, and English prompts.
4. Complete adjacent-unit boundary ledger and exact postproduction text/timing.

Use dark blue-gray backgrounds, muted gold headings, readable light body text, wide centered content, bordered cards and generous paragraph spacing. Keep the 16:9 preview frames, mobile wrapping and copy controls. Summaries/tables may be collapsible, but the upload checklist must not be hidden in closed details, hover content, JSON, a global gallery, or another page. Do not require the user to scroll to a global asset list to discover a unit's input files.

Default style tokens (adapt spacing responsively): background `#101923`, card `#16232e`, border `#425361`, text `#e5e9ed`, accent `#e6c493`, link `#9ed8db`; main width about 1320px, padding 28px desktop / 12px mobile. Embed CSS and JS locally. Avoid external fonts or scripts. Never copy project-specific prose as template defaults.

## One input map, one visible checklist

Compile the actual upload map before prompt serialization. Render the checklist and prompt reference definitions from that same map. At each independent unit, numbering restarts at 1 **within each modality**; image 1 and audio 1 are independent positions. Preserve input roles: identity + wardrobe, environment, style-only, keyframe, motion source, audio timbre reference or original-signal reuse.

Each row must visibly show:

- **图片 1 / 视频 1 / 音频 1**, in the exact upload order;
- exact filename, linked to the actual local/approved remote asset, with a named subject and concise purpose;
- for audio, the target character/source, duration, `audio reference` versus `audio reuse`, and whether a short derivative or full original is intended;
- for ambiguous visual bindings, the corresponding model label (e.g. reusable `<Subject 2>` versus first-frame `<Picture 2>`) and its role. Image upload order is not automatically identical to Subject numbering; honor the actual mapping.

Prefer small linked image thumbnails where useful; always retain the exact visible filename. Full source paths may be secondary details. For portable deliveries use `assets/` and `audio/` links with matching packaged files; for a single HTML use verified absolute file links or embedded previews plus access to the actual upload file. A thumbnail or data URI alone is not an uploadable filename. Never claim a missing local file is available, and never use dead illustrative filenames in a final deliverable.

Repeat shared references at every consuming unit, including the actual global style input and its position. List only active references, not every project asset. If no audio/video is used, omit that modality's list; do not invent bindings. For units with no visual inputs under a supported mode, show an explicit empty-state reason instead of a fake image. H3 Ref2VA in this skill still requires real visual reference input.

Outside prompts, explain once that the Chinese review, Machine-aligned Chinese generation, and English blocks are alternative serializations for the same clip, not text to concatenate. Copy buttons must copy only prompt text through `textContent`, with success feedback and a selection fallback. Keep filenames and upload instructions outside the model-facing prompt grammar. Never silently change approved audio mappings, reference exclusions or an approved calibration prompt when improving the HTML.

## Machine-readable HTML component

Place exactly one expanded checklist inside its `h3-unit` article, after the unit plan and before its first prompt block. The scene preview may be before the article. Replace sample values with actual unit data and HTML-escape text/attributes. Repeat rows in actual upload order, images first, then any videos, then any audio. Reuse the canonical `h3-unit` timing/state attributes from `HTML_TEMPLATE.md`.

```html
<section class="upload-order" data-upload-unit="{UNIT_ID}" aria-label="本段上传顺序">
  <h3>本段上传顺序</h3>
  <ol class="upload-list">
    <li data-upload-kind="image" data-slot="1"
        data-filename="{ACTUAL_IMAGE_FILENAME}" data-role="{NAMED_SUBJECT_AND_ROLE}"
        data-model-label="{ACTUAL_MODEL_LABEL}">
      <strong>图片 1</strong> ·
      <a href="{ACTUAL_IMAGE_HREF}">{ACTUAL_IMAGE_FILENAME}</a>
      <span>{NAMED_SUBJECT_AND_ROLE}</span>
      <!-- Optional linked thumbnail uses the same actual file, not a substitute asset. -->
    </li>
  </ol>
  <!-- Add a separate ordered list only when actual audio inputs are active. -->
  <ol class="upload-list">
    <li data-upload-kind="audio" data-slot="1"
        data-filename="{ACTUAL_AUDIO_FILENAME}" data-role="{VOICE_PURPOSE}"
        data-target="{LOCKED_CHARACTER}" data-audio-mode="audio reference"
        data-model-label="&lt;Audio 1&gt;">
      <strong>音频 1</strong> ·
      <a href="{ACTUAL_AUDIO_HREF}">{ACTUAL_AUDIO_FILENAME}</a>
      <span>{LOCKED_CHARACTER} · {VOICE_PURPOSE} · {ACTUAL_DURATION}s · {ORIGINAL_OR_DERIVATIVE}</span>
    </li>
  </ol>
</section>
```

When the supported mode truly has zero visual inputs, use `data-no-visual-inputs="{EXPLICIT_REASON}"` on the checklist and show the same reason visibly. This is not a bypass for missing assets. Videos follow the same row contract with `data-upload-kind="video"`. Do not number audio after the final image; it begins at audio 1.

## Production CSS & Interactive JS Engine

The following embedded styles and vanilla script power the dark cinematic interface, responsive cards, multi-tab switching, pill badges, and one-click copy operations with zero external dependencies.

```css
/* Base tokens and unit cards */
:root {
  --bg-dark: #101923;
  --card-bg: #16232e;
  --border-color: #425361;
  --text-main: #e5e9ed;
  --text-muted: #8892b0;
  --gold-accent: #e6c493;
  --cyan-accent: #9ed8db;
  --emerald-accent: #34d399;
  --blue-accent: #60a5fa;
  --rose-accent: #fb7185;
}

body {
  background-color: var(--bg-dark);
  color: var(--text-main);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 24px;
}

.h3-unit {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 28px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
}

.h3-unit-plan {
  border-bottom: 1px solid rgba(66, 83, 97, 0.6);
  padding-bottom: 16px;
  margin-bottom: 16px;
  line-height: 1.7;
}

.h3-unit-plan b { color: var(--gold-accent); }

/* 1. Cinematic Shot Badges */
.cinematic-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 14px 0 16px;
}
.badge-pill {
  display: inline-flex;
  align-items: center;
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 9999px;
  border: 1px solid transparent;
  letter-spacing: 0.02em;
}
.badge-focal   { background: rgba(59, 130, 246, 0.15); border-color: rgba(96, 165, 250, 0.4); color: #93c5fd; }
.badge-shot    { background: rgba(230, 196, 147, 0.15); border-color: rgba(230, 196, 147, 0.4); color: #fde68a; }
.badge-camera  { background: rgba(52, 211, 153, 0.15); border-color: rgba(52, 211, 153, 0.4); color: #6ee7b7; }
.badge-light   { background: rgba(168, 85, 247, 0.15); border-color: rgba(192, 132, 252, 0.4); color: #d8b4fe; }
.badge-acting  { background: rgba(244, 63, 94, 0.15); border-color: rgba(251, 113, 133, 0.4); color: #fda4af; }

/* 2. Upload Checklist */
.upload-order {
  padding: 18px;
  margin: 16px 0 20px;
  border: 1px solid var(--border-color);
  border-radius: 10px;
  background: #1c2a36;
}
.upload-order h3 { margin: 0 0 12px; font-size: 14px; color: var(--gold-accent); text-transform: uppercase; }
.upload-list { list-style: none; padding: 0; margin: 0; }
.upload-list li {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
  padding: 10px 0;
  border-top: 1px solid rgba(66, 83, 97, 0.6);
  font-size: 13px;
  position: relative;
}
.upload-list li:first-child { border-top: none; }
.upload-thumb-wrap {
  position: relative;
  flex-shrink: 0;
  width: 44px;
  height: 44px;
  border-radius: 6px;
  border: 1px solid rgba(158, 216, 219, 0.4);
  background: #090e13;
  display: flex;
  align-items: center;
  justify-content: center;
}
.upload-mini-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 5px;
  display: block;
}
.upload-hover-preview {
  display: none;
  position: absolute;
  bottom: calc(100% + 8px);
  left: 0;
  width: 260px;
  background: #0d151c;
  border: 1px solid var(--cyan-accent);
  border-radius: 8px;
  padding: 6px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.85);
  z-index: 100;
  pointer-events: none;
}
.upload-hover-preview img {
  width: 100%;
  max-height: 150px;
  object-fit: cover;
  border-radius: 4px;
  display: block;
}
.preview-caption {
  font-size: 10px;
  color: var(--text-muted);
  margin-top: 4px;
  line-height: 1.4;
  white-space: normal;
}
.upload-thumb-wrap:hover .upload-hover-preview {
  display: block;
  animation: fadeIn 0.15s ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}
.upload-info { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; flex-grow: 1; }
.upload-list strong { color: var(--gold-accent); }
.upload-list a { color: var(--cyan-accent); text-decoration: none; overflow-wrap: anywhere; }
.upload-list a:hover { text-decoration: underline; }
.upload-list span { color: #c5d0d8; }

/* 3. Prompt Multi-Tab Container */
.prompt-tabs-container {
  margin-top: 18px;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  overflow: hidden;
  background: #131d27;
}
.prompt-tabs-nav {
  display: flex;
  background: #0d151c;
  border-bottom: 1px solid var(--border-color);
  gap: 2px;
}
.tab-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 10px 18px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  border-bottom: 2px solid transparent;
}
.tab-btn:hover { color: #fff; background: rgba(255,255,255,0.03); }
.tab-btn.active[data-tab="zh"] { color: var(--gold-accent); border-bottom-color: var(--gold-accent); background: rgba(230,196,147,0.08); }
.tab-btn.active[data-tab="zh-exec"], .tab-btn.active[data-tab="zh-machine"] { color: var(--emerald-accent); border-bottom-color: var(--emerald-accent); background: rgba(52,211,153,0.08); }
.tab-btn.active[data-tab="en"] { color: var(--blue-accent); border-bottom-color: var(--blue-accent); background: rgba(96,165,250,0.08); }

.prompt-tab-pane { padding: 16px; }
.prompt-pane-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.copy-btn {
  padding: 4px 12px;
  background: #233342;
  border: 1px solid #4a5d6e;
  border-radius: 4px;
  color: #e5e9ed;
  font-size: 11px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}
.copy-btn:hover { background: #32475b; border-color: var(--cyan-accent); color: #fff; }
.copy-btn.copied { background: #065f46; border-color: #34d399; color: #a7f3d0; }
.copy-btn.mini { font-size: 10px; padding: 2px 8px; }

.prompt-block {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 12px;
  line-height: 1.65;
  white-space: pre-wrap;
  word-break: break-word;
  background: #0b1117;
  padding: 14px;
  border-radius: 6px;
  border: 1px solid rgba(66, 83, 97, 0.4);
  color: #d1d9e0;
}

/* 4. Asset Hub & Gallery */
.asset-hub-section, .prop-tracker-section, .qa-checklist-section {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px;
  margin: 28px 0;
}
.section-header-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 12px;
  margin-bottom: 20px;
}
.section-title { margin: 0; font-size: 18px; color: var(--gold-accent); }
.section-badge {
  font-size: 10px;
  padding: 3px 8px;
  border-radius: 4px;
  background: rgba(158, 216, 219, 0.15);
  color: var(--cyan-accent);
  border: 1px solid rgba(158, 216, 219, 0.3);
  text-transform: uppercase;
}

.asset-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 18px;
}
.asset-card {
  background: #111a22;
  border: 1px solid rgba(66, 83, 97, 0.8);
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.asset-thumb-box {
  position: relative;
  width: 100%;
  height: 180px;
  background: #090e13;
  display: flex;
  align-items: center;
  justify-content: center;
}
.asset-thumb { width: 100%; height: 100%; object-fit: cover; }
.asset-view-switch {
  position: absolute;
  bottom: 8px;
  left: 8px;
  display: flex;
  gap: 4px;
  background: rgba(13, 21, 28, 0.85);
  padding: 3px;
  border-radius: 6px;
  border: 1px solid rgba(66, 83, 97, 0.6);
  backdrop-filter: blur(4px);
  z-index: 2;
}
.view-btn {
  background: transparent;
  border: none;
  color: #8892b0;
  font-size: 10px;
  padding: 2px 8px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}
.view-btn:hover { color: #fff; }
.view-btn.active {
  background: #1e2c38;
  color: var(--cyan-accent);
  font-weight: 600;
  border: 1px solid rgba(158, 216, 219, 0.3);
}
.img-fallback {
  display: flex;
  align-items: center;
  justify-content: center;
  background: repeating-linear-gradient(45deg, #111a22, #111a22 10px, #16232e 10px, #16232e 20px);
  color: #64748b;
  font-size: 11px;
}
.asset-tag {
  position: absolute;
  top: 8px;
  right: 8px;
  background: rgba(0,0,0,0.75);
  color: #fff;
  font-size: 10px;
  padding: 2px 6px;
  border-radius: 4px;
  z-index: 2;
}
.asset-details { padding: 14px; display: flex; flex-direction: column; flex-grow: 1; }
.asset-name { margin: 0 0 6px; font-size: 14px; color: #fff; }
.asset-meta { font-size: 12px; color: var(--text-muted); margin: 0 0 12px; line-height: 1.5; flex-grow: 1; }
.asset-prompt-actions { display: flex; gap: 8px; }
.asset-copy-btn {
  flex: 1;
  padding: 5px 8px;
  font-size: 10px;
  background: #1e2c38;
  border: 1px solid #3d4f5e;
  border-radius: 4px;
  color: #d1d9e0;
  cursor: pointer;
  transition: all 0.2s;
}
.asset-copy-btn:hover { background: #283a4b; color: #fff; border-color: var(--cyan-accent); }

/* 5. Prop Physical State Tracker */
.prop-timeline { display: flex; flex-direction: column; gap: 12px; }
.prop-card {
  background: #111a22;
  border: 1px solid rgba(66, 83, 97, 0.8);
  border-radius: 8px;
  padding: 14px 18px;
}
.prop-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
.prop-name { font-weight: bold; color: var(--gold-accent); font-size: 13px; }
.prop-stage { font-size: 11px; color: var(--cyan-accent); background: rgba(158, 216, 219, 0.1); padding: 2px 6px; border-radius: 4px; }
.prop-desc { font-size: 12px; color: #c5d0d8; line-height: 1.5; }
.prop-connector {
  align-self: center;
  color: var(--text-muted);
  font-size: 11px;
  font-weight: bold;
  padding: 4px 12px;
  background: rgba(255,255,255,0.03);
  border-radius: 9999px;
}

/* 6. QA Checklist & Emergency Fixes */
.qa-content-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
@media (max-width: 900px) { .qa-content-grid { grid-template-columns: 1fr; } }
.qa-sub-title { margin: 0 0 14px; font-size: 14px; color: var(--gold-accent); }
.qa-checklist-list { list-style: none; padding: 0; margin: 0; font-size: 12px; line-height: 2; }
.qa-checklist-list label { display: flex; align-items: center; gap: 8px; color: #cbd5e1; cursor: default; }
.fix-item {
  background: #111a22;
  border: 1px solid rgba(66, 83, 97, 0.7);
  border-radius: 6px;
  padding: 10px 14px;
  margin-bottom: 10px;
}
.fix-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
.fix-title { font-size: 12px; font-weight: 600; color: #fda4af; }
.fix-code {
  font-family: monospace;
  font-size: 11px;
  color: var(--text-muted);
  margin: 0;
  word-break: break-all;
}

@media print {
  body { background: #fff; color: #000; }
  .h3-unit, .asset-hub-section, .prop-tracker-section, .qa-checklist-section {
    background: #fff; border: 1px solid #ccc; color: #000; box-shadow: none; break-inside: avoid;
  }
  .prompt-block { background: #f8f9fa; color: #000; border: 1px solid #ddd; }
  .prompt-tabs-nav, .copy-btn, .asset-copy-btn { display: none; }
  .prompt-tab-pane { display: block !important; padding: 8px 0; }
}
```

```javascript
// Native Zero-Dependency Tab Switching and 1-Click Safe Copy Engine
function switchPromptTab(button, tabType) {
  const container = button.closest('.prompt-tabs-container');
  if (!container) return;

  // Toggle navigation buttons
  container.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  button.classList.add('active');

  // Toggle panes
  container.querySelectorAll('.prompt-tab-pane').forEach(pane => {
    pane.classList.remove('active');
    pane.style.display = 'none';
  });

  let targetPane = container.querySelector(`.tab-pane-${tabType}`);
  if (!targetPane && tabType === 'zh-exec') {
    targetPane = container.querySelector('.tab-pane-zh-machine');
  } else if (!targetPane && tabType === 'zh-machine') {
    targetPane = container.querySelector('.tab-pane-zh-exec');
  }
  if (targetPane) {
    targetPane.classList.add('active');
    targetPane.style.display = 'block';
  }
}

function switchAssetView(button, targetImgId) {
  const box = button.closest('.asset-thumb-box');
  if (!box) return;
  box.querySelectorAll('.view-btn').forEach(btn => btn.classList.remove('active'));
  button.classList.add('active');

  box.querySelectorAll('.asset-thumb').forEach(img => {
    img.classList.remove('active');
    img.style.display = 'none';
  });
  const target = box.querySelector(`#${targetImgId}`);
  if (target) {
    target.classList.add('active');
    target.style.display = 'block';
  }
}

function copyPromptText(button) {
  const pane = button.closest('.prompt-tab-pane');
  if (!pane) return;
  const block = pane.querySelector('.prompt-block');
  if (!block) return;
  const text = block.textContent || '';
  navigator.clipboard.writeText(text).then(() => {
    const originalText = button.textContent;
    button.textContent = '已复制!';
    button.classList.add('copied');
    setTimeout(() => {
      button.textContent = originalText;
      button.classList.remove('copied');
    }, 1800);
  });
}

function copySnippet(button, text) {
  navigator.clipboard.writeText(text).then(() => {
    const originalText = button.textContent;
    button.textContent = '已复制!';
    button.classList.add('copied');
    setTimeout(() => {
      button.textContent = originalText;
      button.classList.remove('copied');
    }, 1800);
  });
}
```

## Delivery checks

Run `python scripts/h3_upload_order_lint.py <html-file>` alongside existing prompt/runtime linters. It checks structural association, ordering, filename links, required roles and audio targets, simple hidden/collapsed markup, and local-file existence. It does **not** prove semantic reference correspondence, media quality, remote-link reachability, or CSS visibility. Also compare rows against the real input map, inspect in a browser, follow the asset links, and test copy buttons and mobile layout. No media generation is needed to test a template.

For tool maintenance run `python scripts/h3_upload_order_tests.py`. Existing projects without these semantic attributes remain historical deliverables; a skill-only update does not authorize mass rewriting them.

