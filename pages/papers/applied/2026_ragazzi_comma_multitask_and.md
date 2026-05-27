---
title: "Comma: A multi-task and multi-lingual dataset of constitutional verdicts"
authors: ['Luca Ragazzi', 'Giacomo Frisoni', 'Gianluca Moro', 'Paolo Italiani', 'Lorenzo Molfetta', 'Veronika Folin']
year: 2026
venue: "Artificial Intelligence and Law"
tags: ['Artificial Intelligence in Law', 'Legal Language and Interpretation', 'Topic Modeling']
source: raw/applied/applied_2026_Comma_A_multitask_and_mul_s10506_026_09520_x.md
---

# Comma: A multi-task and multi-lingual dataset of constitutional verdicts
**제목(한글)**: Comma: 헌법 판결문 다중 태스크 및 다국어 데이터셋

**저자**: Luca Ragazzi; Giacomo Frisoni; Gianluca Moro; Paolo Italiani; Lorenzo Molfetta; Veronika Folin
**출처**: Artificial Intelligence and Law, Vol.None
**발행일**: 2026-05-05
**DOI**: https://doi.org/10.1007/s10506-026-09520-x

## 한국어 요약

**연구질문**: 영미법이 아닌 비대륙법계(이탈리아) 사법 환경에서 고도의 전문 용어와 긴 호흡을 특징으로 하는 헌법 판결문을 전산 분석할 대규모 법률 다국어 벤치마크는 어떻게 구축하고 평가하는가?

**방법론**:
- 이탈리아 공화국 헌법재판소의 14,000건의 판결문으로 데이터셋 구축
- 4개 주요 언어(영어, 이탈리아어 등)로 확장하고 다단계 요약, 판결문 생성, 법조문 검색, 판결 분류의 4대 법률 NLP 태스크 설계
- 최신 대형 언어 모델들을 퓨샷 및 풀파인튜닝 조건 하에서 벤치마킹 분석

**주요 결과**:
- 제안된 Comma 벤치마크를 통해 판결 판독률을 측정하여 법률 특화 NLP의 성능 향상 여지가 매우 큼을 검증함
- 코드를 오픈소스로 공개하여 영미법 중심주의 법률 AI의 한계를 다변화하는 사법 공학의 기틀을 다짐


## 초록 (원문)

Abstract Transformer-based language models have sparked a revolutionary change in Legal NLP, endowing lawyers with unparalleled tools to effectively navigate, understand, and draft large volumes of text. However, the dearth of large-scale datasets from authoritative sources hampers further progress. The available resources are primarily single-task, English-only, and written in layman’s terms. To bridge this gap, we introduce Comma , a multi-task and multi-lingual archive of 14K verdicts drawn from the Constitutional Court of the Italian Republic, grounded in a non-common law system. Documents in Comma diverge from ordinary legal manuscripts as they address fundamental principles and rights, involve technical jargon, exhibit an articulated structure, are diachronic, have extended length, and demand more significant expertise and interpretation. By embracing 4 widespread languages, Comma tackles a panoply of necessity-driven tasks: multi-granular abstractive summarization, decision generation, article retrieval, and ruling classification. We systematically benchmark a catalog of language models in both few-shot and full settings, uncovering substantial headroom for improvement. We contribute to the new era of Legal NLP systems by openly releasing Comma and best-performing models (https://github.com/disi-unibo-nlp/comma).

## 키워드

Legal aspects of computing, Philosophy of law, Computational linguistics, Legal history, Constitutional law, Bridge (graph theory), Legal research

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

