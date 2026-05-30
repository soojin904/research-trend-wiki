---
title: "Zero-Inflated Text Data Analysis Using Imbalanced Data Sampling and Statistical Models"
authors: ['Sunghae Jun']
year: 2025
venue: "Computers"
tags: ['Text and Document Classification Technologies', 'Imbalanced Data Classification Techniques', 'Topic Modeling']
source: raw/applied/applied_2025_ZeroInflated_Text_Data_An_computers14120527.md
---

# Zero-Inflated Text Data Analysis Using Imbalanced Data Sampling and Statistical Models

**제목(한글)**: 불균형 데이터 샘플링과 통계 모델을 활용한 영과잉(Zero-Inflated) 텍스트 데이터 분석

## 한국어 요약

**연구질문**: 문서-키워드 행렬의 과도한 영값(Zero-Inflation)과 과산포(Overdispersion) 문제를 언더샘플링 기반 전처리와 확률적 계수 모델의 결합으로 해결할 수 있는가?

**방법론**:
- 언더샘플링(Undersampling) 기반 불균형 데이터 처리와 고전적 확률적 계수 모델 통합 프레임워크 제안
- 포아송 일반화 선형 모델(Poisson GLM), 영과잉 포아송(ZIP), 영과잉 음이항(ZINB) 모델 적용
- 실세계 특허 문서와 시뮬레이션 데이터셋을 활용한 프레임워크 평가

**주요 결과**:
- 언더샘플링 기반 전처리가 다운스트림 모델 수정 없이 모델 적합도 향상
- 희소 계수 데이터의 통계적 해석 가능성을 유지하면서 영과잉 텍스트 분석 가능
- 특허 문서 등 고희소성 텍스트 데이터 분석의 실용적 전처리 전략 제시
- 모델 선택 및 데이터 균형화 기법에 대한 실질적 통찰 제공

**저자**: Sunghae Jun
**출처**: Computers, Vol.14, pp.527-527
**발행일**: 2025-12-02
**DOI**: https://doi.org/10.3390/computers14120527

## 초록 (원문)

Text data often exhibits high sparsity and zero inflation, where a substantial proportion of entries in the document–keyword matrix are zeros. This characteristic presents challenges to traditional count-based models, which may suffer from reduced predictive accuracy and interpretability in the presence of excessive zeros and overdispersion. To overcome this issue, we propose an effective analytical framework that integrates imbalanced data handling by undersampling with classical probabilistic count models. Specifically, we apply Poisson’s generalized linear models, zero-inflated Poisson, and zero-inflated negative binomial models to analyze zero-inflated text data while preserving the statistical interpretability of term-level counts. The framework is evaluated using both real-world patent documents and simulated datasets. Empirical results demonstrate that our undersampling-based approach improves the model fit without modifying the downstream models. This study contributes a practical preprocessing strategy for enhancing zero-inflated text analysis and offers insights into model selection and data balancing techniques for sparse count data.

## 키워드

Interpretability, Undersampling, Statistical model, Preprocessor, Model selection, Data modeling, Probabilistic logic, Data pre-processing

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

