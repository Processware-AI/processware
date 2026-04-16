---
type: input_document
source_type: "{{source_type}}"       # standard_original | law | guide | as_is | industry
source_file: "{{원본파일명}}"
source_publisher: "{{발행기관}}"
source_year: "{{발행년도}}"
source_pages: "{{페이지범위}}"
clause: "{{조항번호}}"
clause_title: "{{조항명}}"
license: "{{라이선스}}"               # "ISO copyright — paraphrase only" | "공공저작물" | "내부 자산" 등
paraphrase_only: true
content_mode: "paraphrase"            # verbatim | paraphrase | summary
converted_at: "{{date}}"
converted_by: "{{작성자 or 도구}}"
tags: [input, "{{표준코드}}"]
---

# {{조항번호}} {{조항명}}

> 원본 출처: `{{원본파일명}}` {{페이지범위}}
> 발행: {{발행기관}} {{발행년도}}
> content_mode: **{{content_mode}}**

## 1. 요지 (paraphrase)
> ⚠️ `content_mode: paraphrase/summary` 인 경우만 사용. verbatim 은 원본 그대로.

(요약 내용)

## 2. 핵심 요구사항
- (의무/권고)
- 

## 3. 관련 조항
- 상위: [[{{상위조항}}]]
- 하위: [[{{하위조항}}]]
- 타 표준 매핑: 

## 4. 해설 / 주석 (선택)
(변환자가 추가한 해설. 원문과 구분되게 명시)

---

## 변환 체크리스트
- [ ] 조항번호·제목 정확
- [ ] content_mode 에 맞는 서술 (verbatim/paraphrase/summary)
- [ ] frontmatter 라이선스 기입
- [ ] source_pages 원본 대조 가능
- [ ] `content_mode: verbatim` 이면 저작권 보호 표기 (ISO 원문 등)
