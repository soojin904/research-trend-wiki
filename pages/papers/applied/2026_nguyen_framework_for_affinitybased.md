---
title: "A framework for affinity-based personalized review recommendation"
authors: ['Duy Tan Nguyen', 'Warut Khern-am-nuai', 'Yossiri Adulyasak', 'Jean‐François Cordeau']
year: 2026
venue: "Electronic Commerce Research"
tags: ['Digital Marketing and Social Media', 'Sentiment Analysis and Opinion Mining', 'Spam and Phishing Detection']
source: raw/applied/applied_2026_A_framework_for_affinityb_s10660_026_10143_2.md
---

# A framework for affinity-based personalized review recommendation
**제목(한글)**: 친밀도 기반 개인화된 리뷰 추천을 위한 프레임워크

**저자**: Duy Tan Nguyen; Warut Khern-am-nuai; Yossiri Adulyasak; Jean‐François Cordeau
**출처**: Electronic Commerce Research, Vol.None
**발행일**: 2026-05-09
**DOI**: https://doi.org/10.1007/s10660-026-10143-2

## 한국어 요약

**연구질문**: 정보 과부하 상태의 리뷰 플랫폼 환경에서, 군중 평점이나 단순 인기 순위 추천 방식의 한계를 극복하고 개별 사용자 친밀도를 반영한 리뷰를 추천해 플랫폼 체류 시간을 늘릴 방안은 무엇인가?

**방법론**:
- 아시아 대형 맛집 리뷰 플랫폼의 대규모 로그 데이터를 수집
- 사용자와 작성자 간 유사성, 리뷰 반응 성향 등을 포함한 개념 모델 및 반사실적(counterfactual) 시뮬레이션 기법 설계
- 리뷰별 상호작용 확률을 예측하는 머신러닝 예측 알고리즘 구축

**주요 결과**:
- 집단주의 성향이 짙은 아시아 문화권 플랫폼 환경에서는 '작성자-사용자 간 인구통계학적/성향적 유사성'이 친밀도 형성에 가장 강력한 요인임을 규명함
- 반사실적 분석을 통해 친밀도 기반 추천 랭킹을 적용했을 때 플랫폼에 대한 사용자 인게이지먼트와 총 체류 시간이 유의미하게 늘어남을 실증함


## 초록 (원문)

Abstract Online review platforms have proliferated thanks to technological advances and consumers’ increased dependence on each other’s opinions for purchase decisions. However, users typically face an enormous number of online reviews and suffer from information overload. Unlike previous research that relies mainly on popularity, crowd-based evaluation, or filtering methods, we propose a framework for personalized review recommendation based on user-review affinity. Indeed, this study seeks to identify and recommend reviews to each user according to the probability that he/she will like (hit the helpfulness vote/like button), comment on, or re-read those reviews, whereby user login time increases, which in turn correlates positively with user affinity toward the platform. We hypothesize a conceptual model, conduct predictive analytics, and perform counterfactual simulations on the log data of a large restaurant review platform in Asia and find that reviewer-user similarity is among the most significant explanatory factors, which is in line with the collectivist culture of the country where platform operates. Built on the results of the explanatory analysis, machine learning-based predictive models are then applied to predict the likelihood that each user will interact with each review for each business. Our counterfactual analysis demonstrates the potential of the resultant affinity-based ranking to increase user engagement with the platform.

## 키워드

Counterfactual thinking, Helpfulness, Collaborative filtering, Ranking (information retrieval), Recommender system, Rank (graph theory), Similarity (geometry), Conceptual model

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

