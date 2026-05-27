---
title: "Blending sentiment and topic analysis to explain discrete emotions from online fitness center customer reviews"
authors: ['Enrique Alcántara Alcover', 'Antonio Hernández Martín', 'Ricardo Cuevas Campos', 'Daniel Duclos Bastías']
year: 2026
venue: "Dialnet (Universidad de la Rioja)"
tags: ['Sentiment Analysis and Opinion Mining', 'Digital Marketing and Social Media', 'Mental Health via Writing']
source: raw/applied/applied_2026_Blending_sentiment_and_to_nodoi.md
---

# Blending sentiment and topic analysis to explain discrete emotions from online fitness center customer reviews
**제목(한글)**: 온라인 피트니스 센터 고객 리뷰를 통한 개별 감정 설명을 위한 감성 분석과 토픽 분석의 융합

**저자**: Enrique Alcántara Alcover; Antonio Hernández Martín; Ricardo Cuevas Campos; Daniel Duclos Bastías
**출처**: Dialnet (Universidad de la Rioja), Vol.None
**발행일**: 2026-01-01
**DOI**: 

## 한국어 요약

**연구질문**: 디지털 리뷰의 텍스트에 나타난 단어의 주제(Topic) 연관성과 감성 극성이 헬스장 회원들이 느끼는 구체적 감정(기쁨, 분노, 슬픔, 신뢰 등)을 어떻게 예측하고 유발 인자를 역추적할 수 있는가?

**방법론**:
- 스페인 피트니스 센터 38곳에서 수집된 3,250개의 온라인 리뷰 활용
- LDA 기반 토픽 모델링, TextBlob 감성 분석, XGBoost 모델 학습, 그리고 SHAP 설명 가능 인공지능(Explainable AI) 기법을 융합한 "양극화된 토픽(Polarized topics)" 예측 접근법 구축

**주요 결과**:
- 직원 친절도, 가성비, 청결도가 감정 예측에 매우 강력한 인자이며, 특히 코로나 관련 임시 휴업 언급이 분노와 슬픔을 증가시킴을 증명
- 양극화된 토픽 기반 예측 모델을 통해 주요 10가지 감정에서 F1-스코어 0.84 이상의 매우 높은 분류 성능을 확보하고, 서비스 디자인 개선을 위한 해석 지표를 제시


## 초록 (원문)

Introduction: Emotions elicited by services influence customer satisfaction and overall experience. Online reviews provide a valuable source for identifying these emotional patterns through text‑analysis techniques. Objective: To examine how topic relevance and sentiment expressed in digital reviews predict discrete emotions among gym users, proposing an approach based on “polarized topics.” Methodology: A total of 3,250 reviews from 38 Spanish gyms were analyzed. The study employed a mixed‑methods approach combining topic modeling using LDA, sentiment analysis with TextBlob, and machine‑learning algorithms (XGBoost), integrated with SHAP explainability techniques. The interaction between topics and sentiment polarity was used to predict ten discrete emotions, including joy, anger, sadness, and trust. Results: Staff friendliness, value for money, and hygiene emerged as highly predictive topics. Positive evaluations of staff increased emotions such as joy and trust, whereas comments related to COVID‑related absences were associated with higher levels of anger and sadness. The “polarized topics” approach yielded strong emotional classification performance, achieving F1‑scores above 0.84 for most emotions. Discussion: The findings show that the combination of topic modeling, sentiment analysis, and explainable AI enables precise identification of which service attributes trigger specific emotions, offering a useful interpretive framework for managers in the fitness sector. Conclusions: The proposed method constitutes a scalable and transparent approach for predicting discrete emotions in reviews. Its application can support improvements in service design and emotional alignment in organizations oriented toward wellbeing.

## 키워드

Sentiment analysis, Relevance (law), Identification (biology), Service (business), Topic model, Anger, Social media, Customer satisfaction

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

