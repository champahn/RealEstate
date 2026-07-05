# 실패 및 실수를 최소화하는 부동산시행 실무 매뉴얼 제작 종합 실행 플랜

작성일: 2026-07-05
상태: 승인 대기
대상 원본: `<LOCAL_ORIGINAL_DIR>/부동산개발_시스템_아파트시행매뉴얼_v1.0.docx`

## 0. 결론

기존 v1.0 매뉴얼은 아파트 시행의 8 Phase 구조, Gate, PF, 책임준공, 유치권, QS 분쟁, 분양, 준공정산의 기본 골격이 이미 좋다. 다만 목표가 단순 절차서가 아니라 "실패 및 실수 최소화"라면 v1.0을 그대로 늘리는 방식은 부족하다. G002 실패사례 DB와 G003 v1.0 정밀감사 결과를 기준으로, v1.1 작업은 다음 방향으로 진행해야 한다.

1. 원본 v1.0은 보존하고 작업본만 만든다.
2. 기존 8 Phase는 유지하되 각 단계에 `Owner / Trigger / Threshold / Evidence / Stop-or-Approve / Training Scenario`를 붙인다.
3. 누락된 운영축인 조직/RACI, 세무·회계·SPC, 데이터룸·개인정보, 개발업 컴플라이언스, 교육훈련을 독립 장으로 신설한다.
4. PF와 법령 부록은 2026년 이후 제도·판례·정책 변화 추적 구조가 없으므로 최신성 tracker와 연결한다.
5. 실패사례 DB는 부록이 아니라 매뉴얼 본문 Gate와 교육훈련에 연결되는 운영 DB로 승격한다.

승인 전에는 매뉴얼 본문을 편집하지 않는다. 이 문서는 후속 매뉴얼 제작을 위한 실행 플랜이며, 승인 후에만 작업본 DOCX/MD를 생성한다.

## 1. 증거 입력

이 플랜은 다음 산출물을 근거로 한다.

| 구분 | 경로 | 플랜 반영 방식 |
| --- | --- | --- |
| 원본 보존 백업 | `<LOCAL_BACKUP_DIR>/부동산개발_시스템_아파트시행매뉴얼_v1.0_ORIGINAL_20260705.docx` | 원본 v1.0 preservation workflow의 기준 파일 |
| 실패사례 DB | `<REPO_ROOT>/failure_case_db_v0.1.jsonl` | 12개 core-axis 보강 workstream의 근거 |
| 실패사례 종합 | `<REPO_ROOT>/SYNTHESIS.md` | 통제 stack과 다음 추가 장 도출 |
| v1.0 추출본 | `<REPO_ROOT>/manual_v1_extracted.md` | 기존 문단/표 위치 기준 |
| v1.0 구조 JSON | `<REPO_ROOT>/manual_v1_structure.json` | 197개 문단, 75개 표, 61개 heading 대조 |
| Obsidian 인벤토리 | `<REPO_ROOT>/obsidian_inventory.md` | 현재본 및 백업본 위키 차이/출처 확인 |
| v1.0 갭 감사 | `<REPO_ROOT>/manual_v1_gap_audit.md` | MISSING/PARTIAL/OUTDATED 판단 기준 |
| v1.0 갭 매트릭스 | `<REPO_ROOT>/manual_v1_gap_matrix.json` | G004 coverage validation 기준 |
| blind spot 재점검 | `<REPO_ROOT>/blind_spot_recheck_addendum.md` | G003-BS-A~D 반영 |
| insane-search 재시도 보강 | `<REPO_ROOT>/insane_search_retry_addendum.md` | aside-browser 실패 지점 중 국토부 `제2차 부동산서비스산업 진흥 기본계획` 공식 페이지/PDF 재검증 완료 |
| 원본 보존 감사 | `<REPO_ROOT>/source_preservation_audit.md` | 최종 보존 검증 기준 |

주의: `SYNTHESIS.md`는 실패 DB를 64건으로 표현하지만 실제 `failure_case_db_v0.1.jsonl`과 G002/G003 검증 기준은 63건이다. 이 63-vs-64 count discrepancy는 후속 작업 Phase 1에서 정정하거나 누락 row 여부를 재확인한다.

## 2. 원본 v1.0 Preservation Workflow

후속 작업의 첫 단계는 원본 보존이다. 기존 원본은 이미 백업되었고 SHA256도 동일하게 검증되었다.

