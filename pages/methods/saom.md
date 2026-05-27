---
title: "SAOM / RSiena (확률적 행위자 지향 모형)"
tags: [saom, rsiena, stochastic-actor-oriented, longitudinal, coevolution]
netminer_support: "❌ 미지원"
---

# 확률적 행위자 지향 모형 (Stochastic Actor-Oriented Model, SAOM / RSiena)

행위자들이 네트워크 유대를 능동적으로 선택·유지·해소하는 과정을 연속 시간 마르코프 과정으로 모델링하는 종단 통계 방법론. SNA 학술지 2020–2026에서 18편이 활용하여 7위를 기록했다. ERGM(26편)과 함께 SNA 통계 모형의 양대 축을 이룬다.

## 핵심 개념

SAOM의 핵심 아이디어는 행위자가 소규모 변화(유대 추가·삭제·유지)를 목적함수(objective function)를 최대화하도록 순차적으로 선택한다는 것이다:

- **목적함수**: 네트워크 위치의 효용을 통계적으로 추정
- **연속 시간 과정**: 관찰 사이 어디서든 변화가 일어날 수 있음 (ERGM과 차별점)
- **공진화 모형**: 네트워크와 행동(behavior)이 동시에 변하는 구조 가능
- **RSiena**: SAOM의 주요 R 구현체

### ERGM vs. SAOM 주요 차이

| | ERGM | SAOM |
|--|------|------|
| 시간 처리 | 단일 시점 (STERGM은 종단) | 연속 시간 종단 |
| 행위자 역할 | 수동적 (네트워크 확률 모형) | 능동적 (유대 선택 과정) |
| 이론적 성격 | 통계 모형 | 이론+통계 모형 (Leifeld & Cranmer 논쟁) |
| 공진화 | 제한적 | 네트워크+행동 동시 모형화 |
| 주 소프트웨어 | R statnet | R RSiena |

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2025_kruidhof_the_coevolution_informal\|Kruidhof 외 (2025)]] | 3파 종단 연구에서 SAOM으로 비공식 지위와 가십 삼자 관계 공진화 분석 | 낮은 지위 직원이 가십 수신 多 → 지위 향상; 가십 전송은 지위에 영향 없음 |
| [[pages/papers/sna/2023_espinosara_coevolution_sociocognitive\|Espinosa-Rada 외 (2023)]] | 1모드·2모드 네트워크용 SAOM으로 천문학자 인용·협력·기관 네트워크 공진화 분석 | 사회적 관계(협력·기관 근접성)가 인지 기반보다 인용 공진화를 더 잘 설명 |
| [[pages/papers/sna/2022_hachen_generators_diffusers_examining\|Hachen 외 (2022)]] | 이원 네트워크용 SAOM으로 동아리·음악 장르·수강 과목 등 초점 유형별 역할 비교 | 동아리=유대 생성자, 음악 장르=취향 확산자, 수강 과목=혼합 |
| [[pages/papers/sna/2022_leifeld_the_stochastic_actororiented_m\|Leifeld & Cranmer (2022)]] | SAOM의 이론적 성격 재검토 — TERGM과 모형 비교 방법론 논쟁 | SAOM은 방법론인 동시에 이론이며, 내재 이론 검증이 시급한 과제 |

### 확장 모형: 랜덤 효과 SAOM

[[pages/papers/sna/2024_ceoldo_stochastic_actor_oriented_mode\|Ceoldo 외 (2024)]]는 SAOM에 랜덤 효과를 도입하여 행위자 간 이질성을 포착하는 방법을 제안. 기존 고정 효과 모형 대비 유연성 향상.

## NetMiner 지원 현황

❌ 미지원 — NetMiner는 SAOM/RSiena를 지원하지 않는다. 이는 고급 종단 연구자들이 R로 이탈하는 주요 원인으로, 사이람의 제품 기획 시 고려해야 할 핵심 공백이다.

**대안 도구**:
- R `RSiena` 패키지 (주요 구현체, 무료)
- R `sienaRI` 패키지 (역할 지표)
- SIENA 독립 실행형 소프트웨어 (구버전)

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/ergm|ERGM]] (경쟁·보완 관계; STERGM과 SAOM 비교)
- [[pages/methods/longitudinal_network|종단/동적 네트워크]] (SAOM이 포함되는 상위 범주)
- [[pages/tools/other_tools|Other Tools (ERGM·SAOM 지원 도구)]]
