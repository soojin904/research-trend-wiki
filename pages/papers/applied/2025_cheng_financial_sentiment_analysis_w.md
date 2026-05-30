---
title: "Financial Sentiment Analysis with Large Language Models"
authors: ['Xinyu Cheng']
year: 2025
venue: "Finance & Economics"
tags: ['Stock Market Forecasting Methods', 'Sentiment Analysis and Opinion Mining', 'Machine Learning in Healthcare']
source: raw/applied/applied_2025_Financial_Sentiment_Analy_gvntfv56.md
---

# Financial Sentiment Analysis with Large Language Models
**제목(한글)**: 대형 언어 모델을 활용한 금융 감성 분석

## 한국어 요약

**연구질문**: 파라미터 효율적 파인튜닝(LoRA, QLoRA)을 적용한 LLM이 금융 특화 모델 FinBERT보다 금융 텍스트 감성 분석에서 더 높은 성능을 낼 수 있는가?

**방법론**:
- Llama-3.1-8B 및 Qwen-3-8B 모델에 LoRA·QLoRA 파인튜닝 적용
- Financial PhraseBank 및 FiQA-SA 데이터셋으로 평가
- FinBERT와 성능 비교

**주요 결과**:
- LLM이 FinBERT 대비 일관되게 높은 성능: PhraseBank에서 최대 88.9% 정확도
- LoRA는 소수 클래스에서 우수한 성능, QLoRA는 메모리 절감과 유사 정확도 유지
- Qwen-3은 MoE(Mixture-of-Experts) 구조 덕분에 노이즈 많은 마이크로블로그에서 Llama-3.1 능가

**저자**: Xinyu Cheng
**출처**: Finance & Economics, Vol.1
**발행일**: 2025-12-19
**DOI**: https://doi.org/10.61173/gvntfv56

## 초록 (원문)

Financial sentiment analysis is vital for applications such as market prediction and risk management. While domain-specific models like (Financial Bidirectional Encoder Representations from Transformers) FinBERT are widely used, their limited scalability constrains performance across diverse financial texts. This paper investigates the effectiveness of large language models (LLMs) with parameter-efficient fine-tuning strategies. We fine-tune Llama-3.1-8B and Owen-3-8B using LoRA and QLoRA, and evaluate them on Financial PhraseBank and FiOASA datasets. Experiments show that LLMs consistently outperform FinBERT, achieving up to 88.9% accuracy on PhraseBank and 81.7% accuracy with 0.74 macro-Fl on FiQA-SA LoRA yields stronger performance, especially on minority classes, while QLoRA maintains comparable accuracy with significantly reduced memory cost. Moreover, Qwen-3 outperforms Llama-3.1 on noisy microblogs, benefiting from its Mixture-of-Experts (MoE) architecture, which enhances efficiency and diversity through conditional computation. These findings confirm that parameter-efficient fine-tuned LLMs provide both accuracy and efficiency, and represent strong alternatives to domain-specific models in financial sentiment analysis.

## 키워드

Financial market, Scalability, Diversity (politics), Encoder, Language model, Sentiment analysis, Predictive modelling

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

