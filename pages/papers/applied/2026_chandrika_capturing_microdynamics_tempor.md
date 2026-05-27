---
title: "Capturing Microdynamics of Temporal Network Growth: An HMM-Based Model of Triadic Closure"
authors: ['Vidyalekshmi Chandrika', 'Lekshmi S. Nair', 'Tummalapalli Sanjit Teja']
year: 2026
venue: "IEEE Access"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Opportunistic and Delay-Tolerant Networks']
source: raw/applied/applied_2026_Capturing_Microdynamics_o_access_2026_3653512.md
---

# Capturing Microdynamics of Temporal Network Growth: An HMM-Based Model of Triadic Closure
**제목(한글)**: 시계열 네트워크 성장의 미세 역학 포착: HMM 기반 삼항 폐쇄 모델

**저자**: Vidyalekshmi Chandrika; Lekshmi S. Nair; Tummalapalli Sanjit Teja
**출처**: IEEE Access, Vol.14, pp.8542-8560
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1109/access.2026.3653512

## 한국어 요약

**연구질문**: 소셜 네트워크 및 바이오망의 성장을 좌우하는 미세 구조인 '삼항 폐쇄'의 확률적 시간 진화 거동을 어떻게 stochastic 모델로 규명할 수 있는가?

**방법론**:
- 방향성이 있는 세 노드 간의 64개 가능한 미세 위상 패턴을 6개의 매크로 상태로 추상화한 6-state Hidden Markov Model 프레임워크 설계
- HMM 수학적 증명(stationary distribution 존재성 확인, 요동 한계 bound 정립) 및 Higgs 트위터 인터랙션 시계열 데이터셋으로 검증
- MTM, TERGM, DSBM 모델과 비교하여 성능 평가

**주요 결과**:
- 제안된 HMM 프레임워크가 시계열 연결 구조 예측에서 최고 F1-score와 함께 AUC 0.88의 압도적이고 안정적인 성능을 보임을 검증
- 복잡한 로컬 네트워크 링크 생성 역학을 수학적 근거를 바탕으로 투명하게 설명해내는 데 성공


## 초록 (원문)

Complex networks with their nontrivial topological features and rich patterns of interactions are commonly used to model real-world systems, including social networks, biological systems, and communication networks. Triads, three-node subgraphs that encapsulate local connectivity, are the elementary structural motifs of such networks. Triadic closure governs the growth of social and complex networks by capturing the microlevel dynamics that drive their evolution and cohesion. In this work, we present a theoretical, generative framework that models triadic closure as a hidden stochastic process, governed by a six-state Hidden Markov Model (HMM). By aggregating the 64 possible directed 3-node microstates into interpretable macrolevel states, we construct an HMM that describes the probabilistic evolution of triadic motifs over time and the transitions that lead to closure events. We prove through theoretical results, including the existence of stationary distributions, bounds on closure probabilities, robustness under transition perturbations, and statistical anomaly detection via divergence measures. The primary contribution of this work is theoretical, but the work is further validated using symbolic examples and experiments. We used both simulated data and the Higgs Twitter interaction dataset to analyze model behavior and closure stability. The proposed HMM is bench-marked against three existing temporal network baselines, the Motif Transition Model MTM, Temporal Exponential Random Graph Model TERGM, and Dynamic Stochastic DSBM is compared by examining the predictive performance in terms of AUC and mean log-likelihood. The proposed HMM framework demonstrates strong predictive performance with an AUC of 0.88 and a stable generalization over various horizons of prediction. Theoretical and empirical work in tandem yield an interpretable and mathematically well-grounded analysis of the time-evolving networks’ local structure dynamics.

## 키워드

Hidden Markov model, Probabilistic logic, Robustness (evolution), Closure (psychology), Generative model, Graphical model, Statistical model, Graph

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

