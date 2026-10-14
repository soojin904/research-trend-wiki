# 위키 로그

## [2026-10-14] synthesize | 2026-10-07 이후 신규분 증분 합성 (응용 60편, 유효 57편)

- **대상**: 2026-10-07 마지막 synthesize 이후 신규 생성된 개별 페이지만 — `pages/papers/applied/` 신규(untracked) 60편. `pages/papers/sna/`는 이번 ingest에서 신규 0편(전수 중복)이라 대상 없음. 기존 963편/321편 본문은 재열람하지 않음
- **제외**: 60편 중 3편을 의사과학/비검증·안내성 콘텐츠로 집계 제외 — `2026_computing_october_top_read_articles`(Zenodo 안내글, 실증 없음), `2026_lvarez_sociometra_ordinal_computacion`(자가출판 유사과학 매니페스토), `2026_kurdin_macroscope_case_studies_part`(비표준 자가지시적 프레임워크). 유효 57편 기준 집계
- **탐색**: 병렬 에이전트 4개(각 15편)로 초록 수준 판독
- **methods 갱신**: `centrality.md`(+10편, 완전 재현 가능 데모 2건 신규 확보: wu·fernández), `ergm.md`(Bright — ERGM을 개입평가 시뮬레이션 도구로 쓰는 신규 응용 패턴), `community_detection.md`(sommer·feoh·fernández + signed network 공백 재확인), `topic_modeling.md`(+3편, STM 공변량 결합형 공백 재확인), `sentiment_analysis.md`(커스텀 하이브리드 딥러닝 감성모델 클러스터 4편+, ABSA·XAI 사례 추가), `llm_nlp.md`(LLM 에이전트 네트워크 시뮬레이션 추가 사례, GNN+LSTM 시공간 융합), `gnn.md`(mardamsyah 시공간 융합 사례)
- **insights 갱신**: `applied_method_frequency_2026.md`에 "8. 2026-10-14 증분 갱신" 절 신설 — 57편 기준 방법론 분포, 1,023편 환산 비율
- **tools 갱신**: `other_tools.md`(VOSviewer 편수 갱신, SHAP/LIME·IndoBERT 신규 추가), `netminer.md`(signed network/균형이론 기능 공백 신규 행 추가)
- **핵심 발견**:
  1. **신규 기능 공백**: signed network(부호화 네트워크)/균형이론 — Zhang(2026, Science Advances, graph-tool 개발자 Peixoto 참여) 확인. NetMiner Blockmodel/Community 메뉴는 비부호 네트워크 전제라 미지원
  2. **커스텀 하이브리드 딥러닝 감성모델 확산**: Bourasi·Orgun·Sumy·Zhao 등 4편+ — NetMiner Lab 단일 BERT 모델과의 격차가 좁혀지지 않고 구조적으로 확대되는 신호
  3. **ERGM의 신규 활용 패턴**: Bright — 모형 적합이 아닌 "개입 평가 시뮬레이션"(네트워크 1,000개 생성) 도구로 ERGM 활용. 범죄학 마케팅 소재로 가치
  4. **진성 SNA 비중 재급등(~35%)의 원인은 ingest 게이트 선택효과**: 2026-10-07 증분과는 다른 메커니즘 — 이번 60편은 관련도 스코어링(threshold=3) 통과분만 개별 페이지화된 표본이라 SNA 관련도가 원래 높게 선별됨. 학술 트렌드 변화로 해석하지 않음
  5. **완전 재현 가능 데모 2건 신규 확보**: wu(중국 마약거래 조직, 중심성 4종), fernández(대학 미션성명, Bonacich+QAP+Word Network)
  6. **데이터 품질 플래그**: `unknown_deep_learning_based_cyberbully`·`unknown_semanticbased_approach` 2편이 저자 미표기 + 주제 무관 저널(의약전달지) 게재 — 약탈적 저널 가능성, 다음 lint 시 확인 필요
- **미조치**: 60편 중 1편 편수 카운트 불일치(ingest 로그는 "61편 신규"로 기록했으나 실제 git untracked 개별 파일은 60개 확인 — 원인 미파악, 다음 lint 시 재확인 권장)

---

## [2026-10-14] ingest | raw/sna, raw/applied 신규분 일괄 ingest

- **대상**: `raw/sna/`, `raw/applied/` 전체에서 `batch_ingest.py` 기준 미등록 파일 탐색 (`raw/netminer/`는 이번 작업 제외)
- **raw/sna**: 신규 파일 644개 발견했으나 전부 기존 페이지(321편)·카탈로그에 이미 반영되어 있어 **신규 생성 0건** (제목 슬러그·카탈로그 타이틀 매칭으로 중복 확인). `raw/sna/` 자체는 이미 git에 커밋된 상태였음
- **raw/applied**: 신규(untracked) 파일 518개 중 게이트(SNA/텍스트마이닝 키워드) 탈락 2,532편 제외, 관련도 스코어링(threshold=3) 결과 **개별 페이지 61편 신규 생성**(`pages/papers/applied/`), **카탈로그 6편 추가**(`catalog_2026.md`, 총 64건)
- **번역**: 미포함 (기본 정책 — 번역은 별도 요청 시에만 수행)
- **NetMiner 사례**: 신규 61편 전수 `netminer` 키워드 검색 — 언급 없음. `pages/tools/netminer.md` 갱신 불필요
- **신규 61편 주제 경향**: 감성분석(Sentiment Analysis)·토픽모델링·텍스트 분류 등 NLP 계열이 다수, 네트워크 고유 방법(여론 동학·전파) 소수 — 기존 `sentiment_analysis.md`/`topic_modeling.md`/`llm_nlp.md` 등의 통계(789/963편 기준 전수 집계)와 정합성을 맞추려면 **개별 수치 수정 대신 `/wiki:synthesize`로 전수 재합성 필요** → 이번 ingest에서는 methods/concepts/overview.md 본문 미수정, index.md 통계만 갱신
- **index.md 갱신**: 응용 분야 개별 1,023편·카탈로그 88편, 총 페이지 1,427편으로 통계 정정 (기존 1,861편 표기는 papers 집계 오류로 판단되어 실제 파일 수 기준 재계산)
- **핵심 인사이트**: `raw/sna`는 이미 포화 상태(신규 수집분도 전량 중복) — 다음 수집 주기부터는 `raw/sna` 자동 수집분의 중복률을 먼저 점검할 가치가 있음

