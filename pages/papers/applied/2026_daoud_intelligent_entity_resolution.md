---
title: "An Intelligent Entity Resolution at Scale: A Graph-Based Social Network Framework"
authors: ['Mohammad SH Daoud', 'Hussain Al-Aqrabi', 'Yousef Q. Saadeh', 'Bayan AbuShawar', 'Samer Aoudi']
year: 2026
venue: "International Journal of Advances in Soft Computing and its Applications"
tags: ['Data Quality and Management', 'Machine Learning and Data Classification', 'Topic Modeling']
source: raw/applied/applied_2026_An_Intelligent_Entity_Res_ijasca_169.md
---

# An Intelligent Entity Resolution at Scale: A Graph-Based Social Network Framework

**저자**: Mohammad SH Daoud; Hussain Al-Aqrabi; Yousef Q. Saadeh; Bayan AbuShawar; Samer Aoudi
**출처**: International Journal of Advances in Soft Computing and its Applications, Vol.18, pp.394-410
**발행일**: 2026-10-11
**DOI**: https://doi.org/10.15849/ijasca.169

## 초록 (원문)

Entity Resolution (ER) seeks to identify and merge, within one or more datasets, whichever records ultimately correspond to the same real-world entity. As one of the tasks most consequential for data quality and for the reliability of downstream analysis, ER becomes markedly harder under Big Data conditions, given the sharp rise in both the volume of data and the speed of its arrival. This work approaches ER by recasting it as a problem set within a Social Network space, so that Social Network Analysis (SNA) measures and tools can be brought to bear on it directly. A six-phase framework is proposed that represents entity records as nodes and edges of a graph and applies centrality measures to reveal redundancy among them. Four established models were evaluated against datasets of three different sizes (500, 10,000, and 2,000,000 records): k-means, Levenshtein distance, Jaro-Winkler distance, and Soundex. Levenshtein and Soundex achieved the highest measured precision (100%), while Jaro-Winkler followed closely (99.99%) and k-means trailed substantially (91.33%) despite running fastest; precision was computed as TP/(TP+FP) against RLdata10000's known duplicate structure. Because true matches make up under 0.1% of all record pairs in this dataset, these figures behave closer to a non-match specificity score than to a conventional precision measure computed over predicted matches alone, and should be interpreted with this caveat in mind. The findings indicate that the ER problem can be resolved effectively from within an SNA setting, with the Levenshtein algorithm providing the strongest balance of speed against accuracy for the proposed SNA-driven framework.

## 키워드

entity resolution, duplicate detection, social network analysis, graph-based framework, network centrality, big data, data quality, Levenshtein distance

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모

