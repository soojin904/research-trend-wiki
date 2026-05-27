---
title: "Pseudo-likelihood-based M-estimation of random graphs with dependent edges and parameter vectors of increasing dimension"
authors: ['Jonathan R. Stewart', 'Michael Schweinberger']
year: 2026
venue: "The Annals of Statistics"
tags: ['Bayesian Modeling and Causal Inference', 'Statistical Methods and Inference', 'Markov Chains and Monte Carlo Methods']
source: raw/applied/applied_2026_Pseudolikelihoodbased_Mes_25_aos2535.md
---

# Pseudo-likelihood-based M-estimation of random graphs with dependent edges and parameter vectors of increasing dimension
**제목(한글)**: 종속적 에지 및 증가하는 차원의 매개변수 벡터를 가진 무작위 그래프의 유사 우도 기반 M-추정

**저자**: Jonathan R. Stewart; Michael Schweinberger
**출처**: The Annals of Statistics, Vol.54
**발행일**: 2026-02-01
**DOI**: https://doi.org/10.1214/25-aos2535

## 한국어 요약

**연구질문**: 통계적 네트워크 분석 시 복잡한 종속 에지 관계와 고차원 파라미터를 가짐에도 수치 계산이 가능하고 통계적 수렴성을 보장하는 무작위 그래프 추정 기법을 어떻게 설계할 수 있는가?

**방법론**:
- 우도 함수 연산이 불가능한 discrete undirected graphical model에 대해 유사 우도(Pseudo-likelihood) 기반 M-estimator 모델 정립
- 단일 관측 시나리오 하에서 매개변수 차원이 늘어날 때의 수렴율(Convergence rates) 유도
- 통계적 위상 전이(Phase transition) 및 모델 축퇴(Degeneracy) 현상이 수렴 정밀도에 미치는 영향 분석
- 중첩 서브그룹을 통해 종속성을 제어하는 새로운 일반화 베타 모델 설계

**주요 결과**:
- 제안하는 유사 우도 기반 추정기가 밀집(Dense) 및 희소(Sparse) 그래프 환경 모두에서 계산 복잡도를 낮추며 수렴 안정성을 확보함을 수학적으로 증명
- 공간 및 시계열 분석 시 종속 네트워크 모델 추정에 활용할 수 있는 통계학적 증명을 제공함


## 초록 (원문)

An important question in statistical network analysis is how to estimate models of discrete and dependent network data with intractable likelihood functions, without sacrificing computational scalability and statistical guarantees. We demonstrate that scalable estimation of random graph models with dependent edges is possible, by establishing convergence rates of pseudo-likelihood-based M-estimators for discrete undirected graphical models with exponential parameterizations and parameter vectors of increasing dimension in single-observation scenarios. We highlight the impact of two complex phenomena on the convergence rate: phase transitions and model near-degeneracy. The main results have possible applications to discrete and dependent network, spatial, and temporal data. To showcase convergence rates, we introduce a novel class of generalized β-models with dependent edges and parameter vectors of increasing dimension, which leverage additional structure in the form of overlapping subpopulations to control dependence. We establish convergence rates of pseudo-likelihood-based M-estimators for generalized β-models in dense- and sparse-graph settings.

## 키워드

Estimator, Consistency (knowledge bases), Mathematics, Random graph, Dimension (graph theory), Random variable, Convergence (economics), Multivariate random variable

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

