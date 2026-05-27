---
title: "Fine-tuning SciBERT to enable ASJC-based assessments of the disciplinary orientation of research collections"
authors: ['Michael Gusenbauer', 'Jochen Endermann', 'Harald Huber', 'Simone I. Strasser', 'Andreas‐Nizar Granitzer', 'Thomas Ströhle']
year: 2025
venue: "Scientometrics"
tags: ['Text and Document Classification Technologies', 'Advanced Graph Neural Networks', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2025_Finetuning_SciBERT_to_ena_s11192_025_05490_0.md
---

# Fine-tuning SciBERT to enable ASJC-based assessments of the disciplinary orientation of research collections

**제목(한글)**: ASJC 기반 연구 컬렉션의 학문 지향성 평가를 위한 SciBERT 미세조정

## 한국어 요약

**연구질문**: ASJC(All Science Journal Classification) 분류 체계의 한계를 극복하기 위해 SciBERT를 다중 레이블 분류용으로 미세조정하면 개별 문서 수준에서 학문 지향성을 얼마나 정확하게 평가할 수 있는가?

**방법론**:
- SciBERT 모델을 307개 ASJC 주제에 대해 다중 레이블 분류용으로 미세조정
- Crossref 대규모 데이터셋 사용, 제목·초록·출처명 메타데이터 활용
- 선택적 메타데이터 제거(overfitting 완화) 및 데이터 증강 전략 적용
- 맞춤형 레이블 평균화 방법으로 개별 문서 및 대규모 컬렉션의 학문 지향성 비교 가능

**주요 결과**:
- 완전 메타데이터 사용 시 307개 주제에서 가중 F1-score 0.892 달성
- 출처명 정보 없이도 F1-score 0.532로 준수한 성능 유지
- 모델을 Hugging Face를 통해 공개하여 재현 가능성과 후속 연구 촉진

**저자**: Michael Gusenbauer; Jochen Endermann; Harald Huber; Simone I. Strasser; Andreas‐Nizar Granitzer; Thomas Ströhle
**출처**: Scientometrics, Vol.131, pp.2401-2438
**발행일**: 2025-12-01
**DOI**: https://doi.org/10.1007/s11192-025-05490-0

## 초록 (원문)

Abstract Subject classification is essential for navigating scientific literature, yet the influential All Science Journal Classification (ASJC) has limited practical applicability. Its limitations stem from reliance on an incomplete source list restricted to Scopus content, and from journal-level classifications that often misrepresent individual documents. The most significant recent development in ASJC-based classification is OpenAlex, but it narrows the framework by reducing the number of categories and enforcing single-label assignments—both of which diminish classification accuracy. In response, this study introduces the first open, multi-label, implementation of the ASJC taxonomy that more accurately classifies individual documents, including those published in general science or interdisciplinary journals. We develop a fine-tuned SciBERT model for multi-label classification across 307 ASJC subjects, trained on a large-scale Crossref dataset using title, abstract, and source title metadata. The model achieves a weighted F1-score of 0.892 on 307 subjects and 0.934 on its 26 parent subjects on a Crossref test set with full metadata. It maintains respectable performance-0.532 and 0.694, respectively—even without the source title information that ASJC classification relies upon. Our fine-tuning strategy includes selective metadata omission to mitigate overfitting and data augmentation for underrepresented categories. In addition, we introduce a tailored label-averaging method that enables assessment of the disciplinary orientation and comparison of individual documents and larger collections—such as researcher portfolios, institutions, and entire databases. To promote transparency, reproducibility, and further research, we openly release our model via Hugging Face ( https://huggingface.co/asjc-classification ), providing ready-to-use ASJC-based subject classification.

## 키워드

Overfitting, Metadata, Subject (documents), Set (abstract data type), Scopus, Taxonomy (biology), Discipline, Orientation (vector space)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

