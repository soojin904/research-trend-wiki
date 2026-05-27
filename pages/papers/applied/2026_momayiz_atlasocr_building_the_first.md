---
title: "AtlasOCR: Building the First Open-Source Darija OCR Model with Vision Language Models"
authors: ['Imane Momayiz', 'Soufiane Ait Elaouad', 'Abdeljalil Elmajjodi', 'Haitame Bouanane']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Handwritten Text Recognition Techniques', 'Multimodal Machine Learning Applications', 'Topic Modeling']
source: raw/applied/applied_2026_AtlasOCR_Building_the_Fir_nodoi.md
---

# AtlasOCR: Building the First Open-Source Darija OCR Model with Vision Language Models

**제목(한글)**: AtlasOCR: 비전 언어 모델을 활용한 최초의 오픈소스 다리자어(모로코 아랍 방언) OCR 모델 구축

## 한국어 요약

**연구질문**: 자원이 극히 부족한 모로코 아랍 방언(Darija)을 위한 특화 OCR 시스템이 전무한 상황에서, 대규모 비전 언어 모델(VLM)을 파인튜닝하여 공개 배포 가능한 최초의 Darija OCR 모델을 어떻게 구축할 수 있는가?

**방법론**:
- 합성 데이터 생성 라이브러리(OCRSmith)와 실제 세계 데이터를 결합하여 Darija 특화 학습 데이터셋 구축
- 파라미터 효율적 학습을 위해 QLoRA와 Unsloth를 활용한 Qwen2.5-VL 3B 모델(30억 파라미터) 파인튜닝
- 주요 하이퍼파라미터 최적화를 위한 체계적 어블레이션(Ablation) 연구 수행

**주요 결과**:
- 자체 구축한 AtlasOCRBench 및 기존의 KITAB-Bench 평가에서 최첨단(State-of-the-art) 성능을 달성하여 더 큰 규모의 모델들과 동등한 경쟁력을 입증함
- 표준 아랍어와 Darija 방언 양쪽에서의 강력한 범용성(Generalization)을 검증함

**저자**: Imane Momayiz; Soufiane Ait Elaouad; Abdeljalil Elmajjodi; Haitame Bouanane
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-04-09
**DOI**: 

## 초록 (원문)

Darija, the Moroccan Arabic dialect, is rich in visual content yet lacks specialized Optical Character Recognition (OCR) tools. This paper introduces AtlasOCR, the first open-source Darija OCR model built by fine-tuning a 3B parameter Vision Language Model (VLM). We detail our comprehensive approach, from curating a unique Darija-specific dataset leveraging both synthetic generation with our OCRSmith library and carefully sourced real-world data, to implementing efficient fine-tuning strategies. We utilize QLoRA and Unsloth for parameter-efficient training of Qwen2.5-VL 3B and present comprehensive ablation studies optimizing key hyperparameters. Our evaluation on the newly curated AtlasOCRBench and the established KITAB-Bench demonstrates state-of-the-art performance, challenging larger models and highlighting AtlasOCR's robustness and generalization capabilities for both Darija and standard Arabic OCR tasks.

## 키워드

Robustness (evolution), Optical character recognition, Character recognition, Arabic, Language model, Key (lock), Generalization, Text recognition

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

