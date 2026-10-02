# T1 TO 9 VISUAL PROMPT OS v2

A portable knowledge pack for designing, compiling, validating, and extending image-generation prompts.

Version: 3.2.1  
Built: 2026-09-25  
Status: canonical replacement pack; the older Project_Source_Knowledge_Pack remains untouched as archive.

[Bootstrap](BOOTSTRAP.md) · [Source and chat audit](SOURCE_AUDIT_AND_CHAT_DECISIONS.md) · [Migration map](MIGRATION_MAP.md) · [Validation report](VALIDATION_REPORT.md)

## What changed

The legacy source contained strong ideas but mixed four different roles:

- claims presented as universal laws;
- prompt assembly;
- family-specific taste;
- historical examples and repeated raw source.

Version 2 separates those roles and adds the decisions established in the current project history:

- generated image prompts are Simplified Chinese;
- every deliverable prompt uses exactly three sections: 母版锁, 分镜, 通用负面提示词;
- the T1 to 9 mark belongs inside 母版锁, never as a fourth section;
- all other text is forbidden unless the current brief explicitly overrides it;
- each album shot is a separate 分镜 block;
- co-role elements with shared function, causal behavior, and compatible ontology become one named system rather than a prop list;
- creature couture is generalized to living forms, plants, artifacts, phenomena, and metaphysical carriers;
- cross-medium images use a render-boundary contract plus an authored relationship; shared-world integration additionally requires a physical bridge;
- album variety comes from rotating axes, not swapping backgrounds.

Version 2.1 completes the operating lifecycle around that visual core:

- the manifest now catalogs every family, template, example, and task route;
- a creative-brief gate connects message, audience, context, feeling, and intended memory to visual decisions;
- a generation/debug log separates observation, diagnosis, causal-hypothesis retry with controlled coupled axes, and knowledge promotion;
- validation checks catalog completeness, strict UTF-8, template contract, and version alignment;
- platform builds publish a source fingerprint so workspace-level validation can prove freshness.

Version 2.2 adds prompt-compression discipline:

- prompt length is judged by independent decisions and role coverage, not character count;
- dense production-type terms receive explicit capture, layout, purpose, or identity jurisdiction;
- discovery, direction, and production modes make the tradeoff between emergence, variance, and portability explicit;
- a successful short prompt must reproduce across samples, subjects, and boundary ratios before becoming a reusable route.

Version 2.3 adds art-direction and synthesis discipline:

- evidence, studio heuristics, cultural readings, and generator-calibrated rules are kept distinct;
- viewing time, major masses, value architecture, figure/ground, edge ownership, rhythm, and color roles enter the decision path before surface detail;
- ambiguous/high-value briefs diverge through candidate territories before convergence;
- fusion now uses per-source context/grammar, explicit modes, default ownership or explicit co-ownership per load-bearing dimension, ratio semantics, relational invariants, hierarchized productive tension, and visible relationship/bridge evidence;
- critique separates observation, causal analysis, interpretation, evaluation, intervention choice, comparison, and lesson scope;
- retry decisions distinguish resample, local patch, system repair, concept reframe, and stop/research;
- focal length is treated with format and camera distance, catchlights obey actual sources, and palette/lighting recipes are conditional rather than universal.

Version 2.4 adds the connoisseurship layer:

- Law 16 requires at least one authored, non-interchangeable decision per design, so passing every structural check is no longer the finish line;
- concept territories are scored for distinction potential (with the cost of each difference recorded), not only for brief fit;
- the formal audit gains notan, gesture/force-axis, and edge-economy passes;
- the validator gains pre-generation pass 16, image pass 11, a Distinction module, and a "correct but anonymous" failure mode;
- in the full workspace, `Knowledge_Mindset/CONNOISSEURSHIP_AND_AESTHETIC_JUDGMENT.md` carries the L0–L5 quality ladder, the East-Asian critical apparatus (Six Laws, 笔墨， 留白/ma, yūgen, wabi-sabi, mono no aware, iki/shibui), the Western connoisseur benchmarks, and the competent-mediocrity defense.

