---
title: "Optimizing influence spread in multilayer networks: A layer-weighted budget allocation and community-based local dominance approach"
authors: ['Jianxin Tang', 'Lijun Liu', 'Chenshuo Li', 'Xin Wang', 'Ping Wang']
year: 2025
venue: "Physica A Statistical Mechanics and its Applications"
tags: ['Complex Network Analysis Techniques', 'Advanced Graph Neural Networks', 'Opportunistic and Delay-Tolerant Networks']
source: raw/applied/applied_2025_Optimizing_influence_spre_j_physa_2025_131203.md
---

# Optimizing influence spread in multilayer networks: A layer-weighted budget allocation and community-based local dominance approach

## 한국어 요약

[내용을 작성하십시오.]


**저자**: Jianxin Tang; Lijun Liu; Chenshuo Li; Xin Wang; Ping Wang
**출처**: Physica A Statistical Mechanics and its Applications, Vol.683, pp.131203-131203
**발행일**: 2025-12-16
**DOI**: https://doi.org/10.1016/j.physa.2025.131203

## 초록 (원문)

The influence maximization problem in multilayer social networks entails selecting seed nodes from each layer under a budget constraint to optimize the overall influence spread. However, the insufficient considerations of topological heterogeneity and cross-layer propagation synergy in existing methods result in imbalanced resource allocation and unsatisfying influence spread easily. To address such challenges, a cross-layer independent cascade model is designed to capture both intra-layer and inter-layer diffusion dynamics. Furthermore, a layer-weighted budget allocation and community-aware local dominance (LWCD) approach is proposed to address the issues of topological heterogeneity and optimal resource allocation in cross-layer propagation. It involves a three-stage process: a layer-weighted assignment method is introduced, where k-core centrality and jaccard overlap are used to quantify the importance of each layer; based on the computed layer weights, the infomap method is applied for community detection, and the budget is allocated proportionally to community sizes; finally, high-potential seed nodes within each community are identified using a local degree metric that captures node influence. Extensive experiments on synthetic and real-world multilayer networks confirm the effectiveness and stability of the proposed LWCD. Compared with state-of-the-art algorithms, LWCD achieves an average improvement of 60.68% in eight networks in terms of influence spread. The complete source code has been made publicly accessible at https://github.com/xiaogoudaidai/LWCDalgorithm to facilitate reproducibility and further research.

## 키워드

Jaccard index, Budget constraint, Maximization, Centrality, Resource allocation, Dominance (genetics), Node (physics), Metric (unit)

## 위키 연관

- [[pages/methods/centrality|Centrality]]
- [[pages/concepts/multilayer_network|다층 네트워크]]

## 메모

