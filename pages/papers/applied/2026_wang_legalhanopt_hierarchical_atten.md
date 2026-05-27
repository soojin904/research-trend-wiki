---
title: "LegalHANOpt: A Hierarchical Attention Network with BOHB Optimization for Predicting and Explaining Legal Case Decisions"
authors: ['Aijun Wang']
year: 2026
venue: "Informatica"
tags: ['Artificial Intelligence in Law', 'Topic Modeling', 'Explainable Artificial Intelligence (XAI)']
source: raw/applied/applied_2026_LegalHANOpt_A_Hierarchica_inf_v50i8_10451.md
---

# LegalHANOpt: A Hierarchical Attention Network with BOHB Optimization for Predicting and Explaining Legal Case Decisions
**제목(한글)**: LegalHANOpt: 사법 판결 예측 및 설명을 위한 BOHB 최적화 기반 계층적 어텐션 네트워크

**저자**: Aijun Wang
**출처**: Informatica, Vol.50
**발행일**: 2026-02-21
**DOI**: https://doi.org/10.31449/inf.v50i8.10451

## 한국어 요약

**연구질문**: 복잡하고 장황한 법률 텍스트에서 판결 결과를 고도로 예측하고 의사결정의 근거를 설명해줄 수 있는 최적화된 계층적 신경망을 설계할 수 있는가?

**방법론**:
- 단어 및 문장 수준의 맥락을 분석하는 계층적 어텐션 네트워크(HAN) 아키텍처 제안
- BOHB(Bayesian Optimization with Hyperband) 기법을 활용하여 학습률, 드롭아웃 등 초매개변수(hyperparameters) 자동 최적화
- 판결 결과, 법률 조항, 사건 사실을 포함한 대규모 사법 판례 데이터셋 학습 및 검증

**주요 결과**:
- 제안된 LegalHANOpt 모델이 기존 분류 모델을 능가하여 정확도 91%(0.91), 매크로 F1 0.83, AUC-ROC 0.92의 높은 예측 정확도 달성
- 어텐션 맵(Attention Map) 시각화를 통해 판결 예측에 영향을 미친 법률 문서 내 중요 문장을 하이라이트함으로써 높은 설명 가능성(explainability) 확보
- 법률 전문가의 신속하고 정확한 의사결정을 보조할 수 있는 인공지능 도구로서의 가능성 제시


## 초록 (원문)

Legal documents are often lengthy and complex, making it challenging and time-consuming for experts to accurately predict case outcomes. Older methods are not well-suited to the structure and language used in legal texts. This paper proposes a model called LegalHANOpt (Legal Hierarchical Attention Network with Optimized Parameters) to make accurate predictions about legal case decisions and explain how those decisions are made. LegalHANOpt utilizes a Hierarchical Attention Network (HAN) that analyzes legal documents by examining individual words and sentences, much like lawyers typically do. To improve the model's performance, Bayesian Optimization with Hyperband (BOHB) is utilized. This sophisticated method automatically determines the optimal settings for training the model, such as learning rate and dropout. The LegalHANOpt is trained on an extensive collection of past legal cases, including relevant facts, laws, and decisions. Results show that LegalHANOpt gives more accurate predictions than older methods achieving superior performance with an accuracy of 0.91%, macro F1-score of 0.83%, and AUC-ROC of 0.92%. It also highlights essential parts of the text, helping users understand why the model made a particular decision. In short, LegalHANOpt is a valuable and explainable tool to support legal experts in making better and faster decisions.

## 키워드

Bayesian network, Macro, Subject-matter expert, Dynamic Bayesian network, Legal case, Deep learning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

