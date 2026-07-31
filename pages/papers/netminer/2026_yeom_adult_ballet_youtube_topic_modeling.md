---
title: "LDA토픽모델링을 적용한 성인발레 콘텐츠 동향분석: 2018~2025 유튜브 데이터를 중심으로"
authors: [염지현, Lee Hae Jun]
year: 2026
venue: 한국무용학회지
tags: [topic-modeling, lda, youtube, content-analysis, dance, netminer]
source: raw/netminer/kci_2026_LDA토픽모델링을_적용한_성인발레_콘텐츠_동향_ART003303420.md
---

# LDA 토픽모델링을 적용한 성인발레 콘텐츠 동향분석 (2018~2025 유튜브)

## 연구 질문
2018~2025년 유튜브에서 '성인발레' 담론의 구조와 시계열 변화는 어떠한가?

## 방법론
- 데이터: 연도별 유튜브 상위 100개 동영상, 8년(2018~2025)
- 분석 기법: LDA 토픽모델링, NetMiner v4 기반 전처리, u_mass 의미론적 일관성, Spearman 상관분석

## 주요 결과
- 4개 토픽 도출: ① 학습·성과, ② 발레복·장비·소비문화, ③ 신체효과·건강, ④ 일상화·콘텐츠 확산
- Topic 2(소비·장비)만 시간에 따라 유의한 정(+)의 상관 (ρ=0.347, p=0.042)
- 성인발레 담론이 기능적 학습에서 소비·추천 정보 중심으로 재편되는 경향
- 정보 신뢰성 확보를 위한 표준화와 협찬 표시 투명성 필요성 제기

## NetMiner 연관성
NetMiner v4로 유튜브 텍스트 데이터를 전처리한 후 LDA 토픽모델링을 적용하고, 토픽별 시계열 상관관계를 검증했다.

## 위키 연관
- [[pages/tools/netminer|NetMiner]]
- [[pages/methods/topic_modeling|Topic Modeling]]
- [[pages/methods/text_classification|Text Classification]]
