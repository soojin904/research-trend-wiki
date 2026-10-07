---
title: "Synthesizing Graph Queries from Demonstrations"
authors: ['Xiaoyu Liu', 'Qikang Liu', 'Evan Dyce', 'Keval Vora', 'Yuepeng Wang']
year: 2026
publication_date: 2026-10-01
venue: "Proceedings of the ACM on Programming Languages"
volume: "10"
issue: "OOPSLA2"
pages: "2162-2189"
doi: "https://doi.org/10.1145/3839524"
oa_status: "diamond"
openalex_id: "https://openalex.org/W7215076282"
query_keyword: "social network"
tags: ['Graph Theory and Algorithms', 'Advanced Database Systems and Queries', 'Software Engineering Research']
keywords: ['graph mining', 'graph pattern mining', 'user study']
source: openalex-keyword
---

# Synthesizing Graph Queries from Demonstrations

**저자**: Xiaoyu Liu; Qikang Liu; Evan Dyce; Keval Vora; Yuepeng Wang
**출처**: Proceedings of the ACM on Programming Languages, Vol.10 No.OOPSLA2, pp.2162-2189
**발행일**: 2026-10-01
**DOI**: https://doi.org/10.1145/3839524
**수집 키워드**: social network

## 초록

Writing graph queries is challenging for non-experts due to the complexity of graph data models and the need to identify proper graph patterns. While recent research has advanced query synthesis for relational and document databases, the problem of synthesizing graph queries remains under-explored. We present a novel approach for synthesizing graph queries from computation demonstrations, where users specify the desired output through expressions over properties of input graphs. Our method addresses the challenge of inferring meaningful graph patterns for matching and efficiently constructing the remaining components of the query. Specifically, we combine graph mining, which identifies candidate patterns across input graphs, with deduction-based pruning, which guides an efficient synthesis of the filtering predicate and return clause. We have implemented our approach in a tool called DMiner and evaluated it on 90 benchmarks. Experimental results show that DMiner successfully synthesizes desired queries for 87 benchmarks, with an average synthesis time of 0.6 seconds per query. This outperforms both enumerative search and LLM baselines. We also conducted a user study, which shows that users can provide demonstrations with modest effort and 87.5% of the provided demonstrations are sufficient for DMiner to synthesize the desired query.

## 키워드

graph mining, graph pattern mining, user study

## 주제 분류 (OpenAlex Topics)

- Graph Theory and Algorithms (score: 0.814)
- Advanced Database Systems and Queries (score: 0.064)
- Software Engineering Research (score: 0.017)

## 메모

