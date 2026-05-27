---
title: "HDR‐SA: A Hybrid Deep Learning and RoBERTa‐Based Framework for Sentiment and Aspect Analysis"
authors: ['Laxmi Pamulaparthy', 'C. H. Sumalakshmi']
year: 2026
venue: "IET Software"
tags: ['Sentiment Analysis and Opinion Mining', 'Digital Marketing and Social Media', 'Recommender Systems and Techniques']
source: raw/applied/applied_2026_HDRSA_A_Hybrid_Deep_Learn_9992594.md
---

# HDR‐SA: A Hybrid Deep Learning and RoBERTa‐Based Framework for Sentiment and Aspect Analysis
**제목(한글)**: HDR-SA: 감성 및 속성 분석을 위한 하이브리드 딥러닝 및 RoBERTa 기반 프레임워크

**저자**: Laxmi Pamulaparthy; C. H. Sumalakshmi
**출처**: IET Software, Vol.2026
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1049/sfw2/9992594

## 한국어 요약

**연구질문**: 속성 수준(Aspect-level)의 텍스트 감성 분석에서 특정 도메인의 수동 라벨링 데이터 부족 한계를 극복하고 분류 정확도를 극대화할 딥러닝 모델은 어떻게 구축하는가?

**방법론**:
- RoBERTa 트랜스포머 언어 모델과 CNN-BiLSTM 하이브리드 구조 결합
- VADER 규칙 모델을 사용하여 감성 스코어 보조 지표 생성 및 Word2Vec 임베딩 전처리
- 51만 5천 건의 대규모 호텔 리뷰 데이터셋(Hotel Reviews)을 활용해 판별 성능 벤치마크 검증

**주요 결과**:
- 제안된 HDR-SA 프레임워크가 95.75%의 높은 속성 분류 정확도를 보였으며 F1-score 0.96으로 기존 TD-LSTM 모델을 대폭 압도함
- 대규모 라벨링 리소스 없이도 여러 텍스트 문맥과 타겟 속성을 안정적으로 찾아내는 강력한 확장성(Scalability)을 증명함


## 초록 (원문)

The ability to comprehend complex viewpoints in text is critical for sentiment analysis (SA), particularly at the aspect level, yet existing models struggle with accurately identifying sentiment polarities and aspect‐specific expressions due to their reliance on large, manually annotated, domain‐specific datasets. To address these challenges, this paper introduces hybrid deep learning and RoBERTa‐based SA (HDR‐SA), a novel hybrid deep learning framework that integrates convolutional neural networks (CNNs), bidirectional long short‐term memory (BiLSTM) networks, and the RoBERTa transformer model to perform comprehensive sentiment and aspect analysis. The proposed model begins with rigorous data preprocessing and normalization, utilizes Valence Aware Dictionary and sEntiment Reasoner (VADER) for sentiment scoring, constructs embedding vectors via Word2Vec, and employs a CNN‐BiLSTM architecture enhanced by RoBERTa to capture both sequential and contextual embeddings for refined sentiment classification. The novelty of HDR‐SA lies in its hybrid integration of conventional natural language processing (NLP) techniques with deep learning and transformer‐based contextual understanding, enabling robust SA without the extensive need for domain‐specific annotated data. Evaluated on the large‐scale 515K Hotel Reviews dataset, HDR‐SA achieved an accuracy of 95.75%, a precision of 0.96, a recall of 0.97, and an F1‐score of 0.96, outperforming contemporary models such as target‐dependent LSTM (TD‐LSTM), ResNet‐SCSO, and CNN‐GA. These results demonstrate HDR‐SA’s effectiveness in aspect‐level SA and its scalability across diverse domains while reducing dependency on annotated resources.

## 키워드

Deep learning, Sentiment analysis, Scalability, Novelty, Convolutional neural network, Embedding, Preprocessor, Transformer

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

