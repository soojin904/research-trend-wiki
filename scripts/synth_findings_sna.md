# SNA 탐색 결과 원본 (2026-09-30 synthesize all, 3개 청크 병합)
대상: pages/papers/sna/ 전체 327편 (2020~2026)

---

## 청크1 (1~109번, ~253편 커버 — 범위 초과 처리됨, ERGM/SAOM/중심성/에고센트릭 등 전반)

방법: 각 페이지의 `**방법론**:` 블록, 키워드/태그, `## NetMiner 연관성` 섹션을 grep으로 전수 스캔.

### 방법론별 그룹
**ERGM 계열 (TERGM/STERGM/bipartite ERGM/dERGM 포함, 36편)**
- `2020_yon_exponential_random_graph_model.md`, `2020_weber_homophily_the_formation.md`(Temporal ERGM), `2020_fitzhugh_cognition_and_communication_si.md`(STERGM), `2021_kevork_bipartite_exponential_random_g.md`, `2021_block_statistical_model_for.md`, `2022_karwa_dergms_degeneracyrestricted_ex.md`, `2022_leifeld_the_stochastic_actororiented_m.md`, `2023_schmid_improving_ergm_starting_values.md`, `2023_huang_parameter_estimation_procedure.md`, `2024_pattison_exponential_random_graph_model.md`, `2026_ciordia_unequal_relational_gains.md`, `2026_buttazzo_using_lasso_for_variable.md` 등

**SAOM/RSiena (행위자지향 종단 모델, 23편)**
- `2020_hooijsma_multidimensional_similarity_mu.md`, `2020_kros_avoidance_antipathy_and_aggres.md`, `2022_toroslu_avoidance_action_negative.md`, `2022_leifeld_the_stochastic_actororiented_m.md`, `2023_espinosara_coevolution_sociocognitive.md`, `2024_ceoldo_stochastic_actor_oriented_mode.md`, `2025_snijders_double_agency_and_coevolution.md`, `2025_kruidhof_the_coevolution_informal.md`, `2026_mcmillan_network_rct_causal.md`

**중심성(Centrality) 지표 (48편, 최다 카테고리)**
- `2020_fan_degreelike_centrality_with_str.md`(구조적 0/1 보정), `2020_duxbury_identifying_key_players.md`(이분 네트워크 응집/파편화 중심성), `2021_schoenfeld_shortest_pathbased_centrality_.md`, `2023_skibski_closeness_centrality_via_the.md`, `2024_colladon_why_distinctiveness_centrality.md`, `2025_fernandez_centrality_and_social_domains.md`

**커뮤니티 탐지/블록모델링/SBM (24편)**
- `2020_dao_community_structure_comparativ.md`, `2022_cugmas_approaches_blockmodeling_dynam.md`, `2022_kulj_stochastic_blockmodeling_linke.md`, `2023_reittu_network_community_detection.md`, `2024_estvez_revising_the_borgattieverett_c.md`, `2024_armandola_clan_detector_algorithm.md`, `2025_lubold_spectral_goodnessoffit_tests_f.md`

**잠재공간/잠재위치 모델 (9편)**
- `2020_gollini_modelling_interactions_among_o.md`, `2022_sweet_hierarchical_latent_space.md`, `2023_rastelli_continuous_latent_position_mod.md`, `2025_gwee_modelbased_clustering_for_netw.md`, `2026_lu_zeroinflated_poisson_latent.md`

**임베딩/GNN/딥러닝 (27편)**
- `2020_ilya_recommending_collaborators_via.md`(GNN+토픽모델링), `2020_wilson_analysis_population_functional.md`(multi-node2vec), `2020_liu_learning_count.md`(CNN 그래플릿 카운팅), `2021_payne_diffusion_profile_embedding.md`, `2022_aggrawal_link_prediction.md`, `2022_li_consensus_embedding_for_multip.md`, `2026_yanchenko_labelswitching_algorithm_for.md`

**에고센트릭/퍼스널 네트워크 (42편, 두번째 최다)**
- `2020_hollstein_collecting_egocentric_network_.md`, `2020_stulp_collecting_large_personal_netw.md`, `2022_j_connecting_for_success_egocent.md`, `2023_bianchi_structure_personal_networks.md`, `2025_vlker_whos_your_extended.md`, `2026_almquist_homelessness_personal_network.md`, `2026_zhang_egocentric_csa.md`, `2026_schafer_personal_network_loneliness.md`

