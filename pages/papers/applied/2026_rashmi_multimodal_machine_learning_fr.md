---
title: "Multimodal machine learning framework for fake review detection"
authors: ['C Rashmi', 'Shobha T.', 'Dhanushree C. S.', 'Gayatri S. Santi', 'Jeevita S. Devadig', 'Harshitha L. V.']
year: 2026
venue: "International Journal of Power Electronics and Drive Systems/International Journal of Electrical and Computer Engineering"
tags: ['Spam and Phishing Detection', 'Misinformation and Its Impacts', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Multimodal_machine_learni_ijece_v16i2_pp991_1001.md
---

# Multimodal machine learning framework for fake review detection
**제목(한글)**: 가짜 리뷰 탐지를 위한 다중 모드 머신러닝 프레임워크

**저자**: C Rashmi; Shobha T.; Dhanushree C. S.; Gayatri S. Santi; Jeevita S. Devadig; Harshitha L. V.
**출처**: International Journal of Power Electronics and Drive Systems/International Journal of Electrical and Computer Engineering, Vol.16, pp.991-991
**발행일**: 2026-03-17
**DOI**: https://doi.org/10.11591/ijece.v16i2.pp991-1001

## 한국어 요약

**연구질문**: 전자상거래 및 소비자 리뷰 포털의 신뢰성을 떨어뜨리는 악성 가짜 리뷰를 잡기 위해, 텍스트와 리뷰어 행동, 시간, 네트워크 정보 변수를 융합하는 다중 모드(Multimodal) 탐지 정확도는 어떠한가?

**방법론**:
- 텍스트 감성 점수와 시간별 리뷰 빈도, 리뷰어 간 공동 리뷰 네트워크 엣지 데이터 수집
- 데이터 클래스 불균형 해결을 위해 SMOTE 오버샘플링 적용
- 의사결정 나무, XGBoost, 스태킹(Stacking) 앙상블 학습 및 SHAP 기표를 통한 중요도 시각화

**주요 결과**:
- XGBoost 및 스태킹 앙상블 모델이 F1-score 0.87 및 정확도 94%의 최우수 가짜 리뷰 식별 성능을 나타냄을 보임
- SHAP 분석 결과 리뷰어의 네트워크 연결도 및 감성-평점 간 불일치성이 가짜 여부를 가려내는 가장 지배적인 단서임을 실증함


## 초록 (원문)

Online reviews significantly influence consumer decision-making, yet their credibility is increasingly undermined by the rise of fake and manipulated content. This study addresses the growing challenge of detecting deceptive online reviews by developing a highly accurate, robust, and explainable machine learning framework that supports trust and reliability in digital marketplaces. The proposed multimodal framework integrates textual, behavioural, temporal, and network-based features to enhance detection performance. Textual characteristics are extracted using term frequency-inverse document frequency (TF-IDF) and sentiment analysis, while behavioural and temporal attributes model reviewer activity patterns. Network-oriented features capture suspicious reviewer interactions. To mitigate class imbalance, synthetic samples are generated using the synthetic minority over-sampling technique (SMOTE). Several machine learning models—including logistic regression, decision trees, XGBoost, and a stacking ensemble—are trained and evaluated. Experimental findings show that XGBoost and the stacking ensemble deliver strong balanced performance, achieving an F1-score of approximately 0.87 and an accuracy of 0.94. Decision Trees exhibit high precision (0.98), albeit with comparatively lower recall. To ensure transparency and interpretability, Shapley additive explanations (SHAP) are used to analyse model predictions. Results indicate that reviewer connectivity, co-reviewer counts, and sentiment–rating inconsistencies are among the most influential features. Overall, the proposed framework enhances detection accuracy and provides meaningful, explainable insights, making it well-suited for deployment in real-world digital marketplaces. Future work will focus on extending the framework to multilingual datasets and incorporating adaptive learning mechanisms to address evolving deceptive behaviour.

## 키워드

Credibility, Transparency (behavior), Trustworthiness, Reliability (semiconductor), Focus (optics), Supervised learning, Decision tree, Class (philosophy)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