## Fast start

For ordinary use, load:

1. [BOOTSTRAP.md](BOOTSTRAP.md)
2. the current project profile when supplied/injected; skip for a one-off task with none
3. [core/00_PROJECT_CONTRACT.md](core/00_PROJECT_CONTRACT.md)
4. [core/01_CORE_LAWS.md](core/01_CORE_LAWS.md)
5. [core/02_DECISION_WORKFLOW.md](core/02_DECISION_WORKFLOW.md)
6. [core/03_PROMPT_COMPILER.md](core/03_PROMPT_COMPILER.md)
7. [core/09_VALIDATOR_AND_DEBUGGER.md](core/09_VALIDATOR_AND_DEBUGGER.md)
8. [library/13_FAMILY_REGISTRY.md](library/13_FAMILY_REGISTRY.md)
9. one matching family file

For an album, also load [core/08_ALBUM_ENGINE.md](core/08_ALBUM_ENGINE.md).  
For references, load [core/04_REFERENCE_ANALYZER.md](core/04_REFERENCE_ANALYZER.md).  
For new families or style fusion, load [core/07_FUSION_AND_GROWTH_ENGINE.md](core/07_FUSION_AND_GROWTH_ENGINE.md).  
For mixed media, load [core/05_LAYER_REALITY_ENGINE.md](core/05_LAYER_REALITY_ENGINE.md) and [core/06_MATERIAL_SYSTEM_ENGINE.md](core/06_MATERIAL_SYSTEM_ENGINE.md).

For a persistent project, copy [templates/TEMPLATE_PROJECT_PROFILE.md](templates/TEMPLATE_PROJECT_PROFILE.md) into that project, fill only its specific decisions and overrides, and keep the core pack unchanged.

For a large or ambiguous brief, start with [templates/TEMPLATE_CREATIVE_BRIEF.md](templates/TEMPLATE_CREATIVE_BRIEF.md). Record controlled generation retries in [templates/TEMPLATE_GENERATION_LOG.md](templates/TEMPLATE_GENERATION_LOG.md).

To verify the pack after copying or editing it, run:

~~~powershell
powershell -ExecutionPolicy Bypass -File tools/validate_pack.ps1
~~~

To compile five-file deployment packs for ChatGPT Projects, Grok Projects, Claude Projects, and Kimi Projects, run:

~~~powershell
powershell -ExecutionPolicy Bypass -File tools/build_platform_packs.ps1
~~~

The generated packages are written beside this canonical folder under `Platform_Project_Packs/`. Edit canonical V2 sources, then rebuild; never maintain the compiled copies by hand.

## Directory map

~~~text
README.md                         coordinator and quick start
BOOTSTRAP.md                      portable AI startup instruction
SOURCE_AUDIT_AND_CHAT_DECISIONS.md traceability and decisions recovered from source/chat
MIGRATION_MAP.md                  legacy-to-v2 mapping
CHANGELOG.md                      pack history
VALIDATION_REPORT.md              verified build status and metrics
tools/validate_pack.ps1           repeatable structural validator
tools/build_platform_packs.ps1    deterministic ChatGPT/Grok/Claude/Kimi deployment compiler

core/00_PROJECT_CONTRACT.md       project-specific hard rules
core/01_CORE_LAWS.md              project-scoped visual operating principles and reasoning
core/02_DECISION_WORKFLOW.md      task classification and decision order
core/03_PROMPT_COMPILER.md        exact three-block Chinese output compiler + compression modes
core/04_REFERENCE_ANALYZER.md     image/reference reading and precedence
core/05_LAYER_REALITY_ENGINE.md   3D/2.5D/2D and cross-medium integration
core/06_MATERIAL_SYSTEM_ENGINE.md named material systems and entity translation
core/07_FUSION_AND_GROWTH_ENGINE.md family birth and genuine style fusion
core/08_ALBUM_ENGINE.md           series design, axis grid, arc, anti-attractor
core/09_VALIDATOR_AND_DEBUGGER.md QA, diagnosis, and causal repair ladder
core/10_NEGATIVE_ENGINE.md        tiered, targeted negative strategy

