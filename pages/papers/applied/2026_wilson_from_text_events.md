---
title: "From Text to Events: Turning Freedom House Reports into Evidence of Democratization and Democratic Backsliding"
authors: ['Matthew C. Wilson', 'Kelsey Martin-Morales', 'Gregory Nelson']
year: 2026
venue: ""
tags: ['Computational and Text Analysis Methods', 'Populism, Right-Wing Movements', 'Electoral Systems and Political Participation']
source: raw/applied/applied_2026_From_Text_to_Events_Turni_apsa_2026_hgrxk.md
---

# From Text to Events: Turning Freedom House Reports into Evidence of Democratization and Democratic Backsliding
**제목(한글)**: 텍스트에서 이벤트로: 프리덤 하우스 보고서를 민주화 및 민주주의 후퇴의 증거로 변환하기

**저자**: Matthew C. Wilson; Kelsey Martin-Morales; Gregory Nelson
**출처**: , Vol.None
**발행일**: 2026-03-31
**DOI**: https://doi.org/10.33774/apsa-2026-hgrxk

## 한국어 요약

**연구질문**: 대규모 텍스트 보고서(프리덤 하우스 연례 보고서)를 대규모 언어 모델을 활용해 투명하고 감사가 가능한 민주주의 관련 제도적 사건(event) 데이터로 자동 변환할 수 있는가?

**방법론**:
- 1990~2024년 프리덤 하우스(Freedom House) 국가 보고서를 구조화된 이벤트 데이터로 변환하는 LLM 기반 4단계 파이프라인 구축
- 228개국 대상 약 20만 건의 어노테이션된 이벤트 및 원본 텍스트 연결 증거 추출
- 인간 코더의 코딩 결과 및 기존 정치학 데이터셋과의 비교를 통한 개념적 타당성 검증 및 헝가리/폴란드의 민주주의 후퇴 사례 비교 적용

**주요 결과**:
- 인덱스 수치나 개별 정성 사례 연구의 한계를 보완하여, 국가별 제도적 변화의 시계열 순서(institutional sequencing) 분석을 정밀하게 수행 가능
- 추출된 모든 이벤트가 원문 텍스트의 실제 구절과 일 대 일로 연결되어 추적 및 감사 가능함(auditable interpretation)을 증명하여 학술적 타당성 확보


## 초록 (원문)

A key limitation in debates about democracy measurement and whether democratic backsliding is occurring is the mismatch between theoretical claims — about specific institutional actions and processes — and available data. Political events are the appropriate unit of analysis: they denote discrete actions by identifiable actors with consequences for democratic institutions, but are difficult to produce at scale. This paper presents an LLM-based pipeline that transforms Freedom House's annual country reports (1990–2024) into structured event data. Our four-stage process produces nearly 200,000 annotated events across 228 countries, each tied to textual evidence. Validation against human coders and existing datasets demonstrates high construct validity. We apply the data to compare democratic backsliding in Hungary and Poland. The primary contribution is auditable interpretation as a standard for LLM-assisted measurement — producing outputs traceable to verbatim source material. Such event-level data enables analyses of institutional sequencing where indices and case studies fall short.

## 키워드

Democracy, Democratization, Interpretation (philosophy), Construct (python library), Pipeline (software), Politics, Event (particle physics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

