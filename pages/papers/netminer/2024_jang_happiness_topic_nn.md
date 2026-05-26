---
title: "A Study of Factors Influencing Happiness in Korea: Topic Modelling and Neural Network Analysis"
authors: [Jang Ji-Hyun, Nemoto Masatsugu]
year: 2024
venue: Data & Metadata (doi: 10.56294/dm2024238)
tags: [topic-modeling, neural-network, machine-learning, happiness, mixed-methods, netminer]
source: raw/A Study of Factors Influencing Happiness in Korea Topic Modelling and Neural Network Analysis.pdf
---

# 한국인 행복 영향 요인 연구: 토픽모델링 + 신경망 분석

## 연구 질문
한국인의 행복 수준에 영향을 미치는 주요 요인은 무엇이며, 그 중 가장 중요한 요인은?

## 데이터
- 소스 1: Springer 학술지의 행복 관련 논문 1,000편 → 영향 요인 도출
- 소스 2: 서울대 행정대학원 지역복지연구센터 2020년 설문, 16,655명 응답

## 방법론
| 분석 | 도구 |
|------|------|
| [[topic_modeling\|토픽모델링]] | NetMiner 4.5 |
| 머신러닝 분류 | NetMiner 4.5 |
| [[neural_network_analysis\|신경망 분석]] | SPSS MODELER 18 |

→ [[mixed_methods\|복합 방법론]] 패턴: 텍스트 마이닝으로 변수 도출 → 설문 데이터에 신경망 적용

## 주요 결과
- 행복 영향 요인: 가족생활, 사회적 지위, 소득, 건강, 불평등 인식
- 신경망 분석 결과: **가족생활 만족도**가 가장 강한 영향 요인
- 정책 함의: 가족친화 근무환경, 육아 지원, 가정폭력 예방 프로그램

## NetMiner 연관성
- NetMiner 4.5 사용 (토픽모델링 + 머신러닝 동시 수행)
- 논문에 NetMiner가 공식 분석 도구로 명시됨 → 인용 사례로 활용 가능
- [[netminer\|NetMiner]]

## 한계 / 메모
- 논문 데이터(Springer)와 설문 데이터의 맥락 차이 → 변수 타당성 논의 필요
- 신경망 블랙박스 문제는 언급되지 않음
