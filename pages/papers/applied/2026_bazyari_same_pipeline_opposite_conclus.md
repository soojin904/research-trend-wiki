---
title: "Same Pipeline, Opposite Conclusions: Sample-Surface Effects in Breaking-News Latency"
authors: ['Farhad Bazyari', 'Xianghang Liu', 'Sean Moran']
year: 2026
venue: "ArXiv.org"
tags: ['Media Influence and Politics', 'Computational and Text Analysis Methods', 'Digital Marketing and Social Media']
source: raw/applied/applied_2026_Same_Pipeline_Opposite_Co_nodoi.md
---

# Same Pipeline, Opposite Conclusions: Sample-Surface Effects in Breaking-News Latency

**제목(한글)**: 동일한 파이프라인, 상반된 결론: 속보 지연에서 샘플 표면 효과

## 한국어 요약

**연구질문**: 플랫폼 환경이 변화하고 플랫폼 데이터가 상업적 소셜 리스닝 제공업체를 통해 거의 독점적으로 흐르는 상황에서, 속보 지연에서 샘플 표면 효과가 어떻게 나타나는지 재검토한다.

**방법론**:
- 동일한 다운스트림 파이프라인을 통해 실행되는 두 가지 샘플링 설계를 사용하여 질문을 재검토한다.
- 샘플 A는 문서 페이지뷰 순위가 매겨진 위키백과 최신 이벤트 포털(WCEP)에서 N=50개의 이벤트를 추출한다.
- 샘플 B는 USD 거래량 순위가 매겨진 Polymarket 예측 시장에서 N=109개의 이벤트를 추출하며, 각 이벤트의 뉴스 순간은 가장 큰 1시간 거래량 급증에 고정된다.
- 두 샘플 모두 9개의 인덱싱된 채널에서 단일 상업 제공업체로부터 가져온다.

**주요 결과**:
- (1) X(트위터) 대 뉴스 방향은 샘플에 따라 달라진다. 샘플 A에서는 뉴스가 X보다 중앙값 21.6분 빠르지만, 샘플 B에서는 동일한 비교에서 -0.02분으로 동률을 이룬다(X가 38%에서 가장 빠름).
- (2) 채널 생태계가 다양화되었다. Bluesky, Facebook 공공, YouTube가 함께 가장 빠른 채널 우승의 24-32%를 차지하며, 2014년의 "X 대 뉴스통신사" 프레이밍은 더 이상 적합하지 않다.
- (3) 보도 공백은 구조적이다. 미국 관련 필터링과 페이지뷰 우선순위를 적용하더라도 제공업체의 색인은 무작위로 샘플링된 WCEP 이벤트의 24%에 대해 주제 관련 증거를 반환하지 않는다.
- 샘플 의존성을 노출하는 교차 표면 설계가 이 논문의 기여이다.

**저자**: Farhad Bazyari; Xianghang Liu; Sean Moran
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-05-18
**DOI**: 

## 초록 (원문)

Osborne and Dredze (2014) reported that Twitter was the timeliest social-media source of breaking news, trailing only newswire. Twelve years on, the platform landscape has shifted - Google+ is gone, X replaced Twitter, Bluesky and Threads have appeared - and platform data now flows almost exclusively through commercial social-listening providers that redact key fields. We revisit the question with two sampling designs run through the same downstream pipeline. Sample A draws N = 50 events from the Wikipedia Current Events Portal (WCEP) ranked by article pageviews. Sample B draws N = 109 events from Polymarket prediction markets ranked by USD trading volume, with each event's news moment pinned to the largest 1-hour trade-volume spike. Both samples are pulled from one commercial provider across nine indexed channels. We report three findings. (1) The X-vs-news direction depends on the sample. News leads X by a median of 21.6 min on Sample A (n = 6 paired); the same comparison is tied at -0.02 min on Sample B (n = 16 paired, X earliest in 38%). (2) The channel ecosystem has diversified. Bluesky, Facebook public, and YouTube together account for 24-32% of earliest channel wins; the 2014 "X versus newswire" framing no longer fits. (3) Coverage gaps are structural. Even with U.S.-relevance filtering and a pageview prior, the provider's index returns no on-topic evidence on 24% of randomly-sampled WCEP events. The paper's contribution is the cross-surface design that exposes the sample dependency in (1).

## 키워드

Sample (material), Framing (construction), Channel (broadcasting), The Internet, Key (lock), Sampling (signal processing), Large sample

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

