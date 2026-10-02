# 12 CONTROL AND DELIVERY ENGINE

This engine turns an approved brief into a bounded, reversible generation run and a truthful delivery package. It separates authored intent from generator feasibility and keeps successful layers stable during iteration.

## 1. Control contract

Before generation, create a `control_contract` with:

- one objective and the controlled axes;
- ownership by dimension;
- invariant and preservation levels (`SEMANTIC`, `STRUCTURAL`, or `PIXEL_EXACT` only when tested);
- allowed dependent changes;
- hard gates linked to explicit acceptance checks;
- unresolved questions and stop conditions.

The requested edit must be singular at the causal level. “Change material” may permit dependent highlight or contact-shadow changes; it does not permit an unrequested identity, pose, crop, or world rewrite.

## 2. Runtime boundary

The task packet selects one registered generator profile. The profile supplies only supported capability facts and operational settings: model ID, quality, size, output format, background, reference count, and error handling. Unknown or untested capabilities remain labeled as such.

Use the actual session tool or API surface according to its advertised schema and the selected matching profile. Do not infer edit fidelity, streaming, or live availability from a model name or from an analyst report alone.

## 3. Iteration state machine

`BRIEFED → ANALYZED → DIRECTED → COMPILED → GENERATED → QA_REVIEW → ACCEPTED | RETRY | STOPPED`.

Each transition stores the input hashes, prompt/settings, result IDs, evidence records, and acceptance decision. A retry changes one causal hypothesis or one declared coupled bundle. If the current output has a successful layer, the iteration record names it in `held_controls` and does not rewrite it without a reason. Use `changed_controls` for the causal bundle and `dependent_changes` for permitted coupled consequences.

## 4. Deterministic boundary

Machine-deterministic work includes schema validation, JSON shape, path policy, size arithmetic, file hashes, package manifests, and reproducible builds. Image generation and visual judgment are stochastic or human-reviewed unless a separate live test proves otherwise. The delivery manifest states this boundary explicitly.

## 5. Delivery contract

For an auditable DEEP/generation/release run, retain the following when applicable. Routine prompt-only tasks use the compact state and preflight in core/13_RUNTIME_ROUTER.md; no synthetic Analyst handoff, generator settings, image IDs or checksum report is required. These are internal records, not mandatory chat prose. Mark unexecuted steps NOT_RUN.

The full applicable record includes:

1. the task packet and analyst handoff;
2. the control contract and compiled prompt;
3. runtime settings and generator profile reference;
4. image/result identifiers and evidence records;
5. iteration history and QA decision;
6. checksums, package manifest, limitations, and next acceptance criterion.

The active release pointer is the only selector for runtime packages. Existing historical releases and binary outputs remain preserved. A candidate is not active until the required build, parity, identity, and regression gates pass.

## 6. Failure and rollback

On failure, record the symptom, visible evidence, likely cause, alternative cause, preserve list, acceptance criterion, and the single intervention class. Rollback may restore only files owned by the run and only when their current hash still matches the recorded resulting hash; user edits become conflicts, never silent overwrites.

## 7. Canonical interfaces

The machine-readable contracts are in `schemas/`. Human-readable templates are in `templates/`. Generator-specific settings are in `generators/`. Runtime packages are built from `Runtime_Source/` and selected canonical content, then identified by `Releases/active_release.json`.

## 8. Task and tool routing

The three semantic sections in core/00 are prompt structure. They do not force a prompt-only chat reply when the user asked for an image.

### 8.1 Intent

| User request | Action |
|---|---|
| cùng bàn / thảo luận / discuss first / 先讨论 / why cinematic / chưa viết prompt | `ANALYSIS_ONLY` with cinematic phase `DISCUSS`. DNA and optional directions. Do not compile a renderer prompt. Do not call an image tool. Quoted generate/render inside a pasted prompt is not a tool command. |
| không thảo luận nữa + chọn hướng + viết prompt; phân tích rồi viết prompt hoàn chỉnh | Current deliverable is the prompt: `PROMPT_AUTHOR`. Withdrawing discussion or finishing analysis with an explicit compile request is not still DISCUSS. |
| viết / xem / sửa prompt; show / write / edit the prompt; chọn B viết prompt; tự chọn hướng rồi viết luôn | Compile the three-section Simplified Chinese prompt and show it in chat. Do not call an image tool. Do not re-ask after a real choice or a delegated compile. |
| tạo ảnh / generate / render | Compile the prompt, then call a generate tool that is actually present in this session. On success return the real image and a short note. Show the full prompt in chat only when asked. A later “then make an image” does not authorize a tool call during the current discussion phase. Quoted “discuss” inside a generate request is not analysis. |
| chưa render / không tạo ảnh / only comment on layout | Not a generate authorization. Stay in analysis unless the user also asked to write the prompt now. |
| sửa ảnh; only change coat color; chỉnh màu, giữ nguyên ảnh | Use the target image as input to an edit tool if that tool is present. Local repair is not a cinematic rebuild. |
| Missing required brief or required input image | Ask only for the missing item. Do not generate and do not pretend success. |
| Needed generate/edit tool absent | Reply `GENERATION_BLOCKED_TOOL_UNAVAILABLE`, provide the compiled prompt for reuse, and do not claim an image was created. Host is not the generator; a Grok session without an image tool may still author a GPT Image 2.5 prompt. |
| Generation or edit call errors | Record `image_generation=FAIL`. Never substitute a prompt-only reply as success. |

### 8.2 Chat host versus generator

The chat application (Grok, ChatGPT, Claude, Kimi, Grok Build) is the assistant host. It is not the image generator.

- Do not default Grok to GPT Image 2.5.
- Do not invent model IDs, settings, or capabilities from the host name.
- Inspect tools actually present in the current session and bind generate/edit only to those tools.
- If the session tool is not a registered generator profile, use `generic-image` as a knowledge fallback, then inspect the actual advertised tool schema. Pass only accepted parameters, satisfy required fields and supply the actual reference image through the supported input mechanism. Tool names do not establish a parameter schema; never inject generic quality/size/format fields into a tool that does not expose them.
- Omit `input_fidelity`, streaming, and any untested field.

`tools/TaskToolRouter.ps1` models legacy test adapters. Its name-based parameter examples are not live capability evidence; the actual advertised session schema is authoritative.

### 8.3 Status fields (record separately)

| Field | PASS only when |
|---|---|
| `artifact_release` | Local build/validate gates for packages, packs, and ZIP actually passed. |
| `image_generation` | A real image artifact was received from the bound tool. |
| `visual_review` | That image was inspected. Do not review before the image exists. |
| `api_live_test` | A separate live API test was actually run. Native in-app generation does not prove a distinct API was tested. |

`NOT_RUN` and `BLOCKED` are honest statuses. They are not failures of artifact release.