---

## [2026-10-07] lint | 편수 불일치 정정 + 후속 확인 메모
- **정정**: `methods/ergm.md`·`saom.md`·`centrality.md`·`community_detection.md`·`topic_modeling.md`의 2026-09-30 보강 절 제목·본문 편수를 실제 총계에 맞춤 (SNA 327→321편, applied 909→907편/신규 120→118편). ergm·saom에는 정정 주석 추가
- **후속 확인 메모 (미처리)**:
  1. 위 5개 보강 절의 *서술 내용*이 신규 페이지에 근거한 것인지 미검증. 정정 주석에 "대부분 기존 318편에 포함된 논문의 재정리"라 적었으나 논문별로 확인한 것은 아님 → 다음 전수 재합성 때 절별 근거 검증
  2. `scripts/synth_findings_sna.md`·`synth_findings_applied.md`(327편·909편 기준 임시 합성 메모)는 위키 페이지가 아닌 작업 중간 산출물 — 삭제 여부 사용자 판단 대기
  3. `pages/tools/netminer.md`·catalog에도 어긋난 편수가 있다는 이전 기록이 있으나 "327편/909편" 패턴 검색으로는 안 잡힘 → 별도 확인 필요

## [2026-10-07] synthesize | 2026-09-22 이후 신규분 증분 합성 (SNA 3편 + applied 174편)

- **대상**: 2026-09-22 마지막 전수 synthesize 이후 신규 생성된 개별 페이지만 — `pages/papers/sna/` 3편(`2026_gao_multilayer_network_analysis`, `2026_hncean_returning_network_findings`, `2026_murraywatt_the_decay_impact`), `pages/papers/applied/` 174편(2026-09-30·2026-10-07 두 차례 ingest 분 합산, git untracked 기준). 기존 789편/318편 본문은 재열람하지 않음
- **탐색**: applied 174편은 병렬 에이전트 4개(각 ~44편)로 초록·frontmatter 수준 판독, sna 3편은 직접 판독. 1편(`2026_jalali_postmodern_physics_hamzah`)은 의사과학/AI생성 난센스 텍스트로 집계 제외
- **methods 갱신**: `sentiment_analysis.md`(+44편, 비중 변화 없음 재확인), `llm_nlp.md`(+29편, 온프레미스 LLM 임상 사례 추가), `topic_modeling.md`(+24편, LDA vs BERTopic 경주 반복 확인), `gnn.md`(+18편, CS 방법론 중심 재확인), `centrality.md`(Hâncean 아트갤러리 환원 사례 추가, Murray-Watters는 기존 미커밋 작업에 이미 반영되어 있던 것 확인), `community_detection.md`(응용 분야 Louvain/Infomap 사례 3건 추가)
- **concepts 갱신**: `multilayer_network.md` — Gao 외(2026) Reddit 다층 네트워크(담론 레이어+행위자 레이어, 레이어 간 상관) 추가
- **tools 갱신**: `other_tools.md` — PyTorch Geometric/DGL, 온프레미스 Llama-3.1/Qwen3, Neo4j 신규 추가
- **insights 갱신**: `applied_method_frequency_2026.md`에 "7. 2026-10-07 증분 갱신" 절 신설 — 174편 기준 방법론 분포 집계, 963편 환산 비율 계산
- **핵심 발견**: 신규 174편에서 진성 SNA 비중이 18%로 789편 기준(~7%)보다 뚜렷이 높게 나타났으나, 동물행동생태학 SNA 논문 군집 등 **특정 ingest 배치의 수집 편향**으로 판단 — 963편 전체 환산 시 8.4~9.1% 수준의 소폭 상승에 그침. "응용 분야는 SNA 심화가 아닌 폭 탐색" 결론은 유지
- **overview.md**: 상단 안내문에 증분 synthesize 완료 명시, Part 2·3 전수 수치(318/789)는 2026-09-22 베이스라인으로 유지하고 각 방법론 페이지의 "2026-10-07 보강" 절로 분리 서술
- **미해결 사항**: 2026-09-30 ingest 직후 누군가 methods(centrality/community_detection/ergm/saom/topic_modeling)·netminer.md·catalog 등에 "327편"·"909편" 기준 증분 작업을 이미 해두었으나 커밋되지 않았고 log.md에도 기록이 없었음 — 해당 수치가 현재 실제 총계(SNA 321편, applied 963편)와 불일치. 이번 작업에서는 그대로 두고 손대지 않았으며, 다음 전수 재합성 시 정합성 정리 필요

