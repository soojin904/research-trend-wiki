---
title: "Semantic Alignment and Output Constrained Generation for Reliable LLM-based Classification"
authors: ['Jixiao Yang', 'Sebastian Sun', 'Yang Wang', 'Yutong Wang', 'Xikai Yang', 'Chi Zhang']
year: 2026
venue: ""
tags: ['Topic Modeling', 'Text and Document Classification Technologies', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_Semantic_Alignment_and_Ou_emc68537_2026_11441962.md
---

# Semantic Alignment and Output Constrained Generation for Reliable LLM-based Classification
**제목(한글)**: 신뢰할 수 있는 LLM 기반 텍스트 분류를 위한 시맨틱 정렬 및 출력 제약형 생성 기법

**저자**: Jixiao Yang; Sebastian Sun; Yang Wang; Yutong Wang; Xikai Yang; Chi Zhang
**출처**: , Vol.None, pp.317-322
**발행일**: 2026-01-12
**DOI**: https://doi.org/10.1109/emc68537.2026.11441962

## 한국어 요약

**연구질문**: 생성형 대규모 언어 모델을 텍스트 분류에 활용할 때 발생하는 제어 불가능성, 불안정한 출력 일관성, 그리고 모호한 의사결정 경로를 해소할 수 있는가?

**방법론**:
- 입력 텍스트와 태스크 지시사항을 공동 인코딩하여 의미론적 표현과 분류 제약조건을 통합하는 프레임워크 구축
- 모델이 명시적으로 지시사항의 카테고리 경계 및 판별 기준을 따르도록 강제하는 카테고리 시맨틱 정렬 메커니즘 도입
- 디코딩 단계에서 토큰의 생성 공간을 미리 정의된 유효 카테고리 집합(set)으로 한정하는 구조화된 제약 디코딩(constrained decoding) 구현

**주요 결과**:
- 제안 모델이 프롬프트의 무작위 변형이나 모델 내재 편향에 따른 분류 불일치를 획기적으로 완화함을 규명
- 성능 평가 결과 분류 정확도, 판별 안정성 및 전체 클래스 분리도에서 타 베이스라인 대비 탁월한 성과를 보이며 신뢰할 수 있는 텍스트 분류 프레임워크 구축에 기여


## 초록 (원문)

To address the limited controllability, unstable output consistency, and weakly constrained decision processes of large language models in text classification tasks, this work proposes a controllable prompt-driven text classification method that establishes an end-to-end unified modeling framework from instruction alignment to constrained decoding. Text classification is reformulated as an instruction-conditioned generative discriminative problem. Input texts and task instructions are jointly encoded to form a unified internal representation that integrates textual semantics with classification constraints. On this basis, a category semantic alignment mechanism is introduced to ensure that the model explicitly follows category boundaries and decision criteria defined by the instructions, thereby reducing classification inconsistency caused by prompt variation or implicit bias. To further improve output reliability, a structured constrained decoding strategy is designed to restrict the generation space to a predefined set of valid categories, preventing redundant text or invalid outputs from interfering with classification results. Comparative analysis under unified data and evaluation settings demonstrates that the proposed method achieves more consistent advantages in classification accuracy, discriminative stability, and overall separability. These findings indicate that deeply integrating instruction understanding and output control into the decision process of large language models effectively transforms their generative capacity into stable, interpretable, and controllable text classification capability, providing a systematic solution for building reliable intelligent text analysis systems.

## 키워드

Discriminative model, Semantics (computer science), Set (abstract data type), Generative grammar, Representation (politics), Process (computing), Generative model, Task (project management)

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

