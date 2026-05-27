---
title: "A Bi-GRU and BERT-Based Intelligent Audit System for News Moderation via NLP and Sentiment Analysis"
authors: ['Yuanjie Yuan']
year: 2025
venue: "Informatica"
tags: ['Sentiment Analysis and Opinion Mining', 'Misinformation and Its Impacts', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2025_A_BiGRU_and_BERTBased_Int_inf_v49i36_9274.md
---

# A Bi-GRU and BERT-Based Intelligent Audit System for News Moderation via NLP and Sentiment Analysis

**제목(한글)**: 자연어 처리 및 감성 분석을 통한 뉴스 검토를 위한 Bi-GRU 및 BERT 기반 지능형 감사 시스템

## 한국어 요약

**연구질문**: 정보 폭발 시대에 기존 수작업 뉴스 검토 메커니즘의 한계를 극복하고 뉴스 콘텐츠 허위 정보와 여론 위험을 효과적으로 탐지하는 지능형 자동 감사 시스템을 어떻게 구축할 수 있는가?

**방법론**:
- NLP 구성요소에는 BERT 사전학습 모델을 미세조정, 감성 분석 구성요소에는 LSTM-어텐션 메커니즘 모델을 사용하며 Bi-GRU와 통합하는 계층적 아키텍처 개발
- THUCNews 코퍼스로 뉴스 텍스트 분류, SST-2로 감성 분석 훈련
- mBERT와 XLM-R 등 다국어 사전학습 모델과 언어 어댑터를 통합해 영어·중국어·스페인어 등 다국어 검토 지원

**주요 결과**:
- 뉴스 감사 효율 약 40% 향상, 오류율 약 30% 감소
- 뉴스 분류 정확도 90% 이상, 감성 분석 F1-스코어 85% 이상 달성
- 다국어 데이터셋에서 평균 85% 정확도와 단일 언어 모델 대비 교차 언어 전이 30% 향상

**저자**: Yuanjie Yuan
**출처**: Informatica, Vol.49
**발행일**: 2025-12-20
**DOI**: https://doi.org/10.31449/inf.v49i36.9274

## 초록 (원문)

In the era of information explosion, the exponential growth and rapid update of news data pose significant challenges to traditional manual news dissemination review mechanisms. Existing methods struggle to balance content moderation comprehensiveness and accuracy. To address these issues, this study develops an intelligent audit system for news communication that integrates natural language processing (NLP) and sentiment analysis. Leveraging advanced NLP techniques like semantic analysis and keyword extraction, the system swiftly identifies core news information and potential risk points. Sentiment analysis algorithms are integrated to precise assess the emotional tone and social impact of news content, enabling intelligent screening and risk early warning. The system employs models such as BERT and Bi-GRU for NLP and sentiment analysis components, respectively. Experimental results demonstrate its effectiveness: news audit efficiency has increased by nearly 40%, and the error rate has decreased by about 30%. It can also effectively detect and filter false information and public opinion risks, enhancing news credibility and social value. Outperforming existing methods in accuracy and recall, the system features a hierarchical architecture with data collection, preprocessing, NLP and sentiment analysis, and audit decision-making layers. Data collection is achieved through web crawlers, and preprocessing includes deduplication, cleaning, word segmentation, and vectorization. The BERT pre-trained model is fine-tuned for NLP tasks, while sentiment analysis utilizes an LSTM-attention mechanism model, all implemented in a Python environment with the PyTorch framework. Using the THUCNews corpus for news text classification and SST-2 for sentiment analysis training, the model achieves over 90% news classification accuracy and an F1 score exceeding 85% for sentiment analysis. Additionally, the system incorporates multilingual capabilities by integrating multilingual pre-trained models such as mBERT and XLM-R, and introducing language adapters. It can audit news texts in English, Chinese, Spanish, and other languages, achieving an average accuracy of 85% on multilingual datasets and a 30% improvement in cross-lingual transfer compared to monolingual models, effectively supporting global news dissemination audits and handling multilingual mixed content.

## 키워드

Sentiment analysis, Credibility, Preprocessor, Audit, Social media, Filter (signal processing), Lexicon, Topic model

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

