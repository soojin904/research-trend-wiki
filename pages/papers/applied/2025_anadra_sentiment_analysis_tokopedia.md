---
title: "Sentiment Analysis of Tokopedia Customer Reviews Using BiLSTM and IndoBERT with Comparative Analysis of Preprocessing and Labeling Methods"
authors: ['Rahmi Anadra', 'Hari Wijayanto', 'Kusman Sadik']
year: 2025
venue: "International Journal of Advances in Data and Information Systems"
tags: ['Sentiment Analysis and Opinion Mining', 'Emotion and Mood Recognition', 'Edcuational Technology Systems']
source: raw/applied/applied_2025_Sentiment_Analysis_of_Tok_ijadis_v6i3_1458.md
---

# Sentiment Analysis of Tokopedia Customer Reviews Using BiLSTM and IndoBERT with Comparative Analysis of Preprocessing and Labeling Methods

**제목(한글)**: BiLSTM과 IndoBERT를 이용한 Tokopedia 고객 리뷰 감성 분석: 전처리 및 레이블링 방법 비교

## 한국어 요약

**연구질문**: 인도네시아어 감성 분석에서 전처리 방식·레이블링 전략·클래스 불균형 처리가 BiLSTM과 IndoBERT의 성능에 어떤 영향을 미치는가?

**방법론**:
- Tokopedia 사용자 리뷰 수동·자동 레이블링 후 3가지 전처리 방식 적용
- 20회 계층적 5-겹 교차검증, 클래스 가중치·포컬 손실로 불균형 처리
- 균형 정확도·F1-score 평가

**주요 결과**:
- IndoBERT: 균형 정확도 최대 0.85, F1 최대 0.83으로 최고 성능
- BiLSTM: 균형 정확도 최대 0.78, 에포크당 1~2.5분으로 학습 효율 우수
- 수동 레이블링이 문맥 뉘앙스 포착에서 우수하나 GPT 기반 레이블링도 높은 일치도 보임

**저자**: Rahmi Anadra; Hari Wijayanto; Kusman Sadik
**출처**: International Journal of Advances in Data and Information Systems, Vol.6, pp.773-788
**발행일**: 2025-12-01
**DOI**: https://doi.org/10.59395/ijadis.v6i3.1458

## 초록 (원문)

This study addresses key challenges in Indonesian sentiment analysis related to preprocessing, labeling strategies, and class imbalance. It compares the performance of BiLSTM and IndoBERT using user reviews collected from Tokopedia. The dataset was manually and automatically labeled, then processed under three preprocessing schemes. Both models were trained with tuned hyperparameters and imbalance-handling techniques and evaluated through twenty rounds of stratified five-fold cross-validation. Performance was assessed using balanced accuracy and F1-score. IndoBERT achieved the highest results, with balanced accuracy up to 0.85 and F1-scores up to 0.83, while BiLSTM reached balanced accuracy up to 0.78 and F1-scores up to 0.76. Applying class weight and focal loss improved model performance by approximately 2% to 11% over the baseline. BiLSTM demonstrated greater training efficiency, requiring only 1 to 2.5 minutes per epoch, compared with IndoBERT’s 2.6 to 3.6 minutes. Although manual labeling remained superior in capturing contextual nuance and emotional cues, GPT-based labeling showed strong agreement with the human annotations. A four-way ANOVA revealed that all main factors and several interactions significantly influenced classification outcomes. Overall, BiLSTM provides faster training efficiency, whereas IndoBERT delivers higher predictive accuracy.

## 키워드

Preprocessor, Hyperparameter, Data pre-processing, Training set, Class (philosophy), Sentiment analysis

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

