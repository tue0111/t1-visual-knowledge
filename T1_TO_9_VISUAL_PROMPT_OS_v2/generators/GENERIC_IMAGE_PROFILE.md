# Generic image generator profile

All registered image generators expose the same project boundary: a task packet, dimension-specific reference roles, a control contract, explicit runtime settings, evidence records, and a delivery manifest. Model-specific capabilities are loaded from the selected profile and never generalized from a neighboring model.

The GPT Image 2.5 registration is in `generators/gpt_image_2_5/`. Its capability claims are source-linked, while live generation and input-fidelity behavior remain explicitly untested in this workspace.

When the requested model or surface is not a registered 2.5 profile, use `generators/generic/capabilities.json` (`generic-image`). That fallback is executable: only `quality=auto`, `size=auto|1024x1024`, `output_format=png`, and no streaming/input_fidelity. It is not a claim that the unknown tool equals GPT Image 2.5.

A chat host is not a generator. Grok, ChatGPT, Claude, Kimi, and Grok Build do not inherit the Sunburst default. If the session exposes `image_gen` / `image_edit` (or another unregistered tool), stay on this generic fallback and pass only parameters that tool actually accepts.
