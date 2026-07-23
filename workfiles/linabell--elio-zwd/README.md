# LinaBell Codex Pet — Planning and Direction B Handoff

> Status: Direction A is complete and Direction B is ready for production in a new conversation. This workspace must **not** be merged into `main` as a finished pet submission.

This directory records the pre-production decisions and execution handoff for a LinaBell-inspired Codex pet requested by `@elio-zwd`. The final submission will later be created as exactly:

```text
pets/linabell--elio-zwd/
├── submission.json
├── pet.json
└── spritesheet.webp
```

## Start here in the next conversation

1. Read the [detailed Direction B execution plan](./direction-b-execution-plan.md).
2. Read the machine-readable [handoff state](./handoff-state.json).
3. Copy the complete [next-chat prompt](./NEXT_CHAT_PROMPT.md).
4. Re-upload the successful generated full-body base concept from the previous chat.
5. Optionally re-upload the three original reference images for identity checking.

The available GitHub text-file action cannot upload the generated PNG binary, so the canonical base image is not stored in this branch. Do not begin animation production until the user uploads that image in the new conversation.

## Planning files

- [Character brief](./character-brief.md)
- [Reference preprocessing notes](./reference-notes.md)
- [v2 action and frame plan](./action-list.md)
- [Original production and acceptance plan](./production-plan.md)
- [Detailed Direction B execution plan](./direction-b-execution-plan.md)
- [Direction B handoff state](./handoff-state.json)
- [Next-chat production prompt](./NEXT_CHAT_PROMPT.md)
- [`pet.json` draft](./pet.draft.json)
- [`submission.json` draft](./submission.draft.json)

## Current progress

Completed:

- three supplied references reviewed;
- character definition and main outfit locked;
- Codex Pet v2 technical specification selected;
- all 88 runtime cells planned;
- metadata drafts prepared;
- initial duplicate search completed;
- one usable generated full-body base concept produced in the previous chat;
- detailed new-conversation execution and acceptance plan prepared.

Still required:

- re-upload and approve the generated canonical base;
- create and approve `idle`, `waving` and `review` identity-validation rows;
- create the remaining six standard animation rows;
- create four cardinal look anchors and sixteen look directions;
- assemble and visually inspect the exact `1536x2288` atlas;
- finalize metadata, run repository validation and installation tests;
- create a clean final branch and ready-for-review pull request.

## Current decisions

- Runtime target: Codex Pet **v2**
- Atlas target: `1536x2288`, `8 columns x 11 rows`, `88` cells total
- Cell size: `192x208`
- Main visual variant: pink spring outfit with hat
- Secondary visual variant: blue sailor outfit, postponed to a separate package or later variant
- Art direction: compact plush/chibi fan art, transparent background, no readable text or logos
- Submitter credit: `Elio` / `@elio-zwd`
- Repository usage: non-commercial fan use only

## Reference and asset handling

The three supplied images are private-chat references and are intentionally **not committed** to this public repository. They are used only to identify proportions, palette, costume cues, expression and movement. Final pixels must be independently generated rather than copied, cropped, traced or redistributed from the references.

The generated base concept is also a production work asset rather than part of the final three-file package. It should be uploaded directly into the new private conversation, used as the canonical grounding image, and kept out of the final contributor PR.

## Duplicate check

At planning time, no existing `LinaBell`, `Linabell` or `玲娜贝儿` entry was found in `pets.json`, open issues or pull requests in this repository. Repeat the duplicate check immediately before opening the final pull request.

## Branch policy

Planning branch:

```text
feat/linabell-pet-direction-a
```

Recommended clean final branch, created from the latest `main` only after visual approval:

```text
feat/add-linabell-pet-v2
```

Do not merge this planning branch into the final submission branch. Copy only the approved final three-file package onto the clean branch.

Do not open a finished submission pull request until the user has reviewed the final contact sheet and the final package passes all required repository validation and installation checks.
