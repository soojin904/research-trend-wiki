---
title: "Analyzing Influential Factors in Review-Based Restaurant Recommender Systems: The Role of Review Length, Aspect, and Emotion"
authors: ['Jihyun Yoon', 'Haebin Lim', 'Soohyun Woo', 'Byunghyun Lee', 'Jaekyeong Kim']
year: 2026
venue: "Electronics"
tags: ['Recommender Systems and Techniques', 'Sentiment Analysis and Opinion Mining', 'Digital Marketing and Social Media']
source: raw/applied/applied_2026_Analyzing_Influential_Fac_electronics15091821.md
---

# Analyzing Influential Factors in Review-Based Restaurant Recommender Systems: The Role of Review Length, Aspect, and Emotion
**제목(한글)**: 리뷰 기반 맛집 추천 시스템의 영향 요인 분석: 리뷰 길이, 속성, 감정의 역할

**저자**: Jihyun Yoon; Haebin Lim; Soohyun Woo; Byunghyun Lee; Jaekyeong Kim
**출처**: Electronics, Vol.15, pp.1821-1821
**발행일**: 2026-04-24
**DOI**: https://doi.org/10.3390/electronics15091821

## 한국어 요약

**연구질문**: 맛집 추천 시스템에서 텍스트의 다양한 요소(리뷰 길이, 세부 속성, 감정 유형)가 사용자의 최종 별점 예측(rating prediction) 성능에 어떤 영향을 미치는가?

**방법론**:
- 텍스트 정보를 사전 훈련된 BERT로 임베딩하고 맥락으로 주입하는 비구조적 맥락 인지 모델(UCAM) 적용
- 리뷰 길이를 4분위로 나누어 성능 기여도를 비교하고 맛집 리뷰 속성을 음식, 서비스, 가격, 분위기, 위치로 분류
- 플루칙(Plutchik) 감정 프레임워크를 기반으로 텍스트 감정(기쁨, 신뢰, 기대, 슬픔 등)별 기여도 정량 분석

**주요 결과**:
- 의외로 짧은 리뷰 데이터를 제거하는 경우 전체 평점 예측 성능이 급격히 무너짐을 확인하여 단문 리뷰의 유용성 입증
- 다섯 가지 속성 중 '서비스'와 '음식' 속성이 예측 모델 정확도 개선에 가장 크게 기여하였으며 '위치'는 영향력이 거의 없음
- 기쁨, 신뢰, 기대를 유발하는 긍정 감정을 배제했을 때 성능이 가장 크게 하락한 반면, 슬픔 등 부정 감정 제거는 오히려 성능이 미세하게 향상됨을 실증


## 초록 (원문)

Review text in recommender systems provides rich insights into user preferences and experiences that cannot be fully captured by numerical ratings alone. While recent studies have increasingly leveraged review text to enhance recommendation accuracy, most have primarily focused on improving model performance, with limited attention to quantitatively examining how specific textual elements influence rating prediction. To address this gap, this study empirically investigates the impact of review text characteristics on prediction performance in review-based recommender systems. Specifically, we employ the Unstructured Context-Aware Model (UCAM), where contextual information is replaced with review text embedded using a pre-trained BERT model. Three key textual factors are examined: review length, aspect, and emotion type. Review length is divided into quartiles, and results show that removing shorter reviews significantly degrades performance, indicating their critical role. For analysis, reviews are categorized into food, service, price, atmosphere, and location, with service and food contributing most to performance improvements, while location shows relatively low influence. Emotion types are classified based on Plutchik’s framework, revealing that removing joy, trust, and anticipation reduces performance, whereas excluding sadness slightly improves it. Overall, this study highlights the differential importance of textual features and demonstrates their potential for enhancing recommender system design.

## 키워드

Sadness, Recommender system, Anticipation (artificial intelligence), Key (lock), Sentiment analysis, Service (business)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