| 항목 | 기준 |
| --- | --- |
| 원본 SHA256 | `97295f7b7b25f2d100ef8202a5b88176fd1c31465b732591f6acce6ee9cbad20` |
| 백업 SHA256 | `97295f7b7b25f2d100ef8202a5b88176fd1c31465b732591f6acce6ee9cbad20` |
| 백업 mode | `0o500`, owner write bit 없음 |
| 후속 편집 대상 | 원본 DOCX가 아니라 별도 작업본 |

승인 후 작업 원칙:

1. `부동산개발_시스템_아파트시행매뉴얼_v1.1_WORKING_YYYYMMDD.docx`를 별도 생성한다.
2. 원본 v1.0과 작업본 v1.1의 SHA256, size, mtime을 `version_change_log.md`에 기록한다.
3. 각 보강 단위마다 변경 요약, 근거 source, 검증 결과를 남긴다.
4. 본문 편집 후에는 원본 v1.0, 원본 백업, Obsidian source 파일의 hash/mtime을 재검증한다.
5. 작업본 확정 전에는 `v1.1_DRAFT`, 승인 후에는 `v1.1_APPROVED`로 명명한다.

## 3. Target Deliverables

승인 후 최종 산출물은 다음 6종을 목표로 한다.

| ID | 산출물 | 설명 |
| --- | --- | --- |
| D1 | v1.1 작업본 DOCX | v1.0을 보존한 별도 매뉴얼 작업본 |
| D2 | v1.1 Markdown 추출본 | diff, 리뷰, 검색, 후속 자동화용 |
| D3 | 실패사례 DB v0.2 | G002 63건 정규화, 64건 표기 불일치 정정, 교육 시나리오 연결 |
| D4 | Gate Control Pack | 각 Phase별 Owner/Trigger/Threshold/Evidence/Stop-or-Approve |
| D5 | Template Pack | VDR index, PF exposure map, cash waterfall, tax memo, RACI, training drill 등 |
| D6 | QA Evidence Pack | 원본 보존, coverage matrix, claim ledger, 최신성 tracker, reviewer notes |

## 4. 12 Core-Axis Reinforcement Workstreams

아래 표가 이 플랜의 핵심 coverage matrix다. 모든 MISSING/OUTDATED/PARTIAL core-axis gap은 named workstream으로 배정한다.

| Axis | G003 상태 | Workstream | 주요 추가 내용 | 연결 위치 |
| --- | --- | --- | --- | --- |
| PF | OUTDATED | WS-01 PF 자본구조·보증의존도 최신화 | 자기자본 5/10/15/20% tracker, 브릿지론→본PF 전환성 60/90일 점검, 보증총량 exposure map, repayment source classification, cash waterfall | Phase 3, Phase 5, Appendix D |
| 분양 | PARTIAL | WS-02 분양광고·HUG·환급 SOP | 광고문구 법무승인, 미확정 개발계획 disclaimer, HUG 사고 SOP, 계약해제·환급·재분양 decision tree, P50~P75 실거래가 연결 | Phase 3, Phase 7, Phase 8 |
| 토지 | PARTIAL | WS-03 토지 DD Red-Flag Pack | 유치권·분묘·문화재·접도·토양오염·지장물별 stop condition, 매도인/counterparty DD, 잔금집행 evidence checklist | Phase 1, Phase 2 |
| 인허가 | PARTIAL | WS-04 인허가·민원 Stakeholder Pack | stakeholder map, 주민반대 issue log, 도시계획위원회 쟁점표, 공람 전 Q&A, 장기보류 금융비용 trigger | Phase 1, Phase 4, Gate 2/3 |
| 시공 | PARTIAL | WS-05 공사비·시공사·하도급 통제 | 공사비 claim ledger, 독립 QS trigger, 하도급 DD, 공정률 hold-point, step-in/default 절차 | Phase 5, Phase 6, Phase 8 |
| 법률 | PARTIAL | WS-06 계약·판례·분쟁 SOP | 계약특약 library, 유치권/책준/분양광고/환급 판례 SOP, 법무 signoff log, 법령 최신성 tracker | Phase 2, 4, 5, 7, Appendix D |
| 조직 | MISSING | WS-07 조직/RACI·승인권한 | RACI, 투자심의, 리스크위원회, 변경승인권한, key-person contingency, 인수인계 checklist | PART 1, all Gates |
| 세무·회계·SPC | MISSING | WS-08 세무·회계·SPC·자금통제 | 취득세 taxonomy, VAT 안분 worksheet, SPC 설립/계좌/자금집행, 계약변경 tax memo, closing tax checklist | Phase 2, 3, 5, 8 |
| 데이터룸·문서관리 | MISSING | WS-09 VDR·개인정보·증거보존 | VDR folder taxonomy, 접근권한표, 개인정보 inventory, 다운로드 로그, 72시간 신고 tabletop, 보존기한 | All Phases, Appendix A |
| 개발업 컴플라이언스 | MISSING | WS-10 부동산개발업 컴플라이언스 | 등록요건, 사업실적보고 calendar, 전문인력 roster, 사무실/변경보고, evidence binder | PART 1, compliance appendix |
| 교육훈련 | MISSING | WS-11 실패사례 기반 교육훈련 | onboarding syllabus, Gate drill, red-team review, 실패사례 case card, 역할별 check ride, 분기 회고 | PART 1, every Phase end |
| 준공 후 정산 | PARTIAL | WS-12 준공·하자·미분양 Exit | defect triage, reserve policy, 환급 SLA, 미분양 보유/임대/벌크매각 decision tree, 하자 재교육 | Phase 7, Phase 8 |

