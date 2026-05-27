---
title: "Ensemble Machine Learning and Natural Language Processing for Automated Cancer Indicator Detection in Clinical Notes"
authors: ['Md Yassir Mottalib', 'Nur Nobe', 'MD Tanvir Islam', 'Afjal Hossain Jisan', 'Md. Emran Hossen']
year: 2026
venue: "International Journal of Medical Science and Public Health Research"
tags: ['Machine Learning in Healthcare', 'AI in cancer detection', 'Topic Modeling']
source: raw/applied/applied_2026_Ensemble_Machine_Learning_volume07issue03_05.md
---

# Ensemble Machine Learning and Natural Language Processing for Automated Cancer Indicator Detection in Clinical Notes
**제목(한글)**: 의료 기록지 내 암 지표 자동 탐지를 위한 앙상블 머신러닝 및 자연어 처리 기법

**저자**: Md Yassir Mottalib; Nur Nobe; MD Tanvir Islam; Afjal Hossain Jisan; Md. Emran Hossen
**출처**: International Journal of Medical Science and Public Health Research, Vol.7, pp.27-37
**발행일**: 2026-03-23
**DOI**: https://doi.org/10.37547/ijmsphr/volume07issue03-05

## 한국어 요약

**연구질문**: 병원 전자 의무 기록(EHR)의 비정형 자유 텍스트 임상 기록(Clinical Notes)에서 환자의 조기 암 발병 지표 및 진단 소견을 어떻게 가장 정확하게 자동 식별할 것인가?

**방법론**:
- Kaggle 의료 텍스트 데이터 및 위스콘신 유방암 데이터셋 수집
- TF-IDF 기반 특징 추출 및 의학 용어 벡터화 전처리 수행
- 로지스틱 회귀, SVM, 랜덤 포레스트, 그래디언트 부스팅 분류기 등 다중 알고리즘 앙상블 모델 비교 훈련

**주요 결과**:
- 앙상블 기법 중 그래디언트 부스팅 분류 모델이 정확도 95%, 정밀도 94%, F1-score 93%로 기존 단일 머신러닝 기법들을 압도적으로 능가함
- 의료진의 의사결정 수동 검토 부하를 대폭 경감하는 조기 암 예방용 의사결정 지원 시스템(CDSS) 가이드라인을 제안함


## 초록 (원문)

Trebuchet MSEarly identification of cancer indicators within clinical documentation is essential for improving diagnostic efficiency and patient outcomes. This study presents a Natural Language Processing (NLP) and machine learning framework designed to extract cancer-related indicators from unstructured clinical notes. Clinical text data obtained from Kaggle and structured diagnostic features from the Breast Cancer Wisconsin (Diagnostic) Dataset available through the UCI Machine Learning Repository were used to develop and evaluate the proposed model. The methodology involved comprehensive text preprocessing, TF–IDF-based feature extraction, and feature engineering to represent clinically meaningful patterns in narrative medical text. Multiple machine learning algorithms, including Logistic Regression, Support Vector Machines, Random Forest, and Gradient Boosting classifiers, were trained and evaluated using standard performance metrics. Experimental results indicate that ensemble learning approaches outperform traditional classifiers in detecting cancer-related information from clinical narratives. Among the evaluated models, the Gradient Boosting classifier achieved the best performance with an accuracy of 95%, precision of 94%, recall of 93%, and an F1-score of 0.93. These results demonstrate the effectiveness of machine learning–based NLP systems in identifying cancer indicators within electronic health records. The proposed framework highlights the potential of automated clinical text analysis to support early cancer detection, enhance clinical decision support systems, and improve healthcare data analytics.

## 키워드

Random forest, Support vector machine, Boosting (machine learning), Gradient boosting, Ensemble learning, Feature engineering, Classifier (UML), Clinical decision support system

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

