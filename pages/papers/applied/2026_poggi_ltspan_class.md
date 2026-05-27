---
title: "&lt;span class="
authors: ['Isabella Poggi', 'Tommaso Scaramella', 'Sissy Violini', 'Simona Careri', 'Maria Désirée Epure', 'Daniele Dragoni']
year: 2026
venue: "Preprints.org"
tags: ['Computational and Text Analysis Methods', 'Language, Metaphor, and Cognition', 'Artificial Intelligence Applications']
source: raw/applied/applied_2026_ltspan_classwordgtThe_lts_preprints202601_1391_v1.md
---

# &lt;span class=
**제목(한글)**: 대형 언어 모델을 활용한 다중 모드 정치 담론 분석 기법

**저자**: Isabella Poggi; Tommaso Scaramella; Sissy Violini; Simona Careri; Maria Désirée Epure; Daniele Dragoni
**출처**: Preprints.org, Vol.None
**발행일**: 2026-01-20
**DOI**: https://doi.org/10.20944/preprints202601.1391.v1

## 한국어 요약

**연구질문**: 백악관 정상회담과 같은 대규모 정치적 토론에서 언어적 메시지 외에 손짓, 억양, 시선 처리 등 신체적 의사소통 요소를 Gemini 2.5와 같은 LLM을 통해 정밀하게 감정/논리(LEP) 수준에서 자동 분석할 수 있는가?

**방법론**:
- 2025년 2월 28일 백악관에서 진행된 트럼프-젤렌스키 정상 회담의 다중 모드 비디오 데이터 활용
- 각 발언 문장과 제스처, 표정을 수동 어노테이션하여 Logos(논리), Ethos(신뢰), Pathos(감정) 지표로 분류
- 동일 클립에 대해 Gemini 2.5 모델에 세밀한 멀티모달 어노테이션 프롬프트를 적용하고 인간 전문가 코딩과의 불일치율 측정 및 프롬프트 튜닝 수행

**주요 결과**:
- 최적화된 프롬프트를 장착한 Gemini 2.5 모델이 발화와 신체 언어의 복합 정서 상태를 매우 고속으로 판독함을 실증함
- 일부 지표에서는 인간 어노테이터의 분석 정밀도를 능가하는 성능을 보여, 많은 시간이 소요되는 정치 다중 모드 담론 분석을 대규모로 자동화할 유효한 방법론적 프레임워크를 수립함


## 초록 (원문)

Today, foundation models simulate humans’ skills in translation, literature review, fact checking, fake-news detection, novel and poetry production. But Generative AI can also be applied to discourse analysis. This study instructs the Gemini 2.5 model to analyze multimodal political discourse. We selected some fragments from the Trump-Zelensky debate held at the White House on February 28, 2025, and annotated each sentence, gesture, intonation, gaze, and fa-cial expression in terms of LEP (Logos, Ethos, Pathos) analysis, to assess when speakers, in words or body communication, rely on rational argumentation, stress their own merits or the opponents’ demerits, or express and try to induce emotions in the audi-ence. Through detailed prompts, we asked the Gemini 2.5 model to run the LEP analysis on the same fragments. Then, considering the human’s and model’s annotations in par-allel, we proposed a metric to compare their respective analyses and measure dis-crepancies, finally tuning an optimized prompt for the model’s best performance, which in some cases outperformed the human’s analysis: an interesting application, since the LEP analysis highlights deep aspects of multimodal discourse but is highly time-consuming, while its automatic version allows us to interpret large chunks of speech in a fast but reliable way.

## 키워드

Metric (unit), Generative grammar, Expression (computer science), Stress (linguistics), Measure (data warehouse), Deep learning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

