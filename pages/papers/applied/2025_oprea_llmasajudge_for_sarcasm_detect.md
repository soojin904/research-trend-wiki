---
title: "LLM-as-a-judge for sarcasm detection using supervised fine-tuning of transformers"
authors: ['Simona‐Vasilica Oprea', 'Adela Bârã']
year: 2025
venue: "Journal of King Saud University - Computer and Information Sciences"
tags: ['Sentiment Analysis and Opinion Mining', 'Topic Modeling', 'Language, Metaphor, and Cognition']
source: raw/applied/applied_2025_LLMasajudge_for_sarcasm_d_s44443_025_00379_7.md
---

# LLM-as-a-judge for sarcasm detection using supervised fine-tuning of transformers

**제목(한글)**: 변환기(Transformer)의 지도 미세조정을 활용한 풍자 탐지 LLM-as-a-judge 프레임워크

## 한국어 요약

**연구질문**: 대형 사전학습 언어모델(LLM)을 미세조정하면 다양한 도메인에서 풍자(sarcasm) 및 반어(irony)를 효과적으로 탐지할 수 있는가?

**방법론**:
- 두 가지 오픈소스 데이터셋(뉴스 헤드라인, 제품 리뷰) 활용
- RoBERTa-large, RoBERTa-base, DistilBERT-base-uncased, DistilBERT-SST2 네 가지 트랜스포머 모델 미세조정
- 그룹 인식 데이터 분할(group-aware data splits), 레이블 스무딩(label smoothing), 매크로 F1 기반 조기종료 적용

**주요 결과**:
- DistilBERT-SST2가 가장 안정적인 성능 달성 (Macro F1 = 0.8784)
- 영화·일반·제품/서비스/기술 등 5개 도메인에 걸쳐 강인한 일반화 능력 확인
- 해석 가능하고 재현 가능한 풍자 탐지 기준선(baseline) 제공

**저자**: Simona‐Vasilica Oprea; Adela Bârã
**출처**: Journal of King Saud University - Computer and Information Sciences, Vol.37
**발행일**: 2025-12-01
**DOI**: https://doi.org/10.1007/s44443-025-00379-7

## 초록 (원문)

This research conducts a systematic comparative study of large pre-trained language models (LLMs) for sarcasm and irony detection. While pretrained transformers often struggle to capture sarcastic intent, we fine-tune multiple domain-specific models and assess their adaptability across diverse review contexts. Using two complementary open-source datasets, news headlines and product reviews, we evaluate four transformer-based models (RoBERTa-large, RoBERTa-base, DistilBERT-base-uncased, and DistilBERT-SST2) under consistent experimental conditions. The framework emphasizes algorithmic transparency, reproducibility and structured evaluation through group-aware data splits, label smoothing and macro-F1-based early stopping. Results indicate that DistilBERT-SST2 achieves the strongest and most stable performance (macro F1 = 0.8784) and demonstrates resilience across five distinct review domains (movies, general, product/service/tech). The research provides an interpretable and reproducible baseline for evaluating fine-tuned LLMs in sarcasm detection and identifies key patterns of domain sensitivity and transfer.

## 키워드

Sarcasm, Adaptability, Transformer, Irony, Smoothing, Closeness

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

