# LinaBell Direction B — Visual Rebaseline Tasks

> Date: 2026-07-28
>
> Branch: `feat/linabell-pet-direction-a`
>
> Companion plan: `direction-b-visual-rebaseline-plan.md`
>
> Status legend: `[ ]` not started, `[-]` in progress or blocked, `[x]` completed.

## Phase R0 — preserve source and record provenance

- [x] Receive three new `2x4` candidate sheets for `idle`, `waving` and `review`.
- [x] Confirm all three files are PNG containers at `1448x1086`.
- [x] Confirm their alpha channels are fully opaque and the purple background still requires removal.
- [x] Confirm the three sheets share one coherent new character style.
- [ ] Commit the three generated source sheets to the planning branch under `workfiles/linabell--elio-zwd/assets/generated-candidates/`.
- [ ] Record file names, roles and provenance for those generated sheets.
- [x] Never commit the private photographic reference images.

## Phase R1 — split and identify frames

For every candidate sheet, use this frame order:

```text
top row:    frame 1, frame 2, frame 3, frame 4
bottom row: frame 5, frame 6, frame 7, frame 8
```

### Idle

- [ ] Detect and crop all eight idle silhouettes.
- [ ] Verify no frame is duplicated accidentally.
- [ ] Verify the blink sequence is ordered correctly.
- [ ] Verify tail placement and body orientation remain stable.

### Waving

- [ ] Detect and crop all eight waving silhouettes.
- [ ] Confirm the same paw is used in frames 2 through 7.
- [ ] Confirm frames 3 through 6 show distinct wave beats.
- [ ] Confirm frame 7 lowers the same paw and frame 8 returns to neutral.

### Review

- [ ] Detect and crop all eight review silhouettes.
- [ ] Confirm the clipboard remains attached in all eight frames.
- [ ] Confirm no readable text appears on the clipboard.
- [ ] Confirm the action reads as inspect → think → notice → confirm.

## Phase R2 — remove purple background cleanly

- [ ] Build a non-destructive purple-background removal workflow suitable for the generated sheets.
- [ ] Remove the `#6A00FF` family background from all 24 frames.
- [ ] Clean edge spill and hidden RGB on transparent pixels.
- [ ] Verify fur edges on checkerboard, white and dark backgrounds.

## Phase R3 — normalize runtime cells

- [ ] Normalize each extracted frame to `192x208`.
- [ ] Keep stable body center and foot baseline within each row.
- [ ] Preserve full ears, tail and props within bounds.
- [ ] Export normalized transparent PNG frames for QA.

## Phase R4 — motion QA previews

- [ ] Reassemble idle frames into a loop preview.
- [ ] Reassemble waving frames into a loop preview.
- [ ] Reassemble review frames into a loop preview.
- [ ] Produce a three-row contact sheet preview for approval.

## Phase R5 — visual rebaseline gate

- [ ] Ask the user whether the new three-sheet family should replace the old canonical production base.
- [ ] If approved, mark the new family as the visual baseline for all remaining rows.
- [ ] If rejected, preserve the current work but resume from the previously approved base.

## Phase R6 — remaining production

- [ ] Generate `running-right`.
- [ ] Generate `running-left`.
- [ ] Generate `running`.
- [ ] Generate `jumping`.
- [ ] Generate `failed`.
- [ ] Generate `waiting`.
- [ ] Generate four cardinal look anchors.
- [ ] Generate the sixteen look directions.
- [ ] Assemble final atlas, run transparency QA, validation and clean PR workflow.
