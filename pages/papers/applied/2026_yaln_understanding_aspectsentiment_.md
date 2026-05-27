---
title: "Understanding Aspect-Sentiment Drivers of Overall Ratings in Second Hand Marketplace Apps through Text Analytics and Regression Analysis"
authors: ['Vicdan Yalçın', 'Ahmet Cumhur Öztürk', 'Mustafa Çetin']
year: 2026
venue: "DÜMF Mühendislik Dergisi"
tags: ['Digital Marketing and Social Media', 'Technology Adoption and User Behaviour', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Understanding_AspectSenti_dumf_1790105.md
---

# Understanding Aspect-Sentiment Drivers of Overall Ratings in Second Hand Marketplace Apps through Text Analytics and Regression Analysis
**제목(한글)**: 텍스트 분석 및 회귀 분석을 통한 중고 거래 앱 평점의 속성-감성 유발 요인 이해

**저자**: Vicdan Yalçın; Ahmet Cumhur Öztürk; Mustafa Çetin
**출처**: DÜMF Mühendislik Dergisi, Vol.17
**발행일**: 2026-03-24
**DOI**: https://doi.org/10.24012/dumf.1790105

## 한국어 요약

**연구질문**: 터키의 주요 중고 거래 모바일 앱 사용자 리뷰 데이터에서 특정 속성-감성(aspect-sentiment) 패턴이 전체 앱 평점(star rating)에 미치는 영향은 무엇인가?

**방법론**:
- 터키의 3대 중고 거래 앱(Letgo, Dolap, Gardrops) 리뷰 데이터 수집 및 다단계 NLP 파이프라인 적용
- SBERT 임베딩 및 K-Means 클러스터링을 통한 13개 속성(aspect) 카테고리 도출
- 터키어 ELECTRA 모델 기반 감성 분류 및 리지 회귀(Ridge regression)를 활용한 속성-감성 쌍의 평점 기여도 정량화

**주요 결과**:
- 환불, 배송비 불만, 사기 피해 관련 부정적 속성이 평점을 유의미하게 깎아내린 반면, 사용성, 거래 만족도, 고객 지원의 긍정 요인은 높은 평점을 유도함을 확인
- 높은 평점을 얻은 Dolap(4.4) 및 Gardrops(4.2)와 신뢰/공정성 이슈가 반복된 Letgo(2.7)의 특징적 리뷰 차이를 규명하고 중고 C2C 시장 활성화를 위한 개선 전략 제시


## 초록 (원문)

User-generated reviews and star ratings strongly influence customer trust, download decisions, and platform reputation in mobile app marketplaces. This study analyzes reviews from three Turkish secondhand marketplace applications (Letgo, Dolap, Gardrops) on Google Play to uncover how specific aspect–sentiment patterns affect overall ratings.A multi-stage natural language processing (NLP) pipeline was applied. Review sentences were embedded with multilingual SBERT and clustered using KMeans, resulting in 13 higher level aspect categories. Sentiment was classified using a domain specific Turkish ELECTRA model validated on 1,000 manually annotated sentences. Ridge regression was then employed to quantify the contribution of aspect–sentiment pairs to star ratings. The analysis showed that negative experiences related to returns, shipping costs and fraudulent practices consistently decreased ratings, while positive mentions of usability, transaction satisfaction and customer support produced stronger rating improvements. Comparative findings revealed that higher-rated apps (Dolap: 4.4, Gardrops: 4.2) accumulated more positive experiences, whereas Letgo (2.7) exhibited recurring trust and fairness issues. These results highlight which service aspects most strongly shape customer evaluations. By linking aspect-level sentiment to rating outcomes, the study provides platform managers with actionable insights for improving satisfaction and strengthening competitiveness in secondhand C2C marketplaces.

## 키워드

Turkish, Sentiment analysis, Pipeline (software), Ordinal regression, Reputation, Customer satisfaction, Regression analysis, Download

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

