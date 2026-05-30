---
title: "AI-Based Approaches for Multi-Class Text Classification in Social Media: A Comparative Study"
authors: ['Oleg Gabrielyan', 'Mikhail Gasparyan', 'Ivan Kravchenko', 'Milada Krapivina']
year: 2025
venue: "Engineering Technology & Applied Science Research"
tags: ['Text and Document Classification Technologies', 'Sentiment Analysis and Opinion Mining', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2025_AIBased_Approaches_for_Mu_etasr_14303.md
---

# AI-Based Approaches for Multi-Class Text Classification in Social Media: A Comparative Study

**제목(한글)**: 소셜 미디어에서의 다중 클래스 텍스트 분류를 위한 AI 기반 접근법: 비교 연구

## 한국어 요약

**연구질문**: VKontakte에서 수집된 실세계 소셜 미디어 데이터에서 LSTM, DeBERTa, AutoML 세 가지 텍스트 분류 접근법은 클래스 불균형과 범주 중첩 조건하에서 각각 어떤 성능을 보이는가?

**방법론**:
- VKontakte에서 "영웅(hero)"이라는 단어의 의미 범주별로 레이블링된 데이터셋 구성
- LSTM(장단기 기억 네트워크), DeBERTa(트랜스포머 기반), LightAutoML(AutoML) 세 모델 비교
- 클래스 균형화 및 레이블 정제 실험으로 소수 클래스 분류 성능 개선 시도

**주요 결과**:
- DeBERTa가 매크로 F1 점수 0.32로 균형 잡힌 최우수 성능 달성
- AutoML(LightAutoML)은 낮은 자원 요구량으로 최고 원시 정확도 약 65% 기록
- LSTM은 데이터셋 규모와 복잡성으로 인해 제한적 효과 확인
- 클래스 균형화 및 레이블 정제 시 소수 클래스 분류 성능 향상 확인

**저자**: Oleg Gabrielyan; Mikhail Gasparyan; Ivan Kravchenko; Milada Krapivina
**출처**: Engineering Technology & Applied Science Research, Vol.15, pp.29833-29839
**발행일**: 2025-12-08
**DOI**: https://doi.org/10.48084/etasr.14303

## 초록 (원문)

The increasing volume of unstructured textual data in social networks requires automated tools for efficient classification and monitoring. This study presents the design and evaluation of an AI-based system for multi-class text classification using a dataset collected from VKontakte. The dataset was annotated into several semantic categories of the word "hero," serving as a domain-specific case study for testing classification models under real-world constraints such as class imbalance, overlapping categories, and limited training samples. Three approaches were implemented and compared: a Long Short-Term Memory (LSTM) network, the transformer-based DeBERTa model, and an AutoML solution (LightAutoML). Experimental results show that DeBERTa achieves the best-balanced performance with a macro-F1 score of 0.32, while AutoML provides the highest raw accuracy (~65%) with lower resource requirements. LSTM demonstrated limited effectiveness due to the dataset size and complexity. Additional experiments with class balancing and refined labeling improved performance across underrepresented classes. The findings highlight the trade-off between model complexity, computational cost, and classification performance, and confirm the applicability of transformer-based architectures for text analysis in noisy and imbalanced environments. The proposed system can serve as a foundation for automated monitoring tools in social media and other real-world NLP applications.

## 키워드

Class (philosophy), Word (group theory), Social media, Resource (disambiguation), Raw data, Word list

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

