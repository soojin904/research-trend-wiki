---
title: "Exponential random graph models for little networks"
authors: ['George G. Vega Yon', 'Andrew J. Slaughter', 'Kayla de la Haye']
year: 2020
venue: "Social Networks"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Stochastic processes and statistical mechanics']
source: raw/2020_openalex_Exponential_random_graph_models_for_little_j_socnet_2020_07_005.md
---

# Exponential random graph models for little networks
**제목(한글)**: 소규모 네트워크를 위한 지수 랜덤 그래프 모델

**저자**: George G. Vega Yon; Andrew J. Slaughter; Kayla de la Haye
**출처**: Social Networks, Vol.64, pp.225–238
**발행일**: 2020-08-04
**DOI**: https://doi.org/10.1016/j.socnet.2020.07.005

## 한국어 요약

**연구질문**: 팀, 가족, 개인 네트워크와 같은 소규모 네트워크에 ERGM(지수 랜덤 그래프 모델)을 적용할 수 있는 효과적인 추정 방법은 무엇인가?

**방법론**:
- 소규모 네트워크 대상 완전 열거(exhaustive enumeration)를 통한 ERGM 추정
- 최대 우도 추정(MLE) 기반 풀링 ERGM R 패키지("ergmito") 개발
- 광범위한 시뮬레이션 연구로 MLE 추정량 특성 평가

**주요 결과**:
- 직접 MLE 추정이 근사 방법 대비 여러 이점 확인
- ergmito 패키지를 통해 소규모 네트워크 ERGM 분석이 실용적으로 가능해짐
- 팀·가족·개인 네트워크 연구에 방법론적 혁신 기반 마련


## 초록 (원문)

Statistical models for social networks have enabled researchers to study complex social phenomena that give rise to observed patterns of relationships among social actors and to gain a rich understanding of the interdependent nature of social ties and actors. Much of this research has focused on social networks within medium to large social groups. To date, these advances in statistical models for social networks, and in particular, of Exponential-Family Random Graph Models (ERGMS), have rarely been applied to the study of small networks, despite small network data in teams, families, and personal networks being common in many fields. In this paper, we revisit the estimation of ERGMs for small networks and propose using exhaustive enumeration when possible. We developed an R package that implements the estimation of pooled ERGMs for small networks using Maximum Likelihood Estimation (MLE), called “ergmito”. Based on the results of an extensive simulation study to assess the properties of the MLE estimator, we conclude that there are several benefits of direct MLE estimation compared to approximate methods and that this creates opportunities for valuable methodological innovations that can be applied to modeling social networks with ERGMs.

## 키워드

Exponential random graph models, Estimator, Computer science, Interdependence, Social network analysis, Social network (sociolinguistics), Random graph, Data science

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

