# 응용분야 탐색 결과 원본 (2026-09-30 synthesize all, 7개 청크 병합, 청크2는 4개 하위배치)
대상: pages/papers/applied/ 전체 909편

---

## 청크1 (1~129번: 2025__ ~ 2025_matuszewsk 대)

### 방법론별 그룹
**A. 감성분석/오피니언마이닝 (약 45편, 최다)**
- 어휘기반(VADER/TextBlob/SentiStrength/NRCLex/LIWC): dewi_sentiment_analysis_the, islam_crisis_communication_social, kirilenko_sentiment_and_emotion_analysis, jihad_analyzing_public_sentiment, abutara_beyond_words_understanding_anx
- ML/DL 분류기(SVM·NB·RF·LSTM·CNN·GRU): althobaiti_emotional_detection_social, arif_hate_speech_detection_from, alia_classification_public_sentimen
- Transformer/BERT계열(FinBERT/RoBERTa/DeBERTa/SciBERT/BioBERT): alalmai_prediction_tasi_returns, ali_geospatial_sentiment_analysis, cheng_financial_sentiment_analysis_w, li_predicting_stock_market_trends, gabrielyan_aibased_approaches_for_multicl
- 하이브리드 임베딩융합(GloVe+BERT, Word2Vec+BERT): iyer_hybrid_glovebert_fusion, jiang_multiscale_feature_fusion
- 중국어(Snow NLP/Baidu Senta/SKEP): guo_emotional_evaluation_digital, li_public_feedback_analysis

**B. 토픽모델링(LDA/NMF/BERTopic, 약 25편)**
- BERTopic: cao_analyzing_osha_construction_ac(vs LDA), jihad_analyzing_public_sentiment, mahmutovi_analyzing_usergenerated_review, li_public_feedback_analysis(+SKEP), deka_improving_public_service_griev(LSA/NMF/LDA/BERTopic 벤치마킹)
- LDA전통: hakim_topic_modelling_analysis, ayaz_forty_years_international, benothman_uncovering_key_service_improve, he_regulatory_innovation_for_digi, liu_analyzing_students_emotional_t
- 신경/의미론적: guo_biovmnvtm_geometryaware_neural(VAE+vMF), drissi_topic_modeling_and_analysis(SemaTopic/ARIA)
- keyATM: dai_conceptualizing_digital_democr

**C. LLM 활용(프롬프팅/파인튜닝/에이전트, 약 20편)**
- 상용LLM비교(GPT/Claude/Gemini/Llama/Qwen): burns_comparison_commercial_decodero, enache_from_seo_aeo, brandt_extractive_versus_generative_l, cheng_financial_sentiment_analysis_w(LoRA/QLoRA)
- LLM에이전트/시뮬레이션: boji_agentbased_simulation, chicorico_oratoriaua_virtual_assistant
- LLM기반 주석/분류 파이프라인: langlais_legibot_annotating_legislative, langlais_legibot_comprehensive_theorydr(경량SLM), bedratyuk_logicontological_reconstructio(GPT+온톨로지)
- 제로샷/퓨샷/CoT: griswold_stay_tuned_improving_sentiment, burnham_political_debate_efficient_zer

**D. SNA/네트워크·그래프 분석(약 10편, NetMiner 관련성 높음)**
- 의미연결망+중심성: lee_text_analysis_news(CONCOR), kim_big_datadriven_topical(키워드공출현망+NetworkX 4개중심성+Louvain)
- 서지계량 네트워크: lai_pybiblionet_python_library(인용/공저/키워드공출현, 커뮤니티탐지)
- GNN: khan_adversarial_variational_graph(VGAE), abdelrahem_twophase_bootstrap_approach(SRL+RDF)
- 정치/신념 네트워크 공진화: kammerer_the_hierarchy_beliefs
- SNA+질적혼합: gold_nurseled_models_care, golebie_mixed_methods_research_applica
- 전파/확산 시뮬레이션(SIR): li_emotional_contagion_mechanism_

**E. 질적/혼합방법론**: 담화분석(alkhatib, goloshchuk), 내용분석+PRISMA(fitro, azwar, ali_sentiment_analysis_arabic), 질적+양적혼합(kochalski, lukito_comparing_qualitative_thematic)

**F. 멀티모달**: figueroa_bimodal_gender_classification_(ViLT/CLIP/FLAVA), braster_analyzing_school_photographs(CV+내용분석), gokulnath_empowering_emotional_intellige(CNN+BERT+RNN+GAN)

### 응용 분야
금융/주식(alalmai, li_predicting_stock_market_trends, cheng), 보건/정신건강(abutara, hacohenker, arora, gold), 정치/공공정책(dai, kammerer, goloshchuk, deka), 재난/위기관리(li_public_feedback, gu_analyzing_natural_disaster_ris), 마케팅/고객경험(cahya, mahmutovi, can_metahuman_social_media_influen), 교육(gl_does_chatgpt_argue, liu_analyzing_students, barbara), 산업안전/건설(cao, chen_weaving), 학술동향/서지계량(kim_big_datadriven, lai_pybiblionet, gusenbauer), 미디어/커뮤니케이션(lanabi/lova priming_for_war_ukraine, kharlamov), 인문학(jia, ilyefalvi, christou)

### 사용 도구
NetworkX(kim_big_datadriven), Sastrawi(인니, benothman/hidayat), kiwipiepy(한국어, kim_big_datadriven), TensorFlow/Keras/PyTorch(gokulnath), Word2Vec/GloVe/FastText/ELMo/Flair(alfian), BERTopic, keyATM(dai), VADER/TextBlob/SentiStrength/NRCLex/LIWC/Snow NLP/Baidu Senta/SKEP, Voyant Tools(goloshchuk, ilyefalvi), TextAnalyst 2.32(러시아, kharlamov), UDPipe/huspaCy/e-magyar(헝가리어, barbara), Streamlit(arora), OpenAlex API(lai_pybiblionet). 대다수는 "Python"/ML알고리즘 수준으로만 기술.

### NetMiner 커버리지(잠정)
가능: 키워드공출현망+중심성+커뮤니티탐지(kim_big_datadriven), 의미연결망+CONCOR(lee_text_analysis_news), 서지네트워크(lai_pybiblionet), 감성사전기반(VADER류 대체 가능)
불가: BERTopic/트랜스포머파인튜닝, LLM에이전트시뮬레이션, GNN(VGAE), 멀티모달, 도메인특화파인튜닝(FinBERT/SciBERT)

### 특이 트렌드
1. BERTopic이 LDA 빠르게 대체 중(일관성·다양성 지표 우세)
2. "토픽모델링+감성분석" 결합 패턴 반복 — 복합방법론 관심분야와 직결
3. LLM을 "분석도구"이자 "라벨러"로 이중 활용(자동라벨링→경량모델 학습, GPT에이전트 온톨로지생성)
4. 저자원언어(인니/네팔/카자흐/아랍/헝가리) 특화 전처리 도구 개발 꾸준
5. 에이전트 기반 시뮬레이션 등장(LLM 에이전트로 SNS 사용자행동 시뮬레이션)
6. SNA는 소수지만 "서지계량+네트워크" 조합에서 강세 — NetMiner 워크플로우와 가장 직접 연결

---

## 청크2 (130~257번, 128편 — 자체 10편 직접 + 4개 하위배치)

