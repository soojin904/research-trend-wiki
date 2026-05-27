---
title: "A Movie Recommendation Model Integrating Viewer’s Emotional Experience and TV Feature Extraction"
authors: ['Harmanjeet Singh', 'Chander Prabha', 'Preeti Sharma', 'Balamurugan Balusamy', 'Ahmad Alkhayyat', 'Nithya Rekha Sivakumar']
year: 2026
venue: "Lecture notes in electrical engineering"
tags: ['Sentiment Analysis and Opinion Mining', 'Emotion and Mood Recognition', 'Recommender Systems and Techniques']
source: raw/applied/applied_2026_A_Movie_Recommendation_Mo_978_981_95_5136_1_13.md
---

# A Movie Recommendation Model Integrating Viewer’s Emotional Experience and TV Feature Extraction
**제목(한글)**: 시청자의 감정 경험 및 TV 특징 추출을 결합한 영화 추천 모델

**저자**: Harmanjeet Singh; Chander Prabha; Preeti Sharma; Balamurugan Balusamy; Ahmad Alkhayyat; Nithya Rekha Sivakumar
**출처**: Lecture notes in electrical engineering, Vol.None, pp.131-139
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1007/978-981-95-5136-1_13

## 한국어 요약

**연구질문**: 시청자 피드백의 질적 정보를 효율적으로 추천 서비스에 연동하기 위해 IMDB 리뷰, 넷플릭스 평점, 유튜브 트레일러 반응 및 트위터 대화 데이터를 통합한 하이브리드 추천 알고리즘의 성능은 어떠한가?

**방법론**:
- IMDB, Netflix, YouTube 댓글, Twitter 포스팅 데이터를 수집하여 통합 사용자 프로필 구축
- 트위터 활동 기반 사회적 영향력 점수를 가중치로 융합한 협업 필터링 및 콘텐츠 기반 필터링 하이브리드 추천 모델 설계
- 영화 리뷰 감성을 이진(긍정/부정) 분류하여 추천 리스트를 고도화하기 위해 BERT 임베딩, BiLSTM, BiGRU(Self-attention 적용) 및 CNN 조합 모델 학습 수행

**주요 결과**:
- 제안하는 융합 하이브리드 모델이 테스트 정확도 93.91% 및 AUC 0.9831을 달성하여 단순 감성 분석 기반 추천기 성능을 크게 상회
- 대량의 시각 반응 및 댓글 텍스트 피드백을 실시간으로 수용하여 시청자 맞춤형 정밀 추천 랭킹을 산출할 수 있음을 검증함


## 초록 (원문)

Abstract Acceptance of information-gathering behaviours, especially from the viewpoints of others, is crucial for enhancing decision-making processes. In film critiques, audience feedback offers significant insights regarding a movie’s quality and value as a time investment. The growing volume of review data requires automation for effective processing. This study introduces the creation of a sophisticated movie recommendation engine that amalgamates many data sources, such as IMDB movie reviews, Netflix ratings, YouTube trailer interactions, and Twitter discourse. User-generated input, including comments, likes, tweets, and trailer replies, is integrated to improve the recommendation process. The suggested methodology utilizes collaborative and content-based filtering, integrating users’ social influence as assessed through their Twitter activity and social characteristics. A hybrid recommendation method produces an initial array of film recommendations. Thereafter, sentiment analysis is utilized to enhance and improve the recommendations. The system employs artificial intelligence methodologies, utilizing the IMDB dataset to train and validate a BERT embedding layer alongside a Bi-Directional Long Short-Term Memory (LSTM), a Bi-Directional Gated Recurrent Unit (GRU) incorporating a self-attention mechanism, and a Convolutional Neural Network (CNN). The model attained a testing accuracy of 93.91% and an AUC of 0.9831, indicating exceptional performance in binary sentiment categorization relative to current methodologies.

## 키워드

Social media, Convolutional neural network, Sentiment analysis, Viewpoints, Recommender system, Categorization, Quality (philosophy), Feature extraction

## 위키 연관

- [[pages/concepts/personal_network|퍼스널 네트워크]]

## 메모

