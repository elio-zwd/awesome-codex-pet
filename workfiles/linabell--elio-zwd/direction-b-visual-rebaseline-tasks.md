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
- [x] Commit compact generated previews and provenance notes under `workfiles/`.
- [x] Permit generated workfiles in the planning branch.
- [x] Never commit private photographic reference images.

## Phase R1 — identity rows

### Idle

- [x] Extract eight frames.
- [x] Verify ordered blink sequence, stable tail side and body orientation.
- [x] Approve the cleaned row.

### Waving

- [x] Extract eight frames.
- [x] Confirm one consistent waving paw and a raise-wave-lower sequence.
- [x] Approve the cleaned row.

### Review

- [x] Reject the first processed Review because frame 4 contains a third paw.
- [x] Use image 1 third row as the replacement Review.
- [x] Remove its dark background and normalize eight transparent `192x208` cells.
- [x] Confirm no visible third paw and no readable clipboard text.
- [x] Approve the image 1 Review row.

## Phase R2 — visual rebaseline gate

- [x] Show the updated contact sheet and image 1 Review preview.
- [x] Obtain explicit approval for `idle`, `waving` and image 1 `review`.
- [x] Promote this identity family as the sole production grounding reference.

## Phase R3 — remaining production

### Running-right

- [x] Receive first `running-right` 2x4 candidate.
- [x] Confirm identity, outfit, hat flower, tail and plush style remain stable.
- [x] Build an eight-frame loop preview and numbered contact sheet.
- [x] Detect near-duplicate pairs: frames 4/8 and frames 2/3.
- [x] Reject the first candidate as a final row because the legs do not form a clearly alternating two-sided run cycle.
- [-] Regenerate `running-right` with distinct contact, passing and airborne phases; only frame 8 may return close to frame 1.

### Remaining rows

- [ ] Generate `running-left`.
- [ ] Generate `running`.
- [ ] Generate `jumping`.
- [ ] Generate `failed`.
- [ ] Generate `waiting`.
- [ ] Generate four cardinal look anchors.
- [ ] Generate the sixteen look directions.
- [ ] Assemble the final atlas, repeat transparency QA, run validation and follow the clean PR workflow.
