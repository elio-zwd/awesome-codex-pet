# LinaBell Direction B：四图 Refresh 任务清单

- [x] R0 refresh branch bootstrap：拉取远端并切换至 `feat/linabell-pet-direction-b-refresh-4img`；创建本轮规划、任务和交接文档。
- [ ] R1 four-image intake：接收四张新图，记录其候选类别与参考使用边界。
- [ ] R2 four-image visual QA：逐图检查身份特征、材质/渲染一致性及桌宠尺寸可读性。
- [ ] R3 baseline decision：记录 adopt 新四图为 production baseline，或 reject 并保留旧 baseline 的明确依据。
- [ ] R4 identity-row reconciliation：若 adopt，核对/重做 idle、waving、review；统一为透明背景、单帧 `192 × 208`、单行 `1536 × 208`，并生成三行 QA 联系表和预览，等待用户批准。
- [ ] R5 remaining standard rows：在 identity rows 获批后制作 running-right、running-left、running、jumping、failed、waiting。
- [ ] R6 directions：制作四方向锚点与十六方向环视。
- [ ] R7 final assembly and validation：组装 v2 `1536 × 2288` 图集，执行验证，准备 clean PR 所需三件套；不在本分支创建最终 PR。

## 当前状态

`R0` 已完成。`R1` 至 `R7` 均未开始，等待用户提供四张新图。

