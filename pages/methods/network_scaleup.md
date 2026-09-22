---
title: "Network Scale-Up / ARD (네트워크 규모 추정 방법)"
tags: [network-scale-up, nsum, ard, hidden-population, respondent-driven, hard-to-reach]
netminer_support: "❌ 미지원"
updated: 2026-09-22
---

# Network Scale-Up / ARD (네트워크 규모 추정 방법)

직접 접근이 어려운 집단(은닉 집단, hard-to-reach population)의 규모를 응답자의 사회적 연결망 정보로 간접 추정하는 방법론. **SNA 전문 학술지 전수 318편 중 9편**이 활용한다 ([[pages/insights/sna_method_frequency|방법론 빈도 분석]], 2026-09-22 기준). 공중보건·사회학·선거 연구 등 광범위한 영역에서 사용된다.

> **2026-09-22 갱신**: 이전 집계(7편)보다 편수가 늘었을 뿐 아니라, **전용 리뷰 논문**과 **Bayesian 통합 프레임워크 논문**이 동시에 등장해 하나의 독립 하위 분야로 정착한 것이 확인되었다. 다만 이 분야는 GUI SNA 소프트웨어보다 R/Stan 패키지 영역에 가깝다 — **학술 트렌드로 기록하되 곧바로 NetMiner 기능 공백으로 환산하지 말 것**(아래 지원 현황 참조).

## 핵심 개념

### Network Scale-Up Method (NSUM) 원리

응답자에게 "X라는 집단에 속하는 사람을 몇 명 알고 있나요?"라고 물어 목표 집단 규모를 추정:

$$\hat{N}_{target} = \frac{\sum_i y_{i,target}}{\sum_i y_{i,known}} \times N_{known}$$

- $y_{i,target}$: 응답자 i가 아는 목표 집단 구성원 수
- $N_{known}$: 알려진 규모의 기준 집단 크기
- **핵심 가정**: 목표 집단과 기준 집단에 대한 평균 가시성(visibility)이 동일

### Aggregated Relational Data (ARD)

NSUM 과정에서 수집되는 집계된 관계 데이터. ARD에서 개인 네트워크 규모·구조를 추론하거나 집단 간 관계 패턴을 분석하는 데 활용된다.

### 주요 방법 변형

