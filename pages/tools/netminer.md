---
title: "NetMiner"
tags: [tools, netminer, sna, text-mining, machine-learning]
---

# NetMiner

사이람(Cyram Inc.)이 개발한 소셜 네트워크 분석 및 데이터 마이닝 소프트웨어.
이 위키에 수집된 실사용 논문 43편(PDF 5편 + KCI/OpenAlex 38편)에서 사용됨.

## 전체 기능 메뉴 (현재 버전)

### Pre-process (전처리)
| 기능 | 세부 |
|------|------|
| Value Transform | Diagonal, Dichotomize, Missing Value, Recode |
| Network Transform | Symmetrize, Transpose, Merge (Layers/Multiple link), 2-Mode→1-Mode Projection, Ego Network Extract |
| Pruning | Backbone, Remove Isolates |
| Text(English, Korean, Chinese supported) | Tokenizer, Word Network (Sliding Window / Co-occurrence), Dictionary Generate (Thesaurus / Compound Words / Exception Words)|

### Network (네트워크 분석)
| 기능 | 세부 |
|------|------|
| Neighbor | Degree, Structural Hole, Assortativity |
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
| Evaluation | Confusion Matrix |
| XAI | SHAP |
| Inference | — |
| Clustering | k-means |
| Dimension Reduction | PCA (사용자 확인, 2026-10-13) |

### Text (텍스트 분석)
| 기능 | 세부 |
|------|------|
| Word Statistics | — |
| **BERTopic** | **BERTopic, BERTrend. 결과물에 토픽 간 코사인 유사도 매트릭스 포함(사용자 확인, 2026-10-11)** |
| **LDA** | **Raw Text, TDM** |
| Topic Evaluation(Perplexity, Coherence) | Raw Text, TDM |

### Visualize (시각화)
| 기능 | 세부 |
|------|------|
| Network | 1-Mode (Force Atlas 2, Fruchterman-Reingold, Force, D3 Force, Kamada-Kawai, Clustered), 2-Mode, Multi-Mode |
| Chart | Scatter, Box, Pie, Bar, Line, Radar, Tree Map, Word Cloud |
| Flow/Relation | Arc Diagram, Chord Diagram, Sankey Diagram |

#### Visualize - 캔버스 UI 기능 (v5.2.1, 2026-09)
| 기능 | 세부 |
|------|------|
| 노드 검색 | 라벨(이름) 입력 시 해당 노드로 자동 이동(Pan/Zoom) + 하이라이트 |
| 우클릭 컨텍스트 메뉴 | Select Neighbor(인접 노드 확장 선택), 에고 노드 보기(선택 노드 중심 전환), 새 탭에서 시각화(선택 영역만 서브그래프로 분리) |
| 라벨 스타일 동기화 | Sync with Node Size(라벨 크기를 노드 크기에 연동), Sync with Node Color(라벨·링크 색을 그룹/노드 색상에 통일, 링크 그라데이션 포함) |
| 멀티모드 네트워크 시각화 | 서로 다른 노드셋(예: 저자/논문/키워드)을 한 화면에 통합 시각화 |

> 출처: `03_marketing/outputs/contents/storyboard/2026-09-17_시각화업데이트/` 쇼츠 스토리보드 4건

#### Visualize - 캔버스 UI 추가 기능 (미출시 포함, 사용자 확인 2026-10-13)
| 기능 | 세부 |
|------|------|
| 그룹 축소(Collapse/Expand) | 클러스터드 맵에서 그룹을 1개 점(그룹 노드)으로 축소. 그룹명 라벨 + 소속 노드 수 배지. 마지막 클러스터는 축소 불가. 점 색상·크기는 Preferences > Styling > Node > Group Node에서 설정 |
| Undo/Redo | 캔버스 작업(마우스 동작, 스타일 적용, 툴바의 노드/링크 라벨 표시·숨김, 링크 화살표 머리 표시·숨김(Directional Link Style), 상하/좌우 반전(Flip) 포함) 최대 10단계 저장, Ctrl+Z/Ctrl+Y. 최상단 툴바 아이콘, 현재 시각화에만 적용, 최대 3개 시각화 탭 동시 지원 |
| 노드 속성 확장 | 우클릭 속성 창에 에고넷 크기, In/Out Degree 추가 표시 |
| Show Top (%) | 노드/링크 라벨 크기 연동 시 속성 값 상위 %(기본 10, 1~100)의 라벨만 표시. 수치형은 큰 값순, 텍스트형은 가나다순 |
| Auto Hide Small Labels | 시각화 툴바 토글(기본 켜짐). 화면 배율에 따라 작은 라벨 자동 숨김. Show Top (%) 적용 후 추가 적용 |

### Extension (확장)
| 기능 |
|------|
| SNS Data Collector(유튜브) | 
| Biblio Data Collector(openalex, kci, springer) |
| News Data Collector(한국 뉴스) |

### Lab (실험적 기능)
| 기능 |
|------|
| Knowledge Graph |
| Sentiment Analysis(English, German, Dutch, French, Spanish, Italian, Korean) - BERT 기반 감성 분류 모델 |

---

## 이 위키의 사용 사례

총 43편 (PDF 원문 5편 + KCI/OpenAlex 메타데이터 수집 38편, 2026-07-31 기준). 대표 사례:

