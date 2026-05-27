---
title: "Sparser, Faster, Lighter Transformer Language Models"
authors: ['Edoardo Cetin', 'Stefano Peluchetti', 'Emilio Castillo', 'Akira Naruse', 'Mana Murakami', 'Llion Jones']
year: 2026
publication_date: 2026-03-24
venue: "ArXiv.org"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7140954027"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Natural Language Processing Techniques', 'Advanced Neural Network Applications']
keywords: ['Scalability', 'Inference', 'Computation', 'CUDA', 'Transformer', 'Set (abstract data type)', 'Autoregressive model', 'Redundancy (engineering)']
source: openalex-keyword
---

# Sparser, Faster, Lighter Transformer Language Models

**저자**: Edoardo Cetin; Stefano Peluchetti; Emilio Castillo; Akira Naruse; Mana Murakami; Llion Jones
**출처**: ArXiv.org
**발행일**: 2026-03-24
**DOI**: 
**수집 키워드**: text analysis

## 초록

Scaling autoregressive large language models (LLMs) has driven unprecedented progress but comes with vast computational costs. In this work, we tackle these costs by leveraging unstructured sparsity within an LLM's feedforward layers, the components accounting for most of the model parameters and execution FLOPs. To achieve this, we introduce a new sparse packing format and a set of CUDA kernels designed to seamlessly integrate with the optimized execution pipelines of modern GPUs, enabling efficient sparse computation during LLM inference and training. To substantiate our gains, we provide a quantitative study of LLM sparsity, demonstrating that simple L1 regularization can induce over 99% sparsity with negligible impact on downstream performance. When paired with our kernels, we show that these sparsity levels translate into substantial throughput, energy efficiency, and memory usage benefits that increase with model scale. We will release all code and kernels under an open-source license to promote adoption and accelerate research toward establishing sparsity as a practical axis for improving the efficiency and scalability of modern foundation models.

## 키워드

Scalability, Inference, Computation, CUDA, Transformer, Set (abstract data type), Autoregressive model, Redundancy (engineering), Language model, Compiler

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.182)
- Natural Language Processing Techniques (score: 0.114)
- Advanced Neural Network Applications (score: 0.083)

## 메모

