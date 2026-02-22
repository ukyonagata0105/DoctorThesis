# 既存ファイルと論文章のマッピング

## 概要
このファイルは、現在のワークスペースにある研究ファイルを、計画した博士論文の各章にどう対応させるかを整理したものです。

---

## ファイル一覧と対応関係

### 第1章 序論
| ファイル | 使用内容 | 優先度 |
|---------|---------|-------|
| `Presentations_Archive/現代の政策形成...md` | 生成AIの可能性と限界、「杖」メタファー | 高 |
| `RobotArmProject/docs/final_papers/academic_paper_final.md` | 研究背景・問題設定（Introduction部分） | 高 |

### 第2章 先行研究のレビュー：Human-AI Policyの議論
| ファイル | 使用内容 | 優先度 |
|---------|---------|-------|
| `Research_AI_Policy/thesis_written/Human_Policy_Paper/executive_creativity_v2.tex` | 「執政の創造性」とルーマン理論の基礎づけ | 高 |
| `RobotArmProject/docs/final_papers/academic_paper_final.md` | 協調制御、ガバナンス論などの文献レビュー | 高 |
| `RobotArmProject/docs/reference_materials/cognitive-bias-explanations.md` | 認知バイアスの定義 | 中 |

### 第3章 公共交通政策の現状と課題
| ファイル | 使用内容 | 優先度 |
|---------|---------|-------|
| `Presentations_Archive/官民連携と公共交通_授業ストーリーライン.md` | STOフレームワーク、政策変遷、連携形態 | 高 |
| `RobotArmProject/docs/final_papers/academic_paper_final.md` | Japan MaaS分析、実装ギャップ | 高 |
| `Presentations_Archive/第1章.pdf` | 公共交通政策の背景（要確認） | 中 |
| `Presentations_Archive/「地域公共交通政策」の存立理由...pdf` | 制度変遷の詳細（要確認） | 中 |

### 第4章 認知バイアスの政策協調への影響：計算論的分析
| ファイル | 使用内容 | 優先度 |
|---------|---------|-------|
| `RobotArmProject/docs/final_papers/academic_paper_final.md` | **ほぼそのまま使用可能**（計算モデル、シミュレーション、結果） | 最高 |
| `RobotArmProject/docs/reference_materials/cognitive-bias-explanations.md` | バイアスの説明（補足） | 低 |
| `RobotArmProject/docs/literature_review/cognitive_bias_modeling/` | 文献レビュー詳細 | 中 |

### 第5章 生成AIと人間の関係性：ZK-SNARKs型政策評価システムの提案
| ファイル | 使用内容 | 優先度 |
|---------|---------|-------|
| `Research_AI_Policy/thesis_written/jappm2025.md` | ZK-SNARKs + LLM as a Judge | 高 |
| `Research_ZK_Snarks/thesis_written/*.md` | ZK-SNARKs型政策評価システム | 高 |

### 第6章 制度設計への示唆
| ファイル | 使用内容 | 優先度 |
|---------|---------|-------|
| `RobotArmProject/docs/final_papers/academic_paper_final.md` | 制度設計の提言部分 | 高 |
| `Presentations_Archive/官民連携と公共交通_授業ストーリーライン.md` | STOフレームワークの応用 | 中 |
| `Presentations_Archive/現代の政策形成...md` | AIの「杖」としての役割、市民参加、合意形成支援 | 中 |

### 第7章 結論：都市計画への展開
| ファイル | 使用内容 | 優先度 |
|---------|---------|-------|
| `RobotArmProject/docs/final_papers/academic_paper_final.md` | 結論・今後の課題 | 高 |

---

## 既存論文の活用度（推定）

| 章 | 既存ファイルからの流用可能性 | 新規執筆が必要な部分 |
|----|--------------------------|-------------------|
| 第1章 | 40% | 生成AIの議論を拡張 |
| 第2章 | **90%** | 「執政の創造性」論文を統合完了 |
| 第3章 | 60% | STOフレームワークとの統合 |
| 第4章 | **95%** | ほぼそのまま |
| 第5章 | **80%** | ZK-SNARKs論文等の統合 |
| 第6章 | 50% | 各章からの演繹的構成 |
| 第7章 | 70% | 全体の統合 |

---

## 次のステップ

1. **第1章・第7章の執筆**: 全体の整合性を確保し、導入と結論を仕上げる
2. **第3章の補筆**: 公共交通計画のデータ分析（`publictransportplan/`）の統合
3. **第5章・第6章の最終調整**: 提案システムと制度設計の論理的接続を再確認
4. **全体の一貫性**: 「認知バイアス → 生成AI支援 → ZK-SNARKs → 制度設計」という論理を貫通させる

---

## 未確認ファイル（内容確認が必要）

- `Presentations_Archive/第1章.pdf` - 公共交通政策の章？
- `Presentations_Archive/「地域公共交通政策」の存立理由...pdf` - 詳細な制度分析？
- `Presentations_Archive/20241207.pdf`, `20241116.pdf` - プレゼン資料
- `RobotArmProject/docs/presentations/【計画行政2024名古屋】連携と協働の再構築.pptx.pdf` - 学会発表？

---

*作成日: 2026年2月20日*
