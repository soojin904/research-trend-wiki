---
title: "Build and Query Indexes of Clinical Documents with Easy-to-Reuse Pipelines"
authors: ['Félix Berthou', 'Ghilsain Vaillant', 'Bastien Rance', 'Adrien Coulet']
year: 2026
venue: "Studies in health technology and informatics"
tags: ['Biomedical Text Mining and Ontologies', 'Topic Modeling', 'Electronic Health Records Systems']
source: raw/applied/applied_2026_Build_and_Query_Indexes_o_shti260325.md
---

# Build and Query Indexes of Clinical Documents with Easy-to-Reuse Pipelines
**제목(한글)**: 재사용이 용이한 파이프라인을 활용한 임상 문서 색인 구축 및 조회

**저자**: Félix Berthou; Ghilsain Vaillant; Bastien Rance; Adrien Coulet
**출처**: Studies in health technology and informatics, Vol.336, pp.979-983
**발행일**: 2026-05-21
**DOI**: https://doi.org/10.3233/shti260325

## 한국어 요약

**연구질문**: 의료 연구에서 재활용하기 힘든 단발성 업무에 그쳤던 전자의무기록(EHR) 내 비정형 임상 텍스트의 질병 징후 및 치료 관찰 정보 추출을 영구적이고 재활용 가능하게 구조화하는 방법은 무엇인가?

**방법론**:
- 텍스트 입력 수집, 개체명 인식, OMOP 의료 표준 어휘 변환, 그리고 개념/문서별 양방향 인덱스 구축을 단일화한 파이썬 기반 오픈소스 파이프라인 'medkit Seshat' 개발
- 검색, 텍스트 요약 및 데이터 내보내기가 연동되는 유연한 웹 사용자 인터페이스(UI) 설계

**주요 결과**:
- 임상 실무의 표현형 규정 캠페인에서 생성된 비정형 데이터 결과물을 차기 연구에서도 유연하게 재사용 및 전이할 수 있는 표준 색인 자동화 체계를 정립


## 초록 (원문)

Electronic Health Records are a central source of healthcare data, containing structured data alongside unstructured clinical texts. The latter capture detailed reasoning, observations, treatment plans and clinical evolutions, which are crucial for phenotyping, and real-world evidence generation. Natural language processing enables the extraction, thus the subsequent use, of these crucial elements; however, these extractions remain one-off, study-specific efforts. This is detrimental as the extracted elements could be valuable for future research. We present medkit Seshat, an open-source Python pipeline that: (1) ingests free text, (2) recognizes relevant entities, (3) normalizes them with OMOP vocabularies, (4) builds an index that can either be searched by concept or by document. In addition, we share a flexible web UI to illustrate the interest of built indexes in terms of search, text analysis and export. Seshat aims at facilitating the reuse and adaptation of this prototypical pipeline to various purposes, with the main objective of enabling the secondary use of results of phenotyping campaigns.

## 키워드

Pipeline (software), Reuse, Python (programming language), Adaptation (eye), Pipeline transport, Health records

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

