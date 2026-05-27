---
title: "Revising the Borgatti-Everett core-periphery model: Inter-categorical density blocks and partially connected cores"
authors: ['José Luis Estévez', 'Carl Nordlund']
year: 2024
venue: "Social Networks"
tags: ['Complex Systems and Time Series Analysis', 'Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence']
source: raw/2024_openalex_Revising_the_BorgattiEverett_coreperiphery_model_Intercategorical_j_socnet_2024_11_002.md
---

# Revising the Borgatti-Everett core-periphery model: Inter-categorical density blocks and partially connected cores

**제목(한글)**: Borgatti-Everett 핵심-주변부 모형 수정: 범주 간 밀도 블록과 부분 연결 핵심부

**저자**: José Luis Estévez; Carl Nordlund
**출처**: Social Networks, Vol.81, pp.31–51
**발행일**: 2024-12-16
**DOI**: https://doi.org/10.1016/j.socnet.2024.11.002

## 한국어 요약

**연구질문**: Borgatti-Everett 핵심-주변부 모형의 두 가지 문제(범주 간 연결 처리, 완전 연결 핵심부 정의)를 어떻게 개선할 수 있는가?

**방법론**:
- 직접 블록 모델링(direct blockmodeling) 발전을 토대로 한 모형 수정
- 정밀·최소 밀도 블록 기반 범주 간 연결 처리 방식 도입
- k-코어/k-플렉스의 비례적 변형인 p-코어(p-core) 개발

**주요 결과**:
- 기존 셀 단위 상관 방식을 밀도 블록 기반으로 대체하여 범주 간 연결 처리 개선
- p-코어는 핵심부 응집도 요건 정의에 더 큰 유연성 제공
- 모든 모형은 Socnet.se 클라이언트를 통해 구현 가능

## 초록 (원문)

Borgatti and Everett's model (2000) remains the prevailing standard for identifying categorical core-periphery structures in empirical networks, yet this method poses two significant issues. The first concerns the handling of inter-categorical ties—those linking core and periphery actors. The second problem is the model's definition of the ideal core as a complete block or clique, which can be overly stringent in practical applications. Building on advancements in direct blockmodeling, we propose modifications to address these shortcomings. To better handle inter-categorical ties, we replace the traditional cell-wise correlation approach with one based on exact- and minimum-density blocks. To relax the constraint of a fully connected core, we introduce the p-core, a proportional adaptation of the k-core/k-plex cohesive subgroups, providing greater flexibility in defining the level of cohesion required for core membership. We illustrate the advantages of these enhancements using both classic network examples and synthetic networks. • This paper addresses two limitations in Borgatti and Everett's popular model for categorical core-periphery structures. • We introduce a method that replaces the existing cell value correlation with exact- and minimum-density ideal blocks. • We implement the p-core, a proportional version of the k-core/k-plex, as a more flexible ideal block for core cohesion. • All core-periphery models mentioned in this article are implemented in Socnet.se, a novel client for direct blockmodeling.

## 키워드

Core (optical fiber), Categorical variable, Psychology, Mathematics, Computer science, Statistics

## 위키 연관

- [[pages/concepts/personal_network|퍼스널 네트워크]]

## 메모

