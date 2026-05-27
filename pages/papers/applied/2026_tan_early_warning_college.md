---
title: "Early warning of college students' ideological public opinion based on TF-IDF and RFB neural network"
authors: ['Guixue Tan']
year: 2026
venue: "International Journal of Information and Communication Technology"
tags: ['Ideological and Political Education', 'Sentiment Analysis and Opinion Mining', 'Advanced Computing and Algorithms']
source: raw/applied/applied_2026_Early_warning_of_college__ijict_2026_151873.md
---

# Early warning of college students' ideological public opinion based on TF-IDF and RFB neural network
**제목(한글)**: TF-IDF 및 RBF 신경망에 기반한 대학생 사상 여론의 조기 경보

**저자**: Guixue Tan
**출처**: International Journal of Information and Communication Technology, Vol.27, pp.1-17
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1504/ijict.2026.151873

## 한국어 요약

**연구질문**: 대학생들의 소셜 미디어 상 여론 리스크 및 갈등 조짐을 실시간으로 감지하고 긴급 상황에 대처하기 위해 정확하고 빠른 가벼운 조기 경보 모델을 어떻게 설계할 수 있는가?

**방법론**:
- TF-IDF 기법을 사용해 텍스트 특징 벡터의 희소성을 최적화하는 텍스트 가중치 처리 적용
- 칭화대학교 Weibo-100k 데이터셋 중 32,715건의 아동/청년 댓글을 학습 셋으로 구성하고 ChnSentiCorp 데이터셋으로 도메인 교차 타당성 검증 수행
- 비선형 감정 분류 성능이 우수한 방사 기저 함수(RBF) 신경망 알고리즘 학습

**주요 결과**:
- 테스트셋 평가 결과, 기존 LSTM 모델 대비 F1 점수가 6.2% 향상된 89.7%를 기록하였으며 경보 인지 지연 시간을 12ms 수준으로 대폭 단축하는 성과를 달성
- 학내 사상 갈등 여론 모니터링을 실시간 보조할 수 있는 매우 효율적이고 가벼운 경보 시스템 구축에 성공


## 초록 (원문)

To address the need for real-time early warning of college students' social media opinions, this study proposes a dynamic model integrating term frequency-inverse document frequency (TF-IDF) feature weighting and radial basis function (RBF) neural networks.A subset of 32,715 college-student comments from Tsinghua University's Weibo-100k dataset serves as training samples, with cross-domain validation performed using the ChnSentiCorp benchmark.The approach optimises text feature sparsity via TF-IDF and utilises the nonlinear classification capability of RBF networks for opinion risk categorisation.Experimental results demonstrate an F1-score of 89.7% on the test set -marking a 6.2% improvement over conventional long short-term memory networks -while reducing warning response latency to 12 ms.This confirms high accuracy and real-time performance, providing a lightweight solution for monitoring campus ideological dynamics.

## 키워드

Ideology, Public opinion, Warning system, Artificial neural network, Early warning system

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

