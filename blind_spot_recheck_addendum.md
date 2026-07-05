# blind_spot_recheck_addendum

작성일: 2026-07-05T02:39:41.206182+00:00

G003 재점검 중 추가로 확인한 blind spot과 즉시 보강 조치입니다.

## G003-BS-A: Obsidian 20_WIKI/부동산개발_시스템 경로가 현재본 1개와 백업 4개로 분산되어 있어 단일 경로만 보면 최신/이전 차이를 놓칠 수 있음.

- status: reinforced
- reinforcement: obsidian_inventory.md에 5개 경로, 해시, mtime, heading/wiki-link 목록을 모두 기록; source preservation C003에서 현재본/백업 source 파일 무변경 검증 예정.
- carry_forward_to_g004: 플랜에는 canonical source path와 archive comparison policy를 포함.

## G003-BS-B: SYNTHESIS.md는 DB 64건이라고 적지만 실제 failure_case_db_v0.1.jsonl은 63행이며 G002 검증도 63건으로 통과함.

- status: reinforced
- reinforcement: manual_v1_gap_matrix.json은 실제 JSONL 63건을 기준으로 계산; G004에서 숫자 표기 정정/검증 항목으로 승격.
- carry_forward_to_g004: 최종 플랜에는 evidence count normalization을 작업항목으로 포함.

## G003-BS-C: v1.0은 실무 절차가 강하지만 원본 보존, 작업본, 변경이력, diff, 승인 로그가 문서 운영체계로 없음.

- status: reinforced
- reinforcement: C003 preservation criterion과 source_preservation_audit.md를 추가; G004에는 version governance chapter를 포함.
- carry_forward_to_g004: 매뉴얼 개정 전 original/read-only/source-of-truth policy를 첫 단계로 배치.

## G003-BS-D: G002 12축 중 개발업 컴플라이언스, 데이터룸·개인정보, 세무·회계·SPC, 교육훈련, 조직/RACI는 v1.0에서 독립 운영장으로 확인되지 않음.

- status: reinforced
- reinforcement: manual_v1_gap_matrix.json에서 MISSING으로 분류하고 각각 별도 chapter/control로 carry-forward 지정.
- carry_forward_to_g004: 종합 실행 플랜의 필수 보강 장으로 편입.