## [2026-10-07] ingest | raw/sna/, raw/applied/ 추가 신규분 일괄 인제스트 (raw/netminer/ 제외)
- 대상: 2026-09-30 이후 추가 수집된 raw 파일(sna 525편 중, applied 포함 총 525편이 log.md 기준 신규) — `batch_ingest.py`(--no-translate, 기존 정책 유지) 재실행
- **sna**: 신규 644개 재스캔 → 기존 페이지/카탈로그와 중복 제외, 실질 신규 1편(`2026_gao_multilayer_network_analysis`) 개별 페이지 추가. 카탈로그 변동 없음. 개별 페이지 320→321편
- **applied**: 게이트 탈락 2,113편 → 개별 페이지 60편 신규, catalog_2026 +24편(34→58편). 개별 페이지 907→963편
- NetMiner 언급 여부 확인: 신규 페이지 61편 전수 grep 검색 결과 NetMiner 언급 0건 — `pages/tools/netminer.md` 갱신 불필요
- index.md 통계·목록, overview.md 헤더 갱신. 방법론/개념/overview 전수 재합성(개별 페이지 내용 반영)은 미실시 — 기존 방침대로 `/wiki:synthesize` 별도 실행 필요
- 참고: 직전 2026-09-30 ingest 결과물이 커밋되지 않은 상태로 남아 있었음 — 이번 작업으로 두 세션분이 함께 작업트리에 반영됨 (커밋은 미실행, 필요 시 요청)

## [2026-09-30] ingest | raw/sna/, raw/applied/ 미등록 파일 일괄 인제스트 (raw/netminer/ 제외)
- 대상: `raw/sna/`(689개 중 신규 643개), `raw/applied/`(2,916개) — index.md 미등록분. `raw/netminer/`는 월별 자동수집 전용이라 이번 작업 범위에서 제외
- `batch_ingest.py`(--no-translate 기본값) 실행 — 번역은 별도 요청 시에만 진행(기존 정책 유지)
- **sna**: 신규 643개 중 개별 페이지 대상 225편 산정 → 기존 페이지와 슬러그 중복 223편 제외, 실질 신규 2편(`2026_hncean_returning_network_findings`, `2026_murraywatt_the_decay_impact`). catalog_2026 +2편(21→23편). 개별 페이지 318→320편
- **applied**: 게이트 탈락 1,684편(SNA·넷마이너 알고리즘 키워드 없음) → 개별 페이지 118편 신규(중복 슬러그 8건 제외 실질 순증), catalog_2026 +17편(34→51편). 개별 페이지 789→907편
- NetMiner 언급 여부 확인: 신규 페이지 120편 전수 grep 검색 결과 NetMiner 언급 0건 — `pages/tools/netminer.md` 갱신 불필요
- index.md 통계·목록, overview.md 헤더 갱신(신규분 방법론/도메인 재합성은 미실시 — `/wiki:synthesize` 별도 실행 필요, 안내 문구 추가)
- 미조치 사항: sna 신규 643편 중 개별/카탈로그 어디에도 포함되지 않은 280편은 초록 누락으로 스킵됨(raw 파일 자체 품질 이슈로 추정, 별도 확인 필요)

## [2026-09-22] synthesize | SNA 318편 + 응용분야 789편 전수 재합성 (2026-05-27판 대체)
- 대상: `pages/papers/sna/` 318편 + `pages/papers/applied/` 789편, 총 1,107편 (마지막 synthesize 이후 첫 전체 재합성)
- 탐색: 병렬 에이전트 10개(SNA 3개 × ~106편, applied 7개 × ~113편) 동시 탐색 → 결과 합산
- 합성 작성: 에이전트 2개(SNA 전담 / applied 전담, 파일 소유권 분리로 충돌 방지) + 오케스트레이터가 overview.md·index.md·tools/other_tools.md·log.md 직접 정리
- **신규 생성**: `pages/methods/relational_event_model.md`(REM/RHEM/DyNAM 17편, 2023 Social Networks 특별호 근거), `pages/concepts/egocentric_network_design.md`(에고넷 설계·수집 방법론, SNA 318편 중 단일 최대 클러스터 ~46편)
- **전면 재작성**: `pages/insights/sna_method_frequency.md`, `pages/insights/applied_method_frequency_2026.md`, `pages/insights/applied_domain_venue_2026.md`
- **갱신**: `methods/ergm.md`·`saom.md`·`network_scaleup.md`·`centrality.md`·`community_detection.md`·`bayesian_network_model.md`·`llm_nlp.md`·`sentiment_analysis.md`·`topic_modeling.md`·`semantic_network_analysis.md`, `concepts/mixed_methods.md`, `insights/applied_data_source_2026.md`, `tools/other_tools.md`, `overview.md`(Part 2·3 전면 갱신), `index.md`(통계·Methods·Insights 목록 갱신)
- **netminer.md 대비 정정 2건**: BERTopic(기존 ❌ 기록 → 실제 ✅ Text>BERTopic/BERTrend 지원), BERT 기반 감성분석(기존 ❌ → 실제 ✅ Lab>Sentiment Analysis 7개 언어 지원) — 응용분야 논문 재확인 과정에서 발견
- 핵심 발견:
  1. SNA: ERGM(40)+SAOM(29)+REM(17)=86편(27%)이 "동적·생성적 통계 네트워크 모형" 단일 계열 — 개별 기능이 아닌 계열 전체 공백
  2. SNA: 에고넷 설계·수집 방법론이 46편으로 단일 최대 클러스터. 필요 부품(Ego Network Extract·지표·Hierarchical Clustering·Random Forest)이 이미 NetMiner에 존재 — 워크플로우 문서화만으로 대응 가능한 최고 ROI 기회
  3. SNA: 진짜 GNN 실사용 0/318편 확인(OpenAlex GNN 태그 오탐 10건+ 검증) — GNN은 지원하되 학술 수요 없음을 명확히 분리 서술
  4. 응용: LLM(27%)·감성분석(27%)이 공동 1위로 부상, 진짜 SNA는 7%(50~57편)에 불과 — 유형 C 수집 목적(SNA 심화 아닌 텍스트마이닝 폭넓은 응용 확인)에 부합하는 결과
  5. 응용: 도메인 특화 소형 파인튜닝 모델(ConfliBERT·DEBATE·BERTimbau-LoRA 등)이 범용 LLM 프롬프팅보다 정확도·비용·속도 모두 우위 — 7개 청크 중 4개 이상에서 독립 반복 확인된 강한 근거
  6. 응용: 신규 경쟁 도구 확인 — pyBiblioNet(무료 오픈소스, Biblio Extension 직접 경쟁), Sometrend/TEXTOM(국내 상용, SNA 기능 보유 재확인)
  7. 응용: 보건/정신건강이 최대 응용 분야(18%)인데 NetMiner 침투도 최저 — `lie_quantifying_multidisciplinary`(의료진 협진 네트워크) 등 강력한 데모 후보 확보