### 하위배치 직접 읽은 10편 요약
- maulana_formulation_model: STM+SNA(QAP/MRQAP)+CDA 혼합, 정치커뮤니케이션(인니 정책확산) — 판단보류(STM 미지원 가능성, QAP는 가능)
- min_trend_analysis_anticorruption: LDA(반부패 625편) — 가능
- muflih_emotion_detection_and_sentimen: DistilBERT 감정분류(이커머스) — 불가
- mulianingr_comparative_performance_svm: SVM vs BERT-Base+VADER(패스트패션) — 불가(BERT 부분), VADER는 유사기능 가능성
- nugroho_literaturedriven_contributions: LLM기반 감성분석+동적가중치(개념적) — 판단보류
- murzabekov_the_extraction: DistilBART 자동요약(법률) — 불가
- mukhsimbay_computational_pipeline_for: NLP파이프라인(법률 텍스트) — 판단보류
- nijhara_precise_and_closedform: SimRank 개선(순수 알고리즘) — 불가
- novotn_drivers_return_plans: SEM+탐색적네트워크분석(난민귀환) — 불가
- meng_psychologybased_unified_dynami: IRT기반 커리큘럼러닝(SNA무관) — 불가

### 하위배치1 (30편)
- oko: SemaTopic+ARIA topic modeling(LLM라벨링) — 불가
- oprea: LLM-as-a-judge 파인튜닝(RoBERTa/DistilBERT) — 불가
- ortiz: LLM 감정어노테이션 vs 인간비교 — 불가
- paci: LLM프롬프팅 함축탐지 — 불가
- papachrist: 멀티에이전트LLM 네트워크형성 시뮬레이션 — 판단보류(SNA시뮬레이션 흥미로운 응용)
- patuk: DeepSeek R1 비교분석(지질학 웹서비스) — 불가
- peng_leveraging: LLM+임베딩 단어유사도(WSLE) — 불가
- punuru: 멀티에이전트LLM RAG(Queryome, 생의학) — 불가
- ramadhan: RoBERTa-IndoBERT cross-lingual(통화정책) — 불가
- rahmawati: MLP+문장임베딩(의료 텍스트분할) — 불가
- rasheed_bilstmcrf: BiLSTM-CRF NER(사이버보안) — 불가
- rani: CNN+BiLSTM+BiGRU 하이브리드 — 불가
- pan: GNN+차분진화 — 불가
- padmanabha: TF-IDF+SVM+SMOTE — 가능
- pratama: TF-IDF+SVM/VADER/NB — 가능
- putri: TF-IDF+RandomForest(출판) — 가능
- rahmah: TF-IDF+SVM(종교미디어) — 가능
- rasheed_ansecmm: 감성/부정성 네트워크지표 — 판단보류
- radja: FCA기반 XAI 다중라벨분류 — 판단보류
- park: keyATM — 판단보류
- rmling: 코퍼스+예비토픽모델링(디지털휴머니티) — 가능
- radliski: LLM방법론 리뷰(소프트웨어공학) — 판단보류
- ozimek: EBICglasso 부분상관 심리네트워크(중심성/bridge) — 판단보류
- rizi: 최대엔트로피랜덤그래프, homophily분해, SBM(네트워크과학이론) — 판단보류
- ogheneakok: 설문+회귀(교육) — 판단보류
- ozolaschad: 내용분석+다층모형(정치) — 판단보류
- pronina: Siamese신경망 필적귀속(디지털휴머니티, 이미지기반) — 불가
- poniszewsk: 문헌리뷰 — 판단보류
- peng_unpacking: 개념적 시간프레임워크 에세이 — 불가(이론논문)
- rasheed_building: 커뮤니케이션이론 에세이 — 불가(이론논문)

NetMiner 집계(배치1): 가능 5편 / 불가 16편 / 판단보류 9편
특이사항: LLM-as-a-judge(oprea), 인간vs LLM주석비교 반복(ortiz/paci, LLM 미세의미구분 실패), 멀티에이전트LLM이 인간네트워크형성원리(선호적연결/삼자폐쇄/동질성) 재현(papachrist) — LLM을 SNA시뮬레이션 도구로 보는 새 응용, cross-lingual translate-then-classify(ramadhan), homophily 집단크기별 분해 신규수리모델(rizi)

### 하위배치2 (30편)
- saadi_languageadaptive_ensemble_clus: BERT임베딩+PCA+앙상블클러스터링(정신건강) — 불가
- saleem_reqnet_llmdriven_computational: ALBERT/BERT/XLNet+LSTM/GRU 앙상블(SW공학) — 불가
- salleh_comparative_analysis_backtrans: 역번역+의미유사도(SW공학) — 불가
- samsudin_comparative_machine_learning_a: 어휘라벨링+TF-IDF+ML(정치) — 가능
- sandiva_comparison_random_forest: 감성라벨링+RF vs SVM(비즈니스) — 가능
- sanjaya_review_sentiment_analysis: SLR(멀티모달, 마케팅) — 판단보류
- schumann_detection_contradictions_and: 프롬프트엔지니어링 LLM분류(법률) — 불가
- schuster_advancing_water_security: 서지리뷰+LDA(환경) — 가능
- schwarz_named_entity_recognition_and: NER/EL 개관챕터 — 판단보류
- shayesteh_health_care_utilization: 설문+기술통계+주제분석(보건) — 가능
- shen_adaptive_graph_neural_network: 적응형GNN(디지털휴머니티) — 불가
- shi_research_nlp_techniques: NLP기법 리뷰(SNS행동) — 판단보류
- skorin_application_natural_language: ML+DNN+통계+트랜스포머(전자상거래) — 판단보류
- snchezgmez_swarmbased_multiobjective_appr: 스웜기반 다목적 요약(SNS) — 불가
- stracqualu_digital_communities_and_collec: 개념적 개관(디지털커뮤니티) — 판단보류
- su_lics_locating_intercharacter_s: 장면텍스트탐지(CV, SNA무관) — 불가
- suing_disinformation_and_regulation: 설문+인터뷰+감성분석(정치) — 가능
- sun_can_large_language_models: LLM임상텍스트분석(GPT-4.1/Claude/Deepseek) — 불가
- suwarno_genrebased_sentiment_and_emoti: CRISP-DM+TF-IDF+LR/SVC(미디어) — 가능
- tabassum_llm_based_sentiment_classifica: LoRA/PEFT LLM파인튜닝(전자상거래) — 불가
- talib_computational_sentiment_analys: MNB/RF/LR 감정분류(SNS) — 가능
- tang_optimizing_influence_spread: cross-layer cascade+k-core+Infomap+LWCD — 가능(부분)/판단보류(전체파이프라인)
- tarmizi_named_entity_recognition: PRISMA NER리뷰(종교텍스트) — 판단보류
- teng_interactive_knowledge_extracti: 규칙기반 문장중요도랭킹(교육) — 판단보류
- tissera_natural_language_processing_re: NLP자원 리뷰(타밀어) — 판단보류
- tiurin_multistage_heuristic_filtering: 휴리스틱 텍스트정제(법률) — 가능
- toktobekov_llmbased_multiagent_systems_fo: LLM멀티에이전트 리뷰(수학교육) — 불가
- unknown_decade_deep: LDA+기술로드맵핑(공학) — 가능
- unknown_predicting_mental_health_risk: 언어특징+감성+BERT/RoBERTa(정신건강) — 판단보류
- vadavalli_social_structure_shapes_consen: ABM 다층사회네트워크(인류학) — 불가

