---
title: "AbjadMed: Arabic Medical Text Classification at AbjadNLP 2026"
authors: ['Pranav Gupta', 'Niranjan Kumar M', 'Balaji Nagarajan', 'Imed Zitouni', 'Mo El-Haj']
year: 2026
venue: ""
tags: ['Topic Modeling', 'Natural Language Processing Techniques', 'Biomedical Text Mining and Ontologies']
source: raw/applied/applied_2026_AbjadMed_Arabic_Medical_T_2026_abjadnlp_1_64.md
---

# AbjadMed: Arabic Medical Text Classification at AbjadNLP 2026
**제목(한글)**: AbjadMed: AbjadNLP 2026의 아랍어 의료 텍스트 분류

**저자**: Pranav Gupta; Niranjan Kumar M; Balaji Nagarajan; Imed Zitouni; Mo El-Haj
**출처**: , Vol.None, pp.506-514
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.18653/v1/2026.abjadnlp-1.64

## 한국어 요약

**연구질문**: 극심한 불균형(severe class imbalance), 미세 카테고리 구성 및 의학 질문의 노이즈가 내재한 실제 진료 환경 데이터셋에서 아랍어 의료 텍스트를 정확하게 분류하는 최적의 사전 학습 모델 벤치마크는 어떠한가?

**방법론**:
- 27,951개 훈련셋과 18,634개 테스트셋으로 구성된 아랍어 의료 상담 질의 데이터셋(AHD) 구축
- 82개 세부 의학 카테고리를 대상으로 사전 학습 모델(BERT 계열 등) 학습
- 소수 카테고리 판별 능력을 엄격히 평가하기 위해 Macro-averaged F1 지표를 기준으로 성능 검증

**주요 결과**:
- 최신 사전 학습 모델을 사용하더라도 의미가 겹치거나 빈도가 낮은 의학 질문 분류 정확도가 현저히 하락하는 임상 의료 NLP의 구조적 성능 장벽을 확인함
- 향후 아랍권 의료 보조 봇 성능 개선을 위한 재현 가능한 표준 벤치마크를 정립함


## 초록 (원문)

We present AbjadMed, a shared task on Arabic medical text classification organised as part of the 2nd AbjadNLP workshop at EACL 2026.The task targets supervised multi-class classification under realistic conditions of severe class imbalance, fine-grained category structure, and naturally occurring label noise.Participants assign each Arabic medical question-answer instance to one of 82 predefined categories derived from real healthcare consultations.The dataset is based on the Arabic Healthcare Dataset (AHD) and is released as curated training and test splits containing 27,951 and 18,634 instances respectively, while preserving the original label distribution.Systems are evaluated using macro-averaged F1 to emphasise performance on minority medical topics.Results show that Arabic medical text classification remains challenging even with modern pretrained models, particularly for lowfrequency and semantically overlapping categories.AbjadMed provides a reproducible benchmark for studying robustness and generalisation in Arabic healthcare NLP.

## 키워드

Arabic, Feature (linguistics), Subject (documents), MEDLINE

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

