---
title: "LegalBench-BR: A Benchmark for Evaluating Large Language Models on Brazilian Legal Decision Classification"
authors: ['Pedro Barbosa de Carvalho Neto']
year: 2026
venue: "ArXiv.org"
tags: ['Artificial Intelligence in Law', 'Topic Modeling', 'Legal Language and Interpretation']
source: raw/applied/applied_2026_LegalBenchBR_A_Benchmark__zenodo_19298367.md
---

# LegalBench-BR: A Benchmark for Evaluating Large Language Models on Brazilian Legal Decision Classification

**제목(한글)**: LegalBench-BR: 브라질 법률 판결 분류에 대한 대형 언어 모델 평가 벤치마크

## 한국어 요약

**연구질문**: 브라질 법률 텍스트 분류 과제에서 대형 언어 모델(LLM)들의 성능을 객관적으로 평가할 수 있는 공개 벤치마크가 전무한 상황에서, 실용적이고 신뢰성 있는 평가 데이터셋을 어떻게 구축할 수 있는가?

**방법론**:
- DataJud API(CNJ)를 통해 산타카타리나 주 법원(TJSC)에서 3,105건의 항소 사건 수집
- LLM 보조 레이블링과 휴리스틱 검증을 결합한 5개 법률 영역 어노테이션 수행
- 클래스 균형 테스트셋에서 BERTimbau-LoRA, Claude 3.5 Haiku, GPT-4o mini 등 주요 모델 성능 비교

**주요 결과**:
- BERTimbau-LoRA 모델이 정확도 87.6%, 매크로 F1 0.87을 달성하여 Claude 3.5 Haiku 대비 22%p, GPT-4o mini 대비 28%p 우월한 성능을 보임
- 브라질 포르투갈어 법률 특화 모델이 범용 LLM보다 도메인 특화 분류 과제에서 월등함을 입증함

**저자**: Pedro Barbosa de Carvalho Neto
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-03-28
**DOI**: https://doi.org/10.5281/zenodo.19298367

## 초록 (원문)

We introduce LegalBench-BR, the first public benchmark for evaluating language models on Brazilian legal text classification. The dataset comprises 3,105 appellate proceedings from the Santa Catarina State Court (TJSC), collected via the DataJud API (CNJ) and annotated across five legal areas through LLM-assisted labeling with heuristic validation. On a class-balanced test set, BERTimbau-LoRA achieves 87.6% accuracy and 0.87 F1 macro (+22pp over Claude 3.5 Haiku, +28pp over GPT-4o mini).

## 키워드

Benchmark (surveying), Heuristic, Language model, Macro, State (computer science), Test (biology)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

