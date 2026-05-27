---
title: "Contextual Embedding Comparison for Out-of-vocabulary Handling in Indonesian POS Tagging"
authors: ['Muhammad Alfian', 'Umi Laili Yuhana', 'Daniel Siahaan', 'Harum Munazharoh', 'Eric Pardede']
year: 2025
venue: "Informatica"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Text Readability and Simplification']
source: raw/applied/applied_2025_Contextual_Embedding_Comp_inf_v49i22_11204.md
---

# Contextual Embedding Comparison for Out-of-vocabulary Handling in Indonesian POS Tagging

**제목(한글)**: 인도네시아어 품사 태깅의 미등록어(OOV) 처리를 위한 문맥 임베딩 비교

## 한국어 요약

**연구질문**: 정적 임베딩과 문맥 임베딩 중 어느 것이 인도네시아어 품사 태깅의 미등록어(OOV) 처리에 더 효과적인가?

**방법론**:
- 정적 임베딩(Word2Vec, GloVe, FastText)과 문맥 임베딩(ELMo, BERT, Flair) 비교
- 인도네시아어 코퍼스 30,960 단어, k-겹 교차검증 적용
- OOV 및 등록어(IV) 시나리오 병행 평가

**주요 결과**:
- 문맥 임베딩이 정적 임베딩보다 일관되게 우수한 성능
- Flair가 가장 높은 정확도(95.65%), 제안 모델은 기준선 대비 25.15% 향상된 88.12% 달성

**저자**: Muhammad Alfian; Umi Laili Yuhana; Daniel Siahaan; Harum Munazharoh; Eric Pardede
**출처**: Informatica, Vol.49
**발행일**: 2025-12-18
**DOI**: https://doi.org/10.31449/inf.v49i22.11204

## 초록 (원문)

Out-of-vocabulary (OOV) problems remain a significant challenge in part-of-speech (POS) tagging. These problems affect not only tagging performance, but also downstream tasks, particularly in educational case studies. This issue is related to the limited availability of datasets for low-resource languages (LRLs), the absence of representative features, and the complexity of grammatical variation. Current approaches perform well in recognizing patterned OOV words, but often fail with unpatterned OOV words, such as proper nouns and polysemous words. To address this issue, this study employs contextual embeddings to represent OOV words, improving model recognition. Two types of embeddings are compared: static embeddings (Word2Vec, GloVe, and FastText) and contextual embeddings (ELMo, BERT, and Flair). These embeddings provide appropriate representations for OOV words. We evaluate models using accuracy and the macro F1 score on a curated Indonesian corpus of 30,960 words. The model was evaluated using the k-fold cross-validation method with both OOV and in-vocabulary (IV) word scenarios. The results of the experiment show that models with contextual embeddings outperform those with static embeddings. Flair achieved the highest level of accuracy (95.65%), while BERT and ELMo achieved similar levels of 92.73% and 91.61% respectively. Our proposed model was effective in handling OOV cases, achieving an accuracy of 88.12%, which is a 25.15% improvement over the baseline model. However, it still struggles with redundant words and capitalized letters. Future research should explore integrating form-based and contextual information to improve performance.

## 키워드

Embedding, Word (group theory), Word embedding, Training set, Baseline (sea), Feature (linguistics), Macro

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

