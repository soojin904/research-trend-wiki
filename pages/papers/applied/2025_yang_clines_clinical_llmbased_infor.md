---
title: "CLINES: Clinical LLM-based Information Extraction and Structuring Agent"
authors: ['Zongxin Yang', 'Hongyi Yuan', 'Raheel Sayeed', 'Amelia Li Min Tan', 'Enci Cai', 'Michele Moro', 'Xiudi Li', 'Huaiyuan Ying', 'Nicholas Brown', 'Griffin M. Weber', 'Sheng Yu', 'Isaac S. Kohane', 'Tianxi Cai']
year: 2025
venue: "medRxiv"
tags: ['Topic Modeling', 'Biomedical Text Mining and Ontologies', 'Machine Learning in Healthcare']
source: raw/applied/applied_2025_CLINES_Clinical_LLMbased__2025_12_01_25341355.md
---

# CLINES: Clinical LLM-based Information Extraction and Structuring Agent

**제목(한글)**: CLINES: 임상 LLM 기반 정보 추출 및 구조화 에이전트

## 한국어 요약

**연구질문**: 전자의무기록(EHR) 임상 내러티브에서 수동 차트 리뷰를 대체할 수 있는 고품질 자동화 정보 추출 시스템을 어떻게 구현하며, 기존 방법 대비 개체 추출·단언 상태·수치 추출·날짜 처리 정확도를 어느 수준으로 향상할 수 있는가?

**방법론**:
- 의미 기반 청킹, 추론 가능 대형 언어 모델에 의한 추출, 속성 부여(단언/경험자, 단위 포함 수치), UMLS 정규화, 날짜 해석, i2b2 스타일 스키마로의 집계를 포함한 모듈형 에이전트 파이프라인 CLINES 개발
- MIMIC-III, 4CE, CORAL 종양학 보고서(유방암·췌장암)로 제로샷 평가

**주요 결과**:
- CLINES가 모든 데이터셋에서 규칙/어휘 시스템, 트랜스포머 인코더, 단일 프롬프트 LLM 기준선을 능가하며, 최강 단일 프롬프트 LLM 대비 +0.21~0.38 F1 향상
- 노트 길이가 증가해도 성능이 안정적으로 유지되어 대규모 코호트 구축 및 실세계 증거 생성에 실용적 적용 가능성을 입증

**저자**: Zongxin Yang; Hongyi Yuan; Raheel Sayeed; Amelia Li Min Tan; Enci Cai; Michele Moro; Xiudi Li; Huaiyuan Ying; Nicholas Brown; Griffin M. Weber; Sheng Yu; Isaac S. Kohane; Tianxi Cai
**출처**: medRxiv, Vol.None
**발행일**: 2025-12-02
**DOI**: https://doi.org/10.64898/2025.12.01.25341355

## 초록 (원문)

Abstract Background Clinical narratives in electronic health records (EHRs) contain essential diagnostic, therapeutic, and temporal information that is often missing from structured fields, leaving manual chart review as the de facto standard for high-quality labels, but slow, costly, and variable, thereby constraining accurate cohort construction for clinical trials, large-scale epidemiologic studies, and the development of robust machine-learning models. Methods We developed CLINES, a modular agentic pipeline that extracts and structures clinical concepts: semantic chunking of long notes; extraction by reasoningcapable large language models; assignment of attributes (assertion/experiencer, numerical values with SI units); normalization to the Unified Medical Language System (UMLS); resolution of explicit and relative dates; and aggregation into an i2b2-style schema. Zero-shot evaluation was conducted on de-identified EHR: MIMIC-III notes, 4CE notes, and CORAL oncology reports (breast, pancreas). Comparators included rule/lexicon systems, transformer encoders, and single-prompt LLM baselines. Outcomes were F1 scores for entity extraction, assertion status, value&amp;unit extraction, and date processing. Findings Across all datasets, CLINES led every baseline. F1 scores (entity / assertion / value&amp;unit / date) were: MIMIC-III 0.69 / 0.93 / 0.90 (date not evaluated); 4CE 0.87 / 0.88 / 0.79 / 0.79; CORAL–Breast 0.81 / 0.84 / 0.77 / 0.73; CORAL–Pancreas 0.85 / 0.87 / 0.90 / 0.78. Gains over the strongest single-prompt LLM were +0.21–0.38 across tasks, and transformer encoders trailed by +0.28–0.68 F1 on entity extraction. Performance remained stable across note-length quantiles, while transformer baselines lost recall as notes lengthened. Interpretation CLINES translates narrative text from electronic health records into ontology-grounded, auditable, and schema-ready data, offering a practical route to scale chart-review-like extraction for cohort discovery and real-world evidence. CLINES is model agnostic–different open and close models can be substituted to achieve specific cost, performance, and privacy goals. Future work aims to quantify inter-annotator agreements and explore adaptive feedback and domain-specific fine-tuning.

## 키워드

Transformer, Assertion, Modular design, Electronic health record, Medical record, Recall, Normalization (sociology), Inference

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

