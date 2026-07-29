# LinaBell Direction B：running-right Prompt 修复

## 本轮诊断范围

本记录评估用户本机提供的一张 `1536 × 1024`、2 行 × 4 列的 running-right 候选图。原图仅作本地 QA，未复制、裁切、描摹或复用其像素。

该候选未通过 running-right 动作 QA，不能作为 production row。

## 失败结论

1. **未形成清晰的两相交替步态。** 多个长跨步帧仍然是相近的“右前腿前伸、同一前爪前摆”的构图；看不出对应的另一条腿和另一只前爪在第二半周期接管前伸。
2. **压缩帧变成了下蹲。** 原 prompt 的 `compression`、`body moves lower`、`legs tuck underneath` 与 `airborne` 组合，让模型把正常跑步的轻微重心下降解释成深屈膝/蹲伏和跳跃准备。
3. **近侧/远侧肢体没有可验证的身份锁。** “opposite physical leg/paw” 对二维生成模型过于抽象；裙摆和尾巴又遮挡了远侧腿，使视觉上无法验证四肢交替。

## 修复策略

- 用 **near side（面向观众的一侧）** 与 **far side（被躯干遮挡的一侧）** 固定四肢，而不是仅说“opposite”。
- 把每帧的前后关系写成一张 gait table，并要求两个接触相位为互换关系。
- 移除“身体到达最高点”“双脚离地并缩起”的强跳跃措辞；若出现短暂腾空，髋部只能轻微上浮，不能变成跳跃或蹲跳。
- 将镜头锁为清晰右向侧视或很轻微的三分之四侧视；两条腿必须在裙摆下分别可读，尾巴不得遮挡腿部。
- 强制四肢交叉配对：同一侧的前爪和后腿绝不能同时向 screen-right 前伸；near leg 前伸时 near forepaw 必须后摆，反之亦然。

## 可直接替换的 Prompt

```text
Use the approved new production visual baseline as the mandatory source of truth:
- the approved cleaned Idle row;
- the approved cleaned Waving row;
- the approved image 1 Review family.

Regenerate exactly one 8-frame `running-right` animation sheet for the same character.

This must be one seamless, ordinary rightward running cycle, not a jump, crouch, or bounding loop.
The prior attempt failed because it repeated one long-stride pose and did not visibly alternate the two legs and the two forepaws.

CHARACTER LOCK:
Preserve exactly the approved pink plush fox:
- oversized upright triangular ears;
- pastel-pink plush fur;
- cream-white eye patches and muzzle;
- bright blue eyes with eyelashes;
- small pink nose;
- pale pink floppy hat;
- white flower and pink bow on the same canonical side;
- pink-and-pale-yellow plaid short-sleeved top;
- green neck bow;
- paired cherry decoration;
- pink dotted skirt with lace trim;
- large fluffy pink tail with pale cream tip.

Keep the same high-detail 3D plush rendering style.
Do not introduce the blue sailor outfit.
Do not flip the asymmetric hat decoration.

OUTPUT LAYOUT:
Create exactly 8 poses total, one continuous animation cycle.
Arrange them as a precise 2-row by 4-column sheet:
- top row: frames 1, 2, 3, 4;
- bottom row: frames 5, 6, 7, 8.
Exactly four poses in each row. No extra candidates. No third row.
Use one uniform solid purple background #6A00FF. No gradient, scenery, floor, floor line, shadow, text, logos, effects, motion lines, or dust.

CAMERA, FACING, AND READABILITY LOCK:
- Every pose runs toward screen right.
- Use a clean right-facing side view or only a very slight three-quarter side view; never turn back toward the camera.
- Define `near side` as the viewer-facing side of the character and `far side` as the side behind the torso. Keep those side identities stable throughout all eight frames.
- Both legs must emerge separately below the skirt and be visually distinguishable. Both forepaws must be visibly separate or have unambiguous separate attachments at the shoulders.
- The tail remains behind the body on screen left and must not hide either leg.
- Keep one shared character scale and baseline. The torso stays upright, with at most a slight forward running lean.
- Never sit, kneel, crouch, squat, tuck into a ball, or make a high jump. The hip height may change only slightly between frames; the hat, head, and skirt must not drop dramatically.

NON-NEGOTIABLE CROSS-LATERAL RULE:
For a normal biped run, a forepaw and a hind leg on the SAME physical side must never both swing forward toward screen right.
- When the near hind leg is forward, the near forepaw is back, and the far forepaw is forward.
- When the far hind leg is forward, the far forepaw is back, and the near forepaw is forward.
Frame 1 and frame 5 must be anatomically opposite contact phases, not near-duplicates.

EXACT EIGHT-FRAME GAIT TABLE:

Frame 1 — contact A:
- near hind leg reaches forward toward screen right and is the lead contact;
- far hind leg extends backward toward screen left;
- near forepaw swings backward; far forepaw swings forward;
- upright torso, no squat.

Frame 2 — down A:
- retain the same A-side relationship as frame 1;
- make only a small, springy compression: hips and skirt lower slightly, never into a crouch;
- legs move closer beneath the torso, while the near forepaw is still back and far forepaw still forward.

Frame 3 — passing A to B:
- near hind leg travels backward underneath the hip;
- far knee travels forward underneath the skirt;
- near forepaw now travels forward and far forepaw travels backward;
- this is a passing pose, not a tucked jump and not a seated pose.

Frame 4 — early flight B:
- far hind leg is now clearly the forward leg and near hind leg is clearly behind;
- near forepaw is forward and far forepaw is back;
- if both feet leave the ground, the lift is tiny and natural, never a high airborne leap.

Frame 5 — contact B:
- far hind leg reaches forward toward screen right and is the lead contact;
- near hind leg extends backward toward screen left;
- near forepaw swings forward; far forepaw swings backward;
- this must be visibly opposite to frame 1 in both leg and forepaw arrangement.

Frame 6 — down B:
- retain the B-side relationship from frame 5;
- use only a small elastic compression, never a deep knee bend, squat, or lowered seated silhouette.

Frame 7 — passing B to A:
- far hind leg travels backward underneath the hip;
- near knee travels forward underneath the skirt;
- near forepaw travels backward and far forepaw travels forward;
- keep the body upright and the legs readable below the skirt.

Frame 8 — pre-contact A for loop closure:
- near hind leg is bent forward, almost ready to become the forward contact in frame 1;
- far hind leg is back;
- near forepaw is back and far forepaw is forward;
- it may approach frame 1 but must not duplicate frame 1 exactly.

HARD QA REQUIREMENTS:
- Frames 1 and 5 are opposite contact poses: the lead hind leg and lead forepaw must switch physical sides.
- Frames 3 and 7 are opposite passing poses, with the lead knee and forepaw switch clearly visible.
- At least six frames have visibly different leg silhouettes.
- At least four frames have visibly different forepaw silhouettes.
- No same-side forepaw and hind leg may both point forward in any frame.
- The loop reads as rightward running at thumbnail size, with clear alternating rhythm rather than sliding, hopping, or repeated lunges.
- Keep all limbs anatomically correct: exactly two hind legs and exactly two forepaws, with plush paw shapes only and no human fingers.
```

## 使用条件

这是一份 **待用户确认的生成 prompt**，不是已执行的生产动作。确认后，才可使用已批准的新 production baseline 作为参考生成一个新的 running-right 候选，并对其进行逐帧 QA：两相接触姿、两相 passing 姿、首尾循环、腿部可读性、前爪/后腿对侧摆动、下蹲风险与透明化可行性。

