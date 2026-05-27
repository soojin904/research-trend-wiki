---
title: "Automated Structuring and Analysis of Unstructured Equipment Maintenance Text Data in Manufacturing Using Generative AI Models: A Comparative Study of Pre-Trained Language Models"
authors: ['Yongju Cho']
year: 2026
venue: "Applied Sciences"
tags: ['Digital Transformation in Industry', 'Computational and Text Analysis Methods', 'BIM and Construction Integration']
source: raw/applied/applied_2026_Automated_Structuring_and_app16041969.md
---

# Automated Structuring and Analysis of Unstructured Equipment Maintenance Text Data in Manufacturing Using Generative AI Models: A Comparative Study of Pre-Trained Language Models
**제목(한글)**: 생성형 AI 모델을 활용한 제조업 내 비정형 설비 유지보수 텍스트 데이터의 자동 구조화 및 분석: 사전 학습 언어 모델 비교 연구

**저자**: Yongju Cho
**출처**: Applied Sciences, Vol.16, pp.1969-1969
**발행일**: 2026-02-16
**DOI**: https://doi.org/10.3390/app16041969

## 한국어 요약

**연구질문**: 대규모 인프라 투자나 고가의 가동 센서 추가 없이, 제조 공정 관리 시스템(MES) 내 비정형 텍스트 일지로부터 고장 부품, 고장 유형, 조치 사항 등의 구조화된 데이터를 정밀 추출하는 실용적인 LLM 기반 프레임워크는 어떻게 구축하는가?

**방법론**:
- 국내 대형 자동차 부품 기업의 MES 텍스트 데이터 29,736건을 가공하고, GPT-4와 도메인 전문가 검수를 거쳐 골드 데이터셋 구축
- BART(KoBART), T5(pko-t5-base), 그리고 Qwen 모델을 사용하여 고장 부품, 고장 유형, 고장 조치 등의 구조화 정보 추출 능력 파이팅 튜닝 및 평가
- 정밀도, 재현율, F1-Score, Exact Match, ROUGE 지표를 통해 세 모델의 다중 필드 정보 추출 성능 비교 및 웹 기반 분석 시각화 플랫폼 구축

**주요 결과**:
- Qwen 기반의 추출 모델이 BART 및 T5 모델 대비 전 분야에서 월등히 안정적이고 정확한 구조화 성능을 입증함
- 정형화된 데이터를 기반으로 시계열 분석, 상관 분석, 이상 징후 탐지 등이 가능한 웹 대시보드를 생성하여 설비 예지 보전(Predictive Maintenance) 의사결정을 실무적으로 지원할 수 있음을 검증함


## 초록 (원문)

Manufacturing companies face significant challenges in leveraging artificial intelligence for equipment management due to high infrastructure costs and limited availability of labeled data for failures. While most manufacturing AI applications focus on structured sensor data, vast amounts of unstructured textual information containing valuable maintenance knowledge remain underutilized. This study presents a practical generative AI-based framework for structured information extraction that automatically converts unstructured equipment maintenance texts into predefined semantic fields to support predictive maintenance in manufacturing environments. We adopted and evaluated three representative generative models—Bidirectional and Auto-Regressive Transformers (BART) with KoBART, Text-to-Text Transfer Transformer (T5) with pko-t5-base, and the large language model Qwen—to generate structured outputs by extracting three predefined fields: failed components, failure types, and corrective actions. The framework enables the structuring of equipment management text data from Manufacturing Execution Systems (MES) to build predictive maintenance support systems. We validated the approach using a large-scale MES dataset consisting of 29,736 equipment maintenance records from a major automotive parts manufacturer, from which curated subsets were used for model training and evaluation. Our methodology employs Generative Pre-trained Transformer 4 (GPT-4) for initial dataset construction, followed by domain expert validation to ensure data quality. The trained models achieved promising performance when evaluated using extraction-aligned metrics, including exact match (EM) and token-level precision, recall, and F1-score, which directly assess field-level extraction correctness. ROUGE scores are additionally reported as a supplementary indicator of lexical overlap. Among the evaluated models, Qwen consistently outperformed BART and T5 across all extracted fields. The structured outputs are further processed through domain-specific dictionaries and regular expressions to create a comprehensive analytical database supporting predictive maintenance strategies. We implemented a web-based analytics platform enabling time-series analysis, correlation analysis, frequency analysis, and anomaly detection for equipment maintenance optimization. The proposed system converts tacit knowledge embedded in maintenance texts into explicit, actionable insights without requiring additional sensor installations or infrastructure investments. This research contributes to the manufacturing AI field by demonstrating a comprehensive application of generative language models to equipment maintenance text analysis, providing a cost-effective approach for digital transformation in manufacturing environments. The framework’s scalability and cloud-based deployment model present significant opportunities for widespread adoption in the manufacturing sector, supporting the transition from reactive to predictive maintenance strategies.

## 키워드

Transformer, Structuring, Generative grammar, Predictive maintenance, Unstructured data, Maintenance engineering, Generative model, Information model

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

