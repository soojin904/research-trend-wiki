---
title: "커뮤니티 탐지 (Community Detection)"
tags: [community-detection, modularity, core-periphery, clustering, blockmodel]
netminer_support: "⚠️ 부분 (휴리스틱 알고리즘 ✅ / 모형 기반·검정 기반 ❌)"
updated: 2026-09-22
---

# 커뮤니티 탐지 (Community Detection)

네트워크에서 내부적으로 밀하게 연결되고 외부적으로 희소하게 연결된 노드 집합(커뮤니티)을 자동으로 식별하는 방법론 군. **SNA 전문 학술지 전수 318편 중 24편**(블록모델링·코어-퍼리퍼리 포함, 5위)이 활용한다 ([[pages/insights/sna_method_frequency|방법론 빈도 분석]], 2026-09-22 기준).

> **2026-09-22 갱신의 핵심**: 학계 논의가 "어떤 알고리즘이 더 좋은가"에서 세 방향으로 이동했다 — ① **모형 기반**(확률적 블록모델·잠재공간), ② **통계적 검정**("이 커뮤니티 구조가 유의한가"), ③ **알고리즘 선택 절차의 체계화**. 즉 탐지 실행보다 **결과의 타당성 검증**이 쟁점이다.

## 핵심 개념

### 주요 알고리즘 유형

| 알고리즘 | 원리 | 특징 |
|----------|------|------|
| **모듈성 최적화** (Louvain, Leiden) | 모듈성(Q) 지표 최대화 | 빠르고 확장성 높음 |
| **스펙트럼 군집화** | 라플라시안 행렬 고유값 분해 | 이론적 보장 |
| **블록모델** | 구조적 동치(structural equivalence) | ERGM과 연계 가능 |
| **코어-퍼리퍼리** | 밀한 코어 vs 희소 퍼리퍼리 분리 | 계층 구조 파악 |
| **계층적 군집화** | 덴드로그램 기반 반복 병합/분할 | 다중 해상도 지원 |
| **잠재 공간 군집** | 잠재 위치 모형 + 혼합 모형 | Bayesian 방법과 연결 |

### 최근 쟁점 (318편 전수 기반)

| 쟁점 | 내용 | 대표 논문 |
|------|------|-----------|
| **알고리즘 선택 절차의 체계화** | 후보 알고리즘이 너무 많다는 문제의식에서, 정책 네트워크의 연합(coalition) 식별을 위한 **5단계 선택 프레임워크(BMCD)** 제안 — 탐지 실행 전에 "무엇을 커뮤니티로 볼 것인가"를 먼저 정의 | [[pages/papers/sna/2024_deguilhem_too_many_options_how\|de Guilhem 외 (2024)]] |
| **통계적 검정 기반 탐지** | 커뮤니티 구조의 존재 자체를 **가설 검정**으로 판단 (귀무가설: 구조 없음) | [[pages/papers/sna/2024_yanchenko_generalized_hypothesis_test\|Yanchenko & Sengupta (2024)]] |
| **확률적 블록모델(SBM) 확장** | 연결된 복수 네트워크를 동시에 블록모델링 | [[pages/papers/sna/2022_kulj_stochastic_blockmodeling_linke\|Kejžar 외 (2022)]] |
| **동적 블록모델링** | 시점별 블록 구조 변화 추적 — 접근법별 성능을 몬테카를로로 비교 | [[pages/papers/sna/2022_cugmas_approaches_blockmodeling_dynam\|Cugmas & Žiberna (2022)]] |
| **코어-퍼리퍼리 모형 재정의** | Borgatti-Everett 고전 모형을 **범주 간 밀도 블록 + 부분 연결 코어**로 일반화 | [[pages/papers/sna/2024_estvez_revising_the_borgattieverett_c\|Estévez 외 (2024)]] |
| **다층 + 노드 속성 통합** | 레이어 데이터와 노드 속성을 하나의 데이터 행렬로 통합해 탐지 | [[pages/papers/sna/2023_reittu_network_community_detection\|Reittu 외 (2023)]] |
| **모형 기반 군집 (잠재공간)** | 잠재 공간 차원수와 군집 수를 동시 자동 추론 | [[pages/papers/sna/2025_gwee_modelbased_clustering_for_netw\|Gwee 외 (2025)]] |