### 하위배치3 (30편)
- vaghasiya_automated_detection_hate: SVM+NLP(콘텐츠모더레이션) — 판단보류
- varghese_manual_annotation_based_sentim: 수동주석+SVM/NB/DT/RF/CNN(헬스앱) — 불가(CNN부분)
- vattikunda_novel_transfer_deep: 전이학습+교차언어임베딩(다국어SNS) — 불가
- velden_sentiment_analysis: 문헌리뷰(정치) — 판단보류
- venkatrama_characterizing_language_use: 전산언어분석(장애연구) — 판단보류
- verdear_identifying_and_characterizing: Louvain+동질성지표+네트워크+콘텐츠분석(정치, 2020선거허위정보) — 가능
- verma_decade_data: 서지분석+Lotka/Bradford+공출현+협업네트워크(Biblioshiny/VOSviewer) — 가능
- wahyuni_public_response: 트윗크롤링+InSet렉시콘+TF-IDF+SVM(에너지정책) — 가능
- wahyunings_temporal_topic_modeling: TF-IDF+NMF+시간적시각화(미디어) — 판단보류
- wandwi_decoding_gendered_symbolism_an: NLP+토픽모델링+감성+모티프+의미클러스터+네트워크(문학) — 가능
- wang_automatic_classification_const: BERTopic-GLDA vs YAKE-GLDA/SVM/CNN(건설안전) — 불가
- wang_evolutionary_dynamics_pairwise: 진화게임이론(복잡계) — 불가
- wang_pesticide_residues_reduce_bact: 16S rRNA+모티프네트워크(미생물생태) — 불가
- wang_study_the_evaluation: 다지역투입산출+복잡네트워크+TERGM(농업경제) — 판단보류
- wati_sentiment_analysis_mental: TF-IDF+SVM/KNN/NB/LR/DT/RF(정신건강) — 가능
- wei_entity_relationship_extraction: 의존파싱+GCN+MGRel(보안) — 불가
- willadsen_inferring_employee_concerns_fr: STM vs 지도학습(HR) — 판단보류
- wu_knowledgeenhanced_multitask_fr: LLM+법률지식그래프+멀티태스크(법률) — 불가
- yang_clines_clinical_llmbased_infor: LLM에이전트 임상정보추출(헬스케어) — 불가
- yuan_bigru_and_bertbased: BERT+BiGRU+LSTM-attention+mBERT/XLM-R(미디어) — 불가
- yudianto_support_vector_machine_algorit: ABSA+SVM+베이지안최적화(관광) — 가능
- zahra_language_anxiety_identificatio: BERT파인튜닝(IndoBERTweet)+LIME(교육) — 불가
- zaki_lisa_language_independent_sent: 텍스트→그래프+GCN/GAT+Word2vec(전자상거래) — 불가
- zareer_survey_opinion: 리뷰+ABM+네트워크토폴로지(SNS) — 판단보류
- zein_sentiment_analysis_product: 전처리+NaiveBayes(전자상거래) — 가능
- zghoul_performance_evaluation_classic: TF-IDF+LR/RF/NB(정신건강/고객) — 가능
- zhang_comparative_study_machine: TF-IDF+GridSearchCV+RF/LR/NB/SVM(헬스케어) — 가능
- zhang_ivcn_siamese_network: Siamese BERT(창의성평가) — 불가
- zhao_attentionbased_anomaly_detecti: 어텐션+듀얼오토인코더(사이버보안) — 불가
- zhao_lawllmds_twostage_parametereff: 2단계LoRA+양자화(법률) — 불가

### 하위배치4 (28편)
- zhu_modalities_missing_multimodal: 멀티모달융합 리뷰 — 불가
- zscherneck_rural_network_assemblages_dise: 에고네트워크+질적인터뷰(지역개발) — 가능
- 2026__construction_and_annotation: 코퍼스구축+주석체계(정치) — 판단보류
- 2026__happiness_political_communicat: 안면감정인식+텍스트감성(정치) — 불가
- 2026__historical_science_the: 생성AI 역사텍스트(디지털휴머니티) — 불가
- 2026__hybrid_model_for_authorship: RoBERTa+문체+대조학습(전산언어학) — 불가
- 2026__ltbgt_ltbgtltbgtltbgt_lt: 자동내용분석+프레이밍(공공PR) — 가능
- 2026__prompt_engineering: LLM프롬프트엔지니어링 논의(디지털휴머니티) — 불가
- 2026__weibo: 토픽모델링+어휘의미+담화분석(국제관계) — 가능
- abdrazakh_comparative_analysis_neural: CNN/LSTM/BERT계열 벤치마킹(정신건강) — 불가
- abdulkaree_scientific_text_summarization: ATT-DEC+SciBERT+MLP(생의학) — 불가
- abualigah_multilabel_classification_arab: GloVe+LSTM(아랍미디어) — 불가
- abudalbouh_analyzing_humanitarian_advocac: ML/NLP감성+전문가검증(정치) — 가능
- abudalbouh_new_framework_for: SVM감성(정치, 왕실연설) — 가능
- achelya_comparative_analysis_the: NB/SVM/LR/RF vs IndoBERT(혐오발언) — 판단보류
- adam_integration_bertopic_and: BERTopic+IndoBERTweet ABSA(정책) — 불가
- adeel_embedding_against_the_odds: 인터뷰+에고SNA+아카이브(이민연구) — 가능
- agterberg_overview_asymptotic: SBM 통계이론 리뷰 — 판단보류
- ahmad_research_article_recent_advanc: PRISMA 트랜스포머 다국어감성 리뷰 — 불가
- ahmadi_troll_detection_using_generati: GAN+LSTM+SNA특징(허위정보) — 불가
- akben_advancing_harmful_content_dete: LLM+Elo레이팅(HR) — 불가
- alada_computational_exploration_tren: LDA+공출현네트워크(디지털휴머니티, R) — 가능
- aladaini_digital_brand_resonance: 5단계NLP(감성+ABSA+BERTopic/LDA+SNA+통계삼각측량, 고등교육마케팅) — 판단보류
- alaeddini_textbased_insights_generative: 서지텍스트분석+공출현+토픽모델링+버스트분석(경제) — 가능
- alcover_blending_sentiment_and_topic: LDA+TextBlob+XGBoost+SHAP(마케팅) — 판단보류
- aldossari_wasta_and_gender_inequality: 개념적프레임워크(젠더) — 불가
- alejandro_computational_discourse_analys: 방법론통합프레임워크(디지털휴머니티) — 판단보류
- alheeh_the_rhetorical_features: 질적CDA(언어학) — 불가

### 특이 트렌드(청크2 종합)
- LLM-as-annotator/judge 패턴이 전 배치에 걸쳐 반복 등장
- 멀티에이전트LLM 네트워크형성시뮬레이션(papachrist)이 SNA와 LLM의 새로운 접점

---

## 청크3 (258~386번, 129편)

### 방법론별 그룹
**토픽모델링(LDA/STM/DTM/CTM/BERTopic)**: arima_emergence_class_awareness, aslan_thematic_evolution_educational, chen_from_barbarism_civilization, chen_united_tale, chen_modeling_gender_consciousness_, calcagn_topic_modeling_budget(LSA/fLSA/LDA/CTM비교), cheng_framework_for_tracking(LDA+DTM+STM통합), bakan_detecting_sentiment_analysis_c; STM: cei_the_jae_positioning, dixon_what_does_the_media; BERTopic: ambrosino_celebrating_european_law_and, cui_public_opinion_sentiment_and, chen_what_drives_ebsa_across, couto_exploiting_topic_analysis_mode(LDA vs BERTopic vs TopClus)

