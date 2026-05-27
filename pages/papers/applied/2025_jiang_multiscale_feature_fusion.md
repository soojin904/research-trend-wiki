---
title: "A Multi-Scale Feature Fusion Linear Attention Model for Movie Review Sentiment Analysis"
authors: ['Zi Jiang', 'Chengjun Xu']
year: 2025
venue: "Big Data and Cognitive Computing"
tags: ['Sentiment Analysis and Opinion Mining', 'Emotion and Mood Recognition', 'Recommender Systems and Techniques']
source: raw/applied/applied_2025_A_MultiScale_Feature_Fusi_bdcc9120325.md
---

# A Multi-Scale Feature Fusion Linear Attention Model for Movie Review Sentiment Analysis

**제목(한글)**: 영화 리뷰 감성 분석을 위한 다중 스케일 특성 융합 선형 어텐션 모델

## 한국어 요약

**연구질문**: 지역 세밀 특성과 전역 문맥 특성을 균형 있게 통합하는 다중 스케일 특성 융합 선형 어텐션 모델(MSFFLA)이 영화 리뷰 감성 분류에서 기존 BERT 기반 모델보다 더 효율적이고 정확한 성능을 달성할 수 있는가?

**방법론**:
- BERT 인코더 모듈(기본 의미 특성 추출) + 병렬 다중 스케일 특성 추출(PMFE, 팽창 합성곱) + 전역 다중 스케일 선형 특성 추출(MGLFE, MSLA 어텐션) 세 모듈 구성
- SST-2, Amazon Reviews, MR 세 가지 공개 데이터셋으로 실험

**주요 결과**:
- BERT-CondConv 대비 SST-2에서 정확도 1.8%, F1-score 0.4% 향상; Amazon Reviews에서 각각 1.5%, 0.3% 향상
- 선형 계산 복잡도로 전역 문맥 의존성을 효율적으로 모델링하여 경량 솔루션을 제공함
- 영화 추천 시스템의 감성 분류에 실용적 응용 가능성이 높음

**저자**: Zi Jiang; Chengjun Xu
**출처**: Big Data and Cognitive Computing, Vol.9, pp.325-325
**발행일**: 2025-12-18
**DOI**: https://doi.org/10.3390/bdcc9120325

## 초록 (원문)

Sentiment classification is a key technique for analyzing the emotional tendency of user reviews and is of great significance to movie recommendation systems. However, existing methods often face challenges in practical applications due to complex model structures, low computational efficiency, or difficulties in balancing local details with global contextual features. To address these issues, this paper proposes a Multi-Scale Feature Fusion Linear Attention model (MSFFLA). The model consists of three core modules: the BERT Encoder module for extracting basic semantic features; the Parallel Multi-scale Feature Extraction module (PMFE), which employs multi-branch dilated convolutions to accurately capture local fine-grained features; and the Global Multi-scale Linear Feature Extraction module (MGLFE), which introduces a Multi-Scale Linear Attention mechanism (MSLA) to efficiently model global contextual dependencies with approximately linear computational complexity. Extensive experiments were conducted on three public datasets: SST-2, Amazon Reviews, and MR. The results show that compared to the state-of-the-art BERT-CondConv model, our model achieves improvements in accuracy and F1-Score by 1.8% and 0.4%, respectively, on the SST-2 dataset, and by 1.5% and 0.3% on the Amazon Reviews dataset. This study not only validates the effectiveness of the proposed model but also provides an efficient and lightweight solution for sentiment classification tasks in movie recommendation systems, demonstrating promising practical application prospects.

## 키워드

Sentiment analysis, Feature (linguistics), Feature extraction, Encoder, Key (lock), Semantic feature, Face (sociological concept), Linear model

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