**설문 기반 데이터수집 도구(이름/위치생성기, ARD, NSUM, 17편)**
- `2020_vlker_social_capital_across_the.md`(position generator), `2021_kmetty_party_nexus_position_generator.md`, `2025_lee_use_aggregated_relational.md`(ARD), `2026_arevalillo_network_scaleup_methods.md`, `2026_feld_estimating_unknown_populations.md`, `2026_lubbers_nsm_ard.md`

**베이지안 방법 (21편)**
- `2023_mulder_bayesian_testing_scientific.md`(R 패키지 BFpack), `2023_ren_bayesian_nonparametric_mixture.md`, `2022_spencer_faster_mcmc_for_gaussian.md`, `2026_ward_bayesian_modeling_for_aggregat.md`

**다중/다층 네트워크(multiplex·multilevel, 30편)**
- `2020_hooijsma_multidimensional_similarity_mu.md`, `2020_interdonat_extracting_multilayer_networks.md`, `2024_broccatell_multilevel_integrated_healthca.md`, `2025_coll_hif_the_hypergraph_interchange.md`, `2026_an_peer_influence_multilayer.md`, `2026_fluer_multiplex_survey.md`, `2026_haapanen_coalition_sna_design.md`

**시뮬레이션/통계모형/이론 (44편, 순수 수리통계 다수)**

**QAP/MRQAP**: 이 청크에서는 검출 없음(0편).

### 응용 분야
- 보건/정신건강: `2020_cronin`, `2020_hollstein`, `2024_broccatell_multilevel_integrated_healthca.md`, `2024_browne_evaluating_disease_surveillanc.md`
- 정치/여론: `2020_beuthner`, `2020_cann_correct.md`, `2020_lee_political_isolation_america.md`
- 조직/경영: `2020_duxbury`, `2022_agneessens_network_formation_organization.md`
- 범죄/불법 네트워크: `2020_gollini`(밀수 도청), `2023_ballinger_insurgency_complex_network.md`
- 마케팅/전자상거래: `2026_qiao_ecommerce_rural_china.md`, `2026_zhang_egocentric_csa.md`
- 학계/공저: `2021_boekhout_investigating_scientific_mobil.md`, `2023_stefano_quality_issues_coauthorship.md`
- 교육/학교: `2020_hooijsma`(학교 괴롭힘), `2025_tanaka_bullyvictim_network_perception.md`

### 사용 도구
- RSiena: `2020_hooijsma`, `2020_kros`, `2022_toroslu`, `2024_ceoldo`
- R 패키지(자체 개발): `2020_yon`("ergmito"), `2021_kueffner`(자체), `2023_mulder`("BFpack"), `2024_pham`("aLSEC")
- GENSI(시각적 인터랙티브 네트워크 수집 도구): `2020_stulp`
- 대부분 초록 요약 특성상 Python/R 구체 라이브러리명 미언급 — 도구 정보 전반적으로 부족.

### NetMiner 커버리지 (잠정, netminer.md 재검증 필요)
- 가능: 에고중심 네트워크 분석(`2026_almquist`, `2026_zhang_egocentric_csa`, `2026_schafer_personal_network_loneliness`), 종단 네트워크 변화 추적(`2026_gebhard_intervention_dementia`, `2026_mcmillan_network_rct_causal`)
- 불가/판단보류: 다층·멀티플렉스 통합분석(`2026_an`, `2026_fluer`, `2026_haapanen` — "기능 개발 방향 참고"), 지리정보 통합(`2026_fancello`), ARD 기반 네트워크 추정(`2026_lubbers` — 판단보류), 네트워크 기반 인과추론/RCT 설계(`2026_omalley` — "직접 활용 사례 없음")

### 특이 트렌드
1. 에고센트릭 네트워크(42편)와 중심성 지표(48편)가 압도적 최다 카테고리
2. SAOM(RSiena)과 ERGM/TERGM이 종단 네트워크 분석의 양대 축, coevolution 모델로 확장 중
3. 2026년 카탈로그부터 응용 맥락(보건·마케팅·교육·조직)+개입/RCT 설계 결합 논문 증가
4. 다층/멀티플렉스 네트워크가 2026년 새 소분야로 부상 — NetMiner 로드맵상 잠재 갭
5. 네트워크 규모추정(NSUM/ARD)이 2025~2026년 집중 등장 — hidden population 응용과 결합
6. QAP/MRQAP은 이 청크(초반)에서 검출되지 않음
7. 소프트웨어/도구명 기재 전반적으로 희소 — OpenAlex 초록 요약 기반 구조적 한계