- 데이터 품질 이슈 발견(별도 조치 필요, 이번 synthesize에서는 미조치): 응용분야 논문 다수 페이지에 한국어 요약 섹션 인코딩 깨짐(mojibake) — 번역 파이프라인 버그 추정. 중복 논문 3건, 유형 B로 재분류해야 할 순수 이론 논문 다수가 `applied/`에 혼입된 것으로 추정 — 다음 lint 시 확인 필요

## [2026-07-31] ingest | raw/·raw/applied/ 미등록 파일 일괄 인제스트 (전체 마무리)
- 대상: index.md에 미등록된 raw/ 전체 (raw/sna, raw/applied, raw/netminer)
- **sna**: `batch_ingest.py` 실행 → 개별 페이지 7편 신규 (`pages/papers/sna/`), catalog_2026 +1편. 총 개별 페이지 258→318편
- **applied**: `batch_ingest.py --no-translate` 실행 (raw/applied 2,309개 소스, 게이트 탈락 1,264편) → 개별 페이지 107편 신규(중복 슬러그 3건 제외 실질 순증), catalog_2026 +16편. 총 개별 페이지 682→789편
- **netminer**: raw/netminer/ 신규 65개 소스(KCI 35 + OpenAlex 30, `monthly_netminer.py` 자동수집분) 병렬 에이전트 3개로 처리 후 수작업 정합성 검증
  - NetMiner 본문 언급 0건인 13편은 제외 (OpenAlex 키워드 오매칭 — SCHEMA.md 경고 사례와 일치)
  - KCI/OpenAlex 이중 수집된 동일 논문 7쌍은 중복 제거 (한글 KCI 버전 유지)
  - 주제 무관 1건(저자명 모호성 해소 LLM 논문) · 근거 불충분 1건(초록 손상) 삭제
  - 노인학대 뉴스보도 분석 1편은 NetMiner 명시 불확실하나 SNA 방법론(의미연결망+LDA) 근거로 유지, 페이지 내 플래그 처리
  - 최종 순증 38편 → `pages/papers/netminer/` 5편 → 43편
- `index.md` Papers A/B/C 섹션 및 통계 갱신 (총 786 → 1,188페이지), `pages/tools/netminer.md` 사용 사례 카운트 갱신
- raw/ 파일은 전량 읽기만 하고 수정하지 않음
- **주의**: 병렬 에이전트 동시 작업으로 인해 raw/netminer 처리 과정에서 슬러그 중복·오탐 페이지가 발생했으며, 본 항목에서 수작업으로 정합성 검증 후 정리함 — 향후 대량 파일을 여러 에이전트에 분배할 때는 사전에 동일 논문의 중복 소스(KCI vs OpenAlex 등)를 먼저 걸러내는 것이 필요

## [2026-07-31] ingest | raw/netminer 미등록 21개 소스 → 논문 페이지 19편 생성
- 대상: KCI 15편 + OpenAlex 6편(raw/netminer/kci_2026_*, netminer_2026_*)
- 2쌍은 동일 논문의 KCI/OpenAlex 중복 수집본으로 확인되어 1페이지로 병합
  - 영유아교사 연구(An & Nam) — kci_ART003313264 + netminer_koaece31_1_06
  - 청소년 우울 연구(Shin & Jeong) — kci_ART003310230 + netminer_jss_11_1_6
- 2건은 NetMiner 사용 여부가 초록상 확인되지 않아 페이지 내 명시적으로 플래그 처리
  - 노인학대 뉴스보도 분석(Kim) — BIGKinds 도구만 언급
  - 저자명 모호성 해소(Zhang 외, arXiv) — NetMiner 무관 가능성 높음 (OpenAlex 오분류 추정)
  - 수산물 구매행동 비교(Kim & Kim) — 초록 원문 손상으로 확인 불가
