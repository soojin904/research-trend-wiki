---
title: "PRISM: LLM-Guided Semantic Clustering for High-Precision Topics"
authors: ['Connor Douglas', 'Utkucan Balci', 'Joseph Aylett-Bullock']
year: 2026
venue: "ArXiv.org"
tags: ['Topic Modeling', 'Computational and Text Analysis Methods', 'Expert finding and Q&A systems']
source: raw/applied/applied_2026_PRISM_LLMGuided_Semantic__nodoi.md
---

# PRISM: LLM-Guided Semantic Clustering for High-Precision Topics
**제목(한글)**: PRISM: 고정밀 토픽 발굴을 위한 LLM 안내 의미적 클러스터링

## 한국어 요약

**연구질문**: LLM의 풍부한 표현 능력과 잠재 의미 클러스터링 방법의 저비용·해석 가능성을 결합하여, 좁은 도메인 내 유사 토픽들을 정밀하게 분리하는 토픽 모델링 프레임워크를 어떻게 구성할 수 있는가?

**방법론**:
- Precision-Informed Semantic Modeling(PRISM) 프레임워크 제안: LLM이 코퍼스 샘플에 희소 레이블을 제공하면 문장 인코딩 모델을 파인튜닝
- 임계값 기반 클러스터링으로 임베딩 공간 분할 — 근접 토픽 간 분리 향상
- 학생-교사(Student-Teacher) 파이프라인을 통해 희소한 LLM 감독을 경량 모델로 증류

**주요 결과**:
- 복수의 코퍼스에서 최신 로컬 토픽 모델 및 대형 프런티어 임베딩 모델 클러스터링 대비 토픽 분리성 향상
- 소량의 LLM 쿼리만으로 학습 가능하며, 웹 규모 텍스트 분석과 온라인 미묘한 주장·서브토픽 추적에 실용적인 배포 가능 프레임워크 제공

**저자**: Connor Douglas; Utkucan Balci; Joseph Aylett-Bullock
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-04-03
**DOI**: 

## 초록 (원문)

In this paper, we propose Precision-Informed Semantic Modeling (PRISM), a structured topic modeling framework combining the benefits of rich representations captured by LLMs with the low cost and interpretability of latent semantic clustering methods. PRISM fine-tunes a sentence encoding model using a sparse set of LLM- provided labels on samples drawn from some corpus of interest. We segment this embedding space with thresholded clustering, yielding clusters that separate closely related topics within some narrow domain. Across multiple corpora, PRISM improves topic separability over state-of-the-art local topic models and even over clustering on large, frontier embedding models while requiring only a small number of LLM queries to train. This work contributes to several research streams by providing (i) a student-teacher pipeline to distill sparse LLM supervision into a lightweight model for topic discovery; (ii) an analysis of the efficacy of sampling strategies to improve local geometry for cluster separability; and (iii) an effective approach for web-scale text analysis, enabling researchers and practitioners to track nuanced claims and subtopics online with an interpretable, locally deployable framework.

## 키워드

Cluster analysis, Interpretability, Topic model, Embedding, Sentence, Pipeline (software), Set (abstract data type), Space (punctuation)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

