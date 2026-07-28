# LinaBell Direction B — Visual Rebaseline Production Plan

> Date: 2026-07-28
>
> Repository: `elio-zwd/awesome-codex-pet`
>
> Planning branch: `feat/linabell-pet-direction-a`
>
> Status: three new identity-validation candidate sheets received; visual rebaseline is not yet user-approved.
>
> This document supplements `direction-b-execution-plan.md`. The original v2 technical contract, row order, validation requirements, clean-branch policy and final three-file scope remain authoritative.

## 1. Why a visual rebaseline is required

Three newly generated `2x4` contact sheets now provide a coherent candidate set for:

1. `idle`;
2. `waving`;
3. `review`.

The three sheets are internally consistent with one another, but they differ visibly from the previously approved canonical base in face proportions, hat brim, costume rendering, skirt motif treatment and overall plush-render style. Mixing the old base with these new sheets would create identity drift across the final atlas.

Therefore, before producing the remaining six standard animation rows, the project must choose one of two mutually exclusive paths:

- approve the new three-sheet family and derive a new canonical production base from it; or
- reject the new family and return to the previously approved canonical base.

The recommended path is to adopt the new family, because the three actions now share one stable design language and the waving/review semantics are substantially clearer than previous attempts.

## 2. Current visual QA

### 2.1 Shared strengths

All three new sheets:

- contain exactly eight poses arranged as `2 rows x 4 columns`;
- preserve the same large ears, cream face patches, bright blue eyes, pink nose and plush texture;
- preserve the same spring outfit family, green neck bow, paired cherries and skirt decoration;
- keep the hat flower on one consistent canonical side;
- keep a single attached tail with stable side placement and pale tip;
- avoid text, logos, scenery, speech bubbles and detached effects;
- use matching body scale and rendering quality across the three actions.

### 2.2 Idle candidate

Strengths:

- stable forward-facing body;
- clear blink sequence;
- consistent tail placement and costume;
- strong loop closure between the final and first poses.

Remaining work:

- motion is currently dominated by blinking and needs measured frame-to-frame registration to confirm that breathing and settling are visible at `192x208`;
- duplicate or near-duplicate frames may need small local adjustments after extraction;
- the sheet background is visually purple and the PNG alpha channel is fully opaque, so transparency still requires deterministic removal.

Disposition: **candidate accepted for extraction and motion preview; not yet final-approved**.

### 2.3 Waving candidate

Strengths:

- one consistent waving paw is used throughout;
- the paw rises, remains near the head, waves, lowers and returns to neutral;
- the gesture remains readable without motion lines;
- the other paw, feet, costume and tail remain stable.

Remaining work:

- confirm that frames 3 through 6 produce a visible outward/inward wave after normalization;
- normalize small body-scale and paw-height differences;
- verify that paw pads and arm attachment remain clean after background removal.

Disposition: **best current waving candidate; proceed to extraction and preview**.

### 2.4 Review candidate

Strengths:

- the pink clipboard remains present and physically held in all eight poses;
- the sequence reads as ready, inspect, point, think, notice, verify, approve and reset;
- clipboard design and color remain stable;
- no readable text or floating icons are present;
- character identity remains consistent with the idle and waving sheets.

Remaining work:

- verify consistent clipboard handedness and size after per-frame cropping;
- check that the free paw does not create human-finger shapes at pet size;
- normalize head and clipboard registration;
- confirm that the final pose loops naturally to frame 1.

Disposition: **candidate accepted for extraction and motion preview; not yet final-approved**.

## 3. Visual rebaseline gate

Before generating `running-right`, `running-left`, `running`, `jumping`, `failed` or `waiting`:

1. extract all 24 poses from the three candidate sheets;
2. remove the purple background and create true alpha;
3. normalize each frame to `192x208` without distorting body proportions;
4. align body center and feet baseline;
5. produce transparent `idle`, `waving` and `review` rows;
6. produce loop previews for all three rows;
7. produce one three-row contact sheet;
8. present the contact sheet and previews to the user;
9. obtain explicit approval that the new family replaces the old canonical visual base.

