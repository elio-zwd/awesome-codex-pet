# LinaBell Direction B — Detailed Execution Plan

> Branch: `feat/linabell-pet-direction-a`
>
> Status: production handoff prepared; no final pet package or pull request exists yet.
>
> This document is the authoritative execution plan for the next ChatGPT/Codex conversation.

## 1. Goal

Produce a high-quality, independently generated, non-commercial LinaBell-inspired Codex desktop pet using the repository's v2 format.

The final deliverable must be exactly:

```text
pets/linabell--elio-zwd/
├── submission.json
├── pet.json
└── spritesheet.webp
```

The main visual variant is the pink spring outfit. The blue sailor outfit is intentionally postponed to a separate future package or variant.

## 2. Current state at handoff

Completed:

- repository access and administrator permissions confirmed for `elio-zwd/awesome-codex-pet`;
- planning branch created: `feat/linabell-pet-direction-a`;
- three user-supplied reference images reviewed;
- character identity, costume, visual anchors and failure conditions documented;
- duplicate search completed against `pets.json`, open issues and open pull requests;
- no obvious existing LinaBell / Linabell / 玲娜贝儿 submission found at planning time;
- v2 action map and frame semantics documented;
- draft `pet.json` and `submission.json` created;
- one usable independently generated full-body base concept was produced in the previous chat.

Not completed:

- the generated full-body base concept has not been uploaded to GitHub because the available GitHub contents action supports UTF-8 text only;
- the generated base concept has not received a final explicit user approval in a fresh production context;
- no animation row has been generated;
- no look-direction row has been generated;
- no final spritesheet exists;
- no validation or installation test has been run;
- no final three-file pet package or pull request exists.

## 3. Required inputs in the new conversation

The new conversation does not inherit images from the previous chat. The user must upload:

1. the successful generated full-body base concept from the previous chat;
2. preferably the three original character reference images again, for identity checking only.

The generated base concept should be treated as the canonical visual source for production. The original photographs are supporting references only and must not be cropped, traced, republished or used as final pixels.

If only the generated base concept is supplied, production may continue because all written identity constraints are already stored in this branch. If the generated base concept is missing, pause before animation production and ask the user to upload it.

## 4. Locked character definition

### 4.1 Identity anchors

The pet must consistently read as the same pink fox mascot character:

- oversized upright triangular ears;
- pink plush fur;
- cream-white eye patches and muzzle;
- very large bright blue eyes with visible eyelashes;
- small pink nose;
- cheerful, curious and friendly expression;
- large fluffy pink tail with a pale cream tip;
- short compact chibi body and plush-toy material.

### 4.2 Locked main outfit

The entire main atlas uses one outfit only:

- pale pink floppy sun hat;
- white flower and pink bow decoration on the canonical side of the hat;
- pink-and-pale-yellow plaid short-sleeved top;
- green ribbon bow at the neck;
- paired cherry decoration at the chest;
- pink flared skirt with subtle light dots and lace edge;
- small fruit/cherry patch on the skirt where readable at pet size.

Do not mix in the blue sailor outfit anywhere in this atlas.

### 4.3 Personality

- warm and energetic rather than chaotic;
- expressive through ears, tail, paws, posture and face;
- curious planner/reviewer personality;
- suitable as a friendly coding companion.

### 4.4 Forbidden drift

Reject and regenerate any row that introduces:

- cat-like facial proportions that remove the fox identity;
- changed eye color, missing eyelashes or missing cream face patches;
- different hat shape, swapped flower side or missing cherry/green-bow cues;
- sailor clothing or other costume substitution;
- missing, detached, duplicated or radically resized tail;
- human hands, long human legs or non-plush anatomy;
- readable text, brand logos, Disney logos or scenery;
- detached stars, motion lines, speech bubbles, thought bubbles or floor shadows;
- significant body scale changes across frames.

## 5. Technical contract

Use Codex Pet v2:

