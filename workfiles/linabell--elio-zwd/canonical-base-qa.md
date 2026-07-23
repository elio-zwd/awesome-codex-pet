# Canonical Base Approval and QA

Status: **approved** by the user on 2026-07-23.

## Asset

- Repository production copy: `assets/canonical-base.webp`
- Repository copy dimensions: `256x341`
- Original generated source dimensions in the production conversation: `1086x1448`
- Provenance: independently generated fan art grounded in private reference photographs
- Private reference photographs: not committed

The repository copy is intentionally compact but remains larger than the final desktop-pet display scale. The approved source image in the active production conversation remains the visual source of truth.

## Identity review

Passed:

- oversized upright triangular ears;
- pink plush fur;
- cream-white eye patches and muzzle;
- large bright blue eyes and eyelashes;
- small pink nose and friendly expression;
- pale pink floppy hat;
- white flower and pink bow kept on the approved viewer-left side;
- pink-and-pale-yellow plaid top;
- green neck bow and paired cherry decoration;
- broad pink skirt with light dots, lace edge and small fruit motif;
- full attached fluffy tail with pale tip;
- both paws, both feet, both ears and the full tail are visible;
- no sailor outfit, readable text, logo, prop, scenery, floor shadow or detached effect.

## `192x208` scale test

A deterministic fit test placed the visible character at approximately `132x190` pixels inside a `192x208` cell:

- left/right free space: approximately `30px` each;
- top free space: approximately `10px`;
- bottom/baseline free space: approximately `8px`.

The face, blue eyes, hat, green bow, cherries, skirt silhouette and tail remain readable at target size. The small plaid and lace details may be simplified during animation generation.

## Animation cautions

- Preserve the flower and bow on the same canonical side in every frame.
- Keep the tail attached and within the slot; its large volume requires deliberate side-motion planning.
- Keep the hat brim width and ear spacing stable.
- Use the approved base as an image input for every visual row; prompt-only row generation is invalid.
- Generate `running-left` independently unless a reviewed frame-by-frame mirror preserves all asymmetric details.

## Next approval gate

Generate `idle`, `waving` and `review` as three separate coherent eight-frame rows. After deterministic frame extraction and loop QA, show the user a three-row contact sheet plus motion previews. Do not continue to the remaining six standard rows until the user approves this gate.
