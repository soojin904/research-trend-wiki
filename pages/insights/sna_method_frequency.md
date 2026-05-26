---
title: "SNA 방법론 사용 빈도 분석 (2020–2026)"
tags: [method-frequency, ergm, saom, centrality, topic-modeling, egocentric]
generated_by: wiki:query
query_date: 2026-05-26
---

# SNA 방법론 사용 빈도 분석 (2020–2026)

**분석 범위**: Social Networks + Network Science 학술지 2020–2026 개별 페이지 181편
**집계 방식**: 논문 파일 단위 (중복 제거, 카탈로그 제외)

## 순위표

| 순위 | 방법론 | 논문 수 | 최근 추가 | 분류 |
|------|--------|---------|----------|------|
| 1 | 에고중심 / 퍼스널 네트워크 | 37 | — | 데이터 구조 |
| 2 | 종단 / 동적 네트워크 | 30 | — | 분석 설계 |
| 3 | ERGM (및 변형: STERGM, ergmito) | 26 | — | 통계 모델링 |
| 4 | 중심성 분석 (Centrality) | 24 | +1 NWS | 구조 측정 |
| 5 | 다층 / 멀티플렉스 / 이분 네트워크 | 23 | +1 NWS | 데이터 구조 |
| 6 | 토픽모델링 / LDA | 20 | +1 NWS (topic+network) | 텍스트+네트워크 |
| 7 | SAOM / RSiena | 18 | — | 종단 통계 모델 |
| 8 | ML / 딥러닝 (전통 ML 중심, GNN ≈ 2–3건) | 15 | — | 예측 모델 |
| 9 | Bayesian / 잠재공간 모델 | 14 | +1 NWS | 통계 추정 |
| 10 | 확산 / 전파 (Diffusion, immunization 포함) | 11 | +1 NWS | 동학 분석 |
| 10 | 커뮤니티 탐지 / 코어-퍼리퍼리 | 11 | +1 NWS | 구조 분석 |
| 12 | **데이터 수집 방법론** | 10 | — | 방법 설계 |
| 13 | Network Scale-Up / ARD | 7 | — | 데이터 수집 |
| 14 | 혼합 방법론 | 5 | — | 설계 |
| 15 | 의미연결망 / 키워드 네트워크 / 가치네트워크 | 4 | +1 NWS | 텍스트+네트워크 |

## 주요 해석

### 에고중심 네트워크 1위 유지 (37편)
2020년 추가 7편으로 더 강화. 에고넷 데이터 수집 방법론(GENSI 등 시각적 도구, 대규모 수집) 논문도 2020년에 집중 — 방법론 정교화 시기로 해석.

### 종단/동적 네트워크 2위로 상승
2020년 추가 8편으로 ERGM을 제치고 2위. SAOM(18편)과 결합하면 종단 방법론 합산 48편 — SNA의 핵심 관심사가 정적 구조에서 **시간에 따른 변화**로 이동 중.

### ERGM 변형 확산이 새로운 흐름
2020년 STERGM(시계열 분리 ERGM)·ergmito(소규모 네트워크용 MLE) 등장. ERGM이 단일 모델을 넘어 적용 맥락에 맞게 분화하고 있음. NetMiner 기본 ERGM 외 변형 지원 검토 필요.

### 통계적 네트워크 모델링 최다 유지
ERGM(26) + SAOM(18) = **44편** — SNA 논문의 표준 통계 도구로 확고한 위치.

### 데이터 수집 방법론이 독자 연구 흐름으로 부상 (10편)
에고넷 데이터 수집 도구, 시각적 설문 방법, 대규모 퍼스널 네트워크 수집 노하우 등 — 2020년에 집중적으로 등장. SNA 인프라 연구로 볼 수 있음. NetMiner의 Extension(SNS/Biblio/News Collector)과 직결.

### 토픽모델링이 SNA 전문지에도 진입 (19편)
2020년 추가 없음 — 2021년 이후 새로운 트렌드로 등장한 것 확인. 사이람 핵심 기술과 직결.

### 다층 네트워크 상승세 지속 (22편)
단일 레이어 한계 인식 확산. 2024–2026년 집중, **상승 트렌드** 유지.

## NetMiner 포지셔닝 시사점

| 방법론 | NetMiner 지원 | 시사점 |
|--------|:------------:|--------|
| 에고중심 네트워크 | ✅ | 기존 강점 — 마케팅 강화 기회 |
| 종단 / 동적 | ⚠️ 부분 | 2위로 상승 — 시계열 네트워크 시각화 강화 필요 |
| ERGM (변형 포함) | ✅ (기본) | 변형(STERGM·ergmito)은 미지원 — 기본 ERGM 홍보 우선 |
| 중심성 분석 | ✅ | 핵심 기능, 안정적 수요 |
| 다층 / 이분 네트워크 | ✅ | 지원 확인, 홍보 부족 가능성 |
| 토픽모델링 / LDA | ✅ | SNA 학술지 진입 확인 — 경쟁 우위 영역 |
| SAOM / RSiena | ❌ | 고급 연구자 이탈 요인 |
| ML / 딥러닝 | ✅ (GNN 포함) | 실제 GNN 사용 ≈ 2–3건 — 미래 선점 포지셔닝 |
| 데이터 수집 방법론 | ✅ (Ego Network Extract) | 논문들은 에고넷 인터뷰·설문 수집 방법론. Extension(SNS/Biblio)과 무관. 수집 도구(Network Canvas 등) → NetMiner 분석 워크플로우 콘텐츠 기회 |

## NetMiner 대조 분석

→ 상세: [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]]

**핵심 발견**: ERGM·GNN·BERTopic·Two-Mode 등 NetMiner가 지원하는 기능이 예상보다 넓음.
미지원은 SAOM, 종단 동적 모델링, 확산 시뮬레이션이 핵심 공백.

## 위키 연관

- [[pages/concepts/personal_network|퍼스널 네트워크]]
- [[pages/methods/centrality|Centrality]]
- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/concepts/multilayer_network|다층 네트워크]]
- [[pages/concepts/causal_inference_networks|인과 추론과 네트워크]]
- [[pages/tools/netminer|NetMiner]]
- [[pages/tools/other_tools|Other Tools (ERGM·SAOM 지원 도구)]]
