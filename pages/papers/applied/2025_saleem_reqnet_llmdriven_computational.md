---
title: "ReqNet: an LLM-driven computational framework for automated requirements extraction from unstructured documents"
authors: ['Summra Saleem', 'Muhammad Nabeel Asim', 'Andreas Dengel']
year: 2025
venue: "Complex & Intelligent Systems"
tags: ['Software Engineering Techniques and Practices', 'Software Engineering Research', 'Topic Modeling']
source: raw/applied/applied_2025_ReqNet_an_LLMdriven_compu_s40747_025_02143_w.md
---

# ReqNet: an LLM-driven computational framework for automated requirements extraction from unstructured documents

**제목(한글)**: ReqNet: 비정형 문서에서 요구사항 자동 추출을 위한 LLM 기반 계산 프레임워크

## 한국어 요약

**연구질문**: 소프트웨어 개발 과정에서 비정형 문서로부터 요구사항을 수동으로 추출하는 데 따르는 비효율성과 오류 가능성을 해결하고, 이를 자동화하며 성능을 향상시키는 효과적인 방법을 제시하는 것은 무엇인가?

**방법론**:
- 7가지 LLM 변형(small, large, Xlarge, XXlarge) 및 2가지 딥러닝(DL) 아키텍처(LSTM, GRU)를 포함하는 ReqNet 프레임워크 개발
- 세 가지 예측 파이프라인 유형 (단독 LLM, LLM + 외부 분류기, 다중 LLM 표현 앙상블 + 외부 분류기) 구축
- 2가지 공개 데이터셋(PURE, Dronology)과 1가지 독립 테스트셋(RFI)을 대상으로 48가지 예측 파이프라인 실험

**주요 결과**:
- LLM과 DL 아키텍처로 구성된 예측 파이프라인이 LLM 단독 파이프라인보다 전반적으로 우수한 성능을 보였다.
- ALBERT, BERT, XLNet 세 가지 LLM과 LSTM 분류기를 앙상블한 모델이 PURE 데이터셋에서 최신 예측기 대비 F1-점수 3% 개선을 달성했다.
- Dronology 데이터셋에서 10% 개선, RFI 독립 테스트셋에서 3% 개선을 보였다.

**저자**: < >

## ѱ 

****: <>

****:
- <׸>

**ֿ **:
- <׸>


**저자**: Summra Saleem; Muhammad Nabeel Asim; Andreas Dengel
**저자**: Complex & Intelligent Systems, Vol.12
**저자**: 2025-12-15
**저자**: https://doi.org/10.1007/s40747-025-02143-w

## 초록 (원문)

Abstract Within software development life-cycle, requirements guide the entire development process from inception to completion by ensuring alignment between stakeholder expectations and the final product. Requirements extraction from miscellaneous information is a challenging and complex task. Manual extraction of requirements is not only prone to human error but also contributes to increased project costs and delayed project timelines. To automate the requirement extraction process, researchers have investigated the potential of deep learning architectures, large language models (LLM) and generative language models such as ChatGPT and Gemini. However, the performance of requirements extraction could be further enhanced through the development of predictive pipelines by utilizing the combined potential of language models and deep learning architectures. To develop a powerful AI application for requirements extraction by utilizing the combined potential of LLMs and DL architectures, this study presents ReqNet framework. The framework encompasses 7 most widely used LLMs variants (small, large, Xlarge, XXlarge) and 2 DL architectures (LSTM, GRU). The framework facilitates the development of three distinct types predictive pipelines, namely standalone LLMs, LLMs + external classifiers and an ensemble of multiple LLMs representation + external classifiers. Extensive experimentation of 48 predictive pipelines across 2 public core datasets and 1 independent test set, demonstrates that predictive pipelines made up from LLMs and DL architectures generally exhibited superior performance compared to pipelines solely reliant on LLMs. In addition, a ensemble of three distinct LLMs (ALBERT, BERT and XLNet) and LSTM classifier achieved a 3% improvement in F1-score over state-of-the-art predictors on the PURE dataset, a 10% improvement on the Dronology dataset and a 3% improvement on the RFI independent test set.

## 키워드

Classifier (UML), Pipeline transport, Ensemble forecasting, Computational intelligence, Generative model, Process (computing), Stakeholder, Information extraction

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모


