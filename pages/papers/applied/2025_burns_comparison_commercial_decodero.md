---
title: "Comparison of commercial decoder-only large language models for multilingual sentiment analysis of short text"
authors: ['John W. Burns', 'Tom Kelsey']
year: 2025
venue: "Journal of Social Media Research"
tags: ['Sentiment Analysis and Opinion Mining', 'Topic Modeling', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2025_Comparison_of_commercial__jsomer_38.md
---

# Comparison of commercial decoder-only large language models for multilingual sentiment analysis of short text
**제목(한글)**: 다국어 단문 감성 분석을 위한 상용 디코더 전용 대형 언어 모델 비교

## 한국어 요약

**연구질문**: 상용 디코더 전용 LLM(ChatGPT, Claude, Gemini)이 다국어 단문 감성 분석에서 원문 그대로 처리하는 것과 영어로 번역 후 처리하는 것 중 어느 방식이 더 효과적인가?

**방법론**:
- 7개 언어(영어, 스페인어, 프랑스어, 포르투갈어, 아랍어, 일본어, 한국어) 단문 1,000개 샘플 수집
- Google Translate를 이용한 영어 번역 후 비교 실험
- 디코더 전용 LLM(ChatGPT, Claude, Gemini) 및 인코더 전용 LLM, RNN, 어휘사전(lexicon) 방식 비교

**주요 결과**:
- 디코더 전용 LLM은 원문 언어 처리 시 모든 감성 분석 방법 중 최고 정확도 달성
- 프랑스어는 예외로, RNN이 가장 높은 정확도 기록
- ChatGPT가 7개 언어 중 4개에서 최고 정확도, Claude는 2개, Gemini는 6개 언어에서 2위

**저자**: John W. Burns; Tom Kelsey
**출처**: Journal of Social Media Research, Vol.2, pp.319-331
**발행일**: 2025-12-04
**DOI**: https://doi.org/10.29329/jsomer.38

## 초록 (원문)

This article explores multilingual sentiment analysis of short texts using three commercial decoder-only Large Language Models (“LLMs” ): OpenAI’s ChatGPT, Anthropic’s Claude, and Google’s Gemini. The training data for these models is approximately 90% English, and it remains an open question whether it is better to evaluate text data in its original language or translate it into English first. We build on previous research on sentiment analysis of multilingual short texts, such as those found on social media, using 1000 short text samples in seven languages (English, Spanish, French, Portuguese, Arabic, Japanese, and Korean) translated into English using Google Translate. We processed these samples with decoder-only LLMs and compared their results with those from other methods (encoder-only LLMs, RNNs, lexicons). We found that decoder-only LLMs achieved the highest accuracy across all sentiment analysis methods when working with the original language data. The only exception was with the French data, where an RNN was the most accurate. Among the three decoder-only LLMs, ChatGPT had the highest accuracy in four of the seven languages, Claude in two, and Gemini, which ranked second in six of the seven languages.

## 키워드

Sentiment analysis, Language model, Training set, Computational linguistics, English language

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

