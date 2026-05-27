---
title: "Modeling roles and trade-offs in multiplex networks"
authors: ['Nikolaos Nakis', 'Sune Lehmann', 'Nicholas A. Christakis', 'Morten Mørup']
year: 2026
venue: "Nature Communications"
tags: ['Complex Network Analysis Techniques', 'Bioinformatics and Genomic Networks', 'Graph Theory and Algorithms']
source: raw/applied/applied_2026_Modeling_roles_and_tradeo_s41467_026_68896_1.md
---

# Modeling roles and trade-offs in multiplex networks
**제목(한글)**: 다중 네트워크에서의 역할 및 트레이드오프 모델링

**저자**: Nikolaos Nakis; Sune Lehmann; Nicholas A. Christakis; Morten Mørup
**출처**: Nature Communications, Vol.17
**발행일**: 2026-03-07
**DOI**: https://doi.org/10.1038/s41467-026-68896-1

## 한국어 요약

**연구질문**: 다양한 종류의 관계가 혼재된 다중 네트워크(Multiplex Network) 상에서 개별 행위자의 역할과 레이어 간 관계적 상호작용을 어떻게 수학적으로 모델링하고 예측할 것인가?

**방법론**:
- 독립성(independence), 의존성(dependence), 상호의존성(interdependence)을 동시에 산출하는 다중 잠재 트레이드오프 모델(Multiplex Latent Trade-off Model, MLT) 프레임워크 개발
- 온두라스 서부 마을의 사회적, 보건적, 경제적 관계 레이어를 포함한 176개 다중 네트워크에 적용
- 링크 예측(Link-prediction) 분석을 통한 모델 정합성 검증

**주요 결과**:
- 친구 관계와 같은 '사회적 관계망 레이어'는 행위자 간의 상호의존성(interdependence) 구조를 모사할 때 링크 예측 정확도가 극대화됨을 확인함
- 반면, 보건 및 경제적 관계 레이어는 상호의존성보다는 개인의 사회적 지위(status)나 독립적 행동 특성에 더 크게 지배받는 트레이드오프 구조를 규명함


## 초록 (원문)

Multiplex social networks capture multiple types of relations among the same people. Their structure reflects how exchanges arise from individual attributes related to independence, the status or resources of others related to dependence, and mutual influence related to interdependence. Understanding these systems is challenging because layers can play distinct yet complementary roles. We introduce the Multiplex Latent Trade-off Model, MLT, a framework for identifying roles in multiplex networks that incorporates independence, dependence, and interdependence. MLT represents roles as trade-offs, requiring each node to distribute source and target roles across layers while allocating community memberships within hierarchical structures. Applying MLT to 176 multiplex networks, including social, health, and economic layers from villages in western Honduras, we identify core principles of social exchange and reveal multi-scale communities. Link-prediction analyses show that modeling interdependence most improves predictions for social ties, whereas health and economic ties are shaped more strongly by individual status and behavior. People manage different relationships, including friendships and health-related and economic ties. The authors present a model that reveals how these layers of social life interact, showing that friendship ties rely strongly on interdependence, whereas health and economic ties are shaped more by status.

## 키워드

Multiplex, Genomics, Key (lock), Gene regulatory network

## 위키 연관

- [[pages/concepts/multilayer_network|다층 네트워크]]

## 메모