```text
atlas size: 1536 x 2288
columns: 8
rows: 11
cell size: 192 x 208
standard animation cells: 72
look-direction cells: 16
total cells: 88
pet.json spriteVersionNumber: 2
```

Runtime row order is fixed:

| Row | Runtime state | Frame count |
|---:|---|---:|
| 0 | `idle` | 8 |
| 1 | `running-right` | 8 |
| 2 | `running-left` | 8 |
| 3 | `waving` | 8 |
| 4 | `jumping` | 8 |
| 5 | `failed` | 8 |
| 6 | `waiting` | 8 |
| 7 | `running` | 8 |
| 8 | `review` | 8 |
| 9 | look directions `000°` through `157.5°` | 8 |
| 10 | look directions `180°` through `337.5°` | 8 |

Never invent additional runtime rows. Rich behavior must be expressed inside the nine supported standard rows.

## 6. Production strategy

### Stage B0 — reopen repository context

Before changing files:

1. inspect this branch and read:
   - `README.md`;
   - `character-brief.md`;
   - `reference-notes.md`;
   - `action-list.md`;
   - `production-plan.md`;
   - this document;
   - `pet.draft.json`;
   - `submission.draft.json`;
2. read repository `AGENTS.md`, `CONTRIBUTING.md`, `.agents/skills/submit-codex-pet/SKILL.md`, and `.agents/skills/hatch-pet-v2/SKILL.md`;
3. repeat the duplicate search before final publication, not necessarily before every visual iteration;
4. do not modify `main`.

### Stage B1 — canonical-base approval

Use the successful generated full-body concept as the sole canonical base image.

Check it against the locked definition:

- full body visible;
- ears, paws and tail fully visible;
- outfit matches the pink spring version;
- face and fur colors match the brief;
- silhouette remains readable after scaling to `192x208`;
- sufficient empty margin exists above ears and around the tail;
- no text, logos or scene details;
- no anatomy defects.

Show the image to the user and ask only for a visual approval or one consolidated correction request.

Do not generate multiple replacements unless the user rejects the base. This avoids unnecessary identity drift.

After approval, preserve the exact approved image as the canonical grounding image for every subsequent visual job.

### Stage B2 — identity-validation rows

Generate these three rows first:

1. `idle`;
2. `waving`;
3. `review`.

These rows are the identity gate because they expose the face, outfit, hat, paw anatomy and personality clearly.

#### Idle row

Eight-frame loop:

1. neutral standing pose;
2. subtle inhale/body rise;
3. blink begins;
4. eyes closed, ears slightly relaxed;
5. eyes reopen;
6. tail makes a small controlled sway;
7. slight head return and body settle;
8. near-neutral loop closure.

Rules:

- no large gesture;
- no new prop;
- no walking or waving;
- visible micro-motion is required;
- feet remain on a stable baseline.

#### Waving row

Eight-frame loop:

1. neutral greeting preparation;
2. one paw rises;
3. paw reaches greeting height;
4. wave outward;
5. wave inward;
6. second smaller wave;
7. paw lowers;
8. returns to neutral.

Rules:

- gesture uses the paw only;
- no wave marks or sparkles;
- tail may counterbalance subtly;
- hat and flower must remain stable.

#### Review row

Eight-frame loop with a small attached pink clipboard/planner:

1. bring clipboard into view;
2. look down attentively;
3. trace/check one item with paw;
4. thoughtful pause;
5. small realization or pleased expression;
6. confident nod;
7. lower clipboard slightly;
8. return to review-ready pose.

Rules:

- clipboard contains no readable text;
- prop stays physically attached to the paw/body silhouette;
- no floating icons or thought bubbles;
- preserve face readability.

After each row:

- split into eight `192x208` cells;
- inspect all cells at 1x and enlarged scale;
- review the animated loop;
- compare identity to the canonical base;
- regenerate the complete row if identity drifts across multiple cells;
- repair only the smallest failing scope when one cell has a local defect and the row identity remains coherent.

Create a temporary contact sheet for these three rows and show it to the user before continuing.

