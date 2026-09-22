---
title: "관계 사건 모형 (REM / RHEM / DyNAM)"
tags: [relational-event-model, rem, rhem, dynam, event-history, temporal-network, longitudinal]
netminer_support: "❌ 미지원"
created: 2026-09-22
---

# 관계 사건 모형 (Relational Event Model, REM / RHEM / DyNAM)

타임스탬프가 찍힌 **개별 상호작용 사건의 시퀀스**를 직접 모형화하는 네트워크 통계 방법론.
SNA 전문 학술지 전수 318편 중 **17편**이 활용하며, [[pages/methods/ergm|ERGM]](40) · [[pages/methods/saom|SAOM]](29)과 함께 86편 규모의 동적·생성적 모형 군을 구성한다 ([[pages/insights/sna_method_frequency|방법론 빈도 분석]], 2026-09-22 기준).

## 왜 별도 패러다임인가

기존 SNA 방법론이 다루는 데이터는 "누가 누구와 연결되어 있는가"라는 **상태(state)** 이다. REM이 다루는 데이터는 "언제, 누가, 누구에게, 무엇을 했는가"라는 **사건(event)** 이다.

| | 정적/패널 모형 (ERGM·SAOM) | REM |
|--|---------------------------|-----|
| 입력 데이터 | 인접 행렬 (또는 t1·t2·t3 스냅샷) | `(시각, 송신자, 수신자, 유형)` 이벤트 로그 |
| 모형 대상 | 유대의 존재 확률 | **다음 사건의 발생 위험률(hazard rate)** |
| 시간 해상도 | 조사 파동 단위 | 초·분 단위 연속 시간 |
| 전형적 자료 | 설문 네트워크 | 이메일·통화·회의 발언·협업 기록·접촉 일지 |

즉 **NetMiner의 기본 자료구조(노드-링크 행렬)로는 입력조차 표현되지 않는** 별개 패러다임이다.

## 주요 변형

| 변형 | 특징 |
|------|------|
| **REM** (Butts 2008 계열) | 이벤트 위험률을 사건 이력 통계량(상호성·삼자성·최근성)의 함수로 추정 |
| **RHEM** (Relational *Hyper*event Model) | 송·수신자가 **집합**인 사건 (공저 논문, 다자 회의) 모형화 |
| **DyNAM** (Dynamic Network Actor Model) | 사건을 "행위자의 선택"으로 분해 — SAOM 사고방식의 이벤트 버전 |
| **Random-effects DyNAM** | 행위자 이질성을 랜덤 효과로 흡수 |
| **Dyadic latent class REM** | 관계 유형을 잠재 클래스로 구분 |

## 하위 분야 성숙 신호: 2023년 Social Networks REM 특별호

