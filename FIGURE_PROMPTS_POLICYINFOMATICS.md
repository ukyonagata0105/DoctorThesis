# 図作成プロンプト集：Policyinfomatics論文用

対象論文：「AI時代の『執政の創造性』―ルーマン理論による基礎づけ」
出力先：`figure/ch2/` （博士論文と共用）またはPolicyinfomatics投稿時はdocxに埋め込み
フォント：日本語対応（japanize_matplotlib等）
スタイル：学術論文向け・白背景・モノクロ対応（グレースケールでも読める）
サイズ：すべて300dpi

---

## 図P-1：論文の理論的構造図（全体俯瞰）

**出力先：** `figure/ch2/fig_p1_overview.png`
**サイズ：** 900×500px

```
Create a flowchart showing the overall logical structure of the paper.

Layout: left to right, three columns

LEFT COLUMN — Empirical foundation:
  Box: 政策過程モデル (Policy Process Models)
    ・キングドン：政策の窓
    ・サバティエ：唱導連携
    ・村松：三者関係
  ↓
  Box: ウィキッド・プロブレム
    (Wicked Problems)
    ・価値の競合が構造的
    ・正解がない
    ・非可逆的

CENTER COLUMN — Conceptual development:
  Box: 執政の創造性
    (Executive Creativity)
    定義：価値判断を基盤に
    新たなガバナンスの範囲を
    生成・配分し正当性を担保する実践
  ↕ 必要条件
  Box: 意味の創造性
    (Semantic Creativity)
    ルーマン Sinn 概念
    心的システムによる価値的意味選択

RIGHT COLUMN — Applications:
  Box: AIの原理的限界
    ・心的システムを持たない
    ・情報・伝達段階のみ担当可
    ・意味の創造性に参加不可
  ↓
  Box: 政策制度設計への示唆
    ・HITL の再解釈
    ・理解段階を上流に配置
    ・Fischer 層②以上を人間が担当

Arrows connecting:
  Left column → Center (empirical grounding)
  Center → Right (theoretical application)

Title above: 「AI時代の執政の創造性」論文の理論的構造
Caption below: 出典：筆者作成
```

---

## 図P-2：ハーバーマスとルーマンの比較——なぜルーマンか

**出力先：** `figure/ch2/fig_p2_habermas_luhmann.png`
**サイズ：** 900×500px

```
Create a comparison diagram (two-column layout) contrasting
Habermas and Luhmann's communication frameworks.

LEFT COLUMN — Habermas (light red/pink background):
  Title: ハーバーマス的枠組み
         (Habermasian Framework)

  Communication model:
    コミュニケーション → 了解 (Understanding/Agreement)
  
  Ideal: 理想的言語状況
         Ideal Speech Situation
  
  Problem: 手続き的定義
  "了解を達成する手続きを正しく踏めば
   主体が人間でなくても合理的コミュニケーションが成立"
  
  Result (red warning box):
    Habermas Machine (Google DeepMind, 2024)
    "AIが熟議促進者として評価される"
    ← 手続き的定義の構造的脆弱性

RIGHT COLUMN — Luhmann (light blue background):
  Title: ルーマン的枠組み
         (Luhmannian Framework)
  
  Communication model:
    情報 → 伝達 → 理解
    (Information → Mitteilung → Verstehen)
  
  Key insight: 「わかり合えなさ」は逸脱ではなく本質
  
  Psychic system requirement:
    理解（Verstehen）は
    オートポイエティックな心的システムの
    固有的作動として生起
  
  Result (blue affirmation box):
    AIは心的システムを持たない
    → 手続きを精緻化してもAIは
      「理解」の主体になれない
    → AI代替を構造的に封じる

Center divider arrow: 「なぜルーマンか」
Bottom caption: 出典：Luhmann (1984); Habermas (1981); Schismenos (2026) をもとに筆者作成
```

---

## 図P-3：ルーマンのコミュニケーション3段階とAI/人間の役割分担

**出力先：** `figure/ch2/fig_p3_luhmann_roles.png`
**サイズ：** 900×450px

