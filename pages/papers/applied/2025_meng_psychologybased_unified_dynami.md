---
title: "A Psychology-based Unified Dynamic Framework for Curriculum Learning"
authors: ['Guangyu Meng', 'Qinkai Zeng', 'John P. Lalor', 'Hong Yu']
year: 2025
venue: "Computational Linguistics"
tags: ['Intelligent Tutoring Systems and Adaptive Learning', 'Topic Modeling', 'Machine Learning and Data Classification']
source: raw/applied/applied_2025_A_Psychologybased_Unified_coli_a_584.md
---

# A Psychology-based Unified Dynamic Framework for Curriculum Learning

**제목(한글)**: 커리큘럼 학습을 위한 심리학 기반 통합 동적 프레임워크

## 한국어 요약

**연구질문**: 다양한 난이도의 예시로부터 직접 학습하는 것은 인간과 기계 학습 모델 모두에게 어려운 일입니다. 보다 효과적인 전략은 학습자에게 쉬운 것부터 어려운 것 순서로 점진적으로 예시를 노출하는 것입니다. 커리큘럼 학습(Curriculum Learning, CL)은 이러한 전략을 기계 학습 모델 훈련에 적용하기 위해 제안되었습니다. 그러나 CL 프레임워크 설계에는 두 가지 주요 과제가 남아있습니다. 바로 훈련 데이터의 난이도를 정의하는 것과 각 훈련 단계에서 입력할 적절한 데이터 양을 결정하는 것입니다.

**방법론**:
- 본 논문은 심리측정학(Psychometrics)에서 영감을 받아 커리큘럼 학습을 위한 심리학 기반 통합 동적 프레임워크(Psychology-based Unified Dynamic Framework for Curriculum Learning, PUDF)를 제안합니다.
- 인공 크라우드(Artificial Crowds, AC)의 응답에 문항 반응 이론(Item Response Theory, IRT)을 적용하여 훈련 데이터의 난이도를 정량화합니다. 이 이론 기반의 IRT-AC 접근 방식은 전역적(즉, 모델 독립적)이며 해석 가능한 난이도 값을 도출합니다.
- IRT를 활용하여, 모델 훈련 중 적절한 데이터 양을 스케줄링하기 위한 훈련 전략인 모델 능력 추정 기반 동적 데이터 선택(Dynamic Data Selection via Model Ability Estimation, DDS-MAE)을 제안합니다.
- 우리의 난이도 레이블링과 모델 능력 추정은 일관된 이론인 IRT에 기반하므로, 이들의 값은 동일한 범위 내에서 비교 가능하며, 이는 다른 CL 방법론에 비해 정렬된 훈련 데이터 선택과 더 빠른 수렴으로 이어질 수 있습니다.

**주요 결과**:
- 실험 결과는 PUDF를 사용하여 사전 학습된 대규모 언어 모델(Large Language Models)을 미세 조정(Fine-tuning)할 때, 표준 미세 조정 및 최첨단 CL 방법론에 비해 벤치마크 데이터셋 스위트(suite)에서 더 높은 정확도와 더 빠른 수렴을 달성함을 보여줍니다.
- 어블레이션 연구(Ablation studies)와 다운스트림 분석(Downstream analyses)은 CL을 위한 PUDF의 영향을 추가로 검증합니다.

**저자**: Guangyu Meng; Qinkai Zeng; John P. Lalor; Hong Yu
**출처**: Computational Linguistics, Vol.None, pp.1-49
**발행일**: 2025-12-11
**DOI**: https://doi.org/10.1162/coli.a.584

## 초록 (원문)

Abstract Directly learning from examples of varying difficulty levels is often challenging for both humans and machine learning models. A more effective strategy involves exposing learners to examples in a progressive order from easy to difficult. Curriculum Learning (CL) has been proposed to implement this strategy in machine learning model training. However, two key challenges persist in CL framework design: defining the difficulty of training data and determining the appropriate amount of data to input at each training step. Drawing inspiration from psychometrics, this paper presents a Psychology-based Unified Dynamic Framework for Curriculum Learning (PUDF).We quantify the difficulty of training data by applying Item Response Theory (IRT) to responses from Artificial Crowds (AC). This theory-driven IRT-AC approach leads to global (i.e., model-independent) and interpretable difficulty values. Leveraging IRT, we propose a training strategy, Dynamic Data Selection via Model Ability Estimation (DDS-MAE), to schedule the appropriate amount of data during model training. Since our difficulty labeling and model ability estimation are based on a consistent theory, namely IRT, their values are comparable within the same scope, potentially leading to aligned training data selection and faster convergence compared to the other CL methods. Experimental results demonstrate that fine-tuning pre-trained large language models with PUDF leads to higher accuracy and faster convergence on a suite of benchmark datasets compared to standard fine-tuning and state-of-the-art CL methods. Ablation studies and downstream analyses further validate the impact of PUDF for CL.

## 키워드

Benchmark (surveying), Crowds, Suite, Convergence (economics), Schedule, Curriculum, Selection (genetic algorithm), Key (lock)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

