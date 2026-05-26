---
title: "A generalized hypothesis test for community structure in networks"
authors: ['Eric Yanchenko', 'Srijan Sengupta']
year: 2024
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Mental Health Research Topics']
source: raw/2024_openalex_A_generalized_hypothesis_test_for_community_nws_2024_1.md
---

# A generalized hypothesis test for community structure in networks

**제목(한글)**: 네트워크 커뮤니티 구조에 대한 일반화 가설 검정

**저자**: Eric Yanchenko; Srijan Sengupta
**출처**: Network Science, Vol.12, pp.122–138
**발행일**: 2024-03-11
**DOI**: https://doi.org/10.1017/nws.2024.1

## 한국어 요약

**연구질문**: 주어진 네트워크가 통계적으로 유의미한 커뮤니티 구조를 가지고 있는지를 모델 비의존적인 방식으로 어떻게 검정할 수 있는가?

**방법론**:
- 일반화된 모델 비의존적 커뮤니티 구조 파라미터 정의
- 두 가지 가설 검정 프레임워크 제안: 점근 검정 및 부트스트랩 기반 검정
- 실제 네트워크 데이터셋에 적용하여 이론적 성질 증명 및 검증

**주요 결과**:
- 네트워크 커뮤니티 구조 존재 여부를 원칙적으로 검정하는 해석 가능한 방법론 제시
- 두 검정 프레임워크 모두 이론적 성질 증명 및 실증 데이터에서 풍부한 통찰 제공
- 기존 클러스터링 방법의 사전 단계로 커뮤니티 구조 유의성 확인에 활용 가능

## 초록 (원문)

Abstract Researchers theorize that many real-world networks exhibit community structure where within-community edges are more likely than between-community edges. While numerous methods exist to cluster nodes into different communities, less work has addressed this question: given some network, does it exhibit statistically meaningful community structure? We answer this question in a principled manner by framing it as a statistical hypothesis test in terms of a general and model-agnostic community structure parameter. Leveraging this parameter, we propose a simple and interpretable test statistic used to formulate two separate hypothesis testing frameworks. The first is an asymptotic test against a baseline value of the parameter while the second tests against a baseline model using bootstrap-based thresholds. We prove theoretical properties of these tests and demonstrate how the proposed method yields rich insights into real-world datasets.

## 키워드

Community structure, Test statistic, Statistical hypothesis testing, Statistic, Computer science, Framing (construction), Mathematics, Test (biology)

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모

