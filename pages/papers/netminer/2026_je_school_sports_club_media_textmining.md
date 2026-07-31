---
title: "학교스포츠클럽에 대한 언론보도 변화 분석 - 텍스트마이닝을 활용한 빅데이터 분석을 중심으로 -"
authors: [Minsu Je, Kim In Hyung]
year: 2026
venue: 한국스포츠사회학회지
tags: [text-mining, tf-idf, semantic-network-analysis, centrality, sports, netminer]
source: raw/netminer/kci_2026_학교스포츠클럽에_대한_언론보도_변화_분석_ART003326639.md
---

# 학교스포츠클럽에 대한 언론보도 변화 분석 - 텍스트마이닝을 활용한 빅데이터 분석을 중심으로 -

## 연구 질문
2007~2023년 학교스포츠클럽 관련 언론 보도의 핵심 주제어와 네트워크 구조는 시기별로 어떻게 변화했는가?

## 방법론
- 데이터: 빅카인즈 수집 언론 기사 7,922건(2007~2023)에서 추출한 키워드 27,286개, 3개 시기(1기 2007-2011, 2기 2012-2018, 3기 2019-2023) 구분
- 도구: NetMiner 4.5
- 분석: TF-IDF 분석, 의미연결망(semantic network) 분석, 네트워크 시각화

## 주요 결과
- TF-IDF 핵심어: 1기(체육, 참여, 지원), 2기(교육, 지역, 종목), 3기(건강, 체력, 코로나)
- 연결중심성 상위: 1기(스포츠, 체육, 학교, 학생, 교육), 2기(스포츠, 학교, 학생, 활동, 대회, 인성, 폭력), 3기(스포츠, 체육, 학교, 학생, 건강, 코로나, 온라인, 소통)
- 정책 환경·사회적 이슈 변화에 따라 언론 보도의 핵심 키워드와 연결 구조가 시기별로 달라짐 확인

## NetMiner 연관성
NetMiner 4.5로 TF-IDF 분석, 의미연결망 분석, 네트워크 시각화를 수행해 시기별 언론보도 담론 구조 변화를 분석했다.

## 위키 연관
- [[pages/tools/netminer|NetMiner]]
- [[pages/methods/semantic_network_analysis|Semantic Network Analysis]]
- [[pages/methods/centrality|Centrality]]
