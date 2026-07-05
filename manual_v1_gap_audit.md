# manual_v1_gap_audit

작성일: 2026-07-05T02:39:41.205997+00:00

## Executive Verdict

v1.0 매뉴얼은 8 Phase 골격, Gate, PF/책임준공/유치권/QS/분양/준공정산의 기본 실무 틀이 이미 강하다. 다만 G002 실패사례 DB와 Obsidian 작업기록을 대조하면 “절차서”로는 충분해도 “실패·실수 최소화 운영체계”로는 보강해야 할 blind spot이 남아 있다.

핵심 결론은 다음과 같다.

- `COVERED`: 1개 섹션성 항목(2축 모듈 매트릭스)만 명확히 충분.
- `PARTIAL`: 대부분의 Phase는 기본 내용이 있으나 G002의 owner/trigger/evidence/stop-line 형식으로 재작성 필요.
- `MISSING`: 조직/RACI, 세무·회계·SPC, 데이터룸·문서관리, 개발업 컴플라이언스, 교육훈련은 별도 운영장으로 신설 필요.
- `OUTDATED`: PF와 법령 부록은 v1.0 작성 이후 2026~2027 제도·판례·정책 변화 추적 구조가 없어 최신성 tracker가 필요.

## Evidence Sources

- v1.0 extraction: `<REPO_ROOT>/manual_v1_extracted.md`
- v1.0 structure: `<REPO_ROOT>/manual_v1_structure.json`
- Obsidian inventory: `<REPO_ROOT>/obsidian_inventory.md`
- Failure DB: `<REPO_ROOT>/failure_case_db_v0.1.jsonl` (63 rows parsed)
- Blind spot register: `<REPO_ROOT>/blind_spot_register.md`

## Core Axis Gap Matrix

| Axis | Status | Manual hit count | Failure DB cases | Required reinforcement |
| --- | --- | ---: | ---: | --- |
| PF | OUTDATED | 76 | 60 | PF 자본구조·보증의존도 별도 장 신설; 본PF 전환성 checklist와 exposure map을 Gate 3/PF Closing 필수 증빙으로 편입; regulatory_update_tracker와 연동해 PF 제도 변경 시 threshold 재검토 |
| 분양 | PARTIAL | 63 | 58 | 분양광고 legal signoff와 disclaimer library; 계약해제·환급·재분양 decision tree; P50~P75 실거래가 산정표를 Phase 3/7 필수 입력으로 편입 |
| 토지 | PARTIAL | 56 | 63 | 토지 DD red-flag chapter 신설; Gate 1에 stop/approve matrix와 법무의견서 필수화; 계약특약 library와 잔금집행 evidence checklist |
| 인허가 | PARTIAL | 40 | 63 | 인허가·민원 stakeholder chapter 신설; 공람 전 Q&A pack과 회의록/쟁점표 증빙화; 인허가 지연 금융비용 재산정 trigger를 Gate 2/3에 연결 |
| 시공 | PARTIAL | 94 | 57 | 공사비·책임준공·신탁 chapter에 claim ledger 편입; 하도급·시공사 counterparty DD pack; 공정률 hold-point와 변경승인 RACI 설정 |
| 법률 | PARTIAL | 55 | 63 | 법률 레퍼런스 시트를 living tracker로 전환; 분쟁 유형별 escalation ladder와 법무 signoff log; 계약특약 library를 Phase 2/5/7에 연결 |
| 조직 | MISSING | 34 | 42 | 조직·권한·RACI chapter 신설; Gate별 approver/evidence/meeting minute 표준화; key-person contingency와 인수인계 checklist |
| 세무·회계·SPC | MISSING | 26 | 63 | 세무·회계·SPC chapter 신설; funds-flow matrix와 계좌/증빙 대장; 계약변경 tax memo와 정산 전 세무 검토 gate |
| 데이터룸·문서관리 | MISSING | 18 | 24 | 데이터룸·개인정보·증빙보존 chapter 신설; VDR signoff와 permission matrix; 개인정보 inventory 및 사고 대응 drill |
| 개발업 컴플라이언스 | MISSING | 2 | 6 | 개발업 컴플라이언스 chapter 신설; 등록·변경·실적보고 calendar; 전문인력 roster와 evidence binder |
| 교육훈련 | MISSING | 12 | 6 | 초보자 교육·시뮬레이션 chapter 신설; case-based drill deck와 역할별 check ride; 분기별 재교육 및 오류사례 회고 프로세스 |
| 준공 후 정산 | PARTIAL | 71 | 55 | 준공 후 정산·하자·exit chapter 보강; defect triage와 reserve policy; 미분양/환급/입주율 stress trigger를 Gate 5에 연결 |

## Axis Detail

### PF — OUTDATED

v1.0은 PF 구조, 책임준공, 출구전략을 상당히 다루지만 2026~2027 제도 전환, 자기자본 단계별 요건, repayment-source classification, sponsor/project exposure 분리 통제가 빠져 최신 실패사례 기준으로는 갱신 필요.

**Key gaps**
- 자기자본 5/10/15/20% 제도 tracker와 투자심의 stop-line 부재
- 보증의존도·차주별 exposure map·cash waterfall 검증 항목 부족
- 본PF 전환 실패 60~90일 전 자동 재평가 및 신규 익스포저 차단 기준 부족

