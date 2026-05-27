---
title: "SUPPORT VECTOR MACHINE TO CLASSIFY SENTIMENT REVIEWS ON GOOGLE PLAY STORE"
authors: ['Agus Nursikuwagus', 'Suherman', 'Heri Purwanto', 'Tono Hartono']
year: 2026
venue: "JITK (Jurnal Ilmu Pengetahuan dan Teknologi Komputer)"
tags: ['Sentiment Analysis and Opinion Mining', 'Recommender Systems and Techniques', 'Digital Marketing and Social Media']
source: raw/applied/applied_2026_SUPPORT_VECTOR_MACHINE_TO_jitk_v11i3_7282.md
---

# SUPPORT VECTOR MACHINE TO CLASSIFY SENTIMENT REVIEWS ON GOOGLE PLAY STORE
**제목(한글)**: 구글 플레이 스토어 앱 리뷰 감성 분류를 위한 서포트 벡터 머신 적용 연구

**저자**: Agus Nursikuwagus; Suherman; Heri Purwanto; Tono Hartono
**출처**: JITK (Jurnal Ilmu Pengetahuan dan Teknologi Komputer), Vol.11, pp.724-732
**발행일**: 2026-02-10
**DOI**: https://doi.org/10.33480/jitk.v11i3.7282

## 한국어 요약

**연구질문**: 앱 스토어 평점과 본문 글의 감성이 불일치하는 평점-본문 괴리(Rating-content discrepancy) 현상을 해결하기 위해, 리뷰 텍스트의 실제 감성을 정확히 예측하는 최적 분류 알고리즘은 무엇인가?

**방법론**:
- 데이터 마이닝 표준 프로세스인 CRISP-DM 프레임워크 준수
- 구글 플레이 스토어 리뷰 600건 데이터셋 구축
- 서포트 벡터 머신(SVM)과 K-최근접 이웃(KNN) 분류 모델 학습 및 정확도 비교 평가
- Streamlit을 연동하여 실시간 감성 분류 대시보드 웹 인터페이스 구현

**주요 결과**:
- SVM 모델이 정확도 0.84를 기록하여 KNN 모델(0.48) 대비 압도적인 분류 정확도를 달성함
- 텍스트와 같은 고차원 희소 데이터 분류에서 최적 결정 초평면(hyperplane)을 형성하는 SVM의 강력한 텍스트 마이닝 적합성을 입증함


## 초록 (원문)

This research addresses the "rating-content discrepancy" on the Google Play Store, where numerical star ratings often conflict with the actual sentiment of textual reviews. Utilizing the CRISP-DM framework, the study evaluates the effectiveness of machine learning in resolving these inconsistencies by classifying Instagram user reviews into positive and negative categories. Two primary algorithms were compared using a dataset of 600 reviews. The Support Vector Machine (SVM) model demonstrated high efficacy with an accuracy of 0.84. In contrast, the K-Nearest Neighbors (KNN) model performed poorly, achieving an accuracy of only 0.48. This significant performance gap highlights SVM's superior ability to handle high-dimensional text data through optimal hyperplane separation. The research further integrated the Streamlit library to create an interactive web interface for real-time sentiment prediction and result visualization. Ultimately, this study confirms that a structured CRISP-DM approach combined with SVM provides a robust solution for automated opinion mining, offering a reliable methodology for future data science applications in social media analysis

## 키워드

Support vector machine, Sentiment analysis, Social media, Hyperplane, Interface (matter), Web application

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