**감성/정서분석**: cahyani_sentiment_analysis_user(SVM/LR/RF), daraghmi_sentiment_classification_amazo, bahekapl_analyzing_middle_school_studen; 도메인특화BERT: bharad_multidocument_nlp_framework(FinBERT), chavan_finenzo_financial_sentiment_ba; 다중모드: deshpande_integrating_facial_emotion_rec, badouch_from_emotion_action(ABSA+베이지안+업리프트); demiral_machine_learning_approach(Ekman/Plutchik+토픽모델링)

**SNA/네트워크분석**: bezerra_leveraging_gans_for_citation(인용망 PageRank/Betweenness), daniel_the_network_and_care(의료제공자망), chenchu_barriers_hindering_knowledge_m(건설업지식경영 SNA), corsi_social_life_the(돌고래사회연결망), bhattachar_inferences_mixing_probabilitie(DCMM), chandrika_capturing_microdynamics_tempor(HMM triadic closure), detering_bootstrap_percolation_random, dangelo_networked_migrants_and_denetwo(이주정책 관계망), chavezmigu_collaborative_agrobiodiversity(혼합방법SNA+민족지)

**LLM활용**: benoit_using_large_language_models, besley_economic_policy_narratives, choi_finetuned_large_language_model; RAG: asai_synthesizing_scientific_litera(OpenScholar), choi_mapping_and_comparing_climate(LangChain), chen_the_legalization_international(CoT+RAG); 질적보조: braune_gamechanger_for_qualitative(ChatGPT코딩), dai_context_matters_llmassisted; 안전성: aliberti_the_illusion_insight, canale_llm_safety_boundary_dissolutio; 벤치마킹: anuyah_benchmarking_llms_for_pairwise, arzideh_comparison_proprietary_and

**트랜스포머/BERT NER**: alkasem_machine_learning_methods_for(우울증), aurpa_bangla_meder_multibert_ensembl, bajestani_cognitive_graph_transformer_in, bayu_explainable_afroxlmr_approach; NER: cao_domain_lexicon_enhanced_named(BERT-CRF), azam_hybrid_llm_and(SapBERT+FAISS); bashir_dualbert_adversarial_learning_(GAN+듀얼BERT)

**GNN/GAN 하이브리드**: alqusair_integrating_syntactic_and_sema(듀얼GCN, ABSA), alhothali_pastognn_promptaware_spatiotem(시공간GNN), bezerra(cGAN-SciBERT), altameem_qrnngru_framework_for_automati(QRNN-GRU)

**의미연결망/텍스트유사도**: alriyaee_study_semantic(코사인유사도), boratyn_textual_similarity_invariant(번역불변성), bombelli_spherical_double_kmeans

**전통ML분류/클러스터링**: bahena_evaluation_text_classification(NB/RF/SVM/LR/KNN/K-means), dahake_clustering_business_news_for(K-means+BERT임베딩), dharmendra_classifying_public_complaints(CNN/RNN/LSTM+스태킹)

**서지계량+네트워크**: bahari_systematic_review_hyperparamet(PRISMA+VOSviewer), demirel_sentiment_analysis_communicati(bibliometrix+협업네트워크)

**디지털인문학/코퍼스도구**: castrocort_introduccin_anlisis(Quanteda), cuip_digital_analysis(Voyant), armand_introduction_histtext(HistText), castrogonz_gpto_and_executable_text(KNIME vs GPT-4o)

**OCR/필기인식**: amin_powered_handwritten_answer, biswas_novel_approach

### 응용 분야
정신건강(alkasem, ciobotaru, chng, daniati, couto, chen_multiscale), 정치/정책(benoit, besley, baumgartne, birkenmaier, choi_finetuned, cern, deng, bazyari), 마케팅/관광(badouch, blancomore, brahmane, dahake), 법률(bhatt, calcagn, chen_the_legalization, dhala), 의료/헬스케어(arzideh, ayalew, berthou, cai, cherukuri, daniel), 교육(aslan, bahekapl, braune, chansaeng), 금융/증권(bharad, cajner, chavan), 미디어/저널리즘(bhargava, bilal, dixon), 생태/생물(briggs, corsi, chavezmigu), 제조/건설(cao, cho, chenchu), 디지털인문학/역사(armand, carius, cuip, chelali)

### 사용 도구
BERTopic, LDA(gensim), STM(R stm), Quanteda(R), fLSA/CTM; BERT/RoBERTa/XLM-RoBERTa/AfroXLMR/SciBERT/FinBERT/DistilBERT/ELECTRA/SBERT/LoRA; spaCy, CAMeL Tools(아랍어), TajikNLP, medkit, Presidio; FAISS, LangChain; Voyant Tools, HistText; KNIME, Orange, VOSviewer, bibliometrix(R); TF-IDF, Word2Vec, FastText, PyMuPDF; Cohen's kappa, Wilcoxon, Shapley, HMM

### NetMiner 커버리지 (netminer.md 직접 대조 수행됨)
- 가능: LDA/BERTopic 토픽모델링(Text메뉴 확인됨), 중심성분석(7종 지원), 커뮤니티탐지(Louvain/Leiden), 의미연결망(제한적, 단순동시출현만), 감성분석(BERT기반, 7개국어 제한적), GCN/GraphSAGE/GAT(표준 GNN분류만), ERGM/MR-QAP(지원확인, 적극홍보대상), 전통ML분류(AdaBoost/RF/SVM/kNN)
- 불가: LLM파인튜닝/RAG/프롬프팅(CoT등), GAN/듀얼BERT/QRNN-GRU 등 커스텀딥러닝, OCR/필기인식/멀티모달(영상+음성+텍스트), HMM/bootstrap percolation/혼합멤버십 등 통계이론모델, 임베딩기반 코사인유사도(alriyaee/boratyn)
- 부분가능: 서지분석(Biblio Data Collector로 수집 가능, VOSviewer식 시각화는 별도)

