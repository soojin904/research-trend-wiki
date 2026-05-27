---
title: "Human rights violations reporting dataset"
authors: ['Constantinos Djouvas', 'Nikandros Ioannides', 'Iosif Kovras', 'Christos Christodoulou']
year: 2026
venue: "Data in Brief"
tags: ['Human Rights and Development', 'Computational and Text Analysis Methods', 'Political Conflict and Governance']
source: raw/applied/applied_2026_Human_rights_violations_r_j_dib_2026_112854.md
---

# Human rights violations reporting dataset
**제목(한글)**: 인권 침해 보고서 데이터셋

**저자**: Constantinos Djouvas; Nikandros Ioannides; Iosif Kovras; Christos Christodoulou
**출처**: Data in Brief, Vol.66, pp.112854-112854
**발행일**: 2026-05-15
**DOI**: https://doi.org/10.1016/j.dib.2026.112854

## 한국어 요약

**연구질문**: 문서 단위 요약 수준에 그치던 기존 데이터의 한계를 극복하고, 주요 글로벌 인권단체들의 날 것 그대로의 원본 텍스트를 문단 수준으로 분석 가능한 대규모 전처리 데이터셋으로 어떻게 구축 및 보급할 것인가?

**방법론**:
- 국제사면위원회(Amnesty International), 휴먼라이츠워치(HRW), 미국 국무부, 강제실종실무그룹(WGEID)의 1999~2023년 발간 인권 보고서 수집
- PDF 파싱, 웹 크롤링 기법과 함께 LLM 기반 오탈자 자동 교정(캐릭터 레벨 에러율을 8.3%에서 1.7%로 경감) 파이프라인 가동
- 문단 단위 분할 후 개체명 인식(NER), 감성 분석, 텍스트 분류, 카테고리 필터링 등의 NLP 정보 보강을 수행해 832,220개 문단 코퍼스 및 23개 메타데이터 필드 설계

**주요 결과**:
- 전 세계 인권 실태 문서를 국가-연도 식별자와 호환되는 고품질 문단 코퍼스로 규격화하여 학계에 배포함
- 각 기구들이 지난 25년간 인권 침해 사건을 묘사하고 분석하는 톤앤매너와 주요 관심사 변화의 정교한 비교 연구를 지원할 수 있는 핵심 리소스를 확보함


## 초록 (원문)

Human rights research increasingly employs computational text analysis, but existing datasets provide either document-level aggregations or event-level extractions from news sources, limiting fine-grained analysis of primary organizational reports. We present the Human Rights Violation Reporting Dataset, a comprehensive paragraph-level corpus comprising reports from Amnesty International, Human Rights Watch, the US State Department, and the Working Group on Enforced or Involuntary Disappearances, spanning 1999-2023. The dataset contains 832,220 paragraphs processed using a custom pipeline combining PDF extraction, custom crawlers, language model-based text correction (reducing character-level errors from 8.3% to 1.7%), and comprehensive natural language processing (NLP) enrichment, including named entity recognition, sentiment analysis, text classification, and content moderation. Each paragraph is enriched with 23 metadata fields enabling entity network analysis, topic modelling, cross-organizational comparison, and machine learning applications. Data are provided in comma-separated values (CSV) format, with standardized country-year identifiers compatible with existing political science datasets. This dataset enables previously impossible fine-grained computational analysis of how major human rights organizations document violations across time, space, and organizational contexts.

## 키워드

Metadata, Paragraph, Identifier, Pipeline (software), Human rights, Named-entity recognition, Word (group theory), Amnesty

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

