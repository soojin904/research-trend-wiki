---
title: "Geospatial Sentiment Analysis of Negative Comments on the 2024 Election Using the Robustly Optimized BERT Approach (RoBERTa)Geospatial Sentiment Analysis of Negative Comments on the 2024 Election Using the Robustly Optimized BERT Approach (RoBERTa)Geospat"
authors: ['Md. Haidar Ali', 'Yuliant Sibaroni']
year: 2025
venue: "International Journal on Information and Communication Technology (IJoICT)"
tags: ['Hate Speech and Cyberbullying Detection', 'Sentiment Analysis and Opinion Mining', 'Data Mining and Machine Learning Applications']
source: raw/applied/applied_2025_Geospatial_Sentiment_Anal_ijoict_v11i2_9575.md
---

# Geospatial Sentiment Analysis of Negative Comments on the 2024 Election Using the Robustly Optimized BERT Approach (RoBERTa)Geospatial Sentiment Analysis of Negative Comments on the 2024 Election Using the Robustly Optimized BERT Approach (RoBERTa)Geospat

**제목(한글)**: RoBERTa를 활용한 2024년 선거 부정 댓글의 지리공간 감성 분석

## 한국어 요약

**연구질문**: RoBERTa 모델로 2024년 선거 관련 혐오발언을 분류하고, 이를 지리공간적으로 시각화하면 어떤 분포 패턴이 나타나는가?

**방법론**:
- 소셜미디어 댓글 11,903건, 10-겹 교차검증 적용 RoBERTa 다중 분류
- 지오코딩 및 Folium 히트맵 시각화

**주요 결과**:
- 평균 정확도 91.54%, 최종 모델 94.29%
- 데이터의 75%가 인도네시아 발신, 자바섬에 혐오발언 집중
- 인도네시아 내외 혐오발언 비율 유사(45.6% vs 44.3%), HS_Strong 카테고리가 96.4%로 우세

**저자**: Md. Haidar Ali; Yuliant Sibaroni
**출처**: International Journal on Information and Communication Technology (IJoICT), Vol.11, pp.150-158
**발행일**: 2025-12-03
**DOI**: https://doi.org/10.21108/ijoict.v11i2.9575

## 초록 (원문)

This study develops a geospatial sentiment analysis system to detect and map hate speech related to the 2024 Election using the Robustly Optimized BERT Approach (RoBERTa). The dataset consists of 11,903 social media comments that have undergone comprehensive preprocessing, including text normalization, stopword removal, and stemming. The RoBERTa model was implemented using 10-fold cross-validation for multi-class classification (HS_Weak, HS_Strong, Not_Abusive) and achieved an average accuracy of 91.54% (±1.08%), with a final model accuracy of 94.29%. Geospatial analysis using geocoding and Folium visualization revealed that 75% of the data originated from Indonesia, with the highest concentration in the Jakarta area. The distribution of hate speech showed consistent patterns between Indonesia (45.6% hate speech) and outside Indonesia (44.3% hate speech), with the HS_Strong category dominating at 96.4%. Heatmap analysis identified hate speech hotspots on the island of Java and a global distribution across various continents. The findings confirm the effectiveness of RoBERTa for sentiment analysis in the Indonesian language and provide valuable insights into the geographic patterns of hate speech in the context of digital politics, which can be used to develop mitigation strategies and real-time monitoring systems.

## 키워드

Geocoding, Geospatial analysis, Sentiment analysis, Context (archaeology), Social media

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