## 5. Phase-by-Phase Rewrite Plan

기존 v1.0의 8 Phase는 유지한다. 다만 각 Phase 끝에 "실패방지 Control Box"를 추가한다.

### PART 1. 시스템 아키텍처

보강 목표:

- 단순 3계층 구조를 운영 시스템으로 전환한다.
- 원본/작업본/승인본 version governance를 추가한다.
- 리스크 DB 운영 방식과 교육훈련 연결 방식을 명시한다.
- RACI와 Gate approver를 별도 표로 둔다.

추가 산출물:

- `version_change_log.md`
- `source_preservation_manifest.md`
- `RACI_matrix.xlsx 또는 md`
- `risk_db_operating_rule.md`

### Phase 1. 사업기획 및 토지 발굴

기존 강점:

- 입지 분석, 예비 사업수지, 토지 발굴 채널, Gate 0이 잘 구성되어 있다.

보강 내용:

- 사업 진입 전 PF 제도 변화와 자기자본 ratio 예비 검토.
- 초기사업성에 P50~P75 실거래가 기준을 연결.
- stakeholder map과 민원 예상 이슈를 초기부터 작성.
- 환경·지반·재난·보험 preliminary red flag를 추가.

Control Box:

- Owner: 개발PM, 재무, 법무
- Trigger: 후보지 검토 착수
- Threshold: 토지비 30% 초과, 자기자본 계획 미확정, P75 초과 분양가 가정, 민원 high-risk
- Evidence: 실거래가 산정표, 토지이용계획, stakeholder map, 예비 PF memo
- Stop-or-Approve: 대표+재무+법무 승인 전 LOI/계약금 집행 금지

### Phase 2. 토지 확보 및 실사

기존 강점:

- 등기부, 토지이용규제, 실사, 계약특약이 있다.

보강 내용:

- 유치권, 분묘, 문화재, 접도, 토양오염, 지중장애물 각각을 stop condition으로 분리.
- 매도인/counterparty DD와 잔금집행 evidence pack 추가.
- 토지거래허가, 농지, 가압류, 가등기, 지상권 등 권리별 법무의견서 필수화.

Control Box:

- Owner: 개발PM, 법무, 외부 법무법인
- Trigger: 계약서 초안 수령, 중도금/잔금 지급 전
- Threshold: 권리하자 미해소, 지장물 비용 미반영, 법무의견 미완료
- Evidence: title opinion, red-flag checklist, 잔금집행 checklist
- Stop-or-Approve: red flag 미해소 시 잔금 지급 금지

### Phase 3. 사업타당성 분석

기존 강점:

- Best/Base/Worst 민감도, 기부채납 buffer, 공기 지연, 물가변동 예비비가 있다.

보강 내용:

- 실거래가 P50~P75 분양가 산정 도구를 공식 입력으로 연결.
- 세무·회계·SPC 구조, 취득세/VAT/법인세, 자금집행 계좌를 수지표에 반영.
- PF 자기자본·보증의존도·cash waterfall을 사업성 Gate에 편입.
- G002 실패사례의 root cause를 시나리오 변수로 반영.

