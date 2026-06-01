# 図作成プロンプト集

Codex向け。各プロンプトに出力先パスを明記。日本語（英語）併記で作成すること。
フォント：日本語対応（japanize_matplotlib または matplotlib + IPAexGothic 等）
スタイル：学術論文向け・白背景・クリーンなデザイン

---

## 図1：Fischerの政策正当化四層モデル

**出力先：** `figure/ch2/fig_fischer_matrix.png`
**サイズ：** 800×500px、300dpi

```
Create a 2×2 matrix figure showing Fischer's four-level policy justification framework.

Axes:
- Horizontal axis (left→right): 目標達成度 (Goal Achievement) → 規範的評価 (Normative Evaluation)
- Vertical axis (top→bottom): ミクロ (Micro) → マクロ (Macro)

Four quadrants:
- Top-left [light gray]:
    ① プログラムの技術的検証
    (Program Verification)
    "目標達成・資源効率への適合"
- Top-right [light blue]:
    ② 状況的妥当性の検証
    (Situational Validation)
    "この文脈でプログラム目標は適切か"
- Bottom-left [light blue]:
    ③ 体制的正当化
    (Systemic Vindication)
    "支配的社会秩序への貢献"
- Bottom-right [light blue]:
    ④ 合理的社会選択
    (Rational Social Choice)
    "代替的価値体系との比較"

Add:
- Horizontal dashed line between micro and macro rows
- Vertical dashed line between left and right columns
- Left bracket spanning top row only, labeled: "第一次担論 (First-order Discourse)"
- Left bracket spanning bottom row only, labeled: "第二次担論 (Second-order Discourse)"
- Shaded region annotation over quadrants ②③④:
  "執政の創造性が発揮される領域（層②以上）"
- Bottom caption: "出典：Fischer (1980); Hoppe (1993); 佐野他 (2021) をもとに作成"
```

---

## 図2：意味の創造性と執政の創造性の関係図

**出力先：** `figure/ch2/fig_concept_relation.png`
**サイズ：** 900×500px、300dpi

```
Create a conceptual relationship diagram with two connected boxes.

LEFT BOX (light yellow, rounded rectangle):
  Title: 意味の創造性 (Semantic Creativity)
  Subtitle: ルーマン Sinn 概念に基づく
  Content:
    ・心的システムによる価値的意味選択
    ・可能性の地平から現実性を選択するプロセス
    ・意味の自己運動性（オートポイエーシス）
  Below box, label: "操作化：Boswell et al. 四基準"
    ① 選択肢の認識
    ② グッドハートの法則への対処
    ③ 合成の誤謬への対処
    ④ トレードオフの記録

ARROW (center, left→right):
  Label above arrow: "必要条件 (Necessary Condition)"
  Label below arrow: "※逆は成立しない"

RIGHT BOX (light blue, rounded rectangle):
  Title: 執政の創造性 (Executive Creativity)
  Subtitle: Fischer 政策正当化論に基づく
  Content:
    ・価値判断を基盤とした政策コミュニケーション
    ・規範的正当化（Fischer 層②以上）
    ・新たなガバナンス範囲の生成・配分
  Below box, label: "操作化：Fischer 四層②③④"
    ② 状況的妥当性
    ③ 体制的正当化
    ④ 合理的社会選択

Bottom note:
  "意味の創造性が政策コミュニケーションの場で規範的正当化として結実したとき、執政の創造性となる"

Style: clean academic, two-column layout, Japanese+English labels
出典：筆者作成（Luhmann 1984; Fischer 1980; Hoppe 1993 をもとに）
```

---

## 図3：AIと人間の役割分担図（ルーマン3段階×Fischer層）

**出力先：** `figure/ch2/fig_ai_human_roles.png`
**サイズ：** 900×500px、300dpi

