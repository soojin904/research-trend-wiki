---
title: "TheraMind: a multi-LLM ensemble for accelerating drug repurposing in lung cancer via case report mining"
authors: ['Vrushket More', 'Lyra Lu', 'Zeyu Ding', 'Zhaohan Xi', 'Seth Mizia', 'Nancy Lan Guo']
year: 2026
venue: "npj Precision Oncology"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Biomedical Text Mining and Ontologies']
source: raw/applied/applied_2026_TheraMind_a_multiLLM_ense_s41698_025_01265_1.md
---

# TheraMind: a multi-LLM ensemble for accelerating drug repurposing in lung cancer via case report mining
**제목(한글)**: TheraMind: 임상 증례 보고서 마이닝을 통한 폐암 약물 재창출 가속화를 위한 다중 LLM 앙상블 시스템

**저자**: Vrushket More; Lyra Lu; Zeyu Ding; Zhaohan Xi; Seth Mizia; Nancy Lan Guo
**출처**: npj Precision Oncology, Vol.10
**발행일**: 2026-01-29
**DOI**: https://doi.org/10.1038/s41698-025-01265-1

## 한국어 요약

**연구질문**: 방대한 의학 문헌 내 흩어져 있는 비정형 임상 증례 보고서(Clinical Case Reports)에서 폐암 치료제 후보 물질 관련 실증 데이터를 효율적으로 추출할 고성능 자동화 프레임워크는 무엇인가?

**방법론**:
- 비소세포폐암(NSCLC) 관련 10,023건의 PubMed 증례 보고서 대상 18종 후보 약물 정합성 추출
- GPT-4o-mini, Gemini-2.0-Flash, LLaMA-3-8B를 결합한 다수결(majority-vote) 앙상블 기법 설계
- 진단명, 투약, 투약 중단 및 치료 결과로 구성된 구조화 질문 프롬프트 적용

**주요 결과**:
- 세 가지 모델의 다수결 앙상블을 적용했을 때 재현율(Recall) 92% 및 특이도(Specificity) 99.7%의 극대화된 임상 데이터 식별 성능을 확보함
- 방대하고 복잡한 비정형 의료 논문에서 약물 재창출 연구용 실제 데이터(RWE)를 추출할 수 있는 신뢰성 높은 인프라를 성공적으로 정립함


## 초록 (원문)

Published clinical case reports are a valuable yet underutilized source of evidence for drug repurposing. However, systematically identifying relevant reports remains a challenge due to the volume of literature and the diversity of candidate compounds. We present TheraMind, an AI system that leverages large language models (LLMs) to automate the identification and analysis of case reports supporting potential drug repurposing for non-small cell lung cancer (NSCLC). Our system screened 10,023 PubMed-indexed case reports across 18 candidate drugs using coordinated data extraction and standardized four-question prompts assessing diagnosis, drug administration, discontinuation, and clinical outcomes. We employed three evaluation strategies, rule-based classifiers, single-model validators, and a majority-vote ensemble integrating GPT-40-mini, Gemini-2.0-Flash, and LLaMA-3-8B. The ensemble approach achieved 92% recall and 99.7% specificity in detecting clinically relevant reports. Structured outputs included patient demographics, therapeutic responses, and case summaries. This LLM-driven framework offers a scalable approach to accelerate drug repurposing by mining real-world evidence from unstructured clinical literature.

## 키워드

Drug repositioning, Repurposing, Drug, Lung cancer, Identification (biology), Scalability, Ensemble learning, DrugBank

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

