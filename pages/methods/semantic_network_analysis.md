---
title: "의미연결망 분석 (Semantic Network Analysis)"
tags: [semantic-network, keyword-network, co-occurrence, text-network]
netminer_support: "✅ 지원"
---

# 의미연결망 분석 (Semantic Network Analysis)

텍스트에서 단어(키워드) 간 공출현(co-occurrence) 관계를 네트워크로 구성하고 분석하는 방법. [[pages/methods/topic_modeling|토픽모델링]]과 함께 텍스트+네트워크 복합 연구의 두 축을 이룬다. SNA 학술지 2020–2026에서 4편이 활용했으며 (15위), 빈도는 낮으나 고유한 적용 맥락을 가진다.

## 핵심 아이디어

- **노드**: 단어·키워드
- **엣지**: 동일 문서(또는 문장, 윈도우) 내 공출현 → 의미적 연관성 프록시
- **중심성 높은 단어** = 해당 담론의 핵심 개념
- **커뮤니티** = 의미적으로 연관된 단어 군집

## 핵심 개념

| 요소 | 설명 |
|------|------|
| 공출현 윈도우 | 문장, 단락, 문서 단위로 달라지며 결과에 큰 영향 |
| 가중치 | 공출현 빈도 또는 PMI(상호정보량) 등 정규화 방식 |
| 시계열 분석 | 동일 네트워크의 시간 슬라이스 비교 → 담론 변화 추적 |
| 커뮤니티 탐지 | 의미 군집 식별 (Suitner 2022) |

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/2022_suitner_the_rise_climateaction\|Suitner 외 (2022)]] | 트위터 기후변화 담론 2017–2019 시계열 의미 네트워크 + 커뮤니티 탐지 알고리즘 | FridaysForFuture 이후 집합행동 수사 강화, 인그룹 미래 투영 표현 증가 |
| [[pages/papers/2026_almquist_search_common\|Almquist 외 (2026)]] | 키워드 보조 토픽 모델로 가치 네트워크 추출 → 국가별 협상 구조 분석 | "공정성·권력"에서 "환경·성취" 중심 가치로 전환 |
| [[pages/papers/2023_koskinen_analysing_networks_networks\|Koskinen 외 (2023)]] | 개별 의미 구조를 사회적 유대로 연결하는 다층 네트워크 분석 프레임 | 라인 그래프 변환으로 의미 네트워크의 네트워크 분석 가능 |

## [[pages/methods/topic_modeling|토픽모델링]]과의 차이

| | 의미연결망 분석 | 토픽모델링 (LDA) |
|--|--|--|
| 단위 | 단어 쌍 (엣지) | 단어 분포 (토픽) |
| 결과 | 네트워크 구조 | 잠재 주제 군집 |
| 강점 | 개념 간 관계 시각화 | 숨겨진 주제 발견 |
| 약점 | 토픽 경계 불명확 | 관계 구조 미포착 |

→ **둘을 함께 쓰면 상호 보완**: 복합 방법론 패턴의 핵심

## NetMiner 지원 현황

✅ 지원 — 한국어 포함 의미연결망 분석 지원. 텍스트 수집부터 공출현 행렬 생성, 네트워크 시각화까지 통합 워크플로우 제공. 시계열 슬라이스 비교 기능으로 담론 변화 분석 가능.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/community_detection|커뮤니티 탐지]] (의미 커뮤니티 식별)
- [[pages/methods/centrality|중심성 분석]] (핵심 개념어 식별)
