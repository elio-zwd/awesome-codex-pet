# LinaBell Direction B：四图 Refresh 交接

## 项目背景

项目此前已完成一轮视觉 baseline 审批，已批准 idle、waving 与 review；其中 review 曾修复“第三只手”问题，最终采用过替换后的 image1 版本。

现进入 `refresh-4img` 新阶段：用户表示已取得四张更好的新图片，需要先重新评估视觉基线，再决定是否继续后续动作生产。

## 当前状态

`refresh-3img-baseline-adopted-running-right-attempt-01-rejected-motion-anchor-pending`

已完成：在 refresh planning / production 分支创建本轮 plan、tasks、handoff 文档；接收并完成 idle / waving / review 三个候选图的 intake 与视觉 QA，结果记录于 `direction-b-refresh-3img-intake-and-qa.md`。用户已取消第 4 张输入，且已采用这三图定义的身份家族为新的 production baseline。

未完成：新基线的 identity rows 尚未统一为透明生产行，review 必须无道具重做。旧 running-right 候选与本地重新生成的候选 01 均不合格：候选 01 虽改善下蹲，却仍未呈现可辨认的对侧四肢交替。候选 01 的 QA 详见 `direction-b-refresh-running-right-local-attempt-01-qa.md`。

## 下一步

先准备非运行时的 8 格步态姿势锚点，作为生成 `running-right` 的 motion/layout reference；再结合三张已采用的本地身份参考图，重新生成完整候选并执行逐帧动作 QA。候选 01 不进入拆帧或生产素材。之后：

- 若 adopt：将其标为新的 production baseline，核对旧 idle / waving / review 是否仍一致；不一致则重做，并在用户批准三行 identity QA 后继续其余动作。
- 若 reject：记录具体原因，明确继续沿用此前 baseline，并从 running-right 继续推进。

## 重要边界

- 私人原始参考图只用于本地视觉判断，不提交、不裁切、不描摹、不复用像素。
- 蓝色水手服不混入主图集。
- 最终 clean PR 只允许 `submission.json`、`pet.json`、`spritesheet.webp` 三个运行时文件；本 refresh 分支不创建最终 PR。