```
Create a horizontal three-stage diagram showing Luhmann's communication
model with AI/human role division.

Three boxes connected by arrows (left to right):

BOX 1 (light green, labeled "AI担当"):
  情報 (Information)
  "何を語るかの選択"
  ────────────────
  AIの役割:
  ・需要データ分析
  ・B/C計算・試算
  ・選択肢の生成
  ・政策文書の初稿

  Fischer層: ① 技術的検証

BOX 2 (light green, labeled "AI担当"):
  伝達 (Mitteilung)
  "いかに語るかの選択"
  ────────────────
  AIの役割:
  ・説明資料の作成
  ・複数シナリオの提示
  ・コミュニケーション支援

  Fischer層: ① 技術的検証

BOX 3 (light blue, labeled "人間担当" with bold border):
  理解 (Verstehen)
  "いかに受け止めるかの選択"
  ────────────────
  人間の役割:
  ・パーパス・目標の設定
  ・価値対立の調停
  ・説明責任の引き受け
  ・最終的な政策判断

  Fischer層: ②状況的妥当性
             ③体制的正当化
             ④合理的社会選択

  ★意味の創造性・執政の創造性
    が発揮される領域

Bracket below BOX 1+2: "AIに委ねてよい領域"
Bracket below BOX 3: "人間が担うべき領域（HITL の核心）"

Title: ルーマンのコミュニケーション三段階とAI/人間の役割分担
Caption: 出典：Luhmann (1984); Fischer (1980); Keenan & Sokol (2023) をもとに筆者作成
```

---

## 図P-4：意味の創造性と執政の創造性——概念と必要条件関係

**出力先：** `figure/ch2/fig_p4_concepts.png`
**サイズ：** 800×500px

```
Create a diagram showing the two core concepts and their logical relationship.

TWO BOXES with an arrow between them:

LEFT BOX (light yellow, Luhmann level label at top):
  ルーマン理論レベル
  ──────────────────
  意味の創造性
  (Semantic Creativity)

  定義：
  心的システムと社会システムの
  構造的カップリングにおいて、
  心的システムが独自の価値判断に
  基づいて可能性の中から現実性を
  選択するプロセス

  理論的根拠：
  ルーマン「Sinn」概念
  意味の自己運動性（SoSy:101）

  誰でも：
  すべての人間（心的システム）

ARROW (center):
  ↓
  必要条件
  (Necessary Condition)
  ※逆は成立しない

RIGHT BOX (light blue, Fischer level label at top):
  政策実践レベル（Fischer 層②以上）
  ──────────────────
  執政の創造性
  (Executive Creativity)

  定義：
  社会の構成員同士のコミュニケーションを
  前提に、価値判断を基盤として、
  新たなガバナンスの範囲を生成・配分し、
  以て政策の正当性を担保する実践

  条件：
  ・価値的意味構成（意味の創造性）あり
  ・かつ Fischer 層②以上の正当化が成立

Bottom note:
  "意味の創造性が政策コミュニケーションの場で
   規範的正当化（Fischer 層②以上）として結実したとき、執政の創造性となる"

Caption: 出典：Luhmann (1984); Fischer (1980); Hoppe (1993) をもとに筆者作成
```

---

## 図P-5：Fischerの政策正当化四層と執政の創造性

**出力先：** `figure/ch2/fig_p5_fischer.png`
**サイズ：** 750×500px

```
Create a 2×2 matrix showing Fischer's four levels of policy justification,
with annotation showing which levels correspond to 執政の創造性.

Axes:
- Horizontal: 目標達成度 ← | → 規範的評価
- Vertical: ミクロ ↑ | ↓ マクロ

Four quadrants:

Top-left [white/light gray]:
  ① 技術的検証
  (Program Verification)
  "目標達成・効率性への適合"
  例：B/C 計算、利用者数達成率
  → 通常の行政執行

Top-right [light blue]:
  ② 状況的妥当性
  (Situational Validation)
  "この文脈でプログラム目標は適切か"
  例：地域ニーズへの適合確認
  → 執政の創造性の発揮始まる

Bottom-left [light blue]:
  ③ 体制的正当化
  (Systemic Vindication)
  "支配的社会秩序への貢献"
  例：地方自治の本旨との整合
  → 執政の創造性

Bottom-right [light blue]:
  ④ 合理的社会選択
  (Rational Social Choice)
  "代替的価値体系との比較"
  例：移動権 vs 財政効率のトレードオフ
  → 執政の創造性（最高次）

Add:
- Dashed lines separating quadrants
- Bracket on right spanning ②③④: "執政の創造性が発揮される領域"
- Bracket on left for ①: "技術的執行（AI支援可）"
- Label between ① and ②③④: "← 臨界点"

Caption: 出典：Fischer (1980); Hoppe (1993); 佐野他 (2021) をもとに作成
```

---

## 図P-6：意味の創造性の操作化——Boswell et al.四基準

**出力先：** `figure/ch2/fig_p6_boswell.png`
**サイズ：** 800×500px

