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
- **사례**: [[pages/papers/sna/2026_kreager_mixed_methods_lifecourse|Kreager 외 (2026)]] — 생애 과정 전환의 의사결정·네트워크 동학
- **특징**: 기존 패턴(텍스트+네트워크)과 달리 **행동·의사결정 과정**에 집중

### 패턴 6: 토픽모델링 + 감성분석 (응용 분야 표준 조합)
- **구성**: LDA 또는 BERTopic으로 주제 파악 → BERT/VADER 감성 분석으로 감정 레이어 추가
- **강점**: "무슨 주제에서"(토픽) + "어떤 감정으로"(감성) 동시 파악
- **응용 편수**: ~30편 (마케팅·커뮤니케이션·보건 분야)
- **도구**: Python (gensim + transformers) 또는 NetMiner (LDA) + 외부 감성 도구
- **사례 분야**: 소비자 리뷰 분석, 소셜미디어 담론, 의료 SNS 텍스트

### 패턴 7: 텍스트 분석 + SNA (서지계량·허위정보·정책 담론)
- **구성**: 텍스트 마이닝(토픽·감성) → 결과를 네트워크 구조로 연결
- **응용 편수**: ~20편
- **대표 맥락**: 서지계량(키워드 공출현+중심성), 허위정보 전파망, 정치 네트워크 담론 분석
- **도구**: NetMiner 핵심 강점 영역 — 텍스트 마이닝 + SNA 통합 가능

## NetMiner 제품 연관성
- 패턴 1–4, 6–7 모두 NetMiner에서 수행 가능
- **핵심 세일즈 포인트**: 단일 소프트웨어로 복합 방법론 전체 파이프라인 지원
- 특히 패턴 1 (의미연결망 + 토픽), 패턴 7 (텍스트+SNA)은 NetMiner의 경쟁 우위 영역
- 패턴 5(정성+네트워크)는 NetMiner가 직접 지원하기 어렵지만, 네트워크 분석 파트 담당 가능
- 패턴 6 (토픽+감성)은 LDA 부분은 지원, ABSA(측면 기반 감성분석) 기능 강화 필요

→ 응용 분야 복합 방법론 빈도 상세: [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026)]]

## 미해결 질문
- GNN과 전통 SNA의 결합 패턴은? → 응용 분야에서 GNN ~23편 확인; 주로 CS 방법론 논문
- LLM + 네트워크 분석 결합 패턴: 응용 분야에서 LLM ~186편 — 아직 LLM+SNA 직접 결합은 소수