**Controls to add**
- PF 자본구조·보증의존도 별도 장 신설
- 본PF 전환성 checklist와 exposure map을 Gate 3/PF Closing 필수 증빙으로 편입
- regulatory_update_tracker와 연동해 PF 제도 변경 시 threshold 재검토

**Manual evidence sample**
- `P0016` v0.9 → PF 출구전략, HUG 모니터링, 법령 Annex 분리, 공기지연 민감도 추가
- `P0017` v1.0 → 신탁사 책임준공 의사결정, 유치권 방어 플랜, QS 분쟁해결, 기부채납 Buffer 추가
- `T002R06` ⑤ PF 자금조달 | v1.0 | 예정 | 예정 | 예정 | 예정 | 예정 | 예정
- `T003R05` G3 | PF 착수 승인 | 인허가 진행 중/완료 후 | PF 조달을 위한 조건이 갖춰졌는가?
- `T008R01` ⚠ 의사결정 기준 (Threshold) — 이 수치를 반드시 준수할 것 • 토지비 비중: 총사업비의 30% 이내 (수도권 기준) • 예상 분양가: 인근 시세의 85~110% 범위 내 설정 • 목표 시행 이익률: 세전 10% 이상 • BEP 분양률: 70% 이하 • PF 금리 시나리오: 현재 금리 +2%p 적용해도 사업성…
- `T016R01` 🚪 Gate 1: 토지 매입 의사결정 아래 항목을 모두 충족해야 다음 단계로 진행할 수 있다: ☐ 등기부등본 갑구·을구 법무법인 검토 완료 (가압류, 가등기, 지상권 등 0건) ☐ 토지이용계획확인서 재확인 (Phase 1 대비 변동사항 없음) ☐ 경계측량 완료 및 실제 면적 확인 ☐ 지반조사 완료 (연약지반 여부 확인)…

Failure DB sample case IDs: `KR-PF-001, KR-PF-002, KR-PF-003, KR-PF-004, KR-PF-005, KR-PF-006, KR-PF-007, KR-PF-008, KR-PF-009, KR-PF-010, KR-SALES-001, KR-SALES-002, KR-SALES-003, KR-SALES-004, KR-SALES-005, KR-HUG-001, KR-LAND-001, KR-LAND-002`

### 분양 — PARTIAL

v1.0은 분양가 산정, HUG, 미분양 대응을 포함하지만 광고문구 법무승인, 해약·환급 SOP, 실거래가 P50~P75 도구 연결, 분양대행사 리스크 통제가 부족.

**Key gaps**
- 분양광고 표현 승인/증빙보존 workflow 부재
- 계약해제·환급·HUG 사고 시나리오 SOP 부족
- Obsidian에 기록된 실거래가 기반 P50~P75 도구가 v1.0 본문에 통합되지 않음

**Controls to add**
- 분양광고 legal signoff와 disclaimer library
- 계약해제·환급·재분양 decision tree
- P50~P75 실거래가 산정표를 Phase 3/7 필수 입력으로 편입

**Manual evidence sample**
- `P0016` v0.9 → PF 출구전략, HUG 모니터링, 법령 Annex 분리, 공기지연 민감도 추가
- `T001R03` Layer 2 | 의사결정 프레임워크 | Go/No-Go 판단을 위한 수치적 기준(Threshold)과 Gate를 제공 | BEP 분양률 ≤ 70% 시 사업 진행
- `T002R08` ⑦ 분양/마케팅 | v1.0 | 예정 | 예정 | 예정 | 예정 | 예정 | 예정
- `T003R06` G4 | 분양 개시 승인 | 분양 준비 완료 후 | 분양 시점과 조건이 적절한가?
- `T006R05` 공공기관 (LH, SH, 지자체) | 공공분양/임대 연계 가능, 대규모 택지 | 공모 조건 준수 필수, 수익률 제한 가능
- `T007R08` 시장 분석 | 인근 아파트 시세 및 거래량 | 국토교통부 실거래가, KB시세 | 분양가 산정 근거 확보

Failure DB sample case IDs: `KR-PF-001, KR-PF-002, KR-PF-003, KR-PF-004, KR-PF-005, KR-PF-006, KR-PF-007, KR-PF-008, KR-PF-009, KR-PF-010, KR-SALES-001, KR-SALES-002, KR-SALES-003, KR-SALES-004, KR-SALES-005, KR-HUG-001, KR-LAND-001, KR-LAND-002`

### 토지 — PARTIAL

v1.0은 토지 발굴, 입지, 법률·물리 실사, 계약 특약을 다루지만 red-flag별 stop condition과 증빙 수준이 사건 DB 기준만큼 세분화되어 있지 않음.

**Key gaps**
- 유치권·분묘·문화재·접도·토양오염·지장물별 중단조건이 하나의 표준 DD pack으로 묶여 있지 않음
- 매도인/counterparty DD와 자금집행 조건부 통제가 부족

**Controls to add**
- 토지 DD red-flag chapter 신설
- Gate 1에 stop/approve matrix와 법무의견서 필수화
- 계약특약 library와 잔금집행 evidence checklist

