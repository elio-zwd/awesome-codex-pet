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
- are high enough resolution for later frame extraction and downscaling.

### 2.2 Idle candidate

Strengths:

- coherent eight-pose idle candidate;
- readable blink cycle;
- stable body scale and baseline;
- no detached props or gesture confusion.

Checks still required after extraction:

- confirm that the body-breathing and settle motion remain visible at `192x208`;
- confirm that frame 8 loops naturally back to frame 1;
- verify that tail motion is not so small that the row becomes visually static.

### 2.3 Waving candidate

Strengths:

- clear greeting semantics;
- one paw remains the dominant waving paw through the loop;
- no detached action marks;
- good costume/identity stability.

Checks still required after extraction:

- confirm the same waving paw is used consistently in frames 2–7 after splitting;
- confirm the wave beats remain readable at runtime cell size;
- confirm no cropping of the raised paw or tail in normalized cells.

### 2.4 Review candidate

Strengths:

- the pink clipboard remains visible in all eight poses;
- the sequence communicates inspect → think → notice → confirm;
- the character identity remains close to the idle and waving candidates.

Checks still required after extraction:

- confirm the clipboard stays attached and does not cover the face after crop normalization;
- confirm the blank clipboard contains no readable text or iconography;
- confirm frames 6–8 create a smooth resolution and loop closure.

## 3. Updated asset policy

### 3.1 Allowed to commit

The following **may and should be committed** to the planning branch for provenance, collaboration and handoff clarity:

- the three newly generated candidate sheets for `idle`, `waving` and `review`;
- future generated row sheets for other runtime states;
- extracted frame PNGs used for QA;
- derived review contact sheets or preview assets stored under `workfiles/`.

These are generated production workfiles, not private user photographs.

Recommended location:

```text
workfiles/linabell--elio-zwd/assets/generated-candidates/
```

### 3.2 Still forbidden to commit

The following remain forbidden in the public repository:

- the user’s private original photographic reference images;
- cropped or traced derivatives of those photographs presented as final art;
- any asset that republishes private source photos directly.

### 3.3 Final PR policy unchanged

Even though generated candidate sheets are allowed in the planning branch, they still must **not** be included in the final clean submission PR.

The final submission branch and final contributor PR must still contain only:

```text
pets/linabell--elio-zwd/submission.json
pets/linabell--elio-zwd/pet.json
pets/linabell--elio-zwd/spritesheet.webp
```

## 4. Immediate next steps

1. Save the three current candidate sheets into the planning branch under `workfiles/linabell--elio-zwd/assets/generated-candidates/`.
2. Record their role and provenance.
3. Split each `2x4` sheet into ordered frames 1–8.
4. Remove the solid purple background and normalize all cells to `192x208`.
5. Produce idle / waving / review preview loops.
6. Ask the user whether this new three-sheet family should replace the old canonical production base.

## 5. Decision gate

The next approval gate is now explicitly:

- **Approve new visual baseline**; or
- **Reject new visual baseline and revert to old base**.

Only after that decision should the remaining six standard animation rows be produced.
