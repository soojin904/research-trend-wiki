---
title: "Digital Health Care Industry Ecosystem: Network Analysis"
authors: [Park Yoonseo, Park Sewon, Lee Munjae]
year: 2022
venue: Journal of Medical Internet Research, 24(8), e37622
tags: [network-analysis, topic-modeling, digital-healthcare, stakeholder, news-data, netminer]
source: raw/Digital Health Care Industry Ecosystem Network Analysis.pdf
---

# 디지털 헬스케어 산업 생태계: 네트워크 분석

## 연구 질문
디지털 헬스케어 산업 생태계의 주요 이해관계자와 핵심 이슈는?

## 데이터
- 뉴스 기사 1,822건 (Big Kings 빅데이터 플랫폼)
- 기간: 2016~2021년 8월 (공공보건센터 모바일 헬스케어 사업 추진 기간)

## 방법론
| 분석 | 도구 |
|------|------|
| [[network_analysis\|네트워크 분석]] (이해관계자 네트워크) | [[netminer\|NetMiner]] |
| [[topic_modeling\|토픽모델링]] | R |
| 중심성 분석 ([[centrality\|centrality]]) | NetMiner |

- 뉴스 데이터 기반 [[social_network_analysis\|SNA]] → 미디어 담론 분석 응용

## 주요 결과
**최고 중심성 이해관계자**: 한국 정부, 보건복지부
**주요 이슈**: 원격진료 도입 검토, 지역 의원 폐업 우려, 정밀의료 통합 플랫폼 구축
**주요 기관·기업**: 서울대병원, 강북삼성병원, 아주대병원, 삼성, Vuno

핵심 이슈 3축: **원격진료 / 데이터 / 헬스케어 비즈니스**

## NetMiner 연관성
- R과 병행 사용 → NetMiner가 네트워크 시각화·중심성 분석 담당
- 의료·공공 정책 분야 응용 사례

## 메모
- 뉴스 데이터 + [[network_analysis\|네트워크 분석]] 조합: 산업 생태계 파악에 효과적
- COVID-19 맥락에서 디지털 헬스케어 수요 급증 배경 서술
