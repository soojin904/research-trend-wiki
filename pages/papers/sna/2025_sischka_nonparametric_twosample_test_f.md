---
title: "Nonparametric two-sample test for networks using joint graphon estimation"
authors: ['Benjamin Sischka', 'Göran Kauermann']
year: 2025
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Graph theory and applications', 'Limits and Structures in Graph Theory']
source: raw/2025_openalex_Nonparametric_twosample_test_for_networks_using_nws_2025_5.md
---

# Nonparametric two-sample test for networks using joint graphon estimation
**제목(한글)**: 공동 그라폰 추정을 이용한 네트워크의 비모수 이표본 검정

**저자**: Benjamin Sischka; Göran Kauermann
**출처**: Network Science, Vol.13
**발행일**: 2025-01-01
**DOI**: https://doi.org/10.1017/nws.2025.5

## 한국어 요약

**연구질문**: 부드러운 그라폰(smooth graphon) 모델과 공동 추정(joint estimation)을 활용해 두 네트워크 구조의 등가성을 검정하는 비모수 방법론을 어떻게 설계할 수 있는가?

**방법론**:
- 공동 그라폰 추정으로 다수 네트워크를 동일 그라폰 기준으로 정렬(alignment)
- EM 형 알고리즘으로 다중 네트워크 동시 적합
- 국소 에지 밀도 비교 기반 카이제곱형 검정 통계량 구성

**주요 결과**:
- 시뮬레이션에서 네트워크 비교 전략의 적용 가능성 확인
- 실제 데이터 분석 사례를 통해 방법론 효용성 시연
- 비모수 방법으로 복잡한 구조 패턴 포착하면서도 시뮬레이션 불필요

## 초록 (원문)

Abstract This paper focuses on the comparison of networks on the basis of statistical inference. For that purpose, we rely on smooth graphon models as a nonparametric modeling strategy that is able to capture complex structural patterns. The graphon itself can be viewed more broadly as local density or intensity function on networks, making the model a natural choice for comparison purposes. More precisely, to gain information about the (dis-)similarity between networks, we extend graphon estimation towards modeling multiple networks simultaneously. In particular, fitting a single model implies aligning different networks with respect to the same graphon estimate. To do so, we employ an EM-type algorithm. Drawing on this network alignment consequently allows a comparison of the edge density at local level. Based on that, we construct a chi-squared-type test on equivalence of network structures. Simulation studies and real-world examples support the applicability of our network comparison strategy.

## 키워드

Nonparametric statistics, Joint (building), Estimation, Test (biology), Computer science, Sample (material), Statistics, Artificial intelligence

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

