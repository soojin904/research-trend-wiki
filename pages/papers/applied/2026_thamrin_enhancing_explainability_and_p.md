---
title: "Enhancing explainability and performance of the depression detection model on social media utilizing feature engineering and LLMs"
authors: ['Syauki Aulia Thamrin', 'Arbee L. P. Chen']
year: 2026
venue: "Health Information Science and Systems"
tags: ['Mental Health via Writing', 'Sentiment Analysis and Opinion Mining', 'Digital Mental Health Interventions']
source: raw/applied/applied_2026_Enhancing_explainability__s13755_026_00446_x.md
---

# Enhancing explainability and performance of the depression detection model on social media utilizing feature engineering and LLMs
**제목(한글)**: 피처 엔지니어링 및 LLM을 활용한 소셜 미디어 상의 우울증 감지 모델의 설명가능성 및 성능 향상

**저자**: Syauki Aulia Thamrin; Arbee L. P. Chen
**출처**: Health Information Science and Systems, Vol.14, pp.48-48
**발행일**: 2026-03-23
**DOI**: https://doi.org/10.1007/s13755-026-00446-x

## 한국어 요약

**연구질문**: 소셜 미디어 게시글을 이용한 종래의 우울증 분류 모델이 지닌 설명력 한계를 극복하고, 환자의 감정 기복 추이를 인지하기 쉬운 진단 징후 설명문 형태로 제시할 수 있는가?

**방법론**:
- 포스팅 전후 일정 기간 동안의 감정 흐름을 모니터링하기 위해 12가지 감정 상태 특징을 정량 산출하는 시계열 피처 엔지니어링 적용
- 텍스트 언어 특징을 추출하는 단어 임베딩 기법과 게시글 간 중요도를 찾는 어텐션 메커니즘 순차 모델 훈련
- 정신건강 도메인 데이터로 fine-tuning된 LLM을 결합하여, 추출된 감정 변화 상태와 정신의학적 우울증 특징 진단을 상호 연계 서술하는 융합 설명 생성기 설계

**주요 결과**:
- 단순히 우울 여부를 이진 분류하는 데 그치지 않고, 사용자의 세부 감정 상태 변동과 정신 의학 징후를 이해하기 쉬운 보고서 텍스트 형태로 설명하는 고도화된 진단 설명 기능을 확보함


## 초록 (원문)

Depression is a mental disorder that negatively affects many people worldwide. The traditional method to help diagnose depression is through questionnaires, and better diagnoses can be obtained by consulting psychiatrists. Because the methods are time-consuming, researchers search for a way to efficiently and effectively diagnose depression before it is too late. Social media data is then utilized for detecting depression since people tend to express their feelings on social media. Different deep learning methods have been proposed for detecting depression on social media. However, the explainability regarding the classification result is limited to identifying negative emotions from the words in the posts. In this research, we aim to enhance the explainability and performance of the depression detection model by utilizing feature engineering and Large Language Models (LLMs). For feature engineering, we compute emotional status, which consists of twelve features representing emotion not just for each post but also before and after the post for some period of time. We also consider language used in the post by using different word embedding models. Different sequence models are also explored, and an attention mechanism is used to help identify the most important posts. The emotional status of the important posts and the classification result are then input to the LLM to describe and relate the emotional status to the characteristics of depression. Based on our experiment, fine-tuning LLM using mental health-related data did help the LLM to produce better explainability by relating easier-understood emotional status to specific characteristics of depression.

## 키워드

Depression (economics), Feeling, Feature (linguistics), Social media, Feature engineering, Word embedding, Mental health, Feature extraction

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

