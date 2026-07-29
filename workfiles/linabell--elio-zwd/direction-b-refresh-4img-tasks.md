# LinaBell Direction B：四图 Refresh 任务清单

- [x] R0 refresh branch bootstrap：拉取远端并切换至 `feat/linabell-pet-direction-b-refresh-4img`；创建本轮规划、任务和交接文档。
- [x] R1 three-image intake（原 four-image intake）：用户取消第 4 张输入；已接收 idle / waving / review 三张并记录候选类别与参考使用边界。
- [x] R2 three-image visual QA（原 four-image visual QA）：用户取消第 4 张输入；已完成完整范围内的身份特征、材质/渲染一致性及桌宠尺寸可读性 QA。
- [x] R3 baseline decision：adopt 三图定义的新粉色毛绒 LinaBell 身份家族为 production baseline；review 的新增剪贴板不进入最终 production row。
- [x] R4 identity-row reconciliation：用户以“继续下一步”确认三行 identity QA；idle（6 帧）、waving（4 帧）、无道具 review（6 帧）已成为透明生产候选。
- [x] R5 remaining standard rows：running-right、独立生成的 running-left、jumping、failed、waiting、non-directional running 均已完成候选生产和增量结构检查。running 使用用户批准的无名称原地专注处理策略；镜像版 running-left 因尾尖分离碎片已拒绝，不计入生产素材。
- [x] R6 directions：四方向锚点、十六方向环视、三人盲测及方向语义 QA 均完成；左侧中间四格曾重做以消除上下语义歧义。
- [x] R7 final assembly and validation：已组装并验证 v2 `1536 × 2288` 正式图集，写入三件套并安装到本机 Codex；不在本分支创建最终 PR。
- [x] R8 motion-smoothing refresh：基于 Codex 运行时固定的播放节奏，重做默认 idle 的前六格与 waving 的前四格，使姿势过渡更连续；已完成预览、QA、回装与验证。

## 当前状态

`R0` 至 `R8` 均已完成。R8 采用用户确认的眨眼 idle 与四格连续 waving，正式候选为 `runs/production-v2-attempt-01/candidates/motion-smoothing-r8/spritesheet-r8-clean.webp`；v2 验证和透明边缘处理通过，随后已回装三件套至 `C:/Users/70455/.codex/pets/linabell--elio-zwd/`。未创建 PR、未修改 main。
