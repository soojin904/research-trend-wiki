---
title: "A New Semisupervised Technique for Polarity Analysis using Masked Language Models"
authors: ['Kohei Watanabe']
year: 2026
venue: "ArXiv.org"
tags: ['Computational and Text Analysis Methods', 'Sentiment Analysis and Opinion Mining', 'Human Mobility and Location-Based Analysis']
source: raw/applied/applied_2026_A_New_Semisupervised_Tech_nodoi.md
---

# A New Semisupervised Technique for Polarity Analysis using Masked Language Models
**제목(한글)**: 마스크 언어 모델을 활용한 극성(polarity) 분석을 위한 새로운 반지도학습 기법

## 한국어 요약

**연구질문**: word2vec을 마스크 언어 모델로 활용한 잠재 의미 스케일링(Latent Semantic Scaling, LSS) 기법이 기존 공간 기반 극성 모델보다 더 정확하고 해석 가능한 극성 점수를 산출할 수 있는가?

**방법론**:
- word2vec 기반 마스크 언어 모델을 도입한 LSS의 새로운 버전 개발
- 단어와 문서에 시드 단어 출현 예측 확률로 극성 점수를 부여하는 확률적 극성 모델 설계
- 코로나19 팬데믹 기간 China Daily의 국가별 건강 이슈 보도를 분석 대상으로 확률 모델과 공간 모델 비교 검증

**주요 결과**:
- 확률적 극성 점수가 공간 기반 모델보다 더 정확하고 일관되며 해석 가능한 결과를 산출함을 실증
- 더 발전된 마스크 언어 모델 적용 시 반지도학습 기반 텍스트 분석 성능이 추가 향상될 것으로 기대

**저자**: Kohei Watanabe
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-04-29
**DOI**: 

## 초록 (원문)

I developed a new version of Latent Semantic Scaling (LSS) employing word2vec as a masked language model. Unlike original spatial models, it assigns polarity scores to words and documents as predicted probabilities of seed words to occur in given contexts. These probabilistic polarity scores are more accurate, interpretable and consistent than those spatial polarity models can produce in text analysis. I demonstrate these advantages by applying both probabilistic and spatial models to China Daily's coverage of China and other countries during the coronavirus disease (COVID) pandemic in terms of achievement in health issues. The result suggests that more advanced masked language models would further improve the semisupervised machine learning technique.

## 키워드

Polarity (international relations), Probabilistic logic, Semantics (computer science), Language model, Word2vec, Statistical model, Distributional semantics, Word (group theory)

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

