---
title: "증상-유전자 네트워크 분석을 활용한 파킨슨병의 한의학적 적용 가능성 탐색"
authors: [YeRim Kang, GeunBi Lee, Ji Won Ha, La Yoon Choi, Gi-Sang Bae, Mi Hye Kim, Dae Yong Kim]
year: 2026
venue: 대한한의학회지
tags: [network-analysis, centrality, two-mode-network, bioinformatics, parkinsons-disease, netminer]
source: raw/netminer/kci_2026_증상유전자_네트워크_분석을_활용한_파킨슨병의_ART003307116.md
---

# 증상-유전자 네트워크 분석을 활용한 파킨슨병의 한의학적 적용 가능성 탐색

## 연구 질문
파킨슨병의 다양한 증상과 관련된 핵심 유전자를 네트워크 중심성 분석으로 식별하고, 한의학 본초와의 연관성을 통해 과학적 근거를 탐색할 수 있는가?

## 방법론
- 데이터: GeneCards에서 수집한 파킨슨병 관련 증상-유전자 이원(two-mode) 네트워크
- 분석 기법: 연결중심성·매개중심성·근접중심성·고유벡터중심성 계산 (NetMiner), 핵심 유전자와 한의학 임상진료지침 본초 매칭, DAVID를 통한 농축 분석(enrichment analysis)

## 주요 결과
- REM 수면행동장애가 모든 네트워크 지표에서 가장 중심적인 증상으로 확인
- 핵심 유전자 13개(SNCA, MAPT, APOE, IL6, APP 등) 식별
- 41개 본초 중 복숭아씨(Prunus persica)와 지렁이(Pheretima aspergillum)가 핵심 유전자와 강한 연관성을 보여 시냅스 조절·신경염증·아밀로이드 대사에 다중표적 효과 가능성 시사

## NetMiner 연관성
증상-유전자 이원 네트워크를 NetMiner로 구축하고 4종 중심성 지표(연결·매개·근접·고유벡터)를 산출해 핵심 유전자를 식별하는 시스템생물학적 접근에 활용했다.

## 위키 연관
- [[pages/tools/netminer|NetMiner]]
- [[pages/methods/centrality|Centrality]]
- [[pages/concepts/social_network_analysis|SNA]]