---

## 청크2 (110~215번, 106편 — ERGM/SAOM/REM/중심성/커뮤니티탐지/잠재공간/임베딩/에고센트릭 등)

### 방법론별 그룹화
**ERGM 계열 (약 15편)**: DERGM(`2022_karwa`), 협업네트워크 ERGM(`2022_smith_understanding_collaboration_pa.md`), 동종선호(`2023_hoffman_the_role_selection.md`), count-valued ERGM(`2023_huang`), 베이지안검정(`2023_mulder`), 시작값개선(`2023_schmid`), 다층ERGM(`2023_koskinen_analysing_networks_networks.md`), 다중네트워크ERGM(`2023_tolochko_same_but_different.md`), ERNM(`2023_wang_understanding_networks_with_ex.md`), 횡단ERGM(`2023_zwier_knowing_knowing_you.md`), R&D협력ERGM(`2023_lee_rampd_cooperation_collaborativ.md`), DPM-ERGM(`2023_ren_bayesian_nonparametric_mixture.md`), 다층ERGM의료(`2024_broccatell`)

**SAOM/RSiena (약 10편)**: 이론논쟁(`2022_leifeld_the_stochastic_actororiented_m.md`, `2022_leifeld_theoretical_and_empirical.md`), 부정적유대(`2022_toroslu`), 1모드+2모드 인용공진화(`2023_espinosara`), 에이전트기반확장(`2023_renzini`), 랜덤효과(`2024_ceoldo`), 반학교문화(`2024_kruse`), 교실상호작용(`2024_lintner`), 다층DyNAM(`2023_uzaheta_random_effects_dynamic.md`), 다중모달동적네트워크(`2022_haunss`)

**REM/RHEM (약 7편)**: 종설(`2023_butts_relational_event_models.md`), 기억감쇠(`2023_arena`), 변화점탐지(`2023_kamalabad`), 베이지안정규화(`2023_karimova`), 신경망REM(`2024_filippimaz`, DREAM), RHEM공저자(`2022_lerner`), RHEM공동범죄(`2023_bright`)

**중심성 (약 10편)**: 단조성이론(`2023_boldi`), 계층적해체(`2022_mayajarieg_use_hierarchical.md`), 중심성편향(`2022_tasselli`), 콩도르세근접중심성(`2023_skibski`), 지표간유사성(`2023_schoch`), 시간적매개중심성(`2024_bu`), Distinctiveness중심성(`2024_colladon`), WIP중심성(`2024_king`), 평균연결차수메타분석(`2024_neal_methodological_moderators_aver.md`), SAS PROC NETWORK(`2022_pinheiro_network_centralities.md`)

**커뮤니티탐지/블록모델링 (약 8편)**: 확률적블록모델링(`2022_kulj`), 랜덤워크클러스터링(`2022_queiros`), 다층+속성통합(`2023_reittu`), 씨족탐지(`2024_armandola`), 핵심-주변부(`2024_estvez`), BMCD알고리즘선택(`2024_deguilhem`), 10개커뮤니티방법비교(`2024_letina`), SAS Louvain(`2022_pinheiro_subnetwork_analysis.md`)

**잠재공간/잠재변수 (약 5편)**: 가우시안MCMC(`2022_spencer`), 계층적잠재공간매개(`2022_sweet`), 연속잠재위치(`2023_rastelli`), 교환가능프로빗(`2023_marrs`), NNTuck텐서분해(`2024_aguiar`)

**그래프임베딩/ML결합 (약 7편)**: 임베딩평가프레임워크(`2022_kamiski`), 합의임베딩SVD/VAE/CCA(`2022_li_consensus_embedding_for_multip.md`), 랜덤포레스트에고유형화(`2022_laier`), 딥러닝이미지네트워크(`2023_ballinger`), 그래프러닝+이산선택(`2023_tomlinson`), Python네트워크분석정신건강(`2024_ghosh`), ML네트워크구성원예측(`2024_lai`)

**구조적균형/양극화 (4편)**: 속성통합모형(`2023_grski`), 부호화동적시스템(`2023_morrison`), 가족내구조균형(`2023_stein`), 의미네트워크담론(`2022_suitner`, `2022_roth`)

