# 博士論文 章別ソース地図

作成日: 2026-07-06

このファイルは、`doctorthesis` の各章が、ワークスペース内のどの研究フォルダ・論文個別ファイル・実験フォルダを主な素材としているかを整理する地図である。既存の `CHAPTER_MAPPING.md` は章番号とTeXファイルの対応表、`notes/FILE_MAPPING.md` は初期7章構成時代の古い対応表なので、現在の10章構成に合わせて更新した。

## 見方

- 「主ソース」は、その章の骨格または実証データの出所。
- 「補助ソース」は、背景説明、図、先行議論、レビュー対応などで参照すべき素材。
- 「反映状態」は、2026-07-06時点での概略。個別論文側が更新されている場合は、本文に追いついているかを別途確認する。

## 章別マップ

| 章 | 博論ファイル | 章の役割 | 主ソース | 補助ソース | 反映状態・注意 |
|---|---|---|---|---|---|
| 第1章 | `texts/chapter1.tex` | 序論、政策のメタ・ネイチャー、課題設定 | 博論内で新規統合作成 | `THESIS_PLAN.md`, `CHAPTER_MAPPING.md`, 各章本文 | 2026-07-06にメタネイチャー、知識接続、生成AIスロップ化リスク、第8章の更新を反映済み。 |
| 第2章 | `texts/chapter4.tex` | 公共交通政策におけるメタネイチャー未達の診断、日本版MaaS | `My_Papers/日本版MaaS_交通まちづくり_考察.md` | `Research_JCoMaaS/thesis_written/`, `doctorthesis/texts/maas_*.tex`, `doctorthesis/texts/chapter4_full.tex` | 旧MaaS論文由来。現在の章題上は「第2章」だが、ファイル名は旧構成の `chapter4.tex`。 |
| 第3章 | `texts/chapter5.tex` | 地域公共交通政策のパーパス設定、活性化・再生法運用問題 | `Research_Purpose_transport/purpose_transport.tex` | `Research_Regional_Transport_Governance/thesis_written/Revitalization_Admin_Paper/`, 自治体アンケートdocx群 | 章冒頭に Source コメントあり。3自治体インタビュー、北海道・東北運輸局管内42自治体アンケートの反映章。 |
| 第4章 | `texts/chapter6.tex` | 地域公共交通計画の評価指標の同型化、987自治体・12,568指標 | `publictransportplan/ptp_final/` | `publictransportplan/ptp_final/manuscript_sources/公共交通計画分析_JES_short.tex`, `publictransportplan/ptp_final/analysis_data/`, `Research_LLMBunruiki/classifier_final/` | 本文は概ね反映済み。ただしコンパイル時に `bureau_*png` の図欠落が残っている。 |
| 第5章 | `texts/chapter2.tex` | 生成AI時代の政策規範、創造システム・社会システム理論、AIの限界 | `Research_AI_Policy/thesis_written/Human_Policy_Paper/executive_creativity_v2.tex` | `Research_AI_Policy/thesis_written/Human_Policy_Paper/Policyinfomatics/`, `Research_AI_Policy/thesis_written/LLM_Planning_Paper/`, `Research_CARATS/analysis_nextgen/` | `THESIS_PLAN.md`上では反映済み。アクティブ草稿は `executive_creativity_v2.tex` 系、提出済みWord群は別系統として扱う。 |
| 第6章 | `texts/chapter3.tex` | 認知バイアスと協調的ガバナンスの計算論的分析 | `RobotArmProject/issj_paper/issj_paper.tex` | `RobotArmProject/docs/final_papers/academic_paper_final.md`, `RobotArmProject/results/`, `RobotArmProject/src/` | 章冒頭に Source コメントあり。22,000回シミュレーション、確証バイアス・現状維持・狭い視野の結果を反映。 |
| 第7章 | `texts/chapter7.tex` | 秘密保護と民主的正当性を両立する政策評価システム設計 | `Research_ZK_Snarks/jjsce_v1.2/paper-policy-evaluation.tex` | `Research_ZK_Snarks/thesis_written/`, `Research_AI_Policy/thesis_written/jappm2025.md`, `Research_ZK_Snarks/experiments/cai_privacy_poc/`, `Research_ZK_Snarks/review_claude.md` | 章冒頭に Source コメントあり。2026-07-06に、第8章の80分フィールド実験は最小実装である旨を追記。 |
| 第8章 | `texts/chapter8.tex` | Verdictによる実証、公共的価値接続、フィールド実験 | `Research_ZK_Snarks/apply/20260509/ieee_template/r10_htc2026_paper.tex`, `Research_ZK_Snarks/apply/20260608_verdict_field/` | `Research_ZK_Snarks/apply/20260527/05_draft_paper.md`, `Research_ZK_Snarks/apply/20260509/41_model_family_judge_training_handoff_note.md`, `Research_ZK_Snarks/apply/20260527/data/` | 2026-07-06に大幅更新。盛岡100ケースC0--C3、LoRAの限定的結果、80分ワークショップ、秘密保護の限定検証を反映。 |
| 第9章 | `texts/chapter9.tex` | 制度設計への示唆 | 博論内で統合作成 | 第3章・第4章・第6章・第7章・第8章、`Presentations_Archive/現代の政策形成...md`（要所在確認） | まだ `【編集中】` が残る。第8章更新後のVerdict実証、AIの杖、知識接続の議論を再統合する必要がある。 |
| 第10章 | `texts/chapter10.tex` | 結論、公共交通政策への展開、今後の課題 | 博論内で統合作成 | 全章、特に第7・8章 | 2026-07-06に第8章を「実施予定」から「ラボ実証・フィールド実験設計・限定検証」に修正済み。 |

