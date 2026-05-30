---
title: "Automatic classification of construction accident reports using BERTopic-GLDA approach"
authors: ['Jun Wang', 'Ziyi Qu', 'Shujie Wu', 'Martin Skitmore', 'Leyuan Ma']
year: 2025
venue: "Engineering Construction & Architectural Management"
tags: ['Occupational Health and Safety Research', 'Topic Modeling', 'Text and Document Classification Technologies']
source: raw/applied/applied_2025_Automatic_classification__ecam_04_2025_0692.md
---

# Automatic classification of construction accident reports using BERTopic-GLDA approach

**제목(한글)**: BERTopic-GLDA 접근 방식을 활용한 건설 사고 보고서의 자동 분류

## 한국어 요약

**연구질문**: 레이블된 데이터 의존도 감소, 클래스 불균형 관리, 분류 결과 해석 가능성 향상을 위한 준지도 분류 프레임워크를 제안한다.

**방법론**:
- 준지도 BERTopic-GLDA 프레임워크 도입 (BERTopic의 문맥 키워드 추출 + GLDA의 준지도 기능 통합)
- BERTopic을 이용한 문맥 인식 언어 임베딩 기반 시드 워드(seed words) 생성
- 두 개의 OSHA 데이터셋을 활용하여 프레임워크 평가
- YAKE-GLDA, SVM, CNN 등 기존 방법론들과 성능 비교

**주요 결과**:
- BERTopic-GLDA 프레임워크가 모든 평가 지표에서 우수한 성능을 보임 (Dataset 1 매크로 F1 0.64, Dataset 2 매크로 F1 0.73).
- 소수 클래스 분류에서 특히 뛰어난 성능을 보여 클래스 불균형 문제를 효과적으로 완화함.
- 사전 레이블된 데이터 의존도를 줄이고 분류 결과의 해석 가능성(interpretability)을 향상시킴.
- 건설 사고 보고서 분류에 대한 새로운 준지도 접근 방식을 제시하여 높은 분류 정확도와 불균형 데이터셋 문제 극복.

**저자**: Jun Wang; Ziyi Qu; Shujie Wu; Martin Skitmore; Leyuan Ma
**출처**: Engineering Construction & Architectural Management, Vol.None, pp.1-30
**발행일**: 2025-12-25
**DOI**: https://doi.org/10.1108/ecam-04-2025-0692

## 초록 (원문)

Purpose This study aims to propose a semi-supervised classification framework that reduces reliance on labeled data, manages class imbalance and improves the interpretability of classification outcomes. This study proposes a semi-supervised classification framework designed to minimize reliance on labeled data, effectively address class imbalance and enhance the interpretability of classification results. Design/methodology/approach A semi-supervised BERTopic-Guided Latent Dirichlet Allocation (GLDA) framework is introduced, integrating BERTopic's contextual keyword extraction with the semi-supervised capabilities of GLDA. BERTopic uses context-aware language embeddings to generate semantically rich, domain-specific seed words. These seed words guide GLDA in defining topics a priori, thereby enabling robust semi-supervised classification. The framework is evaluated on two OSHA datasets and benchmarked against statistical keyword-based methods, including YAKE-GLDA. Its performance is also compared with traditional supervised models such as SVM and CNN. Findings The BERTopic-GLDA framework demonstrates superior performance across all evaluation metrics. For Dataset 1, it achieves a macro F1 score of 0.64, outperforming YAKE-GLDA (0.53, a 20.8% improvement), support vector machine (SVM) (0.33, a 93.9% improvement) and convolutional neural network (CNN) (0.30, a 113% improvement). For Dataset 2, it achieves a macro F1 score of 0.73, surpassing YAKE-GLDA (0.43, a 69.8% improvement), SVM (0.55, a 32.7% improvement), and CNN (0.41, a 78.0% improvement). The framework performs particularly well in classifying minority classes, where traditional supervised models often fail and YAKE-GLDA performs poorly. This capability effectively mitigates class imbalance. Additionally, the method reduces dependence on pre-labeled data and improves interpretability, providing a scalable solution for real-world construction safety applications. Originality/value A novel semi-supervised approach is introduced for classifying construction accident reports, achieving higher classification accuracy while overcoming challenges posed by imbalanced datasets. Unlike conventional supervised methods, the framework does not require extensive pre-labeled datasets, reducing resource demands. Linking classification outcomes to meaningful topic keywords ensures interpretability, allowing practitioners to trace predictions to underlying linguistic patterns. Integrating BERTopic and GLDA significantly advances semi-supervised learning for construction accident classification, providing a practical tool for enhanced risk assessment and decision-making. In practice, the framework can be integrated into safety dashboards to categorize new reports automatically, visualize emerging trends and highlight high-risk categories. This integration facilitates faster incident response and more targeted safety management.

## 키워드

Interpretability, Support vector machine, Class (philosophy), Latent Dirichlet allocation, Scalability, Macro, Convolutional neural network, Artificial neural network

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

