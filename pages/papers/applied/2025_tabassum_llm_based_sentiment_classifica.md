---
title: "LLM Based Sentiment Classification from Bangladesh E-Commerce Reviews"
authors: ['Sumaiya Tabassum']
year: 2025
venue: ""
tags: ['Sentiment Analysis and Opinion Mining', 'Spam and Phishing Detection', 'Text and Document Classification Technologies']
source: raw/applied/applied_2025_LLM_Based_Sentiment_Class_iccit68739_2025_11491094.md
---

# LLM Based Sentiment Classification from Bangladesh E-Commerce Reviews

**제목(한글)**: LLM 기반 방글라데시 전자상거래 리뷰 감성 분류

## 한국어 요약

**연구질문**: 본 연구는 방글라데시 전자상거래 리뷰에 대한 감성 분석을 위해 트랜스포머(transformer) 기반 BERT 모델 및 기타 대규모 언어 모델(LLM)의 활용 가능성을 탐구한다.

**방법론**:
- 방글라데시 전자상거래 리뷰 원본 데이터셋에서 벵골어 및 영어 고객 리뷰 4000개 샘플을 추출하여 모델 미세 조정(fine-tuning)에 활용함.
- Llama-3.1-8B, Phi-3.5-mini-instruct, Mistral-7B-v0.1, DistilBERT-multilingual, mBERT, XLM-R-base 등 다양한 LLM 및 BERT 기반 모델을 미세 조정함.
- LoRA 및 PEFT와 같은 파라미터 효율적인 미세 조정 기법을 사용하여 계산 오버헤드(computational overhead)를 줄이고 자원 제약적인 환경에 적합하도록 함.

**주요 결과**:
- 미세 조정된 Llama-3.1-8B 모델이 다른 미세 조정 모델(Phi-3.5-mini-instruct, Mistral-7B-v0.1, DistilBERT-multilingual, mBERT, XLM-R-base)보다 우수한 성능을 보였으며, 종합 정확도(accuracy) 95.5%, 정밀도(precision) 93%, 재현율(recall) 88%, F1 점수 90%를 기록함.
- 본 연구는 LLM이 저자원 언어(low-resource languages)의 감성 분석 발전에 기여할 수 있음을 보여줌.

**저자**: Sumaiya Tabassum
**출처**: , Vol.None, pp.281-286
**발행일**: 2025-12-19
**DOI**: https://doi.org/10.1109/iccit68739.2025.11491094

## 초록 (원문)

Sentiment analysis is an essential part of text analysis, which is a larger field that includes determining and evaluating the author's emotional state. This method is essential since it makes it easier to comprehend consumers' feelings, viewpoints, and preferences holistically. The introduction of large language models (LLMs), such as Llama, has greatly increased the availability of cutting-edge model applications, such as sentiment analysis. However, accurate sentiment analysis is hampered by the intricacy of written language and the diversity of languages used in evaluations. The viability of using transformer-based BERT models and other LLMs for sentiment analysis from Bangladesh ecommerce reviews is investigated in this paper. A subset of 4000 samples from the original dataset of Bangla and English customer reviews was utilized to fine-tune the model. The finetuned Llama-3.1-8B model outperformed other fine-tuned models, including Phi-3.5-mini-instruct, Mistral-7B-v0.1, DistilBERT-multilingual, mBERT, and XLM-R-base, with an overall accuracy, precision, recall, and <tex xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">$\mathbf{F 1}$</tex> score of 95.5%, <tex xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">$93 \%, 88 \%, 90 {\%}$</tex>. The study emphasizes how parameterefficient fine-tuning methods (LoRA and PEFT) can lower computational overhead and make it appropriate for contexts with limited resources. The results show how LLMs can help advance sentiment analysis for low-resource languages.

## 키워드

Bengali, Sentiment analysis, Field (mathematics), Diversity (politics), Language model, Overhead (engineering)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

