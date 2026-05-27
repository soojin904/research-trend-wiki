---
title: "Continuous latent position models for instantaneous interactions"
authors: ['Riccardo Rastelli', 'Marco Corneli']
year: 2023
venue: "Network Science"
tags: ['Data Management and Algorithms', 'Complex Network Analysis Techniques', 'Human Mobility and Location-Based Analysis']
source: raw/2023_openalex_Continuous_latent_position_models_for_instantaneous_nws_2023_14.md
---

# Continuous latent position models for instantaneous interactions
**제목(한글)**: 순간적 상호작용을 위한 연속 잠재위치 모형

**저자**: Riccardo Rastelli; Marco Corneli
**출처**: Network Science, Vol.11, pp.560–588
**발행일**: 2023-07-24
**DOI**: https://doi.org/10.1017/nws.2023.14

## 한국어 요약

**연구질문**: 이메일, 전화, 교통 네트워크처럼 순간적 상호작용이 빈번한 데이터에서 행위자의 쌍별 상호작용 타이밍과 빈도를 어떻게 모델링할 수 있는가?

**방법론**:
- 잠재위치 네트워크 모형(latent position network model)의 새로운 확장 제안
- 행위자를 잠재 유클리드 공간에 임베딩하고 시간에 따라 연속적으로 이동하는 궤적 가정
- 관찰된 상호작용 데이터로 개별 궤적 추정하는 추론 프레임워크 개발

**주요 결과**:
- 순간적 상호작용 데이터(이메일·전화·교통)의 타이밍과 빈도를 동시에 설명
- 인공 및 실제 데이터 적용에서 모형의 유효성 확인
- 동적 네트워크 분석을 위한 연속 시간 잠재위치 모형의 새로운 방향 제시

## 초록 (원문)

Abstract We create a framework to analyze the timing and frequency of instantaneous interactions between pairs of entities. This type of interaction data is especially common nowadays and easily available. Examples of instantaneous interactions include email networks, phone call networks, and some common types of technological and transportation networks. Our framework relies on a novel extension of the latent position network model: we assume that the entities are embedded in a latent Euclidean space and that they move along individual trajectories which are continuous over time. These trajectories are used to characterize the timing and frequency of the pairwise interactions. We discuss an inferential framework where we estimate the individual trajectories from the observed interaction data and propose applications on artificial and real data.

## 키워드

Computer science, Pairwise comparison, Position (finance), Phone, Artificial intelligence, Data mining

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

