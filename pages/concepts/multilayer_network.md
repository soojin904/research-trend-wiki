---
title: "다층·멀티플렉스 네트워크 (Multilayer / Multiplex Network)"
tags: [multilayer-network, multiplex, interlayer, network-structure]
---

# 다층·멀티플렉스 네트워크

동일한 노드 집합에 **복수의 관계 유형(레이어)**이 존재하는 네트워크. 현실의 복잡한 사회적 관계를 단일 레이어 네트워크보다 충실하게 표현한다.

## 개념 구분

| 유형 | 정의 |
|------|------|
| Multiplex network | 같은 노드 집합, 다른 관계 유형 (예: 친구 + 동료 + 가족) |
| Multilevel network | 다른 수준의 노드 포함 (예: 개인-조직 혼합) |
| Temporal network | 시간에 따른 레이어 변화 |

## 주요 분석 이슈

- **레이어 간 상관(interlayer correlation)**: 한 레이어의 연결이 다른 레이어 연결 예측
- **레이어 간 영향(interlayer influence)**: 한 레이어에서의 행동이 다른 레이어로 파급
- **집계 문제**: 레이어를 단순 집계하면 정보 손실

## 연구 동향 (Social Networks 2026)

- [[pages/papers/2026_an_peer_influence_multilayer|An 외]] — 다층 네트워크에서 동료 영향 추정 (내생성 처리)
- [[pages/papers/2026_fluer_multiplex_survey|Fluer 외]] — 설문 데이터 → 멀티플렉스 모델 (레이어 간 상관 포함)
- [[pages/papers/2026_haapanen_coalition_sna_design|Haapanen 외]] — 연합의 다층 구조(개인간 + 조직간)와 SNA 설계

## NetMiner 연관성

- 다층 네트워크 분석은 현재 학계 핵심 방향 → **기능 개발 우선순위 참고**
- 복수 관계 유형 동시 처리, 레이어 간 비교 기능 수요 높음
