---
title: "Comparing LaBSE with Contrastively and Soft-Label Fine-Tuned mBERT Models for Semantic Search over a Nepali Knowledge Base"
authors: ['Dipesh Baral']
year: 2025
venue: "International Journal on Engineering Technology"
tags: ['Information Retrieval and Search Behavior', 'Topic Modeling', 'Expert finding and Q&A systems']
source: raw/applied/applied_2025_Comparing_LaBSE_with_Cont_injet_v3i1_87019.md
---

# Comparing LaBSE with Contrastively and Soft-Label Fine-Tuned mBERT Models for Semantic Search over a Nepali Knowledge Base

**제목(한글)**: 네팔어 지식 베이스 의미 검색을 위한 LaBSE와 대조 학습·소프트 레이블 파인튜닝 mBERT 비교

## 한국어 요약

**연구질문**: 네팔어 의미 검색에서 제로샷 LaBSE, 대조 학습 파인튜닝 mBERT, 지식 증류 소프트 레이블 mBERT 중 어느 방법이 가장 우수한가?

**방법론**:
- 이커머스·예약 도메인 네팔어 문장 쌍 약 800개 데이터셋 구축
- Top-1/5/10 정확도 및 MRR(평균 역수 순위) 기준 평가
- 코사인 유사도 기반 의미 검색 태스크

**주요 결과**:
- LaBSE(제로샷)가 Top-1 정확도 41.57%, MRR 0.5246으로 최고 성능
- 지식 증류 mBERT(Top-1 34.83%)가 대조 학습 mBERT(21.35%)보다 우수
- 저자원 언어에서 의미 검색을 위한 실용적 파인튜닝 방향 제시

**저자**: Dipesh Baral
**출처**: International Journal on Engineering Technology, Vol.3, pp.146-155
**발행일**: 2025-12-24
**DOI**: https://doi.org/10.3126/injet.v3i1.87019

## 초록 (원문)

In this paper, the performance of multilingual sentence embedding models in semantic search for the Nepali language has been compared through three approaches: LaBSE under a zero-shot setting, mBERT fine-tuned through contrastive learning, and mBERT fine-tuned through soft similarity scores obtained by knowledge distillation from LaBSE. A customized dataset of approximately 800 labeled sentence pairs was developed from the e-commerce and appointment booking domains. The dataset contains questions written in Devanagari Nepali, with some code-mixed English. Each sentence pair was labeled as either semantically similar or dissimilar. Hard binary labels and a margin-based contrastive loss were utilized to train the contrastively trained model, while the distilled model was trained using a regression loss to match similarity scores obtained using LaBSE embeddings. All models were evaluated on a semantic retrieval task in which 89 user queries were embedded and compared with a corpus of 130 candidate sentences using cosine similarity. The quality of retrieval was calculated in terms of Top-1, Top-5, and Top-10 accuracy, and Mean Reciprocal Rank (MRR). LaBSE, without any task-specific fine-tuning, topped the results with Top-1 accuracy of 41.57% and MRR of 0.5246. The contrastively fine-tuned mBERT model achieved a Top-1 accuracy of 21.35% and MRR of 0.3204. The soft-label distilled mBERT model ranked mid-range with Top-1 accuracy of 34.83% and MRR of 0.4488, which shows that knowledge distillation can effectively transfer semantic similarity knowledge from LaBSE to mBERT. These findings demonstrate that while zero-shot LaBSE is strong, multilingual models like mBERT can be repurposed for Nepali semantic search through targeted fine-tuning. This research establishes a baseline for semantic search in Nepali and suggests practical approaches to enhancing sentence embeddings in low-resource language environments.

## 키워드

Nepali, Sentence, Mean reciprocal rank, Cosine similarity, Semantic similarity, Task (project management), Similarity (geometry)

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

