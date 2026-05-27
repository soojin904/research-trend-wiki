---
title: "A two-phase bootstrap approach to facilitate conversion from text to semantic graphs"
authors: ['Mohamed Abd-Elrahem', 'Salwa El-Gamal', 'Besheer Youssef', 'M ZAKI']
year: 2025
venue: "Discover Computing"
tags: ['Sentiment Analysis and Opinion Mining', 'Advanced Graph Neural Networks', 'Graph Theory and Algorithms']
source: raw/applied/applied_2025_A_twophase_bootstrap_appr_s10791_025_09570_w.md
---

# A two-phase bootstrap approach to facilitate conversion from text to semantic graphs

**제목(한글)**: 텍스트를 의미 그래프로 변환하는 2단계 부트스트랩 접근법

## 한국어 요약

**연구질문**: 긴 텍스트를 의미 그래프(semantic graph)로 변환할 때 발생하는 단편화 문제를 어떻게 해결할 수 있는가?

**방법론**:
- 분할 정복(divide and conquer) 1단계: 입력 텍스트를 소규모 조각으로 분할 후 하위 그래프 생성
- 집중 주의(focus attention) 2단계: 부트스트랩 알고리즘으로 하위 그래프를 강연결 단일 그래프로 통합
- SRL(의미역 레이블링) 및 RDF(자원 기술 프레임워크) 활용

**주요 결과**:
- 제안 접근법이 텍스트-그래프 변환의 정확성과 사용성을 향상시킴
- 감성 분석 및 지식 그래프 구축 등 NLP 응용에 실용적으로 활용 가능

**저자**: Mohamed Abd-Elrahem; Salwa El-Gamal; Besheer Youssef; M ZAKI
**출처**: Discover Computing, Vol.28
**발행일**: 2025-12-27
**DOI**: https://doi.org/10.1007/s10791-025-09570-w

## 초록 (원문)

Abstract This paper proposes a two-phase unlearnable approach for converting a text into its semantic graph, addressing the challenge of efficiently generating a fully connected representation. Existing text-to-graph conversion tools struggle with processing long or complex texts, often resulting in fragmented representations. To overcome this, the proposed approach consists of two phases. In the first phase, divide and conquer, the input text is divided into small pieces manageable by the available text-to-graph conversion tool (e.g., Senna), yielding a collection of small subgraphs where each represents a corresponding piece of the input text. In the second phase, focus attention, these subgraphs are appended together using a bootstrapped algorithm to construct a strongly connected single graph that represents the entire input text. In these two phases, both SRL and RDF are considered and thoroughly explained. Accordingly, the corresponding algorithms for divide and conquer and focus attention are bootstrapped, evaluated, and compared. The implementation demonstrates that this approach enhances the accuracy and usability of text-to-graph conversion while remaining simple, fast, straightforward, and practical. This makes it particularly useful for NLP applications such as sentiment analysis and knowledge graph construction.

## 키워드

Focus (optics), RDF, Usability, Graph, Construct (python library), Knowledge graph, Divide and conquer algorithms

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

