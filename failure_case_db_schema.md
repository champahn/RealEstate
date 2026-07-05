# 실패사례 DB 스키마 v0.1

작성일: 2026-07-05  
목적: 부동산개발 실패사례를 기사 요약이 아니라 `root_cause -> early_warning_signal -> manual_control` 체인으로 재코딩해 v1.0 매뉴얼 보강에 바로 연결한다.

## 1. 원칙

1. 사건 1개는 하나의 `case_id`로 관리하고, 기사·판례·공시·보고서·스크린샷은 source table로 분리한다.
2. 모든 case는 기존 매뉴얼의 8 Phase 중 하나 이상과 연결한다.
3. 고위험 법률·금융·정책 주장은 source date와 claim status를 기록한다.
4. 초보 실무자가 재발을 막을 수 있는 통제로 내려오지 않는 사례는 DB에 넣지 않는다.
5. 뉴스는 발견 단서로만 쓴다. 원인, 손실액, 법적 결론, 규제 적용성, 현재 상태는 1차 자료 또는 고신뢰 자료로 확인되지 않으면 `claim_status=unresolved`로 둔다.
6. 동일 사업이 브릿지론, 경매, 공사중단, 신탁분쟁, 회생, 소송으로 여러 번 보도된 경우에는 하나의 사건으로 병합하고, 별도의 실패 메커니즘이 확인될 때만 새 행으로 분리한다.
7. 정책·법령·감독기준은 `announced_date`, `effective_date`, `transition_rule`, `recheck_before_manual_publish`를 분리한다. 시행 전 정책은 즉시 의무 통제로 쓰지 않고 준비 통제로만 쓴다.
8. 모든 `control_to_add`는 최소한 소유자, 트리거, 임계값/조건, 요구 증빙, 중단 또는 예외 승인 경로, v1.0 삽입 후보 위치를 포함해야 한다.
9. `manual_gap`은 v1.0의 검색/대조 위치를 남긴다. 아직 G003 매뉴얼 정밀감사가 끝나지 않은 경우 `v1.0 대조 예정`으로 표시하고, 최종 매뉴얼 반영 전 재확인한다.

## 1-1. 중복 판정 키

새 case를 넣기 전 아래 키를 기준으로 기존 행과 대조한다.

| 키 | 설명 |
| --- | --- |
| normalized_project_site | 사업장명, 지번, 구역명, 단지명 별칭 |
| developer_spc_group | 시행사, SPC, 계열사, 보증 제공자 |
| lender_pf_package | 브릿지론, 본PF, 대주단, 보증·신탁 패키지 |
| court_or_proceeding_id | 판례 사건번호, 회생·파산 사건, 행정심판 번호 |
| dart_or_disclosure_id | DART 접수번호, 공시 유형, 법인 코드 |
| incident_window | 최초 경고 신호부터 손실·중단·분쟁이 확정된 기간 |
| source_title_cluster | 같은 보도자료/기사 묶음 또는 동일 판결 해설 묶음 |

## 1-2. Claim Ledger 필드

`claim-ledger.md`는 아래 필드를 가진다.

| 필드 | 설명 |
| --- | --- |
| claim_id | `CLM-0001` |
| case_id | 연결 case. 정책·제도 claim은 `POLICY-*` 허용 |
| exact_assertion | 매뉴얼 또는 DB가 주장하려는 정확한 문장 |
| risk_class | legal / financial / policy / tax / privacy / operational / low-risk |
| supporting_sources | source_id 배열 |
| counter_search | 반대·예외·최신성 검토 메모 |
| primary_source_status | primary-confirmed / secondary-only / unavailable / conflicting |
| verdict | verified / unresolved / refuted / low-risk |
| allowed_downstream_use | manual-control / research-backlog / context-only / reject |

## 2. Case Table

