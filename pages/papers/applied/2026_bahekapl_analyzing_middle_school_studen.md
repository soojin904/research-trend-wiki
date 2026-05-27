---
title: "Analyzing Middle School Students’ Distance Education Experiences in COVID-19 via Sentiment Analysis and Topic Modeling"
authors: ['Ekrem Bahçekapılı', 'Bülent Kandemir', 'Elif Baykal Kablan']
year: 2026
venue: "The International Review of Research in Open and Distributed Learning"
tags: ['Online Learning and Analytics', 'Computational and Text Analysis Methods', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Analyzing_Middle_School_S_irrodl_v27i1_8920.md
---

# Analyzing Middle School Students’ Distance Education Experiences in COVID-19 via Sentiment Analysis and Topic Modeling
**제목(한글)**: 감성 분석 및 토픽 모델링을 통한 COVID-19 상황 하의 중학생들의 원격 교육 경험 분석

**저자**: Ekrem Bahçekapılı; Bülent Kandemir; Elif Baykal Kablan
**출처**: The International Review of Research in Open and Distributed Learning, Vol.27, pp.107-129
**발행일**: 2026-02-10
**DOI**: https://doi.org/10.19173/irrodl.v27i1.8920

## 한국어 요약

**연구질문**: 코로나 대유행기 긴급 원격 수업을 경험한 터키 중학생들의 주관적인 만족과 불안 요인을 대규모 자연어 처리를 통해 어떻게 분류하고 정량화할 수 있는가?

**방법론**:
- 9~15세 터키 학생 2,739명의 서술형 설문 응답 텍스트 활용
- TF-IDF, Word2Vec, FastText 텍스트 표현과 5가지 지도 분류 알고리즘을 융합한 반지도 학습 감성 모델 구축 (최적 조합: TF-IDF + SVM)
- LDA 토픽 모델링으로 6개 핵심 테마 추출

**주요 결과**:
- TF-IDF + SVM 모델이 F1-스코어 0.85로 긍정 1,867건과 부정 2,542건을 판별하며 학생들이 전반적으로 원격 교육에 비판적이었음을 실증
- 긍정 요인은 학습 시간 유연성 및 자율 학습 배양이 주를 이룬 반면, 부정 요인은 스크린 피로도와 구조적 소통 불평등이 높게 나타나 균형 잡힌 미래 디지털 커리큘럼 설계 기반을 마련


## 초록 (원문)

This study investigated middle school students’ experiences with emergency remote education during the COVID-19 pandemic using natural language processing (NLP), sentiment analysis, and topic modeling techniques. A total of 2,739 valid responses from Turkish students (ages 9–15) were collected through open-ended survey questions regarding the perceived advantages and disadvantages of distance learning. Sentiment classification was performed using a semi-supervised machine learning approach, combining TF-IDF, Word2Vec, and FastText vectorization with five classification algorithms. The TF-IDF + support vector machines (SVM) combination yielded the highest performance (F1 = 0.85). Results show a total of 1,867 positive and 2,542 negative opinions, indicating that students generally adopted a more critical view of distance education. To explore the thematic structure of opinions, topic modeling was applied with six topics. Positive sentiments clustered around themes such as educational continuity, health protection, time savings, flexible scheduling, self-regulated learning, and digital literacy. Negative sentiments were dominated by themes including limited interaction, screen fatigue, perceived low quality, technical barriers, and structural inequalities. Findings suggest that while students appreciated the safety and flexibility of remote learning, they also faced significant pedagogical, physical, and technological challenges. The study contributes methodologically by demonstrating the effectiveness of AI-based text analysis and offers practical implications for designing more equitable and student-centered digital education models. These results underscore the importance of integrating NLP and machine learning tools into educational research to uncover deeper insights from student-generated content at scale.

## 키워드

Sentiment analysis, Distance education, Turkish, Thematic analysis, Flexibility (engineering), Topic model, Vectorization (mathematics), Educational technology

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

