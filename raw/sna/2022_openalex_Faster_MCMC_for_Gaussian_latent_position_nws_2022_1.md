---
title: "Faster MCMC for Gaussian latent position network models"
authors: ['Neil A. Spencer', 'Brian W. Junker', 'Tracy M. Sweet']
year: 2022
publication_date: 2022-02-22
venue: "Network Science"
volume: "10"
issue: "1"
pages: "20–45"
doi: "https://doi.org/10.1017/nws.2022.1"
oa_status: "green"
oa_url: "https://arxiv.org/pdf/2006.07687"
openalex_id: "https://openalex.org/W3035013770"
tags: ['Markov Chains and Monte Carlo Methods', 'Bayesian Methods and Mixture Models', 'Gaussian Processes and Bayesian Inference']
keywords: ['Markov chain Monte Carlo', 'Posterior probability', 'Computer science', 'Gibbs sampling', 'Prior probability', 'Hybrid Monte Carlo', 'Monte Carlo method', 'Bayesian inference']
source: openalex
---

# Faster MCMC for Gaussian latent position network models

**저자**: Neil A. Spencer; Brian W. Junker; Tracy M. Sweet
**출처**: Network Science, Vol.10 No.1, pp.20–45
**발행일**: 2022-02-22
**DOI**: https://doi.org/10.1017/nws.2022.1

## 초록

Abstract Latent position network models are a versatile tool in network science; applications include clustering entities, controlling for causal confounders, and defining priors over unobserved graphs. Estimating each node’s latent position is typically framed as a Bayesian inference problem, with Metropolis within Gibbs being the most popular tool for approximating the posterior distribution. However, it is well-known that Metropolis within Gibbs is inefficient for large networks; the acceptance ratios are expensive to compute, and the resultant posterior draws are highly correlated. In this article, we propose an alternative Markov chain Monte Carlo strategy—defined using a combination of split Hamiltonian Monte Carlo and Firefly Monte Carlo—that leverages the posterior distribution’s functional form for more efficient posterior computation. We demonstrate that these strategies outperform Metropolis within Gibbs and other algorithms on synthetic networks, as well as on real information-sharing networks of teachers and staff in a school district.

## 키워드

Markov chain Monte Carlo, Posterior probability, Computer science, Gibbs sampling, Prior probability, Hybrid Monte Carlo, Monte Carlo method, Bayesian inference, Bayesian probability, Artificial intelligence, Machine learning, Mathematics, Statistics

## 주제 분류 (OpenAlex Topics)

- Markov Chains and Monte Carlo Methods (score: 1.000)
- Bayesian Methods and Mixture Models (score: 0.998)
- Gaussian Processes and Bayesian Inference (score: 0.997)

## 메모

