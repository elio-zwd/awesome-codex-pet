# LinaBell v2 Action and Frame Plan

## Runtime constraints

The Codex Pet v2 atlas has a fixed `8 x 11` layout:

- rows `0-8`: nine standard animation states, eight frames each;
- rows `9-10`: sixteen clockwise look directions;
- total final cells: `88`;
- final atlas: `1536x2288`;
- each cell: `192x208`.

The pet can feel action-rich by giving every eight-frame row a clear mini-performance while preserving the runtime's required state meanings.

## Standard action rows

| Row | Runtime state | LinaBell performance | Main visual beats |
| ---: | --- | --- | --- |
| 0 | `idle` | Calm curious idle | breathing, blink, tiny ear twitch, restrained tail sway |
| 1 | `running-right` | Cheerful rightward run | alternating feet, slight body bounce, ears/tail counter-motion |
| 2 | `running-left` | Cheerful leftward run | generated separately if asymmetric hat/flower makes mirroring unsafe |
| 3 | `waving` | Friendly broad paw wave | paw rises, two wave beats, smile, returns to neutral |
| 4 | `jumping` | Excited hop | crouch, launch, apex, gentle landing, recovery |
| 5 | `failed` | Cute disappointed recovery | ears lower, body slumps, brief sad face, self-composes |
| 6 | `waiting` | Patient planner | holds clipboard close, glances aside, tiny foot/ear movement |
| 7 | `running` | Front-facing eager scamper | quick in-place scamper with forward energy, distinct from side runs |
| 8 | `review` | Curious detective review | raises magnifying glass, inspects clipboard, satisfied nod |

## Per-frame choreography

### Row 0 — idle

1. neutral full-body pose;
2. slight inhale, shoulders rise minimally;
3. soft blink begins;
4. eyes closed, one ear tilts a few degrees;
5. eyes reopen, tail shifts slightly;
6. tiny curious head tilt;
7. return through centered pose;
8. near-neutral loop closure.

Rules: no props, no waving, no stepping, no large motion. The motion must remain visible but low-distraction.

### Row 1 — running-right

1. rightward anticipation, front foot reaches;
2. opposite foot pushes, body lowers;
3. passing pose;
4. airborne/up pose, ears and skirt lag;
5. opposite contact;
6. opposite push;
7. second passing pose;
8. second airborne/up pose, ready to loop.

Rules: feet must alternate naturally; tail counter-swings without crossing the cell edge; hat remains attached and stable.

### Row 2 — running-left

Use the same gait timing as row 1 but preserve the canonical side of the hat decoration and costume asymmetry. A simple horizontal mirror is allowed only if visual review confirms that the character identity and decorative placement remain acceptable. Otherwise generate the row independently.

### Row 3 — waving

1. neutral smile;
2. waving paw begins to rise;
3. paw reaches greeting height;
4. paw rotates outward;
5. paw rotates inward;
6. second outward wave with brighter smile;
7. paw lowers;
8. returns to neutral.

Rules: communicate the wave only through the limb; no floating motion marks, sparkles or text.

### Row 4 — jumping

1. neutral;
2. crouch with bent knees and compressed body;
3. launch upward;
4. rising pose;
5. apex with happy expression and compact limbs;
6. descending pose;
7. soft landing crouch;
8. recover toward neutral.

Rules: no floor shadow, dust, impact burst or detached effect.

### Row 5 — failed

1. confident neutral;
2. realization, eyes widen slightly;
3. ears lower and shoulders slump;
4. deepest disappointed pose;
5. small attached tear at eye edge or no effect;
6. takes a breath and lifts head;
7. ears begin to recover;
8. calm recovery pose suitable for looping.

Rules: keep the emotion cute and readable, not distressing; avoid loose tears, floating punctuation and detached stars.

### Row 6 — waiting

1. holds a small blank clipboard close to body;
2. glances screen-left;
3. returns center;
4. glances screen-right;
5. subtle foot or tail shift;
6. checks the blank clipboard briefly;
7. attentive forward look;
8. returns to start.

Rules: clipboard must stay attached to the paw/body silhouette; no readable text; waiting should feel patient rather than like the full review action.

### Row 7 — running

1. front-facing ready pose;
2. left foot forward, body dips;
3. center passing pose;
4. right foot forward, body rises;
5. left foot forward with stronger energy;
6. center passing pose;
7. right foot forward;
8. compact loop closure.

Rules: use an in-place eager scamper or slight three-quarter forward motion so it is visually distinct from rows 1 and 2.

### Row 8 — review

1. attentive neutral with blank clipboard;
2. raises small magnifying glass;
3. leans toward clipboard;
4. scans the upper area;
5. scans the lower area;
6. thoughtful head tilt;
7. satisfied nod/smile;
8. returns to attentive neutral.

Rules: magnifying glass and clipboard stay physically connected to the character; no readable writing, UI or floating symbols.

## Look-direction rows

The final sixteen cells rotate clockwise in `22.5°` steps. Direction means where the character looks/turns, not where it moves.

### Row 9

`000° up`, `022.5°`, `045°`, `067.5°`, `090° screen-right`, `112.5°`, `135°`, `157.5°`

### Row 10

`180° down`, `202.5°`, `225°`, `247.5°`, `270° screen-left`, `292.5°`, `315°`, `337.5°`

Before producing the two look rows, approve four cardinal anchors in this order:

1. `000°` up;
2. `090°` screen-right;
3. `180°` down;
4. `270°` screen-left.

The large ears, hat brim, face patches and tail must rotate coherently. The rear-facing directions need a deliberate design because no rear-view reference was supplied.

## Extra richness outside the runtime atlas

The following may be generated locally for exploration and QA but must not be committed inside the final pet directory:

- 3-4 canonical base-art candidates;
- face and expression exploration sheet;
- hat/flower placement turnaround;
- tail-volume turnaround;
- prop scale tests for magnifying glass and clipboard;
- one contact sheet for all 88 final cells;
- motion previews for every standard row;
- checkerboard, dark-background and light-background edge previews.

These extra images improve selection quality without violating the fixed runtime action set.

## Acceptance criteria per row

Every row must pass all of the following:

- eight distinct frames with coherent timing;
- same character identity, proportions, outfit and material;
- stable baseline except where vertical motion is intentional;
- no cropped ears, paws, skirt or tail;
- no frame crossing into neighboring cells;
- no accidental transparent holes inside the body;
- no white, green, cyan, purple or magenta edge residue;
- clean loop from frame 8 back to frame 1;
- state meaning readable at actual desktop-pet size.