**Manual evidence sample**
- `T001R02` Layer 1 | 실무 매뉴얼 | 각 단계(Phase)별 절차, 산출물, 담당자를 명시 | 토지 매매계약 체크리스트
- `T002R02` ① 사업기획/토지발굴 | v1.0 | 예정 | 예정 | 예정 | 예정 | 예정 | 예정
- `T002R03` ② 토지확보/실사 | v1.0 | 예정 | 예정 | 예정 | 예정 | 예정 | 예정
- `T003R02` G0 | 사업 진입 검토 | 사업기획 완료 후 | 이 토지/사업에 진입할 가치가 있는가?
- `T003R03` G1 | 토지 매입 의사결정 | 실사 완료 후 | 이 토지를 매입해도 안전한가?
- `P0038` Phase 1. 사업기획 및 토지 발굴

Failure DB sample case IDs: `KR-PF-001, KR-PF-002, KR-PF-003, KR-PF-004, KR-PF-005, KR-PF-006, KR-PF-007, KR-PF-008, KR-PF-009, KR-PF-010, KR-SALES-001, KR-SALES-002, KR-SALES-003, KR-SALES-004, KR-SALES-005, KR-HUG-001, KR-LAND-001, KR-LAND-002`

### 인허가 — PARTIAL

v1.0은 인허가 프로세스와 심의 대응을 다루지만 주민반대, 도시계획위원회 보류, 대안안, 공람 전 Q&A pack, 이해관계자 커뮤니케이션이 약함.

**Key gaps**
- stakeholder map과 민원 issue log 부재
- 심의 보류/반려 시 대안안·자료보완 playbook 부족
- 장기보류 시 금융비용/브릿지론 영향 자동 연결 부족

**Controls to add**
- 인허가·민원 stakeholder chapter 신설
- 공람 전 Q&A pack과 회의록/쟁점표 증빙화
- 인허가 지연 금융비용 재산정 trigger를 Gate 2/3에 연결

**Manual evidence sample**
- `T002R05` ④ 인허가 | v1.0 | 예정 | 예정 | 예정 | 예정 | 예정 | 예정
- `T003R05` G3 | PF 착수 승인 | 인허가 진행 중/완료 후 | PF 조달을 위한 조건이 갖춰졌는가?
- `T007R03` 법적 검토 | 지구단위계획 수립 여부 | 지자체 도시계획과 확인 | 허용 용도 및 층수 제한
- `T007R13` 환경/민원 | 일조권·조망권 영향 | 인접 건물 높이·거리 확인 | 남측 이격거리 부족 시 민원·소송 리스크
- `T007R14` 환경/민원 | 혐오시설 인접 여부 | 현장 확인 + 주민 인터뷰 | 장례식장, 쓰레기처리장 등
- `T007R15` 규제 | 교육환경보호구역 해당 여부 | 학교환경위생정화구역 조회 (교육청) | 반경 200m 내 학교 시 심의 필수 → 2~6개월 추가

Failure DB sample case IDs: `KR-PF-001, KR-PF-002, KR-PF-003, KR-PF-004, KR-PF-005, KR-PF-006, KR-PF-007, KR-PF-008, KR-PF-009, KR-PF-010, KR-SALES-001, KR-SALES-002, KR-SALES-003, KR-SALES-004, KR-SALES-005, KR-HUG-001, KR-LAND-001, KR-LAND-002`

### 시공 — PARTIAL

v1.0은 유치권 방어, QS 분쟁, 중대재해, 설계변경을 다루지만 공사비 claim ledger, 하도급·counterparty DD, 공정률 구간별 특별승인 기준이 부족.

**Key gaps**
- 공사비 증액 claim ledger와 증빙서류 표준 부재
- 하도급업체 재무/기술 DD 및 default/step-in 절차 부족
- 공정률 70% 이후 변경·정산 승인권한 강화 기준 부족

**Controls to add**
- 공사비·책임준공·신탁 chapter에 claim ledger 편입
- 하도급·시공사 counterparty DD pack
- 공정률 hold-point와 변경승인 RACI 설정

**Manual evidence sample**
- `P0017` v1.0 → 신탁사 책임준공 의사결정, 유치권 방어 플랜, QS 분쟁해결, 기부채납 Buffer 추가
- `T002R07` ⑥ 시공관리 | v1.0 | 예정 | 예정 | 예정 | 예정 | 예정 | 예정
- `T007R06` 물리적 검토 | 지반 조건, 경사도 | 현장 확인 + 지질조사 | 연약지반 여부, 급경사 10% 이상 시 추가 공사비
- `T013R02` 지반조사 | 시추조사(보링 테스트) | 1,000~3,000만원 | 연약지반 시 기초공사비 50~100% 증가 가능
- `T018R04` 지출 | 공사비 | 직접공사비, 간접공사비, 설계비, 감리비 | 40~55%
- `T018R07` 지출 | 예비비 | 공사비 증액 대비 (통상 공사비의 3~5%) | 2~3%

Failure DB sample case IDs: `KR-PF-001, KR-PF-002, KR-PF-003, KR-PF-004, KR-PF-005, KR-PF-006, KR-PF-007, KR-PF-008, KR-PF-009, KR-PF-010, KR-SALES-001, KR-SALES-002, KR-SALES-003, KR-SALES-004, KR-SALES-005, KR-HUG-001, KR-LAND-001, KR-LAND-002`

### 법률 — PARTIAL