```
Create a diagram showing the division of roles between AI and humans
in the policy process, based on Luhmann's communication tripartite model
and Fischer's legitimation levels.

Layout: horizontal flow with three stages

STAGE 1 (left, light green background):
  Label: 情報 (Information)
  Luhmann: "何を語るかの選択"
  Fischer: 層① 技術的検証
  Role: AI担当 🤖
  Examples: 需要予測、B/C計算、データ分析

STAGE 2 (center, light green background):
  Label: 伝達 (Mitteilung)
  Luhmann: "いかに語るかの選択"
  Fischer: 層① 技術的検証
  Role: AI担当 🤖
  Examples: 計画書初稿生成、説明資料作成

STAGE 3 (right, light blue background):
  Label: 理解 (Verstehen)
  Luhmann: "いかに受け止めるかの選択"
  Fischer: 層②③④ 規範的正当化
  Role: 人間担当 👤
  Examples: パーパス設定、価値対立の調停、説明責任

Arrows connecting the three stages left to right.

Above diagram: title "ルーマンのコミュニケーション三段階とAI/人間の役割分担"
Below diagram:
  Green box label: "AI支援可能領域"
  Blue box label: "意味の創造性・執政の創造性の領域（人間が担うべき）"

Bottom caption: "出典：Luhmann (1984); Fischer (1980); Keenan & Sokol (2023) をもとに筆者作成"
```

---

## 図4：既存の地域公共交通計画フロー

**出力先：** `figure/ch3/fig_flow_existing.png`
**サイズ：** 600×900px、300dpi
※ `Research_Purpose_transport/fig1_flow_existing.png` の置き換え版

```
Create a vertical flowchart showing the EXISTING public transport
planning process in Japan.

Boxes (top to bottom, connected by downward arrows):

[現状把握・課題整理]
(Current Situation Analysis)
    ↓
[目標設定]
(Goal Setting)
※注釈："専門家・交通事業者・地方運輸局が主導"
    ↓
[施策の検討・比較]
(Policy Options Development)
※注釈："費用便益分析 B/C による比較"
    ↓
[計画の策定]
(Plan Formulation)
    ↓
[住民・市民への説明・意見聴取]  ← ★市民参加はここのみ
(Public Consultation)
    ↓
[計画の確定・認定]
(Plan Approval)
※注釈："地方運輸局による審査（B/C>1 が実質要件）"
    ↓
[実施・評価]
(Implementation & Evaluation)

Right side annotation box (red border):
"問題点 (Issues):
・B/C>1 が実質的な認定要件として機能
・市民参加は意見表明のみ（理解段階の欠如）
・まちづくり目標が計画に反映されにくい
・地方自治体の創意が収益基準に制約される"

Style: clean flowchart, rectangles with rounded corners, gray color scheme
出典：屋井 (2021) をもとに作成
```

---

## 図5：既存の計画確定行為の正当性条件

**出力先：** `figure/ch3/fig_rationality_existing.png`
**サイズ：** 600×600px、300dpi
※ `Research_Purpose_transport/fig2_rationality_existing.png` の置き換え版

```
Create a pyramid diagram showing the legitimacy conditions of the
EXISTING planning process.

Pyramid (top=least dominant, bottom=most dominant in practice):

TOP (small, white):
  手続き的合理性 (Procedural Rationality)
  "正当なプロセスを踏んだか"

MIDDLE (medium, light gray):
  計画の合理性 (Planning Rationality)
  "費用便益比（B/C）が基準を満たすか"

BOTTOM (large, dark gray):
  経営的合理性 (Economic Rationality)
  "路線・事業の収益性"
  ★ 現行制度では実質的支配

Add vertical arrow on left pointing DOWN, labeled:
"現行制度での実質的優先順位 →"

Add annotation box below pyramid:
"移動権・まちづくり目標・コミュニティ価値は
正当性評価の対象外 (Fischer 層①のみ)"

Style: pyramid, Japanese+English labels, grayscale
出典：筆者作成（屋井 2021; ヒアリング調査 2022 をもとに）
```

