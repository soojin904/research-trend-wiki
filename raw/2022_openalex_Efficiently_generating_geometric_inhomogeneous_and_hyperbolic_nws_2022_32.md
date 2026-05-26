---
title: "Efficiently generating geometric inhomogeneous and hyperbolic random graphs"
authors: ['Thomas Bläsius', 'Tobias Friedrich', 'Maximilian Katzmann', 'Ulrich Meyer', 'Manuel Penschuck', 'Christopher Weyand']
year: 2022
publication_date: 2022-11-23
venue: "Network Science"
volume: "10"
issue: "4"
pages: "361–380"
doi: "https://doi.org/10.1017/nws.2022.32"
oa_status: "hybrid"
oa_url: "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EE2080A5FEC3A6C2B3AB451934A340AC/S2050124222000327a.pdf/div-class-title-efficiently-generating-geometric-inhomogeneous-and-hyperbolic-random-graphs-div.pdf"
openalex_id: "https://openalex.org/W2945615200"
tags: ['Complex Network Analysis Techniques', 'Graph Theory and Algorithms', 'Topological and Geometric Data Analysis']
keywords: ['Degree distribution', 'Random graph', 'Degree (music)', 'Generator (circuit theory)', 'Computer science', 'Mathematics', 'Graph', 'Theoretical computer science']
source: openalex
---

# Efficiently generating geometric inhomogeneous and hyperbolic random graphs

**저자**: Thomas Bläsius; Tobias Friedrich; Maximilian Katzmann; Ulrich Meyer; Manuel Penschuck; Christopher Weyand
**출처**: Network Science, Vol.10 No.4, pp.361–380
**발행일**: 2022-11-23
**DOI**: https://doi.org/10.1017/nws.2022.32

## 초록

Abstract Hyperbolic random graphs (HRGs) and geometric inhomogeneous random graphs (GIRGs) are two similar generative network models that were designed to resemble complex real-world networks. In particular, they have a power-law degree distribution with controllable exponent $\beta$ and high clustering that can be controlled via the temperature $T$ . We present the first implementation of an efficient GIRG generator running in expected linear time. Besides varying temperatures, it also supports underlying geometries of higher dimensions. It is capable of generating graphs with ten million edges in under a second on commodity hardware. The algorithm can be adapted to HRGs. Our resulting implementation is the fastest sequential HRG generator, despite the fact that we support non-zero temperatures. Though non-zero temperatures are crucial for many applications, most existing generators are restricted to $T = 0$ . We also support parallelization, although this is not the focus of this paper. Moreover, we note that our generators draw from the correct probability distribution, that is, they involve no approximation. Besides the generators themselves, we also provide an efficient algorithm to determine the non-trivial dependency between the average degree of the resulting graph and the input parameters of the GIRG model. This makes it possible to specify the desired expected average degree as input. Moreover, we investigate the differences between HRGs and GIRGs, shedding new light on the nature of the relation between the two models. Although HRGs represent, in a certain sense, a special case of the GIRG model, we find that a straightforward inclusion does not hold in practice. However, the difference is negligible for most use cases.

## 키워드

Degree distribution, Random graph, Degree (music), Generator (circuit theory), Computer science, Mathematics, Graph, Theoretical computer science, Complex network, Power (physics), Combinatorics

## 주제 분류 (OpenAlex Topics)

- Complex Network Analysis Techniques (score: 0.996)
- Graph Theory and Algorithms (score: 0.989)
- Topological and Geometric Data Analysis (score: 0.988)

## 메모

