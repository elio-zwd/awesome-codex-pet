# LinaBell Direction B：身份行候选 01 QA

## 目的

在三图 production baseline 已采用后，将 identity rows 统一为 v2 可组装的透明生产候选：idle（6 帧）、waving（4 帧）、review（6 帧）。本轮仅为 QA 候选，尚未获得用户统一视觉批准，因此不标记为完成生产素材。

## 来源与边界

- idle、waving：使用已采用的三图 baseline 对应候选；原始输入未复制进仓库。
- review：使用新生成的无道具候选 `candidates/review-no-prop-attempt-01.png`；明确排除原 review 图中的剪贴板，未引入其他新增道具。
- 所有行均由候选图的独立图像区域透明化并注册；未提交、裁切或复用用户私人原始参考照片的像素。

## 帧选择与运行时布局

候选图均为 2 × 4 格。下表中的索引按从左到右、从上到下的原始格序编号。

| 行 | 选用原始格 | 生产帧数 | 透明未用格 |
| --- | --- | ---: | --- |
| idle | 0、1、2、3、4、5 | 6 | 第 6–7 格 |
| waving | 0、2、5、7 | 4 | 第 4–7 格 |
| review | 0、1、2、3、4、5 | 6 | 第 6–7 格 |

每个生产帧均为 `192 × 208`，每行均为透明背景 `1536 × 208`。已检查未用格 alpha 为全 0。

## 视觉 QA

- 三行持续使用已采用的粉色毛绒狐身份：脸部、帽檐与花朵、绿色蝴蝶结/樱桃、格纹上衣、点点裙、尾巴和毛绒渲染一致。
- idle 采用自然的睁眼、半睁与闭眼微动；waving 采用中性、抬手、最高点与回到中性的循环序列。
- review 为新生成的无剪贴板专注姿态，保持可读的头部与前爪小幅变化；未见第三只手或新道具。
- 使用 `stable-slots` 提取，以避免自动组件提取造成的比例跳动。结构检查为零错误；该工具按策略给出 3 条预期提示，要求通过预览确认循环稳定与无裁切。

## 产物

- 透明行：`runs/identity-rows-attempt-01/row/{idle,waving,review}.png`
- 深色三行联系表：`runs/identity-rows-attempt-01/qa/identity-rows-contact-sheet-dark.png`
- 单行动画预览：`runs/identity-rows-attempt-01/qa/{idle,waving,review}-preview-dark.gif`
- 结构检查：`runs/identity-rows-attempt-01/qa/review.json`

## 结论与待确认项

推荐将此三行作为新的 identity-row production 候选。请用户查看三行联系表及预览，并明确批准或指出需要修改的行；批准前不得开始其余标准动作行。
