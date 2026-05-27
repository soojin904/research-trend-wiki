---
title: "Benchmarking LLMs for Pairwise Causal Discovery in Biomedical and Multi-Domain Contexts"
authors: ['Sydney Anuyah', 'Sneha Shajee-Mohan', 'Ankit-Singh Chauhan', 'Sunandan Chakraborty']
year: 2026
publication_date: 2026-01-21
venue: "ArXiv.org"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7125567362"
query_keyword: "text analysis"
tags: ['Biomedical Text Mining and Ontologies', 'Topic Modeling', 'Artificial Intelligence in Healthcare and Education']
keywords: ['Pairwise comparison', 'Benchmarking', 'Causality (physics)', 'Causation', 'Best practice', 'Causal model', 'Core (optical fiber)']
source: openalex-keyword
---

# Benchmarking LLMs for Pairwise Causal Discovery in Biomedical and Multi-Domain Contexts

**저자**: Sydney Anuyah; Sneha Shajee-Mohan; Ankit-Singh Chauhan; Sunandan Chakraborty
**출처**: ArXiv.org
**발행일**: 2026-01-21
**DOI**: 
**수집 키워드**: text analysis

## 초록

The safe deployment of large language models (LLMs) in high-stakes fields like biomedicine, requires them to be able to reason about cause and effect. We investigate this ability by testing 13 open-source LLMs on a fundamental task: pairwise causal discovery (PCD) from text. Our benchmark, using 12 diverse datasets, evaluates two core skills: 1) \textbf{Causal Detection} (identifying if a text contains a causal link) and 2) \textbf{Causal Extraction} (pulling out the exact cause and effect phrases). We tested various prompting methods, from simple instructions (zero-shot) to more complex strategies like Chain-of-Thought (CoT) and Few-shot In-Context Learning (FICL). The results show major deficiencies in current models. The best model for detection, DeepSeek-R1-Distill-Llama-70B, only achieved a mean score of 49.57\% ($C_{detect}$), while the best for extraction, Qwen2.5-Coder-32B-Instruct, reached just 47.12\% ($C_{extract}$). Models performed best on simple, explicit, single-sentence relations. However, performance plummeted for more difficult (and realistic) cases, such as implicit relationships, links spanning multiple sentences, and texts containing multiple causal pairs. We provide a unified evaluation framework, built on a dataset validated with high inter-annotator agreement ($κ\ge 0.758$), and make all our data, code, and prompts publicly available to spur further research. \href{https://github.com/sydneyanuyah/CausalDiscovery}{Code available here: https://github.com/sydneyanuyah/CausalDiscovery}

## 키워드

Pairwise comparison, Benchmarking, Causality (physics), Causation, Best practice, Causal model, Core (optical fiber)

## 주제 분류 (OpenAlex Topics)

- Biomedical Text Mining and Ontologies (score: 0.535)
- Topic Modeling (score: 0.267)
- Artificial Intelligence in Healthcare and Education (score: 0.052)

## 메모

