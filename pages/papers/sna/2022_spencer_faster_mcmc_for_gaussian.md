---
title: "Faster MCMC for Gaussian latent position network models"
authors: ['Neil A. Spencer', 'Brian W. Junker', 'Tracy M. Sweet']
year: 2022
venue: "Network Science"
tags: ['Markov Chains and Monte Carlo Methods', 'Bayesian Methods and Mixture Models', 'Gaussian Processes and Bayesian Inference']
source: raw/2022_openalex_Faster_MCMC_for_Gaussian_latent_position_nws_2022_1.md
---

# Faster MCMC for Gaussian latent position network models
**제목(한글)**: 가우시안 잠재위치 네트워크 모델을 위한 고속 MCMC

**저자**: Neil A. Spencer; Brian W. Junker; Tracy M. Sweet
**출처**: Network Science, Vol.10, pp.20–45
**발행일**: 2022-02-22
**DOI**: https://doi.org/10.1017/nws.2022.1


## 한국어 요약

**연구질문**: 잠재위치 네트워크 모델(latent position network model)에서 기존 Metropolis within Gibbs보다 효율적인 MCMC 전략은 무엇인가?

**방법론**:
- 분할 해밀토니안 몬테카를로(split Hamiltonian Monte Carlo) 도입
- Firefly 몬테카를로와 결합한 복합 MCMC 전략 제안
- 합성 네트워크와 실제 학교 정보공유 네트워크 데이터로 성능 검증

**주요 결과**:
- 제안한 MCMC 전략이 Metropolis within Gibbs와 다른 알고리즘보다 우수한 성능 달성
- 사후 분포의 함수 형태를 활용하여 더 효율적인 사후 계산 가능
- 대규모 네트워크에서 기존 방법의 비효율(수용 비율 계산 비용, 상관된 사후 샘플)을 개선


## 초록 (원문)

Abstract Latent position network models are a versatile tool in network science; applications include clustering entities, controlling for causal confounders, and defining priors over unobserved graphs. Estimating each node’s latent position is typically framed as a Bayesian inference problem, with Metropolis within Gibbs being the most popular tool for approximating the posterior distribution. However, it is well-known that Metropolis within Gibbs is inefficient for large networks; the acceptance ratios are expensive to compute, and the resultant posterior draws are highly correlated. In this article, we propose an alternative Markov chain Monte Carlo strategy—defined using a combination of split Hamiltonian Monte Carlo and Firefly Monte Carlo—that leverages the posterior distribution’s functional form for more efficient posterior computation. We demonstrate that these strategies outperform Metropolis within Gibbs and other algorithms on synthetic networks, as well as on real information-sharing networks of teachers and staff in a school district.

## 키워드

Markov chain Monte Carlo, Posterior probability, Computer science, Gibbs sampling, Prior probability, Hybrid Monte Carlo, Monte Carlo method, Bayesian inference

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

