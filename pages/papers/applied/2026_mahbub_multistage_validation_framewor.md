---
title: "A Multi-Stage Validation Framework for Trustworthy Large-scale Clinical Information Extraction using Large Language Models"
authors: ['Maria Mahbub', 'Gregory M. Dams', 'Josh A. Arnold', 'Caitlin Rizy', 'Sudarshan Srinivasan', 'Elliot M. Fielstein', 'Minu A. Aghevli', 'Kamonica Craig', 'Elizabeth M. Oliva', 'Joseph Erdos', 'Jodie Trafton', 'Ioana Danciu']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Topic Modeling', 'Biomedical Text Mining and Ontologies', 'Machine Learning in Healthcare']
source: raw/applied/applied_2026_A_MultiStage_Validation_F_nodoi.md
---

# A Multi-Stage Validation Framework for Trustworthy Large-scale Clinical Information Extraction using Large Language Models

**제목(한글)**: 대규모 언어 모델을 활용한 신뢰할 수 있는 대규모 임상 정보 추출을 위한 다단계 검증 프레임워크

## 한국어 요약

**연구질문**: 대규모 언어 모델(LLM)을 사용하여 비정형 건강 기록에서 임상적으로 의미 있는 정보를 추출하는 신뢰할 수 있고 확장 가능한 검증 접근 방식의 부재를 해결하기 위한 다단계 검증 프레임워크를 제안한다.

**방법론**:
- 프롬프트 교정, 규칙 기반 타당성 필터링, 의미론적 기반 평가, 독립적인 고성능 심사 LLM을 사용한 표적 확증 평가, 선별적 전문가 검토 및 외부 예측 타당성 분석을 통합한다.
- 불확실성을 정량화하고 광범위한 수동 주석 없이 오류 모드를 특성화한다.
- 919,783개의 임상 기록에서 11개 물질 범주에 걸쳐 물질 사용 장애(SUD) 진단을 추출하는 데 이 프레임워크를 적용한다.

**주요 결과**:
- 규칙 기반 필터링 및 의미론적 기반은 지원되지 않거나, 관련 없거나, 구조적으로 불가능한 LLM 긍정 추출의 14.59%를 제거한다.
- 높은 불확실성 사례의 경우, 심사 LLM의 평가가 주제 전문가 검토와 상당한 일치(Gwet의 AC1=0.80)를 보였다.
- 심사 평가된 출력을 참조로 사용하여 기본 LLM은 완화된 매칭 기준에서 F1 점수 0.80을 달성했다.
- LLM 추출 SUD 진단은 구조화된 데이터 기준선보다 이후 SUD 전문 치료 참여를 더 정확하게 예측했다(AUC=0.80).
- 이러한 결과는 주석 집약적인 평가 없이도 LLM 기반 임상 정보 추출의 확장 가능하고 신뢰할 수 있는 배포가 가능함을 보여준다.

**저자**: Maria Mahbub; Gregory M. Dams; Josh A. Arnold; Caitlin Rizy; Sudarshan Srinivasan; Elliot M. Fielstein; Minu A. Aghevli; Kamonica Craig; Elizabeth M. Oliva; Joseph Erdos; Jodie Trafton; Ioana Danciu
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-04-07
**DOI**: 

## 초록 (원문)

Large language models (LLMs) show promise for extracting clinically meaningful information from unstructured health records, yet their translation into real-world settings is constrained by the lack of scalable and trustworthy validation approaches. Conventional evaluation methods rely heavily on annotation-intensive reference standards or incomplete structured data, limiting feasibility at population scale. We propose a multi-stage validation framework for LLM-based clinical information extraction that enables rigorous assessment under weak supervision. The framework integrates prompt calibration, rule-based plausibility filtering, semantic grounding assessment, targeted confirmatory evaluation using an independent higher-capacity judge LLM, selective expert review, and external predictive validity analysis to quantify uncertainty and characterize error modes without exhaustive manual annotation. We applied this framework to extraction of substance use disorder (SUD) diagnoses across 11 substance categories from 919,783 clinical notes. Rule-based filtering and semantic grounding removed 14.59% of LLM-positive extractions that were unsupported, irrelevant, or structurally implausible. For high-uncertainty cases, the judge LLM's assessments showed substantial agreement with subject matter expert review (Gwet's AC1=0.80). Using judge-evaluated outputs as references, the primary LLM achieved an F1 score of 0.80 under relaxed matching criteria. LLM-extracted SUD diagnoses also predicted subsequent engagement in SUD specialty care more accurately than structured-data baselines (AUC=0.80). These findings demonstrate that scalable, trustworthy deployment of LLM-based clinical information extraction is feasible without annotation-intensive evaluation.

## 키워드

Medical diagnosis, Matching (statistics), Subject-matter expert, Scalability, Information extraction, Comparability, Population, Trustworthiness

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