library/11_CAMERA_LIGHT_OPTICS.md operational photographic grammar
library/12_ILLUSION_MECHANISMS.md mechanism cards and physical proof
library/13_FAMILY_REGISTRY.md     family selection and precedence

families/                         canonical family definitions
families/KERNELS_*.md             locked user-approved instance definitions
templates/                        reusable worksheets and three-block skeletons
examples/                         complete Chinese prompt cases; examples never define laws
~~~

## Single-source-of-truth policy

A concept is defined once:

| Concept | Canonical source |
|---|---|
| Output language, three sections, logo policy | core/00_PROJECT_CONTRACT.md |
| Project-wide doctrines and Laws 1-16 with exception boundaries | core/01_CORE_LAWS.md |
| Decision order | core/02_DECISION_WORKFLOW.md |
| Prompt assembly and formatting | core/03_PROMPT_COMPILER.md |
| Reference handling | core/04_REFERENCE_ANALYZER.md |
| Layer behavior and medium boundaries | core/05_LAYER_REALITY_ENGINE.md |
| Named material systems | core/06_MATERIAL_SYSTEM_ENGINE.md |
| Family birth and fusion | core/07_FUSION_AND_GROWTH_ENGINE.md |
| Album construction | core/08_ALBUM_ENGINE.md |
| Validation and repair | core/09_VALIDATOR_AND_DEBUGGER.md |
| Negative strategy | core/10_NEGATIVE_ENGINE.md |
| Camera, light, DOF, atmosphere | library/11_CAMERA_LIGHT_OPTICS.md |
| Illusion mechanisms | library/12_ILLUSION_MECHANISMS.md |
| Family selection | library/13_FAMILY_REGISTRY.md |
| Family-specific DNA | the matching families/FAMILY_*.md file |
| Locked approved instances | the matching families/KERNELS_*.md file |

If two files appear to conflict, the higher authority wins:

current request/reference/latest correction > supplied current project profile > project contract > core laws > matching family > engines/libraries > formation knowledge by evidence scope > examples.

## Operating loop

1. Select one primary task/delivery mode and any routing modifiers.
2. For ambiguous/high-value work, diverge concept territories and select against the brief.
3. Decide mechanism, viewing sequence, major masses, value/space/edge/rhythm, anchor, and family.
4. Lock identity, invariant/variation, and concept DNA.
5. For fusion, assign mode, per-source context, jurisdiction/co-ownership rules, ratio semantics, organized tension, render boundary, and the intended physical bridge or non-integration relationship.
6. Decide layers, light, optics, color roles, material/process, and certainty.
7. Compile in Chinese into three sections.
8. Validate formal structure, meaning/context, physics, render budget, continuity, and formatting.
9. On feedback, choose resample, local patch, system repair, concept reframe, or stop/research.
10. Register a new family only after repeated samples, multiple structures, transfer/stress, ablation, and failure-repair evidence.

## Output contract summary

Prompt content is Simplified Chinese. Vietnamese may be used outside prompt blocks for explanation.

~~~text
【母版锁】
[stable identity, world, material, lighting language, logo rule]

【分镜】
[one shot; albums contain multiple separately copyable shot blocks]

【通用负面提示词】
[targeted shared blockers; T1 to 9 is the sole text exception]
~~~

The best prompt is not the longest. It is the one in which every layer has a justified role, every exception has evidence appropriate to its claim and ontology, and every shot belongs to the same project without becoming a clone.