Until step 9 is complete, status remains `visual-rebaseline-candidate`.

After approval:

- select a clean neutral frame from the new family, preferably idle frame 1 or frame 8;
- promote it as the new canonical production base;
- update `canonical-base.webp`, `canonical-base-qa.md` and `handoff-state.json`;
- do not mix pixels, scale references or face geometry from the old base into subsequent rows.

## 4. Deterministic extraction and transparency process

Each uploaded sheet is `1448x1086`, PNG, RGBA container with alpha fixed at 255. The purple background is therefore visible opaque RGB, not transparency.

For each sheet:

1. define four equal logical columns and two logical rows;
2. detect each character silhouette within its logical slot;
3. crop with safety margin around ears, hat, paws, skirt, feet and tail;
4. remove the purple background using a color-distance mask rather than one exact RGB value;
5. preserve pink fur and red/pink costume pixels by combining color distance with edge-connected background detection;
6. refine partially transparent edge pixels to avoid purple fringe;
7. clear hidden RGB for pixels whose alpha becomes zero;
8. fit the silhouette into a `192x208` cell with a shared scale target;
9. align the feet baseline consistently within the action row;
10. visually inspect on checkerboard, dark and light backgrounds.

Reject any extracted frame with:

- purple, white or dark fringe;
- transparent holes in fur, clothing, eyes or clipboard;
- cropped ears, hat, feet or tail;
- detached tail, paw or clipboard pieces;
- scale drift or baseline jump that cannot be corrected by translation alone.

## 5. Motion preview acceptance criteria

### Idle

- no walking, waving or prop use;
- blink remains smooth rather than abrupt;
- at least one visible non-blink micro-motion exists;
- frame 8 returns naturally to frame 1;
- tail remains calm and attached.

### Waving

- the same paw performs the entire gesture;
- frames 3 to 6 visibly alternate the wave direction;
- the paw does not cover the face;
- no extra limbs or human fingers appear;
- frame 8 returns cleanly to frame 1.

### Review

- the clipboard stays attached and blank;
- the sequence reads as one continuous review workflow;
- eyes and free paw track the clipboard appropriately;
- the thinking and satisfied states are distinguishable at pet size;
- frame 8 closes naturally to frame 1.

## 6. Remaining standard rows after approval

Generate and review one row at a time in this order:

1. `running-right`;
2. `running-left`;
3. `running`;
4. `jumping`;
5. `failed`;
6. `waiting`.

Every generation must use the new approved canonical base plus the approved three-row contact sheet as identity references.

Do not use the old canonical base after rebaseline approval.

For `running-left`, do not blindly mirror `running-right`; the hat flower is asymmetric and must remain on the canonical character side.

## 7. Direction production

After all nine standard rows are approved:

1. generate `000°`, `090°`, `180°`, `270°` anchors;
2. obtain user approval for the four anchors;
3. generate all sixteen clockwise directions;
4. verify hat, ears, face visibility, skirt and tail rotate together;
5. verify `337.5° -> 000°` closure.

## 8. Final assembly and publication

The final atlas remains:

```text
1536 x 2288
8 columns x 11 rows
192 x 208 per cell
88 cells total
spriteVersionNumber: 2
```

The final clean branch must still be created from the latest `main`:

```text
feat/add-linabell-pet-v2
```

The final pet directory must contain exactly:

```text
pets/linabell--elio-zwd/submission.json
pets/linabell--elio-zwd/pet.json
pets/linabell--elio-zwd/spritesheet.webp
```

Before opening a ready-for-review PR, actually run:

```bash
npm run validate:pr
npm run lint
npm run install:pet -- linabell--elio-zwd --codex-home /tmp/codex-pet-test
```

Do not automatically merge the PR.

## 9. Approval gates

Execution must stop for explicit user approval at:

1. new three-row visual rebaseline contact sheet and previews;
2. four cardinal direction anchors;
3. final 88-cell contact sheet and required motion previews;
4. final PR readiness if any visual or validation concern remains.