```
Create a diagram showing the four evaluation criteria for 意味の創造性,
based on Boswell et al. (2015).

Layout: central concept with four radiating boxes

CENTER circle:
  意味の創造性の評価
  「可能性の地平を認識した
   上で選択が行われているか」

FOUR BOXES radiating outward (top, right, bottom, left):

TOP:
  ① 選択肢の認識
  (Horizon Awareness)
  問い：採用した評価基準以外の
  選択肢が俎上に載せられたか
  
  Boswell: narrowing down（選択肢の狭小化）
  交通政策例: B/C以外の便益定義が議論されたか

RIGHT:
  ② グッドハートの法則への対処
  (Anti-Goodhart)
  問い：指標が目的化するリスクへの
  警戒が組み込まれているか
  
  Boswell: crowding out（目標の侵食）
  交通政策例:「B/C>1達成」が目標に
  すりかわっていないか

BOTTOM:
  ③ 合成の誤謬への対処
  (Anti-Composition Fallacy)
  問い：個別最適化が全体目標と
  齟齬をきたす可能性が検討されたか
  
  Boswell: locking in（固定化）
  交通政策例: 路線単体の収支最適化が
  地域移動権全体を損なっていないか

LEFT:
  ④ トレードオフの記録
  (Trade-off Documentation)
  問い：異なる価値基準間の優先順位付けが
  明示的に議論・記録されているか
  
  交通政策例: 収益性 vs 移動権の
  対立が協議議事録に残っているか

Note below: "B/C偏重の採用それ自体は問題でない。熟議を経た選択であれば意味の創造性の発揮。"

Caption: 出典：Boswell et al. (2015); Bächtiger & Parkinson (2019) をもとに筆者作成
```

---

## 図P-7：HITLの再解釈——理解段階を上流に置く

**出力先：** `figure/ch2/fig_p7_hitl.png`
**サイズ：** 900×550px

```
Create a side-by-side comparison of OLD vs NEW HITL interpretation.

Title: Human-in-the-Loop の再解釈

LEFT SIDE — 従来の HITL (gray/red tones):
  Title: 従来の HITL（形式的解釈）
  "最終確認のボタンを押す人間"

  Flow (top to bottom):
  [技術専門家・事業者が計画策定]
      ↓
  [費用便益分析・路線最適化]
      ↓
  [計画案の提示]
      ↓
  [住民への説明・意見聴取] ← 人間はここのみ
      ↓
  [人間が承認ボタンを押す] 👆
      ↓
  [計画確定]

  Problem box (red):
  ・情報段階が理解段階に先行
  ・価値判断の枠組みは所与
  ・執政の創造性が制度的に封じられる

RIGHT SIDE — 本稿の HITL（blue/green tones):
  Title: 本稿の HITL（実質的再解釈）
  "意味の創造性が発揮される場所に人間を置く"

  Flow (top to bottom):
  [市民によるパーパス討議] 👥 ← 人間が最上流
  "まちづくり目標・公共交通の存在意義"
      ↓
  [地域目標の確定]
      ↓
  [AI支援による現状把握・効果試算] 🤖
  （情報・伝達段階）
      ↓
  [施策比較・市民による選択] 👥
  （理解段階：人間が担う）
      ↓
  [計画確定・継続的評価]

  Benefit box (blue):
  ・理解段階が最上流
  ・価値判断の枠組みを市民が設定
  ・執政の創造性が制度的に確保される

Caption: 出典：Parasuraman & Wickens (2008); 筆者作成
```

---

## 実行メモ

- 出力先：`figure/ch2/` （すでに作成済み）
- ファイル命名：`fig_p1_overview.png` ～ `fig_p7_hitl.png`
- フォント：`japanize_matplotlib` または IPAexGothic
- モノクロ印刷でも読めるようグレースケール対応を意識すること
- 図内の日本語ラベルには英語訳を括弧内で併記
- 出典（Caption）は図内下部に小さく記載

## work.mdへの挿入位置（参考）

| 図 | 挿入位置 |
|---|---|
| P-1 全体俯瞰 | 1章末（本稿のアプローチの後） |
| P-2 ハーバーマスvsルーマン | 4章 4.1節「なぜルーマンか」の後 |
| P-3 3段階とAI/人間役割 | 4章 4.2節「コミュニケーションの3段階」の後 |
| P-4 意味の創造性と執政の創造性 | 4章 4.4節「意味の創造性の定義」の後 |
| P-5 Fischer四層 | 3章 3.1節「定義」の後 |
| P-6 Boswell四基準 | 6章 6.1節の評価基準説明の後 |
| P-7 HITLの再解釈 | 6章 6.2節「HITLの再解釈」の後 |
