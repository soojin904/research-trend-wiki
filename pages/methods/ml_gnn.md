---
title: "ML/딥러닝/GNN (Machine Learning & Graph Neural Networks)"
tags: [machine-learning, deep-learning, gnn, graph-neural-network, link-prediction, embedding]
netminer_support: "✅ 지원 (GNN 포함; 실사용 ≈ 2–3건)"
---

# ML/딥러닝/GNN (Machine Learning & Graph Neural Networks)

네트워크 데이터에 전통적 머신러닝부터 그래프 신경망(GNN)까지 적용하는 방법론 범주. SNA 학술지 2020–2026에서 15편이 활용하여 8위를 기록했다. GNN 실제 사용은 2–3건 수준으로, 대부분은 전통 ML(랜덤 포레스트, 로지스틱 회귀, 링크 예측 등) 적용이다.

## 핵심 개념

### 적용 유형 구분

| 유형 | 설명 | 예시 |
|------|------|------|
| **링크 예측** | 미형성 연결을 예측 | 친구 추천, 협력 가능성 |
| **노드 분류** | 네트워크 위치 기반 속성 예측 | 범죄 가담 예측, 이탈 예측 |
| **커뮤니티 탐지 ML** | 군집 레이블 학습 | GNN 기반 community detection |
| **그래프 분류** | 전체 네트워크 수준 예측 | 단백질 기능, 분자 특성 |
| **동적 네트워크 ML** | 이벤트 기반 비선형 관계 학습 | Relational Event Model + 신경망 (DREAM) |

### GNN 핵심 원리

GNN은 노드를 이웃 노드 표현의 집계로 업데이트:
$$h_v^{(k)} = \text{AGGREGATE}^{(k)}\left(\{h_u^{(k-1)}: u \in \mathcal{N}(v)\}\right)$$

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/2024_lai_predicting_network_members_fro\|Lai 외 (2024)]] | 소셜 미디어 부분 접촉 기록으로 개인 네트워크 구성원 예측 — 머신러닝 모델 개발 | 부분 기록만으로 네트워크 구성원 예측 가능성 시연; 간접 네트워크 측정 방법론 기여 |
| [[pages/papers/2023_tomlinson_graphbased_methods_for_discret\|Tomlinson & Benson (2023)]] | 그래프 학습으로 이산 선택 모형 향상 — 선거 결과·앱 설치 예측 | 소셜 네트워크 구조 통합이 다항 로짓 예측 개선; 앱 설치는 사회적 영향, 사용은 습관 |
| [[pages/papers/2024_filippimaz_modeling_nonlinear_effects_wit\|Filippi-Mazzola & Wit (2024)]] | 신경망 기반 DREAM(관계 이벤트 가산 모형)으로 동적 네트워크 비선형 효과 모델링 | 약 800만 노드·1억 이벤트 처리; REM 대비 계산 효율성 우수 |
| [[pages/papers/2022_aggrawal_link_prediction\|Aggrawal & Anand (2022)]] | 소셜 네트워크 링크 예측 방법론 체계화 — GNN 기반 접근법 포함 | 네트워크 위상 기반 유사도 지표 vs GNN 접근법 비교; SNA 링크 예측 응용 사례 소개 |

## NetMiner 지원 현황

✅ 지원 (GNN 포함) — NetMiner는 GNN을 포함한 ML 기능을 지원하나, SNA 학술지 실제 논문에서 NetMiner의 GNN 기능 사용 사례는 2–3건 수준이다.

**현실적 포지셔닝**:
- 전통 ML(분류, 회귀, 군집화)은 안정적 수요
- GNN은 미래 선점 포지셔닝 가능 — 학술 연구보다 응용(추천, 지식 그래프)에서 성장 중
- BERTopic 등 임베딩 기반 방법론이 텍스트+네트워크 융합 영역에서 부상 중

**추가 도구**:
- Python `PyTorch Geometric`, `DGL` (GNN)
- Python `node2vec`, `DeepWalk` (그래프 임베딩)
- Python `scikit-learn` (전통 ML)

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/bayesian_network_model|Bayesian/잠재공간 모델]] (임베딩과의 경계)
- [[pages/methods/topic_modeling|토픽모델링]] (BERTopic 등 임베딩 기반 토픽)
- [[pages/methods/longitudinal_network|종단/동적 네트워크]] (동적 네트워크 ML)
