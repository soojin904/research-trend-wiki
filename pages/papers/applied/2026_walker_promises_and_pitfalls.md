---
title: "Promises and pitfalls of using LLMs to identify actor stances in political discourse"
authors: ['Viviane Walker', 'Mario Angst']
year: 2026
venue: ""
tags: ['Computational and Text Analysis Methods', 'Sentiment Analysis and Opinion Mining', 'Discourse Analysis in Language Studies']
source: raw/applied/applied_2026_Promises_and_pitfalls_of__5a3k8_v2.md
---

# Promises and pitfalls of using LLMs to identify actor stances in political discourse
**제목(한글)**: 정치적 담론에서 행위자의 입장 식별을 위한 LLM 활용의 성과와 한계

**저자**: Viviane Walker; Mario Angst
**출처**: , Vol.None
**발행일**: 2026-02-06
**DOI**: https://doi.org/10.31235/osf.io/5a3k8_v2

## 한국어 요약

**연구질문**: 특정 도메인이나 진술에 국한되지 않는 일반화된 형태의 입장 탐지(stance detection) 과업에서 대규모 언어 모델(LLM)을 활용한 제로샷 분류가 전통적 분류 방법 대비 유효한 성과를 내는가?

**방법론**:
- 4종의 공개 LLM에 대한 제로샷 입장 분류 수행 및 다양한 범용 프롬프트 체인(prompt chains) 테스트
- 지속 가능한 도시 교통 도메인의 독일 신문 기사 문단 1,710개 내 조직 개체(entity)들의 5가지 규범적 진술에 대한 입장 어노테이션 데이터셋 구축
- 기존 컴퓨터 언어학적 기법과 LLM의 분류 정확도 및 성향 비교

**주요 결과**:
- LLM을 통해 기존 접근 방식을 개선하고 유의미한 입장 분류 수준을 달성할 수 있음을 확인
- 분류 결과는 사용된 프롬프트 체인 설계, LLM 모델 종류 및 평가 진술문 내용에 따라 편차가 크게 나타남
- 모델의 복잡성과 성능 간 트레이드오프 분석을 수행하고, LLM 평가 시 도메인 특화 데이터셋 구축의 중요성을 입증


## 초록 (원문)

Empirical research in the social sciences is often interested in understanding actor stances; the positions that social actors take regarding normative statements in societal discourse. In automated text analysis applications, the classification task of stance detection remains challenging. Stance detection is especially difficult due to semantic challenges such as implicitness or missing context but also due to the general nature of the task. In this paper, we explore the potential of Large Language Models (LLMs) to enable stance detection in a generalized (non-domain, non-statement specific) form. Specifically, we test a variety of different general prompt chains for zero-shot stance classifications.Our evaluation data consists of textual data from a real-world empirical research project in the domain of sustainable urban transport. For 1710 German newspaper paragraphs, each containing an organizational entity, we annotated the stance of the entity toward one of five normative statements. A comparison of four publicly available LLMs show that they can improve upon existing approaches and achieve adequate performance. However, results heavily depend on the prompt chain method, LLM, and vary by statement. Our findings have implications for computational linguistics methodology and political discourse analysis, as they offer a deeper understanding of the strengths and weaknesses of LLMs in performing the complex semantic task of stance detection. We strongly emphasise the necessity of domain-specific evaluation data for evaluating LLMs and considering trade-offs between model complexity and performance.

## 키워드

Normative, Newspaper, Context (archaeology), Politics, Task (project management), Variety (cybernetics), Strengths and weaknesses

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

