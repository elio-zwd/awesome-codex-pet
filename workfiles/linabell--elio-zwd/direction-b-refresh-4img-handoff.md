# LinaBell Direction B：四图 Refresh 交接

## 项目背景

项目此前已完成一轮视觉 baseline 审批，已批准 idle、waving 与 review；其中 review 曾修复“第三只手”问题，最终采用过替换后的 image1 版本。

现进入 `refresh-4img` 新阶段：用户表示已取得四张更好的新图片，需要先重新评估视觉基线，再决定是否继续后续动作生产。

## 当前状态

`refresh-4img-three-image-qa-complete-fourth-pending-running-right-prompt-repair-drafted`

已完成：在 refresh planning / production 分支创建本轮 plan、tasks、handoff 文档；接收并完成 idle / waving / review 三个候选图的阶段性 intake 与视觉 QA，结果记录于 `direction-b-refresh-3img-intake-and-qa.md`。

未完成：第 4 张新图尚未提供，完整四图 intake、四图视觉 QA 与最终 adopt / reject 决策均未完成。前三图的 review 候选有新增剪贴板，若采用新身份家族，review 必须无道具重做。另有一个 running-right 本地候选因重复跨步、未呈现对侧四肢交替且出现下蹲而判定不合格；待用户确认修复 prompt 后才可重新生成。

## 下一步

接收第 4 张图，完成四图视觉基线评估；用户确认后，使用 `direction-b-refresh-running-right-prompt-repair.md` 中的修复 prompt 重新生成 running-right 候选。评估完成后：

- 若 adopt：将其标为新的 production baseline，核对旧 idle / waving / review 是否仍一致；不一致则重做，并在用户批准三行 identity QA 后继续其余动作。
- 若 reject：记录具体原因，明确继续沿用此前 baseline，并从 running-right 继续推进。

## 重要边界

- 私人原始参考图只用于本地视觉判断，不提交、不裁切、不描摹、不复用像素。
- 蓝色水手服不混入主图集。
- 最终 clean PR 只允许 `submission.json`、`pet.json`、`spritesheet.webp` 三个运行时文件；本 refresh 分支不创建最终 PR。
