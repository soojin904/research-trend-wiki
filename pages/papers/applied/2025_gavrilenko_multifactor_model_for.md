---
title: "A multifactor model for detecting propaganda in textual data"
authors: ['Olena Gavrilenko', 'Kyryl Feshchenko']
year: 2025
venue: "Information, computing and intelligent systems"
tags: ['Misinformation and Its Impacts', 'Computational and Text Analysis Methods', 'Public Relations and Crisis Communication']
source: raw/applied/applied_2025_A_multifactor_model_for_d_2786_8729_7_2025_342630.md
---

# A multifactor model for detecting propaganda in textual data

**제목(한글)**: 텍스트 데이터에서 선전 탐지를 위한 다요인 모델

## 한국어 요약

**연구질문**: 방대한 텍스트 데이터 내 선전(propaganda) 요소를 객관적이고 효율적으로 탐지하기 위한 방법론은 무엇인가?

**방법론**:
- 정량적 및 의미론적 텍스트 분석 (quantitative and semantic text analysis)
- 선형 컨볼루션(linear convolution)을 활용한 다요인 모델 구축
- 통계 분석, 지능형 데이터 분석, 기계 학습 (machine learning)을 통한 지표 값 계산
- 유틸리티 함수(utility function) 및 데이터셋 평균 기반의 선전 강도 정량화 및 분류

**주요 결과**:
- 선전 수준을 결정하는 13가지 어휘적, 구문론적, 의미론적 지표를 포함하는 다요인 모델 제시
- 각 요인의 영향 수준을 결정하는 알고리즘과 전체 선전 수준을 평가하는 척도 제안
- 전문가 라벨링 없이 텍스트 자료의 객관적 분류 가능
- 인간의 주관성을 배제하여 다양한 유형의 텍스트 데이터에서 선전 탐지를 위한 보편적인 분석 도구로서 기능

**저자**: Olena Gavrilenko; Kyryl Feshchenko
**출처**: Information, computing and intelligent systems, Vol.None, pp.160-179
**발행일**: 2025-12-27
**DOI**: https://doi.org/10.20535/2786-8729.7.2025.342630

## 초록 (원문)

Detecting elements of propaganda in large volumes of textual data is currently one of the key tools in combating the information warfare taking place worldwide. This paper presents a multifactor model for determining the level of propaganda in a publication. The analyzed publications included text-based news articles and social media posts, which were processed using both quantitative and semantic text analysis methods. The model was constructed using the method of linear convolution, which enables the integration of multiple heterogeneous indicators into a unified value reflecting the degree of propaganda. The proposed model considers thirteen indicators, each of which, when exhibiting a high value, signals the potential presence of propaganda within a text. The indicators encompass lexical, syntactic, and semantic characteristics such as emotional tone, subjective evaluation, presence of manipulative triggers, and calls to action. The value of each indicator was calculated using methods of statistical analysis, intelligent data analysis, and machine learning. An algorithm for determining the influence level of each factor was proposed, as well as a scale for assessing the overall level of propaganda. For every analyzed publication, a utility function value was computed to quantify its propaganda intensity. The threshold value of this utility function – beyond which a publication is considered propagandistic – was defined as the sample mean across the dataset. This approach allows for an objective classification of textual materials without the need for expert labeling. The advantage of the developed method lies in the fact that each indicator is derived exclusively from empirical statistical data and validated computational procedures, ensuring the elimination of human subjectivity. The study demonstrates that the modified multifactor model can serve as a universal analytical tool for detecting propaganda in various types of textual data, thereby enhancing the transparency and reliability of media content analysis.

## 키워드

Function (biology), Key (lock), Value (mathematics), Sample (material), Social media, Scale (ratio), Term (time)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

