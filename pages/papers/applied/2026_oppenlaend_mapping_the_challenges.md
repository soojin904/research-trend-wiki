---
title: "Mapping the Challenges of HCI: An Application and Evaluation of ChatGPT for Mining Insights at Scale"
authors: ['Jonas Oppenlaender', 'Joonas Hämäläinen']
year: 2026
venue: "International Journal of Human-Computer Interaction"
tags: ['Topic Modeling', 'Artificial Intelligence in Healthcare and Education', 'AI in Service Interactions']
source: raw/applied/applied_2026_Mapping_the_Challenges_of_10447318_2026_2647543.md
---

# Mapping the Challenges of HCI: An Application and Evaluation of ChatGPT for Mining Insights at Scale
**제목(한글)**: HCI 분야 연구 도전 과제 매핑: 대규모 통찰력 마이닝을 위한 ChatGPT 적용 및 평가

**저자**: Jonas Oppenlaender; Joonas Hämäläinen
**출처**: International Journal of Human-Computer Interaction, Vol.None, pp.1-32
**발행일**: 2026-04-06
**DOI**: https://doi.org/10.1080/10447318.2026.2647543

## 한국어 요약

**연구질문**: 방대한 양의 학술 논문 코퍼스에서 인공지능 모델(ChatGPT)을 활용해 연구의 한계와 미래 도전 과제를 높은 신뢰도와 설명성으로 일괄 추출하는 지능형 파이프라인은 어떻게 구성하는가?

**방법론**:
- ACM CHI 2023 콘퍼런스 프로시딩 879편의 논문 풀텍스트 대상 2단계 프롬프트 설계
  - 1단계: GPT-3.5를 활용해 후보 도전 과제 추출
  - 2단계: GPT-4를 활용해 가장 타당한 요약 과제 결정
- 인간 평가자의 수동 정합성 평가 및 카파(Kappa) 일치도 검증 수행
- 총 4,392개 추출 과제에 대한 토픽 모델링 및 인터랙티브 시각화 플랫폼 구축

**주요 결과**:
- 추출된 연구 과제가 실제 인간 전문가 검수와 비교해 매우 일치도가 높음(Kappa = 0.97)을 검증함
- 전체 코퍼스 처리 비용이 단 50달러로, 대용량 정성적 텍스트 분석에 있어 LLM 파이프라인의 극대화된 비용 효율성과 실용적 타당성을 규명함


## 초록 (원문)

Large language models (LLMs) are increasingly used for analytical tasks, yet their effectiveness in real-world applications remains underexamined, partly due to the opacity of proprietary models. We evaluate ChatGPT (GPT-3.5 and GPT-4) on the practical task of extracting research challenges from a large scholarly corpus in Human-Computer Interaction (HCI). Using a two-step approach, we first apply GPT-3.5 to extract candidate challenges from the 879 papers in the 2023 ACM CHI Conference proceedings, then use GPT-4 to select the most relevant challenges per paper. This process yielded 4,392 research challenges across 113 topics, which we organized through topic modeling and present in an interactive visualization. We compare the identified challenges with previously established HCI grand challenges and the United Nations Sustainable Development Goals, finding both strong alignment in areas such as ethics and accessibility, and gaps in areas such as human-AI collaboration. A task-specific evaluation with human raters confirmed near-perfect agreement that the extracted statements represent plausible research challenges (\k{appa} = 0.97). The two-step approach proved cost-effective at approximately US$50 for the full corpus, suggesting that LLMs offer a practical means for qualitative text analysis at scale, particularly for prototyping research ideas and examining corpora from multiple analytical perspectives.

## 키워드

Task (project management), Scale (ratio), Key (lock), Computer science, Data science, Field (mathematics), Engineering, Geography

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

