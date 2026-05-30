---
title: "A Precise and Closed-Form Solution for Edge-Ranking"
authors: ['Prajjwal Nijhara', 'Jainan Tandel', 'Rohit Prajapati', 'Dip Sankar Banerjee']
year: 2025
venue: ""
tags: ['Advanced Graph Neural Networks', 'Complex Network Analysis Techniques', 'Graph Theory and Algorithms']
source: raw/applied/applied_2025_A_Precise_and_ClosedForm__3772290_3772316.md
---

# A Precise and Closed-Form Solution for Edge-Ranking

**제목(한글)**: 간선 랭킹을 위한 정밀한 닫힌 형식 해법

## 한국어 요약

**연구질문**: SimRank의 '제로 유사성(zero-similarity)' 문제와 기존 해결책들의 확장성 및 수렴 체크 비용 문제를 해결하는 정밀하고 효율적인 SimRank 계산 방법은 무엇인가?

**방법론**:
- 재귀적 유사성 정의를 닫힌 형식 방정식으로 재구성
- 행렬 분해 기법

**주요 결과**:
- 기존 방법론 대비 일관적으로 더 높은 정확도 제공
- 제로 유사성 문제를 다루는 최신 솔루션 대비 최대 3.22배 빠른 속도

**저자**: < >

## ѱ 

****: <>

****:
- <׸>

**ֿ **:
- <׸>


**저자**: Prajjwal Nijhara; Jainan Tandel; Rohit Prajapati; Dip Sankar Banerjee
**저자**: , Vol.None, pp.138-142
**저자**: 2025-12-30
**저자**: https://doi.org/10.1145/3772290.3772316

## 초록 (원문)

Quantifying node similarity is central to graph analysis, particularly in social networks. SimRank, a popular measure by Jeh and Widom [7], defines similarity recursively as two nodes are similar if they are referenced by similar nodes. However, its limitation to equal-length paths leads to the ?zero-similarity??problem, where even the structurally related nodes may score zero due to the lack of symmetric in-neighbor paths. Many approaches exist to solve this problem; however, they often require expensive convergence checks and can struggle with scalability on large graphs. To address these limitations, we propose a closed-form solution for SimRank computation. We first reformulate the recursive similarity definition into a closed-form equation and solve it via the matrix decomposition technique. Our experiments demonstrate that our formulation consistently delivers higher accuracy than traditional methods and runs up to 3.22 × faster than state-of-the-art solutions addressing the zero-similarity problem.

## 키워드

Scalability, Convergence (economics), Similarity (geometry), Node (physics), Similarity measure, Measure (data warehouse), Graph, Matrix (chemical analysis)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


