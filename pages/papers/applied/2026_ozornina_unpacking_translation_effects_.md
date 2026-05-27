---
title: "Unpacking Translation Effects. Influences of Target Language Choice on Topic Modeling in Multilingual Environments"
authors: ['Nadezhda (Nadja) Ozornina', 'Mario Haim']
year: 2026
venue: "Medien & Kommunikationswissenschaft"
tags: ['Computational and Text Analysis Methods', 'Sentiment Analysis and Opinion Mining', 'Topic Modeling']
source: raw/applied/applied_2026_Unpacking_Translation_Eff_1615_634x_2026_1_71.md
---

# Unpacking Translation Effects. Influences of Target Language Choice on Topic Modeling in Multilingual Environments
**제목(한글)**: 번역 효과 규명: 다국어 환경에서 대상 언어 선택이 토픽 모델링에 미치는 영향

**저자**: Nadezhda (Nadja) Ozornina; Mario Haim
**출처**: Medien & Kommunikationswissenschaft, Vol.74, pp.71-87
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.5771/1615-634x-2026-1-71

## 한국어 요약

**연구질문**: 다국어 텍스트 말뭉치에 대한 토픽 모델링(Topic Modeling) 수행 시, 번역 언어의 선택(오리지널 언어로 직접 번역 vs 제3의 공통 영어로 중개 번역)이 최종 도출되는 토픽 분포와 단어 중요도에 어떤 통계적 왜곡을 미치는가?

**방법론**:
- UN의 러시아어-독어 병렬 텍스트 말뭉 3,760건 분석
- 러시아어를 독어로 직접 번역한 케이스와 두 언어 모두 영어(Intermediary Language)로 변환한 케이스 비교
- 어휘 중첩도(feature overlap), 토픽 분포(prevalence), 토픽 단어 의미 대조 기법 적용
- 434건의 다국어 뉴스 기사 말뭉치로 검증성 복제 수행

**주요 결과**:
- 공통 영어 중개 번역 시 다국어 토픽 분포가 대칭적이고 어휘 중첩도가 높은 장점이 있으나, 전체 유효 어휘 사전 크기(vocabulary size)가 유의미하게 억제되어 디테일한 주제가 누락되는 트레이드오프가 존재함을 폭로함
- 다국어 커뮤니케이션 연구에서 최적의 번역 언어 선정을 위한 정량적 가이드를 수립함


## 초록 (원문)

Machine translation is widely used in communication science to consolidate texts, not least for exploratory clustering approaches such as multilingual topic modeling. However, the impact of target language choice on topic modeling results remains unclear. This study examines these effects by (a) consolidating texts into one of the original document languages and (b) translating texts into an intermediary language not present in the dataset under study. To assess the effects, we use a corpus of parallel United Nations texts in Russian and German (N = 3,760). We compare the results of structural topic modeling after translating Russian texts into German, chosen as the original language, with consolidating the entire corpus into English as an intermediary language. The translation approaches are compared based on feature overlap, topical prevalence, and topical content. The findings show that intermediary-language translation yields a more symmetrical topic distribution and higher overlap in top words, but significantly reduces vocabulary size compared to consolidation into the original language. The results are replicated using a second bilingual journalistic corpus (N = 434) and validated across different numbers of topics. Finally, we discuss best practices for target language selection in multilingual topic modeling and situate them within the context of recent developments in computational communication science.

## 키워드

Vocabulary, German, Topic model, Selection (genetic algorithm), Machine translation, Context (archaeology), Language model, Cluster analysis

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

