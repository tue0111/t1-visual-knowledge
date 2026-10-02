# ART & WORLD-BUILDING KNOWLEDGE BASE
## A case-derived operating system for authoring image-generation prompts
### Mindset · Structure · Visual grammar · Style library · Character DNA · World-building · Rules & locks · Workflow · Error taxonomy

> **What this file is.** A loadable knowledge base distilled from building a full multi-style comic production system (10+ style masters, 29-page two-part story, hundreds of debugged generations), expanded with the general art knowledge that made those files work. Load it into a GPT / Claude knowledge base and it becomes the "how to think and how to write" layer beneath every image prompt you author.
>
> **The one-sentence thesis:** an image prompt is not a description — it is a **contract**. Everything in this file exists to make that contract precise, layered, reusable and debuggable.
>
> **2026 scope note:** this is compatibility and case-derived prompting knowledge, not universal art theory or universal generator behavior. Brief/intent precedes world construction; mixed media may use one line/medium grammar per ontology; neutral balance, prompt order, capitals, numeric force and negative recency are calibrated hypotheses unless tested. Use `00_FORMATION_ROUTER.md` for the current authority map.

---

# PART I — MINDSET

## 1.1 The five convictions

**1. Brief and intent before world; world before character staging.** First decide what the image must do for its audience/context. Then decide what universe can carry that intent, who inhabits it, and what happens. Content-first lists often produce pasted props; world-first without a brief can produce beautiful irrelevance.

**2. Style is a worldview, not a filter.** "Make it Art Nouveau" is a filter. A real style decision answers: how does this universe build space? what is its light logic? is everything one substance or two tiers? what does it leave out? A style fully answered this way can re-skin an entire story without touching the script.

**3. Identity lives in anchors, not in rendering.** A character survives any style change if you pin: silhouette + costume color anchors + a small set of face constants + a dignity/behavior rule. Everything else (paint, cel, ink, glass) is free to change.

**4. Treat ambiguity as a production risk.** Models sometimes infer useful intent and sometimes follow an unintended reading; behavior varies by model/version/context. When a known ambiguity matters, state the visible evidence and exclusion precisely. In one case, "Silhouette of Wukong beneath the skin" produced a full cartoon monkey; the scoped repair requested a single tiny gold dot and excluded the body.

**5. Unassigned decisions invite drift; deliberate open invites useful variation.** Lock identity, safety, hierarchy, mechanism and known failures. Explicitly leave micro-gesture, incidental life or natural accident open when surprise is useful. The cure is neither omission nor infinite detail, but scoped certainty.

## 1.2 The layer model

Every finished prompt is an assembly of four independent layers. Keeping them separable is what makes a system instead of a pile of one-off prompts:

```
STYLE layer      – how it looks (line, color, material, framing, lettering)
CHARACTER layer  – who is in it (fixed DNA, per character)
LAYOUT layer     – how the page/frame is arranged (panel count, shapes, camera)
CONTENT layer    – what happens (the beat, staging, acting)
```

Change one layer without touching the others. Ten styles × one story = ten books; one style × ten stories = a series. This is the whole economics of the method.

---

# PART II — STRUCTURE: anatomy of a master file

A **master file** is a self-assembling document an AI can execute page by page. The proven skeleton:

```
§0  BATCH RUN + GLOBAL HARD RULES
    – parsing rules (how to find each page block)
    – FINAL PROMPT ASSEMBLY recipe (which blocks to concatenate, in order, per page type)
    – global hard rules (override anything softer)
    – SETTINGS (model, aspect, language, file naming, generation order)
    – RETRY map (symptom → corrective phrase to prepend)
§1  STYLE       – all visual-language blocks, each a named [BLOCK]
§2  CONTENT LOCKS – style-agnostic rule blocks (anatomy, safety, isolation, state machines)
§3  CHARACTER DNA – fixed identity per character
§4  PAGE INDEX  – table: page · title · panel count · field
§5  PAGE PROMPTS – one fenced block per page: LOCKS line, LAYOUT line, per-panel lines, Extra negative
§6  REFERENCE   – domain facts the images must respect (e.g. an anatomy reference)
§7  CONTINUITY  – one-paragraph restatement of the whole arc, page by page
```

### Why each piece exists