| 필드 | 필수 | 설명 |
| --- | --- | --- |
| case_id | Y | `KR-PF-2026-001` 형식. 국가/축/연도/일련번호 |
| geography | Y | KR, US, UK, JP, AU 등 |
| project_or_company | Y | 프로젝트명, 시행사, 시공사, 신탁사, 금융기관 |
| period | Y | 사건 발생·진행 기간 |
| asset_type | Y | 아파트, 오피스텔, 상가, 물류, 도시개발, 산업단지 등 |
| phase | Y | Phase 1~8 중 주된 실패 단계. 복수 가능 |
| failure_mode | Y | PF, 분양, 토지, 인허가, 시공, 법률, 조직, 세무·회계·SPC, 데이터룸·문서관리, 개발업 컴플라이언스, 교육훈련, 준공 후 정산 |
| root_cause | Y | 재발 방지 가능한 구조적 원인 |
| contributing_factors | N | 금리, 경기, 공사비, 제도 변화 등 보조 요인 |
| trigger_event | Y | 본PF 전환 실패, 분양률 미달, 인허가 반려, 시공사 부도 등 |
| early_warning_signal | Y | 사전에 볼 수 있었던 지표·문서·행동 신호 |
| loss_or_impact | Y | 손실액, 지연 기간, 소송, 회생, 사업중단, 평판 손상 |
| manual_gap | Y | v1.0 매뉴얼의 부족 지점 |
| control_to_add | Y | Gate, 체크리스트, 계약특약, 승인권자, 데이터룸 증빙 등 |
| control_owner | Y | 시행 대표, PM, 재무, 법무, 세무, 분양, 현장 등 |
| regulatory_status | Y | 기준일, 적용 예정일, 재확인 필요일 |
| tax_accounting_impact | Y | 취득세, 부가세, 법인세, PF/SPC 회계, 자금흐름 영향 |
| data_room_ref | Y | 증빙 문서, 폴더, 권한, 보존기간 |
| training_scenario | Y | 신규 담당자 drill 또는 red-team 질문 |
| source_refs | Y | source_id 배열. 최소 1개, 고위험 claim은 1차 자료 우선 |
| confidence | Y | high / medium / low |
| claim_status | Y | verified / unresolved / refuted / low-risk |
| notes | N | 조사자 메모 |

## 2-1. Case Acceptance Checklist

각 case 행은 아래 조건을 만족해야 한다.

1. `source_refs` 중 최소 하나가 존재하고, 고위험 주장은 claim-ledger에서 `verified` 또는 `low-risk`여야 한다.
2. 뉴스만 있는 행은 원인·손실액·법적 결론·규제의무를 단정하지 않는다.
3. `root_cause`는 단순 시간 순서가 아니라 예방 가능한 통제 실패를 설명해야 한다.
4. `control_to_add`는 현업자가 실행할 수 있는 게이트나 체크리스트 형태여야 한다.
5. 세무, 개인정보, 정책, 법률 claim은 발행일과 재확인일을 남긴다.
6. 교육훈련·준공 후 정산처럼 직접 실패사례가 얇은 축은 실제 사례 3개 이상 또는 `insufficient-evidence` 메모를 둔다.

## 3. Source Table

| 필드 | 필수 | 설명 |
| --- | --- | --- |
| source_id | Y | `SRC-0001` |
| case_id | Y | 연결 case_id |
| source_type | Y | official, court, filing, audit, news, academic, screenshot, dataset |
| title | Y | 출처 제목 |
| url_or_path | Y | URL 또는 로컬 파일 경로 |
| publisher | Y | 기관/매체 |
| published_date | N | 발행일 |
| accessed_date | Y | 접근일 |
| key_claims | Y | 이 출처가 뒷받침하는 claim |
| reliability | Y | primary, high, medium, low |
| quote_limit_note | N | 직접 인용 제한 준수 메모 |

## 4. Coverage Gate

DB v0.1은 아래 조건을 통과해야 한다.

1. 총 40개 이상 distinct case.
2. 국내 관련 30개 이상.
3. 해외·비교·판례·감사·공시·정책 10개 이상.
4. 각 core axis 최소 1개 이상: PF, 분양, 토지, 인허가, 시공, 법률, 조직, 세무·회계·SPC, 데이터룸·문서관리, 개발업 컴플라이언스, 교육훈련, 준공 후 정산.
5. 모든 case는 `manual_gap`과 `control_to_add`가 있어야 한다.
6. 고위험 법률·금융·정책 claim은 claim-ledger에서 verified/unresolved/refuted 중 하나로 잠가야 한다.
