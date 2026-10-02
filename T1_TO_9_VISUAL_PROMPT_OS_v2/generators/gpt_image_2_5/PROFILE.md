# GPT Image 2.5 generator profile

This profile is an operational boundary for the GPT Image 2.5 family. It is not a universal visual law and it does not claim that a live request has been run.

## Registered surfaces

- `gpt-image-2.5-sunburst` — default quality/accuracy profile for complex or reference-sensitive work.
- `gpt-image-2.5-flare` — faster everyday profile when latency is the controlling trade-off.
- Image API image generation/editing surface.
- Responses API `image_generation` tool surface.

## Settings contract

Use only the settings recorded in `capabilities.json`: `quality` (`auto`, `low`, `medium`, `high`, `xhigh`, `max`), `size` (`auto`, standard dimensions, or a validated custom dimension), `output_format` (`png`, `jpeg`, `webp`), `background` (`auto`, `opaque`, `transparent`), and optional JPEG/WebP `output_compression`.

Custom dimensions must be multiples of 16, have an aspect ratio between 1:3 and 3:1, have no edge above 3840 pixels, and remain within the documented pixel-area limits. Transparent output requires PNG or WebP.

## Capability status

The model pages state that streaming is not supported for these model profiles. The general image guide documents a streaming interface for image generation, so the workspace records this as a surface/model conflict and resolves it conservatively to `NOT_SUPPORTED_ON_REGISTERED_2_5_MODELS` until a direct live probe proves otherwise.

`input_fidelity` for GPT Image 2.5 is `UNKNOWN` in this pack. A capability is never inferred from GPT Image 1/2 behavior, an analyst estimate, or an inaccessible external article.

## Compile, reference, and edit (project rules)

These are workflow decisions for this OS, not secret model internals. Official prompting guidance: assign each reference a role; describe visible requirements and preservation constraints; treat camera specifications as appearance cues, not guaranteed physical simulation; restate constraints because repeated edits can drift; choose a prompt format for maintainability, not magic syntax. Settings (`quality`, `size`, `background`, `output_format`) belong in tool arguments, not as a substitute for the three-section prompt. [SOURCE_REGISTER: OFFICIAL-PROMPTING, retrieved 2026-09-17]

If the user only names “GPT Image 2.5” for a complex reference rebuild, recommend `gpt-image-2.5-sunburst` and label it assumed/recommended. Keep an explicit user model choice. A prompt written for that target on a Grok host is still a prompt; it does not mean the host is running the model.

A rebuild prompt must be usable in another session: reference roles, final scene, invariants, change. Do not write “keep as above.” Do not ship seed/CFG/steps/image-weight from other model families. Do not paste the analysis chain, citations, or the whole cinematic JSON into the renderer.

Reference-driven new scenes use original references by role. Edits use the designated target frame. Exact identity is an inspection goal against the reference, not a pixel-identical promise. Live capability remains `NOT_RUN` until a live test exists.

## Error boundary

Record API failures with endpoint, model, HTTP/error code, retryability, moderation stage when provided, request correlation ID, and whether any output artifact was produced. A moderation block is not a generation success.
