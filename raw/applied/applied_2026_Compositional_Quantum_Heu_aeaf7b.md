---
title: "Compositional Quantum Heuristics for Max-Clique Detection"
authors: ['Tiffany Duneau', 'Colin Krawchuk', 'Anna Pearson']
year: 2026
publication_date: 2026-10-02
venue: "Quantum Science and Technology"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1088/2058-9565/aeaf7b"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W7160875268"
query_keyword: "social network"
tags: ['Quantum Computing Algorithms and Architecture', 'Quantum many-body systems', 'Quantum Information and Cryptography']
keywords: ['barren plateaus', 'quantum graph neural networks', 'quantum machine learning']
source: openalex-keyword
---

# Compositional Quantum Heuristics for Max-Clique Detection

**저자**: Tiffany Duneau; Colin Krawchuk; Anna Pearson
**출처**: Quantum Science and Technology
**발행일**: 2026-10-02
**DOI**: https://doi.org/10.1088/2058-9565/aeaf7b
**수집 키워드**: social network

## 초록

Abstract Quantum machine learning holds the promise of combining the success of classical machine learning methods with the power of quantum computing, however one of the largest obstacles facing the field is the problem of barren plateaus. Parameterised quantum circuits offer a flexible framework for developing quantum machine learning models, but their practicality is constrained by a trade-off between trainability and classical simulability. In general, circuits that are sufficiently expressive to model complex behaviour often exhibit barren plateaus, where gradients vanish and optimisation fails. In this work we investigate a compositional approach to mitigate this trade-off. We exploit the recursive structure of Max-Clique by reusing a model trained on small graph instances to guide a sequence of induced-subgraph problems whose outputs are composed into a clique of the original graph. To ensure trainability of these subcomponents, we describe a framework for constructing group-invariant loss functions, which introduce symmetry-induced inductive bias and lead to improved gradient behaviour and generalisation. In particular, we use this framework to design permutation-equivariant quantum graph neural networks for identifying maximum cliques in graphs. The models we construct exhibit superior training trajectories through symmetry-induced bias, reaching accuracies up to 30% better than the un-symmetrised counterparts. Our experiments demonstrate that the trained models generalise to larger, more complex problem instances, which we demonstrate on 8 to 16 node graphs. Finally, inspired by Quantum-Informed Recursive Optimisation Algorithms [FKS+24], we implement a recursive hybrid quantum-classical heuristic using the learned quantum models to guide a classical search procedure, demonstrating improved inference accuracy and scalability. Together, these results suggest that compositional circuits could be a viable pathway towards scalable quantum learning models that remain challenging to reproduce classically.

## 키워드

barren plateaus, quantum graph neural networks, quantum machine learning

## 주제 분류 (OpenAlex Topics)

- Quantum Computing Algorithms and Architecture (score: 1.000)
- Quantum many-body systems (score: 0.000)
- Quantum Information and Cryptography (score: 0.000)

## 메모

