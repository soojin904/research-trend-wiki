---
title: "Graph-based methods for discrete choice"
authors: ['Kiran Tomlinson', 'Austin R. Benson']
year: 2023
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Human Mobility and Location-Based Analysis', 'Opinion Dynamics and Social Influence']
source: raw/2023_openalex_Graphbased_methods_for_discrete_choice_nws_2023_20.md
---

# Graph-based methods for discrete choice
**제목(한글)**: 이산 선택을 위한 그래프 기반 방법론

**저자**: Kiran Tomlinson; Austin R. Benson
**출처**: Network Science, Vol.12, pp.21–40
**발행일**: 2023-11-06
**DOI**: https://doi.org/10.1017/nws.2023.20

## 한국어 요약

**연구질문**: 소셜 네트워크 구조를 이산 선택 모형에 통합하는 그래프 학습 기반 방법론이 개인의 선호도 예측을 어떻게 향상시킬 수 있는가?

**방법론**:
- 그래프 학습(graph learning) 기법을 이산 선택 모형에 통합하는 세 가지 방법 제안
  - 선택자(chooser) 표현 학습, 선택 모형 모수 정규화, 네트워크로부터 직접 예측
- 2016년 미국 선거 결과와 Android 앱 설치·사용 데이터에 실증 적용
- 다항 로짓(multinomial logit) 모형과 성능 비교

**주요 결과**:
- 소셜 네트워크 구조 통합이 표준 계량 경제 선택 모형 예측 향상
- 앱 설치는 사회적 맥락의 영향을 받으나 앱 사용은 습관 중심적
- 이산 선택 프레임워크가 분류·회귀 접근법보다 더 풍부한 인사이트 제공

## 초록 (원문)

Abstract Choices made by individuals have widespread impacts—for instance, people choose between political candidates to vote for, between social media posts to share, and between brands to purchase—moreover, data on these choices are increasingly abundant. Discrete choice models are a key tool for learning individual preferences from such data. Additionally, social factors like conformity and contagion influence individual choice. Traditional methods for incorporating these factors into choice models do not account for the entire social network and require hand-crafted features. To overcome these limitations, we use graph learning to study choice in networked contexts. We identify three ways in which graph learning techniques can be used for discrete choice: learning chooser representations, regularizing choice model parameters, and directly constructing predictions from a network. We design methods in each category and test them on real-world choice datasets, including county-level 2016 US election results and Android app installation and usage data. We show that incorporating social network structure can improve the predictions of the standard econometric choice model, the multinomial logit. We provide evidence that app installations are influenced by social context, but we find no such effect on app usage among the same participants, which instead is habit-driven. In the election data, we highlight the additional insights a discrete choice framework provides over classification or regression, the typical approaches. On synthetic data, we demonstrate the sample complexity benefit of using social information in choice models.

## 키워드

Multinomial logistic regression, Computer science, Discrete choice, Conformity, Machine learning, Graph, Social network (sociolinguistics), Artificial intelligence

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

