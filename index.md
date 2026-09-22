# 위키 인덱스

> LLM이 쿼리 시 가장 먼저 읽는 카탈로그. 새 페이지 생성 시 즉시 업데이트.

---

## Overview

- [[overview|분야 전체 합성]] — NetMiner 사용 사례 + 학계 트렌드 분리 정리

> **분석 시 주의사항** (검증된 오류 패턴 — 자세한 내용: [[SCHEMA.md]])
> 1. OpenAlex `tags`는 AI 자동 태그 — 오태깅 빈번. 방법론 빈도 집계 시 초록·본문으로 재확인 필수
> 2. "NetMiner 지원 ✅" ≠ "학술 수요 높음" — 항상 분리해서 서술 (BERTopic·GNN이 대표 사례)
> 3. 논문 주제 → NetMiner 기능 연결 시 실제 워크플로우 성립 여부를 구체적으로 확인 (데이터수집 논문 → Extension 연결은 오류였음)
> 4. "Reprint of: ..." 논문은 빈도 집계에서 원본과 동일 취급 (중복 제거)

---

## Papers

### A. NetMiner 사용 논문 (PDF/KCI/OpenAlex 수집)

> 실제 NetMiner를 사용한 연구. 제품 마케팅·사례 연구 자료로 활용.
> 2026-07-31: `raw/netminer/` 신규 수집분(KCI·OpenAlex 메타데이터 기반) 65건 검토 → NetMiner 언급 없는 12건 제외, KCI/OpenAlex 중복 수집 7건 병합, 근거 불충분 2건(초록 손상, 주제 무관) 제외 → 38편 신규 등재.

