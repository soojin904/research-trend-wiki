---
title: "Automatic Analysis of Political Discourse: A Comparative Study of Multilingual and Large Language Models"
authors: ['Ayaulym Sairanbekova']
year: 2026
venue: "Journal of Applied Data Sciences"
tags: ['Computational and Text Analysis Methods', 'Sentiment Analysis and Opinion Mining', 'Topic Modeling']
source: raw/applied/applied_2026_Automatic_Analysis_of_Pol_jads_v7i2_1118.md
---

# Automatic Analysis of Political Discourse: A Comparative Study of Multilingual and Large Language Models
**제목(한글)**: 정치적 담론의 자동 분석: 다국어 모델 및 대형 언어 모델의 비교 연구

**저자**: Ayaulym Sairanbekova
**출처**: Journal of Applied Data Sciences, Vol.7, pp.1136-1148
**발행일**: 2026-04-19
**DOI**: https://doi.org/10.47738/jads.v7i2.1118

## 한국어 요약

**연구질문**: 카자흐어와 같은 저자원 언어로 작성된 온라인 정치 담론 및 감성을 높은 정확도로 자동 분류하기 위해, 미세 조정된 다국어 트랜스포머 모델과 초소형 데이터(few-shot) 환경의 LLM을 어떻게 비교 평가할 수 있는가?

**방법론**:
- 2019~2023년 공식 성명서, TV 토론, SNS 등에서 추출한 3,022문장 규모의 최초 카자흐어 정치 담론 주석 데이터셋(Corpus) 구축 및 타당성 분석
- 다국어 사전 학습 모델 기반 미세 조정(Fine-tuning)과 LLM의 퓨샷(Few-shot) 감성 분류 학습 방식 적용
- 코드 스위칭(외래어 혼용 등) 및 문맥적 특징 모델링 기법의 영향력 평가

**주요 결과**:
- 파인튜닝된 다국어 트랜스포머 모델이 F1 점수 0.90을 보였으며, LLM의 퓨샷 설정을 활용한 경우 F1 점수 0.94로 우수한 분류 성과를 달성
- 코드 스위칭과 화용론적 강조 등 지역 언어 특징을 결합했을 때 성능이 약 4%p 향상됨을 실증하여 저자원 언어에 대한 고성능 감성 분석 프레임워크를 제시함


## 초록 (원문)

This paper proposes the growing importance of automated analysis of political discourse in low-resource languages, using the Kazakh language as a case study. As political communication in Kazakhstan has increasingly moved online between 2019 and 2023, the need for accurate tools to evaluate political sentiment has grown. However, limited linguistic resources in Kazakh have hindered tool development. This paper introduces the first annotated corpus of political discourse in Kazakh, comprising 3,022 sentences selected from official statements, televised debates, policy documents, and social media publications. Each text was manually annotated for political sentiment by expert linguists and political scientists, with inter-annotator agreement measured to confirm reliability. Two main methodological approaches were employed for automatic sentiment classification: adapting multilingual neural network models to the Kazakh corpus and testing advanced generative language models in scenarios with minimal training examples. Performance was evaluated using standard classification procedures. The inclusion of pragmatic features such as code-switching, rhetorical emphasis, and discursive context led to notable improvements in classification accuracy. Experimental results demonstrate that models adapted to multilingual input achieved high classification quality, with fine-tuned multilingual transformer models reaching F₁-scores of up to 0.90, while large language models reached an F₁-score of 0.94 in few-shot settings. Explicit modeling of code-switching and pragmatic features yielded an improvement of approximately 4 percentage points in F₁. This research contributes a practical resource and a methodological framework for analyzing political sentiment in underrepresented languages, highlighting the feasibility of developing high-quality automated tools for political text analysis without extensive training data.

## 키워드

Politics, Natural language, Key (lock), Multilingualism, Government (linguistics), Field (mathematics)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

