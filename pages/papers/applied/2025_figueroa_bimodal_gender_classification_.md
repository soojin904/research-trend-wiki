---
title: "Bimodal Gender Classification Across Community Question-Answering Platforms"
authors: ['Alejandro Figueroa', 'Esteban Martínez']
year: 2025
venue: "Information"
tags: ['Expert finding and Q&A systems', 'Topic Modeling', 'Advanced Graph Neural Networks']
source: raw/applied/applied_2025_Bimodal_Gender_Classifica_info17010007.md
---

# Bimodal Gender Classification Across Community Question-Answering Platforms

**제목(한글)**: 커뮤니티 질의응답 플랫폼에서의 바이모달 성별 분류

## 한국어 요약

**연구질문**: 텍스트 상호작용과 프로필 이미지 두 가지 양식(Bimodal)을 결합한 트랜스포머 모델이 커뮤니티 질의응답(cQA) 플랫폼에서 단일 양식 모델보다 성별 분류를 더 정확하게 수행할 수 있는가?

**방법론**:
- 텍스트와 이미지 신호를 융합하는 바이모달(Bimodal) 트랜스포머 모델 활용
- ViLT, CLIP, FLAVA 세 가지 멀티모달 트랜스포머 모델 비교 평가
- Stack Exchange(희소 데이터셋)와 Yahoo! Answers, Reddit(대규모 컬렉션) 데이터 활용
- 정성적·정량적 분석으로 프로필 아바타의 기여도와 한계 탐구

**주요 결과**:
- 프로필 아바타는 텍스트 입력에 나타난 특정 성별 신호를 강화하며 긍정적으로 기여
- 동일 프로필 사진을 공유하는 커뮤니티 구성원 수가 많을수록 아바타의 기여도 증가
- 임시/가짜 프로필 구별 목적으로는 이미지 활용이 오히려 역효과를 낼 수 있음
- ViLT는 희소 데이터셋(Stack Exchange)에, CLIP/FLAVA는 대규모 데이터셋에 각각 우수

**저자**: Alejandro Figueroa; Esteban Martínez
**출처**: Information, Vol.17, pp.7-7
**발행일**: 2025-12-22
**DOI**: https://doi.org/10.3390/info17010007

## 초록 (원문)

Community Question-Answering (cQA) sites have an urgent need to be increasingly efficient at (a) offering contextualized/personalized content and (b) linking open questions to people willing to answer. Most recent ideas with respect to attaining this goal combine demographic factors (i.e., gender) with deep neural networks. In essence, recent studies have shown that high gender classification rates are perfectly viable by independently modeling profile images or textual interactions. This paper advances this body of knowledge by leveraging bimodal transformers that fuse gender signals from text and images. Qualitative results suggest that (a) profile avatars reinforce one of the genders manifested across textual inputs, (b) their positive contribution grows in tandem with the number of community fellows that provide this picture, and (c) their use might be detrimental if the goal is distinguishing throwaway/fake profiles. From a quantitative standpoint, ViLT proved to be a better alternative when coping with sparse datasets such as Stack Exchange, whereas CLIP and FLAVA excel with a large-scale collection—namely, Yahoo! answers and Reddit.

## 키워드

Artificial neural network, Coping (psychology), Transformer, Deep neural networks, Qualitative research

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모

