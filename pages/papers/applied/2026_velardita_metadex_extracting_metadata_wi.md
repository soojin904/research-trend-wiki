---
title: "MetaDex: extracting metadata with confidence using generative AI."
authors: ['MICHELE VELARDITA']
year: 2026
venue: "Electronic Theses and Dissertations Repository (University of Pisa)"
tags: ['Handwritten Text Recognition Techniques', 'Topic Modeling', 'Text and Document Classification Technologies']
source: raw/applied/applied_2026_MetaDex_extracting_metada_nodoi.md
---

# MetaDex: extracting metadata with confidence using generative AI.
**제목(한글)**: MetaDex: 생성형 AI를 활용한 신뢰도 기반 메타데이터 추출

**저자**: MICHELE VELARDITA
**출처**: Electronic Theses and Dissertations Repository (University of Pisa), Vol.None
**발행일**: 2026-02-22
**DOI**: 

## 한국어 요약

**연구질문**: 서식이 다른 다수의 반정형 문서 이미지/텍스트로부터 사용자에게 정확성 신뢰 지표를 동반해 정보를 자동 추출해주는 신뢰성 높은 추출 시스템을 어떻게 구축할 수 있는가?

**방법론**:
- 이미지 OCR 판독 파이프라인과 생성형 AI(출력 로짓 획득이 가능한 모델 및 Black-box API) 융합 모듈 설계
- 정보 추출 과정에서 수반되는 모델의 불확실성(Uncertainty)을 수학적으로 계산 및 추정하는 기법 개발
- 추출된 개체(Entity)와 메타데이터의 신뢰성 검증을 돕는 메타데이터 추출 플랫폼 MetaDex 설계 및 유효성 평가

**주요 결과**:
- 사용자에게 단순 데이터 출력뿐만 아니라 추출 항목별 정확성 확률(Uncertainty-aware metric)을 시각 제시하여 오류를 방지함
- 다양한 오타나 템플릿 손상 상황에서도 추출 결과의 가독성과 해석력이 향상됨을 실증


## 초록 (원문)

This thesis project addresses the problem of structured extraction of heterogeneous data from semi-structured documents characterized by multiple formats and templates. The work focuses on document understanding and entity extraction tasks, using generative AI models, both black-box systems and models with access to output logits, combined with optical character recognition (OCR) pipelines. The primary focus is the implementation and experimental validation of uncertainty estimation techniques, with the goal of providing informative confidence metrics to the end user. Different uncertainty measures are evaluated on real-world document datasets. The results highlight the potential of uncertainty-aware extraction systems to improve reliability and interpretability in their outputs.

## 키워드

Interpretability, Metadata, Reliability (semiconductor), Generative grammar, Focus (optics), Information extraction, Generative model

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

