---
title: "Exact recovery of Granger causality graphs with unconditional pairwise tests"
authors: ['Ryan Kinnear', 'Ravi R. Mazumdar']
year: 2023
publication_date: 2023-06-06
venue: "Network Science"
volume: "11"
issue: "3"
pages: "431–457"
doi: "https://doi.org/10.1017/nws.2023.11"
oa_status: "hybrid"
oa_url: "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F39B8DA90C8C5BB52CA0529DEDB7A1B8/S2050124223000115a.pdf/div-class-title-exact-recovery-of-granger-causality-graphs-with-unconditional-pairwise-tests-div.pdf"
openalex_id: "https://openalex.org/W4379512678"
tags: ['Gene Regulatory Network Analysis', 'Gene expression and cancer classification', 'Bioinformatics and Genomic Networks']
keywords: ['Pairwise comparison', 'Granger causality', 'Causality (physics)', 'Heuristics', 'Heuristic', 'Mathematics', 'Graph', 'Computer science']
source: openalex
---

# Exact recovery of Granger causality graphs with unconditional pairwise tests

**저자**: Ryan Kinnear; Ravi R. Mazumdar
**출처**: Network Science, Vol.11 No.3, pp.431–457
**발행일**: 2023-06-06
**DOI**: https://doi.org/10.1017/nws.2023.11

## 초록

Abstract We study Granger Causality in the context of wide-sense stationary time series. The focus of the analysis is to understand how the underlying topological structure of the causality graph affects graph recovery by means of the pairwise testing heuristic. Our main theoretical result establishes a sufficient condition (in particular, the graph must satisfy a polytree assumption we refer to as strong causality ) under which the graph can be recovered by means of unconditional and binary pairwise causality testing. Examples from the gene regulatory network literature are provided which establish that graphs which are strongly causal, or very nearly so, can be expected to arise in practice. We implement finite sample heuristics derived from our theory, and use simulation to compare our pairwise testing heuristic against LASSO-based methods. These simulations show that, for graphs which are strongly causal (or small perturbations thereof) the pairwise testing heuristic is able to more accurately recover the underlying graph. We show that the algorithm is scalable to graphs with thousands of nodes, and that, as long as structural assumptions are met, exhibits similar high-dimensional scaling properties as the LASSO. That is, performance degrades slowly while the system size increases and the number of available samples is held fixed. Finally, a proof-of-concept application example shows, by attempting to classify alcoholic individuals using only Granger causality graphs inferred from EEG measurements, that the inferred Granger causality graph topology carries identifiable features.

## 키워드

Pairwise comparison, Granger causality, Causality (physics), Heuristics, Heuristic, Mathematics, Graph, Computer science, Theoretical computer science, Mathematical optimization, Artificial intelligence, Econometrics

## 주제 분류 (OpenAlex Topics)

- Gene Regulatory Network Analysis (score: 0.999)
- Gene expression and cancer classification (score: 0.992)
- Bioinformatics and Genomic Networks (score: 0.987)

## 메모

