# DoctorThesis

博士論文：政策形成における生成AIと人間の関係性 - 公共交通政策を事例として

## 構成

```
.
├── main.tex           # メインファイル
├── texts/             # 各章のtexファイル
│   ├── title.tex
│   ├── abstract_ja.tex
│   ├── abstract_en.tex
│   ├── acknowledgement.tex
│   ├── publication.tex
│   ├── chapter1.tex   # 序論
│   ├── chapter2.tex   # 先行研究のレビュー
│   ├── chapter3.tex   # 公共交通政策の現状と課題
│   ├── chapter4.tex   # 認知バイアスの計算論的分析
│   ├── chapter5.tex   # ZK-SNARKs型政策評価システム
│   ├── chapter6.tex   # 制度設計への示唆
│   ├── chapter7.tex   # 結論
│   └── appendix.tex
├── refs/              # 参考文献（各章ごと）
│   ├── ref_ch1.bib
│   ├── ref_ch2.bib
│   ├── ref_ch3.bib
│   ├── ref_ch4.bib
│   ├── ref_ch5.bib
│   ├── ref_ch6.bib
│   └── ref_ch7.bib
├── figure/            # 図
└── notes/             # 論文計画・メモ
    ├── THESIS_PLAN.md
    └── FILE_MAPPING.md
```

## コンパイル方法

```bash
# LaTeXmkを使用する場合
latexmk -pvc main.tex

# 手動コンパイルの場合
lualatex main.tex
biber main
lualatex main.tex
lualatex main.tex
```

## 論文の構成

1. **第1章 序論** - 研究の背景、問題の所在、研究目的
2. **第2章 先行研究のレビュー** - Human-AI Policy、協調的ガバナンス、認知バイアス、ZK-SNARKs
3. **第3章 公共交通政策の現状と課題** - 政策変遷、制度設計、Japan MaaS分析
4. **第4章 認知バイアスの計算論的分析** - 協調ロボット制御モデルによる分析
5. **第5章 ZK-SNARKs型政策評価システム** - 生成AIと人間の関係性の具体化
6. **第6章 制度設計への示唆** - バイアス対処戦略、AIを組み込んだ制度設計
7. **第7章 結論** - 研究の総括、都市計画への展開

## 関連リポジトリ

- 既存研究: `/Volumes/UNTITLED/Obsidian/Academic_Research/`
- RobotArmProject: 認知バイアスの計算論的分析
- Research_AI_Policy: ZK-SNARKs政策評価
- Research_ZK_Snarks: ZK-SNARKs型システム

## ライセンス

MIT License
