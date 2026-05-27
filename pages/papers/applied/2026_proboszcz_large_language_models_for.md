---
title: "Large Language Models for Biomedical Article Classification"
authors: ['Jakub Proboszcz', 'Paweł Cichosz']
year: 2026
venue: "ArXiv.org"
tags: ['Biomedical Text Mining and Ontologies', 'Topic Modeling', 'Text and Document Classification Technologies']
source: raw/applied/applied_2026_Large_Language_Models_for_nodoi.md
---

# Large Language Models for Biomedical Article Classification

**제목(한글)**: 의생명 논문 분류를 위한 대형 언어 모델 활용 연구

## 한국어 요약

**연구질문**: 의생명 도메인 텍스트 분류 과제에서 다양한 크기의 LLM들이 텍스트 분류기로서 기존의 전통적 분류 알고리즘과 비교하여 어느 수준의 성능을 발휘하며, 어떤 설정이 가장 효과적인가?

**방법론**:
- 소형 및 중형 오픈소스 LLM 및 일부 독점 모델을 대상으로 다양한 프롬프트 유형, 출력 처리 방식, 퓨샷(Few-shot) 예시 수 및 선택 방법을 포함한 포괄적 구성 비교 실험
- 15개의 도전적 의생명 데이터셋에 대해 PR AUC 지표를 활용하여 성능 평가

**주요 결과**:
- 제로샷 프롬프팅에서 평균 PR AUC 0.4 이상, 퓨샷 프롬프팅에서 약 0.5를 달성하여 나이브 베이즈(0.5), 랜덤 포레스트(0.5~0.55), 파인튜닝된 트랜스포머 모델(0.5)과 동등한 수준임을 확인
- 클래스 확률 예측을 위해 출력 토큰 확률(Output Token Probabilities)을 활용하는 방식이 가장 효과적인 설정임을 검증

**저자**: Jakub Proboszcz; Paweł Cichosz
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-03-12
**DOI**: 

## 초록 (원문)

This work presents a systematic and in-depth investigation of the utility of large language models as text classifiers for biomedical article classification. The study uses several small and mid-size open source models, as well as selected closed source ones, and is more comprehensive than most prior work with respect to the scope of evaluated configurations: different types of prompts, output processing methods for generating both class and class probability predictions, as well as few-shot example counts and selection methods. The performance of the most successful configurations is compared to that of conventional classification algorithms. The obtained average PR AUC over 15 challenging datasets above 0.4 for zero-shot prompting and nearly 0.5 for few-shot prompting comes close to that of the naïve Bayes classifier (0.5), the random forest algorithm (0.5 with default settings or 0.55 with hyperparameter tuning) and fine-tuned transformer models (0.5). These results confirm the utility of large language models as text classifiers for non-trivial domains and provide practical recommendations of the most promising setups, including in particular using output token probabilities for class probability prediction.

## 키워드

Language model, Classifier (UML), Random forest, Naive Bayes classifier, Class (philosophy), Security token, Hyperparameter, Selection (genetic algorithm)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