**2모드/이중성 네트워크 (4편)**: 2모드생성모형(`2023_neal_the_duality_networks.md`), Breiger이중성(`2023_liardo_twomode_relational_similaritie.md`), 이분네트워크정지규칙(`2024_neal_stopping_rule_for.md`)

**퍼스널/에고센트릭 방법론 (약 9편)**: EgoNet프로그램(`2022_j_connecting_for_success_egocent.md`), 접촉일기(`2023_bianchi`), 알터표집(`2022_peng_random_sampling_alters.md`), 대리응답품질(`2022_stark`), 듀오중심유형(`2023_kennedy`), 이름순서효과(`2023_liu_name_order_effects.md`), 네트워크포트폴리오다양성(`2024_fu`), Trellis소프트웨어(`2022_lungeanu`), 상상네트워크모티프(`2023_tanaka_imaginary_network_motifs_struc.md`)

### 응용 분야
정치/담론(haunss, zaytsev, marrs, morrison), 보건/의료(ghosh, browne, maldonado, kim, broccatell), 교육(lintner, kruse, letina, kim, liu, j_connecting), 범죄/안보(bright, ballinger), 경제/금융(lrincz, lee), 과학사회학/서지계량(stefano, kuskova, espinosara), 가족/친족(armandola, stein, luken), 기후/SNS담론(suitner, roth), 비즈니스 SAS사례(pinheiro 시리즈)

### 사용 도구
EgoNet, Trellis, SAS PROC NETWORK/OPTNETWORK, RSiena(명시적), R패키지BFpack, Python3(라이브러리불명, ghosh), Python class공개배포(gonzlezcas), Socnet.se(estvez), R코드배포(colladon distinctiveness centrality). 대다수 논문은 "R"/"시뮬레이션"으로만 서술, statnet/igraph/networkx 등 명시 없음.

### NetMiner 커버리지 (잠정, netminer.md 재검증 권고)
- 가능: 중심성 전반, 커뮤니티탐지(Louvain), 블록모델링/핵심-주변부, 2모드 분석·투영, 에고센트릭 수집·분석, 시각화
- 판단보류/부분가능: ERGM, SAOM/RSiena(전용 R패키지 의존), 시간적 매개중심성 등 고급 temporal 알고리즘
- 불가: REM/RHEM(전문 패키지 필요), 베이지안 커스텀추정(BFpack/MCMC), 신경망결합모형(DREAM), 그래프임베딩(SVD/VAE/CCA), 에이전트기반모형/진화게임이론

### 특이 트렌드
1. ERGM과 SAOM/RSiena가 압도적 주류, 이론적비교/논쟁 다수(leifeld-cranmer)
2. REM(관계적사건모형) 급부상 — 2023 Social Networks/Network Science 특별호, 감쇠함수·변화점탐지·베이지안정규화·신경망결합 등 확장 집중
3. ERGM의 베이지안화 경향(Bayes factor, DP혼합모형)
4. ML/딥러닝과의 결합 증가(임베딩평가, 랜덤포레스트유형화, 신경망REM, 딥러닝이미지→네트워크)
5. 중심성 이론에 대한 메타적 재검토(단조성문제, 방법론선택영향, 지표간유사성 착시)
6. 개인/에고센트릭 네트워크 "측정 방법론" 자체가 독립 연구주제로 자리잡음(대리응답정확도, 알터표집, 이름순서효과)
7. 다층(multilevel/multilayer) 네트워크 방법론 표준화(ERGM/SAOM/커뮤니티탐지 모두 다층확장판)
8. 소프트웨어 도구 명시가 드묾(RSiena, BFpack, SAS PROC, EgoNet, Trellis, Socnet.se 정도만 확인)

---

## 청크3 (216~327번, 111편 — SAOM/ERGM/커뮤니티탐지/중심성/NSUM-ARD/이원네트워크/잠재공간/확산게임/텍스트+네트워크/개입RCT/기타통계)

### 방법론별 그룹화
**SAOM/확률적 행위자지향모델 (최빈)**: `2024_waxenecker_corruption_dynamics_public.md`, `2025_gilsbach_digital_communication_and_tie.md`(SAOM+MI), `2025_cowen_trends_friends_time.md`, `2025_kruidhof_the_coevolution_informal.md`, `2025_reiner_moving_beyond_constrained_sett.md`, `2025_parker_the_effect_perceptions.md`(SIENA), `2025_shappell_accounting_for_edge_uncertaint.md`(SAOM+HMM), `2025_snijders_double_agency_and_coevolution.md`(이원SAOM확장), `2026_park_intersectoral_structural_netwo.md`, `2026_mcmillan_network_rct_causal.md`, `2026_vit_rigid_boundaries_selective_sal.md`(베이지안 다층SAOM)

