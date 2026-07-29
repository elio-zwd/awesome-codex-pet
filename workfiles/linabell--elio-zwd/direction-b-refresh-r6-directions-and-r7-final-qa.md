# LinaBell Direction B：R6 方向与 R7 最终 QA

## R6：方向制作

- 已制作 000°、090°、180°、270° 四方向锚点，并据此完成 16 格环视。
- 环视行按 000°–157.5°、180°–337.5° 排列。
- 初版左侧中间的 247.5° / 292.5° 上下语义在盲测中出现歧义；未接受尺度跳变更大的两格修复，而是重做 225°–292.5° 的连续四格。
- 重做后的无标签 A/B 盲测由三名独立复核者完成，所有水平与垂直配对均通过，无警告、无待确认项。结果见 `runs/production-v2-attempt-01/qa/direction-blind-validation-r6.json`。

## R7：最终组装与验证

- 最终候选：`runs/production-v2-attempt-01/final/spritesheet-extended-final.webp`
- 图集：1536 × 2288，8 × 11，单格 192 × 208，RGBA WEBP，`spriteVersionNumber: 2`。
- 透明边缘已执行紫色抠图去溢色；结构验证无 errors、无 warnings，见 `final/validation-extended-final.json`。
- 最终视觉 QA 通过：形象一致、脚部基线稳定、动作可读、帽子/尾巴/肢体完整，16 方向连续且可辨。详细 QA 输入位于 `qa/contact-sheet-extended-final.png`、`qa/look-directions-final.png`、`qa/previews-final/`。

## 边界与交接

本记录及所有素材均为 planning / production 分支 workfiles。没有提交私人原始参考图，没有使用蓝色水手服，也没有创建最终 PR。进入 clean PR 时只可转入 `submission.json`、`pet.json` 和 `spritesheet.webp` 三件套。
