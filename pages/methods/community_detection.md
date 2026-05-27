---
title: "커뮤니티 탐지 (Community Detection)"
tags: [community-detection, modularity, core-periphery, clustering, blockmodel]
netminer_support: "✅ 지원"
---

# 커뮤니티 탐지 (Community Detection)

네트워크에서 내부적으로 밀하게 연결되고 외부적으로 희소하게 연결된 노드 집합(커뮤니티)을 자동으로 식별하는 방법론 군. SNA 학술지 2020–2026에서 11편이 활용하여 공동 10위를 기록했다.

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

✅ 지원 — 주요 커뮤니티 탐지 알고리즘(모듈성 기반, 계층적 군집화 등) 지원. 결과 시각화 및 속성 연계 분석 가능.

**추가 고려**: 잠재 공간 기반 군집(LPCM, LSPCM)은 R/Python 구현이 필요.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/bayesian_network_model|Bayesian/잠재공간 모델]] (잠재 공간 군집화와 연결)
- [[pages/methods/semantic_network_analysis|의미연결망]] (의미 커뮤니티 탐지)
- [[pages/methods/ergm|ERGM]] (블록모델과의 관계)
