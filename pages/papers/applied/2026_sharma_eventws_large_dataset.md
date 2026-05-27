---
title: "EVENT5Ws: A Large Dataset for Open-Domain Event Extraction from Documents"
authors: ['Praval Sharma', 'Ashok Samal', 'Leen-Kiat Soh', 'Deepti Joshi']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Topic Modeling', 'Data Visualization and Analytics', 'Advanced Text Analysis Techniques']
source: raw/applied/applied_2026_EVENT5Ws_A_Large_Dataset__nodoi.md
---

# EVENT5Ws: A Large Dataset for Open-Domain Event Extraction from Documents
**제목(한글)**: EVENT5Ws: 문서에서의 오픈 도메인 이벤트 추출을 위한 대용량 데이터셋

## 한국어 요약

**연구질문**: 폐쇄 도메인 이벤트 유형의 제한성과 오픈 도메인 대규모 수동 검증 데이터셋 부재라는 기존 한계를 극복하여, 범용적인 이벤트 추출 알고리즘 개발과 벤치마크 평가를 가능하게 하는 데이터셋을 어떻게 구축할 수 있는가?

**방법론**:
- 체계적인 어노테이션 파이프라인을 설계하여 대규모 수동 어노테이션 및 통계적 검증을 거친 오픈 도메인 이벤트 추출 데이터셋(EVENT5Ws) 구축
- 5W(Who, What, When, Where, Why) 기반 이벤트 요소를 구조화하고, 최신 사전 학습 LLM들에 대한 벤치마크 평가 수행

**주요 결과**:
- EVENT5Ws로 학습한 모델이 서로 다른 지리적 맥락을 가진 데이터셋에도 효과적으로 일반화됨을 보여, 일반화 가능한 이벤트 추출 알고리즘 개발에 대한 잠재력을 입증
- 어노테이션 복잡성에 관한 경험적 통찰과 향후 대규모 데이터셋 구축을 위한 권고 사항을 제시

**저자**: Praval Sharma; Ashok Samal; Leen-Kiat Soh; Deepti Joshi
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-04-23
**DOI**: 

## 초록 (원문)

Event extraction identifies the central aspects of events from text. It supports event understanding and analysis, which is crucial for tasks such as informed decision-making in emergencies. Therefore, it is necessary to develop automated event extraction approaches. However, existing datasets for algorithm development have limitations, including limited coverage of event types in closed-domain settings and a lack of large, manually verified dataset in open-domain settings. To address these limitations, we create EVENT5Ws , a large, manually annotated, and statistically verified open-domain event extraction dataset. We design a systematic annotation pipeline to create the dataset and provide empirical insights into annotation complexity. Using EVENT5Ws, we evaluate state-of-the-art pre-trained large language models and establish a benchmark for future research. We further show that models trained on EVENT5Ws generalize effectively to datasets from different geographical contexts, which demonstrates its potential for developing generalizable algorithms. Finally, we summarize the lessons learned during the dataset development and provide recommendations to support future large-scale dataset development.

## 키워드

Event (particle physics), Benchmark (surveying), Pipeline (software), Annotation, Information extraction, Task (project management)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

