---
title: "Network Scale-Up / ARD (네트워크 규모 추정 방법)"
tags: [network-scale-up, nsum, ard, hidden-population, respondent-driven, hard-to-reach]
netminer_support: "❌ 미지원"
---

# Network Scale-Up / ARD (네트워크 규모 추정 방법)

직접 접근이 어려운 집단(은닉 집단, hard-to-reach population)의 규모를 응답자의 사회적 연결망 정보로 간접 추정하는 방법론. SNA 학술지 2020–2026에서 7편이 활용하여 13위를 기록했다. 공중보건·사회학·선거 연구 등 광범위한 영역에서 사용된다.

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
| **RDS** (Respondent-Driven Sampling) | 은닉 집단 내 연쇄 표집 |
| **LSPCM 기반 ARD** | 잠재 공간 모형으로 ARD에서 구조 추론 |

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2026_lubbers_nsm_ard\|Lubbers 외 (2026)]] | NSUM·ARD의 발전 역사와 응용 분야 종합 리뷰 — 은닉 집단 추정에서 사회 구조 파악까지 | ARD가 단순 규모 추정을 넘어 네트워크 구조 연구 도구로 진화 |
| [[pages/papers/sna/2026_arevalillo_network_scaleup_methods\|Arevalillo 외 (2026)]] | ARD로 스페인 총선 투표 의향 간접 추정 — 다양한 NSUM 기법 비교 | 주요 여론조사 기관과 유사한 정확도; 민감 정보 노출 위험 낮은 대안 |
| [[pages/papers/sna/2026_feld_estimating_unknown_populations\|Feld & McGail (2026)]] | NSUM 기준 집단과 포획-재포획 결합 하이브리드 추정 — 페이스북 데이터로 신입생 규모 추정 검증 | 중복 보고로 외생 정보 없이 추정치 보정 가능; 가시성 차이 있는 집단에 적합 |
| [[pages/papers/sna/2025_vlker_whos_your_extended\|Völker 외 (2025)]] | 네덜란드 2021년 NSUM으로 성인 확장 지인 네트워크 규모(중앙값 446명)·동질성 분석 | 취업 상태·가구원 수·나이·소득이 더 큰 네트워크와 연관; 성별·교육 분리 확인 |
| [[pages/papers/sna/2026_almquist_homelessness_personal_network\|Almquist 외 (2026)]] | RDS 표집으로 킹 카운티 노숙 경험자 3,000명+ ARD 수집 — 퍼스널 네트워크 3년 종단 분석 | 친밀 우정 네트워크 감소(4.9→4.19), 가족 동거 증가 — 고립 심화 신호 |

## NetMiner 지원 현황

❌ 미지원 — NetMiner는 NSUM/ARD 기반 은닉 집단 규모 추정 기능을 제공하지 않는다.

**대안 도구**:
- R `NSUM` 패키지
- R `RDS` 패키지 (Respondent-Driven Sampling)
- Stata `networkscaleup` 모듈
- Python 커스텀 구현

**NetMiner 연관 활용**: NSUM으로 수집된 ARD 데이터를 에고 네트워크로 변환 후 NetMiner에서 퍼스널 네트워크 분석·시각화는 가능.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/bayesian_network_model|Bayesian/잠재공간 모델]] (ARD에서 잠재 공간 추론)
- [[pages/concepts/personal_network|퍼스널 네트워크]] (NSUM이 측정하는 확장 네트워크)
- [[pages/tools/other_tools|Other Tools (ERGM·SAOM 지원 도구)]]