- `index.md` A섹션(NetMiner 사용 논문 목록) 및 통계 갱신 (5편 → 24편, 총 767 → 786페이지)

## [2026-05-27] update | applied_domain_venue + applied_data_source 682편 기준 업데이트
- `pages/insights/applied_domain_venue_2026.md` — 379편 → 682편 비례 재추정 (도메인 분포, 언어 분포). 학술지 섹션은 원본 379편 실측 유지
- `pages/insights/applied_data_source_2026.md` — 모든 수치 682편 기준 비례 확장. 저자원 언어 목록에 방글라·카자흐 추가
- 임시 synthesis chunk 파일 (`scripts/synth_chunk_*.txt`) 삭제

## [2026-05-27] ingest + synthesize | raw/applied 2025년 신규 논문 인제스트 및 682편 기준 재합성
- **인제스트**: `batch_ingest.py` 실행 — 2025년 신규 논문 231편 개별 페이지 생성 (2026년 신규 72편 포함, 총 303편 신규)
- **기준 변경**: 379편 → 682편 (2026년 451편 + 2025년 231편, arXiv 제외)
- **탐색 에이전트**: 8개 병렬 에이전트 × 38편 (303편 전체 커버)
- **업데이트 파일**:
  - `pages/insights/applied_method_frequency_2026.md` — 682편 기준 재합성. 감성 분석이 1위로 상승(~253편, 37%), LLM 2위(~234편, 34%). STM·keyATM·NMF 신규 추가. ABSA 급성장(~25편) 확인
  - `overview.md` — Part 3 제목·수치 갱신 (682편)
  - `index.md` — C 섹션 현황 갱신 (682편)
  - `pages/methods/topic_modeling.md` — STM·keyATM 등장 반영, 682편 기준 수치 갱신
  - `pages/methods/sentiment_analysis.md` — 682편 1위로 갱신, 저자원 언어 급증·ABSA 성장 추가
  - `pages/methods/llm_nlp.md` — LoRA/PEFT 경량화·RAG+지식그래프·LLM 에이전트 트렌드 추가
- **핵심 발견**:
  1. 감성 분석이 2025 신규 논문에서 46%로 압도적 1위
  2. BERTopic·STM·keyATM으로 토픽모델링 세분화 가속
  3. LoRA/PEFT 경량 파인튜닝 표준화, 오픈소스 LLM 급부상
  4. NetMiner 추정 사용 (2025_lee 한국 법률 담론), TEXTOM 직접 언급 (2026_yoo K-POP)
  5. 저자원 언어 NLP (인도네시아·아랍어·방글라어 등) 20% 이상 차지

## [2026-05-27] schema | methods 페이지 목적 명시 — 제품 기획 검토 자료
- `SCHEMA.md` — methods/ 폴더 설명 갱신: NetMiner 기능 목록([[pages/tools/netminer]])을 기준으로 ① 신규 기능 후보(❌) ② 기존 기능 개선 근거(⚠️) 두 가지 용도 명시
- `index.md` — Methods 섹션 헤더에 기준선(NetMiner 현재 기능 요약) 및 용도 주석 추가

## [2026-05-27] synthesize | method 페이지 분리 및 텍스트 분류 신규 추가
- `pages/methods/ml_gnn.md` → 삭제 후 3개로 분리
  - `pages/methods/ml.md` (신규) — 전통 ML / 앙상블: SVM·RF·XGBoost·K-Means·SHAP/XAI
  - `pages/methods/gnn.md` (신규) — GNN: GCN·GAT·지식 그래프·GraphRAG, SNA 학술지 사용 사례 포함
  - `pages/methods/text_classification.md` (신규) — 텍스트 분류 (~76편, 20%, 응용 3위): BERT 파인튜닝·제로샷·앙상블
- `index.md`, `applied_method_frequency_2026.md`, `topic_modeling.md`, `bayesian_network_model.md` 링크 갱신

## [2026-05-27] synthesize | applied 논문 arXiv 제외 후 재합성 완료 — 379편 전체
- arXiv 제외 후 남은 개별 페이지 379편, 탐색 에이전트 10개 × 38편 (chunks 0–9, 100% 커버)
- **업데이트 파일**:
  - `pages/insights/applied_method_frequency_2026.md` — 분석 기준 379편으로 갱신, 수치 재조정 (LLM 40%·감성 30%·토픽 18%·SNA 10%)
  - `pages/insights/applied_domain_venue_2026.md` — 379편, arXiv 게재 학술지 행 제거, 분야별 편수 재조정
  - `pages/insights/applied_data_source_2026.md` — 379편 기준 데이터 소스 비율 재조정
  - `overview.md` — Part 3 제목·수치 갱신 (100% 커버, arXiv 제외)
  - `index.md` — applied 현황 379편으로 갱신
- 주요 발견 (청크 8·9 추가 반영): 토픽+감성 복합, GNN/RAG 적용 확산, 도메인: 법률·의료·관광 등 다양화 확인

## [2026-05-27] synthesize | sna 데이터 소스 insight 추가
- `pages/insights/sna_data_source.md` (신규) — 설문/에고넷 56%, 종단 28%, 표준 데이터셋(Add Health·SSND·BHPS 등), 응용 분야 데이터 소스와 대조 테이블

