# Creative Chain distill (from VOXCAT ChatGPT→Eagle exporter)

Tooling repo is a Chrome extension. This note is the craft-relevant model only.

## What to keep when archiving / revising
- Preserve the **causal chain**: Base Prompt → Generated → Revision → Generated…
- **Base Prompt (NEW ROOT)** starts a chain; later style forks should usually start a new chain (conservative).
- **Revision** = explicit modify-prior-image intent (“背景换成纯白，其他不变”).
- **Freeze context**: later prompts must not rewrite metadata of images already generated.
- Separate **Generated / Edited / User Reference** — refs are context, not the deliverable image set by default.

## EggOS mapping
- Director Final room message ≈ one Base Prompt (or one Revision of the active case).
- User “sửa lại…” after a Final ≈ Revision — keep prior locks unless they override.
- Do not smash two unrelated looks into one chain (conservative mode).
- Analyst packs annotate observation; they do not invent a second Base in the room.

## Not this skill
Installing/running the Chrome extension; Eagle localhost API; ChatGPT DOM scraping.
