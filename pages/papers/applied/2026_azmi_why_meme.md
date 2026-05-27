---
title: "Why So Meme? A Comparative and Explainable Analysis of Multimodal Hateful Meme Detection"
authors: ['Nor Saiful Azam Bin Nor Azmi', 'Michal Ptaszynski', 'Fumito Masui', 'Abu Nowhash Chowdhury']
year: 2026
venue: "Machine Learning and Knowledge Extraction"
tags: ['Hate Speech and Cyberbullying Detection', 'Sentiment Analysis and Opinion Mining', 'Misinformation and Its Impacts']
source: raw/applied/applied_2026_Why_So_Meme_A_Comparative_make8020050.md
---

# Why So Meme? A Comparative and Explainable Analysis of Multimodal Hateful Meme Detection
**제목(한글)**: 왜 밈인가? 다중 모드 유해 밈 탐지에 대한 비교 및 설명 가능 분석

**저자**: Nor Saiful Azam Bin Nor Azmi; Michal Ptaszynski; Fumito Masui; Abu Nowhash Chowdhury
**출처**: Machine Learning and Knowledge Extraction, Vol.8, pp.50-50
**발행일**: 2026-02-21
**DOI**: https://doi.org/10.3390/make8020050

## 한국어 요약

**연구질문**: 텍스트와 이미지가 결합된 인터넷 '유해 밈(Hateful Memes)'을 판별할 때 단일 모드 모델 대비 다중 모드 융합 모델이 지니는 강점과 설명 가능 모델(XAI)이 보여주는 판단 근거는 무엇인가?

**방법론**:
- 후기 융합 프레임워크인 RoBERViT와 단일 모드 모델(RoBERTa, ViT), 그리고 멀티모달 LLM인 LLaVA를 Facebook 및 Innopolis 벤치마크 데이터셋에서 비교 평가
- LIME 설명 기법 및 LLaVA의 질적 인지 추적을 병행 적용

**주요 결과**:
- 융합 모델(RoBERViT)이 Innopolis 데이터에서 F1-스코어 0.6439를 얻어 단일 텍스트(0.5794) 대비 우수함을 검증
- 그러나 Facebook 밈의 경우 텍스트 단독이 여전히 강세를 보였는데, 융합 모델이 이미지 내 텍스트 오버레이를 단순 유해 시각 징후로 오탐하는 패턴과 LLaVA가 환각 유해 감정을 유발하는 한계를 포착해 보완 과제를 제시


## 초록 (원문)

The rise of toxic content, particularly in the form of hateful memes, poses a significant challenge to social media platforms. This paper presents an empirical comparative study of unimodal and multimodal architectures for toxic content detection. Rather than proposing a novel architecture, the study evaluates the efficacy of a modular Late Fusion framework (RoBERViT) against specialized unimodal baselines (RoBERTa and ViT) and a generalist Large Multimodal (LLaVA). Both unimodal and multimodal configurations across two distinct benchmarks—the imbalanced Innopolis Hateful Memes dataset and the confounder-driven Facebook Hateful Meme dataset—were explored. Beyond quantitative metrics, this study conducts a qualitative analysis using Explainable AI (LIME) and a Large Multimodal Model (LLaVA) to investigate model reasoning. Results demonstrate that the multimodal fusion model consistently outperformed its unimodal counterparts on the Innopolis Hateful Meme dataset, achieving a toxic class F1-score of 0.6439 compared to the text-only score of 0.5794. However, on the Facebook Hateful Meme dataset, text-only models remain competitive, highlighting the “benign confounder” challenge. The qualitative analysis reveals that text remains the dominant modality, with models often relying on surface-level keywords. Notably, the Vision Transformer frequently uses text overlays as a visual proxy for hate, while the LLaVA model struggles with hallucinated toxicity in benign confounder contexts. These findings underscore the persistent challenge of achieving true multimodal understanding in hate speech detection.

## 키워드

Hallucinating, Multimodal therapy, Multimodality, Qualitative analysis, Class (philosophy), Social media

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

