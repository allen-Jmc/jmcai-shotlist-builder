# Final quality gate

The delivery gate for H3 work, previously inlined in `SKILL.md`.

**Passing the three linters does not close this gate.** The scripts prove structure:
field order, cut-time parity, filename isolation, speech budget arithmetic. They cannot
tell you that a performance is flat, that a prop chain silently breaks at unit 7, or that
two units cover the same source beat. This file covers what the scripts cannot.

Work through it in order and record the result of each block. If a block fails, fix it
before moving on — later blocks assume earlier ones hold.

---

# Final quality gate

Before H3 delivery:

1. Confirm authority separation, source-beat closure, prop-chain closure, transcript fidelity, and post-node routing.
2. Confirm every unit has one scene, one relationship turn, one action chain, complete opening/exit states, valid duration, valid speech budget, and stable head/tail handles.
3. Confirm the scene shot ladder is continuous and `N` adjacent units have exactly `N-1` complete boundary ledgers.
4. Confirm prompt nouns and soundscapes pass per-unit truth isolation; voice profiles remain stable and performance is playable rather than generic. Audit each `EMOTIONAL_RHYTHM_MAP`: opening pressure, exact trigger, one turn, visual motif, sonic pulse, tempo curve, and afterimage must all have observable evidence in final shot prose.
5. When a submitted style reference is declared global, audit every unit's reference list: the same style file must be present everywhere, no unit may exceed the platform reference cap, and any displaced reference must be a non-critical environment/secondary input with its scene truth still written explicitly.
5a. When `AUDIO_REFERENCE_MAP` is active, audit the operator checklist's exact filename spelling, real upload order, one-to-one character/source locks, unique audio labels, compatible mode/retention markers, and copied/referenced scope. Confirm both prompts use the checklist's slot labels at the correct vocal events; confirm the Chinese `主体定义：` contains one filename-free compact binding line per active label and no source filename. When inactive, confirm neither prompt contains `<Audio N>`, `Audio mode`, `Retention`, `audio reuse`, or `audio reference` routing language.
6. Confirm the Chinese prompt uses the six canonical sections in order (`主体定义：` → `任务摘要：` → `保留分析：` → `镜头详述：` → `环境音响：` → `非剧情音乐：`), that cut times inside `镜头详述：` increase without gaps or overlap, and that exactly one copyable Chinese prompt and one copyable English prompt exist for the unit with matching shot counts and cut times. When score is used, confirm its texture, pulse, entry, and exit are concrete and do not duplicate diegetic sound.
7. Confirm every spoken line remains verbatim on the line immediately following its delivery colon. Confirm the voice baseline and line delivery appear before it, and that no tag, bracketed instruction, quotation wrapper, or long acting note follows the dialogue in the same beat.
8. Search the submission prompt for authoring-template leakage and option language. Reject phrases that defer the actual shot choice, refer to a “next source fact,” use generic event placeholders, or instruct the writer/model to choose among several framings.
9. Confirm every audible speaker repeats a complete, self-contained voice baseline within that unit and that no dialogue direction says to match H3-001, the previous unit, or any unseen clip. A real audio reference may reinforce the match, but it does not remove this textual requirement.
10. When no audio reference is bound, compare every speaking unit for each character against the locked baseline string. Reject omissions, abbreviations, paraphrases that change acoustic meaning, or line delivery that contradicts the baseline. For VO split across shots, confirm an explicit continuous-event bridge.
11. For each triggered `MICRO_PERFORMANCE_SCORE`, confirm that the cue is visible at the chosen scale, caused by current scene truth, chronological rather than stacked, compatible with speech and lip sync, and carried into a polarity-consistent after-state in both prompt blocks. Reject decorative blinking, swallowing, tears, smiles, or hand business that does not change the dramatic reading.
12. Recompute `PACKED_RUNTIME` from the final unit records and compare it with every visible project and scene subtotal. Do not trust a previously approved or hand-entered total.
13. Run both deliverable linters and the permanent H3 regression suite. Treat any non-zero result as a build failure:

```text
python scripts/h3_prompt_lint.py <html-file>
python scripts/h3_unit_lint.py <html-file>
python scripts/h3_regression_tests.py
python scripts/h3_upload_order_lint.py <html-file>
```

13a. Check the per-unit upload checklist from `templates/H3_PRODUCTION_LAYOUT.md`: it is expanded, occurs before the unit's prompts, has contiguous modality-local numbering, exact clickable filenames with inline micro-thumbnails and instant hover zoom cards, meaningful roles, and audio targets/purposes when present. Compare its ordering with the actual input map and both prompt versions. Open the local links, copy both prompts, and check narrow-screen layout. After editing upload-order tooling, run `python scripts/h3_upload_order_tests.py`; these checks use local fixtures and must not generate media. This requirement applies to new or revised deliverables; do not retroactively rewrite a completed film when the task is only skill maintenance.

13b. Assemble the 5 industrial visual presentation modules from `templates/HTML_TEMPLATE.md` and `templates/H3_PRODUCTION_LAYOUT.md`:
  - **Module 1: Visual Asset Hub & Dual-Track Gallery (`{ASSET_HUB_SECTION}`)**: Render top-level character/scene asset cards equipped with 1-click copy buttons and native toggles between portrait looks and 4-view production turnaround sheets.
  - **Module 2: Prop State Progression Chain (`{PROP_STATE_TRACKER_BLOCK}`)**: Render timeline-ordered physical prop degradation/change nodes across scene events.
  - **Module 3: Cinematic Shot Badges (`{CINEMATIC_SHOT_BADGES}`)**: Render colored micro-crystal pill badges (focal length, shot size, camera move, lighting atmosphere, micro-acting) in each unit card.
  - **Module 4: Zero-Dependency Dual-Prompt Tab Container**: Wrap Tab 1 中文版 (Chinese six-section prompt) and Tab 2 英文版 (English six-section prompt) inside responsive tabs (`.prompt-tabs-container`) with native JS switching and toast copy feedback. Both tabs carry a generation copy control. There is no third tab.
  - **Module 5: 14-Point Anti-Glitch QA & Emergency Fix Spells (`{QA_CHECKLIST_AND_FIXES_CARD}`)**: Render the full 14-point audit checklist and the 5 high-frequency rescue spell copy panels.

14. Perform a per-shot action-density pass on the submitted `镜头设计`: locate the first frame where each shot's stated action or information lands. If the remaining duration is not an explicitly directed reaction, listening/decision process, environmental development, or final stable handle, repack the shot. Reject shots that park a character in a completed pose simply to fill a nominal duration.
15. Perform a scene-rhythm pass: verify every key action has an onset, change, and result; every reaction names its trigger and visible consequence; high-information dialogue is not competing with unrelated complex action; camera movement and shot-size changes have an information-bearing destination; and every cut is an action, eyeline, sound, or emotional handoff. Review each three-to-five-shot run for unmotivated sameness of scale, motion, or emotional temperature.
16. Perform a vocal-placement pass: every audible line has an explicit start/end window inside its owning shot, a visible or off-screen source valid for that window, a pre-line action/breath, and a separately timed reaction or tail. Reject any prompt where dialogue could plausibly be delayed to the end of a broad shot because its internal placement is unspecified.
17. Perform a self-containment pass: reject relative continuity wording in the copyable prompt, and verify that the unit states its own opening geometry rather than relying on another unit.
18. Perform the dual-prompt parity pass from `MINIMAX_H3_DUAL_PROMPT_CONTRACT.md`: compare shot count and cut times, reference roles, speaker mapping, exact dialogue payloads, action/prop states, soundscape, score decision, and exit state. Any mismatch blocks delivery.
