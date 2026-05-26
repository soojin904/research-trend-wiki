---
title: "Using LASSO for variable selection in exponential random graph models"
authors: ['Sergio Buttazzo', 'Göran Kauermann']
year: 2026
venue: "Social Networks"
tags: ['Complex Network Analysis Techniques', 'Mental Health Research Topics', 'Bayesian Modeling and Causal Inference']
source: raw/2026_openalex_Using_LASSO_for_variable_selection_in_j_socnet_2025_12_007.md
---

# Using LASSO for variable selection in exponential random graph models

**제목(한글)**: ERGM에서의 LASSO 변수 선택

**저자**: Sergio Buttazzo; Göran Kauermann
**출처**: Social Networks, Vol.86, pp.1–11
**발행일**: 2026-01-03
**DOI**: https://doi.org/10.1016/j.socnet.2025.12.007

## 한국어 요약

**연구질문**: LASSO 정칙화 기법을 지수 랜덤 그래프 모델(ERGM)의 변수 선택에 적용하면 모델 구조를 효과적으로 특정할 수 있는가?

**방법론**:
- ERGM 추정에 LASSO 페널티 적용 (일부 파라미터를 0으로 수축)
- 후보 모델 항목의 중요도 평가를 위한 순위 결정 절차(ranking procedure) 제안
- 표준 회귀에서 확립된 LASSO를 ERGM 프레임워크로 확장

**주요 결과**:
- LASSO가 ERGM에서 관련 변수를 자동 선택하는 데 유효함을 실증
- 모델 구조의 잘못된 지정(misspecification) 문제를 완화하는 실용적 절차 제공
- 기존 ERGM 추정 대비 변수 선택 효율성 향상

## 초록 (원문)

Exponential Random Graph Models (ERGMs) are a powerful and flexible framework for modeling network data. A fundamental challenge in ERGM estimation is the correct specification of the (sufficient) statistics that define the model structure. This paper addresses the problem of variable selection in ERGMs by making use of LASSO, a penalized estimation technique that shrinks some parameter estimates to zero, effectively selecting relevant variables. While LASSO is well established in standard regression settings, its application to ERGMs remains less explored. Here, we demonstrate how LASSO can be employed in the ERGM framework to perform variable selection and propose a ranking procedure to assess the relevance of candidate model terms.

## 키워드

Lasso (programming language), Exponential random graph models, Ranking (information retrieval), Feature selection, Model selection, Selection (genetic algorithm), Variable (mathematics), Graph

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

