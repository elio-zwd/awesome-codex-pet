# LinaBell Direction B：R5 标准动作候选 01 QA

## 阶段结论

用户以“继续下一步”确认继续身份行后的 R5 生产。本轮已将 running-left、jumping、failed、waiting 纳入 production-v2 候选运行；非位移的 running 行在内置图像生成中连续两次被安全系统拒绝，未产出候选文件，因此 R5 尚未完成，不能进入方向环视或最终图集组装。

## 已通过的行

| 行 | 帧数 | 来源与处理 | 结构检查 |
| --- | ---: | --- | --- |
| running-right | 8 | 先前已批准的候选 03 | 零错误、零警告 |
| running-left | 8 | 初始逐帧镜像候选被拒绝后，改用完整独立生成的 8 帧行 | 零错误、零警告 |
| jumping | 5 | 新生成，预备/上升/最高点/下降/落地姿态 | 零错误、零警告 |
| failed | 8 | 新生成的失败情绪循环，无浮动符号或独立特效 | 零错误、零警告 |
| waiting | 6 | 新生成的期待式询问循环，无新道具 | 零错误、零警告 |

所有已通过帧均为透明 `192 × 208`。已形成 `running-left` 的透明 `1536 × 208` 行、深色联系表与循环预览。

## 镜像候选修复记录

running-left 的初始逐帧镜像在结构检查中未报错，但深色联系表显示多个帧有可见的脱离尾尖碎片。这是视觉 QA 的硬失败，因此没有将其作为生产行使用。随后重新生成完整的 coherent 8 帧 leftward row；新行尾巴与奶油色尾尖在每帧均保持连接，且左向步相可读。

## 当前阻塞：non-directional running

`running` 是 Codex 的“积极处理/思考”状态，不是字面跑步。已依照行 prompt 发起内置生成并按失败规则重试一次；两次均被安全系统拒绝，均未产生文件。没有使用其他动作行、手工拼图或本地绘制作为替代品。

需要用户确认新的生成路径（例如提供一张可用的工作姿态候选，或明确授权以不同的简短语义重新发起一个新的 running 候选策略）后，才能继续该行。

## QA 产物

- 部分标准行联系表：`runs/production-v2-attempt-01/qa/partial-standard-contact-sheet-dark.png`
- 左向行联系表与预览：`runs/production-v2-attempt-01/qa/running-left-contact-sheet-dark.png`、`runs/production-v2-attempt-01/qa/running-left-preview-dark.gif`
- 已通过帧的汇总结构检查：`runs/production-v2-attempt-01/qa/partial-standard-review.json`
- 各新生成行的增量检查：`runs/production-v2-attempt-01/qa/rows/`

部分标准行联系表按最终行顺序保留 9 行；第 7 行 `running` 被故意留空，以直观记录该阻塞。它不是可组装或可发布的中间图集。
