---
title: "How fast do we forget our past social interactions? Understanding memory retention with parametric decays in relational event models"
authors: ['Giuseppe Arena', 'Joris Mulder', 'Roger Leenders']
year: 2023
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Mental Health Research Topics']
source: raw/2023_openalex_How_fast_do_we_forget_our_nws_2023_5.md
---

# How fast do we forget our past social interactions? Understanding memory retention with parametric decays in relational event models
**제목(한글)**: 과거 사회적 상호작용을 얼마나 빨리 잊는가? 관계적 사건 모형의 모수적 감쇠를 통한 기억 유지 이해

**저자**: Giuseppe Arena; Joris Mulder; Roger Leenders
**출처**: Network Science, Vol.11, pp.267–294
**발행일**: 2023-04-04
**DOI**: https://doi.org/10.1017/nws.2023.5

## 한국어 요약

**연구질문**: 관계적 사건 모형(REM)에서 과거 사건의 영향이 시간에 따라 어떻게 감소하는지를 모수적으로 추정하는 방법은 무엇이며, 잘못된 감쇠 함수 사용이 추정에 어떤 편향을 초래하는가?

**방법론**:
- 지수(exponential), 선형(linear), 단계(one-step) 세 가지 모수적 가중 감쇠 함수 제안
- 베이즈 인수(Bayes factor)를 통해 최적 감쇠 함수와 기억 모수 선택 방법론 개발
- 시뮬레이션 연구로 편향 분석 및 두 가지 실증 사례에 적용

**주요 결과**:
- 감쇠 함수와 기억 모수를 적절히 추정하지 않으면 추정치에 편향 발생
- 베이즈 인수로 서로 다른 기억 감쇠 모형을 직접 비교 가능
- 실증 데이터에서 과거 상호작용의 영향이 시간에 따라 비균등하게 감소함을 확인

## 초록 (원문)

Abstract In relational event networks, endogenous statistics are used to summarize the past activity between actors. Typically, it is assumed that past events have equal weight on the social interaction rate in the (near) future regardless of the time that has transpired since observing them. Generally, it is unrealistic to assume that recently past events affect the current event rate to an equal degree as long-past events. Alternatively one may consider using a prespecified decay function with a prespecified rate of decay. A problem then is that the chosen decay function could be misspecified yielding biased results and incorrect conclusions. In this paper, we introduce three parametric weight decay functions (exponential, linear, and one-step) that can be embedded in a relational event model. A statistical method is presented to decide which memory decay function and memory parameter best fit the observed sequence of events. We present simulation studies that show the presence of bias in the estimates of effects of the statistics whenever the decay, as well as the memory parameter, are not properly estimated, and the ability to test different memory models against each other using the Bayes factor. Finally, we apply the methodology to two empirical case studies.

## 키워드

Event (particle physics), Parametric statistics, Function (biology),  theorem", , , , , , , 

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

