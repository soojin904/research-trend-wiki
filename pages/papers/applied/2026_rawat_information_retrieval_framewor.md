---
title: "Information retrieval framework using knowledge graph embeddings and uncertainty modelling using probabilistic soft logic"
authors: ['Romil Rawat', 'Kamal Borana', 'Shyam Gehlot', 'Anjali Rawat', 'Hitesh Rawat', 'Chandrapal Singh Dangi']
year: 2026
venue: "Discover Computing"
tags: ['Advanced Graph Neural Networks', 'Topic Modeling', 'Graph Theory and Algorithms']
source: raw/applied/applied_2026_Information_retrieval_fra_s10791_025_09859_w.md
---

# Information retrieval framework using knowledge graph embeddings and uncertainty modelling using probabilistic soft logic
**제목(한글)**: 지식 그래프 임베딩과 확률론적 소프트 로직을 이용한 불확실성 모델링 기반 정보 검색 프레임워크

**저자**: Romil Rawat; Kamal Borana; Shyam Gehlot; Anjali Rawat; Hitesh Rawat; Chandrapal Singh Dangi
**출처**: Discover Computing, Vol.29
**발행일**: 2026-02-04
**DOI**: https://doi.org/10.1007/s10791-025-09859-w

## 한국어 요약

**연구질문**: 지식 그래프의 의미론적 구조와 확률론적 논리를 결합하여 정보 검색 시 수반되는 불확실성을 어떻게 정밀하게 정량화하고 검색 성능을 향상할 수 있는가?

**방법론**:
- 확률론적 소프트 로직(PSL)과 트랜스포머 기반 지식 그래프 임베딩(TEKGE)을 융합한 하이브리드 프레임워크 설계
- 지식 그래프 엔티티 및 관계 전반의 인식적/우연적 불확실성을 모델링하기 위해 동적 불확실성 정량화 레이어(DUQL) 및 베이지안 정규화 임베딩 기반 다중 홉 확률 그래프 탐색(MPGT) 기법 적용
- 벤치마크 데이터셋(CN15k, O*NET20k)을 활용한 성능 평가 및 등합치 예측(Conformal Prediction)을 통한 정밀성(UAP) 검증

**주요 결과**:
- 벤치마크 평가에서 nDCG@20 11.6% 상승, 평균 상위 순위(MRR) 14.2% 향상, 불확실성 고려 정밀도(UAP) 0.87 달성
- 기호적 추론과 신경망 표상 학습을 성공적으로 통합하여, 불확실성이 큰 검색 환경에서도 신뢰성 있고 설명 가능한 결과를 산출할 수 있는 확장 가능한 모델 구현


## 초록 (원문)

The growing complexity and uncertainty inherent in modern information retrieval tasks necessitate systems that can reason probabilistically while leveraging rich semantic structures. This research explores the core question: How can uncertainty-aware retrieval be enhanced through the integration of probabilistic logic and knowledge graph semantics? To address this, we introduce a novel hybrid framework that fuses probabilistic soft logic (PSL) with transformer-enhanced knowledge graph embeddings (TEKGE), further empowered by a dynamic uncertainty quantification layer (DUQL). DUQL enables granular modeling of both epistemic and aleatoric uncertainties across graph entities and relationships. Additionally, a multi-hop probabilistic graph traversal (MPGT) mechanism, informed by Bayesian-regularized contextual embeddings, guides the retrieval process. Empirical evaluations on two benchmark datasets—CN15k and O*NET20k—demonstrate the system’s effectiveness, with notable gains including an 11.6% increase in nDCG@20, a 14.2% improvement in mean reciprocal rank (MRR), and an uncertainty-aware precision (UAP) score of 0.87. The use of conformal prediction ensures statistically valid confidence calibration across retrieval outputs. This work presents a scalable and interpretable approach that combines symbolic reasoning with neural representation learning, achieving both robustness and trustworthiness in uncertain environments, the study reaffirms the importance of quantifiable confidence in semantic retrieval, contributing a resilient solution to the broader challenge of explainable and reliable information systems.

## 키워드

Probabilistic logic, Divergence-from-randomness model, Mean reciprocal rank, Graph, Scalability, Probabilistic logic network, Robustness (evolution), Knowledge representation and reasoning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

