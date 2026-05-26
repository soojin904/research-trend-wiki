---
title: "DERGMs: Degeneracy-restricted exponential family random graph models"
authors: ['Vishesh Karwa', 'Sonja Petrović', 'Denis Bajić']
year: 2022
publication_date: 2022-03-01
venue: "Network Science"
volume: "10"
issue: "1"
pages: "82–110"
doi: "https://doi.org/10.1017/nws.2022.5"
oa_status: "closed"
oa_url: "https://doi.org/10.1017/nws.2022.5"
openalex_id: "https://openalex.org/W4220926869"
tags: ['Markov Chains and Monte Carlo Methods', 'Statistical Methods and Inference', 'Complex Network Analysis Techniques']
keywords: ['Exponential random graph models', 'Degeneracy (biology)', 'Exponential family', 'Inference', 'Markov chain Monte Carlo', 'Computer science', 'Random graph', 'Theoretical computer science']
source: openalex
---

# DERGMs: Degeneracy-restricted exponential family random graph models

**저자**: Vishesh Karwa; Sonja Petrović; Denis Bajić
**출처**: Network Science, Vol.10 No.1, pp.82–110
**발행일**: 2022-03-01
**DOI**: https://doi.org/10.1017/nws.2022.5

## 초록

Abstract Exponential random graph models, or ERGMs, are a flexible and general class of models for modeling dependent data. While the early literature has shown them to be powerful in capturing many network features of interest, recent work highlights difficulties related to the models’ ill behavior, such as most of the probability mass being concentrated on a very small subset of the parameter space. This behavior limits both the applicability of an ERGM as a model for real data and inference and parameter estimation via the usual Markov chain Monte Carlo algorithms. To address this problem, we propose a new exponential family of models for random graphs that build on the standard ERGM framework. Specifically, we solve the problem of computational intractability and “degenerate” model behavior by an interpretable support restriction. We introduce a new parameter based on the graph-theoretic notion of degeneracy, a measure of sparsity whose value is commonly low in real-world networks. The new model family is supported on the sample space of graphs with bounded degeneracy and is called degeneracy-restricted ERGMs, or DERGMs for short. Since DERGMs generalize ERGMs—the latter is obtained from the former by setting the degeneracy parameter to be maximal—they inherit good theoretical properties, while at the same time place their mass more uniformly over realistic graphs. The support restriction allows the use of new (and fast) Monte Carlo methods for inference, thus making the models scalable and computationally tractable. We study various theoretical properties of DERGMs and illustrate how the support restriction improves the model behavior. We also present a fast Monte Carlo algorithm for parameter estimation that avoids many issues faced by Markov Chain Monte Carlo algorithms used for inference in ERGMs.

## 키워드

Exponential random graph models, Degeneracy (biology), Exponential family, Inference, Markov chain Monte Carlo, Computer science, Random graph, Theoretical computer science, Mathematics, Graph, Monte Carlo method, Algorithm, Artificial intelligence, Machine learning, Statistics

## 주제 분류 (OpenAlex Topics)

- Markov Chains and Monte Carlo Methods (score: 0.986)
- Statistical Methods and Inference (score: 0.968)
- Complex Network Analysis Techniques (score: 0.957)

## 메모

