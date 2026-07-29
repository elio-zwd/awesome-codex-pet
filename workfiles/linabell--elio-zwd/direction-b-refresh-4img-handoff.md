# LinaBell Direction B：四图 Refresh 交接

## 项目背景

项目此前已完成一轮视觉 baseline 审批，已批准 idle、waving 与 review；其中 review 曾修复“第三只手”问题，最终采用过替换后的 image1 版本。

现进入 `refresh-4img` 新阶段：用户表示已取得四张更好的新图片，需要先重新评估视觉基线，再决定是否继续后续动作生产。

## 当前状态

`refresh-3img-baseline-adopted-standard-rows-qa-awaiting-user-review`

已完成：在 refresh planning / production 分支创建本轮 plan、tasks、handoff 文档；接收并完成 idle / waving / review 三个候选图的 intake 与视觉 QA，结果记录于 `direction-b-refresh-3img-intake-and-qa.md`。用户已取消第 4 张输入，且已采用这三图定义的身份家族为新的 production baseline。

已完成：用户以“继续下一步”确认 identity rows。idle（6 帧）、waving（4 帧）及无道具 review（6 帧）已透明化、注册并组装为 `1536 × 208` 单行；三行均通过结构检查，未用格均为完全透明。详细记录见 `direction-b-refresh-identity-rows-attempt-01-qa.md`。

R5 已完成：running-right、完整独立生成的 running-left、jumping、failed、waiting、non-directional running 均通过增量及汇总结构检查。初始逐帧镜像的 running-left 因深色 QA 联系表中的尾尖分离碎片被拒绝，后续独立生成行替代该候选。running 的初始两次生成均被安全系统拒绝；用户授权无名称、原地专注处理策略后，成功生成并通过 6 帧候选。详情见 `direction-b-refresh-r5-standard-rows-attempt-01-qa.md`。

## 下一步

下一步：请用户审看 `runs/production-v2-attempt-01/qa/contact-sheet-standard.png` 及需要的循环预览。确认后继续 R6 四方向锚点与十六方向环视；本分支仍不创建最终 PR。

## 重要边界

- 私人原始参考图只用于本地视觉判断，不提交、不裁切、不描摹、不复用像素。
- 蓝色水手服不混入主图集。
- 最终 clean PR 只允许 `submission.json`、`pet.json`、`spritesheet.webp` 三个运行时文件；本 refresh 分支不创建最终 PR。
