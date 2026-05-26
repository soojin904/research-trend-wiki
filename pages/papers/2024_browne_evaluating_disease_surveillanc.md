---
title: "Evaluating disease surveillance strategies for early outbreak detection in contact networks with varying community structure"
authors: ['Axel Browne', 'David Butts', 'Edgar Jaramillo-Rodriguez', 'Nidhi Parikh', 'Geoffrey Fairchild', 'Zach Needell', 'Cristian Poliziani', 'Tom Wenzel', 'Timothy C. Germann', 'Sara Y. Del Valle']
year: 2024
venue: "Social Networks"
tags: ['Data-Driven Disease Surveillance', 'COVID-19 epidemiological studies', 'Complex Network Analysis Techniques']
source: raw/2024_openalex_Evaluating_disease_surveillance_strategies_for_early_j_socnet_2024_06_003.md
---

# Evaluating disease surveillance strategies for early outbreak detection in contact networks with varying community structure

**제목(한글)**: 다양한 커뮤니티 구조를 가진 접촉 네트워크에서의 조기 발병 탐지를 위한 질병 감시 전략 평가

**저자**: Axel Browne; David Butts; Edgar Jaramillo-Rodriguez; Nidhi Parikh; Geoffrey Fairchild; Zach Needell; Cristian Poliziani; Tom Wenzel; Timothy C. Germann; Sara Y. Del Valle
**출처**: Social Networks, Vol.79, pp.122–132
**발행일**: 2024-07-10
**DOI**: https://doi.org/10.1016/j.socnet.2024.06.003

## 한국어 요약

**연구질문**: 다양한 커뮤니티 구조를 가진 접촉 네트워크에서 COVID형 발병의 조기 경보를 위한 최적의 센서 선택 전략은 무엇인가?

**방법론**:
- 5가지 센서 선택 전략을 합성 접촉 네트워크 4개 시나리오에서 평가
- 뉴욕시 680만 명 규모 에이전트 기반 시뮬레이션 네트워크 포함
- 네트워크 커뮤니티 구조 변화에 따른 전략 성능 비교

**주요 결과**:
- 최적 전략은 네트워크의 커뮤니티 구조에 크게 의존
- 고연결 노드 선택·네트워크 커버리지 최대화 전략은 여러 구조에서 효과적이나 실제 적용에 한계
- '무작위 체인(random chain)' 전략은 네트워크 사전 지식 없이도 안정적 조기 경보 제공

## 초록 (원문)

Disease surveillance systems allow public health agencies to respond to emerging diseases before they become widespread. Developing such systems requires identifying optimal ways to monitor in the context of an epidemic outbreak; this problem is known as sensor selection. Contact networks represent the dynamics of interaction in a population and are used to model how a disease spreads in a population and to explore strategies of sensor selection. We evaluated five sensor selection strategies on their ability to provide an early warning of a COVID-like outbreak in synthetic contact networks encapsulated in four network scenarios. Three of these scenarios assessed different aspects of community structure. The fourth scenario employed a contact network representing the population and interactions of 6.8 million people in New York City, constructed from an agent-based simulation using census and transportation data. This scenario exemplifies how sensor selection strategies may perform in a real-world, urban context. Our findings suggest that the choice of the optimal strategy depends heavily on the community structure of the network. Strategies that select highly connected nodes or maximize network coverage are the optimal surveillance strategy for outbreak detection in many network community structures. However, a naive implementation of these strategies may fail to provide an early warning at all—including in the New York City scenario. Moreover, these methods are impractical for real-world use as they require knowledge of the underlying contact network. Instead, a selection strategy that starts with a set of random nodes and then performs a random walk through a chain of neighbors reliably provides early warnings without requiring prior knowledge of the network. We find this method, called “random chain”, to be the most pragmatic for implementation in a real-world disease surveillance context.

## 키워드

Context (archaeology), Computer science, Population, Selection (genetic algorithm), Warning system, Outbreak, Disease surveillance, Data science

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/centrality|Centrality]]

## 메모

