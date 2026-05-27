---
title: "A Mechanism and Optimization Study on the Impact of Information Density on User-Generated Content Named Entity Recognition"
authors: ['蒋小波 Jiang Xiaobo', 'Dinghong Lai', 'Song Qiu', 'Yadong Deng', 'Xinkai Zhan']
year: 2026
publication_date: 2026-04-21
venue: "ArXiv.org"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7155452422"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Mental Health via Writing', 'Advanced Graph Neural Networks']
keywords: ['Named-entity recognition', 'Robustness (evolution)', 'Annotation', 'Class (philosophy)', 'Alias', 'Entity linking', 'Key (lock)', 'Noise (video)']
source: openalex-keyword
---

# A Mechanism and Optimization Study on the Impact of Information Density on User-Generated Content Named Entity Recognition

**저자**: 蒋小波 Jiang Xiaobo; Dinghong Lai; Song Qiu; Yadong Deng; Xinkai Zhan
**출처**: ArXiv.org
**발행일**: 2026-04-21
**DOI**: 
**수집 키워드**: text analysis

## 초록

Named Entity Recognition (NER) models trained on clean, high-resource corpora exhibit catastrophic performance collapse when deployed on noisy, sparse User-Generated Content (UGC), such as social media. Prior research has predominantly focused on point-wise symptom remediation -- employing customized fine-tuning to address issues like neologisms, alias drift, non-standard orthography, long-tail entities, and class imbalance. However, these improvements often fail to generalize because they overlook the structural sparsity inherent in UGC. This study reveals that surface-level noise symptoms share a unified root cause: low Information Density (ID). Through hierarchical confounding-controlled resampling experiments (specifically controlling for entity rarity and annotation consistency), this paper identifies ID as an independent key factor. We introduce Attention Spectrum Analysis (ASA) to quantify how reduced ID causally leads to ``attention blunting,'' ultimately degrading NER performance. Informed by these mechanistic insights, we propose the Window-Aware Optimization Module (WOM), an LLM-empowered, model-agnostic framework. WOM identifies information-sparse regions and utilizes selective back-translation to directionally enhance semantic density without altering model architecture. Deployed atop mainstream architectures on standard UGC datasets (WNUT2017, Twitter-NER, WNUT2016), WOM yields up to 4.5\% absolute F1 improvement, demonstrating robustness and achieving new state-of-the-art (SOTA) results on WNUT2017.

## 키워드

Named-entity recognition, Robustness (evolution), Annotation, Class (philosophy), Alias, Entity linking, Key (lock), Noise (video), Named entity

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.833)
- Mental Health via Writing (score: 0.027)
- Advanced Graph Neural Networks (score: 0.024)

## 메모

