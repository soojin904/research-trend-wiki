---
title: "확산/전파/면역화 (Diffusion, Contagion & Immunization)"
tags: [diffusion, contagion, spread, immunization, influence, sir-model, epidemic]
netminer_support: "❌ 미지원 (시뮬레이션)"
---

# 확산/전파/면역화 (Diffusion, Contagion & Immunization)

네트워크를 통해 정보·행동·질병 등이 어떻게 퍼지는지를 모델링하고, 전파를 막기 위한 최적 전략(면역화, 차단 노드 선택)을 탐구하는 방법론. SNA 학술지 2020–2026에서 11편이 활용하여 공동 10위를 기록했다.

## 핵심 개념

### 주요 전파 모형

| 모형 | 상태 | 설명 |
|------|------|------|
| **SI** | Susceptible → Infected | 단순 전파, 회복 없음 |
| **SIR** | S → I → Recovered | 회복 후 면역 획득 |
| **SIS** | S → I → S | 재감염 가능 |
| **SIR-UA** | SIR + Unaware/Aware | 감염+인식 동시 모형화 (멀티플렉스) |
| **복잡 전파** | 다중 접촉 필요 | 행동·규범 확산에 적합 |

### 면역화 전략

- **무작위 면역화**: 비용 효율 낮음
- **고연결 노드 우선**: 허브 타깃, 효과적이나 사전 지식 필요
- **PageRank 기반**: 영향력 있는 노드 선택
- **Random Chain**: 무작위 출발 후 이웃 탐색, 사전 지식 불필요 (실용적)

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/2026_asil_immunization_method_using\|Asil & Khansari (2026)]] | 멀티플렉스 네트워크에서 SIR-UA 모형 + MCPR 지표(PageRank+근접 중심성 결합)로 면역화 전략 비교 | 10% 면역화 시 홍역 2.2%, 천연두 7% 유행 규모 감소; 파라미터 최적화로 최대 9.5% 추가 개선 |
| [[pages/papers/2024_browne_evaluating_disease_surveillanc\|Browne 외 (2024)]] | 뉴욕시 680만 명 에이전트 기반 시뮬레이션으로 5가지 감시 전략 비교 — COVID형 발병 조기 탐지 | Random Chain 전략이 사전 네트워크 지식 없이도 안정적 조기 경보 제공 |
| [[pages/papers/2024_king_walkindependence_probabilities\|King (2024)]] | 포함-배제 원리 기반 보행 독립 확률(WIP) 공식으로 정확한 노드-노드 확산 확률 계산 | 기존 확산 중심성의 과대 추정 문제 해결; WIP 중심성·차단 중심성 신규 지표 도출 |
| [[pages/papers/2020_young_modeling_the_dynamism\|Young 외 (2020)]] | 노숙 청소년 다중 네트워크에서 HIV 정보 확산 동적 시뮬레이션 | 네트워크 역동성이 확산에 유의한 영향; 정적 네트워크 가정 시 효과 과대·과소 추정 |

## NetMiner 지원 현황

❌ 미지원 (시뮬레이션) — NetMiner는 SIR/SIS/SIR-UA 등 확산 시뮬레이션을 직접 지원하지 않는다. 이는 사이람의 핵심 미지원 공백 중 하나로 평가된다.

**대안 도구**:
- Python `ndlib` (네트워크 확산 라이브러리)
- Python `EoN` (Epidemics on Networks)
- R `EpiModel`
- NetLogo (에이전트 기반 시뮬레이션)

**NetMiner 활용 포인트**: 확산 시뮬레이션 전 네트워크 구조 분석(중심성, 커뮤니티 구조) 및 결과 시각화는 가능.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/centrality|중심성 분석]] (면역화 전략의 노드 선택에 활용)
- [[pages/methods/community_detection|커뮤니티 탐지]] (커뮤니티 구조가 확산 전략 효율에 영향)
- [[pages/methods/longitudinal_network|종단/동적 네트워크]] (동적 확산 과정)
- [[pages/concepts/multilayer_network|다층 네트워크]] (멀티플렉스 확산 모형)
