---
title: "Classifying Public Complaints in Denpasar: a Comparative Study of CNN, RNN, LSTM, and Stacking Deep Learning Models"
authors: ['I Komang Dharmendra', 'I Made Pasek Pradnyana Wijaya', 'I Made Agus Wirahadi Putra', 'Yohanes Priyo Atmojo', 'Luh Putu Safitri Pratiwi']
year: 2026
venue: "Jurnal Teknik Informatika (Jutif)"
tags: ['Imbalanced Data Classification Techniques', 'AI and HR Technologies', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Classifying_Public_Compla_1_jutif_2026_7_1_4153.md
---

# Classifying Public Complaints in Denpasar: a Comparative Study of CNN, RNN, LSTM, and Stacking Deep Learning Models
**제목(한글)**: 덴파사르시 대민 민원 분류: CNN, RNN, LSTM 및 스태킹 딥러닝 모델의 비교 연구

**저자**: I Komang Dharmendra; I Made Pasek Pradnyana Wijaya; I Made Agus Wirahadi Putra; Yohanes Priyo Atmojo; Luh Putu Safitri Pratiwi
**출처**: Jurnal Teknik Informatika (Jutif), Vol.7, pp.411-430
**발행일**: 2026-02-15
**DOI**: https://doi.org/10.52436/1.jutif.2026.7.1.4153

## 한국어 요약

**연구질문**: 시민들이 등록한 대민 민원 텍스트의 극심한 분류 클래스 불균형을 극복하고, 민원을 정확하게 자동 분류하기 위한 다중 딥러닝 앙상블 스태킹(Stacking) 모델의 유효성은 어떠한가?

**방법론**:
- 인도네시아 덴파사르시 민원 포털에서 수집된 10,302건의 시민 작성 민원 원문 활용
- 민원, 건의, 문의, 일반정보의 4개 클래스로 데이터 전처리
- 클래스 불균형 완화를 위해 SMOTE(Synthetic Minority Over-sampling Technique)를 적용하고 TF-IDF로 벡터화 수행
- CNN, RNN, LSTM 단일 모델 학습 및 이들을 메타 모델로 엮는 스태킹(Stacking) 앙상블 기법 설계 비교

**주요 결과**:
- 개별 딥러닝 베이스라인(CNN, RNN, LSTM) 모델 단독 구동 대비, 이들의 장점을 통합한 스태킹 앙상블 모델이 77.83%의 최고 분류 정확도와 74.38%의 F1-Score를 달성함
- 대민 포털 내 정보 처리 투명성과 신속성을 높여 행정 시스템 책임성을 강화하는 자동화 모델로의 실용 가능성을 입증함


## 초록 (원문)

The process of lodging complaints represents a complex behavioral construct, influenced by the interplay of emotional states, sociocultural factors, and situational contexts. It functions as a pivotal channel for citizens to express dissatisfaction regarding the quality of governmental services. This research aims to optimize public complaint management by leveraging deep learning-based text classification on citizen submissions collected from the Denpasar City Complaint Web Portal. The methodological approach integrates several neural network models, including Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Long Short-Term Memory (LSTM) networks, further enhanced by a Stacking ensemble technique that amalgamates the strengths of each architecture. The dataset consists of 10,302 textual records, categorized into four semantic classes: Complaints, Suggestions, Inquiries, and Information. To improve the robustness and reliability of the classification, advanced preprocessing steps were implemented, including the application of the Synthetic Minority Over-sampling Technique (SMOTE) to alleviate class imbalance and the utilization of Term Frequency–Inverse Document Frequency (TF-IDF) for extracting the most informative textual features. Empirical results demonstrate that the Stacking ensemble model significantly outperforms individual baseline models, achieving an accuracy of 77.83%, with recall and F1-score values of 74.38%. These findings highlight the effectiveness of ensemble deep learning approaches in multiclass complaint classification, thereby supporting improvements in public service delivery and fostering greater governmental transparency. Ultimately, this study contributes to the field of automated text classification by illustrating the potential of advanced neural architectures to enhance citizen participation and institutional accountability.

## 키워드

Complaint, Robustness (evolution), Deep learning, Convolutional neural network, Recall, Preprocessor, Field (mathematics), Ensemble learning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

