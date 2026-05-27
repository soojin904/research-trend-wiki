---
title: "TTSR: Test-Time Self-Reflection for Continual Reasoning Improvement"
authors: ['Haoyang He', 'Zihua Rong', 'Liangjie Zhao', 'Yunjia Zhao', 'Lan Yang (457660)', 'Honggang Zhang']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Topic Modeling', 'Multimodal Machine Learning Applications', 'Intelligent Tutoring Systems and Adaptive Learning']
source: raw/applied/applied_2026_TTSR_TestTime_SelfReflect_nodoi.md
---

# TTSR: Test-Time Self-Reflection for Continual Reasoning Improvement
**제목(한글)**: TTSR: 지속적 추론 향상을 위한 테스트 시간 자기 성찰

**저자**: Haoyang He; Zihua Rong; Liangjie Zhao; Yunjia Zhao; Lan Yang (457660); Honggang Zhang
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-02-06
**DOI**: 

## 한국어 요약

**연구질문**: 테스트 시간 훈련(Test-time Training)에서 어려운 문제에 대한 자가 생성 의사 레이블(pseudo-labels)의 신뢰성 부족 문제와 모델별 추론 약점에 적응하는 메커니즘 부재를 해결하기 위해, 학생-교사 역할 교대 방식의 자기 성찰 프레임워크는 어떻게 설계되는가?

**방법론**:
- 단일 사전 훈련 언어 모델이 테스트 시간에 학생(Student)과 교사(Teacher) 역할을 교대하는 TTSR 프레임워크 설계
- 학생은 문제 풀이와 변형 문제 학습, 교사는 실패한 추론 궤적 분석 및 반복되는 추론 약점을 파악해 맞춤형 변형 문제 생성
- 복수의 수학 추론 벤치마크와 다양한 모델 백본에서 평가

**주요 결과**:
- TTSR은 복수의 어려운 수학 추론 벤치마크에서 추론 성능을 일관되게 향상시키며 다양한 모델 백본과 일반 영역 추론 과제에서도 높은 일반화 능력을 보임
- 교사 매개 자기 성찰이 테스트 시간에 안정적이고 지속적인 추론 향상을 위한 효과적인 경로임을 실증함

## 초록 (원문)

Test-time Training enables model adaptation using only test questions and offers a promising paradigm for improving the reasoning ability of large language models (LLMs). However, it faces two major challenges: test questions are often highly difficult, making self-generated pseudo-labels unreliable, and existing methods lack effective mechanisms to adapt to a model's specific reasoning weaknesses, leading to inefficient learning. To address these issues, we propose \textbf{TTSR}, a self-reflective test-time self-evolving training framework. TTSR employs a single pretrained language model that alternates between the roles of a \textit{Student} and a \textit{Teacher} at test time. The Student focuses on solving problems and learning from synthesized variant questions, while the Teacher analyzes the Student's failed reasoning trajectories, summarizes recurring reasoning weaknesses, and synthesizes targeted variant questions accordingly. This process guides the model to improve within a learnable regime through a continual self-evolving loop. Experimental results on multiple challenging mathematical reasoning benchmarks show that TTSR consistently improves reasoning performance and generalizes well across different model backbones and general-domain reasoning tasks. These findings suggest that teacher-mediated self-reflection provides an effective pathway for stable and continual reasoning improvement at test time.

## 키워드

Process (computing), Test (biology), Case-based reasoning, Adaptation (eye), Model-based reasoning, Reasoning system, Adaptive reasoning, Non-monotonic logic

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

