---
title: "From Accuracy to Insight: Explainability in Review Rating Prediction with Transformers"
authors: ['Dhefaf T. Radain', 'Dimah Alahmadi', 'Arwa M. Wali']
year: 2026
venue: "International Journal of Advanced Computer Science and Applications"
tags: ['Explainable Artificial Intelligence (XAI)', 'Sentiment Analysis and Opinion Mining', 'Artificial Intelligence in Healthcare and Education']
source: raw/applied/applied_2026_From_Accuracy_to_Insight__ijacsa_2026_0170194.md
---

# From Accuracy to Insight: Explainability in Review Rating Prediction with Transformers
**제목(한글)**: 정확성에서 통찰로: 트랜스포머를 활용한 리뷰 평점 예측의 설명 가능성

**저자**: Dhefaf T. Radain; Dimah Alahmadi; Arwa M. Wali
**출처**: International Journal of Advanced Computer Science and Applications, Vol.17
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.14569/ijacsa.2026.0170194

## 한국어 요약

**연구질문**: 자연어 처리 도구가 미비하고 모호한 모바일 행정 서비스 앱의 '아랍어(Arabic)' 사용자 리뷰에서, 정확하고 인공지능 판정의 이유를 시각적으로 해명해 줄 설명 가능한 프레임워크는 무엇인가?

**방법론**:
- 영어 및 아랍어 모바일 행정 서비스 앱의 대규모 이용자 리뷰 코퍼스 수집
- ELECTRA 및 AraBERTv2 트랜스포머 분류 모델 학습 및 평점 예측 정확도 평가
- 설명 가능성 도구인 SHAP(Shapley Additive Explanation)과 LIME을 분류 결과에 접목해 판정 단어 가중치 시각화

**주요 결과**:
- 영어 리뷰에서 ELECTRA 모델이 96%, 아랍어 리뷰에서 AraBERTv2 모델이 95%의 높은 평점 예측 정확도를 나타냄을 규명함
- SHAP과 LIME 모델 간의 단어 기여도 정렬이 매우 높은 일치도를 보임으로써 모바일 행정 앱 개발사들이 AI의 예측 결과를 신뢰하고 실무에 반영할 수 있는 과학적 투명성을 입증함


## 초록 (원문)

Mobile application (app) reviews provide valuable information that facilitates understanding of users’ needs, leading to better design of developed products. They have abundant data that can be utilized by different models to explain the prediction results to stakeholders. This will lead mobile app developers to trust and rely on the models that are used to develop their apps and satisfy the users’ needs. To leverage this information, outstanding improvements in complex learning algorithms have led to the development of transformer-based models that are used for natural language processing (NLP) and to exploit rating predictions. However, such models are complex and lack explainability, especially for Arabic reviews. Most studies have applied explainability models for transformer-based models to the English language and various other languages but not the Arabic language. This study presents a rating prediction explain-ability (RPE) framework that combines transformer-based and explainability models for review rating predictions from mobile government (m-government) apps. The transformer-based models predict the ratings for reviews written in English or Arabic. Then, local explainability models, such as SHapley Additive exPlanation (SHAP) and local interpretable model-agnostic explanations (LIME), explain and visualize the results. In RPE, not only high prediction accuracy was achieved for both English and Arabic reviews, but the resulted predictions were also justified with consistency between the different explainability models. The transformer-based model ELECTRA yielded the highest accuracy and F1 score of 96% for the rating prediction of English reviews, whereas the transformer-based model AraBERTv2 had 95%accuracy and F1 score for the rating prediction of Arabic reviews. The results of both explainability models provided equivalent explanations and emphasized the same words that affected the predicted ratings.

## 키워드

Leverage (statistics), Arabic, Exploit, Transformer, Consistency (knowledge bases), Predictive modelling, Language model

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