## [2026-05-27] synthesize | applied 신규 method·insight 페이지 추가
- `pages/methods/llm_nlp.md` (신규) — LLM/GPT 활용, 응용 분야 1위(~186편), ❌ NetMiner
- `pages/methods/sentiment_analysis.md` (신규) — 감성 분석, 응용 분야 2위(~140편), ⚠️ 부분 지원, ABSA 심화 포함
- `pages/insights/applied_data_source_2026.md` (신규) — Twitter/X 1위, 소셜미디어 40%·뉴스 16%·리뷰 14%, 다국어 NLP 15–20%, 고객 세그먼트별 데이터 소스 정리

## [2026-05-27] synthesize | applied 응용 분야 논문 지식 합성 완료 — 592편
- 대상: `pages/papers/applied/` 개별 페이지 459편 (에이전트 8개 × 74편 = 592편 분석)
- 에이전트 실패: chunks 8–9 (141편, 세션 한도) — 약 80% 커버
- **생성/업데이트 파일**:
  - `pages/insights/applied_domain_venue_2026.md` (신규) — 7개 분야 분포, 261개 학술지
  - `pages/insights/applied_method_frequency_2026.md` (신규) — LLM 31%·감성 24%·토픽 14%·SNA 8%
  - `pages/methods/topic_modeling.md` — 응용 분야 섹션 추가 (LDA 55편, BERTopic 18편, 조합 패턴)
  - `pages/methods/ml_gnn.md` — 응용 분야 섹션 추가 (Transformer 120편, GPT 60편, XGBoost 30편)
  - `pages/methods/semantic_network_analysis.md` — 응용 분야 섹션 추가 (공출현 18편, Textom 경쟁 언급)
  - `pages/concepts/mixed_methods.md` — 패턴 6 (토픽+감성), 패턴 7 (텍스트+SNA) 추가
  - `pages/tools/other_tools.md` — BERTopic, Textom, Sometrend, Orange, Hugging Face 추가
  - `overview.md` — Part 3 (응용 분야 인사이트 + NetMiner 시사점) 추가
- 핵심 발견: LLM 방법론 도구화 급증, BERTopic이 LDA 잠식 중, SNA+텍스트 결합이 응용 분야 표준 패턴, Textom이 국내 직접 경쟁자로 부상

## [2026-05-26] update | 폴더 구조 재편 — raw/sna/, pages/papers/sna/ 신설
- `raw/*.md` (667개) → `raw/sna/` 이동
- `pages/papers/*.md` (265개, 개별 258편 + catalog 7개) → `pages/papers/sna/` 이동
- wikilink 업데이트: index.md + concepts 4개 + methods 9개 + tools 1개 (총 17개 파일)
- SCHEMA.md, overview.md 경로 표기 갱신
- batch_ingest.py 경로 상수 갱신 (RAW_DIR, PAGES_DIR → sna/ 하위)

## [2026-05-26] ingest | 응용 분야 논문 (유형 C) 최초 인제스트 — 973편
- 수집 스크립트: `fetch_applied.py` — "social network" + "text analysis" 키워드, cited_by_count:desc 정렬, 쿼리당 최대 500건
- 수집 기간: 2026년 (--from-date 2026-01-01 --to-date 2026-12-31)
- 제외 학술지: Social Networks / Network Science / Connections (유형 B와 중복 방지)
- 인제스트 결과: 개별 페이지 733편 (`pages/papers/applied/`) + 카탈로그 240편 (`pages/papers/applied/catalog_2026.md`)
- 번역: 미적용 (--no-translate). 필요 시 소급 번역 가능
- 총 페이지: 291 → 1,025

> append-only. 인제스트·쿼리·린트 이력.
> 파싱 팁: `grep "^## \[" log.md | tail -10` → 최근 10개 항목

## [2026-05-26] lint | 위키 건강 점검
- 총 페이지: 291 (papers 270 · concepts 6 · methods 11 · insights 2 · tools 2)
- 깨진 링크: 0개 ✅
- 고아 페이지: 0개 ✅
- index.md 누락: 0개 ✅
- 링크 부족(2개 미만): 0개 ✅
- 수정: social_network_analysis.md가 methods/에 잘못 생성 → concepts/으로 이동
- 수정: overview.md 메타데이터 "370편" → "635편", index.md 통계 291로 갱신

## [2026-05-26] update | methods/ 페이지 전면 재구성 — 유형 B(OpenAlex SNA 학술지) 기반

**작업 내용**:
- 기존 3개 페이지 유형 B 논문으로 보강 (centrality, topic_modeling, semantic_network_analysis)
  - 유형 A(netminer/) 참조만 있던 내용 → 유형 B 논문 실제 사용 패턴으로 교체/보완
  - 각 페이지에 YAML frontmatter(netminer_support 포함) 추가
- 신규 8개 페이지 생성:
  - ergm.md (26편, 3위) — STERGM·ergmito·Bayesian 변형 포함
  - saom.md (18편, 7위) — 종단 공진화, NetMiner 이탈 요인
  - longitudinal_network.md (30편, 2위) — TERGM·REM·시간 그래프
  - community_detection.md (11편, 공동10위) — 모듈성·블록모델·코어-퍼리퍼리
  - bayesian_network_model.md (14편, 9위) — LPCM·LSPCM·MCMC
  - diffusion_propagation.md (11편, 공동10위) — SIR·면역화·WIP 중심성
  - ml_gnn.md (15편, 8위) — 링크 예측·신경망·그래프 임베딩
  - network_scaleup.md (7편, 13위) — NSUM·ARD·RDS
