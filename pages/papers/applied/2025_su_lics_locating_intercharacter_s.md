---
title: "LICS: Locating Inter-Character Spaces for Multilingual Scene Text Detection"
authors: ['Po-Chyi Su', 'Meng-Chieh Lee', 'Yi-Ting Tung', 'Lizhu Chen', 'Chih-Hung Han', 'Tien-Ying Kuo']
year: 2025
venue: "Sensors"
tags: ['Handwritten Text Recognition Techniques', 'Multimodal Machine Learning Applications', 'Topic Modeling']
source: raw/applied/applied_2025_LICS_Locating_InterCharac_s26010197.md
---

# LICS: Locating Inter-Character Spaces for Multilingual Scene Text Detection

**제목(한글)**: LICS: 다국어 장면 텍스트 감지를 위한 문자 간 공간 찾기

## 한국어 요약

**연구질문**: 다국어 환경에서 장면 텍스트 감지의 문제를 해결하기 위해 언어에 구애받지 않는 구조적 단서로서 문자 간 간격을 감지하는 LICS(Locating Inter-Character Spaces) 방법을 소개한다.

**방법론**:
- 정확한 문자 간 간격 주석이 있는 합성 데이터로 훈련한 다음, 단어 수준 레이블이 있는 실제 데이터셋에 약하게 감독되는 학습을 적용하는 2단계 접근 방식을 사용한다.
- 대상 언어에서 문자 수준 주석의 필요성을 제거하여 주석 부담을 줄이면서 강력한 성능을 유지한다.
- 약 20,000개의 신중하게 주석 처리된 스트리트뷰 이미지로 구성된 새로운 장면 텍스트 데이터셋인 CSVT(Character-Labeled Street View Text)를 소개한다.

**주요 결과**:
- ICDAR 및 Total-Text 벤치마크에서 LICS의 강력한 성능을 입증하며, 특히 아시아 스크립트에서 우수하다.
- CSVT는 다국어 장면 텍스트 분석에서 보다 발전된 연구 개발을 촉진할 것으로 기대된다.

**저자**: Po-Chyi Su; Meng-Chieh Lee; Yi-Ting Tung; Lizhu Chen; Chih-Hung Han; Tien-Ying Kuo
**출처**: Sensors, Vol.26, pp.197-197
**발행일**: 2025-12-27
**DOI**: https://doi.org/10.3390/s26010197

## 초록 (원문)

Scene text detection in multilingual environments poses significant challenges. Traditional detection methods often struggle with language-specific features and require extensive annotated training data for each language, making them less practical for multilingual contexts. The diversity of character shapes, sizes, and orientations in natural scenes, along with text deformation and partial occlusions, further complicates the task of detection. This paper introduces LICS (Locating Inter-Character Spaces), a method that detects inter-character gaps as language-agnostic structural cues, enabling more feasible multilingual text detection. A two-stage approach is employed: first, we train on synthetic data with precise character gap annotations, and then apply weakly supervised learning to real-world datasets with word-level labels. The weakly supervised learning framework eliminates the need for character-level annotations in target languages, substantially reducing the annotation burden while maintaining robust performance. Experimental results on the ICDAR and Total-Text benchmarks demonstrate the strong performance of LICS, particularly on Asian scripts. We also introduce CSVT (Character-Labeled Street View Text), a new scene-text dataset comprising approximately 20,000 carefully annotated streetscape images. A set of standardized labeling principles is established to ensure consistent annotation of text locations, content, and language types. CSVT is expected to facilitate more advanced research and development in multilingual scene-text analysis.

## 키워드

Annotation, Task (project management), Set (abstract data type), Training set, Character (mathematics), Text detection, Labeled data, Natural language

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

