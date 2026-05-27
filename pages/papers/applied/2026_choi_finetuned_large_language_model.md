---
title: "Fine-tuned large language models can replicate expert coding better than trained coders: a study on informative signals sent by interest groups"
authors: ['Dahyun Choi', 'Denis Peskoff', 'Brandon Stewart']
year: 2026
venue: "Political Science Research and Methods"
tags: ['Computational and Text Analysis Methods', 'Misinformation and Its Impacts', 'Media Influence and Politics']
source: raw/applied/applied_2026_Finetuned_large_language__psrm_2025_10086.md
---

# Fine-tuned large language models can replicate expert coding better than trained coders: a study on informative signals sent by interest groups
**제목(한글)**: 미세 조정된 대형 언어 모델은 훈련된 코더보다 전문가 코딩을 더 잘 재현할 수 있다: 이익집단이 보내는 정보 신호 연구

**저자**: Dahyun Choi; Denis Peskoff; Brandon Stewart
**출처**: Political Science Research and Methods, Vol.None, pp.1-19
**발행일**: 2026-02-13
**DOI**: https://doi.org/10.1017/psrm.2025.10086

## 한국어 요약

**연구질문**: 이익집단이 정책 결정권자에게 보내는 문서에서 '실질적인 정치적 의사결정을 돕는 유익한 신호(Informative Signals)'와 '선호만 자극하고 실질 알맹이가 없는 신호(Associative Signals)'를 구분할 때, 미세 조정된 LLM의 코딩 정확성은 인간 코더에 필적하거나 능가할 수 있는가?

**방법론**:
- 이익집단이 발표한 정책 문서를 수집하여 분류 대상 구성
- 미세 조정(Fine-tuned)된 LLM, 단기 훈련된 작업자(Lightly trained workers), 크라우드워커(Crowdworkers), Zero-shot LLM의 텍스트 레이블링 정확도를 비교 분석
- 학습된 모델을 상이한 분야의 데이터셋 2개에 적용해 분포 외 일반화(OOD generalization) 성능 평가

**주요 결과**:
- 미세 조정된 LLM이 단기 학습된 작업자 및 일반 크라우드워커, 그리고 튜닝하지 않은 일반 LLM의 분류 성과를 넘어서서 전문가 수준의 분류 패턴을 보임
- 개발된 분류기가 원본 분포 밖의 외부 데이터셋에서도 우수한 재현력을 발휘하여 확장 가능한 정치 텍스트 코딩 도구로 기능할 수 있음을 검증함


## 초록 (원문)

Abstract Understanding how political information is transmitted requires tools that can reliably and scalably capture complex signals in text. While existing studies highlight interest groups as strategic information providers, empirical analysis has been constrained by reliance on expert annotation. Using policy documents released by interest groups, this study shows that fine-tuned large language models (LLMs) outperform lightly trained workers, crowdworkers, and zero-shot LLMs in distinguishing two difficult-to-separate categories: informative signals that help improve political decision-making and associative signals that shape preferences but lack substantive relevance. We further demonstrate that the classifier generalizes out of distribution across two applications. Although the empirical setting is domain-specific, the approach offers a scalable method for expert-driven text coding applicable to other areas of political inquiry.

## 키워드

Replicate, Classifier (UML), Associative property, Coding (social sciences), Politics, Language model

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

