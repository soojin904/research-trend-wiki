---
title: "Financial Sentiment Analysis with Large Language Models"
authors: ['Xinyu Cheng']
year: 2025
venue: "Finance & Economics"
tags: ['Stock Market Forecasting Methods', 'Sentiment Analysis and Opinion Mining', 'Machine Learning in Healthcare']
source: raw/applied/applied_2025_Financial_Sentiment_Analy_gvntfv56.md
---

# Financial Sentiment Analysis with Large Language Models

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

