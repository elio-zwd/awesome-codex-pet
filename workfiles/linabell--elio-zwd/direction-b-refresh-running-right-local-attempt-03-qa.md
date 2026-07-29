# LinaBell Direction B：running-right 本地候选 03 QA

## 产物

- 候选：`candidates/running-right-local-attempt-03-screen-space.png`
- 输入：三张已采用的 LinaBell 身份参考图。
- 该图为 planning 分支的 AI 生成候选；不是最终透明行、未拆帧、未进入 `pets/`。

## 验收口径

用户已明确选择 **screen-space 交替**：只检查屏幕上可读的腿部前后摆动、前爪摆动、帧间轮廓变化和循环节奏；不要求证明在二维最终图像中不可见的 near/far 物理侧别。

## QA 结果

**通过：用户已批准候选 03 的 screen-space 跑步节奏。**

| 项目 | 结论 | 说明 |
| --- | --- | --- |
| 身份锁定 | 通过 | 帽饰方向、粉色毛绒材质、服装、绿色蝴蝶结、樱桃、裙摆和尾巴均与新 baseline 一致。 |
| 右向与无下蹲 | 通过 | 全部帧朝 screen-right，躯干直立；未见蹲伏、坐姿、跳跃或蓝色水手服。 |
| screen-space 腿部节奏 | 通过 | 序列中存在长跨步、收脚/ passing、抬膝过渡和回到接触前姿的可读变化。 |
| screen-space 前爪节奏 | 通过 | 前爪在前伸、收回和靠近躯干之间变化，未保持单一固定拳姿。 |
| 帧多样性与循环 | 已批准 | 若干长跨步帧仍相近；用户已按 screen-space 验收口径批准其整体节奏。 |
| 生产几何 | 通过 | 8 帧均以 connected-components 方式提取为透明 `192 × 208` PNG；`inspect_frames.py --require-components` 返回零错误、零警告。 |

## 本地行级产物

| 产物 | 路径 | 状态 |
| --- | --- | --- |
| 透明单帧 | `runs/running-right-attempt-03/frames/running-right/00.png` 至 `07.png` | 8 帧均为 `192 × 208`。 |
| 透明单行 | `runs/running-right-attempt-03/row/running-right.png` | `1536 × 208`，按 00–07 从左至右排列。 |
| 深色 QA 联系表 | `runs/running-right-attempt-03/qa/running-right-contact-sheet-dark.png` | 仅供透明边缘与帧间对照。 |
| 深色循环预览 | `runs/running-right-attempt-03/qa/running-right-preview-dark.gif` | 仅供动作 QA。 |
| 结构检查 | `runs/running-right-attempt-03/qa/review.json` | 零错误、零警告。 |

原始 2×4 AI 候选被无损重排为横向 8 帧条带后才输入标准提取脚本；此步骤不改变角色像素或生成新角色内容。该行仍是 planning 分支中的待审 production candidate，尚未写入最终图集。

## 下一步

已完成用户批准、透明拆帧和行级 QA。下一步应先完成 identity-row reconciliation（尤其无新增道具的 review），再继续其余 standard rows；本行在最终 8×11 assembly 前仍须与完整标准行集一起复检。
