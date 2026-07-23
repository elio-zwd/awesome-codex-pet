# LinaBell Production and Acceptance Plan

## Objective

Produce a high-quality, independently generated, non-commercial LinaBell fan-art Codex pet using the repository's v2 workflow. The main package uses the pink spring outfit. The blue sailor outfit remains a separate later variant rather than being mixed into the same atlas.

## Final package target

```text
pets/linabell--elio-zwd/
├── submission.json
├── pet.json
└── spritesheet.webp
```

Technical target:

- v2 atlas: `1536x2288`;
- grid: `8x11`;
- cell size: `192x208`;
- nine standard eight-frame rows;
- sixteen clockwise look directions;
- `pet.json.spriteVersionNumber: 2`.

## Phase 0 — planning complete

- [x] Review three supplied references
- [x] Select pink spring outfit as the main package
- [x] Reserve blue sailor outfit for a later variant
- [x] Define character anchors and failure conditions
- [x] Define all 88 runtime cells
- [x] Prepare metadata drafts
- [x] Search current catalog, issues and pull requests for obvious duplicates

## Phase 1 — canonical base art

Generate multiple independent full-body candidates grounded in all three references and the character brief.

Required candidate count:

- minimum: `3`;
- preferred: `4`;
- choose exactly one canonical base after visual review.

Base-art acceptance:

- full body, ears, feet and tail visible;
- pink spring outfit, no sailor-outfit mixing;
- plush/chibi style readable at `192x208`;
- stable face, blue eyes and cream facial patches;
- no text, logo, scenery, shadow or detached decorative effects;
- enough margin for running, jumping and waving motion;
- generated pixels are independent of the photographic references.

User approval gate: show the selected base candidate before generating the full atlas.

## Phase 2 — nine standard animation rows

Generate each row as a coherent eight-frame strip grounded in:

1. the selected canonical base;
2. all relevant user references;
3. previously approved rows when needed for continuity.

Recommended production order:

1. `idle`;
2. `running-right`;
3. `running-left` or approved mirror derivation;
4. `waving`;
5. `jumping`;
6. `failed`;
7. `waiting`;
8. `running`;
9. `review`.

After every row:

- split into eight cells;
- check frame boundaries and full silhouette;
- inspect animation timing;
- compare face, ears, outfit, tail and props against the canonical base;
- reject row-wide identity drift rather than patching isolated mismatched cells;
- reassemble the row deterministically after approval.

## Phase 3 — look mechanics

Create and approve four cardinal anchors:

- up (`000°`);
- screen-right (`090°`);
- down (`180°`);
- screen-left (`270°`).

Then generate two coherent eight-pose families for rows 9 and 10. Check:

- clockwise order;
- smooth `22.5°` progression;
- stable ear and hat rotation;
- believable front, side and rear face visibility;
- tail placement that follows body orientation;
- seamless boundary between `337.5°` and `000°`.

## Phase 4 — assembly and transparency

- assemble standard rows into an intermediate `8x9` atlas for review only;
- append the two approved look rows;
- produce final `8x11` atlas;
- remove the chroma background without damaging pink fur, cream face patches, blue eyes or green bow;
- clear hidden RGB under fully transparent pixels;
- inspect translucent and opaque boundary pixels for color spill;
- encode final atlas as `spritesheet.webp` at exact target dimensions.

## Phase 5 — visual QA

Generate local or CI review assets:

- full 88-cell contact sheet;
- one motion preview per standard row;
- clockwise look-direction preview;
- checkerboard preview;
- dark-background preview;
- light-background preview.

Visual QA checklist:

- [ ] identity consistent across all 88 cells
- [ ] all standard states semantically clear
- [ ] left/right gait alternates naturally
- [ ] hat decoration remains on the intended canonical side
- [ ] tail stays attached and inside cell boundaries
- [ ] props remain attached to paws/body
- [ ] no readable text or logos
- [ ] no floating effects or floor shadows
- [ ] no accidental transparent holes
- [ ] no chroma residue on any background
- [ ] all loops close smoothly
- [ ] all 16 look directions are ordered correctly

User approval gate: show the contact sheet and representative motion previews before publication.

## Phase 6 — final metadata

Promote the draft metadata into:

- `pets/linabell--elio-zwd/pet.json`;
- `pets/linabell--elio-zwd/submission.json`.

Before promotion, verify:

- final display name and bilingual names;
- submitter credit `Elio` / `@elio-zwd`;
- official character reference URL still resolves;
- final pixels were independently generated;
- non-commercial-only repository terms are accepted;
- description accurately matches the chosen outfit and action design.

## Phase 7 — repository validation

Run the contributor checks required by the repository:

```bash
npm run validate:pr
npm run lint
npm run install:pet -- linabell--elio-zwd --codex-home /tmp/codex-pet-test
```

Verify that `pets/linabell--elio-zwd/` contains exactly three files and no references, prompts, contact sheets, QA media or workfiles.

## Phase 8 — focused pull request

Only after visual approval and successful validation:

1. repeat duplicate search for `LinaBell`, `Linabell`, `玲娜贝儿` and the canonical key;
2. create a clean submission branch containing only the final pet package;
3. open a ready-for-review pull request against `main`;
4. attach the contact sheet to the PR body without committing it to the pet directory;
5. document authorship, reference-only provenance, non-commercial terms, v2 format and validation results;
6. follow CI and fix deterministic failures.

## Scope exclusions

Direction B does not automatically include:

- merging the planning workfiles into `main`;
- publishing private-chat reference images;
- creating the blue sailor variant in the same atlas;
- copying or tracing official image pixels;
- adding repository-generated README, `pets.json` or preview assets to the contributor PR.

## Completion definition

The LinaBell main variant is complete only when:

- the user approves the final contact sheet;
- the final v2 atlas has all 88 valid cells;
- metadata and package structure are valid;
- the isolated installation test succeeds;
- repository validation and lint pass;
- the final PR contains only the intended three-file pet package.