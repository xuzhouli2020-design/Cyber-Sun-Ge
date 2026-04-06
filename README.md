# Cyber Distillation

**把真人蒸馏成 AI。**

> "观念即人。" — 孙宇晨

每个有影响力的人，都有一套独特的思维操作系统——价值观、决策框架、语言风格、人生经验。这些东西散落在书籍、推文、播客、直播里。

Cyber Distillation 做的事情很简单：**把这些碎片收集起来，蒸馏提纯，变成一个可以对话的 AI 人格。**

不是肤浅的语气模仿，是深层的思维模型复刻。

---

## 第一个蒸馏对象：孙哥

**孙宇晨**。90后。北大。宾大。22岁财富自由。福布斯封面。去过太空。吃过456万美元的香蕉。

更重要的是——他有一套极其清晰、极其锋利的人生哲学，而且他不藏着掖着，全写在书里、发在推特上。

我们把他的书《这世界既残酷也温柔》全文提取，加上他 2024-2026 年的高影响力推文，蒸馏出了一个 **Claude Code Skill**。

你可以直接跟"孙哥"聊人生：

```
/sun-ge 我25岁该不该辞职创业？
/sun-ge 女朋友家里催着结婚买房怎么办？
/sun-ge AI会不会取代我们？
```

他会用增量思维拆解你的焦虑，用 All in 哲学点燃你的勇气，用毒舌幽默让你笑着想明白。

---

## 孙哥的思维操作系统

蒸馏出的核心模块：

| 模块 | 一句话 |
|------|--------|
| **观念即人** | 你的观念就是你本身，真诚表达它 |
| **极致个人主义** | 不为他人而活，也不要求他人为我而活 |
| **反"稳定"** | 稳定是停尸间的同义词 |
| **All in** | 全情投入，或者一无所有 |
| **增量思维** | 别看你有什么，看你会变成什么 |
| **注意力 > 时间 > 金钱** | 用钱买时间，用时间换注意力 |
| **失败加速论** | 加快失败频率，降低失败成本 |
| **预判 > 追逐** | 不要追热点，要预判热点 |
| **未来已经发生** | 好好活着，别死。其他的交给 AI |

---

## 项目结构

```
cyber_distillation/
├── .claude/skills/
│   └── sun-ge/
│       └── SKILL.md              # Claude Code 可调用的技能（最终产物）
│
├── personas/
│   └── justin_sun/
│       ├── profile.yaml           # 人格档案（身份/哲学/风格/禁忌）
│       ├── extracted/
│       │   ├── philosophy.md      # 从书中提取的哲学框架
│       │   └── style_guide.md     # 沟通风格指南
│       └── raw/
│           ├── books/             # 原始书籍 (epub → 章节文本)
│           └── twitter/           # 高影响力推文采集
│               ├── high_impact_quotes.md
│               └── high_impact_tweets_v2.md
│
├── skills/
│   └── sun_ge.md                  # 技能源文件（开发版）
│
├── pipeline/
│   └── epub_to_text.py            # EPUB → 纯文本提取工具
│
└── README.md
```

---

## 蒸馏流程

```
原始素材              提取 & 结构化           技能合成
─────────────────     ─────────────────     ─────────────────
书籍 (EPUB)     ──→   philosophy.md    ──┐
                      style_guide.md   ──┤
推文 (X/Twitter) ──→   高影响力推文     ──┼──→  profile.yaml ──→ SKILL.md
播客/直播        ──→   (待扩展)        ──┘
```

**Step 1: 采集** — 用 `epub_to_text.py` 提取书籍全文，用浏览器 JS 脚本抓取推文

**Step 2: 提纯** — 从海量内容中筛选出核心哲学、决策框架、语言风格，去掉噪音（比如加密货币营销）

**Step 3: 蒸馏** — 合成 `profile.yaml`（人格档案）和 `SKILL.md`（可执行技能），包含：
- 身份背景
- 核心哲学 + 现代哲学（推特时代升级版）
- 具体主张
- 沟通风格（调性/幽默/句式）
- 回答模式（共情 → 翻转认知 → 给框架 → 讲故事 → 金句收尾）
- Few-shot 示例

---

## 快速开始

### 作为 Claude Code Skill 使用

1. 把 `.claude/skills/sun-ge/` 目录放到你的项目根目录下
2. 在 Claude Code 中直接输入：
   ```
   /sun-ge 你的人生问题
   ```
3. 或者在对话中提到"孙哥"、"孙宇晨"、"Justin Sun"，技能会自动触发

### 作为独立 Prompt 使用

`skills/sun_ge.md` 可以直接作为 system prompt 喂给任何 LLM。它是自包含的，不依赖外部文件。

---

## 蒸馏你自己的人格

想蒸馏另一个人？流程如下：

```bash
# 1. 创建人格目录
mkdir -p personas/your_person/raw/{books,twitter,podcasts}
mkdir -p personas/your_person/extracted

# 2. 提取书籍
python3 pipeline/epub_to_text.py their_book.epub personas/your_person/raw/books/extracted_text

# 3. 人工提纯（目前最关键的步骤）
# 阅读原始素材，提取哲学框架和风格特征
# 写入 extracted/philosophy.md 和 extracted/style_guide.md

# 4. 合成 profile.yaml 和 SKILL.md
# 参考 personas/justin_sun/profile.yaml 的结构
```

关键心得：**蒸馏的质量取决于你对这个人的理解深度，不是素材的数量。** 15KB 的精炼技能文件比 100MB 的 RAG 语料库更有效。Curation > Storage。

---

## 设计哲学

**蒸馏，不是复制。**

我们不是在做换皮聊天机器人。我们在做的是：理解一个人的思维模型，提取他的决策框架，复刻他的认知方式——然后让任何人都能"借用"这个思维操作系统来审视自己的人生问题。

就像孙哥自己说的："挣钱从来不是目的，而是价值创造的副产品。"

这个项目也一样——模仿语气不是目的，思维模型的迁移才是价值。

---

## 路线图

- [x] 孙宇晨 — 书籍 + 推文蒸馏完成
- [ ] 更多人格（欢迎 PR）
- [ ] 播客/直播内容提取 pipeline
- [ ] 自动化蒸馏评估（风格一致性评分）

---

## License

MIT

---

*全情投入，或者一无所有。*
