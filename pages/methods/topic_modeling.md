---
title: "토픽모델링 (Topic Modeling)"
tags: [topic-modeling, LDA, BERTopic, text-analysis, keyword-assisted]
netminer_support: "✅ 지원"
---

# 토픽모델링 (Topic Modeling)

문서 집합에서 통계적으로 잠재된 주제(토픽)를 자동 추출하는 방법론. SNA 학술지 2020–2026 논문에서 20편이 활용하며 6위를 기록했다. 인용 네트워크·가치 네트워크·공동체 분석 등 네트워크 연구에서 텍스트 레이어를 분석하는 표준 도구로 자리잡았다.

## 핵심 개념

| 알고리즘 | 특징 |
|----------|------|
| **LDA** (Latent Dirichlet Allocation) | 가장 널리 사용. 문서-토픽, 토픽-단어 확률 분포 |
| **BERTopic** | 임베딩 기반, 의미 이해 강화 |
| **CTM** (Contextualized Topic Model) | 사전학습 언어모델 활용 |
| **Keyword-Assisted Topic Model** | 사전 정의 키워드로 토픽 방향성 제어 (Almquist 2026) |

### 분석 흐름 (LDA)

1. 전처리 (불용어 제거, 형태소 분석)
2. 토픽 수(K) 설정 (코히런스 점수로 최적화)
3. 모델 학습
4. 토픽별 상위 단어 해석
5. 시계열 분석 → 토픽 트렌드

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/2026_almquist_search_common\|Almquist 외 (2026)]] | COP 16–28 기후협상 발언문에 키워드 보조 토픽 모델 적용 → 가치 네트워크 추출 | "공정성·권력" 중심에서 "환경·성취" 중심으로 가치 이동 |
| [[pages/papers/2021_keuchenius_adoption_and_adaptation\|Keuchenius 외 (2021)]] | 그라노베터 인용 확산 네트워크에 토픽 모델링 적용 → 학문 공동체별 해석 차이 분석 | 확산은 단순 전달이 아닌 적응·변형 과정; 중심 학자가 공동체 브로커로 기능 |

### 텍스트+네트워크 복합 활용 패턴

토픽모델링 결과를 네트워크 분석 입력값으로 연결하는 파이프라인이 확산 중:
- 텍스트 → 토픽 → 토픽 네트워크 구성 → 중심성·커뮤니티 분석
- 가치 추출 → 국가 간 가치 네트워크 → 협상 구조 해석 (Almquist 2026)
- 인용 확산 → 토픽 공동체 → 아이디어 번역 추적 (Keuchenius 2021)

## [[pages/methods/semantic_network_analysis|의미연결망]]과의 결합

→ 복합 방법론 패턴의 핵심: 토픽 + 네트워크 조합이 SNA 학술지에도 표준 패턴으로 진입

| | 토픽모델링 | 의미연결망 |
|--|------------|-----------|
| 단위 | 단어 분포 (토픽) | 단어 쌍 (엣지) |
| 결과 | 잠재 주제 군집 | 네트워크 구조 |
| 강점 | 숨겨진 주제 발견 | 개념 간 관계 시각화 |

## NetMiner 지원 현황

✅ 지원 — LDA 기반 토픽모델링 내장. 토픽 결과를 네트워크 분석(키워드 네트워크, 공동 출현 행렬)으로 연계하는 워크플로우 가능. BERTopic 등 임베딩 기반 알고리즘은 Python 연계 필요.

**대안 도구**:
- Python: gensim (LDA), BERTopic, contextualized-topic-models
- R: topicmodels, stm (Structural Topic Model)

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/semantic_network_analysis|의미연결망 분석]]
- [[pages/methods/ml_gnn|ML/딥러닝/GNN]] (임베딩 기반 토픽 방법론과의 경계)
