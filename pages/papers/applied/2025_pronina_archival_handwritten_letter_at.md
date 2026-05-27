---
title: "Archival Handwritten Letter Attribution Using Siamese Neural Networks"
authors: ['Nataliia Mikhailovna Pronina']
year: 2025
venue: "Russian Digital Libraries Journal"
tags: ['Handwritten Text Recognition Techniques', 'Topic Modeling', 'Image Retrieval and Classification Techniques']
source: raw/applied/applied_2025_Archival_Handwritten_Lett_1562_5419_2025_28_6_1454_.md
---

# Archival Handwritten Letter Attribution Using Siamese Neural Networks

**제목(한글)**: 샴 신경망(Siamese Neural Networks)을 활용한 아카이브 필기 문서 저자 귀속

## 한국어 요약

**연구질문**: 샴 신경망 기반 방법은 17~19세기 아카이브 필기 문서의 저자 귀속을 자동화할 수 있는가?

**방법론**:
- 샴 신경망 아키텍처로 판별 벡터 표현(임베딩) 추출
- 이미지 단편 수준(300×300 px) 및 개별 텍스트 줄 수준 두 가지 분석 접근법 비교
- 스캔 품질 저하, 필체 변화, 심각한 클래스 불균형(저자당 1~50개 이상 샘플) 등 아카이브 특유 과제 대응

**주요 결과**:
- 알려진 저자 문서 분류뿐 아니라 미지 저자 원고 식별에도 효과적
- 후속 전문가 검증 대상을 크게 축소하는 예비 선별 도구로서 유용
- 데이터 전처리 알고리즘과 두 분석 접근법의 비교 결과 제시

**저자**: Nataliia Mikhailovna Pronina
**출처**: Russian Digital Libraries Journal, Vol.28, pp.1454-1480
**발행일**: 2025-12-01
**DOI**: https://doi.org/10.26907/1562-5419-2025-28-6-1454-1480

## 초록 (원문)

This paper presents a method for the automated attribution of archival handwritten letters based on a Siamese neural network, addressing a key challenge in the digital humanities—the authentication of historical documents. The research is motivated by the mass digitization of 17th- to 19th-century archives, where attribution is often hindered by incomplete or inaccurate metadata about the authors. The method is designed for real-world document collections and accounts for challenges typical of archival materials: poor-quality scans, significant handwriting variation, and substantial class imbalance (from 1 to over 50 samples per author). The use of a Siamese network architecture enables the extraction of discriminative vector representations (embeddings). Based on these embeddings, the method not only classifies documents by known authors but also effectively identifies manuscripts that do not match any known author in the archive. This significantly narrows down the pool of candidates for subsequent expert verification. The study introduces a data preprocessing algorithm and provides a comparative analysis of two approaches to text analysis: at the image fragment level (300×300 px) and at the individual text line level. The developed tool offers archivists and philologists an effective solution for the preliminary sorting and attribution of handwritten documents in large collections.

## 키워드

Handwriting, Preprocessor, Metadata, Artificial neural network, Digitization, Discriminative model, Handwriting recognition, Class (philosophy)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

