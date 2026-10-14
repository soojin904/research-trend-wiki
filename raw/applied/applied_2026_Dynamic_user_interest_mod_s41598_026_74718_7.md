---
title: "Dynamic user interest modeling and prediction integrating query box embedding with graph neural networks"
authors: ['Xu Wang']
year: 2026
publication_date: 2026-10-09
venue: "Scientific Reports"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1038/s41598-026-74718-7"
oa_status: "gold"
openalex_id: "https://openalex.org/W7221074541"
query_keyword: "social network"
tags: ['Recommender Systems and Techniques', 'Information Retrieval and Search Behavior', 'Advanced Bandit Algorithms Research']
keywords: ['temporal drift', 'graph neural networks', 'personalized recommendation', 'pairwise ranking loss', 'user-item interactions', 'gated recurrent unit']
source: openalex-keyword
---

# Dynamic user interest modeling and prediction integrating query box embedding with graph neural networks

**저자**: Xu Wang
**출처**: Scientific Reports
**발행일**: 2026-10-09
**DOI**: https://doi.org/10.1038/s41598-026-74718-7
**수집 키워드**: social network

## 초록

User interests are multi-peaked, vaguely bounded, and prone to temporal drift, yet most recommendation models still encode them as single points in a latent space, discarding coverage and uncertainty alike. This paper represents interest as a region rather than a location, and lets that region move as the interaction record grows. Timestamped user–item interactions are partitioned into overlapping graph snapshots; time-encoded attention aggregation propagates collaborative signal within each snapshot, while a gated recurrent unit carries node states across snapshot boundaries. The resulting states are projected into families of hyperrectangles defined by center and offset vectors, over which differentiable intersection, union, and score-level negation operators resolve composite interest queries such as preference for A and recent B with C excluded. Each operator is given an explicit semantics: intersection is exact and closed, union is reported both as an enclosing box and as a maintained set of disjuncts with its over-covered volume quantified, and negation acts on containment scores rather than on regions, which fixes the query grammar the framework can honestly claim. Prediction is driven by geometric drift — displacement of centers and dilation of offsets across consecutive windows — and optimized jointly with a pairwise ranking loss, volume regularization, and a temporal smoothness constraint. Because set-theoretic box embedding is already established for static personalized recommendation, the novelty claimed here lies in coupling that geometry with temporal graph propagation, not in the geometric formulation itself. Experiments on four openly licensed datasets (MovieLens-25 M, an Amazon Reviews subset, Gowalla, and Taobao UserBehavior) compare the model with eleven reproducible baselines, three of them contemporary temporal-graph recommenders, under a protocol whose training, validation, and test periods are separated before any snapshot is built. Recall@20 and NDCG@20 improve by roughly 5% to 9% over the strongest baseline, with standard deviations over ten seeds and corrected paired significance tests reported throughout. Because extra representational width can buy accuracy on its own, the model is also set against parameter-matched dynamic multi-interest and Gaussian regional controls, where the margin narrows to between 3.6% and 7.7%, and the rolling temporal evaluation is extended to all four corpora and to the strongest contemporary temporal baselines. A stride and event-multiplicity ablation shows that overlapping snapshots contribute roughly two percentage points, leaving a lead of 2.9% to 5.8% when every interaction enters a single snapshot. A purpose-built compositional benchmark scores each operator against operator-specific ground truth under both a symbolic and a behavioral definition of that truth, adding operator-level precision and calibration to recall, a region-guided deletion test, controlled against independently trained and metadata-defined regions, asks whether the geometry the model reports is the geometry it computes with, and a repeat-filtered protocol shows that every model, ours included, sheds a third or more of its apparent accuracy once previously seen items are excluded. Ablation attributes the largest share to box geometry, followed by dynamic propagation. Remaining constraints include volume degeneracy in high dimensions, closure error in union approximation, the score-level negation that leaves counting, ordering, and range queries outside the supported grammar, the absence of a human study of explanation quality, and computational overhead on large graphs.

## 키워드

temporal drift, graph neural networks, personalized recommendation, pairwise ranking loss, user-item interactions, gated recurrent unit

## 주제 분류 (OpenAlex Topics)

- Recommender Systems and Techniques (score: 1.000)
- Information Retrieval and Search Behavior (score: 0.000)
- Advanced Bandit Algorithms Research (score: 0.000)

## 메모

