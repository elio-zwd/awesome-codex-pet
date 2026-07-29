# LinaBell Direction B：四图 Refresh 计划

## 目标与边界

本轮在 `feat/linabell-pet-direction-b-refresh-4img` planning / production 分支执行。目标是基于四张质量更好的新图片，重新评估 LinaBell 的视觉基线，而不是直接创建最终 clean PR。

本分支允许保留候选动作图、拆帧图、QA 联系表、预览 GIF / WEBP 与计划、任务、交接文档；绝不提交用户私人原始参考照片，也不直接裁切、描摹或复用这些照片。蓝色水手服不进入本次主图集。最终 clean PR 仍仅包含 `pets/linabell--elio-zwd/` 下的三件套。

## Refresh 流程

1. 对四张新图进行 intake，记录每张图的可用性、来源边界与候选类别。
2. 进行视觉 QA：检查脸型、帽檐及花朵、绿色蝴蝶结及樱桃、裙子结构和小图案、尾巴的大小/位置/连接关系、毛绒材质与渲染风格，以及缩小到桌宠尺寸后的可读性。
3. 做出明确的 baseline 决策：adopt 或 reject。
4. 若 adopt，将四图标记为新的 production baseline；重新核对或重建 identity rows（idle / waving / review）。
5. 在用户批准 identity rows 后，继续 remaining standard rows：running-right / running-left / running / jumping / failed / waiting。
6. 制作四方向锚点、十六方向环视、最终 `1536 × 2288`（8 列 × 11 行，单格 `192 × 208`）v2 图集。
7. 完成验证并准备最终 clean PR；本分支不创建最终 PR。

## 当前决策门

用户已明确取消第 4 张输入。前三张（idle / waving / review）的 intake 与视觉 QA 现构成本轮完整评估范围，详见 `direction-b-refresh-3img-intake-and-qa.md`。结论为 **adopt**：采用这三图定义的粉色毛绒 LinaBell 身份家族作为新的 production baseline。review 候选另含基础身份中不存在的剪贴板，故该行在最终 production row 中仍须以无新增道具的专注姿态重做。

R4 已形成透明 identity-row 候选 01：idle、waving 与无道具 review 的运行时行和 QA 预览已就绪，记录见 `direction-b-refresh-identity-rows-attempt-01-qa.md`。当前门禁为用户统一视觉批准；在批准前不继续其他标准动作行。

## 技术目标

最终图集使用 `spriteVersionNumber: 2`，固定行顺序为：

| 行 | 内容 |
| --- | --- |
| 0 | idle |
| 1 | running-right |
| 2 | running-left |
| 3 | waving |
| 4 | jumping |
| 5 | failed |
| 6 | waiting |
| 7 | running |
| 8 | review |
| 9 | 000°–157.5° 环视方向 |
| 10 | 180°–337.5° 环视方向 |
