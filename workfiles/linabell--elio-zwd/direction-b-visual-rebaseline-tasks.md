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
- [ ] Keep the uploaded source sheets outside the final pet directory.
- [ ] Decide whether production copies should be committed to the planning branch after user approves the new visual baseline.
- [ ] Never commit the private photographic reference images.

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
- [ ] Confirm the clipboard remains present in all eight frames.
- [ ] Confirm clipboard size, side and clip design remain consistent.
- [ ] Confirm the free paw performs the inspect/think/verify actions.
- [ ] Confirm the sequence reads as one workflow rather than eight unrelated poses.

## Phase R2 — create true transparency

- [ ] Measure representative purple-background samples from corners and gaps.
- [ ] Build a color-distance background mask.
- [ ] Restrict removal to edge-connected background regions.
- [ ] Preserve similar pink/red pixels inside fur, skirt, cherries and clipboard.
- [ ] Refine anti-aliased boundary pixels.
- [ ] Remove purple spill from semi-transparent edge pixels.
- [ ] Clear RGB values under alpha-zero pixels.
- [ ] Check every frame on checkerboard.
- [ ] Check every frame on dark background.
- [ ] Check every frame on light background.
- [ ] Reject and repair any purple fringe or body transparency hole.

## Phase R3 — normalize to runtime cells

- [ ] Establish one shared silhouette scale target for all 24 frames.
- [ ] Fit every frame into `192x208` without non-uniform scaling.
- [ ] Preserve safety margin above ears and around tail and paws.
- [ ] Align feet to a common baseline within each row.
- [ ] Align body centers while allowing action-specific paw movement.
- [ ] Confirm no ear, hat, paw, clipboard, skirt, foot or tail is cropped.
- [ ] Export 24 transparent working PNG cells.

## Phase R4 — motion QA

### Idle preview

- [ ] Assemble the eight normalized idle cells into preview order.
- [ ] Play `1 -> 8 -> 1` at several practical frame intervals.
- [ ] Confirm a readable non-blink micro-motion exists.
- [ ] Confirm no baseline jitter or scale pulse.
- [ ] Confirm frame 8 closes naturally to frame 1.
- [ ] Repair only local frames when identity remains coherent.

### Waving preview

- [ ] Assemble the eight normalized waving cells into preview order.
- [ ] Confirm one-paw continuity.
- [ ] Confirm outward/inward motion is readable at `192x208`.
- [ ] Confirm no paw-face overlap or limb detachment.
- [ ] Confirm frame 8 closes naturally to frame 1.

### Review preview

- [ ] Assemble the eight normalized review cells into preview order.
- [ ] Confirm the clipboard remains attached and blank.
- [ ] Confirm ready/inspect/point/think/notice/verify/approve/reset semantics.
- [ ] Confirm thinking and satisfied expressions remain readable at pet size.
- [ ] Confirm frame 8 closes naturally to frame 1.

## Phase R5 — rebaseline approval package

- [ ] Assemble transparent `idle`, `waving` and `review` one-row strips.
- [ ] Assemble a three-row contact sheet.
- [ ] Produce an animated preview for each of the three rows.
- [ ] Present all four review assets to the user.
- [ ] Obtain explicit approval that this new family replaces the old canonical visual base.
- [ ] If rejected, record consolidated corrections before any regeneration.
- [ ] Do not begin the remaining six standard rows before approval.

## Phase R6 — promote the new canonical base

Run only after Phase R5 approval.

- [ ] Select the cleanest neutral idle frame as the new canonical production base.
- [ ] Verify the selected frame at native size and `192x208`.
- [ ] Replace the planning-branch production copy at `assets/canonical-base.webp`.
- [ ] Update `canonical-base-qa.md` with the new visual anchors and dimensions.
- [ ] Update `handoff-state.json` to `visual-rebaseline-approved`.
- [ ] Record which source frame became canonical.
- [ ] Mark the old canonical base as superseded for future generation grounding.

## Phase R7 — remaining standard animations

Generate, extract, normalize and preview one row at a time.

### Running-right

