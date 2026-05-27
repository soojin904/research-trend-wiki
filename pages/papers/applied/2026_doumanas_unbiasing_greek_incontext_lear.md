---
title: "Unbiasing Greek: In-Context Learning Strategies for Gender Bias Identification and Mitigation for Legal Documents and Job Ads"
authors: ['Dimitrios Doumanas', 'Andreas Soularidis', 'Nikolaos Zafeiropoulos', 'Stamatis Chatzistamatis', 'George E. Tsekouras', 'Andreas El Saer', 'Chrisaphis Nathanailidis', 'Konstantinos Kotis']
year: 2026
venue: "Information"
tags: ['Authorship Attribution and Profiling', 'Topic Modeling', 'Gender Studies in Language']
source: raw/applied/applied_2026_Unbiasing_Greek_InContext_info17040342.md
---

# Unbiasing Greek: In-Context Learning Strategies for Gender Bias Identification and Mitigation for Legal Documents and Job Ads
**제목(한글)**: 그리스어의 편향 완화: 법률 문서 및 구인 광고 내 젠더 편향 식별 및 완화를 위한 문맥 내 학습 전략

**저자**: Dimitrios Doumanas; Andreas Soularidis; Nikolaos Zafeiropoulos; Stamatis Chatzistamatis; George E. Tsekouras; Andreas El Saer; Chrisaphis Nathanailidis; Konstantinos Kotis
**출처**: Information, Vol.17, pp.342-342
**발행일**: 2026-04-02
**DOI**: https://doi.org/10.3390/info17040342

## 한국어 요약

**연구질문**: 성별 굴절 어미(명사, 형용사, 대명사 등)가 모든 형태소에 내재하여 영어식 방법론 적용이 곤란한 그리스어 법률 및 구인 문서에서, 젠더 편향을 실시간 탐지·교정하기 위한 문맥 내 학습(ICL) 모델 간 비교 성능과 최적 전략은 무엇인가?

**방법론**:
- 그리스어 문법 규칙에 근거한 9가지 성별 편향 규칙 분류(Taxonomy) 정의
- 전문가들이 직접 감수한 90건의 분야별 예시 데이터셋 구축
- XML 형식의 프롬프트 엔지니어링을 이용해 상용 LLM(Claude 4.5, GPT-5.2), 오픈 SLM(Mistral 24B, Ministral 14B), 그리스어 전용 특화 모델(Llama Krikri 8B)의 ICL 성능 비교
- 특히 법적 인명의 섣부른 어미 변경을 막기 위해 성별 일치 메타 규칙(meta-rule)을 도입하여 검증 적용

**주요 결과**:
- 상용 대형 LLM은 그리스어 문법 구조 내의 맥락적 편향 요소를 영리하게 포착해 수정한 반면, 일반 소형 SLM 모델들은 무리한 강제 변환(over-correction)이나 문법적 비문 파괴 등의 조악한 성향을 보임
- 희소 언어 환경에서의 편향 완화 시 언어 특화 어드밴티지 및 엄밀하게 구성된 인컨텍스트 레이아웃의 중요성을 규명함


## 초록 (원문)

Gender bias embedded in legal and professional texts perpetuates systemic inequality, yet research on bias identification and mitigation remains largely confined to English. Morphologically rich languages such as Greek, where grammatical gender pervades nouns, adjectives, pronouns, and participles, present unique challenges that existing approaches fail to address. This paper elaborates on a systematic methodology primarily focusing on identifying and mitigating gender bias in Greek-language job advertisements and legal documents. To accomplish that task, we define a taxonomy of nine gender bias rules tailored to the linguistic properties of Greek and construct domain-specific annotated datasets comprising 90 expert-curated few-shot examples across both textual domains. Using these resources, we employ XML-structured prompt engineering with in-context learning (ICL)and systematically compare three classes of models: (i) commercial large language models (LLMs), namely Claude Sonnet 4.5 and GPT-5.2, (ii) two open-weight small language models (SLMs), Mistral Small (24B) and Ministral (14B), and (iii) Llama Krikri (8B), a Greek-native language model built on Llama 3.1 and fine-tuned on high-quality Greek corpora. For each input text, the system identifies biased expressions, maps them to specific bias rules, provides explanations, and generates a fully corrected inclusive version. Our experiments reveal substantial performance disparities across model scales and linguistic specialization, with LLMs demonstrating superior contextual reasoning and SLMs exhibiting systematic over-correction and grammatical errors in Greek morphology. We further introduce a critical meta-rule addressing gender agreement with named entities to prevent spurious corrections in legal texts referencing identified individuals. The findings highlight the importance of model scale, language-specific adaptation, and carefully designed prompting strategies for bias mitigation in underrepresented languages.

## 키워드

Gender bias, Identification (biology), Spurious relationship, Construct (python library), Taxonomy (biology), Confirmation bias, Grammatical gender

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

