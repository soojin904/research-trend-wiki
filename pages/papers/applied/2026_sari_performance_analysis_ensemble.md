---
title: "Performance Analysis of Ensemble Learning in Sentiment Classification of BRImo App Reviews"
authors: ['Novi Puspita Sari']
year: 2026
venue: "Information Technology and Systems"
tags: ['Sentiment Analysis and Opinion Mining', 'Edcuational Technology Systems', 'Data Mining and Machine Learning Applications']
source: raw/applied/applied_2026_Performance_Analysis_of_E_its_v3i1_500.md
---

# Performance Analysis of Ensemble Learning in Sentiment Classification of BRImo App Reviews
**제목(한글)**: BRImo 앱 리뷰의 감성 분류에서 앙상블 학습의 성능 분석

**저자**: Novi Puspita Sari
**출처**: Information Technology and Systems, Vol.3, pp.14-26
**발행일**: 2026-01-15
**DOI**: https://doi.org/10.58777/its.v3i1.500

## 한국어 요약

**연구질문**: 인도네시아 모바일 뱅킹 앱인 BRImo의 사용자 리뷰 텍스트 감성을 분류하기 위해, 단독 모델(SVM, 의사결정나무)과 이들을 조합한 앙상블 모델의 성능은 어떠한가?

**방법론**:
- Google Play Store에서 스크랩한 8,002개의 BRImo 리뷰 데이터셋 구축 및 전처리(정제, 토큰화, 어간 추출 등)
- 어휘집(Lexicon) 기반 감성 레이블링 및 TF-IDF 피처 추출 수행
- SVM과 의사결정나무(Decision Tree) 단일 모델 및 이들의 앙상블 조합(SVM + Decision Tree)에 대해 8:2 분할 검증

**주요 결과**:
- SVM 단일 모델이 고차원 텍스트 분별력 덕에 92.63%로 최고 정확도를 기록하였으며, 앙상블 모델은 89.38%로 약간 낮았으나 안정적 예측력(변동 감소)을 보임
- 의사결정나무는 텍스트 복잡도 처리 한계로 가장 낮은 86.45% 정확도를 보여, SVM 기반 조합이 인도네시아 모바일 뱅킹 리뷰 분석에 일관된 기여를 할 수 있음을 실증함


## 초록 (원문)

The use of mobile banking services in Indonesia continues to increase along with the development of information technology, including the BRImo application owned by Bank Rakyat Indonesia (BRI), which has reached more than 50 million downloads and one million reviews on the Google Play Store. These reviews serve as an important data source for understanding user perceptions and experiences. This study analyzes the performance of the Ensemble Learning method for sentiment classification of BRImo reviews by combining Support Vector Machine (SVM) and Decision Tree. The data was obtained through web scraping techniques, then processed through preprocessing stages including cleaning, case folding, normalization, tokenization, stopword removal, and stemming. Next, a lexicon approach was used for sentiment labeling, while TF-IDF was used for feature extraction. The dataset consists of 8,002 reviews, split with a ratio of 80:20. The study results show that SVM achieved the highest accuracy at 92.63%, due to its strong ability to optimally separate high-dimensional text data. The Ensemble model combining SVM and Decision Tree achieved an accuracy of 89.38%, slightly lower than SVM, but still providing stable predictions. This is because the Ensemble leverages the strength of two algorithms, making it capable of reducing result variance. Meanwhile, the Decision Tree recorded the lowest accuracy at 86.45%, indicating its limitations in handling the complexity of text data. Thus, although the Ensemble does not surpass SVM, the model combination still produces a more balanced and consistent performance. This study has limitations in terms of data coverage and a lexicon approach that is sensitive to context. The findings have implications for the development of the BRImo application based on user perceptions. The novelty of the research lies in the application of the SVM–Decision Tree Ensemble in sentiment analysis of mobile banking applications in Indonesia.

## 키워드

Lexicon, Decision tree, Support vector machine, Ensemble learning, Preprocessor, Sentiment analysis, Feature (linguistics), Data pre-processing

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

