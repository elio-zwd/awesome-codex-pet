# LinaBell Direction B：四图 Refresh 任务清单

- [x] R0 refresh branch bootstrap：拉取远端并切换至 `feat/linabell-pet-direction-b-refresh-4img`；创建本轮规划、任务和交接文档。
- [x] R1 three-image intake（原 four-image intake）：用户取消第 4 张输入；已接收 idle / waving / review 三张并记录候选类别与参考使用边界。
- [x] R2 three-image visual QA（原 four-image visual QA）：用户取消第 4 张输入；已完成完整范围内的身份特征、材质/渲染一致性及桌宠尺寸可读性 QA。
- [x] R3 baseline decision：adopt 三图定义的新粉色毛绒 LinaBell 身份家族为 production baseline；review 的新增剪贴板不进入最终 production row。
- [ ] R4 identity-row reconciliation：若 adopt，核对/重做 idle、waving、review；统一为透明背景、单帧 `192 × 208`、单行 `1536 × 208`，并生成三行 QA 联系表和预览，等待用户批准。
- [ ] R5 remaining standard rows：在 identity rows 获批后制作 running-right、running-left、running、jumping、failed、waiting。已诊断一个不合格的 running-right 本地候选并写出待确认修复 prompt；该候选未计为完成素材。
- [ ] R6 directions：制作四方向锚点与十六方向环视。
- [ ] R7 final assembly and validation：组装 v2 `1536 × 2288` 图集，执行验证，准备 clean PR 所需三件套；不在本分支创建最终 PR。

## 当前状态

`R0` 至 `R3` 已完成。`R4` 尚未完成：新基线的 identity rows 仍需统一为透明生产行，其中 review 必须无道具重做。`R5` 已完成两次本地 running-right 候选和三种角色/通用步态锚点策略的 QA，均未通过可辨认的 A/B 对侧肢体交替验收；等待用户提供明确 A/B 动作参考、允许稳定视觉区分，或调整验收口径。`R6`、`R7` 未开始。
