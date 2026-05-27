---
title: "A Mechanism and Optimization Study on the Impact of Information Density on User-Generated Content Named Entity Recognition"
authors: ['蒋小波 Jiang Xiaobo', 'Dinghong Lai', 'Song Qiu', 'Yadong Deng', 'Xinkai Zhan']
year: 2026
venue: "ArXiv.org"
tags: ['Topic Modeling', 'Mental Health via Writing', 'Advanced Graph Neural Networks']
source: raw/applied/applied_2026_A_Mechanism_and_Optimizat_nodoi.md
---

# A Mechanism and Optimization Study on the Impact of Information Density on User-Generated Content Named Entity Recognition
**제목(한글)**: 정보 밀도가 사용자 생성 콘텐츠 개체명 인식에 미치는 영향에 관한 메커니즘 및 최적화 연구

## 한국어 요약

**연구질문**: 소셜 미디어 등 사용자 생성 콘텐츠(UGC)에서 개체명 인식(NER) 모델 성능이 저하되는 근본 원인이 무엇이며, 이를 낮은 정보 밀도(Information Density)라는 단일 요인으로 설명하고 해결할 수 있는가?

**방법론**:
- 개체 희귀성과 주석 일관성을 통제한 계층적 교란 통제 리샘플링 실험으로 정보 밀도(ID)를 독립 핵심 요인으로 식별
- 어텐션 스펙트럼 분석(Attention Spectrum Analysis, ASA)으로 낮은 ID가 "어텐션 둔화"를 유발하여 NER 성능을 저하시키는 인과 관계 정량화
- LLM 기반 모델 불문 프레임워크 Window-Aware Optimization Module(WOM) 개발 및 WNUT2017, Twitter-NER 등 표준 UGC 데이터셋 검증

**주요 결과**:
- WOM이 WNUT2017에서 최대 4.5% F1 점수 절대 향상을 달성하며 새로운 최고 성능(SOTA) 기록
- 정보 희소 영역 식별 후 선택적 역번역으로 의미 밀도를 높이는 접근법이 다양한 주류 아키텍처에서 강건성 입증

**저자**: 蒋小波 Jiang Xiaobo; Dinghong Lai; Song Qiu; Yadong Deng; Xinkai Zhan
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-04-21
**DOI**: 

## 초록 (원문)

Named Entity Recognition (NER) models trained on clean, high-resource corpora exhibit catastrophic performance collapse when deployed on noisy, sparse User-Generated Content (UGC), such as social media. Prior research has predominantly focused on point-wise symptom remediation -- employing customized fine-tuning to address issues like neologisms, alias drift, non-standard orthography, long-tail entities, and class imbalance. However, these improvements often fail to generalize because they overlook the structural sparsity inherent in UGC. This study reveals that surface-level noise symptoms share a unified root cause: low Information Density (ID). Through hierarchical confounding-controlled resampling experiments (specifically controlling for entity rarity and annotation consistency), this paper identifies ID as an independent key factor. We introduce Attention Spectrum Analysis (ASA) to quantify how reduced ID causally leads to ``attention blunting,'' ultimately degrading NER performance. Informed by these mechanistic insights, we propose the Window-Aware Optimization Module (WOM), an LLM-empowered, model-agnostic framework. WOM identifies information-sparse regions and utilizes selective back-translation to directionally enhance semantic density without altering model architecture. Deployed atop mainstream architectures on standard UGC datasets (WNUT2017, Twitter-NER, WNUT2016), WOM yields up to 4.5\% absolute F1 improvement, demonstrating robustness and achieving new state-of-the-art (SOTA) results on WNUT2017.

## 키워드

Named-entity recognition, Robustness (evolution), Annotation, Class (philosophy), Alias, Entity linking, Key (lock), Noise (video)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

