---
title: "NetMiner"
tags: [tools, netminer, sna, text-mining, machine-learning]
---

# NetMiner

사이람(Cyram Inc.)이 개발한 소셜 네트워크 분석 및 데이터 마이닝 소프트웨어.
이 위키의 기존 PDF 소스 논문 5편 **전부**에서 사용됨.

## 전체 기능 메뉴 (현재 버전)

### Pre-process (전처리)
| 기능 | 세부 |
|------|------|
| Value Transform | Diagonal, Dichotomize, Missing Value, Recode |
| Network Transform | Symmetrize, Transpose, Merge (Layers/Multiple link), 2-Mode→1-Mode Projection, Ego Network Extract |
| Pruning | Backbone, Remove Isolates |
| Text | Tokenizer, Word Network (Sliding Window / Co-occurrence), Dictionary Generate (Thesaurus / Compound Words / Exception Words) |

### Network (네트워크 분석)
| 기능 | 세부 |
|------|------|
| Neighbor | Degree, Assortativity |
| Connection | Shortest Path |
| Subgroup | Component, Clique, Community (Betweenness / Modularity / Louvain / Leiden), k-Core |
| **Centrality** | **Degree, Closeness, Betweenness, Eigenvector, Status, PageRank, HITS** |
| Similarity | Structural Equivalence, SimRank |
| Position | Blockmodel (Conventional), Brokerage |
| Properties | Network Metric, Group Metric |
| **Two-Mode** | **Degree, Degree Centrality, Closeness Centrality, Betweenness Centrality** |
| Models | **ERGM** |

### Statistics (통계)
| 기능 | 세부 |
|------|------|
| Univariate | Frequency, Distribution, t-Test (One Sample) |
| Bivariate | Contingency Table, t-Test (Independent/Paired), ANOVA, Kruskal-Wallis, Correlation, Autocorrelation |
| Multivariate | Linear Regression, Logistic Regression, **MR-QAP** (Linear/Logistic), Hierarchical Clustering |

### Machine-Learning (머신러닝)
| 기능 | 세부 |
|------|------|
| Learn (Classical) | AdaBoost, CART, Gradient Boosted Trees, kNN, Linear/Logistic Regression, MLP, Naive Bayes, Random Forest, SVM |
| **Learn (Graph)** | **GCN, GraphSAGE, GAT** |
| XAI | SHAP |
| Inference | — |
| Clustering | k-means |

### Text (텍스트 분석)
| 기능 | 세부 |
|------|------|
| Word Statistics | — |
| **BERTopic** | **BERTopic, BERTrend** |
| **LDA** | **Raw Text, TDM** |
| Topic Evaluation | Raw Text, TDM |

### Visualize (시각화)
| 기능 | 세부 |
|------|------|
| Network | 1-Mode (Force Atlas 2, Fruchterman-Reingold, Force, D3 Force, Kamada-Kawai, Clustered), Multi-Mode |
| Chart | Scatter, Box, Pie, Bar, Line, Word Cloud |

### Extension (확장)
| 기능 |
|------|
| SNS Data Collector |
| Biblio Data Collector |
| News Data Collector |

### Lab (실험적 기능)
| 기능 |
|------|
| Knowledge Graph |
| Sentiment Analysis |

---

## 이 위키의 사용 사례
| 논문 | NetMiner 활용 내용 |
|------|-------------------|
| [[pages/papers/netminer/2024_jang_happiness_topic_nn|Jang & Nemoto (2024)]] | LDA 토픽모델링 + 머신러닝 |
| [[pages/papers/netminer/2022_morashti_sustainable_packaging|Morashti 외 (2022)]] | 통계 + 키워드 네트워크 + LDA |
| [[pages/papers/netminer/2022_park_digital_healthcare_network|Park 외 (2022)]] | 네트워크 분석 + 중심성 |
| [[pages/papers/netminer/2022_jeon_social_network_health_elderly|Jeon & Park (2022)]] | SNA + 다중회귀 |
| [[pages/papers/netminer/2021_kang_csr_ad_semantic_network|강윤지 외 (2021)]] | 의미연결망 + LDA |

---

## 기능-트렌드 매핑 인사이트 (2021–2026 Social Networks 139편 기반)

→ 상세 분석: [[pages/insights/sna_method_frequency|SNA 방법론 빈도 분석]]
→ 상세 분석: [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]]

| 학술 트렌드 (논문 수) | NetMiner 지원 여부 | 포지셔닝 |
|----------------------|:-----------------:|---------|
| 에고중심 / 퍼스널 네트워크 (30) | ✅ Ego Network Extract | **강점 영역 — 마케팅 강화** |
| ERGM (22) | ✅ ERGM 메뉴 | **지원 확인 — 적극 홍보 필요** |
| 종단 / 동적 네트워크 (22) | ⚠️ 부분 (정적 분석 중심) | 개선 여지 |
| 중심성 분석 (19) | ✅ 7종 중심성 | **핵심 강점** |
| 토픽모델링 / LDA (19) | ✅ LDA + BERTopic | **경쟁 우위 — SNA지에 진입 확인** |
| 다층 / 이분 네트워크 (19) | ✅ Two-Mode, Merge Layers | **지원 확인 — 홍보 부족 가능성** |
| SAOM / RSiena (15) | ❌ 미지원 | 고급 연구자 이탈 요인 |
| Bayesian / MCMC (11) | ❌ 미지원 | 동일 |
| ML / GNN (11) | ✅ GCN, GraphSAGE, GAT | **GNN 지원 — 차별화 포인트** |
| 커뮤니티 탐지 (7) | ✅ Louvain, Leiden 등 4종 | **강점 — 최신 알고리즘 보유** |
| 확산 / 전파 (10) | ⚠️ 없음 (간접 지원) | 기능 공백 |
| 의미연결망 / 키워드 네트워크 (3) | ✅ Word Network | **독보적 강점 (국내)** |

---

## 경쟁 도구 비교
| 도구 | SNA | 텍스트 | 통계 | GNN | GUI | 비용 |
|------|:---:|:------:|:---:|:---:|:---:|:----:|
| **NetMiner** | ✅ | ✅ | ✅ | ✅ | ✅ | 유료 |
| R (igraph+RSiena) | ✅ | ✅ | ✅ | △ | ❌ | 무료 |
| Python | ✅ | ✅ | ✅ | ✅ | ❌ | 무료 |
| Gephi | ✅ | ❌ | ❌ | ❌ | ✅ | 무료 |
| UCINET | ✅ | ❌ | △ | ❌ | ✅ | 유료 |

→ **NetMiner 유일한 포지션**: SNA + 텍스트마이닝 + GNN + 통계를 GUI 환경에서 통합 지원

---

## 마케팅 인사이트
- **ERGM 지원 확인** → 그간 "미지원"으로 알려졌을 가능성 — 적극 홍보 필요
- **GNN (GCN/GraphSAGE/GAT) 보유** → 학술 최신 트렌드 대응 가능한 유일한 GUI 도구
- **BERTopic 탑재** → LDA를 넘어 최신 토픽모델링까지 커버
- **Louvain + Leiden** → 커뮤니티 탐지 최신 알고리즘 보유
- **다층/이분 네트워크** 기능 있으나 트렌드 대비 홍보 부족 가능성
- 논문 인용 사례 5편 → 학술 신뢰도 마케팅 가능
