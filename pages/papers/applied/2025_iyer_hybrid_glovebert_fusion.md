---
title: "A Hybrid GloVe-BERT Fusion Model with Multi-Level Attention-Based CNN-BiLSTM for Sentiment Analysis"
authors: ['Yashaswini Iyer', 'Gnanaprasanambikai L']
year: 2025
venue: "ECTI Transactions on Computer and Information Technology (ECTI-CIT)"
tags: ['Sentiment Analysis and Opinion Mining', 'Misinformation and Its Impacts', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2025_A_Hybrid_GloVeBERT_Fusion_ecti_cit_2026201_263366.md
---

# A Hybrid GloVe-BERT Fusion Model with Multi-Level Attention-Based CNN-BiLSTM for Sentiment Analysis

**제목(한글)**: 감성 분석을 위한 다단계 어텐션 기반 CNN-BiLSTM 적용 하이브리드 GloVe-BERT 융합 모델

## 한국어 요약

**연구질문**: GloVe 임베딩과 BERT 임베딩을 다단계 융합 전략과 어텐션 메커니즘을 통해 결합한 하이브리드 CNN-BiLSTM 모델이 기후변화 뉴스 헤드라인의 감성 분류에서 기존 단일 모델보다 더 높은 성능을 달성할 수 있는가?

**방법론**:
- GloVe 정적 임베딩과 BERT 동적 문맥 임베딩의 다단계 융합 전략 설계
- 병렬 CNN-BiLSTM 분기, 잔차 연결(residual connections), 계층적 어텐션 모듈 구조 채택
- 3점 극성 척도로 주석 처리된 기후 관련 헤드라인 1,023건 평가

**주요 결과**:
- 하이브리드 모델이 80.47% 정확도로 SVM(66%), 나이브 베이즈, K-NN 등 고전 기준 모델 및 단일 CNN(78.63%), BiLSTM(78.36%)을 능가함
- 쌍체 t-검정(paired t-test)으로 모델 간 성능 차이가 통계적으로 유의미함을 확인
- 컴팩트한 도메인 적응형 딥러닝 모델이 기후 담화 추적과 정보 정책 의사결정에 효과적인 도구임을 입증

**저자**: Yashaswini Iyer; Gnanaprasanambikai L
**출처**: ECTI Transactions on Computer and Information Technology (ECTI-CIT), Vol.20, pp.15-25
**발행일**: 2025-12-27
**DOI**: https://doi.org/10.37936/ecti-cit.2026201.263366

## 초록 (원문)

Gauging public sentiment toward climate policy from information-rich news headlines remains challenging for conventional text classification approaches. Conventional sentiment analysis tools miss contextual subtleties in brief headlines, whereas deep learning models capture the public perception more accurately. The proposed work presents hybrid Convolutional Neural Network (CNN) and Bidirectional Long Short-Term Memory (BiLSTM) model that uses combination of GloVe and BERT embeddings with an attention layer for sentiment analysis of climate change news headlines. The novelty of this research lies in the use of GloVe and BERT embeddings through a multi-stage fusion strategy and an attention mechanism to enhance text classification performance in a hybrid model. The architecture employs a hierarchical layering approach to fuse static GloVe embeddings with dynamic, contextualized BERT representations through attention modules that enables the network to selectively focus on salient features. To further model complex semantic dependencies, the design incorporates parallel CNN-BiLSTM branches, structured with residual connections and bolstered with additional layers of attention. Evaluated on 1,023 climate-related headlines annotated on a three-point polarity scale, the proposed model achieves an accuracy of 80.47%, outperforming classi- cal baselines (SVM, Naive Bayes, K-NN) and single branch deep networks (CNN:78.63%, BiLSTM:78.36%). The predictive accuracy of the hybrid model is evaluated using a paired t-test to determine whether the difference between models is statistically significant; this is confirmed by rejecting null hypothesis and accepting alternate hypothesis.This study demonstrates that compact, domain-adaptive deep learning models incorporating contextual embeddings and attention mechanisms that can effectively extract sentiment from news headlines, offering scalable, evidence based tools for tracking climate discourse and information policy decisions.

## 키워드

Sentiment analysis, Deep learning, Novelty, Convolutional neural network, Focus (optics), Artificial neural network, Topic model, Fuse (electrical)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