Control Box:

- Owner: 재무, 회계/세무 자문, 개발PM
- Trigger: 정밀 사업수지 확정 전
- Threshold: Worst Case 이익률 음수, BEP 분양률 80% 초과, P75 초과 분양가, equity funded ratio 미달
- Evidence: 사업수지표, P50/P75 table, tax memo, PF structure memo
- Stop-or-Approve: 투자심의 재상정

### Phase 4. 인허가

기존 강점:

- 프로세스와 설계사무소 선정 기준, 심의 대응이 있다.

보강 내용:

- 도시계획위원회 쟁점표와 주민반대 대응 Q&A pack 추가.
- 공람 전 커뮤니케이션 전략, 민원 issue log, 대안안 관리대장 추가.
- 인허가 지연 시 금융비용 재산정 trigger를 PF 계획과 연결.

Control Box:

- Owner: 개발PM, 설계사, 인허가 대행, 법무
- Trigger: 심의 접수 전, 반려/보류 통보 즉시
- Threshold: 보류 2회 이상, 주요 민원 unresolved, 지연 60일 초과
- Evidence: 회의록, 쟁점표, Q&A pack, 대안안 비교표
- Stop-or-Approve: 금융비용 재산정 없이 PF 착수 금지

### Phase 5. PF 자금조달

기존 강점:

- PF 구조, 책임준공형 관리형 토지신탁, 책임준공 기한, 출구전략, 분양보증이 있다.

보강 내용:

- 2026~2027 PF 제도 변화 tracker.
- 자기자본 ratio, 보증총량, sponsor/project exposure map.
- 브릿지론 만기 90/60/30일 점검과 본PF 전환 실패 action ladder.
- 대주단 EOD, 신탁 waterfall, repayment source classification.

Control Box:

- Owner: CFO/재무책임자, 법무, 대표
- Trigger: 브릿지론 만기 90일 전, 본PF term sheet 수령 전, 보증 추가 요청
- Threshold: equity 미납입, 본PF 조건 미확정, DSCR 미달, 보증총량 상한 초과
- Evidence: exposure map, cash waterfall, term sheet, EOD review memo
- Stop-or-Approve: 리스크위원회 승인 전 신규 보증/차입 금지

### Phase 6. 시공 관리

기존 강점:

- 유치권 방어, QS 분쟁, 중대재해, 설계변경 프로세스가 있다.

보강 내용:

- 공사비 claim ledger와 증빙서류 표준화.
- 시공사·하도급업체 counterparty DD.
- 공정률 30/50/70/90% hold-point와 특별승인 기준.
- step-in/default 절차와 대체 시공사 후보 pool 관리.

Control Box:

- Owner: CM, 개발PM, 법무, 재무
- Trigger: 증액 요구, 공기 지연, 기성 mismatch, 하도급 미지급 징후
- Threshold: 도급액 5% 이상 증액, 공정 지연 30일 초과, 하도급 체불
- Evidence: claim ledger, QS report, 하도급 지급확인, 공정률 report
- Stop-or-Approve: 변경승인 전 시공 착수 금지

### Phase 7. 분양 및 마케팅

기존 강점:

- 분양 시점, 분양가 산정, HUG, 미분양 대응이 있다.

보강 내용:

- 광고문구 법무승인 workflow.
- 미확정 개발계획 disclaimer와 증빙보존.
- 계약해제, 환급, 재분양, 할인분양 의사결정 tree.
- 분양대행사 성과/민원/허위광고 리스크 관리.

Control Box:

- Owner: 마케팅, 법무, 재무
- Trigger: 광고문구 확정 전, 입주자모집공고 전, 분양률 70/50% 미만
- Threshold: 법무 미승인 문구, HUG 기준 미확인, PF EOD 분양률 조건 근접
- Evidence: legal signoff, 광고 evidence binder, 분양률 dashboard
- Stop-or-Approve: 법무승인 전 광고/모집공고 금지

### Phase 8. 준공 및 정산

기존 강점:

- 사용검사, 입주, PF 상환, 최종 정산, 하자 관리가 있다.

보강 내용:

