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
- [x] Confirm all three source files are PNG containers at `1448x1086`.
- [x] Confirm their alpha channels are fully opaque and the purple background requires removal.
- [x] Confirm the three sheets share one coherent new character style.
- [x] Commit compact generated row previews to `workfiles/linabell--elio-zwd/assets/generated-candidates/`.
- [x] Record file names, roles, source layout and provenance in the generated-candidates README.
- [x] Never commit the private photographic reference images.

Tracked generated previews:

```text
workfiles/linabell--elio-zwd/assets/generated-candidates/idle-row-preview.webp
workfiles/linabell--elio-zwd/assets/generated-candidates/waving-row-preview.webp
workfiles/linabell--elio-zwd/assets/generated-candidates/review-row-preview.webp
```

## Phase R1 — split and identify frames

Frame order used for every candidate sheet:

```text
top row:    frame 1, frame 2, frame 3, frame 4
bottom row: frame 5, frame 6, frame 7, frame 8
```

### Idle

- [x] Detect and crop all eight idle silhouettes.
- [x] Verify no frame is an exact accidental duplicate.
- [x] Verify the blink sequence is ordered correctly.
- [x] Verify tail placement and body orientation remain stable.

### Waving

- [x] Detect and crop all eight waving silhouettes.
- [x] Confirm the same paw is used in frames 2 through 7.
- [x] Confirm the raised-paw poses form distinct wave beats.
- [x] Confirm frame 7 lowers the same paw and frame 8 returns to neutral.

### Review

- [x] Detect and crop all eight review silhouettes.
- [x] Confirm the clipboard remains attached in all eight frames.
- [x] Confirm no readable text appears on the clipboard.
- [x] Confirm the action reads as inspect → think → notice → confirm.

## Phase R2 — remove purple background cleanly

- [x] Build a non-destructive first-pass purple-background removal workflow for the generated sheets.
- [x] Remove the purple background family from all 24 frames.
- [x] Apply first-pass purple edge despill and clear fully transparent pixels.
- [x] Inspect fur edges on checkerboard, light and dark review sheets.

> This is the identity-gate cleanup. Final atlas transparency and hidden-RGB QA must still be repeated during Stage B7 after all 88 cells exist.

## Phase R3 — normalize runtime cells

- [x] Normalize each extracted frame to transparent `192x208`.
- [x] Keep a stable body center and foot baseline within each row.
- [x] Preserve complete ears, tail, raised paw and clipboard within bounds.
- [x] Export all 24 normalized PNG frames for QA.
- [x] Reassemble three transparent `1536x208` row images.

## Phase R4 — motion QA previews

- [x] Reassemble idle frames into a loop preview.
- [x] Reassemble waving frames into a loop preview.
- [x] Reassemble review frames into a loop preview.
- [x] Produce checkerboard, light and dark three-row contact sheets.
- [x] Confirm no exact duplicate frames in any row.
- [x] Confirm waving has the strongest action separation and a close frame-8-to-frame-1 return.
- [x] Record that idle is intentionally subtle and needs user judgment at the visual gate.

Local QA artifacts:

```text
/mnt/data/linabell_rebaseline/identity-contact-sheet.png
/mnt/data/linabell_rebaseline/identity-contact-light.png
/mnt/data/linabell_rebaseline/identity-contact-dark.png
/mnt/data/linabell_rebaseline/idle-preview.gif
/mnt/data/linabell_rebaseline/waving-preview.gif
/mnt/data/linabell_rebaseline/review-preview.gif
```

## Phase R5 — visual rebaseline gate

- [-] Show the cleaned three-row contact sheet and three loop previews to the user.
- [ ] Obtain explicit approval that the new three-sheet family replaces the old canonical production base.
- [ ] If approved, promote a neutral frame from the new family as the production grounding reference for all remaining rows.
- [ ] If rejected, preserve the generated workfiles but resume from the previously approved base.

## Phase R6 — remaining production

Blocked until Phase R5 approval:

- [ ] Generate `running-right`.
- [ ] Generate `running-left`.
- [ ] Generate `running`.
- [ ] Generate `jumping`.
- [ ] Generate `failed`.
- [ ] Generate `waiting`.
- [ ] Generate four cardinal look anchors.
- [ ] Generate the sixteen look directions.
- [ ] Assemble final atlas, repeat full transparency QA, run validation and follow the clean PR workflow.
