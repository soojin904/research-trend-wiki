---
title: "From Global to Local: Learning Context-Aware Graph Representations for Document Classification and Summarization"
authors: ['Ruangrin Ldallitsakool', 'Margarita Bugueño', 'Gerard de Melo']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Advanced Graph Neural Networks', 'Topic Modeling', 'Text and Document Classification Technologies']
source: raw/applied/applied_2026_From_Global_to_Local_Lear_nodoi.md
---

# From Global to Local: Learning Context-Aware Graph Representations for Document Classification and Summarization
**제목(한글)**: 글로벌에서 로컬로: 문서 분류 및 요약을 위한 맥락 인식 그래프 표현 학습

**저자**: Ruangrin Ldallitsakool; Margarita Bugueño; Gerard de Melo
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-02-03
**DOI**: 

## 한국어 요약

**연구질문**: 동적 슬라이딩 윈도우 어텐션 모듈을 활용해 문서의 국지적·중간 범위 의미 의존성과 구조적 관계를 효과적으로 포착하는 그래프 기반 문서 표현을 어떻게 자동 구성할 수 있는가?

**방법론**:
- 동적 슬라이딩 윈도우 어텐션을 활용한 데이터 기반 그래프 구성 방법 제안
- 그래프 어텐션 네트워크(GAT)를 학습된 그래프 위에서 훈련하여 문서 분류 및 추출적 요약에 적용

**주요 결과**:
- 기존 방법 대비 낮은 계산 자원으로 문서 분류에서 경쟁력 있는 성능 달성
- 추출적 요약에서의 잠재력과 현재 한계를 탐색적으로 평가함

## 초록 (원문)

This paper proposes a data-driven method to automatically construct graph-based document representations. Building upon the recent work of Bugueño and de Melo (2025), we leverage the dynamic sliding-window attention module to effectively capture local and mid-range semantic dependencies between sentences, as well as structural relations within documents. Graph Attention Networks (GATs) trained on our learned graphs achieve competitive results on document classification while requiring lower computational resources than previous approaches. We further present an exploratory evaluation of the proposed graph construction method for extractive document summarization, highlighting both its potential and current limitations. The implementation of this project can be found on GitHub.

## 키워드

Leverage (statistics), Automatic summarization, Graph, Construct (python library), Knowledge graph, Document classification, Training set

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