- **Named blocks `[LIKE_THIS]`** — the unit of reuse. A page says `LOCKS: A, B, C` and the assembler splices the full text in. Rules are written once, referenced everywhere, fixed in one place.
- **Assembly order matters**: `style → character → layout → page body → "Negative:" + shared negative + page extra negative`. Style first anchors the render; negatives last so they are freshest in context.
- **Global hard rules** exist because soft prose loses to strong priors. Anything the model *wants* to do wrong (mock faces on the wrong character, organs as a chart, amber color wash) must be stated as an override rule, numbered, at the top.
- **The RETRY map** is half the value of the file. Every discovered failure gets a one-line corrective phrase; regeneration = prepend and rerun. A master file without a retry map has not been tested.
- **PAGE INDEX + CONTINUITY** are for the *author* and the *assembler*: they catch renumbering drift, missing pages, and story contradictions before the model ever sees them.

### The lock line

Every page starts with `LOCKS: NAME, NAME, NAME.` — the page's rule manifest. Rules of hygiene: never reference an undefined lock (dangling locks silently vanish); never define a lock that nothing references; when pages renumber, re-verify every lock that mentions page numbers (state machines, escalation ladders).

---

# PART III — VISUAL GRAMMAR: the seven decision axes

Every style, and every prompt, is a setting on seven axes. Name the setting explicitly and the model follows; leave it implicit and you get the average of the internet.

## 3.1 LINE — what describes form?

| Line language | Trigger vocabulary | Belongs to |
|---|---|---|
| Iron-wire fine line | "fine even ink outlines, iron-wire line, meticulous" | Gongbi, classical Chinese |
| Brush / calligraphic | "confident tapering brushstrokes, wet edges, dry-brush" | Ink-wash, sumi-e |
| Whiplash organic | "sinuous tapering whiplash contour, ornamental line" | Art Nouveau |
| Carved / woodcut | "bold carved outlines, slightly tapering, print edge" | Ukiyo-e, linocut |
| Variable-width ink | "bold outer contours, finer interior lines, spotting of black" | American comic, DC noir |
| Cel / animation | "thick clean confident edges, flat interior fills" | Cartoon Network, retro cel |
| Leading (came) | "bold black leading bounds every pane" | Stained glass |
| Screentone + hatch | "fine cross-hatching, halftone screentone gradients" | Seinen manga |
| Lineless / painterly | "forms defined by light and shadow, not outline" | Cinematic manhwa, painterly |

**Starting principle:** one line/edge owner per render domain. Multiple line languages are valid when ontology boundaries and physical bridges are explicit; silent mixing inside one domain often creates the pasted-sticker artifact.

## 3.2 SHAPE & SILHOUETTE — what makes things readable?

- **Silhouette first**: a character or organ must be identifiable as pure black shape. Prompt with "strong silhouette", "recognizable silhouette", "correct silhouette" — the model treats silhouette words seriously.
- **Shape hierarchy**: one big shape, few medium shapes, sparse small shapes. Flat/graphic styles live and die by this.
- **Negative space is a shape.** Deliberately empty area is what makes epic-empty styles (Tartakovsky) and poetic styles (ink-wash 留白) work: "generous negative space", "misty unpainted breathing space".
- **Scale contrast tells stories without words**: "a tiny figure against an enormous simple plane" is the cheapest awe available.

## 3.3 VALUE & LIGHT — what carries the mood?

| Light logic | Prompt formula | Effect |
|---|---|---|
| Single key light | "ONE dominant key light per panel; deep controlled shadow; rim light separates subject" | Cinematic intimacy |
| Noir shaped shadow | "hard key light with deep SHAPED shadow masses; geometry echoed in the shadows" | Weight, menace, prestige |
| Flat graphic shadow | "hard-edged FLAT shadow shapes, no gradients, no rendering" | Animation crispness, stability |
| Cel tones | "2-3 tone cel shading, crisp hard-edged shadow shapes, few clean highlights" | Classic comic |
| Tone/hatch | "volume from cross-hatching and screentone, not color" | Manga documentary realism |
| Backlit / glow | "translucent panes glow as if backlit; the glow is the light source" | Stained glass, holograms, X-ray windows |

