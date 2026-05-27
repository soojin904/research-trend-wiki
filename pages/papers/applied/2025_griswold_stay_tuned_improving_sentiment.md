---
title: "Stay Tuned: Improving Sentiment Analysis and Stance Detection Using Large Language Models"
authors: ['Max Griswold', 'Michael W. Robbins', 'Michael Pollard']
year: 2025
venue: "Political Analysis"
tags: ['Sentiment Analysis and Opinion Mining', 'Computational and Text Analysis Methods', 'Misinformation and Its Impacts']
source: raw/applied/applied_2025_Stay_Tuned_Improving_Sent_pan_2025_10023.md
---

# Stay Tuned: Improving Sentiment Analysis and Stance Detection Using Large Language Models

**제목(한글)**: 계속 주목하라: 대규모 언어 모델을 활용한 감성 분석 및 입장 감지 개선

## 한국어 요약

**연구질문**: 어휘 기반 모델, 지도 학습 모델, LLM(대규모 언어 모델)의 입장 감지(stance detection) 성능을 비교했을 때, 어떤 미세조정(fine-tuning) 전략이 가장 효과적인가?

**방법론**:
- 미국 의회 의원 트윗(대규모)과 일반 사용자 트윗(소규모)을 활용한 2020년 대선 입장 감지 실험
- 어휘 기반 모델, 지도학습 모델, LLM 비교 평가
- 교차 타겟 조율(cross-target tuning), 소수 샷(few-shot) 및 사고 연쇄(chain-of-thought) 프롬프팅 전략 적용

**주요 결과**:
- LLM은 여러 주제가 언급될 때도 특정 대상에 대한 입장을 구분 가능
- 미세조정은 사전학습 모델 대비 성능을 크게 향상시킴
- 교차 타겟 조율은 일부 상황에서 내부 타겟 조율의 대안이 될 수 있으며, 복잡한 프롬프팅은 사전학습 모델 대비 개선되지만 미세조정 방식에는 미치지 못함

**저자**: Max Griswold; Michael W. Robbins; Michael Pollard
**출처**: Political Analysis, Vol.None, pp.1-20
**발행일**: 2025-12-17
**DOI**: https://doi.org/10.1017/pan.2025.10023

## 초록 (원문)

Abstract Sentiment analysis and stance detection are key tasks in text analysis, with applications ranging from understanding political opinions to tracking policy positions. Recent advances in large language models (LLMs) offer significant potential to enhance sentiment analysis techniques and to evolve them into the more nuanced task of detecting stances expressed toward specific subjects. In this study, we evaluate lexicon-based models, supervised models, and LLMs for stance detection using two corpuses of social media data—a large corpus of tweets posted by members of the U.S. Congress on Twitter and a smaller sample of tweets from general users—which both focus on opinions concerning presidential candidates during the 2020 election. We consider several fine-tuning strategies to improve performance—including cross-target tuning using an assumption of congressmembers’ stance based on party affiliation—and strategies for fine-tuning LLMs, including few shot and chain-of-thought prompting. Our findings demonstrate that: 1) LLMs can distinguish stance on a specific target even when multiple subjects are mentioned, 2) tuning leads to notable improvements over pretrained models, 3) cross-target tuning can provide a viable alternative to in-target tuning in some settings, and 4) complex prompting strategies lead to improvements over pretrained models but underperform tuning approaches.

## 키워드

Sentiment analysis, Task (project management), Focus (optics), Key (lock), Presidential system, Social media, Language model

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

