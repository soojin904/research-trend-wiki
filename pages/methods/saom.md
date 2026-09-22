---
title: "SAOM / RSiena (확률적 행위자 지향 모형)"
tags: [saom, rsiena, stochastic-actor-oriented, longitudinal, coevolution]
netminer_support: "❌ 미지원"
updated: 2026-09-22
---

# 확률적 행위자 지향 모형 (Stochastic Actor-Oriented Model, SAOM / RSiena)

행위자들이 네트워크 유대를 능동적으로 선택·유지·해소하는 과정을 **연속 시간 마르코프 과정**으로 모델링하는 종단 통계 방법론.
**SNA 전문 학술지 전수 318편 중 29편(3위)** 이 활용한다 ([[pages/insights/sna_method_frequency|방법론 빈도 분석]], 2026-09-22 기준).
[[pages/methods/ergm|ERGM]](40편)과 함께 통계적 네트워크 모형의 양대 축이며, [[pages/methods/relational_event_model|REM]](17편)까지 더하면 86편 규모의 "동적·생성적 모형" 군을 이룬다.

## 핵심 개념

행위자가 소규모 변화(유대 추가·삭제·유지)를 목적함수(objective function)를 최대화하도록 순차적으로 선택한다고 가정한다.

- **목적함수**: 네트워크 위치의 효용을 통계적으로 추정
- **연속 시간 과정**: 관찰 파동 사이 어디서든 변화 발생 가능
- **공진화(coevolution) 모형**: 네트워크와 행동(behavior)이 동시에 변하는 구조
- **관찰 단위**: **패널 스냅샷(2파 이상)** — 이벤트 로그를 쓰는 REM과 결정적으로 다르다
- **RSiena**: 사실상 유일한 표준 구현체

### 세 패러다임 비교

| | ERGM | SAOM | REM |
|--|------|------|-----|
| 데이터 | 단일 시점 네트워크 | 패널 스냅샷 (t1, t2, t3…) | 타임스탬프 이벤트 스트림 |
| 시간 처리 | 정적 (TERGM은 이산 종단) | 연속 시간, 관찰은 이산 | 연속 시간, 관찰도 연속 |
| 행위자 역할 | 수동적 | 능동적 (유대 선택) | 사건 발생 위험률 |
| 공진화 | 제한적 | 네트워크+행동 동시 | 이벤트 속성 확장 |
| 주 소프트웨어 | R statnet | R RSiena | R remstats/goldfish |

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2025_kruidhof_the_coevolution_informal\|Kruidhof 외 (2025)]] | 3파 종단에서 비공식 지위–가십 삼자 관계 공진화 | 낮은 지위 직원이 가십 수신 多 → 지위 향상; 전송은 무영향 |
| [[pages/papers/sna/2023_espinosara_coevolution_sociocognitive\|Espinosa-Rada 외 (2023)]] | 1모드·2모드 SAOM으로 인용·협력·기관 네트워크 공진화 | 사회적 관계가 인지 기반보다 인용 공진화를 더 잘 설명 |
| [[pages/papers/sna/2022_hachen_generators_diffusers_examining\|Hachen 외 (2022)]] | 이원 네트워크 SAOM으로 초점(focus) 유형별 역할 비교 | 동아리=유대 생성자, 음악 장르=취향 확산자 |
| [[pages/papers/sna/2024_ceoldo_stochastic_actor_oriented_mode\|Ceoldo 외 (2024)]] | SAOM에 **랜덤 효과** 도입 — 행위자 간 이질성 포착 | 고정 효과 모형 대비 유연성 향상 |
| [[pages/papers/sna/2025_snijders_double_agency_and_coevolution\|Snijders (2025)]] | 이중 행위주체성(double agency) 하의 공진화 모형 확장 | SAOM 이론틀 자체의 확장 논의 |
| [[pages/papers/sna/2025_shappell_accounting_for_edge_uncertaint\|Shappell 외 (2025)]] | 엣지 불확실성을 반영한 SAOM 추정 | 측정 오차가 모수 추정에 미치는 영향 보정 |

## 방법론 논쟁: SAOM vs TERGM 비교의 신뢰성 ⚠️

인용 시 반드시 함께 다뤄야 할 논쟁이다.

1. **Leifeld & Cranmer (2019)** — TERGM과 SAOM의 경험적 예측력을 비교해 TERGM 우위를 주장.
2. **[[pages/papers/sna/2022_block_circular_specifications_and_pr\|Block 외 (2022)]]** — 해당 비교가 **순환적 모형 설정(circular specification)** 이며 **미래 시점 정보를 이용해 "예측"** 한 오류를 포함한다고 반박. 즉 원 비교 결과는 방법론적으로 성립하지 않는다.
3. **[[pages/papers/sna/2022_leifeld_the_stochastic_actororiented_m\|Leifeld & Cranmer (2022)]]** — SAOM은 방법론인 동시에 이론이며 내재 이론 검증이 필요하다는 재반박 성격의 논의. [[pages/papers/sna/2022_leifeld_theoretical_and_empirical\|Corrigendum(2022)]]도 별도 게재됨.

> **위키 인용 규칙**: 다른 페이지나 마케팅 콘텐츠에서 "TERGM이 SAOM보다 우수/열등"이라는 단정은 쓰지 않는다. 비교 자체가 논쟁 중이라고 서술할 것.

## NetMiner 지원 현황

**❌ 미지원** — NetMiner에 SAOM/RSiena 계열 기능은 없다([[pages/tools/netminer|기능 목록]] 확인: Network > Models에 ERGM만 존재).

고급 종단 연구자가 R로 이탈하는 주요 원인이며, 학술 수요 29편(3위) 규모에 대응 수단이 전혀 없는 상태다.

**대안 도구**: R `RSiena`(표준), `sienaRI`(역할 지표), `RSienaTest`

### 제품 기획 시사점 (학술 수요 ≠ 지원 여부 분리)

- **학술 수요**: 29편, 3위. 게다가 SAOM 논문 상당수가 **공진화(네트워크+행동 동시 변화)** 라는, 다른 어떤 방법으로도 대체 불가능한 질문을 다룬다.
- **NetMiner 지원**: 전무. 부분 대응도 불가능(패널 네트워크 자료구조 자체는 Merge Layers로 다룰 수 있으나 추정 엔진이 없음).
- **현실적 단기 대응**: 자체 구현보다 **"NetMiner에서 패널 네트워크 정리·시각화 → RSiena로 추정"** 워크플로우 가이드가 비용 대비 효과가 높다. 장기 개발 검토 대상.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석 (318편 전수)]]
- [[pages/methods/ergm|ERGM]] (경쟁·보완 관계)
- [[pages/methods/relational_event_model|관계 사건 모형 (REM/RHEM/DyNAM)]]
- [[pages/methods/longitudinal_network|종단/동적 네트워크]]
- [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]]
- [[pages/tools/netminer|NetMiner]]
- [[pages/tools/other_tools|Other Tools (ERGM·SAOM 지원 도구)]]