### 특이 트렌드
1. "LLM-as-annotator/coder" 패턴 급증(질적코딩/감성라벨링/인과판단을 인간 대신 LLM에 위임, Cohen's kappa 검증)
2. RAG+CoT 결합 확산(법률/과학문헌종합/정책비교)
3. 저자원언어 NLP 자원구축 붐(타지크/하우사/벵골/우르두/암하라/루마니아)
4. 토픽모델 비교연구 정착(LDA vs BERTopic vs TopClus 등) — NetMiner의 LDA+BERTopic 동시지원이 경쟁우위
5. 멀티모달 감성·행동분석 증가(얼굴+음성+텍스트) — NetMiner 커버 불가
6. 인용네트워크×딥러닝 결합(GAN+SciBERT→중심성 재평가) — NetMiner 강점과 결합 가능한 마케팅 포인트
7. 재현성/방법론감사 이슈 부각(GPT-4o vs KNIME 재현성비교 등)

---

## 청크4 (387~515번, 129편)

### 방법론별 그룹
**토픽모델링**: LDA(dutta_harnessing, gad_when_methods_matter, hu_lda_analysis, hall_topic_counts, hong_mapping, ho_discovering, huatangari_analysis); BERTopic(dobrani_approaches, halim_comparative, jesudas_utilizing, kim_llmbased_classification); STM(gosztonyi_sex_love); LLM기반신규기법(douglas_prism, gmezzar_revisiting)

**감성분석**: 고전ML(ginanjar_sentiment, gorbunova_sentiment, hafeez_comparative, helmy_multilingual); 딥러닝(gashaw_bilingual, kakkar_deep_learningbased, jasmir_hybridization); 트랜스포머(gugri_contextaware, khan_novel_hybrid, etelis_generating); LLM aspect-level(hsueh_beyond_single_topics, dobrani_approaches); 문화편향(geng_limitations)

**LLM활용**: 멀티에이전트(elshaer_medrefkg, hu_agentmental, jung_villain); 프롬프트엔지니어링(eldem_the_development, fang_probabilistic, doumanas_unbiasing); 질적분석보조(katz_thematic_analysis, gmezzar_revisiting, hedley_sandpiper, espino_los_llm); 문헌리뷰자동화(joos_leveraging_llms, jiang_large_language_models); 평가/편향(goryunova_the_construct, kanygin_interpretation, dong_one_score, koch_the_social_structure)

**네트워크분석**: SNA(dwitama_collaborative, han_nonprofit_resilience, jiang_the_social_embeddedness-SAOM, guerrero_from_informal-Gephi, gabriel_search_for_sociality, kanbur_mapping_news-Louvain); 의미연결망(eskjr_shifting_semantics, ge_framing_artificial-DNA); GNN(elikten_exploring_graphbased, huang_stage, he_latent_diffusion, heydari_hyperpersona, fan_directed_graph)

**텍스트분류/정보추출/NER**: 법률(etin_trke_hukuk, franchino_identifying, khaliq_evaluating); 의료(gupta_abjadmed, elumalai_twostage, ganesh_deep_learning); 혐오/독성(e_automated_toxicity, karayiit_electrabased)

**번역/다국어**: huy_freetxtvi, idah_benchmarking, huang_exploring, jati_indobert

**혼합방법론**: gelmon_the_scope, dobrani_approaches, herderich_measuring, gosztonyi, huatangari

### 응용 분야
보건/의료(elshaer, elumalai, gupta, guo, hossain, helmy, kamal, hu_agentmental), 정치/거버넌스(franchino, kaneko, goldin, ge, kang), 마케팅/소비자(halim, hu_comparative, ginanjar), 재난/위기(guerrero, jalia, gonzlez), 교육(eldem, jati, hong, ho), 법률(etin, franchino, khaliq), 미디어(haider, kanbur, fayez), 디지털인문학(dobrani, evans, grmar, hu_uncovering), 환경/생태(hu_pollution, gabriel, havran)

### 사용 도구
LDA(gensim), BERTopic; BERT/RoBERTa/DeBERTa/DistilBERT/ALBERT/ClinicalBERT/FinBERT/Financial-RoBERTa/ELECTRA/IndoBERT/ParsBERT/SBERT; TextBlob/VADER/NRCLex; SVM/RF/LR/NB; LSTM/BiLSTM/GRU/CNN, FastText; GPT-4/4o/4.1/5, Claude Sonnet 4.5/4.6, Gemini, Grok, Qwen2.5/3, Llama Krikri, Mistral; Gephi, Python(networkx추정), SAOM/RSiena; GCN/GraphSAGE/GAT; Coh-Metrix, UMAP, Word2Vec; MAP-CARE, STAGE, HEC, SiBot

### NetMiner 커버리지(netminer.md 대조 수행 — LDA+BERTopic, BERT감성, Word Network, ERGM, MR-QAP, GNN, SNA/중심성 확인)
- 가능: LDA(dutta/gad/hall/hong/ho/huatangari), BERTopic(dobrani/jesudas/halim/kim), 감성분석(ginanjar/gorbunova/hafeez/hu_comparative/jadiya — BERT감성모듈 대체가능), 의미연결망(eskjr/ge), SNA/중심성/커뮤니티(dwitama/han/jiang_social/guerrero/gabriel/kanbur/hu_pollution), GNN 개념적대응(elikten/huang_stage)
- 불가: 멀티에이전트프레임워크(elshaer/hu_agentmental/jung_villain), 프롬프트엔지니어링/CoT/APE(eldem/fang/doumanas), LLM질적분석보조(katz/hedley/espino/joos), 커스텀파인튜닝아키텍처(guillenram/huang_stage일부), LSTM+RoBERTa하이브리드(khan_novel), AI텍스트출처귀속(iqbal), 디퓨전모델(he_latent_diffusion)
- 판단보류: 서베이/동향정리형 논문(hussein, ganesh)

### 특이 트렌드
1. LLM-as-annotator/judge 패턴 급증(질적코딩/문헌리뷰필터링/팩트체킹/평가) — 다만 LLM한계지적 연구도 병존
2. 도메인특화 BERT파생모델의 전성기 — 범용LLM보다 실무 정확도·비용 우월 반복확인(SVM=GPT-4o-mini 정확도+무비용, ParsBERT>ChatGPT)
3. 저자원언어 NLP 붐(신디/베트남/테갈란/암하릭/우르두/그리스/터키)
4. 멀티에이전트 LLM 프레임워크 부상(의료/팩트체킹)
5. LLM 안전성/붕괴탐지 메타연구 등장
6. 정보손실 정량화 비판(LDA 단일토픽강제할당 51.2%정보손실 등) — NetMiner의 LDA고도화+BERTopic 병행 홍보 필요성 시사

---

## 청크5 (516~647번, 132편)

### 방법론별 그룹
**토픽모델링**: koffi_harnessing_textual_analytics_f(LDA), kulkarni_topic_modelling_using_lda, law_the_nature_monetary(LDA+TF-IDF+공기어), ku_understanding_welldying_resear(텍스트네트워크+LDA), ludwig_neural_topic_method(LX Topic: FASTopic+LLM정제), nguyen_beyond_coherence_improving_tem(L-DNTM), ng_public_discussion_deepseek(VADER+LDA), lukito_comparing_qualitative_thematic(질적주제분석 vs 기계토픽모델링), ozornina_unpacking_translation_effects_(다국어STM), lu_communicating_and_constructing(토픽모델링+LIWC+계량경제), lin_construction_and_evolution_ana(텍스트마이닝+지식그래프)

**감성분석**: koulammaga_smart_complaint_detection_and(RoBERTa멀티태스크), kulkarni_aspectbased_sentiment_analysis(ABSA), kumar_hybrid_framework_for_sentiment(SenticNet+TextBlob+BioBERT), lavanya_contextaware_sentiment_classif(BiLSTM), lee_the_influence_sentiment(감성+감정8종), li_sentiment_classification_stock(ERNIE), li_imagetext_sentiment_analysis_m(멀티모달), lakshmi_social_media_text_analysis(XGBoost+BiLSTM+CNN+RoBERTa), mamidi_realtime_sentiment_analysis(VADER+RoBERTa앙상블), more_block_chainbased_sentiment_ana, msrnaidu_twitter_sentiment_analysis_usi(BERT), muzaky_comparison_scorebased_and(KNN), nisha_transformerbased_sentiment_ana(PRISMA리뷰), nugraha_public_sentiment_toward_the(BiLSTM-CNN), nursikuwag_support_vector_machine(SVM vs KNN), obiadoh_machine_learning_approach(로지스틱회귀), p_based_psychology_analysis(SVM/LSTM), kseler_detecting_climate_delay_discou(LLM zero/few-shot), milkova_detecting_basic_values(LLM보조라벨링+XLM-RoBERTa), mcdossi_detecting_behavioral_and_emoti(BET프레임워크), mayrhofer_gpt_outperforms_bert_and(GPT vs BERT/LIWC)

**SNA/중심성/네트워크구조**: koistinen_importance_overlapping_network(중심성+확산모델), lie_quantifying_multidisciplinary_(코오커런스+모듈성+중심성), nurkholisa_the_role_social(Gephi+네트노그래피), liu_dynamic_spatial_association_ne(SNA+TERGM+중력모형), ning_unraveling_the_evolution(SNA+모티프+SAOM), nakis_modeling_roles_and_tradeoffs(다층 Trade-off Model), lucas_reducibility_higherorder_netwo, mahapatra_processnets(생물학네트워크앙상블), mburiamwal_disclosure_hiv_positive(에고SNA+GLMM), nunes_redes_sociais_clima(에고SNA, UCINET/NetDraw), maclaurin_large_deviations, lilian_myside_bias_availability_bias, maron_john_adams_the(SNA+지성사), mowbray_the_role_networking(에고네트워크+혼합방법), ouz_soft_trioid_graphs_for(Louvain/Infomap비교), mccombe_implementation_and_evaluation(RE-AIM+SNA)

**GNN/그래프딥러닝**: li_graph_selfsupervised_learning(GraphCL+GraphMAE), liu_graph_neural_networks_for(GCN/GAT/GraphRNN), liu_citation_recommendation_algori(SciBERT+Temporal GAT), ma_bhygnn_unsupervised_representa(하이퍼그래프), ldallitsak_from_global_local(동적슬라이딩윈도우+GAT), liu_planning_emotional_education_s(GAT+BERT-BiLSTM), lu_mmstancedet_retrievalaugmented(RAG+멀티모달멀티에이전트)

**LLM활용/평가**: kousha_how_much_are_llms, liu_what_actually_being(IPR프레임워크), mclaren_magic_words_methodical, meher_build_borrow_just(ConfliBERT vs ModernBERT), mousavi_from_lexicons_large, oppenlaend_mapping_the_challenges(GPT-3.5/4 2단계), mahbub_multistage_validation_framewor, li_esgsasb_label_stability(GPT-4o+Claude), neto_legalbenchbr_benchmark_for(BERTimbau-LoRA vs Claude/GPT), palicki_dont_look_evaluating(CO2-Adjusted F1), lin_large_language_models(LLM심리시뮬레이터), ma_can_machines_think_like(LLM에이전트 행동경제학)

**혼합방법론**: lee_mixed_methods_analysis, li_creators_perceptions_and_attit(워드클라우드+감성+공단어+SNA), morgner_grounded_multiplicity, makkawi_bibliometric_analysis(VOSviewer), koutsoupia_explainable_artificial_intelli(bibliometrix)

**텍스트마이닝/NER/기타**: kulkarni_study(NER+상호참조), kuropatkin_comparative_study(NER+베이지안네트워크), madni_politics_people(Whisper+spaCy+BERTopic+감성), nuriddinov_digital_humanities_based_compu

### 응용 분야
의료/헬스케어(kumar_hybrid, kuropatkin, mahbub, lie, oh_epigenomic, nunes, mccombe, mottalib, more_theramind), 마케팅/전자상거래(kulkarni_aspectbased, lyu_hybrid, nguyen_framework, ludwig), 정치/정책(kseler, lerner, matsuoka, meher, mclaren, ocen, nugraha), 미디어/커뮤니케이션(madni, nguyen_generative, nguyen_representation, liang, lu_communicating), 교육(koistinen, kouba, mirsch, mcgillivra, mowbray), 금융/경제(koulammaga, li_sentiment, law), 사회학/젠더(lee_claiming, oh_social, li_constructing), 법률(lerer, neto), 농업/환경(kulkarni_topic, more_block, liu_dynamic, newton), 심리/정신건강(lakshmi, p_based, milkova, ma_multilevel, low_using)

### 사용 도구
BERT/RoBERTa/ERNIE/SciBERT/BERTimbau/ConfliBERT/ModernBERT/XLM-RoBERTa/BioBERT, GPT-3.5/4/4o/Turbo, Claude 3.5 Haiku, Gemini-2.0-Flash, LLaMA-3; BiLSTM/CNN/GAT/GCN/GraphCL/GraphMAE/Wav2Vec/ANN; LDA/FASTopic/BERTopic/STM; SVM/KNN/RF/GB/LR/NB; Snorkel, BGE embedding; VADER/TextBlob/SenticNet/LIWC; spaCy/NLTK/GATE/scikit-learn/Whisper; Gephi/UCINET/NetDraw/VOSviewer; bibliometrix(R), TERGM, SAOM, PLS-SEM; QLoRA/Unsloth, llama.cpp, construct-tracker(Python)

### NetMiner 커버리지(잠정, 재검증 필요 표시됨)
- 가능: SNA/중심성/커뮤니티/다층네트워크 대부분(koistinen, lie, nurkholisa, ning, maron, mowbray, mccombe, nunes)
- 판단보류: 특수알고리즘(nakis-다층Trade-off모델, ouz-Soft Trioid Graph), 신경망토픽모델(L-DNTM, LX Topic)
- 불가: GNN계열 전반, LLM파인튜닝/에이전트/멀티모달 계열, 트랜스포머딥러닝분류 전반

### 특이 트렌드
1. "토픽모델링+LLM정제" 하이브리드 급증(LDA/BERTopic 결과를 LLM으로 재정제·라벨링)
2. LLM을 "심사자(judge)"로 쓰는 다단계 검증 프레임워크
3. 비용/지속가능성 vs 성능 트레이드오프 논의 본격화(CO2-Adjusted F1, 캐스케이드 소형모델)
4. 감성분석의 다중태스크·멀티모달화(속성+심각도+감정+감성 동시분류, 이미지-텍스트, 오디오+텍스트)
5. SNA와 텍스트분석의 결합(혼합방법) — NetMiner의 "SNA+텍스트마이닝 통합" 포지셔닝과 직접 관련
6. LLM기반 정치/사회과학 텍스트주석의 방법론적 성찰 논문 다수(모범사례가 통제비교에서 유지되는가)
7. 소형/오픈소스 모델의 실용적 재조명

---

## 청크6 (648~777번, 130편)

### 방법론별 그룹
**LLM/생성형AI(제로샷·퓨샷·프롬프팅·RAG·에이전트, 약 35편)**: peez_using_llms_for_measurement(UN안보리), storme_beyond_the_campaign_trail(제로샷트윗분류), sairanbeko_automatic_analysis_political, schoch_fate_but_what(AI거버넌스); schmitt_enhancing_sentiment_classifica(CoT·Self-Consistency), semin_strategies_for_span_labeling(LogitMatch); RAG(sesharatna_legal_document_analysis_and, rawat_information_retrieval_framewor); 로컬LLM(richterpec_onpremise_detection-Llama3.1-70B, schweinber_local_large_language_models-R+Ollama, posta_secure_scalable_large-Qwen3-VL, saukkoriip_automating_clinical_informatio-핀란드EHR); 정보추출(schulte_feasibility_using_large, remaki_syncabel_synthetic_contextuali, samal_data_augmentation_strategies); 에이전트(song_envscaler_scaling_toolinteract, ren_memlens_benchmarking_multimoda); 기타(rybensk_the_use_generative, quevedo_perspectives_llms, shetkar_systematic_review)

**토픽모델링**: patricia_multiplatform_topic_modeling_a, rajabu_uncovering_hidden_factors, qadikolaei_who_plans_the_city, ren_alignment_between_chinas_elder, sanghvi_trends_blockchain, salem_novel_integration, sulaeman_analisis_tingkat_sentimen_opin; BERTopic(phlmann_how_nations_narrate_quantum, shakeel_agrilens_semantic_retrieval); LDA vs BERTopic(riyansyah_application_latent_dirichlet-BERTopic일관성0.99); STM(rainero_the_contemporary_debate); 문서선택비교(rangreji_the_effect_document-LDA/BERTopic/TopicGPT/HiCode)

**감성분석**: pamulapart_hdrsa_hybrid_deep(RoBERTa+CNN-BiLSTM+VADER), r_hybrid_sentiment_analysis(VADER+RoBERTa), riansyahpu_sentiment_analysis(IndoBERT), sultana_hybrid_approach_for(BanglaBERT앙상블), shi_sentiment_and_topic_analytics(BERT-Bi-xLSTM-Attention), polpinij_reliabilityaware_multilingual_

**의미연결망/공동출현**: pan_analysis_hotspot_areas(co-word), park_changes_the_esg(Sometrend), prasetyo_mapping_the_intellectual_struc(VOSviewer), rugaiyah_mapping_the_intersection(ScientoPy+VOSviewer), pokropek_from_keywordbased_text_measure(임베딩코사인→CFA)

**SNA/네트워크(직접적용)**: perdana_grassroots_against_the_bet(SNA+콘텐츠분석), phelps_analysing_student_staff_member(설문기반SNA), pkknen_the_emergence_computational(공동인용, CSS파편화), sukasno_the_politics_forest(Actor-Network-Interest+centrality, 65액터), smith_weightactivated_main_path(Main Path Analysis+토픽모델링), sadhu_motive_motifbased_framework(temporal motif), stewart_pseudolikelihoodbased_mestimat(ERGM류 이론)

**XAI**: radain_from_accuracy_insight(SHAP+LIME), rashmi_multimodal_machine_learning_fr(SHAP), panda_artificial_intelligencebased_d(SHAP), song_integrating_attention_attribut

**프레이밍/담론/내용분석**: saidy_framing_analysis_the(Pan&Kosicki), ping_from_factual_selection, ragnedda_news_media_narrative_authority(43,027건)

### 응용 분야
보건/의료(pandit, poduval, saukkoriip, posta, richterpec, shetkar), 정치/정책/거버넌스(peez, schoch, posazhenni, qadikolaei, sairanbeko, sierra, sltzer, storme), 마케팅/전자상거래(pandiri, pradeep, rashmi, qin, sun_amplifying, peng_modeling), 법률(pavate, ragazzi-comma, peng_review, sesharatna), 금융(peng_parameterefficient-FinBERT/DeBERTa/ModernBERT+LoRA, roy, runchen), 디지털인문학/역사(skantsi-GPT4/LLaMA3.1, song_transforming, pasula), 교육(phelps, pham_enhancing, roscan_mutse-CEFR), 농업(shakeel, polpinij), 환경/에너지정책(sukasno-SNA+ANI, pan_analysis_hotspot_areas)

### 사용 도구
BERT/RoBERTa/DeBERTa-v3/ModernBERT/FinBERT/AraBERT/DarijaBERT/BanglaBERT/IndoBERT/ELECTRA/DistilBERT/mBERT; BERTopic/LDA/TopicGPT/HiCode/STM; Word2Vec/GloVe/Sentence-Transformer/LaBSE; VOSviewer/ScientoPy/Orange/RStudio; VADER/TF-IDF; Llama-3.1-70B/3.2/Qwen3/Gemma2:9B/Mistral7B/GPT-OSS:20B; GPT-4o-mini/gemini-1.5/2.5/Whisper/Claude/ChatGPT/Copilot; UMAP/HDBSCAN/isolation forest; ONNX/OpenVINO/NNCF INT8/vLLM/Databricks; Flask/MySQL/Docker/LoRA; lavaan(CFA), ollamar; **썸트렌드(Sometrend)** — 한국 ESG담론 연구 사용

### NetMiner 커버리지(잠정, netminer.md 미확인 명시됨 — 재검증 필요)
- 가능: 순수SNA/중심성/ERGM류(phelps, smith_weightactivated, sadhu(temporal motif는 특수기능 필요), sukasno), 공동출현네트워크(pan_analysis, park_changes_the_esg, prasetyo, rugaiyah)
- 불가/판단보류: LLM/트랜스폼세부튜닝 영역 대다수(감성분석/분류논문 대부분), 토픽모델링(LDA는 확인됨이나 이 청크에선 재검증 안됨, BERTopic/STM 확인필요)

### 특이 트렌드
1. LLM-as-judge/검증패턴 확산(교차언어 도덕성, CEFR평가)
2. 제로샷/퓨샷 정치텍스트분류가 표준워크플로우로 정착(대규모SNS/의회텍스트→LLM제로샷코딩→통계비교)
3. 저자원언어(아랍방언/벵골어/카자흐어/인니어) BERT계열 미세조정 주류
4. 감성+토픽 결합 프레임워크가 응용분야(자동차/전기차/헬스케어)에서 반복 패턴화
5. XAI(SHAP/LIME) 결합이 감성분석/분류논문의 기본요소로 정착
6. 로컬/온프레미스 LLM배포가 민감도메인(의료/금융/법률)에서 급증 — 데이터보안규제 대응 트렌드
7. **"Ghost 논문" 발견**: `2026_sharks_ghost_meaning_the_semantic.md` — 정상학술논문이 아닌 미래역서술 실험적/의사학술 텍스트, 메타데이터 이상징후(가상미래인용, DOI역설계) — 위키 관리자 검토 권장

---

## 청크7 (778~909번, 130편)

### 방법론별 그룹
**토픽모델링**: ustenko_measuring_citizen_frames_and(BERTopic, 시민프레임), xia_air_pollution_regulation_for(BERTopic, 중국정책12081건), wang_going_beyond_description_multi(다국어BERTopic비교), zhang_scbertopic_semanticcentroid_hi(SC-BERTopic 계층형), ye_research_topic_evolution, xu_media_discourse_construction(LDA); LSA→LDA→BERTopic→LLM 계보리뷰(takola_from_lsa_llm); STM(tulga_academic_literature_deepfakes); 그래프기반term weighting(sutedi_term_weighting_based)

**감성분석/오피니언마이닝(약 35편, 최다)**: Lexicon(unknown_emojbased_sentiment_analysis_s, verma_sentiment_analyzer_multimethod); Transformer(vandana_enhancing_text_sentiment_class-RoBERTa, venkauskas_evaluation_companys-XLM-RoBERTa, utami_effectiveness_finetuned_multil-mBERT, taheripour_multiobjective_portfolio_optim-FinBERT, wan_msar_multistage_adversarial_re); 앙상블(suryavansh_robust_ensemble_machine-NB+SVM+DT); 멀티모달(udoh_sentiment_analysis_model-CNN+LSTM, v_tmh_transformermarkov_hybrid, wang_chain_thought_driven-CoT+KAN); ABSA(yaln_understanding_aspectsentiment_)

**LLM활용(약 40편 이상, 가장 뚜렷한 신흥트렌드)**: 지식그래프구축(yang_ctithinker_llmdriven_system-CTI, zhang_bridging_dual_knowledge_graphs-BifrostRAG, wang_large_language_modelenhanced); RAG/멀티에이전트토론(you_bluemed_retrievalaugmented_mul, trirat_tsdebate_multimodal_collaborat); 이벤트/구조화추출(wilson_from_text_events, trudelle_urban_housing_conflicts, velardita_metadex_extracting_metada, yu_uncertaintyaware_structured_da); 안정화/제약디코딩(xie_cast_achieving_stable_llmbased, yang_semantic_alignment_and_output); 임베딩토픽모델링(trelohan_how_protect_and); 문헌리뷰합성(wagner_generative_artificial_intellig, wei_lrrobot_unified_supervised); 프롬프트압축(zhou_from_similarity_structure, zhu_from_token_token, wan_efficient_task_adaptation); 스탠스/평가탐지(walker_promises_and_pitfalls, traberg_turning_research)

**SNA**: unknown_malaysias_domestic_tourism_net(중심성+Louvain+Fiedler), turo_vehicle_features_influence_pee(P2P카셰어링), yang_exploring_public_spaces_roles(공간격리), wijayanto_new_election_old_affective(사이버부대); 시간적(wang_dynamics_local_clustering-delta clustering); 공간+QAP(wang_structural_evolution_block_dif-어업, xu_carbon_emission_network_centra-탄소배출, y_analysis_the_evolution-TERGM); 하이퍼네트워크(wang_quantifying_government_guidanc); 소셜봇(zhao_analysis_behavioral_features)

**GNN/링크예측/지식그래프**: wang_crossgnn_crossnetwork_embeddin(다층링크예측), zheng_graph_neural_networks_for(이종성그래프서베이), zhao_multiscale_heterogeneous_graph(중첩NER용GNN), zhang_locally_differentially_private(차분프라이버시그래프클러스터링)

**정보확산/영향력최대화**: tang_reinforce_the_particle_swarm(PSO+VNS), zhao_effects_interlayer_alternation(다층SAR모델)

**서지계량학**: yin_from_injury_prevention(CiteSpace+VOSviewer+Bibliometrix), yayla_tracing_thematic_evolution(Co-LCSH), wan_thematic_evolution_commonwealt

### 응용 분야
마케팅/소비자(unknown_aipowered_content_optimization, yaln, xa_emotion_analysis), 관광(xiao_multimodel_text_mining, xu_gated_attentionbased_multimode, wang_analysis_tourist_emotions, unknown_malaysias_domestic_tourism_net), 금융/투자(taheripour, venkataram_llmaugmented_trading_and_decis, yin_constructing_cmbs_default, wan_msar), 정치/거버넌스(topuolu_the_language_protest, wilson_from_text_events, wijayanto, ustenko), 보건/정신건강(thamrin_enhancing_explainability, wu_artificial_intelligencedriven_, zhou_comparative_sentiment_and_them), 기후/환경(sweeney_reading_the_climate_room, tian_public_emotions_and_climate, trelohan, xia_air_pollution_regulation_for), 법률(wang_legalhanopt_hierarchical_atten, zhao_lawllmds), 교육(tretowfish_generative_student, zhi_investigating_the_effects), 사이버보안(yang_ctithinker, unknown_web_guardian), 문학/디지털인문학(wandwi_reframing_narrative_analysis_c, yaseen, zhenzhao), 사회정의/혐오표현(syajar, trager_the_moral_foundations_reddit, yeste)

### 사용 도구
TensorFlow/Keras(udoh), sklearn류(SVM/RF/LR다수), CNN-LSTM, BiLSTM-CapsNet; BERT/RoBERTa/DeBERTa/ALBERT/DistilBERT/XLM-RoBERTa/mBERT/ELECTRA(터키)/IndoBERT/FinBERT/StructBERT/Mengzi-BERT; BERTopic/LDA/Top2Vec/TopicGPT/Biterm(BTM); SBERT/USE/GloVe/Word2Vec/FAISS; LangChain, Streamlit, FastAPI; VADER/TextBlob/HowNet/DUTIR(중국어); **Gephi**(zhao_analysis 봇네트워크), **VOSviewer**(topuolu, yin_from_injury_prevention), CiteSpace/Bibliometrix(R); BeautifulSoup+requests; Google Cloud Vision/Tesseract/EasyOCR/PaddleOCR/ABBYY FineReader; UMAP+K-means++; **TEXTOM**(yoo_timeseries_analysis, 한국계열 텍스트마이닝 플랫폼)

### NetMiner 커버리지(잠정, netminer.md 미열람 명시)
- 가능: unknown_malaysias_domestic_tourism_net(중심성+Louvain), wang_structural_evolution_block_dif(SNA+QAP), xu_carbon_emission_network_centra(중심성), y_analysis_the_evolution(TERGM=ERGM계열), wang_dynamics_local_clustering(clustering coefficient), zhang_health_promotion_solutions_for(SNA+시스템다이내믹스)
- 불가: LLM/RAG/GNN 관련 그룹 대부분 — 딥러닝/생성형AI파이프라인
- 판단보류: 하이브리드(SNA+텍스트마이닝 결합) — wang_quantifying_government_guidanc, wandwi_reframing_narrative_analysis_c, zhao_analysis_behavioral_features

### 특이 트렌드
1. LLM이 거의 모든 서브도메인에 침투 — 단순분류를 넘어 지식그래프구축/RAG/멀티에이전트토론/구조화추출/프롬프트압축 등 인프라적 역할로 확장
2. "LLM비판/성찰" 메타논문 등장(traberg-AI연구단일문화, wu_impact-동료심사질저하, zhi-비판적사고저해)
3. BERTopic이 LDA를 사실상 대체하는 흐름 지속
4. 감성분석+SNA/토픽모델링의 복합방법론이 표준화(3종 결합이 기본패턴)
5. 경량화/효율화 트렌드(LoRA/QLoRA, 선택적파라미터최적화, 프롬프트/토큰압축)
6. 불확실성/신뢰도 정량화가 새로운 요구사항으로 부상
7. 중국어권 연구의 압도적 물량(웨이보/도우인 등 30여편) — 국내 SNA/텍스트마이닝 시장 비교 참고자료

---

## 전체 종합 메모 (오케스트레이터용)
- SNA 327편 + applied 909편 = 1236편 전체 탐색 완료
- 국내(한국) 텍스트마이닝 플랫폼 경쟁도구 재확인: Sometrend(썸트렌드), TEXTOM — 이번 신규 탐색에서도 재등장, 기존 tools/other_tools.md 갱신 대상
- "Ghost 논문" 이상탐지: `pages/papers/applied/2026_sharks_ghost_meaning_the_semantic.md` — 위키 관리자 검토 필요(정상 카탈로그 데이터 아닐 가능성)
- LLM-as-annotator/judge, 멀티에이전트 LLM 시뮬레이션(SNA 형성원리 재현), RAG+CoT 결합이 applied 전역에서 반복되는 최대 트렌드
- BERTopic이 LDA를 사실상 대체하는 흐름이 여러 청크에서 독립적으로 확인됨 — insights 페이지 신설 후보
- 다수 청크가 netminer.md 재검증을 권고("판단보류" 다수) — synthesize 작성 단계에서 반드시 netminer.md 대조 필요(CLAUDE.md 규칙)
