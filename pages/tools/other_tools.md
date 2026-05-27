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
- **응용 편수**: ~18편 (LDA 대비 빠르게 성장)
- **강점**: 사전학습 언어모델(BERT) 기반 — LDA보다 의미론적으로 일관된 토픽
- **약점**: GPU 필요, 초매개변수 설정 복잡
- **NetMiner 관련**: ❌ 미지원 — "BERTopic+LDA 비교" 논문 증가로 중기 도입 검토 필요
- **설치**: `pip install bertopic`

### Textom
- **유형**: 한국어 텍스트 마이닝 + 의미연결망 분석 웹 서비스
- **응용 편수**: ~2편
- **강점**: 한국어 형태소 분석 + 의미연결망 + 중심성 분석, 노코드 웹 UI
- **약점**: SNA 기능 제한적 (NetMiner 대비), 구독형 비용
- **NetMiner 관련**: **국내 직접 경쟁 도구** — 의미연결망 분석 영역에서 NetMiner의 잠재 대체재

### Sometrend
- **유형**: 한국 소셜미디어 분석 서비스
- **응용 편수**: ~1편
- **강점**: 국내 SNS 데이터 수집·트렌드 분석 특화
- **약점**: SNA·네트워크 분석 없음

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
- **강점**: 무료, SLR 키워드 네트워크에 특화, 직관적 UI
- **약점**: 네트워크 분석 기능 제한, SLR 이외 용도 제한적
- **사용자층**: SLR·서지계량 연구자 (NetMiner 잠재 대체재)

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
| Textom | △ | ✅ | △ | ✅ | 유료 |
| Orange Data Mining | ❌ | △ | △ | ✅ | 무료 |

→ **NetMiner의 차별점**: SNA + 텍스트마이닝 + 통계를 GUI 환경에서 통합 지원하는 유일한 도구
→ **경쟁 위협**: Textom(국내 의미연결망), VOSviewer(서지계량)가 NetMiner 일부 사용자층 흡수 중
