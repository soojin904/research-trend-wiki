---
title: "Analyzing OSHA Construction Accident Reports Using BERTopic Topic Modeling for Thematic Insights"
authors: ['Yuntao Cao', 'Ziyi Qu', 'Shujie Wu', 'Yuting Chen', 'Martin Skitmore', 'Xingguan Ma', 'Jun Wang']
year: 2025
venue: "Buildings"
tags: ['Occupational Health and Safety Research', 'Construction Project Management and Performance', 'BIM and Construction Integration']
source: raw/applied/applied_2025_Analyzing_OSHA_Constructi_buildings16010010.md
---

# Analyzing OSHA Construction Accident Reports Using BERTopic Topic Modeling for Thematic Insights

**제목(한글)**: BERTopic 토픽 모델링을 활용한 OSHA 건설 사고 보고서의 주제적 통찰 분석

## 한국어 요약

**연구질문**: BERTopic이 전통적인 LDA 모델 대비 건설 사고 보고서에서 더 유의미한 토픽을 발견할 수 있는가? 대규모 사고 보고서 텍스트에서 자동화된 NLP 기법으로 숨겨진 위험 패턴과 시간적 추세를 식별할 수 있는가?

**방법론**:
- OSHA의 2004~2023년 건설 사고 보고서 22,623건에 토픽 모델링(Topic Modeling) 적용
- BERTopic과 전통적 LDA(잠재 디리클레 할당) 모델의 성능 비교
- 문맥적 임베딩(Contextual Embeddings)을 활용한 BERTopic으로 세밀한 위험 시나리오 식별
- 토픽 일관성(Topic Coherence) 및 토픽 다양성(Topic Diversity) 지표로 모델 평가

**주요 결과**:
- BERTopic이 LDA 대비 토픽 일관성과 다양성 모두에서 우수한 성능 달성
- 직업-사고 패턴, 취약 근로자 집단, 사고 최다 발생 시기 등 실행 가능한 통찰 도출
- 전통적 텍스트 마이닝이 놓쳤던 세밀한 위험 시나리오와 시간적 추세 발견
- 안전 기준에 대한 대중 신뢰 회복 및 위험 완화 의사결정에 유용한 지침 제공

**저자**: Yuntao Cao; Ziyi Qu; Shujie Wu; Yuting Chen; Martin Skitmore; Xingguan Ma; Jun Wang
**출처**: Buildings, Vol.16, pp.10-10
**발행일**: 2025-12-19
**DOI**: https://doi.org/10.3390/buildings16010010

## 초록 (원문)

Hazards at construction sites can lead to severe accidents, posing significant risks to worker safety, financial stability, and public confidence in industry safety standards. As a result, understanding and preventing these accidents has become increasingly critical. Although previous studies have examined historical accidents through detailed reports, few have systematically applied automated natural language processing (NLP) techniques to uncover hidden topics and patterns in large datasets without manual intervention. This study addresses this gap by applying topic modeling to 22,623 accident reports from the Occupational Safety and Health Administration (OSHA) spanning 2004 to 2023. The results demonstrate that BERTopic substantially outperforms the traditional LDA model across multiple accident datasets, achieving higher topic coherence and topic diversity. Leveraging contextual embeddings, BERTopic identifies nuanced risk scenarios, occupation–accident patterns, and temporal trends that earlier text-mining approaches often overlooked. The findings also generate actionable managerial insights, including peak accident periods, vulnerable worker groups, and scenario-specific risk factors. Overall, this study provides a clearer and more data-driven understanding of construction accident mechanisms through advanced topic modeling. Applying BERTopic for topic extraction and content analysis introduces a novel and effective approach to analyzing construction accident reports. The insights derived provide valuable guidance for decision-makers in risk mitigation and accident prevention, while helping to rebuild public confidence in safety standards. Moreover, the approach’s reproducibility and potential for broader safety applications contribute to fostering a safer construction environment.

## 키워드

Topic model, SAFER, Accident (philosophy), Thematic analysis, Construction site safety, Accident analysis, Thematic structure, Risk assessment

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

