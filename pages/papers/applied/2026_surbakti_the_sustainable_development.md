---
title: "The 17 UN Sustainable Development Goals: Classification of Research Topics Using BERT and Logistic Regression"
authors: ['Eunike Endariahna Surbakti', 'Fenina A. T. Tobing', 'Charlie Frederico', 'Sagita Sasmita Wijaya', 'Felix Frederico']
year: 2026
venue: "Evergreen"
tags: ['Computational and Text Analysis Methods', 'Text and Document Classification Technologies', 'scientometrics and bibliometrics research']
source: raw/applied/applied_2026_The_17_UN_Sustainable_Dev_7411078.md
---

# The 17 UN Sustainable Development Goals: Classification of Research Topics Using BERT and Logistic Regression
**제목(한글)**: 유엔의 17대 지속가능발전목표(UN SDGs): BERT 및 로지스틱 회귀를 활용한 연구 주제 분류

**저자**: Eunike Endariahna Surbakti; Fenina A. T. Tobing; Charlie Frederico; Sagita Sasmita Wijaya; Felix Frederico
**출처**: Evergreen, Vol.13, pp.417-431
**발행일**: 2026-03-01
**DOI**: https://doi.org/10.5109/7411078

## 한국어 요약

**연구질문**: 대학의 대규모 연구 산출물(논문 초록 등)을 수작업 없이 17개 UN 지속가능발전목표(SDGs) 분류 카테고리에 정확하게 정렬 및 매핑하기 위한 최적의 텍스트 머신러닝 학습 모델은 무엇인가?

**방법론**:
- 2018~2023년에 발행된 총 76,958건의 대규모 연구 초록 텍스트 데이터를 학습 셋으로 활용
- 사전학습 언어 표상 모델(BERT)을 4 epoch 미세 조정 학습시킨 딥러닝 방식과 TF-IDF 특징 벡터에 L1 페널티 규제를 준 로지스틱 회귀(Logistic Regression) 분류기 방식 설계 및 비교

**주요 결과**:
- BERT 기반 분류 모델이 정확도 90.68%(정밀도 0.99, F1 0.87)를 기록해, 로지스틱 회귀 모델(정확도 90.01%, 정밀도 0.86) 대비 오분류를 줄이고 훨씬 정교한 텍스트 매핑력을 보임을 검증
- 대학 기관의 실질적인 SDGs 성과 평가 자동화 및 연구 인증 관리 효율화를 증명함


## 초록 (원문)

An academic institution with over 200 lecturers has produced more than 3,000 research articles between 2018 and 2023. Accurately classifying these research outputs according to the 17 United Nations Sustainable Development Goals (UN SDGs)—a global agenda addressing issues such as poverty, education, gender equality, clean energy, and climate action—is vital for demonstrating institutional contributions to sustainability and supporting faculty accreditation processes. Traditionally, the Research and Community Service Institute of private universities has performed this classification manually, which is inefficient and time-consuming. To address this challenge, two machine learning-based text classification systems were developed and evaluated. The model was trained on a dataset of 76,958 records. The first approach implements a Bidirectional Encoder Representations from Transformers (BERT) model, a state-of-the-art deep learning framework in Natural Language Processing. Preprocessing was performed using NLTK, and the model was fine-tuned over 4 epochs with a learning rate of 2e-5 and a batch size of 32, using a 70/30 train-test split. This model delivered superior performance, with an accuracy of 90.68%, precision of 0.99, recall of 0.82, and an F1-score of 0.87. The second approach utilizes a Logistic Regression model with TF-IDF (Term Frequency-Inverse Document Frequency) for text vectorization. This model employs the L1 penalty and the Saga solver, trained with 80% of the dataset and tested on the remaining 20%, without additional data cleaning. It achieved an accuracy of 90.01%, a precision of 0.86, recall of 0.82, and an F1-score of 0.84. Both models demonstrated strong performance, but the BERT-based model provided better precision and overall classification quality. The findings show that both models deliver strong classification performance, with the BERT-based model providing superior precision and overall quality. These systems have been presented to the university for potential adoption, offering a more efficient and consistent approach to aligning institutional research with 17 UN SDGs.

## 키워드

Preprocessor, Logistic regression, Sustainability, Precision and recall, Accreditation, Sustainable development, Support vector machine

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

