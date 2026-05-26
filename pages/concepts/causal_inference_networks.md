---
title: "인과 추론과 네트워크 (Causal Inference in Networks)"
tags: [causal-inference, spillover, rct, network-position]
---

# 인과 추론과 네트워크

소셜 네트워크 맥락에서 인과 추론은 행위자 간 상호의존성(interdependence)으로 인해 전통적 방법론의 가정이 깨지는 문제가 발생한다.

## 핵심 문제

| 문제 | 설명 |
|------|------|
| Spillover / 오염(contamination) | 처치군→통제군으로 효과가 전파 → 처치 효과 편향 |
| 네트워크 위치 차이 | RCT 참여자와 비참여자의 네트워크 구조가 다름 → 외적 타당성 위협 |
| 동료 영향(peer influence)과 선택 | 유사한 행위자끼리 연결(homophily)과 실제 영향을 분리하기 어려움 |
| SUTVA 위반 | 안정적 단위 처치값 가정(Stable Unit Treatment Value Assumption) — 네트워크에서 성립 않음 |

## 주요 방법론

- **직접·간접 효과 분해**: spillover를 간접 효과로 명시적 모델링
- **SAOM (Stochastic Actor-Oriented Model)**: 종단 네트워크 변화와 행동 공동 모델링
- **Counterfactual 프레임워크**: 오염 없는 반사실적 세계와 비교
- **Computational knockout experiments**: 특정 네트워크 메커니즘 제거 시뮬레이션

## 관련 연구 (Social Networks 2026)

- [[pages/papers/2026_omalley_spillover_rct|O'Malley 외]] — stepped-wedge RCT에서 의사 네트워크 spillover 추정
- [[pages/papers/2026_mcmillan_network_rct_causal|McMillan 외]] — RCT 참여자 네트워크 위치 차이와 인과 추론 위협
- [[pages/papers/2026_an_peer_influence_multilayer|An 외]] — 다층 네트워크에서 동료 영향 추정 (내생성 문제)

## NetMiner 연관성

- 네트워크 기반 인과 추론은 고급 연구 맥락 — **방법론 세미나 소재**로 적합
- 직접 기능 지원보다는 네트워크 구조 시각화·분석 후 외부 통계 패키지 연계 논의 가능
