# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENT.md

## Project Overview

Ukyo Nagata's doctoral thesis: **「政策形成における人工環境の作用と統治――メタ・ネイチャー概念に基づく地域公共交通政策の診断と生成AI・人間の役割設計――」**
(The Effects and Governance of Artificial Environments in Policy Formation: A Diagnosis of Regional Public Transport Policy and the Design of Human--AI Roles Based on the Concept of Meta-Nature)

- Mid-presentation: June 5, 2026
- Final deadline: January 1, 2027

## Build Commands

```bash
# Full compile (recommended)
lualatex main.tex && biber main && lualatex main.tex && lualatex main.tex

# Auto-recompile on change
latexmk -pvc main.tex

# Deduplicate bibliography entries
python3 refs/dedup.py refs/references.bib refs/references_deduped.bib
```

The thesis uses **LuaLaTeX** (not pdflatex) for Japanese support via `luatexja`. Bibliography is managed with **biber/biblatex** (`refs/references.bib` is the single consolidated bib file).

## File Structure

- `main.tex` — root document; includes all chapter files via `\input{}`
- `texts/` — one `.tex` file per chapter (active files: `chapter1`–`chapter7`, `chapter3_5`, `chapter6_5`)
- `refs/references.bib` — consolidated bibliography (replaces per-chapter `.bib` files)
- `figure/ch{3,4,5}/` — figures organized by chapter
- `notes/THESIS_PLAN.md` — thesis structure, narrative logic, and writing priorities
- `notes/FILE_MAPPING.md` — maps existing research files to thesis chapters

## Chapter Structure (current `main.tex` order)

| Input file | Chapter role |
|---|---|
| `chapter1.tex` | 序論 (Introduction) |
| `chapter2.tex` | 先行研究レビュー (Literature review) |
| `chapter3.tex` | 公共交通政策の現状 (Public transport policy) |
| `chapter3_5.tex` | 地域公共交通計画の運輸局間比較 (Regional plan comparison) |
| `chapter4.tex` | 認知バイアスの計算論的分析 (Cognitive bias analysis) |
| `chapter5.tex` | ZK-SNARKs型政策評価システム (ZK-SNARKs system) |
| `chapter6_5.tex` | 統合的制度ガバナンスの実証 (Empirical validation) |
| `chapter7.tex` | 結論 (Conclusion) |

Note: `chapter6.tex` exists but is not currently included in `main.tex`. Several `*_raw`, `*_full`, `*_temp` variants in `texts/` are drafts—only the canonical files above are compiled.

## Writing Style Rules（全章・全論文に適用）

- **ランドリーリストNG**：「〇〇（2014）はこう指摘した。××（2006）はこう主張している」という先行研究の羅列は禁止。著者（永田）が議論のホストとして自分の論理を主軸に置き、引用は証拠として文末に配置する。
- **引用スタイル**：`\cite{}` は文末。学者名を文の主語に繰り返さない。「〇〇とされている\cite{...}」形式を基本とする。
- **列挙禁止**：「第一に、第二に、第三に」「(1)(2)(3)」形式での羅列は禁止。論理的な因果・対比・展開として記述する。
- **ハルシネーション防止**：引用する論文・書籍は必ず原文（PDF・全文）を確認してから記述する。確認できない場合は引用しない。
- **因果語の慎重な使用**：観察研究・理論論文では「caused」「result in」など強い因果語を避け、「associated with」「suggests」等を使う。
- **重複回避**：背景・考察・結論で同型の文が繰り返されないよう注意する。

## Key Conventions

- **Bibliography**: All citations go in `refs/references.bib`. The old per-chapter bib files (`refs/ref_ch*.bib`) have been deleted; do not recreate them.
- **Cross-references**: Use `\label{}` / `\ref{}` / `\cref{}`. Duplicate labels cause compile errors—check `main.log` if compilation fails.
- **Japanese text**: Write directly in UTF-8. The `luatexja` package handles rendering; no special encoding commands needed.
- **Figures**: Place in `figure/ch{N}/` and reference with just the filename (the `\graphicspath` in `main.tex` covers all chapter subdirectories).
- **Custom commands**: `\red{}`, `\blue{}`, `\green{}`, `\highlight{}` are defined in `main.tex` for draft annotations.
