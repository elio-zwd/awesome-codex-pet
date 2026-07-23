# Next Chat Prompt — LinaBell Direction B

Copy the complete prompt below into a new ChatGPT conversation. Then upload the successful generated full-body base concept from the previous conversation. Re-uploading the three original reference images is recommended but optional.

---

## Prompt

你现在接手我的 LinaBell Codex 桌宠项目，请直接继续执行方向 B，不要重新从零规划，也不要偏离已经锁定的角色定义。

### 仓库和权限

使用我已连接的 GitHub：

```text
https://github.com/elio-zwd/awesome-codex-pet
```

现有规划分支：

```text
feat/linabell-pet-direction-a
```

先通过 GitHub 读取该分支中的全部交接资料：

```text
workfiles/linabell--elio-zwd/README.md
workfiles/linabell--elio-zwd/character-brief.md
workfiles/linabell--elio-zwd/reference-notes.md
workfiles/linabell--elio-zwd/action-list.md
workfiles/linabell--elio-zwd/production-plan.md
workfiles/linabell--elio-zwd/direction-b-execution-plan.md
workfiles/linabell--elio-zwd/handoff-state.json
workfiles/linabell--elio-zwd/pet.draft.json
workfiles/linabell--elio-zwd/submission.draft.json
```

同时读取仓库当前版本的：

```text
AGENTS.md
CONTRIBUTING.md
docs/zh-CN/CONTRIBUTING.md
.agents/skills/submit-codex-pet/SKILL.md
.agents/skills/hatch-pet-v2/SKILL.md
```

以 `direction-b-execution-plan.md` 为方向 B 的权威执行方案。不要只给建议，要实际生成素材、进行 QA、操作 GitHub，并在需要我视觉确认的节点停下来。

### 当前真实状态

已经完成：

- 方向 A 的角色设定、参考图分析、动作规划、技术规格和元数据草案；
- GitHub 规划分支；
- 初步重复检查；
- 一张可用的粉色春日装正面全身母版图已经在上一段对话中生成。

还没有完成：

- 母版最终确认；
- 九组八帧标准动画；
- 四个基础方向锚点；
- 十六个环视方向；
- `1536x2288` 的最终 v2 `spritesheet.webp`；
- 视觉 QA、仓库验证、安装测试和最终 PR。

新对话无法自动看到上一段对话中的图片。我会在发送本提示词后上传那张成功生成的全身母版图；我也可能重新上传三张原始参考图。收到母版图前不要开始生成动画。原始照片只用于身份核对，不得提交到公开仓库，也不得直接抠图、裁切、描摹或复用其像素。

### 已锁定的角色定义

主角色必须始终保持：

- 粉色毛绒狐狸形象；
- 超大直立三角耳朵；
- 奶油白眼周和口鼻区域；
- 大而明亮的蓝色眼睛与睫毛；
- 小粉色鼻子；
- 大型蓬松粉色尾巴，尾尖偏浅色；
- 短小、紧凑、适合桌宠格子的 Q 版毛绒身体；
- 友好、活泼、好奇、带一点计划和检查工作的性格。

主版本服装固定为：

- 浅粉色软檐帽；
- 帽子上的白花与粉色蝴蝶结；
- 粉黄格纹短袖上衣；
- 绿色领口蝴蝶结；
- 胸前双樱桃装饰；
- 粉色蓬裙、浅色点纹和蕾丝边；
- 可读尺寸允许时保留裙子上的小水果图案。

蓝色水手服是以后单独制作的变体，禁止混入本次图集。

### 技术目标

必须制作 Codex Pet v2：

```text
图集：1536 × 2288
网格：8 列 × 11 行
单格：192 × 208
总格数：88
pet.json.spriteVersionNumber：2
```

固定行顺序：

```text
0 idle
1 running-right
2 running-left
3 waving
4 jumping
5 failed
6 waiting
7 running
8 review
9 000°–157.5° 环视方向
10 180°–337.5° 环视方向
```

不得擅自添加运行时新行。丰富动作要融入以上九组标准动画。

### 立即执行顺序

#### 第一步：母版确认

收到我上传的成功母版图后：

1. 对照 GitHub 中的角色定义检查耳朵、脸、蓝眼睛、帽子、樱桃、绿蝴蝶结、裙子、尾巴和全身比例；
2. 检查缩小到 `192x208` 后是否仍能清楚识别；
3. 检查耳朵、脚、尾巴是否有足够边距；
4. 把它作为唯一 canonical base，不要又生成三四个新候选；
5. 向我展示判断并只要求一次“通过”或一组集中修改意见。

