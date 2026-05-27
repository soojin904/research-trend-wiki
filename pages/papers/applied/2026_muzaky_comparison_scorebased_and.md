---
title: "Comparison of Score-Based and Content-Based Automatic Sentiment Labeling Using a K-Nearest Neighbor Classifier"
authors: ['Rifky Khoerul Muzaky', 'Hanipah Diniyaturobiah']
year: 2026
venue: "Journal of Intelligent Systems Technology and Informatics"
tags: ['Sentiment Analysis and Opinion Mining', 'Text and Document Classification Technologies', 'Emotion and Mood Recognition']
source: raw/applied/applied_2026_Comparison_of_ScoreBased__jistics_v2i1_120.md
---

# Comparison of Score-Based and Content-Based Automatic Sentiment Labeling Using a K-Nearest Neighbor Classifier
**제목(한글)**: K-최근접 이웃 분류기를 활용한 평점 기반 및 텍스트 기반 자동 감성 레이블링 비교 연구

**저자**: Rifky Khoerul Muzaky; Hanipah Diniyaturobiah
**출처**: Journal of Intelligent Systems Technology and Informatics, Vol.2, pp.38-44
**발행일**: 2026-03-26
**DOI**: https://doi.org/10.64878/jistics.v2i1.120

## 한국어 요약

**연구질문**: 모바일 애플리케이션 리뷰 데이터 분류 시, 별점 평점(Star Ratings) 기반 레이블링과 텍스트 본문 분석 기반 레이블링 중 어느 쪽이 실제 감성을 더 정확하게 예측하며 불일치 원인은 무엇인가?

**방법론**:
- 리뷰 텍스트를 TF-IDF 벡터로 변환
- 별점 기반 자동 레이블과 본문 감성 기반 자동 레이블로 데이터셋을 각각 구축
- K-최근접 이웃(KNN) 알고리즘을 사용해 분류 모델을 구축하고 정확도, 정밀도, 재현율, F1-score 비교

**주요 결과**:
- 텍스트 본문 기반 분류 방법이 정확도 0.81을 달성하여 평점 기반 분류 방법 대비 월등히 신뢰도 높은 성능을 보임을 규명함
- 사용자가 남긴 수치 평점과 실제 작성한 텍스트에 나타난 주관적 감정선 간의 미스매치가 평점 기반 레이블링의 신뢰성을 저해하는 주요 원인임을 실증함


## 초록 (원문)

This study investigates the performance gap between two automatic sentiment labeling strategies one relying on star ratings and the other derived from textual content in classifying application reviews using the K-Nearest Neighbor (KNN) algorithm. Each review is converted into TF-IDF vectors, and the influence of both labeling approaches on the resulting classifier is examined. Performance is evaluated using accuracy, precision, recall, and F1-score to ensure a comprehensive assessment, with the content-based method achieving an accuracy of 0.81, indicating a more reliable outcome than the score-based variant. The score-driven approach shows weaker consistency, largely due to mismatches between numerical ratings and the sentiment conveyed in written text. Despite these findings, the study is limited by its focus on a single application domain and its reliance on a single classical baseline classifier, which may be sensitive to class imbalance. Future work is encouraged to incorporate more diverse datasets, adopt modern text representation techniques such as word embeddings or transformer-based encodings, and explore classification algorithms that better accommodate uneven class distributions.

## 키워드

Classifier (UML), Sentiment analysis, Representation (politics), Class (philosophy), Pattern recognition (psychology), Word (group theory)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