**ERGM 계열**: `2024_pattison_exponential_random_graph_model.md`, `2025_breuer_investigating_the_dynamics.md`(다층ERGM, Yakuza), `2025_livas_urban_environmental_stewardshi.md`, `2025_reiner_who_would_ask_whom.md`, `2025_tanaka_bullyvictim_network_perception.md`(다중ERGM), `2026_ciordia_unequal_relational_gains.md`(ERGM+TERGM), `2026_buttazzo_using_lasso_for_variable.md`(LASSO+ERGM), `2026_yang_understanding_the_formation.md`

**커뮤니티탐지/클러스터링**: `2024_pham_automated_detection_edge.md`(aLSEC), `2024_yanchenko_generalized_hypothesis_test.md`, `2025_gwee_modelbased_clustering_for_netw.md`(LSPCM), `2026_lu_zeroinflated_poisson_latent.md`, `2026_yanchenko_labelswitching_algorithm_for.md`(core-periphery)

**중심성**: `2024_sziklai_audience_selection_for_maximiz.md`(8개중심성, 마케팅), `2025_fernandez_centrality_and_social_domains.md`, `2025_liardo_the_correspondence_analysis.md`(Bonacich vs 대응분석), `2026_asil_immunization_method_using.md`(PageRank+근접중심성), `2026_murraywatt_the_decay_impact.md`(고유벡터중심성, Friedkin-Johnsen)

**네트워크 스케일업(NSUM)/ARD**: `2025_baum_explaining_contact_patterns.md`, `2025_lee_use_aggregated_relational.md`(ARD+ABM), `2025_gonzlezcas_collecting_large_number.md`, `2025_plaza_networked_inequality_the_role.md`, `2025_vlker_whos_your_extended.md`, `2026_arevalillo_network_scaleup_methods.md`(선거예측), `2026_feld_estimating_unknown_populations.md`(capture-recapture), `2026_lubbers_nsm_ard.md`(리뷰), `2026_ward_bayesian_modeling_for_aggregat.md`(Stan)

**이원(two-mode)/이중성 네트워크**: `2025_larsen_overlapping_social_circles.md`(k-서클), `2025_liardo_the_correspondence_analysis.md`(CA), `2025_espinosara_sociocognitive_networks_betwee.md`(관계초이벤트), `2025_everett_alter_composition_with_overlap.md`(Gould-Fernandez brokerage 일반화), `2025_schler_the_duality_network.md`(MCA), `2025_snijders_double_agency_and_coevolution.md`, `2025_uzaheta_modeling_the_duality.md`(SBM+DyNAM), `2026_tang_twomode_network_autoregressive.md`

**잠재공간/베이지안**: `2025_gwee`, `2026_lu_zeroinflated_poisson_latent.md`, `2026_sweet_investigating_the_impacts.md`(잠재공간+결측), `2026_ward_bayesian_modeling_for_aggregat.md`

**확산/전염/게임이론**: `2024_singh_generating_preferential_attach.md`(선호적연결), `2025_burai_nonlinear_model.md`(비선형DeGroot), `2025_lamberson_network_games_with_local.md`, `2026_asil_immunization_method_using.md`(SIR-UA), `2026_murraywatt_the_decay_impact.md`(선형확산)

**텍스트마이닝/NLP+네트워크 결합**: `2025_angst_automated_extraction_discourse.md`(NER+LLM stance→담론네트워크), `2026_almquist_search_common.md`(키워드보조토픽모델→가치네트워크)

**인과추론/RCT/개입 네트워크**: `2026_mcmillan_network_rct_causal.md`(SAOM+knockout), `2026_omalley_spillover_rct.md`(stepped-wedge), `2026_gebhard_intervention_dementia.md`, `2026_park_intersectoral_structural_netwo.md`, `2025_trasciani_from_mapping_action.md`, `2025_mayajarieg_types_networkbased_interventio.md`, `2025_riddell_methods_for_interventions_usin.md`

