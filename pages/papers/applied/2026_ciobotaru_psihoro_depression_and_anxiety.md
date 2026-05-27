---
title: "PsihoRo: Depression and Anxiety Romanian Text Corpus"
authors: ['Alexandra Ciobotaru', 'Ana-Maria Bucur', 'Liviu P. Dinu']
year: 2026
venue: "Open MIND"
tags: ['Mental Health via Writing', 'Sentiment Analysis and Opinion Mining', 'Digital Mental Health Interventions']
source: raw/applied/applied_2026_PsihoRo_Depression_and_An_arxiv_2602_18324.md
---

# PsihoRo: Depression and Anxiety Romanian Text Corpus
**제목(한글)**: PsihoRo: 루마니아어 우울증 및 불안 텍스트 코퍼스

**저자**: Alexandra Ciobotaru; Ana-Maria Bucur; Liviu P. Dinu
**출처**: Open MIND, Vol.None
**발행일**: 2026-02-20
**DOI**: https://doi.org/10.48550/arxiv.2602.18324

## 한국어 요약

**연구질문**: 루마니아어로 작성된 오픈소스 정신 건강 관련 자연어 코퍼스가 부재한 상황에서, 어떻게 편향되지 않은 고품질 루마니아어 우울증 및 불안 분석 코퍼스를 구축하고 모델링할 것인가?

**방법론**:
- 205명의 루마니아인 응답자를 대상으로 6개의 개방형 질문 및 표준 척도인 PHQ-9, GAD-7 설문을 조합하여 데이터 수집
- 구축된 PsihoRo 데이터셋에 대하여 루마니아어 LIWC, 감정 분석, 통계적 피처 추출 및 토픽 모델링 기법을 적용하여 언어적 패턴 규명

**주요 결과**:
- 루마니아어권 최초의 오픈소스 정신 건강 데이터셋을 구축하여 HuggingFace에 공개함
- 텍스트 분석 결과, 심각한 우울 및 불안 상태를 겪는 응답자군과 비우울군 간의 고유한 통계적 감정 단어 사용 경향 및 테마적 성향 차이를 규명함


## 초록 (원문)

Psychological corpora in NLP are collections of texts used to analyze human psychology, emotions, and mental health. These texts allow researchers to study psychological constructs, identify patterns related to mental health problems and analyze emotional language. However, collecting accurate mental health data from social media can be challenging due to the assumptions made by data collectors. A more effective approach involves gathering data through open-ended questions and then assessing participants' mental health status using self-report screening surveys. This method was successfully employed for English, a language with a lot of psychological NLP resources. However, the same cannot be stated for Romanian, which currently has no open-source mental health corpus. To address this gap, we have collected the first open-source corpus focused on depression and anxiety in Romanian, by utilizing a form with 6 open-ended questions along with the standardized PHQ-9 and GAD-7 screening questionnaires. Although the PsihoRo corpus contains texts from only 205 respondents, it represents an important first step toward understanding and analyzing mental health issues within the Romanian population. We employ statistical analysis, text analysis using Romanian LIWC, emotion detection, and topic modeling to identify the most important features of this newly introduced resource for the NLP community. The data is publicly available at https://huggingface.co/datasets/Alegzandra/PsihoRo.

## 키워드

Romanian, Mental health, Anxiety, Depression (economics), Resource (disambiguation)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