v1.0은 법무검토 포인트와 법령 Annex를 포함하지만 판례 기반 실패모드, 계약유형별 조항 library, 법령변경 tracker, 분쟁 escalation 체계가 별도 운영체계로 분리되어 있지 않음.

**Key gaps**
- 법령 Annex가 static reference라 최신성 검증 주기 부재
- 분양광고/환급/신탁/책준/유치권 판례별 SOP 부족
- 계약 조항 library와 법무 승인 로그 부재

**Controls to add**
- 법률 레퍼런스 시트를 living tracker로 전환
- 분쟁 유형별 escalation ladder와 법무 signoff log
- 계약특약 library를 Phase 2/5/7에 연결

**Manual evidence sample**
- `P0017` v1.0 → 신탁사 책임준공 의사결정, 유치권 방어 플랜, QS 분쟁해결, 기부채납 Buffer 추가
- `T001R02` Layer 1 | 실무 매뉴얼 | 각 단계(Phase)별 절차, 산출물, 담당자를 명시 | 토지 매매계약 체크리스트
- `T001R04` Layer 3 | 리스크 데이터베이스 | 각 단계에서 실제 발생한 실패 사례와 예방책을 축적 | 예고등기 간과로 소유권 분쟁 사례
- `T007R13` 환경/민원 | 일조권·조망권 영향 | 인접 건물 높이·거리 확인 | 남측 이격거리 부족 시 민원·소송 리스크
- `T009R01` ⚠ 이 단계에서 가장 많이 저지르는 실수 • 사례1: 용도지역 착오 — 2종 일반주거지역으로 알고 계약 후, 실제로는 1종 전용주거지역이어서 아파트 건축 불가. • 사례2: 지구단위계획 미확인 — 용적률 250%로 수지 작성했으나, 실제 200%로 제한. 사업수지 붕괴. • 사례3: 매물 이중계약 — 브로커 2곳을 통해…
- `T010R01` 🚪 Gate 0: 사업 진입 검토 (Go/No-Go) 아래 항목을 모두 충족해야 다음 단계로 진행할 수 있다: ☐ 토지이용계획확인서 발급 완료 및 용도지역 적합성 확인 ☐ 지구단위계획 확인 완료 (용적률·건폐율·층수 제한 파악) ☐ 현장 답사 최소 2회 완료 (평일 + 주말, 주간 + 야간) ☐ 인근 시세 조사 완료 (…

Failure DB sample case IDs: `KR-PF-001, KR-PF-002, KR-PF-003, KR-PF-004, KR-PF-005, KR-PF-006, KR-PF-007, KR-PF-008, KR-PF-009, KR-PF-010, KR-SALES-001, KR-SALES-002, KR-SALES-003, KR-SALES-004, KR-SALES-005, KR-HUG-001, KR-LAND-001, KR-LAND-002`

### 조직 — MISSING

v1.0 각 Phase에 담당 부서는 있으나 스타트업 시행사의 의사결정권한, RACI, 위원회, 승인 로그, key-person 부재 대응이 독립 장으로 설계되어 있지 않음.

**Key gaps**
- 대표 감 의존을 줄이는 승인권한표와 RACI 부재
- 리스크위원회/투자심의/변경승인 운영규정 부재
- 퇴사·인수인계·대체승인 체계 부족

**Controls to add**
- 조직·권한·RACI chapter 신설
- Gate별 approver/evidence/meeting minute 표준화
- key-person contingency와 인수인계 checklist

**Manual evidence sample**
- `T001R02` Layer 1 | 실무 매뉴얼 | 각 단계(Phase)별 절차, 산출물, 담당자를 명시 | 토지 매매계약 체크리스트
- `T003R05` G3 | PF 착수 승인 | 인허가 진행 중/완료 후 | PF 조달을 위한 조건이 갖춰졌는가?
- `T003R06` G4 | 분양 개시 승인 | 분양 준비 완료 후 | 분양 시점과 조건이 적절한가?
- `T004R01` ▶ 각 Phase의 표준 구조 • ① 단계 개요: 해당 단계의 목적, 핵심 산출물, 예상 소요기간 • ② 상세 업무 프로세스: 세부 Task별 절차, 담당, 필요서류 • ③ 의사결정 기준: 수치적 Threshold, Go/No-Go 판단 기준 • ④ 핵심 리스크 & 실패 사례: 해당 단계에서 가장 많이 발생하는 리스크와…
- `T005R05` 담당 | 개발팀(토지 발굴), 사업기획팀(사업수지)
- `T011R05` 담당 | 개발팀(실사 총괄), 법무(법률검토), 재무(자금조달)

Failure DB sample case IDs: `KR-PF-001, KR-PF-002, KR-PF-003, KR-PF-004, KR-PF-005, KR-PF-006, KR-PF-007, KR-PF-008, KR-SALES-001, KR-SALES-003, KR-HUG-001, KR-LAND-001, KR-LAND-003, KR-PERMIT-001, KR-PERMIT-002, KR-PERMIT-003, KR-PERMIT-004, KR-PERMIT-005`

### 세무·회계·SPC — MISSING

v1.0은 취득세·법인세를 일부 언급하지만 세무·회계·SPC·자금통제 module은 사실상 별도 장으로 존재하지 않음.

**Key gaps**
- 취득세 cost taxonomy와 VAT 안분 worksheet 부재
- SPC 설립/자금집행/계정과목/증빙보존 통제 부족
- 계약변경·정산 시 tax memo trigger 부재

**Controls to add**
- 세무·회계·SPC chapter 신설
- funds-flow matrix와 계좌/증빙 대장
- 계약변경 tax memo와 정산 전 세무 검토 gate

**Manual evidence sample**
- `T002R09` ⑧ 준공/정산 | v1.0 | 예정 | 예정 | 예정 | 예정 | 예정 | 예정
- `T003R07` G5 | 준공 정산 확인 | 준공 후 | 모든 채무가 정리되고 수익이 확정되었는가?
- `T012R07` 세금 체납 확인 | 국세·지방세 완납증명서 | 중 | 매도인 체납 시 토지 압류 가능
- `T018R03` 지출 | 토지비 | 토지매입비, 취득세(4.6%), 중개수수료, 법무비용 | 25~35%
- `T022R01` ★ 도급계약 물가변동(Escalation) 검토 가이드 • 고정가 계약(Lump Sum): 시공사가 물가변동 리스크를 부담. 도급가가 높게 산정됨. • 실비정산 계약(Cost Plus): 실제 발생 비용 기준 정산. 총사업비 예측이 어려움. • 절충안(Cap 방식): 물가변동 정산을 하되, 증액 상한(Cap)을 설정 (…
- `T034R07` 도급 조건 | 도급금액, 지급 조건, 설계변경 시 정산 방식 | 상

Failure DB sample case IDs: `KR-PF-001, KR-PF-002, KR-PF-003, KR-PF-004, KR-PF-005, KR-PF-006, KR-PF-007, KR-PF-008, KR-PF-009, KR-PF-010, KR-SALES-001, KR-SALES-002, KR-SALES-003, KR-SALES-004, KR-SALES-005, KR-HUG-001, KR-LAND-001, KR-LAND-002`

### 데이터룸·문서관리 — MISSING

v1.0은 필수 서류 목록은 있으나 VDR 구조, 접근권한, 개인정보 inventory, 감사 로그, 증거보존 체계가 없음.

**Key gaps**
- data room index와 folder taxonomy 부재
- 권한표·다운로드 로그·개인정보 최소수집 기준 부재
- 72시간 신고 tabletop 등 개인정보 사고 대응 부재

**Controls to add**
- 데이터룸·개인정보·증빙보존 chapter 신설
- VDR signoff와 permission matrix
- 개인정보 inventory 및 사고 대응 drill

**Manual evidence sample**
- `P0034` 1.4 문서 활용 가이드
- `T004R01` ▶ 각 Phase의 표준 구조 • ① 단계 개요: 해당 단계의 목적, 핵심 산출물, 예상 소요기간 • ② 상세 업무 프로세스: 세부 Task별 절차, 담당, 필요서류 • ③ 의사결정 기준: 수치적 Threshold, Go/No-Go 판단 기준 • ④ 핵심 리스크 & 실패 사례: 해당 단계에서 가장 많이 발생하는 리스크와…
- `T006R06` 직접 발굴 (현장답사, 토지대장 분석) | 남들이 모르는 기회 포착, 협상력 우위 | 시간·인력 소요 큼
- `T012R01` 확인 항목 | 확인 서류 | 리스크 수준 | 확인 포인트
- `T013R05` 접도 조건 | 현장 확인 + 도로대장 | 자체 수행 | 건축법상 도로(4m+) 접면 필수
- `T026R03` 핵심 산출물 | 건축허가서(또는 사업승인서), 각종 심의 통과 서류, 확정 설계도서

Failure DB sample case IDs: `KR-PF-009, KR-SALES-001, KR-SALES-002, KR-SALES-003, KR-LAND-002, KR-LAND-003, KR-LAND-004, KR-GOV-002, KR-GOV-003, KR-TAX-001, KR-TAX-004, KR-DATA-001, KR-DATA-002, KR-DATA-003, KR-DATA-004, KR-DATA-005, KR-DATA-006, KR-COMP-001`

### 개발업 컴플라이언스 — MISSING

v1.0에는 부동산개발업 등록, 사업실적보고, 전문인력 roster, 변경보고 일정 관리가 확인되지 않음.

**Key gaps**
- 개발업 등록요건과 변경보고 calendar 부재
- 전문인력 증빙 roster와 교육 이력 관리 부재
- 사업실적보고·협회/관청 제출 증빙 부재

**Controls to add**
- 개발업 컴플라이언스 chapter 신설
- 등록·변경·실적보고 calendar
- 전문인력 roster와 evidence binder

**Manual evidence sample**
- `T061R04` 3 | 사용검사 신청 | 시행사 → 지자체 | 건축물대장 등록 서류 준비
- `T068R08` 7. 분양마케팅 | 입주자모집공고, 분양계약서, 분양실적보고서 | 자체, 법무, 분양대행사

Failure DB sample case IDs: `KR-DATA-002, KR-COMP-001, KR-COMP-002, KR-COMP-003, KR-POLICY-001, NL-COMP-001`

### 교육훈련 — MISSING

v1.0은 업무 체크리스트는 많지만 신규 인력 교육, Gate drill, 실패사례 기반 red-team, 역할별 시뮬레이션이 별도 운영체계로 설계되어 있지 않음.

**Key gaps**
- 초보자 onboarding syllabus 부재
- 실패사례 DB를 훈련 시나리오로 바꾸는 절차 부재
- Gate 통과 drill과 평가표 부재

**Controls to add**
- 초보자 교육·시뮬레이션 chapter 신설
- case-based drill deck와 역할별 check ride
- 분기별 재교육 및 오류사례 회고 프로세스

**Manual evidence sample**
- `T001R02` Layer 1 | 실무 매뉴얼 | 각 단계(Phase)별 절차, 산출물, 담당자를 명시 | 토지 매매계약 체크리스트
- `T004R01` ▶ 각 Phase의 표준 구조 • ① 단계 개요: 해당 단계의 목적, 핵심 산출물, 예상 소요기간 • ② 상세 업무 프로세스: 세부 Task별 절차, 담당, 필요서류 • ③ 의사결정 기준: 수치적 Threshold, Go/No-Go 판단 기준 • ④ 핵심 리스크 & 실패 사례: 해당 단계에서 가장 많이 발생하는 리스크와…
- `P0045` 1-2. 입지 분석 체크리스트
- `T007R15` 규제 | 교육환경보호구역 해당 여부 | 학교환경위생정화구역 조회 (교육청) | 반경 200m 내 학교 시 심의 필수 → 2~6개월 추가
- `T009R01` ⚠ 이 단계에서 가장 많이 저지르는 실수 • 사례1: 용도지역 착오 — 2종 일반주거지역으로 알고 계약 후, 실제로는 1종 전용주거지역이어서 아파트 건축 불가. • 사례2: 지구단위계획 미확인 — 용적률 250%로 수지 작성했으나, 실제 200%로 제한. 사업수지 붕괴. • 사례3: 매물 이중계약 — 브로커 2곳을 통해…
- `T010R01` 🚪 Gate 0: 사업 진입 검토 (Go/No-Go) 아래 항목을 모두 충족해야 다음 단계로 진행할 수 있다: ☐ 토지이용계획확인서 발급 완료 및 용도지역 적합성 확인 ☐ 지구단위계획 확인 완료 (용적률·건폐율·층수 제한 파악) ☐ 현장 답사 최소 2회 완료 (평일 + 주말, 주간 + 야간) ☐ 인근 시세 조사 완료 (…

Failure DB sample case IDs: `KR-PERMIT-003, KR-DATA-005, KR-COMP-002, KR-POLICY-001, KR-CLOSE-001, KR-TRAIN-001`

### 준공 후 정산 — PARTIAL

v1.0 Phase 8은 사용검사, 입주, PF 상환, 최종정산, 하자를 다루지만 defect triage, refund SLA, reserve, 장기 미분양 exit, 신탁공급계약 소비자 리스크가 부족.

**Key gaps**
- 하자 triage와 반복하자 원인분석/재교육 연결 부족
- 환급·해지·잔금미납 SLA와 책임자 부재
- 미분양 보유/임대/벌크매각 exit decision tree 부족

**Controls to add**
- 준공 후 정산·하자·exit chapter 보강
- defect triage와 reserve policy
- 미분양/환급/입주율 stress trigger를 Gate 5에 연결

**Manual evidence sample**
- `P0017` v1.0 → 신탁사 책임준공 의사결정, 유치권 방어 플랜, QS 분쟁해결, 기부채납 Buffer 추가
- `T002R09` ⑧ 준공/정산 | v1.0 | 예정 | 예정 | 예정 | 예정 | 예정 | 예정
- `T003R07` G5 | 준공 정산 확인 | 준공 후 | 모든 채무가 정리되고 수익이 확정되었는가?
- `T008R01` ⚠ 의사결정 기준 (Threshold) — 이 수치를 반드시 준수할 것 • 토지비 비중: 총사업비의 30% 이내 (수도권 기준) • 예상 분양가: 인근 시세의 85~110% 범위 내 설정 • 목표 시행 이익률: 세전 10% 이상 • BEP 분양률: 70% 이하 • PF 금리 시나리오: 현재 금리 +2%p 적용해도 사업성…
- `T009R01` ⚠ 이 단계에서 가장 많이 저지르는 실수 • 사례1: 용도지역 착오 — 2종 일반주거지역으로 알고 계약 후, 실제로는 1종 전용주거지역이어서 아파트 건축 불가. • 사례2: 지구단위계획 미확인 — 용적률 250%로 수지 작성했으나, 실제 200%로 제한. 사업수지 붕괴. • 사례3: 매물 이중계약 — 브로커 2곳을 통해…
- `T014R01` ▶ 토지 매매계약서에 반드시 포함할 특약 사항 • 소유권이전등기 전까지 제3자에 대한 권리 설정 금지 • 토지이용계획 변경 시 계약 해제 조건 • 토양오염·지중장애물 발견 시 매도인 책임 조항 • 잔금 지급 조건: 근저당·가압류 전부 말소 확인 후 지급 • 위약금 조항: 매도인 귀책 시 계약금의 2배 배상 • 토지거래허…

Failure DB sample case IDs: `KR-PF-001, KR-PF-002, KR-PF-003, KR-PF-004, KR-PF-005, KR-PF-006, KR-PF-007, KR-PF-008, KR-PF-009, KR-PF-010, KR-SALES-001, KR-SALES-002, KR-SALES-003, KR-SALES-004, KR-SALES-005, KR-HUG-001, KR-LAND-001, KR-LAND-002`

## v1.0 Phase/Section Audit

| Section | Style | P# | Status | Audit note |
| --- | --- | ---: | --- | --- |
| PART 1. 시스템 아키텍처 | Heading 1 | 20 | PARTIAL | 구조는 우수하나 원본/버전 거버넌스, 운영권한, 데이터룸 통제가 빠져 실제 운영체계로는 보강 필요. |
| 1.1 3계층(Layer) 구조 | Heading 2 | 22 | PARTIAL | 3층 개념은 있으나 리스크 DB 운영/증거/교육 연계가 미구현. |
| 1.2 2축 모듈 매트릭스 | Heading 2 | 26 | COVERED | 사업유형×기능 공통 모듈화 원칙은 명확함. |
| 1.3 Gate 시스템 (단계별 관문) | Heading 2 | 30 | PARTIAL | Gate 구조는 있으나 G002에서 나온 stop condition, owner, evidence, escalation 필드가 부족. |
| 1.4 문서 활용 가이드 | Heading 2 | 34 | PARTIAL | 활용 가이드는 있으나 원본 보존·작업본·승인로그·diff 절차가 없음. |
| PART 2. 아파트 시행 실무 매뉴얼 v1.0 | Heading 1 | 36 | PARTIAL | 8 Phase 골격은 강하지만 G002 12축 중 신규 운영축 5개 이상이 독립 장으로 없음. |
| Phase 1. 사업기획 및 토지 발굴 | Heading 2 | 38 | PARTIAL | 입지/수지 기준은 있으나 최신 PF 자본구조, 환경·보험, 이해관계자 초기 map 보강 필요. |
| 1-1. 토지 정보 수집 채널 | Heading 3 | 41 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 1-2. 입지 분석 체크리스트 | Heading 3 | 45 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 1-3. 초기 사업성 검토 (예비 사업수지) | Heading 3 | 49 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 1-4. 실패 사례 & 교훈 | Heading 3 | 51 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| Phase 2. 토지 확보 및 실사 (Due Diligence) | Heading 2 | 54 | PARTIAL | 법률/물리 실사는 있으나 red-flag stop condition과 counterparty DD 보강 필요. |
| 2-1. 법률 실사 (Legal Due Diligence) | Heading 3 | 57 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 2-2. 물리적 실사 | Heading 3 | 59 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 2-3. 매매계약 핵심 특약 | Heading 3 | 61 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 2-4. 핵심 리스크 & 실패 사례 | Heading 3 | 63 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| Phase 3. 사업타당성 분석 | Heading 2 | 66 | PARTIAL | 민감도 분석은 좋으나 실거래가 P50~P75 도구, tax/SPC/funds-flow, PF 제도 tracker 연결 필요. |
| 3-1. 사업수지표 구성 항목 | Heading 3 | 69 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 3-2. 시나리오 분석 (Sensitivity Analysis) | Heading 3 | 71 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 3-3. 핵심 리스크 & 실패 사례 | Heading 3 | 77 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| Phase 4. 인허가 | Heading 2 | 80 | PARTIAL | 인허가 절차는 있으나 주민·민원·도시계획위원회 쟁점 pack과 장기보류 대응 보강 필요. |
| 4-1. 인허가 프로세스 개요 | Heading 3 | 83 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 4-2. 설계사무소 선정 및 관리 | Heading 3 | 85 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 4-3. 심의 대응 전략 | Heading 3 | 87 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 4-4. 핵심 리스크 & 실패 사례 | Heading 3 | 89 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| Phase 5. PF (Project Financing) 자금조달 | Heading 2 | 92 | OUTDATED | PF 구조와 책준은 다루지만 2026~2027 PF 제도 전환, 자기자본/보증의존도/repayment source 통제가 최신화 필요. |
| 5-1. PF 자금조달 구조 이해 | Heading 3 | 95 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 5-2. 시공사 선정 및 도급계약 | Heading 3 | 97 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 5-3. PF 금융구조 설계 핵심 | Heading 3 | 99 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 5-3-1. [v1.0] 책임준공형 관리형 토지신탁 의사결정 | Heading 3 | 101 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 5-3-2. 책임준공 기한 도과 리스크 관리 | Heading 3 | 106 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 5-3-3. PF 출구전략 (Contingency Plan) | Heading 3 | 108 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 5-4. 분양보증 | Heading 3 | 113 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 5-5. 핵심 리스크 & 실패 사례 | Heading 3 | 115 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| Phase 6. 시공 관리 | Heading 2 | 118 | PARTIAL | 유치권/QS/중대재해 보강은 좋으나 공사비 claim ledger, 하도급 DD, hold-point가 부족. |
| 6-1. 시행사의 시공관리 역할 | Heading 3 | 121 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 6-2. 설계변경 관리 프로세스 | Heading 3 | 123 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 6-3. [v1.0] 시공사 부도 시 유치권 방어 플랜 | Heading 3 | 125 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 6-4. [v1.0] 공사비 증액(에스컬레이션) 분쟁 해결 프로세스 | Heading 3 | 130 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 6-5. 중대재해처벌법 — 시행사(발주자)의 의무 | Heading 3 | 135 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 6-6. 핵심 리스크 & 실패 사례 | Heading 3 | 137 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| Phase 7. 분양 및 마케팅 | Heading 2 | 139 | PARTIAL | 분양가/HUG/미분양은 있으나 광고문구 법무승인, 환급 SOP, 분양대행사 리스크 통제 부족. |
| 7-1. 분양 시점 결정 | Heading 3 | 142 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 7-2. 분양가 산정 | Heading 3 | 144 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 7-3. 미분양 대응 전략 | Heading 3 | 147 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 7-4. 핵심 리스크 & 실패 사례 | Heading 3 | 149 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| Phase 8. 준공 및 정산 | Heading 2 | 152 | PARTIAL | 정산/하자 기본은 있으나 defect triage, reserve, 미분양 exit, 환급 SLA 보강 필요. |
| 8-1. 사용검사 프로세스 | Heading 3 | 155 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 8-2. 입주 관리 | Heading 3 | 157 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 8-3. PF 상환 및 최종 정산 | Heading 3 | 160 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 8-4. 하자 관리 | Heading 3 | 162 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| 8-5. 핵심 리스크 & 실패 사례 | Heading 3 | 166 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| PART 3. 부록 | Heading 1 | 169 | PARTIAL | 부록은 유용하지만 운영대장·VDR·법령 최신성 tracker가 빠짐. |
| 부록 A. 단계별 필수 서류 총괄표 | Heading 2 | 171 | PARTIAL | 서류 목록은 있으나 데이터룸 taxonomy/권한/보존기한이 없음. |
| 부록 B. 핵심 용어 사전 | Heading 2 | 174 | PARTIAL | 핵심 용어는 있으나 최신 PF/개발업/개인정보/세무 용어 보강 필요. |
| 부록 C. 향후 확장 로드맵 | Heading 2 | 177 | PARTIAL | 사업유형 확장 방향은 있으나 v1.x 현장검증 governance와 승인 기준이 부족. |
| 부록 D. 법령 레퍼런스 시트 | Heading 2 | 182 | OUTDATED | 법령 reference는 static이므로 current-law tracker와 최신성 확인 주기가 필요. |
| D-1. 중대재해 처벌 등에 관한 법률 | Heading 3 | 186 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| D-2. 하자담보책임 (공동주택관리법) | Heading 3 | 188 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| D-3. 분양가 상한제 (주택법) | Heading 3 | 192 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |
| D-4. 도급계약 물가변동(에스컬레이션) | Heading 3 | 194 | PARTIAL | 세부항목은 v1.0에 존재하나 G002 실패사례 기준의 owner/trigger/evidence/stop-line 형태로 재작성 필요. |

## Blind Spot Recheck Addendum

### G003-BS-A — reinforced
- finding: Obsidian 20_WIKI/부동산개발_시스템 경로가 현재본 1개와 백업 4개로 분산되어 있어 단일 경로만 보면 최신/이전 차이를 놓칠 수 있음.
- reinforcement: obsidian_inventory.md에 5개 경로, 해시, mtime, heading/wiki-link 목록을 모두 기록; source preservation C003에서 현재본/백업 source 파일 무변경 검증 예정.
- G004 carry-forward: 플랜에는 canonical source path와 archive comparison policy를 포함.

### G003-BS-B — reinforced
- finding: SYNTHESIS.md는 DB 64건이라고 적지만 실제 failure_case_db_v0.1.jsonl은 63행이며 G002 검증도 63건으로 통과함.
- reinforcement: manual_v1_gap_matrix.json은 실제 JSONL 63건을 기준으로 계산; G004에서 숫자 표기 정정/검증 항목으로 승격.
- G004 carry-forward: 최종 플랜에는 evidence count normalization을 작업항목으로 포함.

### G003-BS-C — reinforced
- finding: v1.0은 실무 절차가 강하지만 원본 보존, 작업본, 변경이력, diff, 승인 로그가 문서 운영체계로 없음.
- reinforcement: C003 preservation criterion과 source_preservation_audit.md를 추가; G004에는 version governance chapter를 포함.
- G004 carry-forward: 매뉴얼 개정 전 original/read-only/source-of-truth policy를 첫 단계로 배치.

### G003-BS-D — reinforced
- finding: G002 12축 중 개발업 컴플라이언스, 데이터룸·개인정보, 세무·회계·SPC, 교육훈련, 조직/RACI는 v1.0에서 독립 운영장으로 확인되지 않음.
- reinforcement: manual_v1_gap_matrix.json에서 MISSING으로 분류하고 각각 별도 chapter/control로 carry-forward 지정.
- G004 carry-forward: 종합 실행 플랜의 필수 보강 장으로 편입.

## G004 Carry-Forward Requirements

1. 원본 v1.0 보존/작업본/변경이력/diff/승인로그를 먼저 설계한다.
2. G002 12축 중 `MISSING` 또는 `OUTDATED` 항목은 종합 실행 플랜의 독립 workstream으로 둔다.
3. 기존 8 Phase는 유지하되 각 Phase를 owner, trigger, threshold, evidence, stop/approve, training scenario 필드로 재구성한다.
4. G002 숫자 불일치(64 vs 실제 63)는 후속 플랜에서 정정하거나 누락 row 여부를 별도 확인한다.
