# Generated candidate assets

These files are AI-generated production workfiles for the LinaBell Codex Pet v2 planning branch. They are allowed to be tracked under `workfiles/`.

## Current tracked previews

- `idle-row-preview.webp`: normalized eight-frame idle preview, 512x69.
- `waving-row-preview.webp`: normalized eight-frame waving preview, 512x69.
- `review-row-preview.webp`: normalized eight-frame review preview, 512x69.

The source sheets supplied in the production conversation were 1448x1086 RGBA PNG files arranged as 2 rows x 4 columns. Their alpha channels were fully opaque and their purple backgrounds required chroma-key cleanup. The tracked files here are compact review previews derived from the source sheets after frame extraction, initial purple-background removal, scale normalization and reassembly.

Frame order for each source sheet:

```text
top row:    1, 2, 3, 4
bottom row: 5, 6, 7, 8
```

## Privacy and scope

- These files are independently generated artwork, not the user's private photographic references.
- Private original reference photographs must never be committed.
- These planning assets must not be copied into the clean final submission PR.
- The final submission branch remains limited to `submission.json`, `pet.json` and `spritesheet.webp`.

## Status

The new visual family is a candidate rebaseline. It still requires motion-preview QA and explicit user approval before the remaining six standard animation rows are generated.
