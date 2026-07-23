# LinaBell Codex Pet — Direction A Workspace

> Status: planning and metadata draft only. This workspace must **not** be merged into `main` as a finished pet submission.

This directory records the pre-production decisions for a LinaBell-inspired Codex pet requested by `@elio-zwd`. The final submission will be created later as exactly:

```text
pets/linabell--elio-zwd/
├── submission.json
├── pet.json
└── spritesheet.webp
```

## Direction A deliverables

- [Character brief](./character-brief.md)
- [Reference preprocessing notes](./reference-notes.md)
- [v2 action and frame plan](./action-list.md)
- [Production and acceptance plan](./production-plan.md)
- [`pet.json` draft](./pet.draft.json)
- [`submission.json` draft](./submission.draft.json)

## Current decisions

- Runtime target: Codex Pet **v2**
- Atlas target: `1536x2288`, `8 columns x 11 rows`, `88` cells total
- Cell size: `192x208`
- Main visual variant: pink spring outfit with hat
- Secondary visual variant: blue sailor outfit, postponed to a separate package or later variant
- Art direction: compact plush/chibi fan-art, transparent background, no readable text or logos
- Submitter credit: `Elio` / `@elio-zwd`
- Repository usage: non-commercial fan use only

## Reference handling

The three supplied images are private-chat references and are intentionally **not committed** to this public repository. They are used only to identify proportions, palette, costume cues, expression and movement. Final pixels must be generated independently rather than copied, cropped, traced or redistributed from the references.

## Duplicate check

At planning time, no existing `LinaBell`, `Linabell` or `玲娜贝儿` entry was found in `pets.json`, open issues or pull requests in this repository. Repeat the duplicate check immediately before opening the final pull request.

## Direction B gate

Direction B begins only after this plan is accepted. It will produce and review:

1. canonical full-body base art;
2. nine coherent eight-frame standard action strips;
3. four cardinal look anchors;
4. sixteen clockwise look-direction cells;
5. a final contact sheet and motion previews;
6. the installable v2 spritesheet and final metadata.

Do not open a finished submission pull request until the user has reviewed the contact sheet and the final package passes repository validation.