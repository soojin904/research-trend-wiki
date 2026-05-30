---
title: "Comparing LaBSE with Contrastively and Soft-Label Fine-Tuned mBERT Models for Semantic Search over a Nepali Knowledge Base"
authors: ['Dipesh Baral']
year: 2025
publication_date: 2025-12-24
venue: "International Journal on Engineering Technology"
volume: "3"
issue: "1"
pages: "146-155"
doi: "https://doi.org/10.3126/injet.v3i1.87019"
oa_status: "diamond"
openalex_id: "https://openalex.org/W7117106707"
query_keyword: "text analysis"
tags: ['Information Retrieval and Search Behavior', 'Topic Modeling', 'Expert finding and Q&A systems']
keywords: ['Nepali', 'Sentence', 'Mean reciprocal rank', 'Cosine similarity', 'Semantic similarity', 'Task (project management)', 'Similarity (geometry)']
source: openalex-keyword
---

# Comparing LaBSE with Contrastively and Soft-Label Fine-Tuned mBERT Models for Semantic Search over a Nepali Knowledge Base

**저자**: Dipesh Baral
**출처**: International Journal on Engineering Technology, Vol.3 No.1, pp.146-155
**발행일**: 2025-12-24
**DOI**: https://doi.org/10.3126/injet.v3i1.87019
**수집 키워드**: text analysis

## 초록

In this paper, the performance of multilingual sentence embedding models in semantic search for the Nepali language has been compared through three approaches: LaBSE under a zero-shot setting, mBERT fine-tuned through contrastive learning, and mBERT fine-tuned through soft similarity scores obtained by knowledge distillation from LaBSE. A customized dataset of approximately 800 labeled sentence pairs was developed from the e-commerce and appointment booking domains. The dataset contains questions written in Devanagari Nepali, with some code-mixed English. Each sentence pair was labeled as either semantically similar or dissimilar. Hard binary labels and a margin-based contrastive loss were utilized to train the contrastively trained model, while the distilled model was trained using a regression loss to match similarity scores obtained using LaBSE embeddings. All models were evaluated on a semantic retrieval task in which 89 user queries were embedded and compared with a corpus of 130 candidate sentences using cosine similarity. The quality of retrieval was calculated in terms of Top-1, Top-5, and Top-10 accuracy, and Mean Reciprocal Rank (MRR). LaBSE, without any task-specific fine-tuning, topped the results with Top-1 accuracy of 41.57% and MRR of 0.5246. The contrastively fine-tuned mBERT model achieved a Top-1 accuracy of 21.35% and MRR of 0.3204. The soft-label distilled mBERT model ranked mid-range with Top-1 accuracy of 34.83% and MRR of 0.4488, which shows that knowledge distillation can effectively transfer semantic similarity knowledge from LaBSE to mBERT. These findings demonstrate that while zero-shot LaBSE is strong, multilingual models like mBERT can be repurposed for Nepali semantic search through targeted fine-tuning. This research establishes a baseline for semantic search in Nepali and suggests practical approaches to enhancing sentence embeddings in low-resource language environments.

## 키워드

Nepali, Sentence, Mean reciprocal rank, Cosine similarity, Semantic similarity, Task (project management), Similarity (geometry)

## 주제 분류 (OpenAlex Topics)

- Information Retrieval and Search Behavior (score: 0.858)
- Topic Modeling (score: 0.068)
- Expert finding and Q&A systems (score: 0.024)

## 메모