我通过后，不得无理由更换母版。

#### 第二步：先做三组身份验证动画

按顺序制作：

```text
idle
waving
review
```

每组必须是同一角色、同一服装、连续的八帧动作条。所有动作都要基于已批准母版生成，不能仅凭文字重新设计角色。

每完成一行：

- 拆分为 8 个 `192x208` 单格；
- 检查边界、脚底基线、耳朵、帽子、脸、衣服、尾巴；
- 播放并检查循环；
- 如果整行身份漂移，整行重做；
- 只有单格局部缺陷时，才修最小范围；
- 不允许可读文字、Logo、漂浮图标、动作线、地面阴影或场景。

三行完成后，制作临时接触表和动画预览给我确认。在我确认前不要继续余下六行。

动作语义按照 `direction-b-execution-plan.md` 执行，尤其注意：

- `idle` 只做呼吸、眨眼、耳朵和尾巴的轻微变化；
- `waving` 只用爪子姿态表现挥手，不画挥手线或星星；
- `review` 可使用无可读文字的小粉色板夹，板夹必须始终与爪子或身体相连。

#### 第三步：完成其余六组标准动画

我通过前三行后，继续：

```text
running-right
running-left
running
jumping
failed
waiting
```

逐行生成、逐行检查，不要一次生成完整 8×11 图集。

左右跑步特别注意帽花属于不对称元素，不得简单镜像后把装饰移到错误的一侧。若镜像会破坏角色定义，应单独生成连贯的左跑动作，或对整行做一致性修复。

#### 第四步：制作环视方向

九组标准动作全部通过后：

1. 先做四个基础方向锚点，顺序固定为 `000°` 向上、`090°` 向右、`180°` 向下、`270°` 向左；
2. 给我确认四个锚点；
3. 再生成第 9 行和第 10 行的 16 个顺时针方向；
4. 检查耳朵、帽子、脸部可见性、裙子、身体和尾巴是否随角度连续旋转；
5. 检查 `337.5° → 000°` 是否平滑闭合。

#### 第五步：组装与 QA

使用确定性的处理方式把已批准的动作行组装成：

```text
spritesheet.webp
1536 × 2288
```

完成：

- 透明背景处理；
- 隐藏 RGB 清理；
- 棋盘格、深色和浅色背景边缘检查；
- 88 格接触表；
- 每组标准动作预览；
- 环视方向预览。

禁止出现：

- 白边、粉边或色键残留；
- 身体内部意外透明洞；
- 耳朵、帽子或尾巴裁切；
- 尾巴脱离或瞬移；
- 多余断裂组件；
- 尺寸和基线漂移。

把最终接触表，以及至少 `idle`、`waving`、`running-right`、`review` 和环视预览给我审核。得到我的明确批准后才能发布。

#### 第六步：正式 GitHub 包和 PR

不要把规划分支中的 `workfiles` 直接合并进正式 PR。

从最新 `main` 创建干净分支：

```text
feat/add-linabell-pet-v2
```

最终只提交：

```text
pets/linabell--elio-zwd/submission.json
pets/linabell--elio-zwd/pet.json
pets/linabell--elio-zwd/spritesheet.webp
```

然后实际运行：

```bash
npm run validate:pr
npm run lint
npm run install:pet -- linabell--elio-zwd --codex-home /tmp/codex-pet-test
```

再次搜索 `LinaBell`、`Linabell`、`玲娜贝儿` 和 canonical key 是否重复。只有我已批准最终视觉、所有检查真实通过后，才能创建 Ready for review 的 PR。不要自动合并，除非我之后明确要求。

### 工作方式

- 默认中文沟通；
- 优先实际执行，不要只输出空泛建议；
- 使用 GitHub 读取和更新仓库；
- 使用图片生成/编辑能力制作动作图；
- 在母版、前三行动画、四方向锚点、最终接触表四个关键节点等待我的视觉确认；
- 其余步骤自主推进并如实报告；
- 任何测试没有实际执行，就不能写“已通过”；
- 遇到确定性问题先修复，不要马上退化为只写 Issue；
- 不要偏离角色定义，不要混入蓝色水手服，不要公开上传我的原始参考照片。

现在先读取 GitHub 中的全部交接资料，然后告诉我你已经理解的当前状态，并等待我上传成功母版图。不要在收到母版图前生成动画。

---