### Stage B3 — locomotion rows

After B2 approval, produce:

1. `running-right`;
2. `running-left`;
3. `running`.

#### Running-right

Use a readable eight-frame gait cycle with alternating foot contact, compression, passing pose and extension. Keep the tail trailing and counterbalancing without crossing cell boundaries.

#### Running-left

Mirror the approved `running-right` row only when all asymmetric details remain correct after mirroring. The hat flower/cherry placement is asymmetric, so a raw mirror may move the decoration to the wrong canonical side. Prefer a separately generated coherent left-running row or repair the full mirrored row consistently.

#### Running

Use a compact forward/energetic run-in-place behavior appropriate to the runtime state. It must be visually distinct from `running-right` and `running-left` while retaining a stable baseline and loop.

Locomotion checks:

- left and right feet alternate naturally;
- no foot duplication or sliding;
- head and torso bob are limited;
- ears and hat respond consistently to motion;
- tail remains attached and does not teleport;
- no speed lines, dust or detached effects.

### Stage B4 — vertical and emotional rows

Produce:

1. `jumping`;
2. `failed`;
3. `waiting`.

#### Jumping

Eight-frame arc:

1. neutral;
2. crouch;
3. launch;
4. rising;
5. apex;
6. descending;
7. landing compression;
8. recovery.

No floor shadow, dust, impact burst or floating effect.

#### Failed

Use readable disappointment without excessive distress:

1. confident/neutral start;
2. realizes mistake;
3. ears lower;
4. shoulders slump;
5. small attached tear or paw-to-face gesture if cleanly rendered;
6. brief discouraged pause;
7. begins recovery;
8. subdued loop closure.

No detached punctuation, icons or loose tears.

#### Waiting

Combine patient waiting and gentle micro-actions:

1. neutral waiting;
2. shift weight;
3. glance slightly aside;
4. tail curls closer;
5. brief sleepy blink or tiny yawn;
6. ears perk up;
7. posture resets;
8. neutral loop closure.

Do not turn this into a full sleep animation or introduce furniture.

### Stage B5 — four cardinal look anchors

After all nine standard rows pass identity review, generate one coherent four-pose anchor strip in this exact order:

1. `000°` — up/back-facing direction;
2. `090°` — screen-right;
3. `180°` — down/front-facing direction;
4. `270°` — screen-left.

Important:

- `000°` means looking upward, not neutral front;
- preserve hat geometry and flower-side logic through rotation;
- rotate ears, muzzle visibility, body, skirt and tail together;
- rear views should not show impossible full facial features;
- side views should show believable one-eye/partial-muzzle visibility.

Approve the four anchors before generating intermediate directions.

### Stage B6 — sixteen look directions

Generate two coherent eight-pose families:

Row 9:

```text
000°, 022.5°, 045°, 067.5°, 090°, 112.5°, 135°, 157.5°
```

Row 10:

```text
180°, 202.5°, 225°, 247.5°, 270°, 292.5°, 315°, 337.5°
```

Checks:

- clockwise progression is correct;
- each step is visually distinct but smooth;
- scale, baseline and body center remain stable;
- ear and hat rotation are continuous;
- face visibility changes naturally;
- tail follows the body turn;
- transition from `337.5°` back to `000°` is smooth.

Do not generate or repair a complete `8x11` atlas as one image. Generate coherent row families and assemble deterministically.

### Stage B7 — deterministic assembly and transparency

1. assemble approved rows 0–8 into an intermediate `8x9` atlas for QA only;
2. append look rows 9–10;
3. produce exact `1536x2288` output;
4. remove the generation background cleanly;
5. preserve pink fur, cream patches, blue eyes, green bow and pale clothing highlights;
6. clear hidden RGB under fully transparent pixels;
7. inspect edge spill on checkerboard, dark and light backgrounds;
8. encode the final runtime image as `spritesheet.webp`.

Reject:

