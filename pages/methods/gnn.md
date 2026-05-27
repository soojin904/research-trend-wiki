---
title: "GNN / 그래프 신경망 (Graph Neural Networks)"
tags: [gnn, graph-neural-network, link-prediction, node-classification, knowledge-graph]
netminer_support: "✅ 지원 (실사용 2–3건)"
---

# GNN / 그래프 신경망 (Graph Neural Networks)

그래프 구조 데이터에 딥러닝을 적용하는 방법론. 노드를 이웃 노드 표현의 집계로 반복 업데이트하여 구조적 패턴을 학습한다. SNA 학술지 2020–2026에서 15편이 활용했고(8위), 응용 분야에서는 지식 그래프·추천 시스템·텍스트-그래프 융합 방향으로 성장 중이다.

---

## 핵심 원리

노드 $v$의 $k$번째 레이어 표현:
$$h_v^{(k)} = \text{AGGREGATE}^{(k)}\left(\{h_u^{(k-1)}: u \in \mathcal{N}(v)\}\right)$$

이웃 노드의 표현을 집계(평균, 합산, 어텐션 등)하여 현재 노드의 표현을 갱신. 레이어를 쌓을수록 더 넓은 이웃 정보를 통합한다.

---

## 주요 GNN 아키텍처

| 모델 | 집계 방식 | 특징 | 주요 응용 |
|------|-----------|------|----------|
| **GCN** (Graph Convolutional Network) | 스펙트럼 기반 평균 | 단순, 이론 기반 | 노드 분류, 링크 예측 |
| **GraphSAGE** | 샘플링 기반 집계 | 대규모 그래프 확장성 | 소셜 네트워크 |
| **GAT** (Graph Attention Network) | 어텐션 가중 집계 | 이웃 중요도 차별화 | 의미 있는 이웃 선택 |
| **HAN** (Heterogeneous Attention Network) | 이종 그래프 어텐션 | 노드 유형·관계 유형 혼합 | 지식 그래프, 추천 |
| **GIN** (Graph Isomorphism Network) | WL 테스트 기반 | 표현력 이론적 최강 | 그래프 분류 |

---

## 적용 유형

| 유형 | 설명 | SNA 예시 |
|------|------|----------|
| **링크 예측** | 미형성 연결 예측 | 친구 추천, 협력 가능성 |
| **노드 분류** | 네트워크 위치 기반 속성 예측 | 범죄 가담 예측, 이탈 예측 |
| **그래프 분류** | 전체 그래프 수준 예측 | 단백질 기능, 분자 특성 |
| **지식 그래프 완성** | 누락 관계 추론 | 엔티티 관계 추론 |

---

## SNA 학술지 사용 사례 (2020–2026)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2022_aggrawal_link_prediction\|Aggrawal & Anand (2022)]] | GNN 기반 링크 예측 방법론 체계화 | 네트워크 위상 기반 유사도 vs GNN 비교 |
| [[pages/papers/sna/2024_filippimaz_modeling_nonlinear_effects_wit\|Filippi-Mazzola & Wit (2024)]] | DREAM — 신경망 기반 관계 이벤트 모형 | 800만 노드·1억 이벤트 처리; REM 대비 계산 효율성 우수 |
| [[pages/papers/sna/2023_tomlinson_graphbased_methods_for_discret\|Tomlinson & Benson (2023)]] | 그래프 학습으로 이산 선택 모형 향상 | 소셜 네트워크 구조 통합이 다항 로짓 개선 |

---

## 응용 분야 사용 패턴 (2026, 379편 기반)

| 맥락 | 편수 | 주요 모델 |
|------|------|----------|
| **지식 그래프 구축 / 완성** | ~8 | HAN, TransE, RotatE |
| **추천 시스템** | ~5 | GraphSAGE, LightGCN |
| **텍스트-그래프 융합** | ~4 | Graph-BERT, DAGNN |
| **이종 그래프 분류** | ~2 | HAN, HGT |

> **CS 방법론 논문 집중**: 응용 분야 GNN 논문의 상당수는 실제 도메인 적용보다 GNN 아키텍처 제안·비교가 중심. 도메인 실사용 비율은 아직 낮음.

**이머징 트렌드**: 
- **GraphRAG** — 지식 그래프 + RAG 결합으로 LLM 추론 능력 강화 (chunks 8, 9에서 다수 등장)
- **이종 그래프 (Heterophilic GNN)** — 동질적 이웃 가정을 완화한 모델

---

## NetMiner 지원 현황

✅ **지원** — NetMiner는 GNN 기능을 내장하지만 SNA 학술지 실제 논문에서 NetMiner의 GNN 기능 사용 사례는 2–3건 수준.

**현실적 포지셔닝**:
- 전통 SNA(중심성, 군집 탐지)의 확장 도구로 미래 선점 가능
- 학술 연구보다 산업 응용(추천, 지식 그래프)에서 GNN 성장 중
- 연구자 사용: Python `PyTorch Geometric` / `DGL` 선호 — NetMiner GUI의 차별화 필요

**추가 도구**:
- `PyTorch Geometric` — GNN 연구 표준 라이브러리
- `DGL` (Deep Graph Library) — 대규모 그래프 처리
- `NetworkX` — 전통 SNA + ML 특징 추출

---

## 관련 페이지

- [[pages/methods/ml|전통 ML]] — GNN 이전의 그래프 ML (링크 예측, 노드 분류)
- [[pages/methods/community_detection|커뮤니티 탐지]] — GNN 기반 군집화와 전통 방법 비교
- [[pages/methods/bayesian_network_model|Bayesian / 잠재공간 모델]] — 임베딩 기반 방법과의 경계
- [[pages/methods/longitudinal_network|종단 / 동적 네트워크]] — 동적 네트워크 GNN (DREAM)
- [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026)]]
- [[pages/insights/sna_method_frequency|SNA 방법론 빈도 (2021–2026)]]