- index.md Methods 섹션 업데이트 (3개 → 11개), 통계 수치 갱신 (283 → 294)
- 각 페이지: 2–5편 유형 B 논문 실제 사용 맥락 반영

## [2026-05-26] update | 폴더 구조 재편 — concepts/methods/insights 분리
- concepts/ (연구 설계 패턴): social_network_analysis, personal_network, causal_inference_networks, multilayer_network, mixed_methods, systematic_literature_review
- methods/ (구체적 분석 기법): centrality, topic_modeling, semantic_network_analysis
- insights/ (신규, 쿼리 결과): sna_method_frequency, netminer_trend_insight
- wikilink 60개 파일 일괄 업데이트, index.md·SCHEMA.md 구조 문서 갱신

## [2026-05-26] update | 개별 페이지 244편 한국어 요약 소급 적용 완료
- 대상: pages/papers/*.md 개별 페이지 전체 (netminer/ 서브디렉토리 제외)
- 추가 내용: **제목(한글)**, ## 한국어 요약 (연구질문·방법론·주요결과), ## 초록 (원문)
- 처리 현황: 2020(37) + 2021(28) + 2022-2023(23) + 2024(33) + 2025(25) + 2026(14) = 160편 신규 추가
  - 나머지 84편: 이미 한국어 내용 있어 건너뜀
- 최종 확인: 미번역 페이지 0편

## [2026-05-26] update | 2024_*.md 33편 한국어 요약 섹션 일괄 추가
- pages/papers/2024_*.md 34개 파일 탐색, 1편(netminer/2024_jang_*) 건너뜀 (이미 한국어 작성)
- 나머지 33편에 **제목(한글)**, ## 한국어 요약 (연구질문·방법론·주요결과), ## 초록 (원문) 삽입
- 초록 비공개 3편(ceoldo, lai, neal_stopping)은 제목+키워드 기반 추정 번역 적용

## [2026-05-26] update | batch_ingest.py 한국어 번역 기능 추가
- 개별 페이지 생성 시 Claude Haiku API 호출 → 제목(한글), 연구질문, 방법론, 주요결과 번역
- 생성 페이지 포맷: 한국어 요약 섹션 + 초록(원문) 구조로 변경
- `--no-translate` 플래그로 번역 건너뜀 가능
- ingest_applied() 에도 동일 번역 적용
- SCHEMA.md, ingest/SKILL.md 규칙 업데이트

## [2026-05-26] query | 수집 학술지 3종 확인 — ISSN 목록 갱신
- ISSN 2050-1250 = Network Science (Cambridge UP), raw/nws_* 188편
- ISSN 2816-4245 = Connections (INSNA, De Gruyter, Diamond OA), raw/connections_2025_000* 5편
- index.md, overview.md 수집 학술지 항목에 3종 모두 명시 (Social Networks + Network Science + Connections)

## [2026-05-26] update | 분석 오류 패턴 문서화 — SCHEMA.md, index.md
- 검증된 오류 3가지를 SCHEMA.md "분석 시 반드시 지켜야 할 규칙" 섹션에 추가
- index.md Overview 하단에 요약 주의사항 추가
- 오류 내용: ① OpenAlex 태그 오신뢰, ② NetMiner 지원=학술수요 오판, ③ 논문주제→기능 잘못 연결(데이터수집→Extension)

## [2026-05-26] ingest + update | Network Science 2026 신규 9편 처리 및 인사이트 반영
- 신규 raw 파일 9편 발견 (Network Science 학술지, nws_2026/nws_2025)
- 개별 페이지 5편 생성, 카탈로그 4편 추가 (catalog_2026 → 16편)
- 수집 학술지 확장: Social Networks → Social Networks + Network Science
- 신규 인사이트:
  - 텍스트→가치 네트워크 파이프라인 (Almquist 2026, climate talks)
  - 중심성 기반 immunization in multiplex (Asil 2026)
  - 코어-퍼리퍼리 탐지 알고리즘 (Yanchenko 2026)
- 업데이트: sna_method_frequency (181편), netminer_trend_insight (신규 섹션 2개), overview/index 수치 갱신
- batch_ingest.py UnicodeEncodeError 수정 (em-dash → -)

## [2026-05-26] update | 2020 논문 인사이트 반영 — 빈도 분석·트렌드·우선순위 갱신
- sna_method_frequency.md: 분석 범위 2020–2026 (176편)으로 확대, 순위 재계산
  - 종단/동적 30편으로 2위 상승, ERGM 26편 3위, 데이터수집방법론 10편 신규 진입
- overview.md: Part2 데이터 갱신, 트렌드 #6(데이터수집방법론) 신규 추가, 우선순위표 갱신
- netminer_trend_insight.md: 우선순위표에 "데이터수집 Extension 홍보" 즉시 항목 추가
- 핵심 신규 발견: 데이터 수집 방법론이 2020년 독자 연구 흐름 — NetMiner Extension과 직결

## [2026-05-26] update | 응용 분야 논문 유형 C 체계 추가
- SCHEMA.md: 논문 소스 3유형 표 및 폴더 구조 업데이트 (A·B 기존 + C 신규)
- index.md: Section C 플레이스홀더 추가 (raw/applied/ → pages/papers/applied/)
- overview.md: 소스 구성 표에 C열 추가
- batch_ingest.py: ingest_applied() 함수 추가 — applied/ 전량 개별 페이지, 점수 임계값 없음

## [2026-05-26] ingest | Social Networks 2020 + 2021–2025 추가분 (OpenAlex 신규 127편+)
- 신규 처리: 2020 논문 127편 + 2021–2025 미처리분 추가
- 개별 페이지 119개 신규 생성 (2020: 37편, 2021–2025 추가분 포함)
- 카탈로그 업데이트: 2020 신규(85편) + 2021~2025 각 추가
- 최종 현황: 개별 페이지 253편, 카탈로그 7개(373편), 총 626편 (2020–2026)

## [2026-05-26] update | overview·index 인사이트 전면 반영
- overview.md: 방법론 빈도 표에 GNN 실사용 ≈ 0 비고 추가, BERTopic 0건 명시, ERGM 홍보 1순위 강조, 트렌드 #6(GNN·BERTopic 미래선점) 신규 추가
- index.md: topic_modeling·netminer_trend_insight·netminer 설명 갱신, 통계 수치 정확화 (147+ → 159)

## [2026-05-26] update | NetMiner PDF 논문 페이지 분리 — pages/papers/netminer/ 서브디렉토리
- pages/papers/ 내 PDF 기반 5편을 pages/papers/netminer/ 로 이동
- 참조 파일 11개 wikilink 전체 업데이트 (index, overview, concepts 4개, methods 2개, tools 2개, papers 1개)
- raw/netminer/ 구조와 대칭

## [2026-05-26] update | 논문 유형 A/B 분리 — index.md, overview.md 재구성
- index.md: A(NetMiner 사용 논문 PDF 5편) / B(학계 트렌드 OpenAlex 370편) 명확히 분리
- overview.md: Part 1(PDF 기반 인사이트) / Part 2(OpenAlex 트렌드 인사이트)로 재구성

## [2026-05-25] update | NetMiner 메뉴 반영 및 인사이트 재정리
- netminer.md: 전체 기능 메뉴 정확히 업데이트 (ERGM·GNN·BERTopic·Two-Mode 등 확인)
- concepts/netminer_trend_insight.md 신규 생성: 트렌드-기능 대조, 홍보 기회·공백·우선순위

## [2026-05-25] query | 가장 자주 사용된 SNA 방법론
- 참조 페이지: 139편 (개별 페이지 전체)
- 신규 저장 페이지: pages/insights/sna_method_frequency.md
- 핵심 결과: 1위 에고중심(30), 2위 ERGM·종단(22), 4위 중심성·토픽모델링·다층(19)

## [2026-05-25] ingest | Social Networks 2021–2025 + 2026 추가분 (OpenAlex 351편)
- 관련도 점수 3 이상: 개별 페이지 120편 생성 (pages/papers/)
- 관련도 하위: 연도별 카탈로그 6개 생성 (catalog_2021~2026.md, 총 231편)
- 핵심 선별 기준: 텍스트마이닝, 복합 방법론, 신규 SNA 방법론, 소프트웨어·도구

## [2026-05-25] update | tools/other_tools 신규 생성
- 이 위키 논문에서 실제 사용된 도구(R, SPSS MODELER, RSiena) + 비교 대상 도구(Gephi, UCINET, Python, VOSviewer) 정리
- NetMiner 포지셔닝 요약 표 포함

## [2026-05-25] update | methods/mixed_methods, tools/netminer 보완
- mixed_methods.md: 패턴 5 추가 (정성+네트워크 동학 — Kreager 2026 기반)
- netminer.md: 기능 개발 방향 인사이트 섹션 추가 (2026 트렌드 기반), 위키링크 경로 수정

## [2026-05-25] ingest | Social Networks 학술지 2026 (OpenAlex 14편)
- 처리 파일: scripts/fetch_openalex.py → raw/2026_openalex_*.md (14건)
- 생성 페이지: 14개 (논문) + 3개 (개념: personal_network, causal_inference_networks, multilayer_network)
- 업데이트 페이지: index.md, overview.md
- 핵심 인사이트: 2026년 Social Networks 학술지 주요 흐름 — 인과 추론×네트워크, 퍼스널 네트워크 다양화, 다층 네트워크로의 전환, 네트워크×공간 통합

---

## [2026-05-25] init | 위키 초기화

- SCHEMA.md, index.md, log.md, overview.md 생성
- 폴더 구조: raw/, pages/concepts, papers, methods, tools

---

## [2026-05-25] ingest | 5개 PDF 일괄 인제스트

**처리 소스**:
1. Jang & Nemoto (2024) — 행복 영향 요인: 토픽모델링 + 신경망
2. Morashti 외 (2022) — 지속가능 패키징 SLR
3. Park 외 (2022) — 디지털 헬스케어 생태계 네트워크 분석
4. Jeon & Park (2022) — 노인 소셜 네트워크와 건강
5. 강윤지 외 (2021) — 광고홍보학 CSR 연구동향 (의미연결망 + 토픽)

**생성 페이지 (12개)**:
- papers/: 5개 논문 요약 페이지
- concepts/: social_network_analysis, centrality, topic_modeling, semantic_network_analysis
- methods/: mixed_methods, systematic_literature_review
- tools/: netminer

**핵심 인사이트**:
- 5개 논문 전부 NetMiner 사용 → 인용 사례 마케팅 자료로 활용 가능
- 의미연결망 + 토픽모델링 복합 방법론이 연구동향 분석의 표준 패턴으로 부상
