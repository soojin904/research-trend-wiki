---
title: "250. Artificial intelligence–driven real-time detection of anxiety symptoms among college students: a campus social media text analysis approach"
authors: ['Xiaofei Wu']
year: 2026
venue: "Schizophrenia Bulletin"
tags: ['Mental Health via Writing', 'Sentiment Analysis and Opinion Mining', 'Digital Mental Health Interventions']
source: raw/applied/applied_2026_250_Artificial_intelligen_sbag003_248.md
---

# 250. Artificial intelligence–driven real-time detection of anxiety symptoms among college students: a campus social media text analysis approach
**제목(한글)**: 인공지능 기반 대학생 불안 증상의 실시간 탐지: 학내 소셜 미디어 텍스트 분석 접근법

**저자**: Xiaofei Wu
**출처**: Schizophrenia Bulletin, Vol.52, pp.S170-S171
**발행일**: 2026-02-01
**DOI**: https://doi.org/10.1093/schbul/sbag003.248

## 한국어 요약

**연구질문**: 학내 익명 소셜 미디어에 작성된 텍스트 데이터와 표준화된 불안 척도(GAD-7)를 결합하여 대학생의 불안 수준을 실시간으로 추정하고 모니터링할 수 있는 AI 프레임워크를 구축할 수 있는가?

**방법론**:
- 12개월간 축적된 학내 소셜 플랫폼의 텍스트 데이터 수집 및 참여자 대상 표준 범불안장애 척도(GAD-7) 설문 매핑
- GAD-7 점수를 반영한 감성 태깅 코퍼스 구축 및 감정 사전 기능을 내장한 사전 훈련된 언어 모델(PLM) 기반 판별 모델 구축
- 시간 슬라이딩 윈도우 및 준실시간 처리 기법을 이용한 시계열 흐름 감시

**주요 결과**:
- 테스트 세트에서 고불안 대학생에 대한 분류 정확도 0.88, 재현율 0.85, F1-Score 0.86을 달성하였으며 GAD-7 점수와 통계적 상관계수 r=0.72의 높은 양의 상관 관계 확인
- 학기말 기말고사 기간에 불안 유발 텍스트 비중이 학기 중 대비 약 55% 증가하는 등 시계열 패턴을 실시간 포착하는 데 성공
- 대학 내 수동적인 상담 신청 시스템을 보완하여 적극적이고 낮은 부담의 공공 보건 예방적 개입 시스템 가능성 제언


## 초록 (원문)

Abstract Background With the popularity of college social media platforms, the emotional expression of college students on campus social media has become an important external representation of their psychological state. The incidence of anxiety among college students is relatively high, and traditional screening methods that rely on self-assessment scales or interviews have shortcomings in real-time and continuous monitoring. Despite the continuous development of artificial intelligence (AI) in text emotion recognition and mental health monitoring, relevant research still lacks empirical analysis of campus situations combined with standardized psychological scales. Based on this, the research integrates AI text analysis and standardized anxiety scales to construct a detection framework that can support real-time recognition and dynamic warning of anxiety emotions among college students, aiming to provide technical support for psychological health monitoring and public health intervention in universities. Methods The study collected anonymous text data from a campus social platform of a certain university within 12 months, and synchronously organized participants to fill out the Generalized Anxiety Disorder Scale (GAD-7) to quantify anxiety levels. After cleaning, segmenting, and feature filtering the text data, a standardized corpus is constructed, and sentiment annotation is performed on some texts based on GAD-7 scores to form a training dataset. Subsequently, a pre trained language model was used for text feature representation, and an anxiety emotion discrimination model was constructed by integrating emotion dictionary features. Finally, through a time sliding window mechanism and near real-time data processing strategy, the model output was quickly responsive and dynamically updated to support real-time continuous detection of anxiety emotions among college students. Results The research findings indicate a high degree of consistency between the model and the GAD-7 scale evaluation results. In the test set, the model achieved a recognition accuracy of 0.88 for individuals with high anxiety, a recall rate of 0.85, and an F1 score of 0.86. The text anxiety score predicted by the model is significantly positively correlated with the total score of GAD-7 (r = 0.72). Stratified analysis found that students with moderate or above GAD-7 scores had a significantly higher proportion of high anxiety texts compared to the low group, and the difference was statistically significant. The time series results show that the proportion of high anxiety texts in the final exam stage has increased by about 55% compared to the middle of the semester, and the model output trend is consistent with. Discussion Research indicates that combining AI-based text analysis with standardized scales enables real-time detection and early warning of anxiety among college students without relying on active reporting, providing a low-burden, high-coverage auxiliary tool for mental health management in universities. This approach helps identify high-risk periods and groups, facilitating a shift from passive response to proactive intervention in psychological services. Future efforts could expand multi-school sample validation and intervention effect tracking to enhance the model's applicability and service value within actual public health systems.

## 키워드

Anxiety, Popularity, Construct (python library), Social anxiety, Mental health, Social media, Fear of negative evaluation, Feature (linguistics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

