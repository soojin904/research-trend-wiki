---
title: "NetMiner 기능-트렌드 인사이트 (2021–2026)"
tags: [netminer, insight, trend, product-planning, marketing]
generated_by: wiki:query
query_date: 2026-05-25
---

# NetMiner 기능-트렌드 인사이트

**근거**: Social Networks 학술지 2021–2026 139편 방법론 빈도 분석 + NetMiner 실제 메뉴 대조
→ 원천 데이터: [[pages/insights/sna_method_frequency|SNA 방법론 빈도 분석]]
→ 기능 상세: [[pages/tools/netminer|NetMiner]]

---

## 1. 예상보다 넓은 지원 범위 — 홍보 기회

기존 이미지("SNA + 텍스트마이닝 도구")보다 실제 기능이 훨씬 광범위하다.

### ERGM 지원 (논문 22편)
- 학술지 트렌드 2위이며 NetMiner가 **ERGM 메뉴를 보유**
- 그간 "ERGM은 R(statnet)만 된다"는 인식이 강해 NetMiner 사용자가 이탈했을 가능성
- **액션**: ERGM 기능 홍보 강화, R statnet과의 비교 콘텐츠 제작

### GNN 지원 (GCN / GraphSAGE / GAT)
- ML 트렌드(논문 11편)에 대응하는 **Graph Neural Network 3종** 탑재
- GUI 환경에서 GNN을 제공하는 도구는 사실상 NetMiner가 유일
- **단, Social Networks 학술지 수집 논문에서 GNN을 방법론으로 직접 사용한 사례는 거의 없음**: GNN 태그가 붙은 3편(Aggrawal 2022 링크예측, Koskinen 2023 다층네트워크, Berenhaut 2025 응집도)도 실제로는 GNN 방법론 논문이 아닌 오태깅. GNN은 SNA 전문지보다 CS/ML 학술지 중심.
- 즉, GNN은 **현재 학계 수요가 큰 방법론이 아니라 미래 선점 포지셔닝** 관점에서 접근해야 함
- SNA 연구자에게 진입장벽을 낮추는 차별화 포인트로 활용 가능 (코딩 없이 GNN)
- **액션**: GNN 기능 케이스 스터디, 코딩 없는 GNN 분석 콘텐츠 (단, 긴급도는 ERGM보다 낮음)

### BERTopic 탑재
- LDA 한계를 극복한 최신 토픽모델링 (BERT 임베딩 기반 클러스터링)
- NetMiner가 LDA + BERTopic + BERTrend 모두 지원 → 토픽모델링 풀 스택
- **단, Social Networks 학술지 수집 논문에서 BERTopic 사용 사례 0건**: 토픽모델링 19편 전부 LDA 기반. BERTopic은 SNA 전문지보다 마케팅·커뮤니케이션·CS 학술지에서 확산 중.
- GNN과 동일한 구도 — 현재 학술 수요보다 NetMiner 지원이 앞서 있는 상태. "이미 갖추고 있다"는 미래 선점 포지셔닝이 적합
- **액션**: BERTopic vs LDA 비교 튜토리얼 제작 (단, 타깃은 SNA 학술 연구자보다 마케팅·실무 분석가 중심으로 설정)

### Two-Mode (이분 네트워크) 지원 (논문 19편)
- 다층/이분 네트워크 트렌드(19편)에 Two-Mode 분석 기능으로 대응 가능
- Mode Projection(2-Mode→1-Mode)도 포함
- **액션**: 이분 네트워크 분석 사례 콘텐츠 강화

### Louvain + Leiden 커뮤니티 탐지
- 4종 알고리즘(Betweenness / Modularity / Louvain / Leiden) 보유
- Leiden은 Louvain의 단점을 개선한 최신 알고리즘 — 경쟁 도구 대비 우위
- Network Science 2026: 코어-퍼리퍼리 탐지 논문 등장 — 커뮤니티 탐지의 변형 영역
- **액션**: 알고리즘 비교 콘텐츠, 코어-퍼리퍼리 활용 사례 추가

### 텍스트 → 가치 네트워크 파이프라인 (Network Science 2026 신규)
- keyword-assisted topic model → value network 추출 → 국가간 협상 구조 분석 (Almquist 외)
- NetMiner의 토픽모델링 + 키워드 네트워크 기능으로 **동일 파이프라인 재현 가능**
- 기후협약·정책 담론·국제 협상 분야로 응용 확장 가능 → 새로운 고객 세그먼트
- **액션**: 정책 텍스트 분석 케이스 스터디 제작 (학술보다 정책 실무자 타깃)

