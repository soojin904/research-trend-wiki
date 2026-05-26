---
title: "Random effects in dynamic network actor models"
authors: ['Alvaro Uzaheta', 'Viviana Amati', 'Christoph Stadtfeld']
year: 2023
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Social Media and Politics']
source: raw/2023_openalex_Random_effects_in_dynamic_network_actor_nws_2022_37.md
---

# Random effects in dynamic network actor models
**제목(한글)**: 동적 네트워크 행위자 모형에서의 랜덤 효과

**저자**: Alvaro Uzaheta; Viviana Amati; Christoph Stadtfeld
**출처**: Network Science, Vol.11, pp.249–266
**발행일**: 2023-02-06
**DOI**: https://doi.org/10.1017/nws.2022.37


## 한국어 요약

**연구질문**: DyNAM(동적 네트워크 행위자 모형)의 동질성 가정을 완화하여 행위자 또는 맥락 간 미관측 이질성을 어떻게 통제할 수 있는가?

**방법론**:
- DyNAM에 랜덤 효과 파라미터 추가 확장
- 조건부 다항 로짓 모형(conditional multinomial logit)에 랜덤 효과 통합
- 온라인 디자이너 커뮤니티의 관계적 사건 데이터에 적용

**주요 결과**:
- 랜덤 효과 DyNAM이 행위자·맥락 간 미관측 이질성을 효과적으로 통제
- 동질성 가정 위반 시 발생하는 추정 편향을 개선
- 디자이너 커뮤니티에서의 상호작용 패턴에 대한 보다 정밀한 분석 제공


## 초록 (원문)

Abstract Dynamic Network Actor Models (DyNAMs) assume that an observed sequence of relational events is the outcome of an actor-oriented decision process consisting of two decision levels. The first level represents the time until an actor initiates the next relational event, modeled by an exponential distribution with an actor-specific activity rate. The second level describes the choice of the receiver of the event, modeled by a conditional multinomial logit model. The DyNAM assumes that the parameters are constant over the actors and the context. This homogeneity assumption, albeit statistically and computationally convenient, is difficult to justify, e.g., in the presence of unobserved differences between actors or contexts. In this paper, we extend DyNAMs by including random-effects parameters that vary across actors or contexts and allow controlling for unknown sources of heterogeneity. We illustrate the model by analyzing relational events among the users of an online community of aspiring and professional digital and graphic designers.

## 키워드

Computer science, Multinomial logistic regression, Exponential random graph models, Multinomial distribution, Event (particle physics), Outcome (game theory), Constant (computer programming), Decision process

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

