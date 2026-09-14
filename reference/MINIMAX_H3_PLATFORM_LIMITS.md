# MiniMax H3 platform input limits

Verified against MiniMax's official H3 open-source announcement on 2026-09-09:

- H3-Base-Ref2VA accepts up to **9 image inputs**.
- It accepts up to **3 video clips**. Each clip must be 2–15 seconds and their combined duration must not exceed 15 seconds.
- It accepts up to **3 audio clips**. Audio must accompany at least one image or video input; each clip must be 2–15 seconds and their combined duration must not exceed 15 seconds.
- H3-Base-FL2VA accepts zero, one, or two images for text-to-video, first-frame, last-frame, or first-and-last-frame generation. The JMCAI Shotlist Builder may retain a narrower production intake when its workflow requires submitted references; do not misstate that workflow choice as a platform limitation.

Official sources:

- https://www.minimax.io/news/minimax-h3-open-source
- https://design.minimax.io/h3

These are hard maxima, not target counts. Use only references with an explicit role in the current unit. Count a global style reference as one image input. Image, video, and audio limits are separate modality caps; do not reduce the image allowance merely because audio is present.

When official limits change, update this file and every caller together. Search the skill for stale numeric caps before delivery.
