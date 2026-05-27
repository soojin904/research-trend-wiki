---
title: "Analyzing and Improving Cross-lingual Knowledge Transfer for Machine Translation"
authors: ['David Stap']
year: 2026
venue: "ArXiv.org"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Multimodal Machine Learning Applications']
source: raw/applied/applied_2026_Analyzing_and_Improving_C_nodoi.md
---

# Analyzing and Improving Cross-lingual Knowledge Transfer for Machine Translation
**제목(한글)**: 기계 번역에서의 교차 언어적 지식 전이 분석 및 개선

## 한국어 요약

**연구질문**: 다국어 신경망 기계 번역 시스템에서 언어 간 효과적인 지식 전이를 방해하는 주요 요인은 무엇이며, 특히 저자원 언어에서의 일반화 및 강건성을 어떻게 개선할 수 있는가?

**방법론**:
- 언어 간 유사도가 전이에 미치는 영향, 저자원 번역 강화를 위한 검색 증강 및 보조 감독(Auxiliary supervision) 기법 분석
- 대형 언어 모델에서 병렬 데이터 미세 조정이 야기하는 의도치 않은 트레이드오프 검토
- 학습 중 언어 다양성이 일반화와 오프 타깃(Off-target) 번역 감소에 미치는 역할 분석

**주요 결과**:
- 번역 커버리지 확대가 일반화를 개선하고 오프 타깃 동작을 줄임을 실증
- 모델링 선택과 데이터 구성이 다국어 학습 결과를 형성하는 방식을 규명하여, 더 포용적이고 탄력 있는 다국어 NLP 시스템 구축을 위한 통찰을 제공

**저자**: David Stap
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-01-07
**DOI**: 

## 초록 (원문)

Multilingual machine translation systems aim to make knowledge accessible across languages, yet learning effective cross-lingual representations remains challenging. These challenges are especially pronounced for low-resource languages, where limited parallel data constrains generalization and transfer. Understanding how multilingual models share knowledge across languages requires examining the interaction between representations, data availability, and training strategies. In this thesis, we study cross-lingual knowledge transfer in neural models and develop methods to improve robustness and generalization in multilingual settings, using machine translation as a central testbed. We analyze how similarity between languages influences transfer, how retrieval and auxiliary supervision can strengthen low-resource translation, and how fine-tuning on parallel data can introduce unintended trade-offs in large language models. We further examine the role of language diversity during training and show that increasing translation coverage improves generalization and reduces off-target behavior. Together, this work highlights how modeling choices and data composition shape multilingual learning and offers insights toward more inclusive and resilient multilingual NLP systems.

## 키워드

Machine translation, Generalization, Robustness (evolution), Training set, Knowledge transfer, Transfer of learning, Translation (biology), Parallel corpora

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