2023년 Social Networks에 REM 특별호가 구성되었고, 본 위키 수집분에도 해당 특별호 논문들이 다수 포함되어 있다. 리뷰·개관 논문([[pages/papers/sna/2023_butts_relational_event_models|Butts 외 2023, "Relational event models in network science"]])이 존재한다는 것은 **실험적 기법이 아니라 정착한 하위 분야**임을 뜻한다.

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2023_butts_relational_event_models\|Butts 외 (2023)]] | REM 특별호 개관 — 네트워크 과학에서의 관계 사건 모형 위치 정리 | 이벤트 데이터 확산에 따른 REM의 제도화 |
| [[pages/papers/sna/2022_lerner_microlevel_network_dynamics\|Lerner 외 (2022)]] | **RHEM**으로 공저 네트워크의 미시 동학과 임팩트 분석 | 공저(하이퍼이벤트) 구조를 이분 네트워크로 환원하지 않고 직접 모형화 |
| [[pages/papers/sna/2023_arena_how_fast\|Arena 외 (2023)]] | 모수적 감쇠(decay) 함수로 과거 상호작용의 **망각 속도** 추정 | 기억 보존 기간이 관계 맥락에 따라 크게 다름 |
| [[pages/papers/sna/2023_kamalabad_what_the_point\|Mulder & Kamalabad (2023)]] | REM에서의 **변화점 탐지(change point detection)** | 네트워크 동학의 구조적 전환 시점을 데이터로 식별 |
| [[pages/papers/sna/2022_fritz_all_that_glitters\|Fritz 외 (2022)]] | 허위·잡음 사건(spurious events)이 섞인 REM 추정 | 관측 오차가 모수를 체계적으로 왜곡 — 보정 절차 제안 |
| [[pages/papers/sna/2023_uzaheta_random_effects_dynamic\|Uzaheta 외 (2023)]] | **DyNAM에 랜덤 효과** 도입 | 행위자 이질성 미반영 시 사건 위험률 과대 추정 |
| [[pages/papers/sna/2024_filippimaz_modeling_nonlinear_effects_wit\|Filippi-Mazzola & Wit (2024)]] | REM의 비선형 효과를 **신경망**으로 근사 | 선형 통계량 가정 완화 (GNN이 아니라 함수 근사용 NN) |
| [[pages/papers/sna/2021_juozaitien_nonparametric_estimation_recip\|Juozaitienė & Wit (2021)]] | 상호성·삼자 효과의 비모수 추정 | 효과의 시간적 형태를 사전 가정 없이 추정 |
| [[pages/papers/sna/2023_karimova_separating_the_wheat_from\|Karimova 외 (2023)]] | 동적 네트워크에서의 **Bayesian 정규화**로 효과 선택 | 다수 후보 통계량 중 유효 효과 자동 선별 |
| [[pages/papers/sna/2026_lakdawala_not_all_bonds_are\|Lakdawala 외 (2026)]] | 이자(dyad) 잠재 클래스 REM | 관계 유형별로 사건 발생 메커니즘이 다름 |
| [[pages/papers/sna/2021_lerner_dynamic_network_analysis\|Lerner 외 (2021)]] | 접촉 일지(contact diary) 데이터의 동적 네트워크 분석 | 일상 접촉 로그에 REM 적용 |

## NetMiner 지원 현황

**❌ 미지원** — NetMiner에 관계 사건 모형(REM/RHEM/DyNAM) 기능은 없다. [[pages/tools/netminer|NetMiner 기능 목록]] 기준으로 `Network > Models`에는 ERGM만 존재하며, 이벤트 로그 자료형을 직접 취급하는 자료구조·메뉴도 없다.

**대안 도구**: R `relevent`(Butts), `remstats`/`remify`/`remstimate`, `goldfish`(DyNAM), `eventnet`(RHEM)

### 제품 기획 시사점 (학술 수요 ≠ 지원 여부 분리)

- **학술 수요**: 17편 + 전용 특별호 + 개관 논문 → 정착한 하위 분야. 게다가 성장 요인이 명확하다(디지털 로그 데이터 증가).
- **NetMiner 지원**: 전무하며, 부분 대응도 어렵다. 기능 하나가 아니라 **자료구조(이벤트 테이블) 지원부터** 필요하기 때문이다.
- **현실적 접근 — 두 단계로 분리**
  1. **단기(저비용)**: 이벤트 로그 → 시간창(time-window) 단위 네트워크 집계·시각화. 추정 모형 없이도 "이벤트 데이터를 네트워크로 보는" 워크플로우는 현재 기능으로 제공 가능하며, 콘텐츠·세미나 소재가 된다.
  2. **장기(고비용)**: REM 추정 엔진 자체. ERGM 변형 확장보다 개발 부담이 크므로 [[pages/methods/ergm|ERGM 변형]]·[[pages/methods/saom|SAOM]] 대응 이후 순위로 두는 것이 합리적이다.
- 단, 마케팅 문구에서 "NetMiner로 동적 네트워크 분석 가능"이라고 쓸 때 **REM 수요를 충족한다는 뜻으로 읽히지 않도록** 범위를 명시할 것.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석 (318편 전수)]]
- [[pages/methods/saom|SAOM / RSiena]] (행위자 지향 사고의 패널 버전)
- [[pages/methods/ergm|ERGM]] (TERGM과의 비교 맥락)
- [[pages/methods/longitudinal_network|종단/동적 네트워크]]
- [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]]
- [[pages/tools/netminer|NetMiner]]
- [[pages/tools/other_tools|Other Tools]]