### 중심성 기반 네트워크 개입 (Immunization, Network Science 2026)
- 다층 네트워크에서 중심성으로 핵심 노드 식별 → 바이러스/정보 확산 차단 (Asil 외)
- NetMiner: 중심성 분석(✅) + 다층 네트워크(✅) → 개입 대상 선별까지 가능
- 확산 시뮬레이션 기능(❌)이 없어도 "중심성으로 취약 노드 파악" 워크플로우는 제공 가능
- **액션**: 방역/보안/마케팅 영향력 확산 차단 사례 콘텐츠

---

## 2. 실질적 기능 공백 — 이탈 위험

### SAOM / RSiena (논문 15편) ← 가장 큰 공백
- 종단 네트워크에서 네트워크 변화와 행동 변화를 **동시 모델링**하는 유일한 방법론
- R 패키지 RSiena로만 가능 → 고급 연구자의 **R 이탈 주요 원인**
- ERGM과 함께 통계적 네트워크 모델링의 양 축 (합산 37편 = 최다)
- **액션**: "ERGM은 NetMiner로, SAOM은 RSiena 연계" 워크플로우 제안 or 장기 개발 검토

### 종단 분석 (논문 22편) — 부분 공백
- 정적(static) 네트워크 분석은 강하나, **시간에 따른 네트워크 변화 추적** 기능 약함
- SAOM 부재와 연결된 문제
- **액션**: 시계열 네트워크 시각화 기능이라도 강화

### 확산 / 전파 시뮬레이션 (논문 10편)
- SIR/SIS 등 확산 모델 시뮬레이션 기능 없음
- 네트워크 기반 전파 연구 수요 증가 대비 공백
- **액션**: 단순 확산 모델 시뮬레이션 기능 추가 검토

---

## 3. 포지셔닝 재정의

기존 메시지: *"SNA + 텍스트마이닝 통합 도구"*

→ 업데이트 메시지 후보:
> **"SNA부터 GNN까지 — 코딩 없이 네트워크 분석 전 파이프라인"**
> - 네트워크 구조 분석 (중심성, 커뮤니티, ERGM)
> - 텍스트 마이닝 (LDA, BERTopic, 의미연결망)
> - 그래프 머신러닝 (GCN, GraphSAGE, GAT)
> - 통계 검증 (회귀, MR-QAP)

---

## 4. 우선순위 정리

| 우선순위 | 액션 | 근거 |
|---------|------|------|
| 🔴 즉시 | ERGM 기능 홍보 (콘텐츠·세미나) | 26편 트렌드, 지원 중이나 미홍보 |
| 🟠 단기 | 에고넷 수집→분석 워크플로우 콘텐츠 | 10편 트렌드 — 수집 도구(Network Canvas·Trellis·GENSI) 결과물을 NetMiner Ego Network Extract로 분석하는 파이프라인. Extension(SNS/Biblio/News)과는 별개 |
| 🟠 단기 | Two-Mode / 이분 네트워크 사례 | 22편 트렌드 대응 |
| 🟠 단기 | GNN 케이스 스터디 제작 | 차별화 포인트, 현재 학술 수요 낮음 — 미래 선점 포지셔닝 |
| 🟠 단기 | BERTopic 튜토리얼 | 학술 수요 낮음 — 실무·마케팅 분석가 타깃, 미래 선점 포지셔닝 |
| 🟡 중기 | 종단 네트워크 시각화 강화 | 30편 트렌드 2위, 부분 대응 가능 |
| 🟡 중기 | SAOM 연계 워크플로우 가이드 | 18편, R 연계로 보완 |
| 🔵 장기 | 확산 시뮬레이션 기능 | 10편, 개발 비용 대비 검토 필요 |

---

## 위키 연관

- [[pages/insights/sna_method_frequency|SNA 방법론 빈도 분석]]
- [[pages/tools/netminer|NetMiner 전체 기능]]
- [[pages/tools/other_tools|경쟁 도구 (RSiena 등)]]
- [[pages/concepts/multilayer_network|다층 네트워크]]
- [[pages/concepts/causal_inference_networks|인과 추론과 네트워크]]
