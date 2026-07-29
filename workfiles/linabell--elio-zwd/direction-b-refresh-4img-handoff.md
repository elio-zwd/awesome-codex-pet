# LinaBell Direction B：四图 Refresh 交接

## 项目背景

项目此前已完成一轮视觉 baseline 审批，已批准 idle、waving 与 review；其中 review 曾修复“第三只手”问题，最终采用过替换后的 image1 版本。

现进入 `refresh-4img` 新阶段：用户表示已取得四张更好的新图片，需要先重新评估视觉基线，再决定是否继续后续动作生产。

## 当前状态

`refresh-3img-baseline-adopted-identity-rows-qa-awaiting-user-approval`

已完成：在 refresh planning / production 分支创建本轮 plan、tasks、handoff 文档；接收并完成 idle / waving / review 三个候选图的 intake 与视觉 QA，结果记录于 `direction-b-refresh-3img-intake-and-qa.md`。用户已取消第 4 张输入，且已采用这三图定义的身份家族为新的 production baseline。

已完成但待批准：identity-row 候选 01 已将 idle（6 帧）、waving（4 帧）及新生成的无道具 review（6 帧）透明化、注册并组装为 `1536 × 208` 单行。三行均通过结构检查（零错误）；未用格均为完全透明。`stable-slots` 策略留下的三条预期提示需要结合循环预览完成最终视觉确认。详细记录见 `direction-b-refresh-identity-rows-attempt-01-qa.md`。

## 下一步

用户已选择 screen-space 交替验收并批准 running-right 候选 03。该行已完成透明拆帧、`192 × 208` 注册、`1536 × 208` 单行组装和深色 QA 联系表/循环预览；结构检查零错误、零警告。此前候选及锚点仍不进入生产素材。

下一步：请用户查看 `runs/identity-rows-attempt-01/qa/identity-rows-contact-sheet-dark.png` 及三个循环预览，并对 idle / waving / review 统一批准或提出修改。仅在这三行批准后，继续 R5 的 running-left、running、jumping、failed、waiting。

## 重要边界

- 私人原始参考图只用于本地视觉判断，不提交、不裁切、不描摹、不复用像素。
- 蓝色水手服不混入主图集。
- 最终 clean PR 只允许 `submission.json`、`pet.json`、`spritesheet.webp` 三个运行时文件；本 refresh 分支不创建最终 PR。
