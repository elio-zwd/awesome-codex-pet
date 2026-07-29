# LinaBell Direction B：四图 Refresh 任务清单

- [x] R0 refresh branch bootstrap：拉取远端并切换至 `feat/linabell-pet-direction-b-refresh-4img`；创建本轮规划、任务和交接文档。
- [x] R1 three-image intake（原 four-image intake）：用户取消第 4 张输入；已接收 idle / waving / review 三张并记录候选类别与参考使用边界。
- [x] R2 three-image visual QA（原 four-image visual QA）：用户取消第 4 张输入；已完成完整范围内的身份特征、材质/渲染一致性及桌宠尺寸可读性 QA。
- [x] R3 baseline decision：adopt 三图定义的新粉色毛绒 LinaBell 身份家族为 production baseline；review 的新增剪贴板不进入最终 production row。
- [x] R4 identity-row reconciliation：用户以“继续下一步”确认三行 identity QA；idle（6 帧）、waving（4 帧）、无道具 review（6 帧）已成为透明生产候选。
- [x] R5 remaining standard rows：running-right、独立生成的 running-left、jumping、failed、waiting、non-directional running 均已完成候选生产和增量结构检查。running 使用用户批准的无名称原地专注处理策略；镜像版 running-left 因尾尖分离碎片已拒绝，不计入生产素材。
- [ ] R6 directions：制作四方向锚点与十六方向环视。
- [ ] R7 final assembly and validation：组装 v2 `1536 × 2288` 图集，执行验证，准备 clean PR 所需三件套；不在本分支创建最终 PR。

## 当前状态

`R0` 至 `R5` 已完成。九条标准行动画均已通过汇总结构检查，标准 8 × 9 联系表与循环预览已生成；它们仍是 planning / production QA 产物。`R6`、`R7` 未开始，等待用户审看标准行后继续。
