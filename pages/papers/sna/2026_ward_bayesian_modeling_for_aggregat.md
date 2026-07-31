---
title: "Bayesian modeling for aggregated relational data: A unified perspective"
authors: ['Owen G. Ward', 'Anna L. Smith', 'Tian Zheng']
year: 2026
venue: "Social Networks"
tags: ['Bayesian Modeling and Causal Inference']
source: raw/sna/2026_openalex_Bayesian_modeling_for_aggregated_relational_data_j_socnet_2026_06_001.md
---

# Bayesian modeling for aggregated relational data: A unified perspective

**저자**: Owen G. Ward; Anna L. Smith; Tian Zheng
**출처**: Social Networks, Vol.87, pp.61–76
**발행일**: 2026-06-13
**DOI**: https://doi.org/10.1016/j.socnet.2026.06.001

## 초록 (원문)

Aggregated relational data is widely collected to study social networks, in fields such as sociology, public health and economics. Many of the successes of ARD inference have been driven by increasingly complex Bayesian models, which provide principled and flexible ways of reflecting dependence patterns and biases encountered in real data. In this work we provide researchers with a unified collection of Bayesian implementations of existing models for ARD, within the state-of-the-art Bayesian sampling language Stan. Our implementations incorporate within-iteration rescaling procedures by default, improving algorithm run time and convergence diagnostics. Estimating ARD parameters requires carefully balancing model complexity against computational cost and data requirements, yet this trade-off has received relatively limited systematic attention in the literature. Moreover, general model comparison tools applicable across a wide range of ARD models remain underdeveloped, and existing approaches often require substantial expertise in Bayesian computation and software. Using synthetic data, we demonstrate how well competing models recover true personal network sizes and subpopulation sizes and how existing posterior predictive checks compare across a range of Bayesian ARD models. We provide code to leverage Stan’s modeling framework for exact K -fold cross-validation, and explain why approximate leave-one-out estimates often fail for many ARD models. This work highlights important connections and future directions in Bayesian modeling of ARD, providing practical guidance for selecting and evaluating Bayesian ARD models.

## 키워드

Leverage (statistics), Bayesian network, Variable-order Bayesian network, Bayesian probability, Implementation, Variety (cybernetics), Key (lock), Missing data

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

