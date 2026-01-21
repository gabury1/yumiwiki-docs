# YumiWiki 문서 자동 생성 작업

## 필수 사전 작업

**작업 시작 전 반드시 prompts 폴더의 모든 파일을 읽어라:**

1. `prompts/Classification.md` - 문서 유형 분류 기준
2. `prompts/Concept.md` - 개념 문서 작성 프롬프트
3. `prompts/Mechanism.md` - 메커니즘 문서 작성 프롬프트
4. `prompts/Standard.md` - 기술/표준 문서 작성 프롬프트
5. `prompts/Implementation.md` - 구현체 문서 작성 프롬프트

이 파일들을 읽어야 문서의 톤, 구조, 작성 규칙을 정확히 따를 수 있다.

---

## 작업 개요

두 가지 작업을 수행한다:

1. **작업 1**: 생성할 문서 목록 정하기
2. **작업 2**: 문서 생성하기

---

## 작업 1: 생성할 문서 목록 정하기

### 목적
백엔드/프론트엔드 IT 기술 용어 목록을 대량으로 제안

### 진행 방식
1. 4가지 유형(concept, mechanism, standard, implementation)을 골고루 포함
2. 주니어 개발자가 알아야 할 핵심 용어 위주로 선정
3. 사용자 확인 후 `documents_to_create.txt`에 `- [ ] 용어명` 형식으로 추가

### 제안 기준
- 백엔드: 서버, DB, API, 인프라, 보안 등
- 프론트엔드: UI, 상태관리, 빌드, 렌더링 등
- 공통: 네트워크, 프로토콜, 개발도구 등

---

## 작업 2: 문서 생성하기

`documents_to_create.txt` 파일에 나열된 문서들을 순차적으로 생성하고, 완료 후 보고서 작성

### 워크플로우

각 문서마다 다음 순서로 진행:

### 1. 목록 확인
`documents_to_create.txt` 파일을 읽고 체크되지 않은 첫 번째 문서 선택

### 2. 분류 단계
`prompts/classification.md` 프롬프트를 읽고 문서 제목을 concept/mechanism/standard/implementation 중 하나로 분류

### 3. 작성 단계
분류 결과에 따라 해당 프롬프트 파일을 읽고 문서 작성:
- concept → `prompts/concept.md`
- mechanism → `prompts/mechanism.md`
- standard → `prompts/standard.md`
- implementation → `prompts/implementation.md`

### 4. 저장 단계
생성된 마크다운 문서를 `docs/{제목}.md`로 저장

### 5. 체크 단계
`documents_to_create.txt`에서 해당 항목을 `- [x]`로 변경

### 6. 반복
모든 항목이 체크될 때까지 1-5 반복

---

## 완료 후 작업

모든 문서 생성 완료 시:

1. `reports/batch_report.md`에 보고서 작성 (아래 템플릿 참고)

---

## 보고서 템플릿
```markdown
# YumiWiki 문서 생성 보고서

## 작업 개요
- 시작 시각: YYYY-MM-DD HH:MM:SS
- 종료 시각: YYYY-MM-DD HH:MM:SS
- 총 소요 시간: X분 Y초

## 생성 결과
- 총 문서 수: X개
- 성공: X개
- 실패: X개

## 문서별 상세

### nginx
- 분류: implementation
- 파일: nginx.md
- 상태: ✅ 성공
- 포함 섹션: 성능, 생태계, 주요 기능
- 특이사항: 없음

### claude
- 분류: implementation
- 파일: claude.md
- 상태: ✅ 성공
- 포함 섹션: 생태계, 비용, 주요 기능
- 특이사항: 없음

### mysql
- 분류: implementation
- 파일: mysql.md
- 상태: ✅ 성공
- 포함 섹션: 성능, 생태계, 주요 기능
- 특이사항: 없음

## 이슈 및 주의사항

(발생한 이슈나 주의할 점 기록)

## 다음 단계 제안

(추가로 생성하면 좋을 문서나 개선 사항 제안)
```

---

## 중요 규칙

1. **출력 형식**: 각 문서는 반드시 마크다운만 출력. 설명이나 주석 없이 바로 마크다운으로 시작
2. **frontmatter 필수**: 모든 문서는 `---\naliases: [...]\n---`로 시작
3. **wiki 링크 사용**: `[[문서명]]` 형식으로 관련 개념 연결
4. **섹션 구조화**: `##` 헤더로 본문 구분, 한 덩어리 텍스트 금지
5. **한 줄 요약**: `#` 제목 바로 다음 줄에 `>` 인용문으로 요약

---

## 디렉토리 구조

```text
yumiwiki_docs/
├── claude/
│   ├── CLAUDE.md (이 파일)
│   ├── documents_to_create.txt
│   └── prompts/
│       ├── Classification.md
│       ├── Concept.md
│       ├── Mechanism.md
│       ├── Standard.md
│       └── Implementation.md
├── docs/
│   ├── nginx.md
│   ├── django.md
│   └── ...
└── reports/
    └── batch_report.md
```