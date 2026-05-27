---
title: "Inferences on mixing probabilities and ranking in mixed-membership models"
authors: ['Sohom Bhattacharya', 'Jianqing Fan', 'Jikai Hou']
year: 2026
venue: "Journal of the American Statistical Association"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Mental Health Research Topics']
source: raw/applied/applied_2026_Inferences_on_mixing_prob_01621459_2026_2671448.md
---

# Inferences on mixing probabilities and ranking in mixed-membership models
**제목(한글)**: 혼합 멤버십 모델에서의 혼합 확률 및 랭킹 추론

**저자**: Sohom Bhattacharya; Jianqing Fan; Jikai Hou
**출처**: Journal of the American Statistical Association, Vol.None, pp.1-29
**발행일**: 2026-05-18
**DOI**: https://doi.org/10.1080/01621459.2026.2671448

## 한국어 요약

**연구질문**: 금융 및 보건 네트워크에서 노드들이 특정 한 커뮤니티에만 속하지 않는 Mixed-Membership 구조를 가질 때, 각 노드의 하이브리드 커뮤니티 가중치의 통계적 불확실성을 어떻게 유한 표본 수준에서 규명하고 랭킹을 매길 수 있는가?

**방법론**:
- 네트워크 데이터 노드의 결합 성향을 차수가 교정된 혼합 멤버십(DCMM) 모델로 정립
- 각 멤버십 가중치 벡터에 대한 유한 표본 팽창 공식을 도출하고 신뢰 구간 추정
- 개별 프로필 순위 매기기 추론을 위해 승수 붓스트랩 기법 설계

**주요 결과**:
- 수학적 근거를 바탕으로 노드들의 커뮤니티 혼합 확률 분포를 명확히 정량 추정하는 공식을 확보
- 인공 데이터와 실제 경제 네트워크 상의 노드들 간 계층 구조 분석에서 랭킹 신뢰도를 크게 높임으로써 혼합 네트워크 통계적 추론 기반 마련


## 초록 (원문)

Network data is prevalent in numerous big data applications, including economics and health networks, where understanding the latent structure of the network is of prime importance. In this paper, we model the network using the Degree-Corrected Mixed Membership (DCMM) model. In the DCMM model, for each node <i>i</i>, there exists a membership vector πi=(πi(1),πi(2),…,πi(K)), where πi(k) denotes the weight that node <i>i</i> puts in community <i>k</i>. We derive a novel finite-sample expansion for the πi(k) s, which allows us to obtain asymptotic distributions and confidence intervals of the membership mixing probabilities and other related population quantities. This fills an important gap in uncertainty quantification on the member’s profile. We further develop a ranking scheme of the vertices based on the membership mixing probabilities on certain communities and perform relevant statistical inferences. A multiplier bootstrap method is proposed for ranking inference of individual membership profiles with respect to a given community. The validity of our theoretical results is further demonstrated via numerical experiments in both real and synthetic data examples.

## 키워드

Mathematics, Mixing (physics), Ranking (information retrieval), Population, Combinatorics, Discrete mathematics, Physics, Computer science

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

