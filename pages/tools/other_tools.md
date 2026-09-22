---
title: "NetMiner 외 도구 (Other Tools)"
tags: [tools, r, python, spss, saom, gephi, ucinet]
---

# NetMiner 외 도구

이 위키 소스 논문에서 실제 사용되었거나, SNA·텍스트마이닝 맥락에서 자주 언급되는 도구 목록.
[[pages/tools/netminer|NetMiner]]와의 비교 포지셔닝 참고용.

---

## 이 위키 논문에서 실제 사용된 도구

### R
- **유형**: 통계 프로그래밍 언어
- **사용 사례**:
  - [[pages/papers/netminer/2022_park_digital_healthcare_network|Park 외 (2022)]] — 토픽모델링 (NetMiner와 병행)
  - [[pages/papers/sna/2026_mcmillan_network_rct_causal|McMillan 외 (2026)]] — SAOM 분석 (RSiena 패키지)
- **관련 패키지**: igraph (네트워크), topicmodels / stm (토픽), RSiena (SAOM)
- **특징**: 무료·오픈소스, 통계 연계 강점, 코딩 필요

### SPSS MODELER 18
- **유형**: 상용 데이터 마이닝·머신러닝 소프트웨어 (IBM)
- **사용 사례**:
  - [[pages/papers/netminer/2024_jang_happiness_topic_nn|Jang & Nemoto (2024)]] — 신경망 분석 (NetMiner에서 토픽 추출 후 연계)
- **특징**: GUI 기반 머신러닝 파이프라인, NetMiner와 역할 분담 가능

### RSiena (R 패키지) / SAOM
- **유형**: 종단 네트워크 분석 전용 R 패키지
- **풀네임**: Stochastic Actor-Oriented Model
- **사용 사례**:
  - [[pages/papers/sna/2026_mcmillan_network_rct_causal|McMillan 외 (2026)]] — RCT 참여자 네트워크 위치 변화 모델링
- **특징**: 네트워크 변화와 행동 변화를 동시에 모델링, R 기반
- **관련 개념**: [[pages/concepts/causal_inference_networks|인과 추론과 네트워크]]

---

## 응용 분야 논문에서 새로 확인된 도구 (2026 수집, 459편)

### BERTopic (Python 라이브러리)
- **유형**: 임베딩 기반 토픽 모델링 라이브러리
- **응용 편수**: 789편 중 ~145편(18%)이 토픽모델링 사용, 그중 다수가 BERTopic — LDA 대비 일관성 높다는 비교 실험이 거의 매 청크에서 반복 확인됨 (2026-09-22 전수 재합성)
- **강점**: 사전학습 언어모델(BERT) 기반 — LDA보다 의미론적으로 일관된 토픽
- **약점**: GPU 필요, 초매개변수 설정 복잡
- **NetMiner 관련**: ✅ **지원함** (Text > BERTopic/BERTrend) — 과거 "❌ 미지원"으로 잘못 기록되어 있었음(2026-09-22 정정). SNA 전문지(Social Networks 등)에서는 실사용 0건이지만 응용분야 논문에서는 매우 흔함 — 학술 수요는 확실히 있으나 지원 사실 자체가 덜 알려짐(마케팅 홍보 부족 문제이지 기능 공백 아님)
- **설치**: `pip install bertopic`

### Textom
- **유형**: 한국어 텍스트 마이닝 + 의미연결망 분석 웹 서비스
- **응용 편수**: ~2편
- **강점**: 한국어 형태소 분석 + 의미연결망 + 중심성 분석, 노코드 웹 UI
- **약점**: SNA 기능 제한적 (NetMiner 대비), 구독형 비용
- **NetMiner 관련**: **국내 직접 경쟁 도구** — 의미연결망 분석 영역에서 NetMiner의 잠재 대체재

### Sometrend (썸트렌드)
- **유형**: 한국 소셜미디어 분석 서비스
- **응용 편수**: 2건 이상 확인 (ESG 담론 분석 등)
- **강점**: 국내 SNS 데이터 수집·트렌드 분석 특화, **공출현 네트워크 + 중심성 분석 기능 보유** (2026-09-22 재확인 — 기존 "SNA 없음" 기록 정정)
- **약점**: NetMiner 대비 SNA 기능 깊이 제한적으로 추정(직접 비교 필요)
- **NetMiner 관련**: 국내 직접 경쟁 도구 — 텍스트+네트워크 결합 포지셔닝이 NetMiner와 유사

### TEXTOM
- **유형**: 한국어 텍스트 마이닝 + 데이터 시각화 상용 플랫폼
- **응용 편수**: 2건 이상 확인
- **강점**: 노코드 웹 UI, 국내 학계 사용 저변
- **NetMiner 관련**: 국내 직접 경쟁 도구 (Textom과 동일 계열 — 2026-09-22 재확인, 표기 통일)

### pyBiblioNet (Python 라이브러리)
- **유형**: OpenAlex 연동 서지 네트워크 분석 오픈소스 라이브러리
- **응용 편수**: 1편(2026-09-22 재합성에서 신규 발견)이나 기능이 매우 포괄적
- **강점**: 인용·공저·키워드공출현 네트워크 생성 + 중심성 + 커뮤니티탐지 + NLP를 하나의 Python 라이브러리로 통합
- **NetMiner 관련**: **NetMiner Biblio Extension과 직접 경쟁** — 무료·오픈소스라는 점에서 위협적. 기능 커버리지 상세 비교 필요

