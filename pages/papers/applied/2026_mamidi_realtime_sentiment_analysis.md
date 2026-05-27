---

title: "Real-Time Sentiment Analysis of YouTube Comments using Ensemble Deep Learning and VADER Models"

authors: ['Komal Mayukha Mamidi']

year: 2026

venue: "International Journal for Research in Applied Science and Engineering Technology"

tags: ['Sentiment Analysis and Opinion Mining', 'Text and Document Classification Technologies', 'Spam and Phishing Detection']

source: raw/applied/applied_2026_RealTime_Sentiment_Analys_ijraset_2026_81799.md

---



# Real-Time Sentiment Analysis of YouTube Comments using Ensemble Deep Learning and VADER Models
**제목(한글)**: 앙상블 딥러닝 및 VADER 모델을 활용한 유튜브 댓글의 실시간 감성 분석



**저자**: Komal Mayukha Mamidi

**출처**: International Journal for Research in Applied Science and Engineering Technology, Vol.14, pp.713-718

**발행일**: 2026-05-09

**DOI**: https://doi.org/10.22214/ijraset.2026.81799



## 한국어 요약

**연구질문**: 실시간으로 쏟아지는 대용량 유튜브 댓글 및 라이브 채팅 텍스트의 감성을 정확하고 빠르게 5단계로 자동 분류할 수 있는 앙상블 딥러닝 시스템을 어떻게 구축할 것인가?

**방법론**:
- 규칙 기반의 VADER 사전식 분석과 사전학습 RoBERTa 모델의 분류 신뢰도를 결합하는 Flask 기반 실시간 앙상블 분석 파이프라인을 구축
- 최대 10만 건의 세션 댓글 데이터로 성능을 테스트함

**주요 결과**:
- 규칙 엔진(VADER)과 맥락 분류기(RoBERTa)의 상호 보완을 통해 단일 모델 대비 감성 분류 정확도를 유의미하게 향상시킴
- 워드클라우드 시각화 기능과 비개발자용 대시보드를 안정적으로 제공함


## 초록 (원문)



This paper presents a hybrid ensemble system for real-time sentiment analysis of YouTube comments, integrating VADER lexicon-based analysis with RoBERTa transformer-based deep learning. The proposed web application leverages the YouTube Data API v3 to process up to 100,000 comments per session, including live stream chat, and classifies sentiments into five categories: Very Positive, Positive, Neutral, Negative, and Very Negative. The ensemble model prioritizes VADER compound scores with RoBERTa confidence as a contextual fallback, improving classification accuracy over single-model baselines. Results demonstrate robust sentiment distribution analysis with comprehensive visualizations including pie charts and word clouds, making the tool practical for content creators, platform analysts, and brand monitoring. The Flask-based interface provides accessibility for non-technical users, bridging the gap between NLP research and real-world social media analysis



## 키워드



Sentiment analysis, Bridging (networking), Deep learning, Social media, Ensemble forecasting, Ensemble learning



## 위키 연관



- [[pages/concepts/social_network_analysis|SNA]]



## 메모

