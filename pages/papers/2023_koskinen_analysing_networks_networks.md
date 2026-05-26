---
title: "Analysing networks of networks"
authors: ['Johan Koskinen', 'Pete Jones', 'Darkhan Medeuov', 'Artem Antonyuk', 'Kseniia Puzyreva', 'Никита Басов']
year: 2023
venue: "Social Networks"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Advanced Graph Neural Networks']
source: raw/2023_openalex_Analysing_networks_of_networks_j_socnet_2023_02_002.md
---

# Analysing networks of networks
**제목(한글)**: 네트워크들의 네트워크 분석

**저자**: Johan Koskinen; Pete Jones; Darkhan Medeuov; Artem Antonyuk; Kseniia Puzyreva; Никита Басов
**출처**: Social Networks, Vol.74, pp.102–117
**발행일**: 2023-03-04
**DOI**: https://doi.org/10.1016/j.socnet.2023.02.002


## 한국어 요약

**연구질문**: 여러 행위자가 보고한 복수의 네트워크 관찰값이 또 다른 네트워크로 연결될 때, 이를 어떻게 통합 분석할 수 있는가?

**방법론**:
- 라인 그래프(line graph) 변환을 통해 다중 네트워크를 다층 네트워크로 재표현
- 다층 지수 랜덤 그래프 모형(multilevel ERGM) 적용
- 지역 홍수 관리 집단의 지식 사회적 구성 사례 분석

**주요 결과**:
- 다층 네트워크 표현을 통해 사회 네트워크와 보고(report) 간 연관성 분석 가능
- 라인 그래프 변환 접근법이 SAOM, 다층 블록모델 등 다양한 모형에 적용 가능
- 지역 홍수 관리 집단의 지식 구성에서 사회 구조의 역할 확인


## 초록 (원문)

We consider data with multiple observations or reports on a network in the case when these networks themselves are connected through some form of network ties. We could take the example of a cognitive social structure where there is another type of tie connecting the actors that provide the reports; or the study of interpersonal spillover effects from one cultural domain to another facilitated by the social ties. Another example is when the individual semantic structures are represented as semantic networks of a group of actors and connected through these actors’ social ties to constitute knowledge of a social group. How to jointly represent the two types of networks is not trivial as the layers and not the nodes of the layers of the reported networks are coupled through a network on the reports. We propose to transform the different multiple networks using line graphs, where actors are affiliated with ties represented as nodes, and represent the totality of the different types of ties as a multilevel network. This affords studying the associations between the social network and the reports as well as the alignment of the reports to a criterion graph. We illustrate how the procedure can be applied to studying the social construction of knowledge in local flood management groups. Here we use multilevel exponential random graph models but the representation also lends itself to stochastic actor-oriented models, multilevel blockmodels, and any model capable of handling multilevel networks.

## 키워드

Exponential random graph models, Computer science, Interpersonal ties, Social network analysis, Social connectedness, Social network (sociolinguistics), Theoretical computer science, Network science

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