- [ ] Generate eight coherent frames.
- [ ] Verify alternating foot contacts and tail counterbalance.
- [ ] Verify no speed lines, dust or floor shadow.
- [ ] Obtain row-level visual approval.

### Running-left

- [ ] Generate separately or repair a mirrored source consistently.
- [ ] Keep the hat flower on the canonical character side.
- [ ] Verify foot sequence is directionally correct.
- [ ] Obtain row-level visual approval.

### Running

- [ ] Generate a forward/run-in-place cycle distinct from side-running rows.
- [ ] Verify limited body bob and stable center.
- [ ] Obtain row-level visual approval.

### Jumping

- [ ] Generate neutral, crouch, launch, rise, apex, descend, land and recover frames.
- [ ] Verify the character remains fully inside every cell.
- [ ] Verify no shadow, dust or impact effect.
- [ ] Obtain row-level visual approval.

### Failed

- [ ] Generate readable mild disappointment and recovery.
- [ ] Keep any tear attached and avoid punctuation/icons.
- [ ] Verify the state is not visually confused with waiting.
- [ ] Obtain row-level visual approval.

### Waiting

- [ ] Generate patient micro-actions and a closed loop.
- [ ] Avoid turning it into a sleep animation.
- [ ] Verify stable costume, baseline and tail.
- [ ] Obtain row-level visual approval.

## Phase R8 — standard-row gate

- [ ] Assemble all nine approved standard rows into an `8x9` QA atlas.
- [ ] Produce previews for all nine rows.
- [ ] Verify row order matches the v2 runtime contract.
- [ ] Verify no mixed visual baseline remains.
- [ ] Obtain approval before look-direction production.

## Phase R9 — direction anchors and sixteen directions

- [ ] Generate cardinal anchors in order: `000°`, `090°`, `180°`, `270°`.
- [ ] Verify `000°` is rear/up-facing and `180°` is front/down-facing.
- [ ] Verify side views show partial face anatomy rather than full front face.
- [ ] Verify tail and hat rotate with the body.
- [ ] Present four anchors for explicit approval.
- [ ] Generate row 9: `000°` through `157.5°`.
- [ ] Generate row 10: `180°` through `337.5°`.
- [ ] Record per-direction semantic QA.
- [ ] Verify adjacent continuity.
- [ ] Verify `337.5° -> 000°` closure.

## Phase R10 — final atlas and visual QA

- [ ] Assemble exact `1536x2288` atlas.
- [ ] Confirm `8 columns x 11 rows` and `192x208` cells.
- [ ] Confirm all 88 cells are present in fixed runtime order.
- [ ] Clear hidden RGB beneath full transparency.
- [ ] Check the atlas on checkerboard, dark and light backgrounds.
- [ ] Reject white, purple, pink, green or dark halos.
- [ ] Reject internal transparency holes.
- [ ] Reject cropped or disconnected components.
- [ ] Export final `spritesheet.webp`.
- [ ] Generate full 88-cell contact sheet.
- [ ] Generate required row and direction previews.
- [ ] Obtain final explicit user visual approval.

## Phase R11 — clean final package and validation

- [ ] Refresh latest `main`.
- [ ] Repeat duplicate searches for `LinaBell`, `Linabell`, `玲娜贝儿` and `linabell--elio-zwd`.
- [ ] Create clean branch `feat/add-linabell-pet-v2` from latest `main`.
- [ ] Add only:
  - [ ] `pets/linabell--elio-zwd/submission.json`
  - [ ] `pets/linabell--elio-zwd/pet.json`
  - [ ] `pets/linabell--elio-zwd/spritesheet.webp`
- [ ] Confirm `spriteVersionNumber: 2`.
- [ ] Run `npm run validate:pr`.
- [ ] Run `npm run lint`.
- [ ] Run `npm run install:pet -- linabell--elio-zwd --codex-home /tmp/codex-pet-test`.
- [ ] Record actual command outputs and failures.
- [ ] Confirm final pet directory contains exactly three files.
- [ ] Open a ready-for-review PR only after all visual and validation gates pass.
- [ ] Attach or link the final contact sheet in the PR body without committing QA media to the pet directory.
- [ ] Do not merge without a later explicit user instruction.