**기타 통계적 네트워크방법**: `2025_sischka_nonparametric_twosample_test_f.md`(그라폰), `2025_lubold_spectral_goodnessoffit_tests_f.md`(랜덤행렬이론), `2026_boschi_beyond_linearity_and_timehomog.md`(RHEM+텐서곱스무딩), `2026_lakdawala_not_all_bonds_are.md`(DLC-REM), `2026_cook_dynamic_programming_for_calcul.md`(DTC)

**데이터수집/도구혁신**: `2025_coll_hif_the_hypergraph_interchange.md`(HIF), `2026_nijs_introducing_vina_engaging.md`(VINA 앱), `2025_neal_closest_relationship.md`(CHIP50), `2026_panti_illustrated_tutorial.md`(MMSNA튜토리얼), `2026_kreager_mixed_methods_lifecourse.md`

**순수 그래프이론**: `2024_tavasoli_the_art_interconnections.md`, `2025_zuev_breadth_depth_and_flux.md`(DAG), `2026_shojaei_counting_chemical_isomers_with.md`

### 응용 분야
마케팅/소비자(`2024_sziklai`, `2026_zhang_egocentric_csa`, `2026_qiao_ecommerce_rural_china`), 정치/여론/양극화(`2025_chen_broken_egg`, `2025_candellone`, `2025_mepham`, `2025_salloum`, `2025_esch`, `2026_almquist_search_common`, `2026_arevalillo`), 보건/노화/웰빙(`2025_ellwardt`, `2025_reiner_moving_beyond`, `2025_reiner_who_would_ask_whom`, `2025_modi`, `2026_gebhard_intervention_dementia`, `2026_schafer_personal_network_loneliness`, `2026_kingma`, `2026_nishi_wellbeing_experimental_network`, `2025_riddell`), 범죄/일탈(`2025_battisti`, `2025_breuer_yakuza`, `2025_girard`), 조직/경영(`2025_parker_exploration_exploitation`, `2025_marantz`, `2025_ghawi`, `2026_marhag`, `2025_soda_conclave`), 교육(`2025_gilsbach`, `2026_vit`, `2025_schler`, `2025_tanaka`), 도시/커뮤니티(`2025_livas`, `2025_mayajarieg_multiple_senses_community`, `2026_fancello`), 과학사회학(`2025_espinosara`, `2026_yang_understanding_the_formation`), 환경/혁신(`2025_sica`)

### 사용 도구
R패키지 `aLSEC`(`2024_pham`), VINA 오픈소스 앱(`2026_nijs`), Stan(`2026_ward`), SIENA(`2025_parker_the_effect_perceptions.md`), HIF JSON스키마(`2025_coll`). 대다수 초록에 언어 수준 언급조차 없음 — 구체 라이브러리(networkx, igraph, statnet, RSiena 등) 명시 논문은 이 청크에서 확인 안 됨(본문 접근 필요).

### NetMiner 커버리지 (잠정)
- 가능(추정): ERGM, 중심성, 커뮤니티탐지, 에고네트워크, 이원네트워크, 대응분석, k-서클류
- 불가/고급통계영역(추정): SAOM(RSiena계열), 베이지안잠재공간모델, 그라폰기반검정, RHEM, DLC-REM, LASSO-ERGM, NSUM/ARD정교추정
- 판단보류: 다층/멀티플렉스면역화(MCPR), 하이퍼그래프(HIF), 텍스트→네트워크파이프라인(LLM stance detection)

### 특이 트렌드
1. SAOM(RSiena계열) 압도적 최다 — 교우관계·조직지식·건강·정치대화 등 종단분석 표준. ERGM과 양대축
2. NSUM/ARD 붐 — 2026 Social Networks에 리뷰/베이지안통합/capture-recapture/선거예측 클러스터
3. 이원(two-mode)/이중성(duality) 네트워크 재조명 — Breiger 이중성 확장 다수
4. 텍스트마이닝+네트워크 결합(LLM 활용) — LLM stance detection→담론네트워크, 키워드보조토픽모델→가치네트워크
5. 개입(intervention)/인과추론 네트워크의 방법론적 성숙 — RCT-네트워크 상호작용(스필오버, 참여자편향) 급증
6. 데이터 수집 방법론 자체의 혁신 — 스마트폰앱(VINA), 데이터정제가이드(CHIP50), 혼합방법튜토리얼(MMSNA)
7. 순수 수학/그래프이론 논문 지속 혼재(Network Science 저널 특성)
