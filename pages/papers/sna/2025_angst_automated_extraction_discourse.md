---
title: "Automated extraction of discourse networks from large volumes of media data"
authors: ['Mario Angst', 'Neitah Noemi Müller', 'Viviane Walker']
year: 2025
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Social Media and Politics', 'Opinion Dynamics and Social Influence']
source: raw/2025_openalex_Automated_extraction_of_discourse_networks_from_nws_2025_4.md
---

# Automated extraction of discourse networks from large volumes of media data
**제목(한글)**: 대규모 미디어 데이터에서 담론 네트워크의 자동 추출

**저자**: Mario Angst; Neitah Noemi Müller; Viviane Walker
**출처**: Network Science, Vol.13
**발행일**: 2025-01-01
**DOI**: https://doi.org/10.1017/nws.2025.4

## 한국어 요약

**연구질문**: 대용량 신문 데이터에서 조직-신념 이원 네트워크(bipartite network)로 이루어진 담론 네트워크를 자동으로 추출하는 방법을 어떻게 개발하고 검증할 수 있는가?

**방법론**:
- 개체명 인식(NER), 개체 연결, 지도 학습 텍스트 분류, 대형 언어 모델(LLM) 기반 입장 탐지(stance detection) 결합
- 취리히 도시 지속가능 교통 담론 네트워크 12년간 200만 건 신문 기사 적용
- 슬라이딩 타임 윈도우(sliding time window) 기반 내부 타당도 검증

**주요 결과**:
- 자동화 방법이 기본 구조와 고차 구조적 지표를 잘 복원함
- 슬라이딩 타임 윈도우를 통한 집계 시 자동화 데이터의 내부 타당도 향상 (윈도우 타당도 가설)
- 고품질 테스트 세트 구축과 정독(close reading)의 중요성 강조

## 초록 (원문)

Abstract Understanding and tracking societal discourse around essential governance challenges of our times is crucial. One possible heuristic is to conceptualize discourse as a network of actors and policy beliefs. Here, we present an exemplary and widely applicable automated approach to extract discourse networks from large volumes of media data, as a bipartite graph of organizations and beliefs connected by stance edges. Our approach leverages various natural language processing techniques, alongside qualitative content analysis. We combine named entity recognition, named entity linking, supervised text classification informed by close reading, and a novel stance detection procedure based on large language models. We demonstrate our approach in an empirical application tracing urban sustainable transport discourse networks in the Swiss urban area of Zürich over 12 years, based on more than one million paragraphs extracted from slightly less than two million newspaper articles. We test the internal validity of our approach. Based on evaluations against manually automated data, we find support for what we call the window validity hypothesis of automated discourse network data gathering. The internal validity of automated discourse network data gathering increases if inferences are combined over sliding time windows. Our results show that when leveraging data redundancy and stance inertia through windowed aggregation, automated methods can recover basic structure and higher-level structurally descriptive metrics of discourse networks well. Our results also demonstrate the necessity of creating high-quality test sets and close reading and that efforts invested in automation should be carefully considered.

## 키워드

Computer science, Artificial intelligence, Natural language processing

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