- defect triage, reserve policy, 반복하자 재교육.
- 환급 SLA와 잔금미납 대응.
- 미분양 보유/임대/벌크매각 exit decision tree.
- 세무 closeout, 법인세·VAT·취득세 사후 조정.

Control Box:

- Owner: 재무, CS, 법무, 세무
- Trigger: 사용검사 신청 전, 입주율 90% 미달, 하자 claim 접수
- Threshold: 잔금미납률 초과, 하자 high-severity, 미분양 장기화
- Evidence: closeout checklist, reserve calculation, defect log, tax closing memo
- Stop-or-Approve: PF 상환·분양보증 해지 전 정산 검증 필수

## 6. Detailed Added-Content Inventory

승인 후 본문 또는 부록에 추가할 상세 내역이다.

| 신규/보강 항목 | 형식 | 포함 필드 |
| --- | --- | --- |
| Version Governance | 본문 + 부록 | 원본, 작업본, 승인본, SHA256, diff, 승인 로그 |
| Failure Case DB Operating Rule | 본문 + DB schema | case_id, phase, failure_mode, root_cause, early_warning, control_to_add, training_scenario |
| Gate Control Sheet | Phase별 표 | Owner, Trigger, Threshold, Evidence, Stop-or-Approve, Escalation |
| PF Exposure Map | 템플릿 | 차주, 보증인, 사업장, 만기, DSCR, LTV, repayment source |
| Cash Waterfall | 템플릿 | 분양수입, 에스크로, 선순위, 후순위, 신탁, 비용 지급순서 |
| P50/P75 Pricing Pack | 템플릿 | 실거래가 source, P25/P50/P75/P90, 적용 분양가, 배제한 호가 |
| Land DD Red-Flag Pack | 체크리스트 | 권리, 물리, 환경, 문화재, 접도, 분묘, 지장물, stop condition |
| Stakeholder/M 민원 Pack | 템플릿 | 이해관계자, 예상 반대, 쟁점, Q&A, 대응 owner |
| Claim Ledger | 템플릿 | 청구자, 사유, 금액, 근거, QS, 협상상태, 승인권자 |
| Contract Clause Library | 부록 | 토지, 도급, 신탁, 분양대행, PF, 하도급 주요 특약 |
| Tax/SPC/Funds Flow Matrix | 본문 + 템플릿 | SPC, 계좌, 취득세, VAT, 법인세, 자금집행 증빙 |
| VDR/Privacy Index | 부록 | 폴더구조, 권한, 개인정보 목록, 다운로드 로그, 보존기한 |
| 개발업 Compliance Calendar | 부록 | 등록, 변경보고, 실적보고, 전문인력, 사무실, 제출증빙 |
| Training Drill Pack | 부록 | 신규 인력 온보딩, Gate drill, 실패사례 red-team, 평가표 |
| Closeout/Defect/Exit Pack | Phase 8 | reserve, defect triage, 환급 SLA, 미분양 exit, 세무 close |

## 7. Execution Phases After Approval

### Phase A. 작업본 생성 및 증거 기준 고정

목표: 원본을 다시 보존하고 작업본을 만든다.

작업:

1. v1.0 원본/백업 hash 재검증.
2. v1.1 working copy 생성.
3. `version_change_log.md` 작성.
4. `manual_v1_gap_matrix.json`을 v1.1 작업 backlog로 변환.

검증:

- 원본 hash unchanged.
- 작업본만 수정 대상.
- approval log 생성.

### Phase B. Evidence Normalization

목표: G002/G003 증거를 후속 편집 가능 상태로 정리한다.

작업:

1. 실패 DB row count를 실제 63건으로 정규화하거나 누락 row 여부를 확인한다.
2. `SYNTHESIS.md`의 64건 표기는 정정 후보로 표시한다.
3. unresolved high-risk claim은 본문 의무통제가 아니라 research backlog로 유지한다.
4. source_refs와 claim-ledger를 chapter별로 재배치한다.

검증:

- DB row count와 synthesis count 일치.
- unresolved claim이 본문 통제로 승격되지 않음.
- 각 control에 source_refs 또는 local evidence 연결.

### Phase C. 12 Workstream 보강 작성

목표: WS-01~WS-12를 본문/부록으로 집필한다.

작업 순서:

