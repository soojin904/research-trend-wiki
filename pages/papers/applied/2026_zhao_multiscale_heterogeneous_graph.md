---
title: "A Multi-Scale Heterogeneous Graph Attention Network for Nested Named Entity Recognition with Syntactic and Dependency Tree Structures"
authors: ['Yifan Zhao', 'Lin Zhang', 'Yangshuyi Xu']
year: 2026
venue: "Electronics"
tags: ['Topic Modeling', 'Advanced Graph Neural Networks', 'Machine Learning in Healthcare']
source: raw/applied/applied_2026_A_MultiScale_Heterogeneou_electronics15061183.md
---

# A Multi-Scale Heterogeneous Graph Attention Network for Nested Named Entity Recognition with Syntactic and Dependency Tree Structures
**제목(한글)**: 구문 및 의존성 트리 구조를 반영한 중첩 개체명 인식용 다중 스케일 이기종 그래프 어텐션 네트워크

**저자**: Yifan Zhao; Lin Zhang; Yangshuyi Xu
**출처**: Electronics, Vol.15, pp.1183-1183
**발행일**: 2026-03-12
**DOI**: https://doi.org/10.3390/electronics15061183

## 한국어 요약

**연구질문**: 문장 내 텍스트 스팬(spans)이 계층적으로 중첩되어 경계 충돌 및 장거리 의존성 모델링이 어려운 중첩 개체명 인식(Nested NER) 문제를 문법 정보 구조 결합으로 해결할 수 있는가?

**방법론**:
- 구문 구조 트리의 계층 제한 조건과 의존성 트리의 단어 관계를 단일 이기종 그래프(heterogeneous graph) 공간에 매핑하는 모델 설계
- 1, 2, 3홉(hop)의 다중 스케일 서브그래프를 유기적으로 생성하고 어텐션을 통해 각 수용야(receptive field) 내 로컬 정보와 글로벌 종속성을 적응형 결합
- ACE2004, ACE2005, GENIA 표준 벤치마크 데이터셋 활용 및 KBP2017, GermEval2014 교차 언어 일반화 테스트

**주요 결과**:
- 제안된 MHGAT 모델이 최신 NER 모델 대비 장문의 중첩 개체 및 희소 개체 탐지 정확도에서 압도적 우위를 입증
- 여러 이종 데이터셋과 복수 언어 환경 전반에서 중첩 형태의 엔티티 경계를 깨끗하게 포착하여 모델의 일반화(generalization) 가능성 확인


## 초록 (원문)

Nested Named Entity Recognition (nested NER) frequently encounters challenges like boundary conflicts, complications in modeling long-distance dependencies, and inadequate representation of deep nested semantics resulting from overlapping spans and hierarchical inclusion relationships of entities. This research presents a multi-scale heterogeneous graph attention network to facilitate end-to-end recognition of nested entities through the collaborative modeling of structure and semantics. The model initially presents the structural integration mechanism, which consolidates the hierarchical restrictions of the syntactic tree and the inter-word relationships of the dependency tree within a singular heterogeneous graph space. It subsequently generates 1/2/3-hop multi-scale subgraphs and employs multi-scale subgraph attention to adaptively integrate information from various structural receptive fields, harmonizing the local cues of shallow entities with the global dependencies of deep entities. The experimental findings on the ACE2004, ACE2005, and GENIA benchmark datasets indicate that the proposed method surpasses several robust baselines regarding overall performance and nested entity recognition, particularly exhibiting notable advantages in identifying long entities and low-frequency entities. We further evaluate MHGAT on KBP2017 and GermEval2014 to validate generalization across datasets and languages.

## 키워드

Dependency (UML), Graph, Generalization, Tree (set theory), Benchmark (surveying), Semantics (computer science), Tree structure

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

