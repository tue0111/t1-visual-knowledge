# REVERSE IMAGE PROMPT LOOP (EggOS · slim)

**Status:** lab process · EggOS Director/Analyst · 2026-09-23  
**Scope:** reverse-match User Reference only (not normal Final path)  
**Mirror skill:** Grok Bot skill `reverse-image-prompt-loop`  
**Token policy:** REVERSE_LOOP-only; default 3 rounds; Analyst room-silent

# Reverse Image Prompt Loop (EggOS · slim)

## When

User reverse-matches a **User Reference** (đoán prompt / recreate / REPAIR toward ref).

Not for: Chrome extensions, second Base, Analyst writing Final, room pack dumps, or normal non-reverse Finals (use the usual Analyst pack path there).

## Roles

| Role | Who | Does |
|------|-----|------|
| **A** | Director · EggOS | One Final (`母版锁`/`分镜`/`负面`) per user room message → STOP. |
| **B** | Analyst · EggOS | One slim `REVERSE_LOOP` DM. No Final. |

Solo: A then B in one turn, labeled. No extra bots/subagents for the loop.

## Token rules (non-negotiable)

1. **Reverse mode = REVERSE_LOOP only.** No full VISUAL_CONTEXT_PACK. No separate FINAL_CHECK unless Director explicitly asks once.
2. **Default max 3 scored rounds.** Round 4–5 only if user says continue. Hard stop at 5.
3. **Analyst: silent in room** (no “pack sent”). DM Director only.
4. **1 user room message → 1 Final → STOP.** Next REPAIR Final only on the next user message.
5. Director uses the latest REVERSE_LOOP as enough advice — do not wait for a second Analyst pack the same turn.
6. Do not open craft knowledge packs unless `Change next` names that craft.
7. Keep REVERSE_LOOP short (template below). Axes = one line each, not essays.
8. ChatGPT-new: Final stays self-contained. VoxCat: one Base; REPAIR = prior locks + named deltas; User Reference ≠ Generated/Edited. Latest user correction wins.

## Round (B → A)

Count user-supplied comparison gens. Prefer User Reference ↔ Generated; else Reference ↔ Final text (`verified: false`).

```markdown
REVERSE_LOOP
Round: <n>/3 (or /5 if user extended)
Score: <0-10>
Decision: continue | stop
verified: true | false
Major differences:
- … (max 5 bullets)
Preserve:
- …
Change next:
- … (max 5 bullets)
Axes: bố cục | chất liệu | chất ảnh | hiệu ứng | bảng màu
```

**Stop:** score ≥ 8.5, or no material gain left, or hard stop.
**A on continue:** edit only `Change next`; keep `Preserve` unless user overrode. Default mode REPAIR; DIVERGE only for a new look/Base.

## Room / handoff

- Director: phone-copy Final only, then STOP. Optional one-line score note outside the prompt body if useful.
- No iteration gallery unless user asks.
- At end: best round + score + `verified` + stop reason; remaining diffs only if meaningful.
