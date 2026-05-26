---
title: "Artificial Benchmark for Community Detection (ABCD)—Fast random graph model with community structure"
authors: ['Bogumił Kamiński', 'Paweł Prałat', 'François Théberge']
year: 2021
publication_date: 2021-01-26
venue: "Network Science"
volume: "9"
issue: "2"
pages: "153–178"
doi: "https://doi.org/10.1017/nws.2020.45"
oa_status: "hybrid"
oa_url: "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/453FE29A1FA3C1798B0EC116587FE422/S2050124220000454a.pdf/div-class-title-artificial-benchmark-for-community-detection-abcd-fast-random-graph-model-with-community-structure-div.pdf"
openalex_id: "https://openalex.org/W3004293141"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Mental Health Research Topics']
keywords: ['Computer science', 'Community structure', 'Benchmark (surveying)', 'Random graph', 'Scalability', 'Graph', 'Theoretical computer science', 'Artificial intelligence']
source: openalex
---

# Artificial Benchmark for Community Detection (ABCD)—Fast random graph model with community structure

**저자**: Bogumił Kamiński; Paweł Prałat; François Théberge
**출처**: Network Science, Vol.9 No.2, pp.153–178
**발행일**: 2021-01-26
**DOI**: https://doi.org/10.1017/nws.2020.45

## 초록

Abstract Most of the current complex networks that are of interest to practitioners possess a certain community structure that plays an important role in understanding the properties of these networks. For instance, a closely connected social communities exhibit faster rate of transmission of information in comparison to loosely connected communities. Moreover, many machine learning algorithms and tools that are developed for complex networks try to take advantage of the existence of communities to improve their performance or speed. As a result, there are many competing algorithms for detecting communities in large networks. Unfortunately, these algorithms are often quite sensitive and so they cannot be fine-tuned for a given, but a constantly changing, real-world network at hand. It is therefore important to test these algorithms for various scenarios that can only be done using synthetic graphs that have built-in community structure, power law degree distribution, and other typical properties observed in complex networks. The standard and extensively used method for generating artificial networks is the LFR graph generator. Unfortunately, this model has some scalability limitations and it is challenging to analyze it theoretically. Finally, the mixing parameter μ , the main parameter of the model guiding the strength of the communities, has a non-obvious interpretation and so can lead to unnaturally defined networks. In this paper, we provide an alternative random graph model with community structure and power law distribution for both degrees and community sizes, the Artificial Benchmark for Community Detection (ABCD graph). The model generates graphs with similar properties as the LFR one, and its main parameter ξ can be tuned to mimic its counterpart in the LFR model, the mixing parameter μ . We show that the new model solves the three issues identified above and more. In particular, we test the speed of our algorithm and do a number of experiments comparing basic properties of both ABCD and LFR. The conclusion is that these models produce graphs with comparable properties but ABCD is fast, simple, and can be easily tuned to allow the user to make a smooth transition between the two extremes: pure (independent) communities and random graph with no community structure.

## 키워드

Computer science, Community structure, Benchmark (surveying), Random graph, Scalability, Graph, Theoretical computer science, Artificial intelligence, Complex network, Degree distribution, Algorithm, Machine learning, Mathematics

## 주제 분류 (OpenAlex Topics)

- Complex Network Analysis Techniques (score: 1.000)
- Opinion Dynamics and Social Influence (score: 0.999)
- Mental Health Research Topics (score: 0.984)

## 메모

