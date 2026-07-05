# Claim Ledger v0.1

작성일: 2026-07-05  
규칙: `verdict=unresolved`인 high-risk claim은 연구 backlog에는 남기되, `SYNTHESIS.md`의 확정 통제나 최종 매뉴얼 의무조항으로 사용하지 않는다.

| claim_id | case_id | exact_assertion | risk_class | supporting_sources | counter_search | primary_source_status | verdict | allowed_downstream_use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CLM-0001 | KR-PF-001 | 태영건설 워크아웃은 PF 보증·유동성 리스크를 사업장별 현금흐름과 건설사 신용에서 분리해 관리해야 함을 보여준다. | financial | S-FSC-TY-20231228; S-FSC-TY-20240108 | FSC 발표는 최종 종결 문서가 아님을 확인 | primary-confirmed | verified | manual-control |
| CLM-0002 | POLICY-PF-CAPITAL | 한국 PF의 구조적 취약점은 낮은 자기자본과 보증 의존이라는 정책·연구기관 공통 진단으로 볼 수 있다. | policy | S-KDI-PF-2024; S-KDI-PF-2025 | KDI는 정책 제언 성격이므로 개별 사건 원인으로 직접 전이하지 않음 | primary-confirmed | verified | context-and-control |
| CLM-0003 | KR-PF-002 | 해외 개발 PF는 국가위험도, 수요검증, 인허가, 담보권 확보를 독립 승인조건으로 분리해야 한다. | financial | S-LAW-168694; S-LAW-168810 | 판례 사건군 내 사실관계와 최종심 연결은 추가 정규화 필요 | primary-confirmed | verified | manual-control |
| CLM-0004 | KR-PF-009 | 책임준공 약정은 PF 대주단 손해배상·보증성 리스크로 확대될 수 있으므로 별도 익스포저 한도를 둬야 한다. | legal-financial | S-LAW-179847; S-LAW-207164 | 개별 사업장 손실액은 판례별 재확인 필요 | primary-confirmed | verified | manual-control |
| CLM-0005 | KR-SALES-001 | 분양광고·모델하우스 설명 중 구체적 거래조건은 계약내용 또는 손해배상 쟁점이 될 수 있다. | legal | S-LAW-70656; S-LAW-167291 | 일반 홍보문구와 구체 조건을 구별해야 함 | primary-confirmed | verified | manual-control |
| CLM-0006 | KR-HUG-001 | HUG 분양보증 사고는 분양이행·환급이행 의사결정과 사고금액 API를 분리해 관리해야 한다. | legal-financial | S-HUG-NOTICE-37172; S-DATA-HUG-15058809; S-DATA-HUG-15002597 | live notice와 annual/API 데이터 기준시점이 다름 | primary-confirmed | verified | manual-control |
| CLM-0007 | KR-LAND-001 | 토지 DD는 유치권·분묘기지권·문화재·접도·가등기·토양오염·지장물을 별도 중단조건으로 다뤄야 한다. | legal-operational | S-LAW-211437; S-LAW-2011DA63017; S-LAW-157317; S-LAW-DRF258067; S-LAW-222877; S-LAW-606215; S-SCOURT-8916 | 일부 사건의 개발사업 직접성은 낮아 통제 근거로만 사용 | primary-confirmed | verified | manual-control |
| CLM-0008 | KR-PERMIT-001 | 도시계획위원회 보류, 장기 보류, 주민 반대, 입안제안 반려는 인허가 전 이해관계자·대안안 관리 게이트가 필요함을 보여준다. | operational-policy | S-SEOUL-17032; S-SEOUL-514958; S-LAW-206096; S-LAW-78216; S-LAW-DECC155457 | 회의록·판례별 맥락이 달라 동일 원인으로 단정하지 않음 | primary-confirmed | verified | manual-control |
| CLM-0009 | KR-CONST-001 | 공사비 증액·공기 지연·책임준공 분쟁은 GMP/물가연동/독립 QS/stop-draw 조건으로 관리해야 한다. | financial-operational | S-EKN-BANGHWA; S-MK-JANGWI; S-BP-DUNCHON; S-EDAILY-MAPLE; S-BLOTER-DAEJO; S-JIPYONG-14113; S-JIPYONG-14838 | 다수 뉴스 source라 조합·공시·판결 원문 추가 필요 | secondary-only | unresolved | research-backlog |
| CLM-0010 | KR-GOV-001 | 시행사 내부통제 실패는 외부투자·관련당사자·자금집행·공시통제 승인 매트릭스가 필요함을 보여준다. | legal-financial | S-DART-MEDICOX; S-LAWTIMES-BAEKHYEON; S-DOBONG-CHANGDONG; S-DART-DAEWOO | 형사 판결문·DART 접수번호 확정 전 원인 단정 금지 | mixed | unresolved | research-backlog |
| CLM-0011 | KR-TAX-001 | 취득세 과세표준과 자문수수료·공사비 분류는 개발사업 closing 전 세무 memo와 cost taxonomy로 잠가야 한다. | tax | S-LAW-616043; S-LAW-419232 | 사건별 비용 범주를 그대로 일반화하지 않음 | primary-confirmed | verified | manual-control |
| CLM-0012 | KR-TAX-003 | 혼합 과세·면세 부동산 프로젝트는 VAT 공통매입세액 안분 로직을 독립 검토해야 한다. | tax | S-LAW-VAT-2012GUHAP18936 | 최신 법령·예규 확인 필요 | primary-confirmed | verified | manual-control |
| CLM-0013 | KR-TAX-004 | 세무신고 편의를 이유로 계약서 형식을 바꾸는 관행은 실질·증빙 불일치 리스크로 관리해야 한다. | tax-legal | S-LAW-213649 | 개발사업 직접성은 중간 수준 | primary-confirmed | verified | manual-control |
| CLM-0014 | KR-DATA-001 | 확인실사와 최종계약 일정은 data-room signoff와 version freeze 없이는 분쟁화될 수 있다. | legal-operational | S-LAW-DD-2009GAHAP132342 | M&A 사례를 부동산 PF VDR에 적용하는 것은 유추임 | primary-confirmed | verified | manual-control |
| CLM-0015 | KR-DATA-002 | 개인정보·문서관리 실패는 외부접근 제한, 암호화, 보존기간, 파기, 72시간 신고 SOP가 필요함을 보여준다. | privacy | S-PIPC-12010; S-PIPC-12066; S-PIPC-10853; S-PIPC-11453; S-PIPC-11923 | 부동산 sales office와 직접 동일하지 않은 사건도 있음 | primary-confirmed | verified | manual-control |
| CLM-0016 | KR-COMP-001 | 부동산개발업 사업실적보고, 인력·사무실 요건, 변경보고는 현재 시행 중인 필수 통제다. | legal-policy | S-KDA-REPORT; S-KDA-REG; S-LAW-DEVLAW; S-LAW-DEVENFORCE; S-LAW-DEVQUAL | 관할·서식은 매년 재확인 필요 | primary-confirmed | verified | manual-control |
| CLM-0017 | POLICY-MGMT-LAW | 부동산개발사업 관리 등에 관한 법률은 2026-05-28 시행 기준으로 준비 통제와 시행 이후 의무 통제를 구분해야 한다. | policy | S-LAW-MGMT-20977; S-MOLIT-MGMT-20250501 | 시행령·시행규칙 조문별 실제 의무 개시일 추가 대조 필요 | primary-confirmed | verified | phased-control |
| CLM-0018 | POLICY-PF-SYSTEM | PF 통합정보시스템의 전국 단위 강행 go-live와 의무 입력 개시일은 이번 조사에서 확정하지 못했다. | policy | S-KDI-PF-2025 | FSC/MOLIT 후속 고시 확인 필요 | unavailable | unresolved | research-backlog |
| CLM-0019 | KR-CLOSE-001 | 준공 후 하자·환급·계약해제 분쟁은 defect triage, refund SLA, settlement waterfall로 사전 통제해야 한다. | operational-legal | S-KCA-NEWAPT; S-KCA-TRUST; S-KCA-SETTLE | 개별 사업장별 법적 책임은 별도 확인 필요 | primary-confirmed | verified | manual-control |
| CLM-0020 | KR-TRAIN-001 | 신축 공동주택 하자 반복은 trade별 검수·재교육·hold-point 승인 통제가 필요한 교육훈련 시나리오다. | operational | S-KCA-NEWAPT | 직접 training failure 판례는 부족함 | secondary-by-symptom | verified | training-scenario |
| CLM-0021 | US-COMP-002 | HVCRE/ADC와 미국 부동산 대출 기준은 PF에 repayment-source classification, equity lock-up, presale/prelease gate를 적용하는 비교 benchmark다. | financial-policy | S-ECFR-HVCRE; S-ECFR-LENDING; S-FDIC-CRISIS | 한국에 그대로 법제화된 것은 아님 | primary-confirmed | verified | comparative-control |
| CLM-0022 | AU-COMP-001 | APRA의 ADC·presale quality 관점은 선분양 숫자가 아니라 계약 품질을 검증해야 함을 보여준다. | financial-policy | S-APRA-APS112; S-APRA-APG112 | 100% presale은 보편 법정 최소치가 아니라 감독 기대·시장관행 문맥 | primary-confirmed | verified | comparative-control |
| CLM-0023 | UK-COMP-001 | Homes England/GLA grant controls는 milestone draw, incurred cost, scheme file, compliance audit를 정책금융 통제로 전환할 수 있다. | operational-policy | S-GOVUK-CFG; S-GLA-AUDIT | 보조금 규율이므로 민간 PF에 직접 이식하지 않음 | primary-confirmed | verified | comparative-control |
| CLM-0024 | JP-NL-COMP | Japan MLIT와 Netherlands DNB 사례는 site technical gate와 loan-level reporting layer가 필요함을 보여준다. | policy-operational | S-MLIT-JP-DEVPERMIT; S-DNB-CRE | 금융 underwriting rule이 아닌 행정·감독 infrastructure | primary-confirmed | verified | comparative-control |
