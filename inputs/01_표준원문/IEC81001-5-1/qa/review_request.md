---
standard_id: IEC81001-5-1
version: "2021"
generated_at: "2026-06-18"
status: pending_review
---

# IEC 81001-5-1 인제스트 검토 요청

## 요약

| 항목 | 값 |
|---|---|
| 총 조항 | 61개 (리프 규범 조항) |
| 요건 추출 | 95건 (shall 91 + should 4) |
| 용어 정의 | 48건 |
| Annex F (normative) | 8건 포함 |
| 검토 필요 | 11건 (복합 shall 문장) |

## ⚠️ 복합 shall 문장 — 분리 여부 검토 (11건)

### 우선 검토 (shall 4회)

- [x] **IEC81001-5-1-5.7.3-REQ-001** (§5.7.3)
  → VULNERABILITY testing 관련 4개 shall 문장 포함. 분리 필요 여부 판단.

### 일반 검토 (shall 2회)

- [x] **IEC81001-5-1-4.2-REQ-001** (§4.2)
  → Security risk management 프로세스 수립 관련.

- [x] **IEC81001-5-1-4.2-REQ-002** (§4.2)
  → Risk management 활동 관련.

- [x] **IEC81001-5-1-4.2-REQ-004** (§4.2)
  → Risk evaluation 관련.

- [x] **IEC81001-5-1-5.2.2-REQ-002** (§5.2.2)
  → Security requirements review 관련.

- [x] **IEC81001-5-1-5.7.1-REQ-001** (§5.7.1)
  → Security requirements testing 관련.

- [x] **IEC81001-5-1-5.7.2-REQ-001** (§5.7.2)
  → Threat mitigation testing 관련.

- [x] **IEC81001-5-1-6.3.1-REQ-001** (§6.3.1)
  → Security update documentation 관련.

- [x] **IEC81001-5-1-7.2-REQ-001** (§7.2)
  → Vulnerability/threat identification 관련.

- [x] **IEC81001-5-1-7.2-REQ-002** (§7.2)
  → Threat identification 관련.

- [x] **IEC81001-5-1-9.5-REQ-005** (§9.5)
  → Security-related issue addressing 관련.

## ℹ️ 미커버 조항 (정상)

| 조항 | 사유 |
|---|---|
| 9.1 Overview | 요구사항 없는 서론 절 — 정상 |
| F.1 Overview | 요구사항 없는 서론 절 — 정상 |

## ℹ️ 품질 정보

- 추출 실패 페이지: 없음 (58/58 성공)
- 원문 매핑 미완료: 2건 (Annex F 일부)
- 전체 추출 품질: **양호**

## 검토 방법

1. 이 파일의 체크박스를 완료 표시하거나, 분리가 불필요한 항목은 그대로 두세요
2. 필요 시 `requirements.yaml` 직접 수정 가능
3. 검토 완료 후 실행:

```
/process-ingest --confirm IEC81001-5-1
```
