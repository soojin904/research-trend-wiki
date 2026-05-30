---
title: "VILLAIN at AVerImaTeC: Verifying Image-Text Claims via Multi-Agent Collaboration"
authors: ['Jaeyoon Jung', 'Yejun Yoon', 'Park, Kunwoo']
year: 2026
venue: "ArXiv.org"
tags: ['Multimodal Machine Learning Applications', 'Topic Modeling', 'Explainable Artificial Intelligence (XAI)']
source: raw/applied/applied_2026_VILLAIN_at_AVerImaTeC_Ver_nodoi.md
---

# VILLAIN at AVerImaTeC: Verifying Image-Text Claims via Multi-Agent Collaboration

**제목(한글)**: AVerImaTeC의 VILLAIN: 다중 에이전트 협업을 통한 이미지-텍스트 클레임 검증

## 한국어 요약

**연구질문**: 이미지-텍스트 클레임을 효과적으로 검증하기 위해 프롬프트 기반 다중 에이전트 협업 시스템을 어떻게 구축하고 활용할 수 있는가?

**방법론**:
- 프롬프트 기반 다중 에이전트 협업 (Multi-Agent Collaboration)
- 비전-언어 모델 (Vision-Language Model, VLM) 에이전트 활용
- 텍스트 및 시각적 증거 검색 및 지식 저장소 구축
- 모달리티별 및 교차 모달 에이전트를 통한 분석 보고서 생성 및 질의응답 (Q&A) 쌍 생성
- 최종 판정 예측 에이전트 (Verdict Prediction agent)를 통한 검증 결과 도출

**주요 결과**:
- VILLAIN은 프롬프트 기반 다중 에이전트 협업을 통해 이미지-텍스트 클레임을 검증하는 다중 모달 팩트체킹 시스템이다.
- AVerImaTeC 공유 태스크에서 모든 평가 지표에서 1위를 차지하며 우수한 성능을 입증했다.
- 비전-언어 모델 에이전트들이 팩트체킹의 여러 단계에서 활용되어, 증거 검색, 분석 보고서 생성, 질의응답 쌍 생성 등을 수행한다.
- 소스 코드가 공개되어 재현 및 추가 연구에 기여한다.

**저자**: < >

## ѱ 

****: <>

****:
- <׸>

**ֿ **:
- <׸>


**저자**: Jaeyoon Jung; Yejun Yoon; Park, Kunwoo
**저자**: ArXiv.org, Vol.None
**저자**: 2026-02-04
**저자**: ## 초록 (원문)

This paper describes VILLAIN, a multimodal fact-checking system that verifies image-text claims through prompt-based multi-agent collaboration. For the AVerImaTeC shared task, VILLAIN employs vision-language model agents across multiple stages of fact-checking. Textual and visual evidence is retrieved from the knowledge store enriched through additional web collection. To identify key information and address inconsistencies among evidence items, modality-specific and cross-modal agents generate analysis reports. In the subsequent stage, question-answer pairs are produced based on these reports. Finally, the Verdict Prediction agent produces the verification outcome based on the image-text claim and the generated question-answer pairs. Our system ranked first on the leaderboard across all evaluation metrics. The source code is publicly available at https://github.com/ssu-humane/VILLAIN.

## 키워드

Key (lock), Outcome (game theory), Source code, Code (set theory)

## 위키 연관

- [[pages/methods/topic_modeling|?픽모델?]

## 메모


