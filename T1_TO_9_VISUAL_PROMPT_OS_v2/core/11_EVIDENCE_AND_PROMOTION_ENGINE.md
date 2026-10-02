# 11 EVIDENCE AND PROMOTION ENGINE

This engine governs what the workspace may claim after a visual change. A prompt, a rendered image, and an interpretation are different artifacts. None may silently stand in for another.

## 1. Evidence class and method

`evidence_class` (epistemic, required by `schemas/evidence_record.schema.json`):

- `SOURCE_FACT` — a documented fact with a locator.
- `VISUAL_OBSERVATION` — something visible in a reference or render.
- `INFERENCE` — an interpretation derived from evidence, never presented as direct observation.
- `HEURISTIC` — a scoped craft rule, not a law.
- `ASSUMPTION` — a working assumption that remains unlabeled as fact.

`evidence_method` (collection axis, optional):

- `DOCUMENTARY` — source, reference, provenance, or context document.
- `RENDER` — an image or image-set observation.
- `PROMPT` — the exact compiled input and generator settings.
- `HUMAN_REVIEW` — a rubric-based judgment that is not a pixel measurement.
- `MACHINE_CHECK` — a reproducible schema, hash, geometry, or package check.

Do not put a method value in `evidence_class`. A source claim and a render claim require separate records even when they concern the same subject.

## 2. Observation discipline

Every evidence record names:

1. the hypothesis or requested change;
2. the prediction that would support it;
3. the falsifier or failure condition;
4. fixed variables and the controlled causal bundle;
5. sample identifiers and the denominator;
6. the acceptance rule;
7. confounders, limitations, and the next test.

Use observable language: position, edge, contact shadow, value relationship, texture behavior, text accuracy, or measured pixel state. “Better”, “more cinematic”, and “looks right” are not sufficient observations without a visible criterion.

## 3. Promotion ladder

`OBSERVED` means one bounded observation. `REPEATED` means the observation survives the declared repeated samples. `TRANSFERRED` means it survives a changed but relevant context. `PROMOTED` means it is scoped to a family, workflow, or generator profile with its denominator, failure modes, and evidence links recorded.

Promotion is prohibited when the result is only a label, palette, borrowed motif, or a single lucky output. If the evidence is incomplete, use `UNTESTED`, `UNKNOWN`, or `CONDITIONAL`; never manufacture certainty.

## 4. Evidence and reference roles

Reference roles are dimension-specific: identity, pose, composition, lighting, material, environment, typography, or negative control. Each role declares whether it is `CARRY`, `LOCK`, `REPAIR`, `OPEN`, or `IGNORE`. One reference must not silently own dimensions assigned to another.

## 5. Ablation and controls

When a support source or prompt clause is claimed to matter, remove or replace only that clause and compare against a control. Record the changed axes, held axes, sample IDs, and the visible difference. If no necessary difference is observable, demote the clause to optional or remove it.

## 6. Human review boundary

Human review can evaluate semantic identity, hierarchy, material behavior, and authored distinction using a rubric. It cannot be reported as a pixel-exact pass. Pixel claims require a machine check with an explicit region, tolerance, and image hash.

## 7. Required handoff

The Analyst hands the Director an `analyst_handoff` containing observations, unresolved questions, reference roles, controlled axes, invariants, and acceptance checks. The Director returns a control contract and shot plan. The Compiler records the exact prompt and settings. QA records result IDs, failures, denominator, and the next acceptance criterion.

## 8. Scope rule

This engine is universal. GPT Image 2.5 behavior, quality, size, format, streaming, and edit limitations belong only in its generator profile and source register; they do not become universal visual laws.
