# Failure Case Synthesis v0.1

작성일: 2026-07-05  
대상: `failure_case_db_v0.1.jsonl`, `source_index.md`, `claim-ledger.md`

## Executive Findings

1. 한국형 PF 실패의 반복 패턴은 낮은 자기자본, 보증·책임준공 의존, 브릿지론의 본PF 전환 리스크, 분양수입금 waterfall 불명확성이다. 이 결론은 FSC 태영건설 자료와 KDI PF 구조 분석, law.go.kr PF 판례군에 의해 확인된다 [S-FSC-TY-20231228], [S-FSC-TY-20240108], [S-KDI-PF-2024], [S-LAW-179847], [S-LAW-207164].
2. 분양 실패는 마케팅 문구 문제가 아니라 법률·환급·HUG·정산 리스크다. 분양광고 판례들은 구체적 스펙, 개발계획, 허위·과장 표현, 계약해제 후 손해산정이 모두 분쟁화될 수 있음을 보여준다 [S-LAW-70656], [S-LAW-124907], [S-LAW-167291], [S-LAW-225125], [S-HUG-NOTICE-37172].
3. 토지 DD는 권리관계 표만으로 부족하다. 유치권, 분묘, 문화재, 접도, 가등기, 토양오염, 지장물은 각각 별도 stop condition으로 설계해야 한다 [S-LAW-211437], [S-LAW-2011DA63017], [S-LAW-157317], [S-LAW-DRF258067], [S-LAW-606215].
4. 인허가 실패는 행정절차보다 이해관계자·대안안·자료 부족 문제로 나타난다. 보류, 장기 보류, 주민 반대, 입안제안 반려 사례는 사전 쟁점표와 민원대응 pack이 필요함을 보여준다 [S-SEOUL-17032], [S-SEOUL-514958], [S-LAW-206096], [S-LAW-DECC155457].
5. blind spot 보강 결과, 세무·회계·SPC, 개인정보/VDR, 개발업 컴플라이언스, 교육훈련, 준공 후 정산은 별도 장으로 승격해야 한다. 취득세·VAT·계약형식, 개인정보위 제재, KDA/법령 의무, 한국소비자원 하자·신탁계약 자료가 이를 지지한다 [S-LAW-616043], [S-LAW-VAT-2012GUHAP18936], [S-PIPC-12010], [S-KDA-REPORT], [S-KCA-NEWAPT].

## Manual Control Stack

| Layer | Control to add | Evidence |
| --- | --- | --- |
| PF 승인 | repayment-source classification, equity funded-before-draw, sponsor/project concentration limit | [S-KDI-PF-2024], [S-ECFR-HVCRE], [S-APRA-APS112] |
| 브릿지론 | 본PF 전환성 60~90일 전 재평가, 전환실패 시 신규 익스포저 자동 차단 | [S-LAW-221215], [S-KDI-PF-2025] |
| 책임준공 | 확약서 법률 risk rating, liability cap, 대주단 직접청구 clause 검토 | [S-LAW-179847], [S-JIPYONG-14113] |
| 분양 | 광고문구 법무승인, 미확정 개발계획 disclaimer, HUG 사고 SOP | [S-LAW-70656], [S-LAW-167291], [S-HUG-NOTICE-37172] |
| 토지 DD | 유치권·분묘·문화재·접도·토양오염·지장물 stop checklist | [S-LAW-211437], [S-LAW-157317], [S-LAW-606215] |
| 인허가 | 도시계획위원회 쟁점표, 주민반대 대응표, 공람 전 Q&A pack | [S-SEOUL-17032], [S-LAW-206096], [S-LAW-78216] |
| 시공 | 공사비 증액 claim ledger, 독립 QS, 공정률 70% 이후 특별승인 | [S-JIPYONG-14113], [S-ASIC-PROBUILD] |
| 세무·회계 | 취득세 cost taxonomy, VAT 안분 worksheet, 계약변경 tax memo | [S-LAW-616043], [S-LAW-419232], [S-LAW-213649] |
| 데이터룸 | VDR signoff, 접근권한표, 개인정보 inventory, 72시간 신고 tabletop | [S-LAW-DD-2009GAHAP132342], [S-PIPC-12010], [S-PIPC-11453] |
| 개발업 컴플라이언스 | 사업실적보고 calendar, 전문인력 roster, 사무실·변경보고 3-way 대사 | [S-KDA-REPORT], [S-KDA-REG], [S-LAW-DEVLAW] |
| 준공 후 정산 | defect triage, refund SLA, trust supply contract consumer-risk review | [S-KCA-NEWAPT], [S-KCA-TRUST], [S-KCA-SETTLE] |
| 교육훈련 | 공종별 hold-point, 반복하자 재교육, punch-list 사진대장 | [S-KCA-NEWAPT] |

## Use Limits

- 공사비 증액·정비사업 사례 중 뉴스가 주 source인 행은 DB v0.1의 research lead로만 둔다. `claim-ledger.md`의 CLM-0009처럼 미확정으로 분류된 claim은 최종 매뉴얼 의무통제로 쓰지 않는다.
- PF 통합정보시스템의 전국 의무 go-live는 확정하지 못했다. 따라서 현재 매뉴얼에는 데이터 표준화 준비 통제로만 반영하고, 의무 입력 통제는 후속 고시 확인 전까지 보류한다 [CLM-0018].
- 기존 v1.0 원본은 보존되었고, 모든 `manual_gap`은 G003 정밀감사에서 v1.0 section/paragraph와 다시 대조해야 한다.

## Next Manual Chapters To Add

1. PF 자본구조와 보증의존도 chapter
2. 토지 DD red-flag chapter
3. 인허가·민원 stakeholder chapter
4. 분양광고·HUG·환급 SOP chapter
5. 공사비·책임준공·신탁 chapter
6. 세무·회계·SPC chapter
7. 데이터룸·개인정보·증빙보존 chapter
8. 부동산개발업 컴플라이언스 chapter
9. 준공 후 정산·하자·교육훈련 chapter

## Evidence Status

DB v0.1 includes 64 distinct rows, with more than 30 Korea-related rows and more than 10 primary or overseas/comparative rows. All rows carry `phase`, `failure_mode`, `root_cause`, `early_warning_signal`, `manual_gap`, `control_to_add`, `source_refs`, and `confidence`.
