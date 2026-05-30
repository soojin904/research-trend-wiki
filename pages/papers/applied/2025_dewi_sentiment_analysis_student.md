---
title: "Sentiment Analysis of Student Comments on Facilities and Infrastructure at Instiki Using Retrieval Augmented Generation"
authors: ['Ni Putu Juliana Dewi', 'I Kadek Dwi Gandika Supartha', 'I Gusti Agung Indrawan', 'Ketut Jaya Atmaja']
year: 2025
venue: "Indonesian Journal of Data and Science"
tags: ['Sentiment Analysis and Opinion Mining', 'Edcuational Technology Systems', 'Data Mining and Machine Learning Applications']
source: raw/applied/applied_2025_Sentiment_Analysis_of_Stu_ijodas_v6i3_377.md
---

# Sentiment Analysis of Student Comments on Facilities and Infrastructure at Instiki Using Retrieval Augmented Generation

**제목(한글)**: 검색 증강 생성(RAG)을 활용한 Instiki 시설·인프라에 대한 학생 의견의 감성 분석

## 한국어 요약

**연구질문**: RAG(Retrieval Augmented Generation) 방법론과 대형 언어 모델(LLM)을 활용하여 인도네시아어 학생 시설 의견에 대한 감성 분석을 자동화할 수 있으며, 어떤 모델이 가장 높은 정확도를 보이는가?

**방법론**:
- RAG(검색 증강 생성) 방식과 어휘 기반(Lexicon-Based) 데이터 레이블링 결합
- 세 가지 LLM 비교: IndoBERT(indobenchmark/indobert-base-p1), TinyLlama-1.1B, Indonesian RoBERTa 감성 분류기
- 인도네시아 비즈니스기술대(INSTIKI) 2024년 학생 의견 데이터 활용
- 2회의 테스트 세션으로 모델 안정성 평가

**주요 결과**:
- IndoBERT가 두 세션 모두 80% 정확도로 최고 성능 달성
- TinyLlama는 세션 1에서 60%, 세션 2에서 65%로 소폭 개선
- Indonesian RoBERTa는 두 세션 모두 60% 정확도 기록
- 인도네시아어 이해 수준이 감성 예측 결과에 직접적 영향을 미침을 확인

**저자**: Ni Putu Juliana Dewi; I Kadek Dwi Gandika Supartha; I Gusti Agung Indrawan; Ketut Jaya Atmaja
**출처**: Indonesian Journal of Data and Science, Vol.6, pp.575-587
**발행일**: 2025-12-31
**DOI**: https://doi.org/10.56705/ijodas.v6i3.377

## 초록 (원문)

This research was conducted to analyze the sentiment of student comments on infrastructure facilities at the Indonesian Institute of Business and Technology (INSTIKI) to overcome the problem of comment analysis that was previously done manually. The data used is in the form of student comments in 2024. The method used in this study is Retrieval Augmented Generation (RAG) with data labeling using Lexicon-Based. The test was carried out on three Large Language Models (LLMs), namely indobenchmark/indobert-base-p1, TinyLlama/TinyLlama-1.1B-Chat-v1.0, and w11wo/indonesian-roberta-base-sentiment-classifier. The test results showed that the indobenchmark/indobert-base-p1 model produced the highest accuracy of 80% in both test sessions compared to other models. The TinyLlama/TinyLlama-1.1B-Chat-v1.0 model produced 60% accuracy in session 1 and 65% in session 2, while the w11wo/indonesian-roberta-base-sentiment-classifier model produced 60% accuracy in both test sessions. The difference in the performance of these three LLMs shows that the model's understanding of Indonesian can affect the results of sentiment predictions.

## 키워드

Session (web analytics), Test (biology), Indonesian, Sentiment analysis, Test data, Training set

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

