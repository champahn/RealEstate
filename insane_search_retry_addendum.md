# Insane-search 재시도 보강 Addendum

작성일: 2026-07-05

## 목적

이 addendum은 이전 작업에서 aside-browser가 접근하지 못해 `Aside 재검증 필요`로 남겨둔 국토교통부 공식 보도자료를 insane-search 계열 Tier 1 fetch로 재시도한 결과를 기록한다.

## 대상

| 항목 | 값 |
| --- | --- |
| 공식 페이지 | `https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?id=95092133&lcmspage=1` |
| 국토부 등록일 | 2026-06-18 11:00 |
| 제목 | 빅데이터·AI로 혁신하고, 신뢰는 높인다 「제2차 부동산서비스산업 진흥 기본계획」 수립 |
| 첨부 PDF | `제2차(’26~’30) 부동산서비스산업 진흥 기본계획.pdf` |

## 재시도 결과

| 단계 | 결과 |
| --- | --- |
| GitHub repo 검토 | `fivetaku/insane-search` clone HEAD `2714e72282b915c6983723652d0c365af08e9e1f` 확인 |
| Codex 실행 경로 | bundled `ultimate-browsing/engine` 사용 |
| 최초 실행 | `curl_cffi not installed`로 실패 |
| 보강 조치 | `python3 -m pip install --user curl_cffi` 성공 |
| 재실행 | `curl_cffi safari + original + referer:self_root -> weak_ok` |
| HTTP status | 200 |
| HTML body size | 60033 bytes |
| 첨부 PDF 다운로드 | 200, 4133300 bytes, `%PDF` header true |
| PDF SHA256 | `dc9c56d4278cb5a489e038138daf3d93cb24bee554bce4ed064c315fc8d77431` |
| PDF text extraction | external PDF `page_count=40`, `실적 확인제` found on pages 29, 30, 40 |

## 산출물 반영 판단

`부동산 개발사업 실적 확인제` 항목은 더 이상 `Aside 재검증 필요` 상태가 아니다. 국토교통부 공식 보도자료 HTML과 공식 첨부 PDF를 통해 다음 두 가지가 확인되었다.

1. 2026-06-18 국토교통부 보도자료는 `제2차 부동산서비스산업 진흥 기본계획` 수립 및 6월 19일 고시 예정임을 확인한다.
2. 공식 첨부 PDF는 `사업실적 확인제` 도입 방향을 포함한다.

다만 이 확인은 `사업실적 확인제` 도입 방향의 확인이다. 세부 시행일, 제출항목, 서식, 주관기관 운영 절차는 후속 고시·협회 안내·법령 개정문에서 별도 확정해야 한다.

## 원본 보존

이 addendum 작성 중 원본 v1.0 DOCX, 원본 백업 DOCX, Obsidian 20_WIKI 원천 파일, 매뉴얼 본문은 편집하지 않았다. 반영 대상은 후속 실행 플랜과 최신성 tracker뿐이다.
