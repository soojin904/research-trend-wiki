---
title: "The Impact of Social Network Characteristics on Health among Community-Dwelling Older Adults in Korea: Application of Social Network Analysis"
authors: [Jeon Byoung-Jin, Park Kang-Hyun]
year: 2022
venue: International Journal of Environmental Research and Public Health, 19(7), 4013 (MDPI)
tags: [sna, centrality, health, aging, ego-network, netminer, regression]
source: raw/The Impact of Social Network Characteristics on Health among Community Dwelling Older Adults in Korea Application of Social Network Analysis.pdf
---

# 지역사회 노인의 소셜 네트워크와 건강: SNA 적용

## 연구 질문
노인의 우정 네트워크 특성(크기, 밀도, 중심성)이 주관적 건강에 미치는 영향?

## 데이터
- 참여자: 146명 (2015년 6~8월)
- 네트워크 유형: 우정 네트워크 (friendship network)

## 방법론
| 분석 | 세부 내용 |
|------|-----------|
| [[social_network_analysis\|SNA]] | 네트워크 크기, 밀도 분석 |
| [[centrality\|중심성 분석]] | out-degree, in-degree, out-closeness, in-closeness |
| 다중선형회귀 | 건강 결과 예측 (NetMiner 4.0) |

## 주요 결과
**건강에 긍정적 영향**:
- out-degree ↑ (외향적 연결 많을수록 건강 좋음)
- in-closeness ↑ (다른 사람과 가까운 위치에 있을수록 건강 좋음)

**건강에 부정적 영향**:
- in-degree ↑ (많은 사람이 선택하는 허브일수록 건강 나쁨 — 스트레스?)
- out-closeness ↑

**인구통계**: 교육 수준 높을수록 건강 좋음, 종교는 부정적 영향

## NetMiner 연관성
- NetMiner 4.0으로 SNA + 다중회귀 동시 수행
- SNA 지표를 독립변수로 활용하는 통계 분석 파이프라인 사례

## 개념 연결
- [[centrality\|중심성 지표]] 해석의 반직관적 결과 (in-degree ↑ → 건강↓) → 흥미로운 논의 포인트
- [[ego_network\|에고 네트워크]] 응용: 개인의 네트워크 위치가 건강 결과에 직접 영향