- [[pages/papers/netminer/2024_jang_happiness_topic_nn|Jang & Nemoto (2024)]] — 행복 영향 요인: LDA + 신경망, **NetMiner 4.5** (#topic-modeling #neural-network #mixed-methods)
- [[pages/papers/netminer/2022_morashti_sustainable_packaging|Morashti 외 (2022)]] — 지속가능 패키징 SLR: 키워드 네트워크 + LDA, **NetMiner 4** (#systematic-review #keyword-network #sustainability)
- [[pages/papers/netminer/2022_park_digital_healthcare_network|Park 외 (2022)]] — 디지털 헬스케어 생태계 네트워크 분석, **NetMiner** + R (#network-analysis #digital-healthcare)
- [[pages/papers/netminer/2022_jeon_social_network_health_elderly|Jeon & Park (2022)]] — 노인 우정 네트워크와 건강: SNA + 회귀, **NetMiner 4.0** (#sna #centrality #health)
- [[pages/papers/netminer/2021_kang_csr_ad_semantic_network|강윤지 외 (2021)]] — 광고홍보학 CSR 연구동향: 의미연결망 + LDA, **NetMiner 4** (#semantic-network #topic-modeling #csr)
- [[pages/papers/netminer/2025_huang_chinese_martial_arts_keyword_network|Huang 외 (2025)]] — 중국 무술 연구동향(WoS): 키워드 네트워크 + 중심성 (#keyword-network #centrality #sports)
- [[pages/papers/netminer/2025_hyun_elderly_dementia_care_network|Hyun 외 (2025)]] — 노인·치매 돌봄서비스 공급자원 SNA (#sna #centrality #elderly-care)
- [[pages/papers/netminer/2025_kim_taekwondo_student_athlete_experience|Kim (2025)]] — 태권도 특기자 학생운동선수 경험: 텍스트 네트워크 분석 (#text-network-analysis #taekwondo)
- [[pages/papers/netminer/2025_yun_nurse_burnout_topic_modeling|Yun (2025)]] — 간호사 소진 연구동향(2015-2024): LDA 토픽모델링 (#topic-modeling #lda #nursing)
- [[pages/papers/netminer/2026_yang_korea_china_relations_topic_modeling|Yang & Zhou (2026)]] — 한중관계 뉴스 빅데이터 토픽모델링(2022-2025) (#topic-modeling #lda #news-discourse)
- [[pages/papers/netminer/2026_sui_athlete_mental_health_keyword_network|Sui 외 (2026)]] — 운동선수 정신건강 연구동향(WoS): 키워드 네트워크 (#keyword-network #centrality #mental-health)
- [[pages/papers/netminer/2026_yeom_adult_ballet_youtube_topic_modeling|염지현 & Lee (2026)]] — 성인발레 유튜브 콘텐츠 동향: LDA 토픽모델링 (#topic-modeling #lda #youtube)
- [[pages/papers/netminer/2026_cho_esports_school_pe_perception|Cho 외 (2026)]] — e스포츠 학교체육 운영 주체 인식: 의미연결망 + TF-IDF (#semantic-network-analysis #esports #education)
- [[pages/papers/netminer/2026_yu_nursing_student_employment_stress|Yu & Park (2026)]] — 간호대학생 취업준비 스트레스: 텍스트 네트워크 분석 (#text-network-analysis #topic-modeling #nursing)
- [[pages/papers/netminer/2026_jung_exhibition_industry_governance_network|정혜인 & Kim (2026)]] — 국가재난시 전시산업 협력적 거버넌스 SNA (#sna #network-analysis #governance)
- [[pages/papers/netminer/2026_park_nonpharmacological_intervention_keyword_network|Park & Yoo (2026)]] — 비약물 중재 연구(MCI·치매) 핵심어 네트워크 (#keyword-network #centrality #dementia)
- [[pages/papers/netminer/2026_lee_stroke_gait_text_mining|Lee 외 (2026)]] — 뇌졸중 환자 보행 분석 연구동향: 텍스트마이닝 체계적 고찰 (#text-mining #topic-modeling #stroke)
- [[pages/papers/netminer/2026_shin_taekwondo_ranking_perception|Shin 외 (2026)]] — 대학 태권도 선수 랭킹제도 인식: 키워드 네트워크 (#semantic-network-analysis #centrality #taekwondo)
- [[pages/papers/netminer/2026_lee_health_information_manager_semantic_network|Lee & Park (2026)]] — 보건의료정보관리사 실습 역량 인식: 의미연결망 (#semantic-network-analysis #centrality #education)
- [[pages/papers/netminer/2026_jo_new_nurse_adaptation_topic_modeling|Jo 외 (2026)]] — 신규간호사 임상적응 인터뷰: 텍스트 네트워크 + 토픽모델링 (#text-network-analysis #topic-modeling #nursing)
- [[pages/papers/netminer/2026_kim_undeclared_major_career_topic_modeling|Kim 외 (2026)]] — 자유전공 대학생 진로 인식·경험 탐색: 텍스트 분석 (#text-analysis #topic-modeling #career-education)
- [[pages/papers/netminer/2026_yun_life_sustaining_treatment_discourse_topic_modeling|Yun & Kwak (2026)]] — 존엄사→연명의료결정 언론 담론 10년 변화: 토픽모델링 (#topic-modeling #lda #news-discourse)
- [[pages/papers/netminer/2026_kang_parkinsons_symptom_gene_network|Kang 외 (2026)]] — 파킨슨병 증상-유전자 네트워크 분석(한의학) (#network-analysis #centrality #bioinformatics)
- [[pages/papers/netminer/2026_kwak_elementary_science_concept_network|Kwak 외 (2026)]] — 초등 식물단원 교사·학생 개념 네트워크: 언어 네트워크 분석 (#language-network-analysis #eigenvector-centrality #science-education)
- [[pages/papers/netminer/2026_lee_kobe6_basketball_shoes_semantic_network|이형주 (2026)]] — 코비6 농구화 소비자 인식: 텍스트마이닝 + 의미연결망 + CONCOR (#semantic-network-analysis #concor #consumer-perception)
- [[pages/papers/netminer/2026_kwon_rejection_sensitivity_topic_modeling|권현정·LEE (2026)]] — 거부민감성 연구동향(2015-2025): 키워드 네트워크 + 토픽모델링, **NetMiner 4.5** (#keyword-network #topic-modeling #centrality)
- [[pages/papers/netminer/2026_jeong_midlife_depression_keyword_network|Jeong (2026)]] — 중년기 우울 연구동향: 키워드 네트워크 + 토픽모델링, **NetMiner 4.5.1** (#keyword-network #topic-modeling)
- [[pages/papers/netminer/2026_yun_elderly_single_households_topic_modeling|Yun & Jeong (2026)]] — 노인 1인가구 연구동향: 키워드 네트워크 + 토픽모델링, **NetMiner 4** (#keyword-network #topic-modeling #aging)
- [[pages/papers/netminer/2026_jeong_young_single_households_topic_modeling|Jeong (2026)]] — 청년 1인가구 연구동향: 키워드 네트워크 + 토픽모델링(BDC 활용), **NetMiner 4.5.1** (#keyword-network #topic-modeling #biblio-data-collector)
- [[pages/papers/netminer/2026_shin_adolescent_depression_keyword_network|Shin & Jeong (2026)]] — 청소년 우울 연구동향: 키워드 네트워크 + 토픽모델링, **NetMiner 4** (#keyword-network #topic-modeling #mental-health)
- [[pages/papers/netminer/2026_lee_art_therapist_knowledge_structure|Lee & Shon (2026)]] — 국내 미술치료사 연구 지식구조: 키워드 네트워크 + 응집성 분석, **NetMiner** (#keyword-network #centrality #community-detection)
- [[pages/papers/netminer/2026_kim_digital_literacy_vulnerable_groups|Kim & Kim (2026)]] — 정보취약계층 디지털 리터러시 연구동향: 키워드 네트워크, **NetMiner 4.3.2** (#keyword-network #centrality #digital-literacy)
- [[pages/papers/netminer/2026_an_early_childhood_teacher_keyword_network|An & Nam (2026)]] — 영유아교사 연구동향(놀이중심 교육과정 이후): 키워드 네트워크, **NetMiner 4.0** (#keyword-network #centrality #early-childhood-education)
- [[pages/papers/netminer/2026_lee_neurofeedback_keyword_network|Lee & Jo (2026)]] — 뉴로피드백 연구동향: 키워드 네트워크 + 구조적 공백 분석, **NetMiner 4x64** (#keyword-network #centrality #neurofeedback)
- [[pages/papers/netminer/2026_ahn_childcare_research_lda_topic_modeling|Ahn 외 (2026)]] — 『육아지원연구』 연구동향(2005-2025): 키워드 빈도 + LDA 토픽모델링, **NetMiner 4.5** (#lda #topic-modeling #childcare)
- [[pages/papers/netminer/2026_kim_taekwondowon_user_experience_textmining|Kim 외 (2026)]] — 태권도원 방문객 리뷰 텍스트마이닝: TF-IDF + LDA + 중심성, **NetMiner 4.0** (#text-mining #lda #centrality #tourism)
- [[pages/papers/netminer/2026_kim_children_oral_health_text_network|Kim (2026)]] — 아동 구강건강 연구동향: 텍스트 네트워크 분석 + 클러스터링, **NetMiner 4** (#text-network-analysis #centrality #community-detection)
- [[pages/papers/netminer/2026_lee_teaching_practicum_text_mining|Lee & Son (2026)]] — 예비교사 교육실습 경험 텍스트마이닝: 키워드 네트워크 + PFNet + 토픽모델링, **NetMiner 4.5** (#text-mining #topic-modeling #centrality)
- [[pages/papers/netminer/2026_son_group_counseling_topic_modeling|Son & Cheon (2026)]] — 집단상담 연구동향(2000-2022): 토픽모델링 + 중심성, **NetMiner 4.5** (#topic-modeling #centrality #group-counseling)
- [[pages/papers/netminer/2026_je_school_sports_club_media_textmining|Je & Kim (2026)]] — 학교스포츠클럽 언론보도 변화(2007-2023): TF-IDF + 의미연결망, **NetMiner 4.5** (#text-mining #semantic-network-analysis #centrality)
- [[pages/papers/netminer/2026_park_moral_resilience_topic_modeling|Park 외 (2026)]] — 도덕적 회복탄력성 연구동향: 텍스트 네트워크 분석 + 토픽모델링 (#text-network-analysis #topic-modeling #nursing)
- [[pages/papers/netminer/2026_oh_prefrontal_function_keyword_network|Oh 외 (2026)]] — 전두엽 기능 평가·중재 연구 주제구조: 키워드 네트워크 (#keyword-network #centrality #prefrontal-function)
- [[pages/papers/netminer/2026_kim_elder_abuse_news_topic_modeling|Kim (2026)]] — 노인학대 뉴스보도 분석: 의미연결망 + LDA 토픽모델링, NetMiner 명시 불확실 (#topic-modeling #semantic-network-analysis #news-media)

---

### B. 학계 트렌드 파악용 논문 (OpenAlex 수집, Social Networks 학술지)

> NetMiner 사용 여부와 무관한 SNA 학계 동향 파악 목적. 제품 기획·방향 설정 참고용.

**트렌드 분석 요약**: [[pages/insights/sna_method_frequency|SNA 방법론 빈도 (2021–2026)]] · [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]]

#### 2026년 주요 논문 (개별 페이지)
- [[pages/papers/sna/2026_omalley_spillover_rct|O'Malley 외 (2026)]] — Stepped-wedge RCT 의사 네트워크 spillover 인과 추론 (#causal-inference #spillover)
- [[pages/papers/sna/2026_haapanen_coalition_sna_design|Haapanen 외 (2026)]] — 다중 조직 연합의 다층 구조와 SNA 설계 (#coalition #multilevel)
- [[pages/papers/sna/2026_mcmillan_network_rct_causal|McMillan 외 (2026)]] — 네트워크 위치 차이가 RCT 인과 추론에 미치는 위협 (#causal-inference #saom)
- [[pages/papers/sna/2026_zhang_egocentric_csa|Zhang & Wang (2026)]] — 에고중심 네트워크와 CSA 소비자 반응 (#egocentric #csa)
- [[pages/papers/sna/2026_almquist_homelessness_personal_network|Almquist 외 (2026)]] — 노숙 경험자 퍼스널 네트워크 (3,000명+, 종단) (#personal-network)
- [[pages/papers/sna/2026_schafer_personal_network_loneliness|Schafer 외 (2026)]] — 동반 관계와 외로움: 퍼스널 네트워크 재평가 (#personal-network #loneliness)
- [[pages/papers/sna/2026_gebhard_intervention_dementia|Gebhard & Ellinger (2026)]] — 치매 환자 개입과 네트워크 변화 (#intervention #dementia)
- [[pages/papers/sna/2026_nishi_wellbeing_experimental_network|Nishi 외 (2026)]] — 동료 웰빙 가시화와 협력 네트워크 (#experimental-network #wellbeing)
- [[pages/papers/sna/2026_lubbers_nsm_ard|Lubbers 외 (2026)]] — Network Scale-Up Method & ARD 발전 리뷰 (#nsum #ard)
- [[pages/papers/sna/2026_fluer_multiplex_survey|Fluer 외 (2026)]] — 설문 → 멀티플렉스 모델 (#multiplex #interlayer)
- [[pages/papers/sna/2026_an_peer_influence_multilayer|An 외 (2026)]] — 다층 네트워크에서 동료 영향 추정 (#multilayer #peer-influence)
- [[pages/papers/sna/2026_kreager_mixed_methods_lifecourse|Kreager 외 (2026)]] — 생애 과정 전환의 혼합 방법론 설계 (#mixed-methods #network-dynamics)
- [[pages/papers/sna/2026_qiao_ecommerce_rural_china|Qiao & Qiu (2026)]] — 농촌 중국 e-커머스 창업의 소셜 영향 (#social-influence)
- [[pages/papers/sna/2026_fancello_sociability_space|Fancello 외 (2026)]] — 소셜 네트워크를 지리 공간에 배치 (#spatial-network)

#### 2020–2026년 고관련도 논문 (개별 페이지 318편)
`pages/papers/sna/` 폴더 직접 탐색 또는 `/wiki:query`로 검색

#### 연도별 카탈로그 (관련도 하위 논문 목록)
- [[pages/papers/sna/catalog_2020|2020년 카탈로그]] — 90편
- [[pages/papers/sna/catalog_2021|2021년 카탈로그]] — 83편
- [[pages/papers/sna/catalog_2022|2022년 카탈로그]] — 94편
- [[pages/papers/sna/catalog_2023|2023년 카탈로그]] — 49편
- [[pages/papers/sna/catalog_2024|2024년 카탈로그]] — 33편
- [[pages/papers/sna/catalog_2025|2025년 카탈로그]] — 49편
- [[pages/papers/sna/catalog_2026|2026년 카탈로그 (추가분)]] — 21편

---

### C. 응용 분야 논문 (키워드 수집, `raw/applied/`)

> **수집 범위**: SNA 전문 학술지(Social Networks·Network Science·Connections) 외 전 저널·분야.
> **수집 방식**: `fetch_applied.py` — "social network" 또는 "text analysis" 키워드로 OpenAlex 검색, 인용 수 상위 500건/쿼리.
> **성격**: NetMiner 사용 여부와 무관. SNA·텍스트마이닝이 마케팅·보건학·경영학·커뮤니케이션 등 응용 분야에서 어떻게 쓰이는지 파악하고 신규 고객 세그먼트를 발굴하는 목적.
> **인제스트**: `batch_ingest.py` → 관련도 점수 기반 분류 (개별 페이지: `pages/papers/applied/`, 카탈로그: `pages/papers/applied/catalog_YYYY.md`).

**현황**: 개별 페이지 789편 (`pages/papers/applied/`) · 카탈로그 2편 — 2025년 24편, 2026년 34편 (`pages/papers/applied/catalog_2025.md`, `catalog_2026.md`)

`pages/papers/applied/` 폴더 직접 탐색 또는 `/wiki:query`로 검색

---

## Concepts (연구 설계 패턴)

> 연구를 어떻게 설계·구성하는가에 관한 프레임워크와 패턴

- [[pages/concepts/social_network_analysis|Social Network Analysis (SNA)]] — SNA 개요, 핵심 분석 유형, 도구 비교
- [[pages/concepts/personal_network|퍼스널·에고중심 네트워크]] — 개념, 측정, 적용 사례
- [[pages/concepts/egocentric_network_design|에고네트워크 설계·수집 방법론]] — 이름생성기·수집도구(GENSI/Network Canvas/Trellis)·회상편향·구조유형 자동분류, SNA 318편 중 단일 최대 클러스터(~46편, 2026-09-22 신규)
- [[pages/concepts/causal_inference_networks|인과 추론과 네트워크]] — spillover·SAOM·RCT 위협 요인
- [[pages/concepts/multilayer_network|다층·멀티플렉스 네트워크]] — 복수 레이어 구조, 분석 방법
- [[pages/concepts/mixed_methods|복합 방법론 (Mixed Methods)]] — 텍스트+네트워크 결합 패턴, NetMiner 연관성
- [[pages/concepts/systematic_literature_review|체계적 문헌 고찰 (SLR)]] — 데이터마이닝 기반 SLR 워크플로우

---

## Methods (구체적 분석 기법)

> **용도**: [[pages/tools/netminer]] 기능 목록을 기준선으로, 두 가지 제품 기획 질문에 답하기 위한 자료.
> 1. **신규 기능 후보** — NetMiner에 없는 방법론 (❌ 표시)
> 2. **기존 기능 개선 근거** — NetMiner에 있지만 학술 트렌드와 격차가 있는 방법론 (⚠️ 표시)
>
> NetMiner 현재 기능 요약: LDA·BERTopic ✅ / GCN·GAT·GraphSAGE ✅ / 감성분석(Lab, 7개 언어) ✅ / 지식그래프(Lab) ✅ / SHAP·Classical ML ✅ / ERGM ✅ | SAOM·LLM·RAG·텍스트분류(Transformer) ❌

### 기존 (유형 A → B 보강)
- [[pages/methods/centrality|Centrality (중심성)]] — degree/closeness/betweenness 등 중심성 지표 (24편, 4위) ✅
- [[pages/methods/topic_modeling|Topic Modeling (토픽모델링)]] — LDA·키워드 보조 토픽 모델, 네트워크 연계 패턴 (20편, 6위) ✅
- [[pages/methods/semantic_network_analysis|Semantic Network Analysis (의미연결망)]] — 키워드 공출현 네트워크, 시계열 담론 분석 ✅

### 신규 (유형 B 기반, 2026-09-22 318편 전수 재합성)
- [[pages/methods/ergm|ERGM (지수 랜덤 그래프 모형)]] — DERGM·다층·Bayesian·이분 변형 포함 (~40편, 2위) ✅ 기본 / ⚠️ 변형
- [[pages/methods/saom|SAOM / RSiena (확률적 행위자 지향 모형)]] — 종단 공진화 모형, NetMiner 이탈 요인 (~29편, 3위) ❌
- [[pages/methods/relational_event_model|관계적 사건 모형 (REM/RHEM/DyNAM)]] — 이벤트 단위 동적 네트워크, 2026-09-22 신규 발견 클러스터 (~17편) ❌
- [[pages/methods/centrality|Centrality (중심성)]] — 기본 7종 + 신규 변형(temporal betweenness·WIP·distinctiveness) (~25편, 4위) ✅ 기본 / ❌ 신규 변형
- [[pages/methods/community_detection|커뮤니티 탐지]] — 모듈성·블록모델·BMCD·코어-퍼리퍼리 재정의 (~24편, 5위) ✅ 기본 / ❌ 신규 변형
- [[pages/methods/longitudinal_network|종단/동적 네트워크 분석]] — 다층·이분 포함 (~23편) ⚠️ 부분
- [[pages/methods/network_scaleup|Network Scale-Up / ARD]] — 은닉 집단 규모 추정, Bayesian/Stan 통합 (9편) ❌
- [[pages/methods/bayesian_network_model|Bayesian / 잠재공간 모델]] — 계층적 잠재공간·텐서 구조 (~6편) ❌
- [[pages/methods/gnn|GNN (그래프 신경망)]] — 지원은 되나 318편 중 진짜 GNN 실사용 **0건**(태그 오탐 10건+ 확인) ✅ 지원 / 수요 없음
- [[pages/methods/ml|전통 ML / 앙상블]] — 링크 예측·노드 분류·SVM·RF·XGBoost ✅
- [[pages/methods/diffusion_propagation|확산/전파/면역화]] — SIR 모형·면역화 전략 ❌

### 신규 (유형 C 응용 분야 기반, 2026-09-22 789편 전수 재합성)
- [[pages/methods/llm_nlp|LLM / GPT 활용]] — 파인튜닝·RAG·자동 코딩, 응용 분야 1위 (~215편, 27%) ❌
- [[pages/methods/sentiment_analysis|감성 분석 (Sentiment Analysis)]] — BERT·VADER·ABSA, 응용 분야 2위 (~213편, 27%) ⚠️ 기본은 ✅ — ABSA·멀티모달 ❌
- [[pages/methods/topic_modeling|Topic Modeling (토픽모델링)]] — LDA·BERTopic·STM, 응용 분야 3위 (~145편, 18%) ✅ (BERTopic 포함, 과거 ❌ 오류 정정)
- [[pages/methods/text_classification|텍스트 분류 (Text Classification)]] — BERT 파인튜닝·제로샷·앙상블 (~120편, 15%) ⚠️ 부분
- [[pages/methods/semantic_network_analysis|Semantic Network Analysis (의미연결망)]] — 응용 분야 진짜 SNA 사례 (~50–57편, 7%) ✅ 최강 데모 후보 다수 확보

---

## Insights (분석 결과·인사이트)

> 위키 쿼리 결과 및 누적 분석 정보

- [[pages/insights/sna_method_frequency|SNA 방법론 사용 빈도]] — 318편 전수 집계(2026-09-22), ERGM+SAOM+REM 86편(27%) 단일 최대 계열
- [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]] — 에고넷 배치분석(즉시 실행 가능)·ERGM 홍보·SAOM/REM 공백, 우선순위 정리
- [[pages/insights/applied_domain_venue_2026|응용 분야 도메인 및 학술지 분포]] — 789편 전수(2026-09-22), 보건/정신건강 1위(18%)
- [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도]] — 789편 전수 집계, LLM 27%·감성분석 27%·토픽 18%·진짜SNA 7%, NetMiner 시사점
- [[pages/insights/applied_data_source_2026|응용 분야 주요 데이터 소스]] — 저자원 언어 NLP 15–20% 지속, "post-API 시대" 수집 위기 신호
- [[pages/insights/sna_data_source|SNA 학술지 주요 데이터 소스 (2020–2026)]] — 설문/에고넷 인터뷰 56%, 종단 28%, 응용 분야와 수집 방식 대조 정리

---

## Tools (도구)

- [[pages/tools/netminer|NetMiner]] — 전체 기능 메뉴, 실사용 사례 43편, 학술 트렌드 대조 (ERGM·GNN·BERTopic 지원 현황)
- [[pages/tools/other_tools|Other Tools]] — R·SPSS MODELER·RSiena 실사용 + Gephi·UCINET·Python 비교

---

## 통계

- 총 페이지: 1,192 (papers 1,159 · concepts 7 · methods 16 · insights 6 · tools 2, synthesize 신규 생성분 반영)
- 최근 업데이트: 2026-09-22 (SNA 318편 + 응용 789편 전수 synthesize — methods/concepts/insights 대량 갱신, netminer.md 대비 지원 현황 오류 2건 정정)
- NetMiner 사용 논문: 43편 (PDF/KCI/OpenAlex, `pages/papers/netminer/`)
- 학계 트렌드 논문: 695편 (OpenAlex, 2020–2026) — 개별 페이지 318편 + 카탈로그 7개(419편)
- 응용 분야 논문: 847편 (키워드 수집, 2025–2026) — 개별 페이지 789편 + 카탈로그 2개(58편)
- 수집 학술지 (유형 B): Social Networks (ISSN 0378-8733), Network Science (ISSN 2050-1250), Connections (ISSN 2816-4245, INSNA)
