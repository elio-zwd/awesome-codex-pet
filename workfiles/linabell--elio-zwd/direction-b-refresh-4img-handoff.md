# LinaBell Direction B：四图 Refresh 交接

## 项目背景

项目此前已完成一轮视觉 baseline 审批，已批准 idle、waving 与 review；其中 review 曾修复“第三只手”问题，最终采用过替换后的 image1 版本。

现进入 `refresh-4img` 新阶段：用户表示已取得四张更好的新图片，需要先重新评估视觉基线，再决定是否继续后续动作生产。

## 当前状态

`refresh-4img-intake-pending`

已完成：在 refresh planning / production 分支创建本轮 plan、tasks、handoff 文档。

未完成：四张新图尚未随当前任务提供，尚未进行 intake、视觉 QA 或 adopt / reject 决策。

## 下一步

接收这四张图并进行新视觉基线评估。评估完成后：

- 若 adopt：将其标为新的 production baseline，核对旧 idle / waving / review 是否仍一致；不一致则重做，并在用户批准三行 identity QA 后继续其余动作。
- 若 reject：记录具体原因，明确继续沿用此前 baseline，并从 running-right 继续推进。

## 重要边界

- 私人原始参考图只用于本地视觉判断，不提交、不裁切、不描摹、不复用像素。
- 蓝色水手服不混入主图集。
- 最终 clean PR 只允许 `submission.json`、`pet.json`、`spritesheet.webp` 三个运行时文件；本 refresh 分支不创建最终 PR。

