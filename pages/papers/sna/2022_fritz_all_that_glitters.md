---
title: "All that glitters is not gold: Relational events models with spurious events"
authors: ['Cornelius Fritz', 'Marius Mehrl', 'Paul W. Thurner', 'Göran Kauermann']
year: 2022
venue: "Network Science"
tags: ['Bayesian Modeling and Causal Inference', 'Complex Network Analysis Techniques', 'Data Quality and Management']
source: raw/2022_openalex_All_that_glitters_is_not_gold_nws_2022_22.md
---

# All that glitters is not gold: Relational events models with spurious events
**제목(한글)**: 빛난다고 다 금은 아니다: 허위 이벤트가 포함된 관계 이벤트 모델

**저자**: Cornelius Fritz; Marius Mehrl; Paul W. Thurner; Göran Kauermann
**출처**: Network Science, Vol.11, pp.184–204
**발행일**: 2022-09-16
**DOI**: https://doi.org/10.1017/nws.2022.22


## 한국어 요약

**연구질문**: 자동 코딩이나 센서 데이터에서 발생하는 허위 이벤트(spurious events, 오탐지)가 관계 이벤트 모델(REM)의 추정과 추론을 어떻게 편향시키며, 이를 어떻게 보정할 수 있는가?

**방법론**:
- 허위 이벤트를 모델링하는 REMSE(Relational Event Model for Spurious Events) 제안
- 경험적 베이즈(empirical Bayesian) 접근법과 데이터 증강(data augmentation)으로 추정
- 시리아 내전 전투 이벤트와 학생 공간 근접 데이터 두 사례 적용

**주요 결과**:
- 허위 이벤트가 존재할 때 기존 REM 모수 추정이 편향됨
- REMSE가 허위 이벤트를 통제하면서 실제 관계 이벤트를 더 정확하게 모델링
- 시뮬레이션과 실제 응용 모두에서 REMSE의 적합성 확인


## 초록 (원문)

Abstract As relational event models are an increasingly popular model for studying relational structures, the reliability of large-scale event data collection becomes more and more important. Automated or human-coded events often suffer from non-negligible false-discovery rates in event identification. And most sensor data are primarily based on actors’ spatial proximity for predefined time windows; hence, the observed events could relate either to a social relationship or random co-location. Both examples imply spurious events that may bias estimates and inference. We propose the Relational Event Model for Spurious Events (REMSE), an extension to existing approaches for interaction data. The model provides a flexible solution for modeling data while controlling for spurious events. Estimation of our model is carried out in an empirical Bayesian approach via data augmentation. Based on a simulation study, we investigate the properties of the estimation procedure. To demonstrate its usefulness in two distinct applications, we employ this model to combat events from the Syrian civil war and student co-location data. Results from the simulation and the applications identify the REMSE as a suitable approach to modeling relational event data in the presence of spurious events.

## 키워드

Spurious relationship, Computer science, Data mining, Event (particle physics), Inference, Bayesian probability, Identification (biology), Bayesian inference

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