---

## 図6：提案する地域公共交通計画フロー

**出力先：** `figure/ch3/fig_flow_proposed.png`
**サイズ：** 600×900px、300dpi
※ `Research_Purpose_transport/fig3_flow_proposed.png` の置き換え版

```
Create a vertical flowchart showing the PROPOSED public transport
planning process.

Boxes (top to bottom):

[市民によるパーパス討議] ← ★起点（青色・強調）
(Citizen-led Purpose Deliberation)
※注釈："まちづくり目標・公共交通の存在意義を市民が設定
 Human-in-the-Loop: 意味の創造性・執政の創造性の核心"
    ↓
[地域目標の確定]
(Regional Goal Setting)
"住民・自治体・事業者の合意形成"
    ↓
[AIを活用した現状把握・効果試算] ← AI担当（緑色）
(AI-assisted Analysis)
"需要予測・B/C試算・複数シナリオ生成（情報・伝達段階）"
    ↓
[施策の比較・市民による選択]
(Options Comparison & Citizen Choice)
"AIが提示→市民が選択（理解段階は人間が担う）"
    ↓
[計画の策定]
(Plan Formulation)
    ↓
[地方運輸局への報告]
(Report to Regional Transport Bureau)
※注釈："関与は進捗確認のみ（審査権限なし）"
    ↓
[実施・市民による継続評価]
(Implementation & Citizen-led Evaluation)

Right side annotation box (blue border):
"変更のポイント (Key Changes):
・計画の上流を市民参画に（理解段階を最上流へ）
・AIは情報・伝達段階を担当
・地方運輸局の関与を進捗確認に限定
・B/Cは参考指標であり認定要件ではない"

Highlight top box with thick blue border.
Style: clean flowchart, blue accent for new elements, Japanese+English
出典：筆者作成
```

---

## 図7：提案する計画確定行為の正当性条件

**出力先：** `figure/ch3/fig_rationality_proposed.png`
**サイズ：** 700×600px、300dpi
※ `Research_Purpose_transport/fig4_rationality_proposed.png` の置き換え版

```
Create a three-circle diagram showing the PROPOSED legitimacy conditions
for plan approval. The three conditions are EQUAL in weight (no pyramid).

THREE CIRCLES arranged in a triangle formation:

TOP circle (light blue):
  パーパス適合性
  (Purpose Alignment)
  "地域が設定したまちづくり目標に
   公共交通計画が貢献しているか
   （Fischer 層③④：体制的正当化・社会選択）"

BOTTOM-LEFT circle (light green):
  手続き的正当性
  (Procedural Legitimacy)
  "市民参加・討議プロセスを
   適切に経たか
   （Fischer 層②：状況的妥当性）"

BOTTOM-RIGHT circle (light gray):
  技術的合理性
  (Technical Rationality)
  "費用便益・効率性の基準
   （Fischer 層①）
   ※ただしパーパスに従属"

CENTER (overlap area):
  統合的正当性
  (Integrated Legitimacy)

Connect all three circles with double-headed arrows.

Below diagram, two annotation boxes:
Box 1: "三条件は対等であり、技術的合理性のみによる判断は正当化されない"
Box 2: "B/C偏重が熟議の結果であれば、それ自体は執政の創造性の発揮である"

Style: three-circle Venn-like diagram, equal-sized circles, Japanese+English
出典：筆者作成（Fischer 1980; Hoppe 1993 をもとに）
```

---

## 実行メモ

- 出力先ディレクトリは事前に作成すること（`figure/ch2/` は新規作成が必要）
- すべてPNG、300dpi
- フォント：`japanize_matplotlib` または `matplotlib.rcParams['font.family'] = 'IPAexGothic'` 等で日本語対応
- 図番号・キャプションは論文本文側で付与するため、図内には含めない（出典表記のみ）
