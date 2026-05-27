---
title: "종단/동적 네트워크 분석 (Longitudinal & Dynamic Network Analysis)"
tags: [longitudinal, dynamic-network, temporal, panel-data, tergm, time-series]
netminer_support: "⚠️ 부분 지원"
---

# 종단/동적 네트워크 분석 (Longitudinal & Dynamic Network Analysis)

네트워크 구조가 시간에 따라 어떻게 변화하는지를 분석하는 방법론 범주. SNA 학술지 2020–2026에서 30편이 활용하여 2위를 기록했다. 정적 구조 분석에서 **시간에 따른 변화 추적**으로의 패러다임 전환을 대표하는 가장 성장하는 분야다.

## 핵심 개념

### 분석 설계 유형

| 유형 | 설명 | 대표 방법 |
|------|------|-----------|
| **패널 네트워크** | 이산 시점(wave) 반복 측정 | SAOM, TERGM |
| **시간 그래프** | 연속/고빈도 시간 스탬프 엣지 | Temporal betweenness, Relational Event Model |
| **동적 시각화** | 시간 윈도우 알고리즘으로 스냅샷 비교 | Time Windows in Networks |
| **종단 에고넷** | 에고 네트워크 반복 측정 | 혼합 방법론 |

### 핵심 방법론 관계

```
종단/동적 네트워크 (30편)
├── SAOM (18편) → 별도 페이지: pages/methods/saom
├── STERGM (ERGM 변형) → 별도 페이지: pages/methods/ergm
├── TERGM (Temporal ERGM)
├── Relational Event Model (REM)
└── 기술적 종단 분석 (패널 비교, 시계열 시각화)
```

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2020_jaramillo_social_cohesion_emerging_from\|Jaramillo 외 (2020)]] | Facebook 프로필 네트워크 2008–2016 시간 윈도우 알고리즘으로 종단 추적 | 신체활동 강사가 허브; 사용자당 1.73개 새 우정으로 초선형 사회 응집 성장 |
| [[pages/papers/sna/2024_bu_algorithmic_aspects_temporal\|Buß 외 (2024)]] | 시간 그래프에서 최단·최선도·최속 경로 기반 시간 매개 중심성 알고리즘 개발 | 최선도·최속 경로 집계는 #P-hard; 최단 경로 기반 다항 시간 알고리즘 제시 |
| [[pages/papers/sna/2023_bright_offence_versatility_among_coof\|Bright 외 (2023)]] | 관계적 하이퍼이벤트 모형(RHEM)으로 2모드 공동 범죄 네트워크 동적 분석 | 공동 범죄자가 단독 범죄자보다 다중 범죄 유형 관여 확률 높음; 사회학습 효과 |
| [[pages/papers/sna/2024_filippimaz_modeling_nonlinear_effects_wit\|Filippi-Mazzola & Wit (2024)]] | DREAM(신경망 기반 관계 이벤트 가산 모형)으로 특허 인용 동적 네트워크 분석 | 비선형 효과 포착 가능; 약 800만 노드·1억 이벤트 대규모 네트워크 처리 |

## NetMiner 지원 현황

⚠️ 부분 지원 — 시계열 네트워크 시각화(스냅샷 비교, 시간 슬라이싱) 가능. 그러나:
- STERGM, TERGM, Relational Event Model 등 종단 통계 모형은 미지원
- SAOM은 별도로 미지원

**대안 도구**:
- R `statnet` (STERGM, TERGM)
- R `RSiena` (SAOM)
- R `relevent`, `rem` 패키지 (Relational Event Model)
- Python `networkx` + 커스텀 시계열 처리

**NetMiner 활용 포인트**: 종단 데이터를 시간 슬라이스로 나누어 각 시점 네트워크 시각화 + 구조 지표 추적은 가능. 통계 모형화 전 탐색적 분석 단계에 효과적.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/saom|SAOM / RSiena]] (종단 통계 모형의 핵심)
- [[pages/methods/ergm|ERGM]] (STERGM이 이 범주에 속함)
- [[pages/methods/centrality|중심성 분석]] (시간에 따른 중심성 변화 추적)
- [[pages/methods/diffusion_propagation|확산/전파]] (동적 네트워크 위의 프로세스)
