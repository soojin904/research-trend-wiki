---
title: "Classification of Public Sentiment towards the Performance of the Ministry of Communication and Digital regarding Online Gambling"
authors: ['Ika Rahma Alia', 'Favorisen Rosyking Lumbanraja', 'Aristoteles Aristoteles', 'Rico Andrian']
year: 2025
venue: "Jurnal Pepadun"
tags: ['Sentiment Analysis and Opinion Mining', 'Multimedia Learning Systems', 'Information Retrieval and Data Mining']
source: raw/applied/applied_2025_Classification_of_Public__pepadun_v6i3_295.md
---

# Classification of Public Sentiment towards the Performance of the Ministry of Communication and Digital regarding Online Gambling

**제목(한글)**: 온라인 도박 관련 인도네시아 디지털통신부 성과에 대한 대중 감성 분류

## 한국어 요약

**연구질문**: 인스타그램 댓글 데이터를 활용해 온라인 도박 이슈에 대한 정부 성과 관련 대중 감성을 자동으로 분류할 수 있는가?

**방법론**:
- Kemkomdigi 공식 인스타그램 댓글 724건 수집 및 3인 주석자 투표 레이블링
- TF-IDF 특성 추출, Random Oversampling으로 데이터 불균형 처리
- 랜덤 포레스트·XGBoost 알고리즘 비교, 10-겹 교차검증 및 GridSearchCV 하이퍼파라미터 튜닝

**주요 결과**:
- 튜닝된 랜덤 포레스트가 정확도 0.7082로 최고 성능
- 머신러닝이 소셜미디어 정책 이슈 관련 감성 자동 분류에 효과적임을 확인

**저자**: Ika Rahma Alia; Favorisen Rosyking Lumbanraja; Aristoteles Aristoteles; Rico Andrian
**출처**: Jurnal Pepadun, Vol.6, pp.264-275
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.23960/pepadun.v6i3.295

## 초록 (원문)

Online gambling is a social issue currently in the spotlight in Indonesia. Although the government, particularly the Ministry of Communication and Digital (Kemkomdigi), has taken various measures, such as blocking websites and conducting digital literacy campaigns, online gambling remains rampant and has sparked various public reactions. Social media, particularly Instagram, has become a public space where people express their opinions and sentiments regarding government performance. This study aims to classify public sentiment based on comments directed at the official Kemkomdigi Instagram account regarding the issue of online gambling. This study uses two machine learning algorithms, Random Forest and XGBoost, to compare the effectiveness of the models in classifying positive and negative sentiment. A total of 724 comments were collected and manually labeled by three annotators using a voting method. Preprocessing included cleaning, case folding, tokenization, normalization, stopword removal, and stemming. Feature representation was performed using the TF-IDF method. The data was split with a 70:30 ratio and balanced using Random Oversampling. Model training used 10-fold cross-validation and hyperparameter tuning through GridSearchCV. The evaluation results showed that the tuned Random Forest performed the best, with an accuracy of 0.7082. These findings demonstrate that machine learning approaches, particularly Random Forest, are effective in automatically identifying public sentiment toward emerging public policy issues on social media.

## 키워드

Random forest, Voting, Government (linguistics), Preprocessor, Sentiment analysis, Digital literacy, Social media, Christian ministry

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

