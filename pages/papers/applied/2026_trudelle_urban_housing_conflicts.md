---
title: "Urban Housing Conflicts in Large Canadian Cities: A Spatio-Temporal and Semantic Analysis Using Large Language Models"
authors: ['Catherine Trudelle', 'Christophe Claramunt', 'Eliott Libner', 'Rodolphe Gonzalès']
year: 2026
venue: "ISPRS International Journal of Geo-Information"
tags: ['Urban Planning and Governance', 'Urbanization and City Planning', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_Urban_Housing_Conflicts_i_ijgi15050193.md
---

# Urban Housing Conflicts in Large Canadian Cities: A Spatio-Temporal and Semantic Analysis Using Large Language Models
**제목(한글)**: 캐나다 대도시의 도시 주거 갈등: 거대 언어 모델을 활용한 시공간 및 의미론적 분석

**저자**: Catherine Trudelle; Christophe Claramunt; Eliott Libner; Rodolphe Gonzalès
**출처**: ISPRS International Journal of Geo-Information, Vol.15, pp.193-193
**발행일**: 2026-05-01
**DOI**: https://doi.org/10.3390/ijgi15050193

## 한국어 요약

**연구질문**: 캐나다 8대 대도시(토론토, 밴쿠버, 퀘벡 등)에서 지난 20년간 누적된 복잡한 비정형 도시 주거 갈등(Housing Conflicts)의 위치, 시기, 의미론적 발생 양상을 AI를 통해 편향 없이 정밀 추출할 수 있는가?

**방법론**:
- municipal 리포트, 미디어 아카이브, NGO 보고서 등 다양한 텍스트 채널에서 주거 갈등 서술 텍스트 수집
- 프롬프트 변조 및 이단계 보정(Calibration) 절차가 결합된 LLM 기반 텍스트 추출/분류 워크플로우 설계
- 1,000건 이상의 갈등 사례에 대해 공간적 위치, 발생 시점, 의미론적 특징 라벨 자동 매핑

**주요 결과**:
- LLM을 활용한 정보 추출 파이프라인이 출력의 획일성(Homogenization) 문제를 방어하면서 도시별 갈등 특징을 정상 분류해냄을 입증
- 분석 결과 2020년 이후 주거비 상승에 따른 갈등 강도가 크게 증가했음을 정량화하여 주거 정책 입안자들에게 가이드라인을 제공함


## 초록 (원문)

This paper introduces a comparative analysis of urban housing conflicts across eight major Canadian cities, Toronto, Vancouver, Québec, Ottawa, Calgary, Edmonton, St. John’s, and Halifax, over a 20-year period. Using Large Language Models (LLMs), we implement a structured workflow to extract, classify, and organize more than one thousand conflict instances from diverse textual sources, including municipal reports, media archives, and non-governmental organization publications. The methodological contribution lies in demonstrating how an LLM-assisted pipeline, combining schema-based extraction, prompt perturbation, and a two-phase calibration procedure, can generate structured, multi-city conflict datasets while addressing challenges such as output homogenization and sensitivity to prompt design. The findings highlight both shared national tendencies and city-specific configurations with post-2020 conflicts intensifying. Overall, the study proposes a transparent workflow for applying LLMs to conflict-related text analysis and offers an exploratory overview of the spatial, temporal, and semantic regularities of housing conflicts in Canadian cities.

## 키워드

Workflow, Exploratory analysis, Semantics (computer science), Semantic analysis (machine learning), Discourse analysis

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

