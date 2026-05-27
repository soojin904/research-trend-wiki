---
title: "Sentiment aware interactive Chatbot AI using multi agent processing model"
authors: ['Vinod Kumar Shukla', 'Sumithra Alagarsamy', 'Vijaylakshmi Nagarajan', 'Gavaskar Shanmugam']
year: 2026
venue: "IAES International Journal of Robotics and Automation (IJRA)"
tags: ['AI in Service Interactions', 'Sentiment Analysis and Opinion Mining', 'Stock Market Forecasting Methods']
source: raw/applied/applied_2026_Sentiment_aware_interacti_ijra_v15i1_pp200_209.md
---

# Sentiment aware interactive Chatbot AI using multi agent processing model
**제목(한글)**: 다중 에이전트 처리 모델을 활용한 감성 인지형 대화형 챗봇 AI

**저자**: Vinod Kumar Shukla; Sumithra Alagarsamy; Vijaylakshmi Nagarajan; Gavaskar Shanmugam
**출처**: IAES International Journal of Robotics and Automation (IJRA), Vol.15, pp.200-200
**발행일**: 2026-03-01
**DOI**: https://doi.org/10.11591/ijra.v15i1.pp200-209

## 한국어 요약

**연구질문**: 소셜 미디어와 이커머스에서 브랜드-소비자 대화 시, 사용자의 미묘하고 중의적인 감성 상태를 실시간 분석하여 최적의 응답을 제공하는 감성 인지형 챗봇(IChat-AI)을 어떻게 개발할 수 있는가?

**방법론**:
- 대화 텍스트 데이터로부터 특징을 추출하기 위해 W2V(Word2Vec), TF-IDF 및 BoW 어휘 가중치 추출 병행 적용
- 감성을 5가지 등급(슬픔, 기쁨, 중립, 분노, 공포)으로 나누어 분류하고 예측하기 위해 크로네커 신경망(DKNN) 아키텍처 학습
- 정확도, Precision, Recall, 실행 속도 및 복잡도 지표를 기준으로 기존 RoBERTa 등 단독 모델들과 비교 실험

**주요 결과**:
- 제안한 IChat-AI 기법이 RoBERTa 대비 5.33%, MMTF-DES 모델 대비 14.39% 높은 감성 분류 정확도를 보임을 확인
- 실시간 사용자 감성에 따라 적절한 톤의 대답을 선택하는 멀티 에이전트 제어 시스템의 응답 속도 및 확장성을 검증함


## 초록 (원문)

Understanding user sentiment has become more important for organizations and consumers due to the rapid growth of social media platforms such as marketplaces, platforms for connecting brands and consumers, and public discussion platforms. Emotions that are based on aspects, nuanced within context, and multifaceted often require complex sentiment analysis algorithms to interpret properly. Furthermore, these systems do not provide real-time information to help companies make better decisions and enhance consumer satisfaction. To tackle these challenges, a novel Interactive Chatbot artificial intelligence (IChat-AI) approach has been proposed in this paper for sentiment-aware chatbot interaction. The word to vector (W2V), term frequency-inverse document frequency (TF-IDF), and bag of words (BoW) are utilized to effectively extract essential features. The deep Kronecker neural network (DKNN) is utilized to predict and classify the emotions into five classes, such as sad, happy, neutral, angry, and fearful. Python has been used to simulate the suggested model. The efficacy of the suggested system is examined employing parameters including recall, execution time, F1-score, complexity, precision, scalability, accuracy, and response time. The developed IChat-AI strategy performs better regarding accuracy than the existing methods, including RoBERTa, TLSA, and multimodal transformers fusion for desire, emotion, and SA (MMTF-DES) approaches, by 5.33%, 4.73%, and 14.39%.

## 키워드

Chatbot, Sentiment analysis, Python (programming language), Social media, Artificial neural network, Question answering

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

