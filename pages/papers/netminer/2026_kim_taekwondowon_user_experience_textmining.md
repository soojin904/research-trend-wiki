---
title: "태권도원 활성화를 위한 사용자 경험 구조 탐색: 텍스트마이닝의 적용"
authors: [Kyo-Sik Kim, Park Kyeong Hoon, YunHo Kim]
year: 2026
venue: 운동재활복지
tags: [text-mining, lda, tf-idf, centrality, tourism, netminer]
source: raw/netminer/kci_2026_태권도원_활성화를_위한_사용자_경험_ART003323168.md
---

# 태권도원 활성화를 위한 사용자 경험 구조 탐색: 텍스트마이닝의 적용

## 연구 질문
태권도원 방문객 온라인 리뷰에 나타난 사용자 경험의 구성 요소와 구조적 특징은 무엇인가?

## 방법론
- 데이터: 태권도원 관련 온라인 리뷰 898건
- 도구: NetMiner 4.0
- 분석: TF, TF-IDF, LDA 토픽모델링(5개 토픽, 일관성지수 0.483), 토픽별 키워드 연결중심성 분석

## 주요 결과
- TF-IDF 최상위 키워드: 최고(114.1), 아이, 공연, 태권도
- 5개 토픽: (1) 전망대·모노레일 등 이동·편의시설, (2) 프로그램·수련 등 글로벌 수련 프로그램, (3) 태권도·공연·아이 등 체험형 관광, (4) 방문객 경험·만족, (5) 시범·경치·산 등 자연환경 결합 시범
- 토픽별 연결중심성 산출로 핵심 주제어 도출, 이용자 관점의 개선방향 제시

## NetMiner 연관성
NetMiner 4.0으로 TF-IDF·LDA 토픽모델링 결과에 대한 토픽별 키워드 연결중심성 네트워크 분석을 수행했다.

## 위키 연관
- [[pages/tools/netminer|NetMiner]]
- [[pages/methods/topic_modeling|Topic Modeling]]
- [[pages/methods/centrality|Centrality]]
