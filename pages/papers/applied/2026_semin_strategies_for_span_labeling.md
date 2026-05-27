---
title: "Strategies for Span Labeling with Large Language Models"
authors: ['Danil Semin', 'Ondřej Dušek', 'Zdeněk Kasner']
year: 2026
venue: "ArXiv.org"
tags: ['Topic Modeling', 'Natural Language Processing Techniques', 'Authorship Attribution and Profiling']
source: raw/applied/applied_2026_Strategies_for_Span_Label_nodoi.md
---

# Strategies for Span Labeling with Large Language Models
**제목(한글)**: 거대 언어 모델을 활용한 스팬 레이블링 전략

## 한국어 요약

**연구질문**: 개체명 인식(NER), 오류 감지 등 스팬 레이블링 태스크에서, 생성형 LLM이 입력 텍스트의 특정 부분을 명시적으로 참조하는 메커니즘을 갖추지 않아 발생하는 비일관성 문제를 어떻게 해결할 수 있는가?

**방법론**:
- 스팬 레이블링 전략을 세 가지 유형으로 분류: 입력 텍스트에 태그를 삽입하는 방식, 스팬의 수치 위치를 인덱싱하는 방식, 스팬 내용을 직접 매칭하는 방식
- 콘텐츠 매칭의 한계를 보완하는 새로운 제약 디코딩 방법인 LogitMatch를 제안하고, 네 가지 다양한 태스크에서 모든 전략의 성능을 비교 평가

**주요 결과**:
- 태깅 방식이 강건한 기본 베이스라인으로 유지되는 가운데, LogitMatch가 스팬 매칭 오류를 제거하여 경쟁적 매칭 기반 방법들을 개선하고 일부 설정에서 다른 전략들을 능가함을 확인

**저자**: Danil Semin; Ondřej Dušek; Zdeněk Kasner
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-01-23
**DOI**: 

## 초록 (원문)

Large language models (LLMs) are increasingly used for text analysis tasks, such as named entity recognition or error detection. Unlike encoder-based models, however, generative architectures lack an explicit mechanism to refer to specific parts of their input. This leads to a variety of ad-hoc prompting strategies for span labeling, often with inconsistent results. In this paper, we categorize these strategies into three families: tagging the input text, indexing numerical positions of spans, and matching span content. To address the limitations of content matching, we introduce LogitMatch, a new constrained decoding method that forces the model's output to align with valid input spans. We evaluate all methods across four diverse tasks. We find that while tagging remains a robust baseline, LogitMatch improves upon competitive matching-based methods by eliminating span matching issues and outperforms other strategies in some setups.

## 키워드

Categorization, Generative grammar, Variety (cybernetics), Matching (statistics), Decoding methods, Span (engineering), Search engine indexing

## 위키 연관

- [[pages/concepts/personal_network|퍼스널 네트워크]]

## 메모

