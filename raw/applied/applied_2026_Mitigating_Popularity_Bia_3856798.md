---
title: "Mitigating Popularity Bias in Recommendation with Global Listwise Learning and Progressive Bi-Weighting"
authors: ['Tianyu Zhu', 'Jiandong Ding', 'Yansong Shi', 'Guoqing Chen', 'Jian‐Yun Nie']
year: 2026
publication_date: 2026-10-08
venue: "ACM Transactions on Information Systems"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1145/3856798"
oa_status: "bronze"
openalex_id: "https://openalex.org/W7214727511"
query_keyword: "social network"
tags: ['Recommender Systems and Techniques', 'Information Retrieval and Search Behavior', 'Advanced Bandit Algorithms Research']
keywords: ['popularity bias', 'recommender systems', 'inverse propensity scoring', 'long-tailed distributions', 'multinomial likelihood', 'bias mitigation', 'representation learning']
source: openalex-keyword
---

# Mitigating Popularity Bias in Recommendation with Global Listwise Learning and Progressive Bi-Weighting

**저자**: Tianyu Zhu; Jiandong Ding; Yansong Shi; Guoqing Chen; Jian‐Yun Nie
**출처**: ACM Transactions on Information Systems
**발행일**: 2026-10-08
**DOI**: https://doi.org/10.1145/3856798
**수집 키워드**: social network

## 초록

In recommender systems, user feedback typically follows a long-tail distribution, which leads many recommendation algorithms to exacerbate popularity bias by disproportionately favoring popular items. To mitigate this issue, recent studies have employed Inverse Propensity Scoring (IPS) to rebalance training data via reweighting user-item interactions. However, the effectiveness of IPS-based approaches is often constrained by locally unbiased objectives and inaccurate propensity estimation. In this paper, we propose Multinomial Likelihood with Bi-Weighting (Mult-BiW) to address these limitations. First, we introduce a debiasing framework, termed Mult-IPS, which integrates multinomial likelihood with IPS to capture global and unbiased user preferences over the entire item set. Second, we develop a Bi-Weighting (BiW) strategy that jointly leverages propensity scores and a collection model, incorporating a smoothing mechanism to enhance the robustness of propensity estimation. We further provide theoretical analyses that establish an upper bound on the empirical bias and characterize the optimal form of the collection model. Third, to mitigate the adverse effects of aggressive reweighting on representation learning, we design a Progressive Bi-Weighting strategy that gradually transitions from discriminative representation learning to popularity debiasing. Extensive experiments on real-world datasets show that Mult-BiW consistently outperforms state-of-the-art baselines.

## 키워드

popularity bias, recommender systems, inverse propensity scoring, long-tailed distributions, multinomial likelihood, bias mitigation, representation learning

## 주제 분류 (OpenAlex Topics)

- Recommender Systems and Techniques (score: 1.000)
- Information Retrieval and Search Behavior (score: 0.000)
- Advanced Bandit Algorithms Research (score: 0.000)

## 메모

