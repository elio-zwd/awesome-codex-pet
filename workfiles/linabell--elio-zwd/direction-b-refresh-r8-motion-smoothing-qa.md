# LinaBell R8：动作过渡平滑化 QA

## 目标与运行时边界

Codex Pet v2 的动画时序由应用固定，不能通过 `pet.json` 提高 FPS。idle 实际播放 6 格（280、110、110、140、140、320 ms）；waving 实际播放 4 格（140、140、140、280 ms）。本轮不向未播放格填充伪帧，而是重做全部已播放格的连续姿态。

## 采用候选

- idle：`candidates/motion-smoothing-r8/idle-source-r2-approved.png`
  - 用户已明确确认眨眼版本可用。
  - 顺序为睁眼、半闭、闭眼、闭眼峰值、半开、睁眼回环；身份、帽饰侧别、衣装、尾巴位置和底线稳定。
- waving：`candidates/motion-smoothing-r8/waving-source.png`
  - 顺序为起势、半抬、最高点、回程；同一只手连续摆动，无换手、额外肢体、手指或独立特效。

## 自动检查

- 拆帧：idle 6/6、waving 4/4，均为 `192 × 208`；无裁切或空帧。
- 结构提示：两行使用稳定等宽拆帧，已在缩小联系表中目检通过。
- 正式候选：`candidates/motion-smoothing-r8/spritesheet-r8-clean.webp`。
- v2 验证、透明边缘去紫均通过；图集仍为 `1536 × 2288`、8 列 × 11 行。
- 预览：`candidates/motion-smoothing-r8/previews/idle.gif`、`candidates/motion-smoothing-r8/previews/waving.gif`。

## 结论

adopt。R8 只替换 idle 与 waving；其余标准动作及十六方向保持此前已批准内容。该变更改善有限固定帧数下的动作连续性，但不会改变 Codex 应用的全局播放帧率。
