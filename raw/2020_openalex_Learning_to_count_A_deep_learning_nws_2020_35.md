---
title: "Learning to count: A deep learning framework for graphlet count estimation"
authors: ['Xutong Liu', 'Yu-Zhen Janice Chen', 'John C. S. Lui', 'Konstantin Avrachenkov']
year: 2020
publication_date: 2020-09-11
venue: "Network Science"
volume: "9"
issue: "S1"
pages: "S23–S60"
doi: "https://doi.org/10.1017/nws.2020.35"
oa_status: "bronze"
oa_url: "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D466ADEEDD5B93EB3C9185A50F7CBC2D/S2050124220000351a.pdf/div-class-title-learning-to-count-a-deep-learning-framework-for-graphlet-count-estimation-div.pdf"
openalex_id: "https://openalex.org/W3085094934"
tags: ['Advanced Graph Neural Networks', 'Complex Network Analysis Techniques', 'Bayesian Modeling and Causal Inference']
keywords: ['Preprocessor', 'Computer science', 'Enumeration', 'Artificial intelligence', 'Machine learning', 'Graph', 'Convolutional neural network', 'Theoretical computer science']
source: openalex
---

# Learning to count: A deep learning framework for graphlet count estimation

**저자**: Xutong Liu; Yu-Zhen Janice Chen; John C. S. Lui; Konstantin Avrachenkov
**출처**: Network Science, Vol.9 No.S1, pp.S23–S60
**발행일**: 2020-09-11
**DOI**: https://doi.org/10.1017/nws.2020.35

## 초록

Abstract Graphlet counting is a widely explored problem in network analysis and has been successfully applied to a variety of applications in many domains, most notatbly bioinformatics, social science, and infrastructure network studies. Efficiently computing graphlet counts remains challenging due to the combinatorial explosion, where a naive enumeration algorithm needs O( N k ) time for k -node graphlets in a network of size N . Recently, many works introduced carefully designed combinatorial and sampling methods with encouraging results. However, the existing methods ignore the fact that graphlet counts and the graph structural information are correlated. They always consider a graph as a new input and repeat the tedious counting procedure on a regular basis even if it is similar or exactly isomorphic to previously studied graphs. This provides an opportunity to speed up the graphlet count estimation procedure by exploiting this correlation via learning methods. In this paper, we raise a novel graphlet count learning (GCL) problem: given a set of historical graphs with known graphlet counts, how to learn to estimate/predict graphlet count for unseen graphs coming from the same (or similar) underlying distribution. We develop a deep learning framework which contains two convolutional neural network models and a series of data preprocessing techniques to solve the GCL problem. Extensive experiments are conducted on three types of synthetic random graphs and three types of real-world graphs for all 3-, 4-, and 5-node graphlets to demonstrate the accuracy, efficiency, and generalizability of our framework. Compared with state-of-the-art exact/sampling methods, our framework shows great potential, which can offer up to two orders of magnitude speedup on synthetic graphs and achieve on par speed on real-world graphs with competitive accuracy.

## 키워드

Preprocessor, Computer science, Enumeration, Artificial intelligence, Machine learning, Graph, Convolutional neural network, Theoretical computer science, Mathematics, Discrete mathematics

## 주제 분류 (OpenAlex Topics)

- Advanced Graph Neural Networks (score: 0.999)
- Complex Network Analysis Techniques (score: 0.995)
- Bayesian Modeling and Causal Inference (score: 0.949)

## 메모