| 논문 | NetMiner 활용 내용 |
|------|-------------------|
| [[pages/papers/netminer/2024_jang_happiness_topic_nn|Jang & Nemoto (2024)]] | LDA 토픽모델링 + 머신러닝 |
| [[pages/papers/netminer/2022_morashti_sustainable_packaging|Morashti 외 (2022)]] | 통계 + 키워드 네트워크 + LDA |
| [[pages/papers/netminer/2022_park_digital_healthcare_network|Park 외 (2022)]] | 네트워크 분석 + 중심성 |
| [[pages/papers/netminer/2022_jeon_social_network_health_elderly|Jeon & Park (2022)]] | SNA + 다중회귀 |
| [[pages/papers/netminer/2021_kang_csr_ad_semantic_network|강윤지 외 (2021)]] | 의미연결망 + LDA |

전체 목록: [[index|index.md]] "A. NetMiner 사용 논문" 섹션 또는 `pages/papers/netminer/` 폴더 직접 탐색.

> 참고: 위 43편은 위키에 개별 페이지로 만든 사례만 집계. NetMiner 전체 "활용"(실사용 확정) 논문은 `03_marketing/netminer_info/nm-reference/research_metadata.xlsx` 기준 724편(2016년 이후)이며, 전수 관리는 netminer_info에서 담당한다.

---

## 최근 3년 NetMiner 활용 트렌드 (2023년~현재, 297건)

> 분석 기준: research_metadata.xlsx `구분`="활용" & `year`≥2023, 297건 (2026-09-22 분석, 2026-10-02 본 페이지로 통합·재구성). **이 섹션은 항상 최근 3년 창으로 롤링 갱신** — 재분석 시 연도 하한을 그 시점 기준으로 다시 계산.

### ① 전체 활용 현황 — 분야·목적·데이터

**연구 분야 비중**: 의학·보건·간호학(30.6%) > 교육학(26.3%) > 체육·스포츠과학(12.8%) — 상위 3개 분야가 69.7% 차지. 간호학은 신규간호사 적응·환자안전·소진(burnout) 등 반복 재생산 클러스터가 뚜렷.

**활용 방향(목적) 비중**: 연구동향/지식지형 분석(39.4%) > 질적·학술 텍스트 토픽분석(22.9%) > 뉴스·미디어 이슈분석(16.8%) > 소셜미디어 반응분석(8.8%) > 정책문서 분석(7.7%) > 순수 관계망 분석(4.4%, 13건 — 상세는 ② 참조).

**주요 데이터 유형**: 학술지 초록/키워드(KCI·RISS·WoS·PubMed 서지), 뉴스 빅데이터(빅카인즈), 질적 텍스트(저널·피드백일지·FGI·개방형 설문), 소셜미디어(YouTube·앱리뷰·SNS), 정책문서, 순수 관계형 데이터(②).

**마케팅 전략 제언 3가지**:
1. 간호·보건의료 학회 대상 "저널/피드백 텍스트 네트워크 분석 실습" 세미나 최우선 추진
2. 교육학·유아교육 연구자 대상 "RISS 수집 + 키워드 네트워크 + LDA" 표준 워크플로우 튜토리얼 재발간
3. "텍스트 마이닝 전용 도구"라는 인식을 넘어 순수 관계망 분석 역량 재소구 (② 참조)

### ② 순수 SNA(관계망) 논문만 — 텍스트 아닌 실제 개체 간 관계 데이터 (4.4%, 13건)

NetMiner는 텍스트 마이닝 전용 도구가 아니라, 실제 개체(Actor) 간 인접행렬·노드-링크 데이터를 입력해 SNA를 수행한 사례도 보유. 최근 3년 "활용" 297건 중 **13건(4.4%)**이 텍스트가 아닌 순수 관계형 데이터 사용.

| 유형 | 데이터 성격 | 대표 사례 (2023년 이후) |
|------|------------|----------|
| 조직·이해관계자 관계망 | 기관 간 연계·협력 Matrix | 노인·치매 돌봄서비스 공급기관 21개 간 연계 네트워크(한국농촌간호학회지, 2025), 충청권 대학 공동연구 네트워크 연도별 변화(한국비교정부학보, 2025) |
| 인적·대인관계망 | 설문 기반 실제 인적 네트워크 | 종합병원 간호단위 간호사 업무·정보교류 관계망(한국간호교육학회지, 2024), 후기 청소년 대인관계 강도 네트워크(Brain and Behavior, 2025) |
| 연구자 공저 네트워크 | 저자-저자 공동 집필 Matrix | 대한가정학회지 공저자 네트워크 분석 2010~2022(Human Ecology Research, 2024) |

→ **마케팅 시사점**: "설문/조직 데이터로 실제 관계망 그리기" 가이드북 콘텐츠로 조직연구·정책 네트워크 연구자(텍스트마이닝 외 신규 세그먼트) 공략 가능.

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
| 부호화 네트워크(signed network) / 균형이론 (신규 확인, 2026-10-14) | ❌ 미지원 | 신규 기능 공백 — Science Advances 게재(Peixoto 참여) 등 저명도 높은 최신 트렌드 |

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
- **Arc/Chord/Sankey Diagram** → 관계·흐름 시각화까지 커버 범위 확장
- **GNN (GCN/GraphSAGE/GAT) 보유** → 학술 최신 트렌드 대응 가능한 유일한 GUI 도구
- **BERTopic 탑재** → LDA를 넘어 최신 토픽모델링까지 커버
- **Louvain + Leiden** → 커뮤니티 탐지 최신 알고리즘 보유
- **다층/이분 네트워크** 기능 있으나 트렌드 대비 홍보 부족 가능성
- 논문 인용 사례 5편 → 학술 신뢰도 마케팅 가능