## 章番号とファイル名のずれ

現在の印刷順とファイル名は一致していない。これは過去の章構成変更の名残である。

| 印刷順 | 実ファイル |
|---|---|
| 第1章 | `texts/chapter1.tex` |
| 第2章 | `texts/chapter4.tex` |
| 第3章 | `texts/chapter5.tex` |
| 第4章 | `texts/chapter6.tex` |
| 第5章 | `texts/chapter2.tex` |
| 第6章 | `texts/chapter3.tex` |
| 第7章 | `texts/chapter7.tex` |
| 第8章 | `texts/chapter8.tex` |
| 第9章 | `texts/chapter9.tex` |
| 第10章 | `texts/chapter10.tex` |

## 更新監視が必要な個別論文・実験フォルダ

以下は、博論本文より個別ファイル側が先に更新されやすいフォルダである。博論更新時は優先的に差分確認する。

| フォルダ・ファイル | 関係章 | 確認ポイント |
|---|---|---|
| `Research_ZK_Snarks/apply/20260509/ieee_template/r10_htc2026_paper.tex` | 第8章 | 最新のVerdictラボ実証。C0--C3、BalNF、LoRA 77件、モデルスケール比較。 |
| `Research_ZK_Snarks/apply/20260527/05_draft_paper.md` | 第8章 | r10より古いが、実験説明やプライバシー運用論が詳しい。数値はr10を優先。 |
| `Research_ZK_Snarks/apply/20260608_verdict_field/` | 第8章 | 80分ワークショップ、協力要請、生成AI活用ガイド、Chapter 7 alignment。 |
| `Research_ZK_Snarks/experiments/cai_privacy_poc/` | 第7・8章 | 秘密漏洩率、CAI LoRA SFT、ロールプレイ攻撃への脆弱性。 |
| `Research_AI_Policy/thesis_written/Human_Policy_Paper/` | 第5章 | 生成AI・政策規範・執政の創造性。TeX系とPolicyinfomatics提出Word系を混同しない。 |
| `publictransportplan/ptp_final/` | 第4章 | 987自治体・12,568指標、分類・図表・査読対応。 |
| `Research_Purpose_transport/purpose_transport.tex` | 第3章 | パーパス設定、B/C偏重、自治体インタビュー・アンケート。 |
| `RobotArmProject/issj_paper/issj_paper.tex` | 第6章 | 22,000回シミュレーション、認知バイアス結果。 |
| `My_Papers/日本版MaaS_交通まちづくり_考察.md` | 第2章 | 日本版MaaS、交通まちづくり、目標・ガバナンス分析。 |

## 既存マッピング文書との関係

- `CHAPTER_MAPPING.md`: 現在の章番号、TeXファイル、図ディレクトリの対応。章ファイルを探すときに使う。
- `THESIS_PLAN.md`: 博論全体の構想、章ごとの役割、既存研究との対応。やや古い箇所が残る。
- `notes/FILE_MAPPING.md`: 初期構成時代の対応表。現在の10章構成とはずれているため、履歴資料として扱う。
- 本ファイル `CHAPTER_SOURCE_MAP.md`: 現在の章ごとの元フォルダ地図。個別論文側の更新漏れ確認に使う。

## 未確定・要確認

- 第9章の元資料として言及される `Presentations_Archive/現代の政策形成...md` は、現在の `/Volumes/UNTITLED/Obsidian/Academic_Research` 直下検索では未確認。別ディレクトリまたは名称変更の可能性がある。
- 第2章のMaaS系素材は、`My_Papers/` と `Research_JCoMaaS/thesis_written/` と `doctorthesis/texts/maas_*` に重複がある。最終的にどれを親版とみなすかは確認が必要。
- 第5章の生成AI・政策規範系は、TeX草稿とWord投稿版が並存している。博論側はTeX草稿を主、投稿版Wordを査読・表現修正の参照として扱うのが安全。
