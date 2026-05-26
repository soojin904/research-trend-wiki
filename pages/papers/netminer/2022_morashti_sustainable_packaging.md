---
title: "A Systematic Literature Review of Sustainable Packaging in Supply Chain Management"
authors: [Morashti Jonathan, An Youra, Jang Hyunmi]
year: 2022
venue: Sustainability, 14(9), 4921 (MDPI)
tags: [systematic-review, keyword-network, topic-modeling, sustainability, netminer, text-mining]
source: raw/A Systematic Literature Review of Sustainable Packaging in Supply Chain Management.pdf
---

# 지속가능 패키징 문헌 분석: 키워드 네트워크 + 토픽모델링

## 연구 질문
1993~2020년 공급망 관리 내 지속가능 패키징 연구의 트렌드와 공백은?

## 데이터
- 학술지 논문: 1993~2020년 출판 저널 논문
- 분석 방법: 정량(데이터마이닝) + 정성(심층 인터뷰) 혼합

## 방법론
| 분석 | 내용 |
|------|------|
| [[keyword_network_analysis\|키워드 네트워크 분석]] | 키워드 간 공출현 네트워크 |
| [[topic_modeling\|토픽모델링]] | 6개 토픽 도출 |
| 통계 분석 | 빈도, TF-IDF |
| 도구 | [[netminer\|NetMiner 4]] |

## 주요 결과
**TF 상위 키워드**: life cycle, environmental impact, consumer, transportation, production
**TF-IDF 상위 키워드**: production, transportation, consumer, food, environmental impact

**6개 토픽**:
1. Consumer behaviour
2. Environmental pollution
3. Circular economy
4. Waste management
5. Resource conservation
6. Operational management

- 2013년 이후 연구 급증 → circular economy 개념과 결합
- 공학·과학 분야 편중, operational management 분야 연구 부족

## NetMiner 연관성
- NetMiner 4로 3가지 분석(통계, 키워드 네트워크, 토픽) 통합 수행
- 외국 연구자가 NetMiner를 선택한 사례 → 글로벌 사용 근거

## 메모
- [[systematic_literature_review\|체계적 문헌 고찰(SLR)]]과 데이터마이닝의 결합 → 연구동향 파악에 효과적
- [[mixed_methods\|복합 방법론]]: 정량(키워드 네트워크 + 토픽) + 정성(인터뷰) 검증