- accidental transparent holes inside the body;
- colored halos or white fringe;
- cropped ears/tail;
- cells with multiple disconnected character components;
- mismatched frame sizes or registration.

### Stage B8 — final visual approval

Generate review assets outside the final pet directory:

- full 88-cell contact sheet;
- GIF or equivalent motion preview for each standard row;
- clockwise look-direction preview;
- checkerboard, dark and light background sheets.

Show the user at minimum:

1. the full contact sheet;
2. `idle` preview;
3. `waving` preview;
4. `running-right` preview;
5. `review` preview;
6. look-direction preview.

Do not publish the final pet until the user explicitly approves or requests specific repairs.

### Stage B9 — final package

Promote the drafts into:

```text
pets/linabell--elio-zwd/pet.json
pets/linabell--elio-zwd/submission.json
pets/linabell--elio-zwd/spritesheet.webp
```

The directory must contain exactly these three files.

Confirm metadata:

- id/folder: `linabell--elio-zwd`;
- display name: `玲娜贝儿` or the final user-approved display name;
- localized names include `LinaBell` and `玲娜贝儿` if retained;
- author: `Elio`;
- author handle: `elio-zwd`;
- final asset provenance: independently generated fan art based on reference-only materials;
- repository usage: non-commercial only;
- `spriteVersionNumber: 2`.

### Stage B10 — validation and clean PR

Run:

```bash
npm run validate:pr
npm run lint
npm run install:pet -- linabell--elio-zwd --codex-home /tmp/codex-pet-test
```

Also verify:

- final image dimensions are exact;
- final pet directory has exactly three files;
- no references, workfiles, prompts, contact sheets or QA media are included in the final submission commit;
- duplicate search is repeated;
- installation produces the expected files.

Create a new focused final-submission branch from the latest `main`; do not merge the planning workfiles into the final PR. Copy only the approved final three-file package onto that clean branch.

Open a ready-for-review PR only after:

- user visual approval;
- all validations pass;
- the contact sheet is available for attachment to the PR body.

## 7. Git and branch policy

Current planning branch:

```text
feat/linabell-pet-direction-a
```

This branch intentionally contains planning workfiles and must not be used directly as the final contributor PR.

Recommended final branch name:

```text
feat/add-linabell-pet-v2
```

Final PR scope:

```text
pets/linabell--elio-zwd/submission.json
pets/linabell--elio-zwd/pet.json
pets/linabell--elio-zwd/spritesheet.webp
```

Nothing else should be included unless a repository validator requires a focused source-code fix, which should normally be handled separately.

## 8. Decision rules for the next assistant

- Act on the repository instead of returning only advice.
- Keep the user informed at approval gates, not after every minor internal step.
- Do not silently change the character definition or outfit.
- Do not replace the canonical base after approval unless a blocking quality defect is found.
- Generate and validate one coherent row at a time.
- Repair the smallest failing scope while preserving row coherence.
- Do not create a PR before the spritesheet exists and the user has approved the visual review.
- Do not merge anything without an explicit user request.
- Never claim a test passed unless it was actually executed.
- Be transparent when a tool cannot upload or preserve binary assets.

## 9. Completion checklist

- [ ] generated base image re-uploaded in the new conversation
- [ ] canonical base visually approved
- [ ] idle row approved
- [ ] waving row approved
- [ ] review row approved
- [ ] three-row identity contact sheet approved
- [ ] running-right row approved
- [ ] running-left row approved
- [ ] running row approved
- [ ] jumping row approved
- [ ] failed row approved
- [ ] waiting row approved
- [ ] four cardinal anchors approved
- [ ] row 9 directions approved
- [ ] row 10 directions approved
- [ ] exact 1536x2288 atlas assembled
- [ ] transparency and edge QA passed
- [ ] full contact sheet reviewed by user
- [ ] metadata finalized
- [ ] `npm run validate:pr` passed
- [ ] `npm run lint` passed
- [ ] isolated installation test passed
- [ ] clean final branch created from current `main`
- [ ] final PR opened ready for review