### Orange Data Mining
- **유형**: 오픈소스 GUI 기반 데이터 마이닝·ML 도구
- **강점**: 시각적 파이프라인, 텍스트 분석·클러스터링 기능
- **약점**: SNA 기능 약함 (네트워크 분석 미지원)
- **NetMiner 관련**: GUI 노코드 분석 도구로서 간접 경쟁

### Hugging Face (플랫폼)
- **유형**: 사전학습 모델 허브 및 배포 플랫폼
- **응용 편수**: ~20편 (transformers 라이브러리 사용)
- **강점**: BERT, GPT 계열 수천 개 모델 무료 이용, `transformers` 라이브러리
- **NetMiner 관련**: ❌ 연동 없음 — 코딩 기반 LLM/감성 분석 연구자들의 표준 플랫폼

---

## 비교 대상으로 자주 언급되는 도구

### Gephi
- **유형**: 오픈소스 네트워크 시각화·분석 소프트웨어
- **강점**: 대규모 네트워크 시각화, 무료, 커뮤니티 탐지 플러그인
- **약점**: 텍스트마이닝 기능 없음, 버전 안정성 이슈, 통계 분석 미지원
- **사용자층**: 시각화 중심 연구자, 디지털 인문학

### UCINET
- **유형**: Windows 기반 SNA 전용 소프트웨어
- **강점**: SNA 학술 표준, 오랜 역사·인용 레거시
- **약점**: GUI 구식, 텍스트·통계 분석 없음, 대용량 데이터 처리 한계
- **사용자층**: 사회학·조직연구 전통 SNA 연구자

### Python (NetworkX, graph-tool 등)
- **유형**: 프로그래밍 언어 + 네트워크 라이브러리
- **강점**: 유연성 최고, 무료, 머신러닝(scikit-learn, PyTorch) 직접 연계
- **약점**: 코딩 필수, GUI 없음, 진입 장벽 높음
- **관련 패키지**: NetworkX (범용), graph-tool (성능), cdlib (커뮤니티), gensim / BERTopic (토픽)

### VOSviewer
- **유형**: 서지계량·키워드 네트워크 시각화 전용 도구
- **응용 편수**: 4편 이상 (2026-09-22 재합성에서 반복 확인 — 가장 자주 언급되는 서지계량 도구)
- **강점**: 무료, SLR 키워드 네트워크에 특화, 직관적 UI
- **약점**: 네트워크 분석 기능 제한, SLR 이외 용도 제한적
- **사용자층**: SLR·서지계량 연구자 (NetMiner 잠재 대체재)

### CiteSpace / R bibliometrix(Biblioshiny) / ScientoPy
- **유형**: 서지계량·과학지도(science mapping) 전용 도구 3종
- **응용 편수**: 각 2~3편 — VOSviewer와 함께 조합 사용되는 경우 많음(예: CiteSpace+VOSviewer+bibliometrix 동시 사용)
- **NetMiner 관련**: Biblio Extension의 대체재 후보군. 서지계량 연구자들이 이미 익숙한 무료 도구 생태계가 형성돼 있어 NetMiner Biblio 홍보 시 "왜 이걸 써야 하는가"에 대한 명확한 차별점 제시 필요

### Voyant Tools / Quanteda(R 패키지)
- **유형**: 디지털 인문학·비프로그래머 대상 텍스트 분석 도구(Voyant, 웹 기반) / R 텍스트분석 패키지(Quanteda)
- **응용 편수**: Voyant 2편, Quanteda 1편(튜토리얼형 논문)
- **약점**: 둘 다 네트워크 분석 기능 없음 — 빈도·공기어(collocation) 중심
- **NetMiner 관련**: 직접 경쟁보다는 "텍스트분석 입문 도구"로 포지셔닝이 다름. 디지털 인문학 연구자 세그먼트 유입 경로로 참고 가치

---

## 포지셔닝 요약

| 도구 | SNA | 텍스트마이닝 | 통계 | GUI | 비용 |
|------|:---:|:----------:|:---:|:---:|:----:|
| **NetMiner** | ✅ | ✅ | ✅ | ✅ | 유료 |
| R (igraph+) | ✅ | ✅ | ✅ | ❌ | 무료 |
| Python | ✅ | ✅ | ✅ | ❌ | 무료 |
| SPSS MODELER | ❌ | △ | ✅ | ✅ | 유료 |
| Gephi | ✅ | ❌ | ❌ | ✅ | 무료 |
| UCINET | ✅ | ❌ | △ | ✅ | 유료 |
| VOSviewer | △ | △ | ❌ | ✅ | 무료 |
| RSiena | △ | ❌ | ✅ | ❌ | 무료 |
| BERTopic | ❌ | ✅ | ❌ | ❌ | 무료 |
| Textom / TEXTOM | △ | ✅ | △ | ✅ | 유료 |
| Sometrend | ❌ | ✅ | △ | ✅ | 유료 |
| pyBiblioNet | ✅ | △ | ❌ | ❌ | 무료 |
| Orange Data Mining | ❌ | △ | △ | ✅ | 무료 |

→ **NetMiner의 차별점**: SNA + 텍스트마이닝 + 통계를 GUI 환경에서 통합 지원하는 유일한 도구
→ **경쟁 위협**: Textom/TEXTOM·Sometrend(국내 의미연결망·SNS 분석), VOSviewer·pyBiblioNet(서지계량)가 NetMiner 일부 사용자층 흡수 중. 특히 pyBiblioNet은 무료 오픈소스로 Biblio Extension 대체 가능성이 있어 주시 필요 (2026-09-22 재합성에서 신규 확인)
