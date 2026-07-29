# LinaBell Direction B：R5 标准动作候选 01 QA

## 阶段结论

用户以“继续下一步”确认继续身份行后的 R5 生产。用户随后明确授权以无名称、原地专注处理策略重试 non-directional running。九条标准行动画现已齐全并通过汇总结构检查；当前等待用户审看标准 8 × 9 联系表后再进入方向环视。

## 已通过的行

| 行 | 帧数 | 来源与处理 | 结构检查 |
| --- | ---: | --- | --- |
| running-right | 8 | 先前已批准的候选 03 | 零错误、零警告 |
| running-left | 8 | 初始逐帧镜像候选被拒绝后，改用完整独立生成的 8 帧行 | 零错误、零警告 |
| jumping | 5 | 新生成，预备/上升/最高点/下降/落地姿态 | 零错误、零警告 |
| failed | 8 | 新生成的失败情绪循环，无浮动符号或独立特效 | 零错误、零警告 |
| waiting | 6 | 新生成的期待式询问循环，无新道具 | 零错误、零警告 |
| running | 6 | 用户批准的无名称、双脚原地专注处理循环 | 零错误、零警告 |

所有已通过帧均为透明 `192 × 208`。已形成 `running-left` 的透明 `1536 × 208` 行、深色联系表与循环预览。

## 镜像候选修复记录

running-left 的初始逐帧镜像在结构检查中未报错，但深色联系表显示多个帧有可见的脱离尾尖碎片。这是视觉 QA 的硬失败，因此没有将其作为生产行使用。随后重新生成完整的 coherent 8 帧 leftward row；新行尾巴与奶油色尾尖在每帧均保持连接，且左向步相可读。

## non-directional running：无名称策略解决

`running` 是积极处理/思考状态，不是字面跑步。最初行 prompt 的两次内置生成均被安全系统拒绝且未产生文件。用户随后授权新的无名称策略：提示不出现角色、系列、产品、应用、代码或品牌名称，只以已批准的视觉参考锁定身份，并指定双脚原地的六帧专注微循环。

该策略成功产生 6 帧候选，包含直立专注、微低头、双爪靠胸、抬头确认、轻点头及闭环中性姿态。帧结构检查零错误、零警告；未使用其他动作行、手工拼图或本地绘制作为替代品。重试提示保存在 `runs/production-v2-attempt-01/prompts/row-retries/running-unnamed-focused.md`。

## QA 产物

- 标准 8 × 9 联系表：`runs/production-v2-attempt-01/qa/contact-sheet-standard.png`
- 九行循环预览：`runs/production-v2-attempt-01/qa/previews/`
- 左向行联系表与预览：`runs/production-v2-attempt-01/qa/running-left-contact-sheet-dark.png`、`runs/production-v2-attempt-01/qa/running-left-preview-dark.gif`
- 已通过帧的汇总结构检查：`runs/production-v2-attempt-01/qa/review.json`
- 各新生成行的增量检查：`runs/production-v2-attempt-01/qa/rows/`

`final/spritesheet-standard.webp` 是标准 8 × 9 中间图集，仅用于本轮 QA；尚未包含 v2 环视行，不是可发布或可安装的最终成品。
