---
title: "LLM-Enhanced Theme Identification and Classification of Urban Housing Policy Texts"
authors: ['Xiaodie Yuan', 'Wenkang Zhang', 'Chengle Zhou', 'Chunshan Zhou']
year: 2026
venue: "E3S Web of Conferences"
tags: ['Computational and Text Analysis Methods', 'Housing, Finance, and Neoliberalism', 'Housing Market and Economics']
source: raw/applied/applied_2026_LLMEnhanced_Theme_Identif_202668301017.md
---

# LLM-Enhanced Theme Identification and Classification of Urban Housing Policy Texts
**제목(한글)**: 도시 주택 정책 텍스트의 LLM 강화 테마 식별 및 분류

**저자**: Xiaodie Yuan; Wenkang Zhang; Chengle Zhou; Chunshan Zhou
**출처**: E3S Web of Conferences, Vol.683, pp.01017-01017
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1051/e3sconf/202668301017

## 한국어 요약

**연구질문**: 전통적 텍스트 마이닝의 맹점인 맥락 이해 결핍을 극복하고, 대규모 언어 모델과 기계학습 모델을 결합해 도시 주택 정책 문서의 핵심 테마를 신속하고 정밀하게 분류할 수 있는가?

**방법론**:
- Mengzi-BERT-Base(MBB)를 활용한 중국 주택 정책 문서의 시맨틱 인코딩 수행
- GPT-4o를 이용해 거시적 논리 분석 및 문맥적 정책 키워드 특징 추출
- 두 가지 다른 특성의 피처 벡터를 랜덤 포레스트(Random Forest) 모델의 피처로 결합하여 최종 분류기 학습

**주요 결과**:
- 제안된 MBB-GPT-RandomForest 융합 프레임워크가 복잡한 도시 주택 정책 문서를 4개의 주요 핵심 테마로 유의미하게 자동 분류
- 종합 성능 지표에서 전체 분류 정확도 70.25%, 개별 주제별 최고 정확도 75.56%를 기록하여 실무 정책 분석 도구로서의 가치를 입증


## 초록 (원문)

Urban housing development has always been a key area of focus in urban studies. Accurate understanding of housing policy texts is of great significance for the sustainable development of urban housing. Different from traditional text analysis methods, we have proposed a machine learning (ML) framework driven by a large language models (LLMs) to quickly and accurately extract policy text themes and classify them. We used Mengzi-BERT-Base (MBB) for semantic encoding of policy documents, used GPT-4o to extract policy keywords and grasp the macro logic, and finally integrated the features of the two using a random forest model to output classification results. The results show that this framework divides housing policy texts into 4 core themes, with an overall accuracy rate of 70.25%, and the accuracy rate of individual themes is 75.56%, indicating that this framework has certain application value in urban policy text analysis.

## 키워드

GRASP, Identification (biology), Theme (computing), Urban policy, Macro, Urban planning, Focus (optics), Random forest

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

