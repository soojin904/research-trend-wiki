---
title: "Text Segmentation in Online Health Consultation Using Multi Layer Perceptron with Sentence Embedding and Sentence Features"
authors: ['Yunianita Rahmawati', 'Daniel Siahaan', 'Diana Purwitasari']
year: 2025
venue: "Informatica"
tags: ['Topic Modeling', 'Health Literacy and Information Accessibility', 'Machine Learning in Healthcare']
source: raw/applied/applied_2025_Text_Segmentation_in_Onli_inf_v49i19_9271.md
---

# Text Segmentation in Online Health Consultation Using Multi Layer Perceptron with Sentence Embedding and Sentence Features

**제목(한글)**: 문장 임베딩과 문장 특징을 활용한 다층 퍼셉트론 기반 온라인 의료 상담 텍스트 분절화

## 한국어 요약

**연구질문**: 의사-환자 소통의 여섯 가지 측면을 기준으로 온라인 의료 상담 텍스트를 효과적으로 분절화하는 방법은 무엇인가?

**방법론**:
- MLPSentFeat 모델 개발: 문장 특징을 구조 내에 직접 통합
- 가능도비(LR) 알고리즘으로 레이블 관련 단어 필터링, 정보이득(InfoGain)으로 최고 정보 특징 선택
- 극단적 레이블 불균형 데이터 처리 (합성 데이터나 복잡한 균형화 기법 없이)

**주요 결과**:
- 최적 모델 MLPSentFeat+DS2+Features3의 세그먼트 오류율 8.18% 달성
- 의료 정보 수집 측면에서 비표준 문장 유형(질문형) 인식 성능 개선
- 교차 도메인 적응성 입증으로 다양한 온라인 의료 상담 시스템에 적용 가능성 확인

**저자**: Yunianita Rahmawati; Daniel Siahaan; Diana Purwitasari
**출처**: Informatica, Vol.49
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.31449/inf.v49i19.9271

## 초록 (원문)

The six aspects of doctor-patient communication are universal and relevant to various medical contexts and are the basis for structuring and analyzing doctors' answer texts in online health care. Identifying each aspect of communication in the doctor's answers is important to ensure effective communication. There are three critical challenges in segmenting the doctor’s answers, i.e. limited public dataset, extreme imbalance data, and implicit semantic variations between aspects. This study proposed a novel approach to text segmentation, focusing on communication aspects, particularly doctor-patient interactions. Unlike classical segmentation methods, which relied on topic similarity, the proposed method segmented text based on the communicative function of each sentence, offering a more accurate reflection of the interaction structure in Online Health Consultation (OHC). The model developed, MLPSentFeat, integrated sentence features directly into its architecture and demonstrated effectiveness in handling data with highly imbalanced label distributions without the need for synthetic data or complex balancing techniques.Sentence features were formed using a combined approach: the Likelihood Ratio (LR) algorithm filtered words relevant to a label, and Information Gain (InfoGain) selected the most informative features. Experimental results showed that integrating these sentence features significantly enhanced the model's sensitivity to variations in linguistic structure, especially in recognizing non-standard sentence types, such as questions, which were prevalent in the information-gathering aspect of medical communication.The best model produced, MLPSentFeat+DS2+Features3, was optimized to achieve the lowest segment error percentage of 8.18%, despite a slight performance decline in some labels after optimization. The use of text normalization, along with appropriate data size, cleanliness, and alignment of sentence features with the sentences' semantic structure, proved crucial in preventing overfitting. The MLPSentFeat model was successfully applied across various domains, demonstrating cross-domain adaptability, including in doctor's answer in online medical consultation systems, with potential for further development to identify questions with diverse sentence structures.

## 키워드

Sentence, Segmentation, Embedding, Perceptron, Function (biology), Structuring, Layer (electronics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

