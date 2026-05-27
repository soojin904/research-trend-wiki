---
title: "MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models"
authors: ['Xiyu Ren', 'Zhaowei Wang', 'Yiming Du', 'Zhongwei Xie', 'Chi Liu', 'Xinlin Yang', 'Haoyue Feng', 'Wenjun Pan', 'Tianshi Zheng', 'Baixuan Xu', 'Zhengnan Li', 'Yangqiu Song', 'Ginny Wong', 'Simon See']
year: 2026
publication_date: 2026-05-14
venue: "ArXiv.org"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7161452593"
query_keyword: "text analysis"
tags: ['Multimodal Machine Learning Applications', 'Topic Modeling', 'Domain Adaptation and Few-Shot Learning']
keywords: ['Benchmark (surveying)', 'Benchmarking', 'Context (archaeology)', 'Code (set theory)', 'Visual reasoning', 'Fidelity']
source: openalex-keyword
---

# MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models

**저자**: Xiyu Ren; Zhaowei Wang; Yiming Du; Zhongwei Xie; Chi Liu; Xinlin Yang; Haoyue Feng; Wenjun Pan; Tianshi Zheng; Baixuan Xu; Zhengnan Li; Yangqiu Song; Ginny Wong; Simon See
**출처**: ArXiv.org
**발행일**: 2026-05-14
**DOI**: 
**수집 키워드**: text analysis

## 초록

Memory is essential for large vision-language models (LVLMs) to handle long, multimodal interactions, with two method directions providing this capability: long-context LVLMs and memory-augmented agents. However, no existing benchmark conducts a systematic comparison of the two on questions that genuinely require multimodal evidence. To close this gap, we introduce MEMLENS, a comprehensive benchmark for memory in multimodal multi-session conversations, comprising 789 questions across five memory abilities (information extraction, multi-session reasoning, temporal reasoning, knowledge update, and answer refusal) at four standard context lengths (32K-256K tokens) under a cross-modal token-counting scheme. An image-ablation study confirms that solving MEMLENS requires visual evidence: removing evidence images drops two frontier LVLMs below 2% accuracy on the 80.4% of questions whose evidence includes images. Evaluating 27 LVLMs and 7 memory-augmented agents, we find that long-context LVLMs achieve high short-context accuracy through direct visual grounding but degrade as conversations grow, whereas memory agents are length-stable but lose visual fidelity under storage-time compression. Multi-session reasoning caps most systems below 30%, and neither approach alone solves the task. These results motivate hybrid architectures that combine long-context attention with structured multimodal retrieval. Our code is available at https://github.com/xrenaf/MEMLENS.

## 키워드

Benchmark (surveying), Benchmarking, Context (archaeology), Code (set theory), Visual reasoning, Fidelity

## 주제 분류 (OpenAlex Topics)

- Multimodal Machine Learning Applications (score: 0.995)
- Topic Modeling (score: 0.001)
- Domain Adaptation and Few-Shot Learning (score: 0.001)

## 메모