1. WS-00 Version Governance와 WS-07 조직/RACI를 먼저 작성한다.
2. WS-01 PF, WS-08 세무·회계·SPC, WS-09 VDR을 Phase 3/5와 연결한다.
3. WS-03 토지, WS-04 인허가, WS-05 시공을 기존 Phase 1/2/4/6에 삽입한다.
4. WS-02 분양, WS-12 준공 후 정산을 Phase 7/8에 삽입한다.
5. WS-10 개발업 컴플라이언스와 WS-11 교육훈련을 부록과 PART 1에 반영한다.

검증:

- 각 core-axis가 본문 또는 부록에 최소 1개 이상 명시적으로 존재.
- 각 Phase가 Control Box를 가진다.
- 각 Control Box가 Owner/Trigger/Threshold/Evidence/Stop-or-Approve/Training을 가진다.

### Phase D. Failure Simulation QA

목표: 매뉴얼이 실제 실패를 막는지 시뮬레이션한다.

대표 시나리오:

1. 브릿지론 만기 60일 전 본PF 조건 미확정.
2. 토지 잔금 전 가압류 또는 지장물 발견.
3. 인허가 심의 2회 보류와 주민 민원.
4. 시공사 공사비 15% 증액 요구.
5. 분양률 50% 미만, PF EOD 근접.
6. 준공 후 잔금 미납과 하자 집단 claim.

검증 방식:

- 각 시나리오에서 매뉴얼이 Stop/Approve 결정을 낼 수 있어야 한다.
- owner와 evidence가 없으면 fail로 본다.
- 단순 설명만 있고 실행서식이 없으면 fail로 본다.

### Phase E. Final Packaging

목표: 승인 가능한 v1.1 draft를 산출한다.

산출:

- v1.1 draft DOCX
- v1.1 draft MD
- template pack
- QA evidence pack
- source preservation report

승인 조건:

- 원본 v1.0 hash unchanged.
- 12 core axes all covered.
- 모든 MISSING/OUTDATED가 resolved 또는 explicit backlog로 전환.
- unresolved legal/current-policy claim은 본문 의무통제로 쓰지 않음.

## 8. Approval Gate Before Manual Body Edits

이 플랜 승인 전에는 다음 작업을 하지 않는다.

- 원본 v1.0 DOCX 편집
- Obsidian 20_WIKI source 파일 편집
- v1.1 working copy 생성
- 매뉴얼 본문 rewrite
- source_refs를 근거 없이 단정문으로 승격

승인 후 처음 수행할 작업은 Phase A의 작업본 생성과 hash 재검증이다.

## 9. Blind Spot Carry-Forward

G003 재점검에서 확인한 blind spot은 모두 후속 플랜에 반영한다.

| ID | Finding | 처리 |
| --- | --- | --- |
| G003-BS-A | Obsidian 20_WIKI 경로가 현재본 1개와 백업 4개로 분산 | canonical source path와 archive comparison policy를 Version Governance에 포함 |
| G003-BS-B | `SYNTHESIS.md` 64건 vs 실제 DB 63건 불일치 | Phase B에서 count normalization 또는 누락 row 확인 |
| G003-BS-C | v1.0에 원본/작업본/diff/승인 로그 운영체계 없음 | WS-00 Version Governance 신설 |
| G003-BS-D | 개발업 컴플라이언스, VDR/개인정보, 세무·회계·SPC, 교육훈련, 조직/RACI가 독립 장으로 없음 | WS-07~WS-11 및 WS-08/09/10/11로 독립 반영 |
| G004-FU-A | aside-browser 실패로 남아 있던 국토부 기본계획 공식 페이지/PDF 접근 공백 | insane-search/curl_cffi 재시도로 공식 HTML과 PDF를 확인했고, `부동산 개발사업 실적 확인제` tracker를 `재검증 완료`로 갱신. 세부 시행일·서식은 후속 고시/협회 안내 확인 대상으로 유지 |

## 10. 승인 요청

승인하면 다음 단계에서는 이 플랜대로 v1.1 작업본을 만들고 실제 매뉴얼 본문 보강을 시작한다. 승인 전 현재 상태에서 확정된 것은 다음뿐이다.

- 원본 v1.0은 보존됨.
- 실패사례 DB와 v1.0 갭 감사는 완료됨.
- 후속 매뉴얼 제작의 필수 보강축은 WS-01~WS-12로 정의됨.
- 매뉴얼 본문 편집은 아직 시작하지 않음.
