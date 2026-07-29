# LinaBell Direction B：四图 Refresh 交接

## 项目背景

项目此前已完成一轮视觉 baseline 审批，已批准 idle、waving 与 review；其中 review 曾修复“第三只手”问题，最终采用过替换后的 image1 版本。

现进入 `refresh-4img` 新阶段：用户表示已取得四张更好的新图片，需要先重新评估视觉基线，再决定是否继续后续动作生产。

## 当前状态

`refresh-3img-baseline-adopted-running-right-motion-anchors-rejected-user-decision-needed`

已完成：在 refresh planning / production 分支创建本轮 plan、tasks、handoff 文档；接收并完成 idle / waving / review 三个候选图的 intake 与视觉 QA，结果记录于 `direction-b-refresh-3img-intake-and-qa.md`。用户已取消第 4 张输入，且已采用这三图定义的身份家族为新的 production baseline。

未完成：新基线的 identity rows 尚未统一为透明生产行，review 必须无道具重做。旧 running-right 候选、候选 01 与候选 02 均不合格：候选 01 改善下蹲却未呈现对侧四肢交替；候选 02 与三种新增步态锚点策略仍不能使 A/B 接触相在桌宠尺寸下可读。完整证据详见 `direction-b-refresh-running-right-local-attempt-01-qa.md` 和 `direction-b-refresh-running-right-attempt-02-and-anchor-qa.md`。

## 下一步

等待用户提供真正可辨认的右向 A/B 两姿动作参考，或允许稳定视觉区分远侧肢体，或调整“物理侧别”验收口径；再为 `running-right` 选择新的生成策略。现有候选及锚点均不进入拆帧或生产素材。之后：

- 若 adopt：将其标为新的 production baseline，核对旧 idle / waving / review 是否仍一致；不一致则重做，并在用户批准三行 identity QA 后继续其余动作。
- 若 reject：记录具体原因，明确继续沿用此前 baseline，并从 running-right 继续推进。

## 重要边界

- 私人原始参考图只用于本地视觉判断，不提交、不裁切、不描摹、不复用像素。
- 蓝色水手服不混入主图集。
- 最终 clean PR 只允许 `submission.json`、`pet.json`、`spritesheet.webp` 三个运行时文件；本 refresh 分支不创建最终 PR。
