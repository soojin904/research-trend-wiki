---
title: "Integrated value iteration and simple games enable calibrated strategic coalition formation in social networks"
authors: ['Vu Duc Nghia', 'János Demetrovics', 'Duc Thi Vu']
year: 2026
publication_date: 2026-07-27
venue: "Scientific Reports"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1038/s41598-026-64149-9"
oa_status: "gold"
openalex_id: "https://openalex.org/W7171450712"
query_keyword: "social network"
tags: ['Game Theory and Voting Systems', 'Game Theory and Applications', 'Opinion Dynamics and Social Influence']
keywords: ['Markov decision process', 'Simple (philosophy)', 'Heuristic', 'Sequence (biology)', 'Discretization', 'Value (mathematics)', 'State space', 'State (computer science)']
source: openalex-keyword
---

# Integrated value iteration and simple games enable calibrated strategic coalition formation in social networks

**저자**: Vu Duc Nghia; János Demetrovics; Duc Thi Vu
**출처**: Scientific Reports
**발행일**: 2026-07-27
**DOI**: https://doi.org/10.1038/s41598-026-64149-9
**수집 키워드**: social network

## 초록

This paper proposes a practical framework that integrates deterministic synchronous value iteration with the theory of simple cooperative games to form minimal winning influencer coalitions in online social networks. The approach casts coalition building as a deterministic Markov decision process (MDP) whose terminal rewards are governed by a simple game characteristic function. A compact three-component state representation (coalition size, discretized reach, terminal flag) and three primitive actions (Add, Boost, Ignore) keep the state space finite, enabling exact value iteration with guaranteed convergence. To bridge the gap between the abstract MDP and real-world influencer data, where marginal reach increments depend on coalition composition, not merely on size, we introduce a fixed-order construction. A single greedy sequence of influencers is pre-computed once on the true follower-overlap data, and the Add action always selects the next influencer in that sequence; the marginal reach values fed into the MDP are then exact by construction, eliminating the need for instance-by-instance calibration. The learned optimal deterministic policy constructs a minimal winning coalition, and a subsequent local-search procedure refines it to a local optimum with respect to net follower reach without compromising minimality. We prove that value iteration converges to the unique optimal Q-function, that the extracted coalition is indeed minimal winning, and that the local search terminates at a locally optimal solution. The NP-hardness of finding a minimal winning coalition of maximum reach is established, justifying the heuristic nature of the reach improvement. For practitioners who prefer to retain compositional flexibility, a stochastic MDP variant that relaxes the fixed-order assumption is also outlined. Experiments on synthetic networks demonstrate that the local optimum coincides with the global optimum in all small instances, while the algorithm scales efficiently. The work delivers a production-ready framework for influencer marketing campaign design that bridges a previously unexplored gap between planning algorithms and cooperative game theory.

## 키워드

Markov decision process, Simple (philosophy), Heuristic, Sequence (biology), Discretization, Value (mathematics), State space, State (computer science), Influencer marketing

## 주제 분류 (OpenAlex Topics)

- Game Theory and Voting Systems (score: 0.567)
- Game Theory and Applications (score: 0.180)
- Opinion Dynamics and Social Influence (score: 0.127)

## 메모

