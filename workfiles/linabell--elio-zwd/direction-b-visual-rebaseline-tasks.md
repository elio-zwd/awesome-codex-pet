# LinaBell Direction B — Visual Rebaseline Tasks

> Date: 2026-07-28
>
> Branch: `feat/linabell-pet-direction-a`
>
> Companion plan: `direction-b-visual-rebaseline-plan.md`
>
> Status legend: `[ ]` not started, `[-]` in progress or blocked, `[x]` completed.

## Phase R0 — preserve source and record provenance

- [x] Receive generated candidates for `idle`, `waving` and `review`.
- [x] Confirm the initial three source files are PNG containers at `1448x1086` with opaque purple backgrounds.
- [x] Commit compact generated previews and provenance notes under `workfiles/`.
- [x] Permit generated workfiles in the planning branch.
- [x] Never commit private photographic reference images.

## Phase R1 — split and identify frames

Frame order for the original `2x4` candidates:

```text
top row:    frame 1, frame 2, frame 3, frame 4
bottom row: frame 5, frame 6, frame 7, frame 8
```

### Idle

- [x] Extract eight frames.
- [x] Verify ordered blink sequence, stable tail side and body orientation.
- [x] Confirm no exact accidental duplicate.

### Waving

- [x] Extract eight frames.
- [x] Confirm one consistent waving paw and a raise-wave-lower sequence.
- [x] Confirm frame 8 returns close to neutral.

### Review — replacement history

- [x] Extract and process the first new review candidate.
- [x] Detect, after user inspection, that its review frame 4 contains an extra third paw.
- [x] Reject the defective processed review row; do not reuse it in the final atlas.
- [x] User selected **image 1** as the replacement source.
- [x] Record the selection in `assets/generated-candidates/review-image1-selection.md`.
- [x] Use only image 1’s third row as the replacement eight-frame `review` family.
- [x] Preserve the approved `idle` and `waving` rows unchanged.
- [x] Confirm the image 1 replacement has one clipboard-holding paw and at most one free paw per frame; no visible third paw.
- [x] Confirm the clipboard remains present and contains no readable text.

## Phase R2 — background cleanup

- [x] Remove the purple backgrounds from the original identity rows.
- [x] Remove image 1’s dark studio background from the replacement review frames by connected-background segmentation.
- [x] Apply first-pass edge feathering, background-color unmixing and transparent-pixel cleanup.
- [x] Inspect replacement Review on checkerboard, light and dark backgrounds.

> Full hidden-RGB and edge QA must be repeated after all 88 cells exist.

## Phase R3 — normalize runtime cells

- [x] Normalize all approved identity frames to transparent `192x208` cells.
- [x] Keep feet near y=203 with stable body registration.
- [x] Preserve full ears, tail, waving paw and clipboard.
- [x] Reassemble transparent `1536x208` rows.
- [x] Replace the local Review QA row with the image 1 third-row extraction.

## Phase R4 — motion QA previews

- [x] Reassemble Idle and Waving previews.
- [x] Rebuild Review preview from image 1.
- [x] Rebuild checkerboard, light and dark three-row contact sheets.
- [x] Confirm the old third-paw Review preview is superseded.

Updated local QA artifacts:

```text
/mnt/data/linabell_image1_final/review-row-image1.png
/mnt/data/linabell_image1_final/review-preview-image1.gif
/mnt/data/linabell_image1_final/identity-contact-sheet-image1.png
/mnt/data/linabell_image1_final/identity-contact-light-image1.png
/mnt/data/linabell_image1_final/identity-contact-dark-image1.png
/mnt/data/linabell_image1_final/processing-report-image1.json
```

## Phase R5 — visual rebaseline gate

- [-] Show the updated contact sheet and image 1 Review preview to the user.
- [ ] Obtain explicit approval that `idle`, `waving` and the image 1 `review` row replace the old canonical production base.
- [ ] After approval, promote a neutral frame from the new family as the grounding reference for remaining rows.

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
- [ ] Assemble the final atlas, repeat transparency QA, run validation and follow the clean PR workflow.
