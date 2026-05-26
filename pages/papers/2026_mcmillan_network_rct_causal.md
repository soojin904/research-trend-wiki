---
title: "Network threats to causal inference: Variations in network position by participation in randomized controlled trials"
authors: ["Cassie McMillan", "Mark C. Pachucki", "Jiaao Yu", "A. James O'Malley", "Anne N. Thorndike", "Douglas E. Levy"]
year: 2026
venue: "Social Networks"
volume: 86
tags: [causal-inference, rct, network-position, homophily, saom]
source: raw/2026_openalex_Network_threats_to_causal_inference_Variations_j_socnet_2026_03_004.md
---

# Network threats to causal inference: Variations in network position by participation in RCTs

**연구질문**: RCT 참여자와 비참여자의 네트워크 위치 차이가 인과 추론의 타당성을 어떻게 저해하는가?

**데이터**: 병원 직원 구내식당 구매 데이터 → 공동구매 네트워크 (2016–2019), 건강식 개입 RCT

## 방법론

| 단계 | 내용 |
|------|------|
| 네트워크 구성 | 구내식당 공동구매 기록 → 종단 네트워크 |
| 모델 | Stochastic Actor-Oriented Models (SAOMs) |
| 실험 | Computational knockout experiments (특정 네트워크 현상 제거 시뮬레이션) |

## 주요 결과

- RCT 참여자가 비참여자보다 동료와 더 많은 공동구매 연결 보유 (더 높은 연결도)
- 참여자-비참여자 간 **네트워크 위치 차이**가 개입 효과 추정치를 하향 편향
- 네트워크 동질성(homophily by RCT enrollment) 확인

## NetMiner 연관성

- SAOM 분석은 NetMiner의 **종단 네트워크 분석** 기능과 비교 가능
- 네트워크 기반 RCT 설계 컨설팅 소재

## 위키 연관

- [[pages/concepts/causal_inference_networks|인과 추론과 네트워크]]
- [[pages/papers/2026_omalley_spillover_rct|O'Malley 외 2026 — Spillover 추정]]
- [[pages/methods/centrality|Centrality]]

## 메모
