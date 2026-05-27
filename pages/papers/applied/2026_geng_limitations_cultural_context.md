---
title: "Limitations in cultural context: systematic biases of LLMs in Chinese sentiment analysis"
authors: ['Ruili Geng', 'Jiwen Zhang', 'Ruixian Yang', 'Mingzhe Quan', 'Xiang Zheng', 'Yishuai Xu']
year: 2026
venue: "Information Research an international electronic journal"
tags: ['Sentiment Analysis and Opinion Mining', 'Emotion and Mood Recognition', 'Neurobiology of Language and Bilingualism']
source: raw/applied/applied_2026_Limitations_in_cultural_c_ir31iconf64278.md
---

# Limitations in cultural context: systematic biases of LLMs in Chinese sentiment analysis
**제목(한글)**: 문화적 맥락의 한계: 중국어 감성 분석에서 나타나는 LLM의 체계적 편향

**저자**: Ruili Geng; Jiwen Zhang; Ruixian Yang; Mingzhe Quan; Xiang Zheng; Yishuai Xu
**출처**: Information Research an international electronic journal, Vol.31, pp.178-192
**발행일**: 2026-03-20
**DOI**: https://doi.org/10.47989/ir31iconf64278

## 한국어 요약

**연구질문**: 중국어 감성 분석에 대형 언어 모델(LLMs)을 적용할 때, 단어와 문장 층위에서 발생하는 중국 문화 고유의 뉘앙스 파악 왜곡 및 과장 편향의 기저 요인은 무엇인가?

**방법론**:
- 중국어 모국어 화자 집단과 주요 국내외 LLM 모델 간의 감성 평가 일치도 검증 실험 설계
- 200개의 중국어 단어와 225개의 복잡한 중국어 문장(반어법, 비유법 가미)을 투입해 카이제곱 검정 및 크루스칼-왈리스 검정 수행

**주요 결과**:
- LLM은 기본적인 단어 감성 분류(긍정/부정 극성 판별)에서는 우수한 성과를 보였으나, 감정의 감도(Intensity)나 각성도(Arousal) 평가에서 인간 평균 대비 과장되게 높게 점수를 부여하는 '과장 편향(exaggeration bias)'을 보임
- 이는 훈련 말뭉치에 편재한 자극적인 마케팅 문체 및 신체적 감각이 결여된 통계적 임베딩 언어 구조에서 기인한 한계로, 텍스트 감성 강도 분석 시 LLM 출력 수치 조율이 필수적임을 규명함


## 초록 (원문)

Introduction. Large language models (LLMs) are increasingly applied in Chinese sentiment analysis; however, their ability to interpret sentiment in culturally specific contexts remains uncertain. This study systematically evaluates the potential biases of LLM-based Chinese sentiment analysis, providing an empirical basis for model optimisation and responsible application. Method. A human-AI comparison experiment was conducted at both word and sentence levels. Two hundred Chinese words from four categories and 225 sentences were used as materials. Judgment data on sentiment polarity, intensity, valence, and arousal were collected from native Chinese speakers and representative Chinese and international LLMs. Data analysis was performed using Chi-square tests and Kruskal–Wallis tests. Results. In sentiment polarity judgment, LLMs are highly consistent with humans and outperform the traditional sentiment lexicon. For continuous dimensions (intensity, valence, arousal), LLMs generally show an exaggeration bias, especially for sensory-perceptual words and ironic sentences. The bias stems from the disembodied cognitive nature of models, exaggerated linguistic patterns in training data, and technical characteristics such as the attention mechanism. Conclusion. This study reveals a systematic limitation of LLMs in Chinese sentiment analysis, characterised by accurate classification but exaggerated quantitative evaluations. Consequently, in practical applications, outputs related to sentiment intensity should be interpreted with caution.

## 키워드

Sentiment analysis, Sentence, Exaggeration, Cognition, Word (group theory), Style (visual arts)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

