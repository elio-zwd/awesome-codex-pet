# LinaBell Direction B：四图 Refresh 交接

## 项目背景

项目此前已完成一轮视觉 baseline 审批，已批准 idle、waving 与 review；其中 review 曾修复“第三只手”问题，最终采用过替换后的 image1 版本。

现进入 `refresh-4img` 新阶段：用户表示已取得四张更好的新图片，需要先重新评估视觉基线，再决定是否继续后续动作生产。

## 当前状态

`refresh-3img-baseline-adopted-v2-packaged-and-locally-installed-no-pr`

已完成：在 refresh planning / production 分支创建本轮 plan、tasks、handoff 文档；接收并完成 idle / waving / review 三个候选图的 intake 与视觉 QA，结果记录于 `direction-b-refresh-3img-intake-and-qa.md`。用户已取消第 4 张输入，且已采用这三图定义的身份家族为新的 production baseline。

已完成：用户以“继续下一步”确认 identity rows。idle（6 帧）、waving（4 帧）及无道具 review（6 帧）已透明化、注册并组装为 `1536 × 208` 单行；三行均通过结构检查，未用格均为完全透明。详细记录见 `direction-b-refresh-identity-rows-attempt-01-qa.md`。

R5 已完成：running-right、完整独立生成的 running-left、jumping、failed、waiting、non-directional running 均通过增量及汇总结构检查。初始逐帧镜像的 running-left 因深色 QA 联系表中的尾尖分离碎片被拒绝，后续独立生成行替代该候选。running 的初始两次生成均被安全系统拒绝；用户授权无名称、原地专注处理策略后，成功生成并通过 6 帧候选。详情见 `direction-b-refresh-r5-standard-rows-attempt-01-qa.md`。

R6、R7 已完成：已建立 000°、090°、180°、270° 四方向锚点及 16 格环视。左侧中间的四格（225°–292.5°）经一次完整重做，使下左、左、上左语义在三人盲测中全部通过。最终候选图集已完成透明边缘去紫、WEBP 编码与 v2 结构验证；最终视觉 QA 无回归标记。记录见 `direction-b-refresh-r6-directions-and-r7-final-qa.md`。

已完成打包与本地安装：正式三件套位于 `pets/linabell--elio-zwd/`，且已通过仓库验证并安装至 `C:/Users/70455/.codex/pets/linabell--elio-zwd/`。为遵守正式包的完整方向行溯源，打包图集使用原始完整生成的第 10 行，而非过程性局部修复候选。247.5° / 292.5° 的中间盲测提示经独立最终视觉 QA 判为 minor，已记录于 `runs/production-v2-attempt-01/qa/blind-review-resolution.json`。

## 下一步

下一步：重启或刷新 Codex 后，在宠物选择器中选择 `LinaBell`。若用户要求公开收录，再从本分支整理只含三件套的 clean PR；本分支仍不创建最终 PR。

## 重要边界

- 私人原始参考图只用于本地视觉判断，不提交、不裁切、不描摹、不复用像素。
- 蓝色水手服不混入主图集。
- 最终 clean PR 只允许 `submission.json`、`pet.json`、`spritesheet.webp` 三个运行时文件；本 refresh 分支不创建最终 PR。