### 성능 평가 기준
- **모듈성(Modularity, Q)**: 무작위 그래프 대비 커뮤니티 내 엣지 밀도
- **NMI (Normalized Mutual Information)**: 벤치마크 대비 정확도
- **안정성**: 동일 네트워크 반복 실행 시 일관성

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2020_dao_community_structure_comparativ\|Dao 외 (2020)]] | 수백 개 네트워크에서 주요 커뮤니티 탐지 방법 대규모 비교 평가 | 방법에 따라 생성되는 커뮤니티 유형이 크게 다름; 실용적 선택 가이드 제공 |
| [[pages/papers/sna/2021_kamiski_artificial_benchmark_for_commu\|Kamiński 외 (2021)]] | LFR 벤치마크 대안으로 ABCD 합성 그래프 모델 제안 | LFR 대비 속도·단순성·확장성 우수; 혼합 파라미터 ξ로 직관적 커뮤니티 강도 조절 |
| [[pages/papers/sna/2023_reittu_network_community_detection\|Reittu 외 (2023)]] | 다층 레이어와 노드 속성 데이터를 통합하는 데이터 행렬 기반 커뮤니티 탐지 | 차수를 열로 추가하면 계층적 스케일프리 네트워크 구조와 잘 일치 |
| [[pages/papers/sna/2022_suitner_the_rise_climateaction\|Suitner 외 (2022)]] | 의미 네트워크에 커뮤니티 탐지 알고리즘 적용 → 의미 커뮤니티 시계열 비교 | FridaysForFuture 이후 기후변화 담론의 의미 커뮤니티 구조 변화 확인 |
| [[pages/papers/sna/2022_mayajarieg_use_hierarchical\|Maya-Jariego & González-Tinoco (2022)]] | 반복적 betweenness 노드 제거로 퍼스널 네트워크 내 중첩 하위 집단 계층 탐색 | 밀한 네트워크가 해체에 강인; 명확한 하위 집단은 해체 속도 빠름 |

## NetMiner 지원 현황

**✅ 지원 — 휴리스틱·결정론적 알고리즘**
`Network > Subgroup`: Component, Clique, Community(**Betweenness / Modularity / Louvain / Leiden**), k-Core. `Network > Position`: **Blockmodel (Conventional)**, Brokerage. 계층적 군집화는 Statistics 메뉴에 별도 존재 ([[pages/tools/netminer|기능 목록]] 기준). Leiden 보유는 경쟁 GUI 도구 대비 우위.

**❌ 미지원 — 모형 기반·검정 기반**
확률적 블록모델(SBM) 및 연결 네트워크 SBM, 동적 블록모델링, 커뮤니티 구조 가설 검정, 잠재공간 기반 군집(LPCM/LSPCM), 일반화 코어-퍼리퍼리 모형, 다층+속성 통합 탐지.
- **대안**: R `blockmodeling`(Žiberna), `sbm`, `latentnet`, Python `graph-tool`(SBM)

### 제품 기획 시사점 (학술 수요 ≠ 지원 여부 분리)

- **학술 수요**: 24편. 그러나 그중 "Louvain을 돌렸다"류는 소수이고, 다수가 **탐지 결과의 통계적 타당성·모형화**를 다룬다.
- **NetMiner 지원**: 실행 알고리즘은 최신(Leiden)까지 보유. 부족한 것은 **결과 검증 수단**이다.
- **저비용 기회**: 알고리즘 추가보다 **"내 커뮤니티 구조가 우연인가"를 판정하는 보조 지표**(무작위 그래프 대비 모듈성 유의성, 알고리즘 간 결과 일치도/NMI 비교 뷰)가 개발 비용 대비 효과가 크다. de Guilhem(2024)의 5단계 선택 프레임워크는 **기능이 아니라 콘텐츠·세미나 소재**로도 바로 쓸 수 있다.
- 코어-퍼리퍼리는 현재 NetMiner에 전용 메뉴가 없다 — 블록모델로 우회 가능하나 동일 기능으로 홍보하지 말 것.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석 (318편 전수)]]
- [[pages/methods/bayesian_network_model|Bayesian/잠재공간 모델]] (잠재 공간 군집화·SBM과 연결)
- [[pages/methods/semantic_network_analysis|의미연결망]] (의미 커뮤니티 탐지)
- [[pages/methods/ergm|ERGM]] (블록모델과의 관계)
- [[pages/concepts/multilayer_network|다층 네트워크]] (다층+속성 통합 탐지)
- [[pages/tools/netminer|NetMiner]]
