---
title: "PGFT-IGR: position-guided feature transformation for incremental gait recognition"
authors: ['Jinyan Wang', 'Yingyi Li', 'LiangYu Dong', 'Zhanyong Mei']
year: 2026
publication_date: 2026-10-04
venue: "Scientific Reports"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1038/s41598-026-73820-0"
oa_status: "gold"
openalex_id: "https://openalex.org/W7219673542"
query_keyword: "social network"
tags: ['Gait Recognition and Analysis', 'Biometric Identification and Security', 'Domain Adaptation and Few-Shot Learning']
keywords: ['gait recognition', 'incremental learning', 'catastrophic forgetting', 'structural alignment', 'covariance correction', 'graph propagation']
source: openalex-keyword
---

# PGFT-IGR: position-guided feature transformation for incremental gait recognition

**저자**: Jinyan Wang; Yingyi Li; LiangYu Dong; Zhanyong Mei
**출처**: Scientific Reports
**발행일**: 2026-10-04
**DOI**: https://doi.org/10.1038/s41598-026-73820-0
**수집 키워드**: social network

## 초록

Real-world gait recognition systems must continuously enroll new users while coping with evolving gait patterns over time. Conventional model training methods cannot adapt to such ongoing changes, leading to catastrophic forgetting and performance degradation. Moreover, in practical scenarios, sensor wearing positions vary across users and usage habits (e.g., thigh or handheld). This observation motivates the explicit use of positional information to guide the learning of more discriminative and separable gait features. Based on these considerations, we propose the Position-Guided Feature Transformation framework for Incremental Gait Recognition (PGFT-IGR), which explicitly incorporates positional guidance and supports continuous enrollment of new users. Specifically, the framework generates pseudo-features for old classes from new class features to mitigate forgetting and retain knowledge of previously learned classes, using a structure alignment module composed of two complementary components: an isotropic scaling component that corrects the spatial distribution of pseudo-features by matching feature dispersion between new and old classes, and an affine transformation component that refines the covariance structure of pseudo-features via an affine matrix to better approximate the true distribution of old classes. Additionally, a dual-layer graph propagation module smooths feature manifolds and optimizes decision boundaries by constructing separate position and class graphs. Experimental results on the publicly available Luo-Gait and HuGaDb datasets show improvements in average accuracy by 6.56% and 2.73%, respectively, compared to current several existing methods. Ablation studies further confirm the effectiveness and complementarity of each module. This work presents a practical approach for incremental gait recognition with multi-position sensors.

## 키워드

gait recognition, incremental learning, catastrophic forgetting, structural alignment, covariance correction, graph propagation

## 주제 분류 (OpenAlex Topics)

- Gait Recognition and Analysis (score: 0.999)
- Biometric Identification and Security (score: 0.000)
- Domain Adaptation and Few-Shot Learning (score: 0.000)

## 메모

