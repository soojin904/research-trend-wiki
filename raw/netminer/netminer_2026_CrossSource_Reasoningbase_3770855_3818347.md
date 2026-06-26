---
title: "Cross-Source Reasoning-based Correction for Author Name Disambiguation"
authors: ['Fanjin Zhang', 'Yunhe Pang', 'Bo Chen', 'Zhiyu Shen', 'Yanghui Rao', 'Evgeny Kharlamov', 'Jie Tang']
year: 2026
publication_date: 2026-06-07
venue: "arXiv (Cornell University)"
publisher: "Cornell University"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1145/3770855.3818347"
openalex_id: "https://openalex.org/W7164176578"
cited_by_count: 0
fwci: 0.0
tags: ['Data Quality and Management', 'Topic Modeling', 'Authorship Attribution and Profiling']
keywords: ['Probabilistic logic', 'Robustness (evolution)', 'Annotation', 'Pipeline (software)', 'Perspective (graphical)', 'Matching (statistics)', 'Process (computing)']
source: openalex-netminer
---

# Cross-Source Reasoning-based Correction for Author Name Disambiguation

**저자**: Fanjin Zhang; Yunhe Pang; Bo Chen; Zhiyu Shen; Yanghui Rao; Evgeny Kharlamov; Jie Tang
**출처**: arXiv (Cornell University)
**발행일**: 2026-06-07
**DOI**: https://doi.org/10.1145/3770855.3818347

## 초록

Author name disambiguation is a critical challenge in academic search systems, often addressed through from-scratch and real-time disambiguation approaches. However, current algorithms remain vulnerable to cumulative errors of paper-author assignments and overlook inconsistent assignments across different sources. Resorting to expert annotation is resource-intensive. To this end, this paper explores a new perspective for author name disambiguation: cross-source correction by leveraging inconsistent assignments across sources. We propose CrossND, a full-stack framework that integrates data refinement, cross-source reasoning, and test-time scaling. First, a chain-of-refinement pipeline denoises author profiles and produces more accurate paper-author matching probabilities. Second, a supervised fine-tuning process incorporates these refined signals and a probabilistic soft logic-based cross-correction module to infer the assignments of which sources are incorrect. Third, test-time scaling further enhances the accuracy and robustness of the predictions. Experiments on real-world datasets indicate that CrossND consistently outperforms 17 baselines by leveraging cross-source reasoning without human intervention.

## 메모

