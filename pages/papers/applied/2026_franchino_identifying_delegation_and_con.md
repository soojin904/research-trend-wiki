---
title: "Identifying delegation and constraints in legislative texts: A computational method applied to the European Union"
authors: ['Fabio Franchino', 'Marta Migliorati', 'Giovanni Pagano', 'Valerio Vignoli']
year: 2026
venue: "European Union Politics"
tags: ['Artificial Intelligence in Law', 'Legal Language and Interpretation', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_Identifying_delegation_an_14651165261423778.md
---

# Identifying delegation and constraints in legislative texts: A computational method applied to the European Union
**제목(한글)**: 입법 문서 내 권한 위임 및 제약 조건 식별: 유럽연합(EU)에 적용된 계산 방법론

**저자**: Fabio Franchino; Marta Migliorati; Giovanni Pagano; Valerio Vignoli
**출처**: European Union Politics, Vol.None
**발행일**: 2026-03-04
**DOI**: https://doi.org/10.1177/14651165261423778

## 한국어 요약

**연구질문**: 지난 수십 년 동안 재정된 유럽연합(EU) 법률문서 속에서 행정 기관 등에의 '권한 위임(delegation)' 규정과 이를 통제하는 '제약 조건(constraints)' 문장을 트랜스포머 모델 및 구문 규칙 기반 computational linguistics로 어떻게 고정밀 추출할 수 있는가?

**방법론**:
- 1958~2019년 사이에 제정된 9,319개의 EU 법안으로부터 600,000개 이상의 법률 문장 추출
- 입법자가 사용하는 특유의 통사 구조를 포착하는 구문 규칙 추출 엔진 파이프라인 개발 및 최신 Transformer 분류기와 성능 대조 실험 진행

**주요 결과**:
- 본 구문 파이프라인 모델이 인간 판독 데이터셋과의 비교 검증 결과 Transformer 계열 모델의 인덱싱 성능을 뛰어넘는 고도의 판별력을 입증함
- 추출된 데이터 분석을 통해 EU 입법 역사 속에서 의사결정 권한이 위임되고 제어되는 정책 통제 패턴의 변화를 역사적으로 명확히 규명함


## 초록 (원문)

We introduce a computational method for identifying delegating and constraining provisions in European Union (EU) laws. Leveraging the syntactic structures employed by legislators, we developed a set of extraction rules applied through a custom-built computational linguistics pipeline. We run through the pipeline more than 600,000 legal sentences that we extracted from 9319 laws adopted between 1958 and 2019. The application performs very well vis-á-vis human annotation and outperforms transformer models. The produced patterns of authority delegation and constraint resonate with our knowledge of the policymaking and history of the EU. Our approach provides valuable insights for designing transparent and adaptable rule-based computational linguistic methods of legal text analysis. We also release the comprehensively annotated dataset and the fine-tuned transformer models developed for this task.

## 키워드

European union, Delegation, Annotation, Legislature, Computational model, Set (abstract data type), Constraint (computer-aided design), Estonian

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

