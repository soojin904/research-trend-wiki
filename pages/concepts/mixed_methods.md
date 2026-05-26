# 복합 방법론 (Mixed Methods in Text+Network Analysis)

텍스트 마이닝 방법론과 네트워크 분석을 결합하는 연구 패턴.
이 위키의 5개 소스 논문 전체에서 공통으로 나타나는 핵심 트렌드.

## 주요 결합 패턴

### 패턴 1: 의미연결망 + 토픽모델링
- **구성**: [[semantic_network_analysis\|의미연결망]] + [[topic_modeling\|LDA 토픽모델링]]
- **강점**: 개념 간 관계(네트워크)와 잠재 주제(토픽)를 동시에 파악
- **사례**: [[pages/papers/netminer/2021_kang_csr_ad_semantic_network\|강윤지 외 (2021)]], [[pages/papers/netminer/2022_morashti_sustainable_packaging\|Morashti 외 (2022)]]
- **도구**: [[netminer\|NetMiner]] 단독으로 수행 가능

### 패턴 2: 토픽모델링 + 신경망/ML
- **구성**: 텍스트 마이닝으로 변수 도출 → ML/신경망으로 예측 모델 구축
- **강점**: 비정형 데이터에서 정형 피처 추출 → 고급 예측 분석 연계
- **사례**: [[pages/papers/netminer/2024_jang_happiness_topic_nn\|Jang & Nemoto (2024)]] — 논문 토픽 → 설문 신경망
- **도구**: NetMiner(토픽) + SPSS MODELER(신경망)

### 패턴 3: 네트워크 분석 + 토픽모델링 (뉴스/소셜 데이터)
- **구성**: 이해관계자/담론 네트워크 + 주요 이슈 토픽
- **강점**: '누가 중요한가(네트워크)' + '무슨 이야기를 하는가(토픽)' 통합
- **사례**: [[pages/papers/netminer/2022_park_digital_healthcare_network\|Park 외 (2022)]]
- **도구**: NetMiner + R 병행

### 패턴 4: SNA 지표 → 통계 분석
- **구성**: SNA 중심성 지표를 독립변수로 → 회귀분석
- **강점**: 네트워크 구조 효과를 정량적으로 검증
- **사례**: [[pages/papers/netminer/2022_jeon_social_network_health_elderly\|Jeon & Park (2022)]]
- **도구**: NetMiner (SNA + 회귀 통합)

## NetMiner 제품 연관성
- 위 패턴 1~4 모두 NetMiner에서 수행 가능
- **핵심 세일즈 포인트**: 단일 소프트웨어로 복합 방법론 전체 파이프라인 지원
- 특히 패턴 1 (의미연결망 + 토픽)은 NetMiner의 경쟁 우위 영역

### 패턴 5: 정성 방법론 + 네트워크 동학 (Hybrid Mixed Methods)
- **구성**: 심층 인터뷰·민족지 등 정성 방법론 + 종단 네트워크 데이터
- **강점**: "왜 네트워크가 변하는가"(정성) + "어떻게 변하는가"(정량) 통합
- **사례**: [[pages/papers/2026_kreager_mixed_methods_lifecourse|Kreager 외 (2026)]] — 생애 과정 전환의 의사결정·네트워크 동학
- **특징**: 기존 패턴(텍스트+네트워크)과 달리 **행동·의사결정 과정**에 집중

## NetMiner 제품 연관성
- 위 패턴 1~4 모두 NetMiner에서 수행 가능
- **핵심 세일즈 포인트**: 단일 소프트웨어로 복합 방법론 전체 파이프라인 지원
- 특히 패턴 1 (의미연결망 + 토픽)은 NetMiner의 경쟁 우위 영역
- 패턴 5(정성+네트워크)는 NetMiner가 직접 지원하기 어렵지만, 네트워크 분석 파트 담당 가능

## 미해결 질문
- GNN과 전통 SNA의 결합 패턴은? → 별도 조사 필요
- LLM + 네트워크 분석 결합 패턴의 최신 사례는?
