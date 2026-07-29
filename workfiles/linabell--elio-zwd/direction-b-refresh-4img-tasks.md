# LinaBell Direction B：四图 Refresh 任务清单

- [x] R0 refresh branch bootstrap：拉取远端并切换至 `feat/linabell-pet-direction-b-refresh-4img`；创建本轮规划、任务和交接文档。
- [ ] R1 four-image intake：已接收 idle / waving / review 三张并记录候选类别与参考使用边界；待接收第 4 张后完成。
- [ ] R2 four-image visual QA：已完成前三图身份特征、材质/渲染一致性及桌宠尺寸可读性的阶段性 QA；待第 4 张后完成完整四图 QA。
- [ ] R3 baseline decision：记录 adopt 新四图为 production baseline，或 reject 并保留旧 baseline 的明确依据。
- [ ] R4 identity-row reconciliation：若 adopt，核对/重做 idle、waving、review；统一为透明背景、单帧 `192 × 208`、单行 `1536 × 208`，并生成三行 QA 联系表和预览，等待用户批准。
- [ ] R5 remaining standard rows：在 identity rows 获批后制作 running-right、running-left、running、jumping、failed、waiting。已诊断一个不合格的 running-right 本地候选并写出待确认修复 prompt；该候选未计为完成素材。
- [ ] R6 directions：制作四方向锚点与十六方向环视。
- [ ] R7 final assembly and validation：组装 v2 `1536 × 2288` 图集，执行验证，准备 clean PR 所需三件套；不在本分支创建最终 PR。

## 当前状态

`R0` 已完成。`R1`、`R2` 正在进行：前三图 QA 已记录，等待第 4 张。`R3`、`R4`、`R6`、`R7` 尚未开始。`R5` 尚未开始生产：一个 running-right 本地候选已被判为不合格，修复 prompt 待用户确认，未生成或拆帧任何可用生产素材。
