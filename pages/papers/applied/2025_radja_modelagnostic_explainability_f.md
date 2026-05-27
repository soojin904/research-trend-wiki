---
title: "Model-Agnostic Explainability for Multi-Label Classification via Formal Concept Analysis"
authors: ['Hakim Radja', 'Yassine Djouadi', 'Karim Tabia']
year: 2025
venue: "Informatica"
tags: ['Text and Document Classification Technologies', 'Explainable Artificial Intelligence (XAI)', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2025_ModelAgnostic_Explainabil_inf_v49i19_9947.md
---

# Model-Agnostic Explainability for Multi-Label Classification via Formal Concept Analysis

**제목(한글)**: 형식 개념 분석(Formal Concept Analysis)을 활용한 다중 레이블 분류의 모델 불가지론적 설명 가능성

## 한국어 요약

**연구질문**: 형식 개념 분석(FCA)을 활용하면 다중 레이블 분류 모델의 예측에 대해 해석 가능하고 컴팩트한 설명을 제공할 수 있는가?

**방법론**:
- 결정적 속성 집합(DAS)과 유의미 속성 집합(SSA) 개념 도입
- FCA 기반 DAS 규칙(DAS-rules) 생성으로 개별 예측 설명
- 클래스별 중요도 점수 산출 및 Stack Overflow·Yelp·TMC2007-500 벤치마크 실험

**주요 결과**:
- 높은 지역 충실도(local fidelity)와 컴팩트한 설명 생성 달성
- 특징 간 상호작용을 성공적으로 포착하는 새로운 설명 가능 AI(XAI) 프레임워크 구축
- 다중 레이블 분류의 설명 가능성 연구에 실용적 효과성 입증

**저자**: Hakim Radja; Yassine Djouadi; Karim Tabia
**출처**: Informatica, Vol.49
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.31449/inf.v49i19.9947

## 초록 (원문)

Multi-label classification refers to a supervised learning problem where a single data instance can correspond to several labels simultaneously. While these models achieve high prediction accuracy, they share some limitations with single-label classifiers, particularly in terms of interpretability and explainability. In this work, we introduce a model-agnostic explainability method that enhances the interpretability of multilabel classification models using Formal Concept Analysis (FCA). Our approach aims to provide users with clearer insights into how these models make predictions, helping them better understand the rationale behind the decisions. Specifically, we address key questions such as: What is the smallest set of featuresneeded for the multi-label classifier f to make a prediction? and Which features are relevant to a specific prediction? By answering these questions, our method seeks to improve user confidence in the model’s decisions and foster a deeper understanding of multi-label classification. We introduce the key concepts of the Decisive Attribute Set (DAS) and the Significant Attribute Set (SSA). A DAS is the smallest set of features that can independently lead to a prediction, while an SSA includes all the features that influence the prediction of one or more labels. Additionally, we introduce a dedicated class-specific importance score that quantifies the role of each attribute, based on its frequency and specificity across formal concepts. Usingthese concepts, we generate clear, interpretable patterns in the form of rules, referred to as “DAS-rules”, which provide straightforward explanations for individual predictions. Our method achieves high local fidelity, generates compact explanations, and successfully captures feature interactions, as demonstrated through extensive experiments on three benchmark datasets (Stack Overflow, Yelp, and TMC2007-500). These results demonstrate the novelty and practical effectiveness of our FCA-based framework for multilabel explainability.

## 키워드

Interpretability, Formal concept analysis, Classifier (UML), Set (abstract data type), Key (lock), Feature (linguistics)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

