---
title: "Dynamic Lifecycle Prediction of FMCG via Multimodal Reviews Combining BLIP and Prophet"
authors: ['Peng Zhao', 'Emily Thorne']
year: 2026
venue: "American Journal of Data Science and Analysis"
tags: ['Forecasting Techniques and Applications', 'Sentiment Analysis and Opinion Mining', 'Stock Market Forecasting Methods']
source: raw/applied/applied_2026_Dynamic_Lifecycle_Predict_ajdsa3599.md
---

# Dynamic Lifecycle Prediction of FMCG via Multimodal Reviews Combining BLIP and Prophet
**제목(한글)**: BLIP과 Prophet을 결합한 다중 모드 리뷰 분석 기반 일용소비재(FMCG)의 동적 수명 주기 예측

**저자**: Peng Zhao; Emily Thorne
**출처**: American Journal of Data Science and Analysis, Vol.7, pp.41-52
**발행일**: 2026-01-31
**DOI**: https://doi.org/10.71465/ajdsa3599

## 한국어 요약

**연구질문**: 높은 수요 변동성과 짧은 수명주기를 특징으로 하는 FMCG 제품에 대해, 소비자 리뷰 텍스트와 첨부 이미지를 융합 분석하여 수명 주기 및 수요 예측 정확도를 획기적으로 향상시킬 수 있는가?

**방법론**:
- BLIP(Bootstrapping Language-Image Pre-training) 모델을 사용해 텍스트와 이미지 결합의 다중 모드 시맨틱 감성 지표 추출
- 추출된 감성 시계열 데이터를 Prophet 예측 모델의 외부 변수(external regressors)로 결합
- 전자상거래 FMCG 대규모 거래 데이터셋을 활용한 경험적 수요 예측 비교 평가

**주요 결과**:
- 다중 모드 감성을 융합한 BLIP-Prophet 모델이 기존의 텍스트 기반 단일 모델이나 전통 통계 모델(ARIMA 등)보다 현저히 높은 정확도로 제품 수명 주기를 동적 예측함을 검증
- 소비자가 자발적으로 업로드하는 이미지가 시장 변화 유도 및 수요 감지에 매우 가치 있는 정성적 피드백 역할을 함을 확인


## 초록 (원문)

The Fast-Moving Consumer Goods (FMCG) industry is characterized by high demand volatility, short product lifecycles, and intense market competition. Accurate prediction of product lifecycles is critical for optimizing inventory management and marketing strategies. Traditional forecasting methods often rely heavily on historical sales data, neglecting the rich semantic information embedded in user-generated content, particularly the interplay between textual reviews and visual imagery. This paper proposes a novel predictive framework that integrates multimodal sentiment analysis with advanced time-series forecasting. We utilize the Bootstrapping Language-Image Pre-training (BLIP) model to extract unified semantic features from consumer reviews, effectively capturing the nuanced sentiment expressed through both text and uploaded product images. These multimodal sentiment indices are subsequently incorporated as external regressors into the Prophet forecasting model, which is adept at handling seasonality and trend shifts. Our empirical analysis, conducted on a large-scale dataset of e-commerce FMCG transactions, demonstrates that the proposed BLIP-Prophet framework significantly outperforms unimodal baselines and traditional time-series models. The results highlight the predictive value of visual consumer feedback in understanding market dynamics and offer a robust tool for decision-makers in the retail sector.

## 키워드

Bootstrapping (finance), Sentiment analysis, Product (mathematics), Fast-moving consumer goods, Demand forecasting, Predictive modelling, Autoregressive integrated moving average, Product category

## 위키 연관

- [[pages/concepts/personal_network|퍼스널 네트워크]]

## 메모

