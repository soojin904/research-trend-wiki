---
title: "중심성 분석 (Centrality)"
tags: [centrality, degree, betweenness, eigenvector, closeness, structural-measure]
netminer_support: "✅ 지원"
---

# 중심성 분석 (Centrality)

SNA에서 네트워크 내 노드의 중요도를 수치화하는 지표군. 소셜 네트워크 학술지 2020–2026 논문에서 24편이 사용하며 4위를 차지하는 핵심 구조 측정 기법이다.

## 핵심 개념

| 지표 | 의미 | 활용 |
|------|------|------|
| **Degree** (연결 중심성) | 직접 연결된 노드 수 | 허브 탐색 |
| out-degree | 내가 선택한 연결 수 | 능동적 연결 행위 |
| in-degree | 나를 선택한 연결 수 | 인기도, 수용 |
| **Closeness** (근접 중심성) | 다른 모든 노드까지의 평균 거리 | 정보 확산 속도 |
| **Betweenness** (매개 중심성) | 최단 경로 상에 위치하는 빈도 | 브로커, 게이트키퍼 탐색 |
| **Eigenvector** | 중요한 노드와 연결된 정도 | 영향력 측정 |
| **PageRank** | 링크 가중치 반영 재귀 중심성 | 웹·멀티플렉스 네트워크 |

### 시간 네트워크 확장

시간 그래프에서의 Temporal Betweenness는 정적 그래프 대비 계산 복잡도가 높다. 최선도(foremost)·최속(fastest) 경로 기반 집계는 #P-hard로 증명되어 있어, 최단 경로 기반 알고리즘이 현실적 대안이다.

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/2025_fernandez_centrality_and_social_domains\|Fernandez (2025)]] | 퍼스널 네트워크의 알터 중심성 → 언어 유사성 인식 예측 (다수준 로지스틱 회귀) | 지지 네트워크 중심 알터는 유사성 인식 ↑, 갈등 네트워크는 ↓ |
| [[pages/papers/2022_tasselli_network_centrality_bias\|Tasselli 외 (2022)]] | 직장 네트워크에서 에고의 in-degree 변화 추적 (종단 2개 연구 종합) | 공동 동기 높은 동료가 중심 인물에 유대 형성 → 중심성 편향 발생 |
| [[pages/papers/2023_kim_adolescent_network_positions_a\|Kim & Kim (2023)]] | 사회계측 네트워크 중심성·인기도 → 성인기 기억 수행 예측 (형제 고정 효과 모형) | 청소년기 중심 위치가 성인기 인지 능력과 유의하게 연관 |
| [[pages/papers/2024_neal_methodological_moderators_aver\|Neal (2024)]] | 아동·청소년 우정 네트워크 71편 메타분석 — outdegree centrality 추정치 조절 변수 검토 | 명칭 생성기 방식·선택 횟수 제한이 추정치에 유의미한 영향 |
| [[pages/papers/2026_asil_immunization_method_using\|Asil & Khansari (2026)]] | 멀티플렉스 네트워크에서 PageRank·근접 중심성 결합 MCPR 지표로 면역화 전략 설계 | 10% 면역화 시 홍역 2.2%, 천연두 7% 유행 규모 감소 |

## 해석 주의사항

- **in-degree ↑가 항상 긍정적이지 않음**: 역할 과부하, 돌봄 요청 부담 등 맥락 의존적 해석 필요
- **방법론적 편향**: 명칭 생성기 설계(친한 친구 vs. 일반 친구)·선택 횟수 제한이 중심성 추정치를 왜곡할 수 있음 (Neal 2024)
- **시간 네트워크**: 중심성의 시간 버전은 계산 복잡도가 높아 알고리즘 선택이 중요

## NetMiner 지원 현황

✅ 완전 지원 — Degree, Closeness, Betweenness, Eigenvector 등 주요 중심성 지표 일괄 산출. in/out 구분, 정규화, 시각화 연계 가능. 중심성 값을 독립변수로 회귀분석까지 연결 가능.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/ergm|ERGM]] (중심성을 독립변수로 포함하는 통계 모형)
- [[pages/methods/longitudinal_network|종단/동적 네트워크]] (시간에 따른 중심성 변화)
- [[pages/methods/community_detection|커뮤니티 탐지]] (중심성과 군집 구조의 연관)
- [[pages/concepts/personal_network|퍼스널 네트워크]]