**Two case-derived heuristics:**
1. **Value can carry mood without a global color cast.** This is a useful repair for unwanted amber wash, not proof that color cannot carry affect.
2. **Shadow can simplify.** "Let shadow hide detail; render fully only where light lands" is useful for some low-key systems; high-key, flat, luminous and diffuse-light worlds need different simplification devices.

## 3.4 COLOR — discipline, not decoration

- **Neutral white balance as a scoped guard.** Use "a white or pale element reads clean-neutral" when the project is fighting unwanted amber/gold drift. Colored illumination, adaptation and expressive grading remain valid when motivated.
- **Local color vs frame color — case guard.** When fighting unwanted cast, say that a costume's mustard-yellow is controlled local color and does not license a global yellow cast. Motivated colored illumination or expressive grading may legitimately affect the frame.
- **Palette roles before quantity.** Three to five named colors plus ground/accent can be a productive constraint. Test field, support, anchor, accent and neutral bridge in context; pigment specificity is a generator hypothesis and must not replace cultural/material research.
- **One anchor color per protagonist** (the Princess's jade-green) gives every page a consistent chromatic center.
- **Proven palette families:** teal-and-gold (cinematic), ink-black/jade/indigo + local gold (dark-deco), desaturated teal/ochre/brick/cream (retro), mineral jewel tones (gongbi), monochrome + one spot color (ink-wash), muted sage/rose/mauve/cream (Mucha), backlit jewel glass (leadlight), indigo/vermilion/moss on washi (ukiyo-e).
- **Liquids — generator/case guard:** in the observed project, unspecified liquid often rendered amber/cloudy. Use "clear pale near-white semi-transparent" only when that is the intended substance; amber, milky, opaque or colored liquids remain valid when the brief requires them.

## 3.5 COMPOSITION & CAMERA

- **Panel shape IS storytelling**: narrow verticals = descent/gaps; round panels = reflections/lenses; jagged edges = flashback; borderless bleed = impact; full-page splash = the one showstopper per act.
- **Layout grammar for a page**: name the grid exactly — "a WIDE establishing panel across the top; a 2-up tier below (P2 … | P3 …); a lower 2-up tier". The model obeys layout lines shockingly well *if* panel count is stated and repeated ("exactly N panels").
- **Density rhythm**: action/dialogue pages = dense mosaics; awe/interior pages = FEW LARGE immersive panels. Alternate to control pacing.
- **Reading order** must be declared when non-default (right-to-left manga) and protected ("clear unambiguous reading order").
- **Camera depth**: "camera deep inside, enclosed, surrounded on all sides AND overhead" versus "high-angle establishing" — placement words do more than lens words.
- **Progressive reveal across panels** (same subject, deeper each panel — e.g. X-ray skin → bone) is a powerful two-panel structure; the key phrase is "the SAME window/subject, a progressive DEPTH reveal."

## 3.6 MATERIAL — the substance contract

The single biggest style decision: **is the page ONE material or TWO tiers?**

- **Unified**: "ONE unified [material] for the whole page — characters, world AND [special content] all share the same [line/fill/shadow], so nothing looks pasted." Maximum cohesion; the default.
- **Two-tier**: a deliberately stylized guest inside a differently-rendered world ("a flat cartoon hero on a hyperreal stage"). Powerful contrast, but it must be *declared as intentional* and glued together by shared lighting: "still lit by the scene — matching cast shadow and ambient — so he sits in the space; his DESIGN stays cartoon."
- Every material has a texture vocabulary: silk + mineral pigment; rice paper + graded ink; backlit glass + black came; washi + carved edge + bokashi; cel + flat fill; digital ink + halftone. Name the *support* (silk, paper, cel, glass), not just the look.

## 3.7 DETAIL BUDGET — where the model's attention goes

Attention is finite. Say where to spend it, and say where NOT to:
"Concentrate detail on (1) the heroine's face, (2) the anatomically-correct focal structure, (3) the page's hero panel. Simplify everything else into [this style's simplification device: shadow / negative space / flat shape / mist]. One focal subject per panel. No noise, no clutter."
Every style needs its named simplification device — that is what keeps generation stable.

---

# PART IV — STYLE LIBRARY

Each entry: worldview → line → color → signature device → chief negative (what it must never drift into). These are compressed, working recipes; expand any into a full §1 with the 12-block template in Part II.

### Built and battle-tested

1. **Cinematic Manhwa (painterly)** — a world lit by one light. Painterly, form-from-light; neutral-balanced teal; device = atmospheric haze + rim light; never: flat sticker characters, amber wash.
2. **Cinematic Art-Deco Xianwuxia** — myth staged as design. Semi-real gloss + flat deco ornament; teal-and-gold; device = moon-disc/bamboo symmetric backdrops + English SFX lettering; never: clutter, photoreal plastic.
3. **Organ Atlas** — the world as a curated gallery. Hyperreal environment + semi-real figures; device = bilingual deco LABEL CARDS (dark-teal plaque, gold leader line, big CJK + small EN, 2–4 per page, never covering the figure); never: chart-like labeling, mislabels.
4. **Dark-Deco DC / Vertigo** — grave inked reality with a toon guest. Variable-width ink + noir shaped shadow; ink-black/teal/indigo + local gold; device = the two-tier toon-in-real-world contrast + thin gold deco borders; never: toon world, photoreal guest.
5. **Dark-Deco Cartoon Network (Tartakovsky)** — epic-empty graphics. Thick clean edges, flat fills, hard flat shadow; limited dark-deco palette; device = monumental negative space + scale contrast; never: gradients, rendering, realism.
6. **Retro 1990s Cartoon (Bruce Timm × Samurai Jack)** — timeless noir-deco serial. Retro cel, 1–2 tone shadow; desaturated teal/ochre/brick/cream + film grain; device = vintage serial nostalgia; never: modern webtoon flatness, anime eyes.
7. **American Modern Comic** — grounded kinetic inked reality. Variable-width ink + 2–3 tone cel; bold neutral-balanced color; device = speed/impact lines + plain black gutters (no decoration!); never: manga tone, deco framing.
8. **Modern Seinen Manga** — near-monochrome documentary. Ink + hatch + screentone; color subordinate to line; device = tone-built atmosphere, slanted gutters, R-to-L; never: decoration of any kind, moe eyes.
9. **Ultra-Realistic Cinematic** — photoreal filmic. Device = physically-plausible light; never: outlines, cel, illustration tells.
10. **Dark-Deco Minimalism** — the world reduced to a poster. Few flat shapes, huge negative space, neutral balance as first law; device = subtraction itself; never: texture, noise, detail creep.
11. **Gongbi silk-scroll (工笔)** — the court painter's jeweled record. Iron-wire line + layered mineral pigment + gold on silk; device = bare-silk negative space + gold detailing; never: looseness, western comic tells.
12. **Ink-wash xianxia (水墨)** — the poem in mist. Brush + graded wash, near-mono + ONE spot color; device = 留白 breathing emptiness; never: hard outlines everywhere, saturated color.
13. **Art Nouveau / Mucha** — the beauty enthroned in ornament. Whiplash line, muted jewel tones; device = halo-arch + botanical border; never: geometric deco confusion, gaudiness.
14. **Stained glass / cloisonné** — the story as a cathedral window. Black leading + backlit glass panes; device = glow-from-within (weaponize it for scan/X-ray/holy moments); never: crude leading, architectural mullions inside organic forms.
15. **Ukiyo-e woodblock (浮世絵)** — the floating-world print. Carved bold outline + flat traditional pigment + bokashi; device = Hokusai wave-curl patterning + cartouche insets; never: modern manga tells, gongbi confusion.

### Expansion shelf (recipes ready to develop)

16. **Moebius / ligne claire** — uniform clean line, flat luminous color, surreal organic vistas; the master key for "interior as an alien planet." Never: heavy shadow, ink noir.
17. **Gouache storybook (mid-century)** — matte opaque brush, soft flat planes, warm; friendly/教育 tone. Never: gloss, digital gradients.
18. **Risograph / spot-color print** — 2–3 ink layers, visible halftone grain, slight mis-registration charm, one fluoro accent. Never: full-color smoothness.
19. **Watercolor & line (Euro album)** — loose transparent washes over firm ink; sunlit, humane. Never: opaque digital fill.
20. **Oil-painting classical** — impasto light, glazed shadow, museum gravity; for "old master" one-offs.
21. **Gothic engraving (Doré)** — dense parallel-line etching, dramatic divine light; for epic dread.
22. **Paper-cut / silhouette theatre** — layered card shapes, backlit rims (Lotte Reiniger); for prologue/legend pages.
23. **Pixel / mosaic** — deliberate grid quantization; for meta or retro-game framings.
24. **Blueprint / technical plate** — white line on cyan, annotated; a cousin of the atlas style for schematic beats.
25. **Chalk & blackboard** — for didactic/comic-relief diagram pages.

**Combinatorics note:** styles fuse best when you take *structure from one, surface from another* (deco framing + xianxia painting; atlas labels + any style; glass glow + noir layout). Declare the fusion explicitly in the STYLE_HEADER — "X FUSED WITH Y" — and give each element its jurisdiction.

---

# PART V — CHARACTER BUILDING: the DNA method

## 5.1 The DNA block

For each recurring character, one paragraph that never changes, pasted into every file:

```
[NAME native-script/latin] role/archetype; SILHOUETTE note; COSTUME with 3-4 exact color anchors;
FACE constants (eye shape, one distinguishing mark, lip/skin notes); HAIR + one signature accessory;
BEARING (posture/dignity rule); consistency clause ("same recognizable face every page");
hard negatives ("never chibi, never photoreal, never X").
```

The costume anchors are the real identity carriers across styles — pick colors that survive any palette (mustard robe / azure sash / deep-blue trousers / tarnished-gold circlet has survived fifteen styles).

## 5.2 Rules that keep characters alive

- **One-per-panel law.** "One X per panel, no clones, no motion duplicates" — image models love to multiply a moving figure. Freeze action at ONE apex pose: "frozen at the clean apex of ONE somersault; one body, no clone."
- **Dignity/casting locks.** Behavior is identity. If a character must never be undignified, write a lock that (a) forbids the behavior AND (b) *assigns it to someone else*: "the one who taunts is a MAID, NEVER the Princess; the Princess presides." Giving the model an approved outlet works far better than prohibition alone.
- **Accessory state tracking.** Anything wearable that changes with the story (a hairpin that falls at the surrender) needs its own lock with explicit page ranges and a default: "if her hair shows, the pin is still in… gone only from P25, never restored."
- **Beauty budget.** If a face is the emotional anchor, say it economically: "top detail budget on her face; consistent recognizable face; dignified and beautiful even in defeat."
- **Scale forms.** A character who changes size/form needs a MODE system: "MODE A micro-silhouette (vistas) · MODE B tiny 2–3 cm humanoid (medium shots) · MODE C insect form (when a humanoid would be unreadably small). Never enlarge for readability."
- **Transformation beats** must be staged in steps and mutually exclusive: "near the lip he resolves into ONE fly in a clear transformation beat; never show both forms at once after the transform resolves."

## 5.3 Expression & acting

Prompt acting through body + face verbs, not emotion nouns: "she braces one hand on the table, teeth clenched, breathing rougher" beats "she is in pain." Reserve emotion nouns for the negative list ("never grotesque, never dead-eyed"). For reactions to unseen causes, forbid the cliché visualizations: "the voice is HEARD, not drawn — no sound rays, no ripples, no glowing belly."

---

# PART VI — WORLD-BUILDING: the seven questions

Answer these seven, in order, and a style/world is fully specified (this is the checklist behind every §1):

1. **What kind of universe is this?** Its emotional register *before any character enters* (mythic-ceremonial, epic-empty, grave-noir, nostalgic-serial, quiet-documentary, jeweled-court, misty-poem, radiant-sacred…). One phrase, first line of the STYLE_HEADER.
2. **How is space built?** Architecture and perspective? Silhouette + flat planes + negative space? Overlapping lit forms receding into shadow? Display space with a centered exhibit?
3. **What is the light logic?** Pick from §3.3 and commit.
4. **One substance or two tiers?** The material contract (§3.6). Declare it.
5. **Ornament or restraint?** Does this world *want* borders, halos, label cards, cartouches — or plain black gutters and silence? (Both are strong; mixing them weakly is what looks cheap.)
6. **Where does the camera live?** Filmic depth, poster frontality, print flatness, window reverence?
7. **What is the texture density?** And what is the named simplification device that absorbs everything you don't detail?

**Interiors / special realms** (a body interior, a dream, an underworld) get the same seven questions PLUS enclosure physics: sealed on all sides including overhead; depth = overlapping soft structures, never open horizon; forbidden concepts listed by name (cave, rock, stalactites, night sky, void, museum display). A fantastic place stays believable when its *boundaries* are strict.

---

# PART VII — RULES & LOCKS: the control system

The lock taxonomy that emerged, generalized — build these seven kinds for any project:

1. **Accuracy locks** (domain truth): "every organ anatomically correct — correct shape, side, position, relative size, neighbors; stylize the RENDERING, never the ANATOMY." Pair with a §6 reference the assembler can consult. Works for anatomy, architecture, machinery, heraldry, uniforms…
2. **Containment locks** (space integrity): sealed interiors, panel isolation ("each panel is a sealed cell; no background leakage, no object migration, no palette bleed between panels").
3. **Safety/taste locks**: intact healthy tissue, no gore, no nudity, tasteful clinical treatment of the body, all characters adults. State them positively where possible ("a plain form-fitting underlayer may cover the area") — an allowed alternative beats a bare prohibition.
4. **State machines** (continuity over a sequence): a per-page table of a character's state ("P18 upright, 0% → P22 on her knees → P25 surrender, hairpin gone, 100%") plus hard floor rules ("no kneeling before P22"). This is THE tool for emotional arcs across generated pages.
5. **Escalation ladders** (plot physics): the permitted order of events, with "never jumps ahead."
6. **Cause-effect ordering**: "internal cause appears BEFORE the external reaction; never reverse."
7. **Stop conditions**: "the instant she surrenders, he stops immediately — this overrides every earlier escalation instruction." Any prompt system that ramps intensity needs an explicit brake.

**Negative prompt design:**
- Two levels: a SHARED_NEGATIVE (style + universal failures, appended to every page) + a per-page "Extra negative" (this page's specific temptations).
- Negatives are *harvested from real failures*, not imagined: every bad generation contributes its named artifact ("cartoon monkey in the window", "featureless blob", "smooth crotch blob", "Princess enthroned", "two flies").
- Ban categories AND their look-alikes: "cave, rock wall, stone texture, straight sharp lines, stalactites" — five words to keep an interior organic.
- When a positive keeps failing, check whether one of your own words is the saboteur (the "silhouette" incident). Rewrite the positive with the exact desired pixels, then add the misreading to the negative.

**In-image text policy:** default NO text; carve explicit exceptions (ONE bold SFX word ≤8 letters; label cards with exact content rules). Always include the fallback: "if text renders garbled, keep the empty frame/balloon and add words in post." Non-ASCII (Vietnamese diacritics, CJK) garbles often — plan for post-production.

---

# PART VIII — WORKFLOW: from idea to shipped pages

## 8.1 The build sequence

1. **Spine first (no style).** Write the story as a style-neutral SPINE: beats → pages → panels, with locks and layout lines but zero rendering words. This is the single source of truth.
2. **Answer the seven world questions** → draft §1 as 12 named blocks (HEADER, RENDER_LAW, LINE, COLOR, WUKONG-equivalent, ORGANS-equivalent, BEAUTY, CAST, LAYOUT, DETAIL, SFX, NEGATIVE).
3. **Assemble the master** = spine + style + DNA + assembly recipe. Every page body stays style-agnostic except a single `__SCENE__`-type flavor word.
4. **Dry-read as the model.** For 3 sample pages, mentally concatenate the full assembled prompt. Look for: contradictions between locks, words with two readings, unstated liquids/backgrounds/light.
5. **Generate a probe set** (first page, one interior, the hardest page). Harvest failures → RETRY map + negatives.
6. **Batch generate** in story order (earlier pages inform later regenerations).
7. **Audit pass** (see 8.3) before declaring done.

## 8.2 Error taxonomy (observed, with cures)

| Symptom | Root cause | Cure |
|---|---|---|
| Global amber/sepia wash | "warm/golden" mood words; unspecified liquids | Neutral-balance law; warmth local-only; liquids "clear pale" |
| Character multiplied / motion clones | Action described as movement | ONE apex pose, "one body, no clone, no motion duplicates" |
| Pasted-sticker character | Material/light contract unstated | Unified-material clause, or two-tier + shared lighting |
| Vague cloud where detail expected | Positive too abstract ("reveals a shape") | Name literal content: "a REAL radiograph: HIP BONES + SACRUM; a single tiny gold dot" |
| Wrong subject fills an inset | An identity word ("silhouette of X") | Replace with exact desired pixels; ban the misreading |
| Interior becomes a cave/void | Model's cavern prior | Containment lock + ban cave/rock/stalactites/void/sky by name |
| Organs like a medical chart | "Anatomy" pulls textbook imagery | "no medical chart, no labels, no collage; embedded, enclosed, alive" |
| Character does off-role acting (mocking queen) | Archetype prior | Casting lock + assign behavior to an approved character |
| Emotional beat fires early | No sequence physics | State machine + floor rules + escalation ladder |
| Ornament everywhere / kitsch | "decorative" unbounded | Jurisdiction: where ornament lives, where it never goes; "elegant, never cluttered" |
| Text garbled | Non-ASCII, long strings | ≤8-letter SFX; empty-frame fallback; post-production plan |
| Wrong panel count | Layout under-specified | "exactly N panels" + named grid + count repeated in LAYOUT line |
| Style bleed between variants | Copy-paste inheritance | Grep for donor-style vocabulary after every derivation; keep a per-style signature word list |

## 8.3 The audit checklist (run before shipping any multi-page master)

- Page numbers contiguous; index table = page headers; generate-line = last page.
- Every `LOCKS:` reference has a definition; no orphan definitions.
- All page-number-bearing locks (state machines, ladders, accessory locks, "from Pxx on") re-verified after ANY renumbering.
- Cross-file continuity: part boundaries ("ended at P17"), handoffs, shared props' first-appearance pages.
- No donor-style vocabulary in a derived file (grep the signature words).
- Negatives present on every page; shared negative appended by the assembly recipe.
- Story-facts audit: does any DNA/lock contradict the current script? (The fan that "appears from P24" when its page moved to P26.)

---

# PART IX — PROMPT MECHANICS: the sentence-level craft

- **Front-load the frame:** medium + genre + aspect + quality register first ("X-style graphic-novel page, 2:3 vertical, premium quality"), then style clauses, then content.
- **CAPITALS as a generator hypothesis.** Used sparingly, capitalization may improve human parsing or some generator runs, but its weighting effect must be tested by model/version rather than claimed as universal.
- **State the positive, then fence it:** every critical instruction = wanted thing + the specific unwanted readings ("STANDING and dignified — NOT kneeling, NOT kowtowing, NOT praying, NOT prostrate"). Enumerate the failure poses; the model knows them all.
- **Repeat across levels, not within them.** A rule appears once in §0 (law), once as a lock (reusable), once in the page body (application) — that triple-echo is reinforcement; repeating a sentence twice in one place is noise.
- **Numbers can reduce ambiguity:** use them when the generator and task can represent the measurement or count; verify obedience rather than assuming numeric force.
- **"Same X every panel/page"** is the consistency spell: same window, same woman, same fly icon, same face. Use SAME in caps when panels must share a subject.
- **Choreograph with spatial verbs** (looms, recedes, overhangs, dwarfs, encloses, spans) — they place things; adjectives only decorate them.
- **Per-panel prefixes** ("P1 (STOMACH only): … P2 (HALL only): …") plus an isolation lock is what keeps multi-panel pages from cross-contaminating.
- **Keep targeted negatives in the designated final section for this project's contract.** Claims that the most recent token is most binding remain generator/version hypotheses.

---

## CODA — the ten commandments, if you keep nothing else

1. Brief/intent first; then world, character staging and content execution.
2. One style = seven answered questions, written as twelve named blocks.
3. Identity = silhouette + color anchors + face constants + a dignity rule.
4. Declare the material contract: unified, or two-tier glued by light.
5. In this case system, value carried mood while local warmth and clear pale liquid guarded against amber drift; other systems may use colored light, tint or different liquids intentionally.
6. Say where detail goes AND name the simplification device that eats the rest.
7. Locks over prose; state machines over hope; a brake on every escalation.
8. Every failure becomes a negative or a retry line — the file must learn.
9. Quantify, capitalize the load-bearing words, enumerate the failure poses.
10. Audit numbers, locks and continuity after every edit — drift is the silent killer.

---

*Art & World-Building Knowledge Base — distilled from the Family-Y multi-style production system as compatibility/case knowledge. Load through the formation router; current core, sourced foundations and scoped calibration evidence define the boundaries.*
