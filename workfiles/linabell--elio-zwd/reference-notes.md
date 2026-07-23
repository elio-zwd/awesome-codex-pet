# Reference Preprocessing Notes

## Scope

Three user-supplied JPEG references were reviewed. They are not committed because they came from a private chat and are only reference material. The production workflow should create independent fan-art pixels.

## Reference inventory

### REF-01 — pink outfit, front view

- Original dimensions: `1206x1194`
- Framing: clean front-facing upper body on a white background
- Strongest information:
  - face geometry;
  - ear size and spacing;
  - blue eye color and eyelashes;
  - pink nose and cream muzzle;
  - pink sun hat, pale brim and flower accent;
  - checked pink/yellow clothing, green bow and cherry motif.
- Limitations:
  - lower body and tail are not visible;
  - arms are posed at the waist, so neutral limb anatomy is partly hidden.
- Role: **primary identity and main-costume reference**.

### REF-02 — pink outfit, three-quarter wave

- Original dimensions: `1206x1202`
- Framing: three-quarter upper body on a white background
- Strongest information:
  - happy open-mouth expression;
  - raised-paw wave;
  - three-quarter head construction;
  - clipboard interaction;
  - alternate pink hat and dress details.
- Limitations:
  - lower legs and tail are not visible;
  - clipboard contains readable text that must not be copied.
- Role: **gesture, expression and review/waiting prop reference**.

### REF-03 — blue sailor outfit, full body

- Original dimensions: `1206x1605`
- Framing: full-body stage photograph with dark side bars and a `1/10` screenshot overlay
- Strongest information:
  - whole-body proportions;
  - leg length and stance;
  - tail volume and placement;
  - raised-paw action;
  - how the large head balances against the body.
- Limitations:
  - stage lighting shifts fur colors;
  - complex background and neighboring subjects;
  - screenshot overlay and side bars;
  - different costume from the main variant.
- Role: **body/tail anatomy and secondary-costume reference only**.

## Preprocessing strategy for Direction B

### 1. Build a non-destructive reference board

Create a local-only board with:

- REF-01 full image and a face/hat crop;
- REF-02 full image and a waving/clipboard crop;
- REF-03 a manually cropped full-body region excluding side bars and the `1/10` overlay;
- palette swatches sampled only as approximate visual cues;
- written labels for immutable identity anchors.

Do not save this board in the final repository submission.

### 2. Normalize color interpretation

Use REF-01 and REF-02 for the main palette because their white backgrounds and even lighting are more reliable. Use REF-03 only to estimate silhouette and tail size. Do not inherit its stage-light blue/purple cast.

Provisional palette families:

- fur: warm dusty pink;
- face/muzzle: warm cream white;
- eyes: deep royal blue with lighter blue highlights;
- nose: muted rose pink;
- main clothing: blush pink, pale yellow and cream;
- accent: soft green bow;
- small motif: cherry red/pink.

Exact production colors should avoid the selected chroma-key color and should remain stable across all rows.

### 3. Separate invariant and optional details

**Invariant:** ears, eye patches, blue eyes, muzzle, pink nose, plush tail, pink fur, main hat silhouette.

**Simplifiable:** tiny plaid lines, stitching, small lace, small printed dots, clipboard text.

**Optional by action:** magnifying glass, clipboard, flower accent motion.

### 4. Reconstruct rather than retouch

The base pet should be newly generated as a compact whole-body plush/chibi illustration. Do not directly remove the white background from REF-01 or REF-02 and animate the result. Do not inpaint REF-03 into a final sprite. This avoids photographic inconsistency, direct pixel reuse and poor frame continuity.

### 5. Canonical base requirements

The approved base frame should:

- show the full body, ears, feet and tail;
- use the pink spring outfit;
- face mostly forward with a calm smile;
- keep both paws visible and free of large props;
- fit safely inside a `192x208` cell with motion margin;
- contain no shadow, scenery, text or logo;
- become the identity anchor for every generated action strip.

## Reference confidence

| Attribute | Best reference | Confidence |
| --- | --- | --- |
| Face and eyes | REF-01 | High |
| Hat and pink outfit | REF-01 + REF-02 | High |
| Wave gesture | REF-02 | High |
| Clipboard interaction | REF-02 | Medium-high |
| Full-body proportion | REF-03 | High |
| Tail volume/placement | REF-03 | High |
| Main outfit lower-body design | inferred from REF-01/02 | Medium |
| Exact rear view | not supplied | Low; must be consistently designed |

## QA risks to watch

- fur edges contaminated by white, green, cyan or magenta residue;
- cream face patches merging into transparent background;
- tail becoming detached or crossing cell boundaries;
- hat brim changing width from frame to frame;
- cherry motif flickering or becoming unreadable noise;
- clipboard or magnifying glass floating away from the paw;
- photographic mascot proportions leaking into some rows while others become flat cartoons;
- left/right mirroring moving asymmetric hat decorations to the wrong canonical side.