| 방법 | 설명 |
|------|------|
| **기본 NSUM** | 응답자 알림 수 기반 추정 |
| **포획-재포획 결합** | 중복 보고 빈도로 추정치 보정 (Feld 2026) |
| **공변량 기반 모형 (covariate-based)** | 지인 접촉 패턴을 공변량으로 설명 — 가시성 가정 완화 (Baum 2025) |
| **통합 Bayesian / Stan 프레임워크** | 흩어져 있던 NSUM 추정량들을 단일 계층 베이지안 틀로 통합 (Ward 2026) |
| **스펙트럼 적합도 검정** | 부분 관측 네트워크·ARD 모형의 적합도 검정 (Lubold 2025) |
| **RDS** (Respondent-Driven Sampling) | 은닉 집단 내 연쇄 표집 |
| **LSPCM 기반 ARD** | 잠재 공간 모형으로 ARD에서 구조 추론 |
| **ARD → ABM 입력** | 추정된 관계 구조를 행위자 기반 모형의 초기 네트워크로 사용 (Lee 2025) |

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2026_lubbers_nsm_ard\|Lubbers 외 (2026)]] | NSUM·ARD의 발전 역사와 응용 분야 종합 리뷰 — 은닉 집단 추정에서 사회 구조 파악까지 | ARD가 단순 규모 추정을 넘어 네트워크 구조 연구 도구로 진화 |
| [[pages/papers/sna/2026_arevalillo_network_scaleup_methods\|Arevalillo 외 (2026)]] | ARD로 스페인 총선 투표 의향 간접 추정 — 다양한 NSUM 기법 비교 | 주요 여론조사 기관과 유사한 정확도; 민감 정보 노출 위험 낮은 대안 |
| [[pages/papers/sna/2026_feld_estimating_unknown_populations\|Feld & McGail (2026)]] | NSUM 기준 집단과 포획-재포획 결합 하이브리드 추정 — 페이스북 데이터로 신입생 규모 추정 검증 | 중복 보고로 외생 정보 없이 추정치 보정 가능; 가시성 차이 있는 집단에 적합 |
| [[pages/papers/sna/2025_vlker_whos_your_extended\|Völker 외 (2025)]] | 네덜란드 2021년 NSUM으로 성인 확장 지인 네트워크 규모(중앙값 446명)·동질성 분석 | 취업 상태·가구원 수·나이·소득이 더 큰 네트워크와 연관; 성별·교육 분리 확인 |
| [[pages/papers/sna/2026_almquist_homelessness_personal_network\|Almquist 외 (2026)]] | RDS 표집으로 킹 카운티 노숙 경험자 3,000명+ ARD 수집 — 퍼스널 네트워크 3년 종단 분석 | 친밀 우정 네트워크 감소(4.9→4.19), 가족 동거 증가 — 고립 심화 신호 |
| [[pages/papers/sna/2026_ward_bayesian_modeling_for_aggregat\|Ward 외 (2026)]] | ARD 추정량들을 **단일 계층 베이지안 관점으로 통합** — Stan 기반 구현 제공 | 기존 NSUM 변형들이 동일 모형의 특수 사례임을 보임; 분야 성숙의 신호 |
| [[pages/papers/sna/2025_baum_explaining_contact_patterns\|Baum 외 (2025)]] | 지인 네트워크 접촉 패턴을 설명하는 **새로운 공변량 기반 모형** | 균일 가시성 가정 대신 공변량으로 접촉 확률 구조화 |
| [[pages/papers/sna/2025_lubold_spectral_goodnessoffit_tests_f\|Lubold 외 (2025)]] | 완전·부분 관측 네트워크 데이터에 대한 **스펙트럼 적합도 검정** | ARD처럼 부분 정보만 있는 경우의 모형 검증 수단 |
| [[pages/papers/sna/2025_lee_use_aggregated_relational\|Lee 외 (2025)]] | ARD를 **행위자 기반 모형(ABM)의 네트워크 입력**으로 활용 | 전수 네트워크 없이도 시뮬레이션용 현실적 구조 생성 |
| [[pages/papers/sna/2025_plaza_networked_inequality_the_role\|Plaza 외 (2025)]] | 확장 지인 네트워크의 규모·이질성 변화와 불평등 태도의 관계 | ARD 기반 네트워크 지표를 사회 태도 설명 변수로 사용 |

## NetMiner 지원 현황

**❌ 미지원** — NetMiner는 NSUM/ARD 기반 은닉 집단 규모 추정 기능을 제공하지 않는다 ([[pages/tools/netminer|기능 목록]] 확인).

**대안 도구**:
- R `NSUM` 패키지
- R `RDS` 패키지 (Respondent-Driven Sampling)
- Stata `networkscaleup` 모듈
- Python 커스텀 구현

### 제품 기획 시사점 (학술 수요 ≠ 지원 여부 분리)

- **학술 수요**: 9편, 신규 식별 클러스터. 리뷰 논문·통합 프레임워크 논문이 나올 만큼 정착했다.
- **NetMiner 지원**: 없음. **다만 이를 곧바로 "기능 공백"으로 기록하는 것은 부적절하다.** NSUM/ARD는 네트워크 *분석* 도구가 아니라 표본 설계·추정 통계 영역이며, 실사용은 R/Stan 코드 기반이다. GUI 도구가 진입해서 얻을 이득이 작다.
- **NetMiner 연관 활용(성립하는 워크플로우)**: NSUM/ARD로 수집된 지인 네트워크 데이터를 에고 네트워크 형태로 변환한 뒤, NetMiner의 **Ego Network Extract** 및 퍼스널 네트워크 분석·시각화로 잇는 경로는 실제로 성립한다 → [[pages/concepts/egocentric_network_design|에고중심 네트워크 연구설계]]
- 반대로 NSUM 자체를 NetMiner 기능으로 홍보하는 연결은 워크플로우가 성립하지 않으므로 금지.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석 (318편 전수)]]
- [[pages/methods/bayesian_network_model|Bayesian/잠재공간 모델]] (ARD에서 잠재 공간 추론)
- [[pages/concepts/egocentric_network_design|에고중심 네트워크 연구설계]] (동일한 "측정 방법론" 흐름)
- [[pages/concepts/personal_network|퍼스널 네트워크]] (NSUM이 측정하는 확장 네트워크)
- [[pages/tools/netminer|NetMiner]]
- [[pages/tools/other_tools|Other Tools (ERGM·SAOM 지원 도구)]]
