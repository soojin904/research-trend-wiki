---
title: "퍼스널 네트워크 (Personal Network / Egocentric Network)"
tags: [personal-network, egocentric-network, alter, ego]
---

# 퍼스널 네트워크 (Personal / Egocentric Network)

특정 개인(ego)을 중심으로 그 사람의 직접 연결(alter)과 그 관계들로 구성된 네트워크. 전체 네트워크(complete network) 데이터를 수집하기 어려운 상황에서 활용된다.

## 에고중심 vs. 전체 네트워크

| 구분 | 에고중심 | 전체 네트워크 |
|------|---------|-------------|
| 데이터 단위 | 개인별 설문 | 집단 전체 매핑 |
| 규모 제약 | 없음 (개인 단위 표집 가능) | 경계 정의 필요 |
| 주요 질문 | 개인의 사회적 자원, 네트워크 구성 | 구조적 패턴, 중심성, 커뮤니티 |
| 적합 집단 | 노숙인·환자 등 접근 어려운 집단 | 조직·커뮤니티 |

## 주요 측정 변수

- **네트워크 규모**: 알터 수
- **밀도(density)**: 알터 간 연결 비율
- **구성(composition)**: 알터의 인구통계·태도 특성
- **동질성(homophily)**: 에고와 알터의 유사성

## 수집 방법

> 수집·측정 설계의 상세 방법론(이름 생성기 설계, 수집 소프트웨어, 회상 편향, 구조 유형 자동 분류)은 별도 문서로 분리했다 → **[[pages/concepts/egocentric_network_design|에고중심 네트워크 연구설계]]** (318편 중 46편, 단일 최대 클러스터)

- 이름 생성(name generator) + 이름 해석(name interpreter) 설문
- Respondent-Driven Sampling (RDS): 은닉 집단 표집
- Aggregate Relational Data (ARD): 직접 네트워크 매핑 없이 규모 추정

## 관련 연구 (Social Networks 2026)

- [[pages/papers/sna/2026_almquist_homelessness_personal_network|Almquist 외]] — 노숙 경험자 퍼스널 네트워크 (3,000명+, 종단)
- [[pages/papers/sna/2026_schafer_personal_network_loneliness|Schafer 외]] — 동반 관계와 외로움: 청년·노년 비교
- [[pages/papers/sna/2026_gebhard_intervention_dementia|Gebhard & Ellinger]] — 치매 환자 개입과 네트워크 변화
- [[pages/papers/sna/2026_zhang_egocentric_csa|Zhang & Wang]] — 에고중심 네트워크와 CSA 소비자 반응

## NetMiner 연관성

- NetMiner는 에고중심 네트워크 분석 기능 지원 (`Pre-process > Network Transform > Ego Network Extract`)
- 알터 구성 분석, 밀도·다양성 지표 계산, 시각화
- 단, **다수 에고넷 일괄 처리·구조 유형 자동 분류는 미지원** → [[pages/concepts/egocentric_network_design|에고중심 네트워크 연구설계]] 참조

## 위키 연관

- [[pages/concepts/egocentric_network_design|에고중심 네트워크 연구설계]]
- [[pages/methods/network_scaleup|Network Scale-Up / ARD]]
- [[pages/insights/sna_method_frequency|SNA 방법론 빈도 분석 (318편 전수)]]
- [[pages/tools/netminer|NetMiner]]
