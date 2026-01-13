---
name: trace
description: |
  실행 추적(Trace) 시스템. 모든 요청에 대해 trace.json과 HTML 대시보드를 강제 생성.
  "/trace <요청>" 형태로 호출하면 타임스탬프 기반 스텁 파일을 선생성하고 작업 수행.
  사용 시점: 작업 기록이 필요할 때, 실행 추적이 필요할 때, "/trace" 명령어 사용 시.
---

# Trace

실행 추적 시스템. 모든 작업을 구조화된 JSON + HTML 대시보드로 기록.

## 실행 흐름

```
/trace <요청>
    ↓
1. init_trace.py 실행 → <T>, 스텁 파일 생성
    ↓
2. 요청 작업 수행
    ↓
3. trace.json 완성 (TODO 항목 채우기)
    ↓
4. generate_html.py 실행 → HTML 대시보드 생성
    ↓
5. 검증 (파일 존재, 스키마 준수)
```

## 사용법

```
/trace 오늘 뉴스 요약해줘
/trace 이 코드 리팩토링해줘
```

## Step 1: 초기화

작업 시작 시 반드시 `scripts/init_trace.py` 실행:

```bash
python3 scripts/init_trace.py "<요청 요약>" --output-dir <프로젝트 경로>
```

출력:
- `<T>` (YYYYMMDDHHmm 형식 타임스탬프)
- `<T>_<S>_trace.json` 스텁 파일
- `<T>_<S>.md` 결과물 스텁 파일

## Step 2: 작업 수행

요청된 작업을 수행하고 결과물 파일(`<T>_<S>.md`)에 내용 작성.

## Step 3: trace.json 완성

스텁 파일의 TODO 항목을 실제 값으로 채움:

```json
{
  "schemaVersion": "1.0",
  "fileName": "<T>_<S>_trace.json",
  "runId": "<T>",
  "startTime": "YYYY-MM-DD HH:mm",
  "summary": "<요청 요약>",
  "status": "success | failure",
  "groupRelation": {
    "text": "그룹 간 관계 설명",
    "type": "sequential | parallel | dependency"
  },
  "groups": [
    {
      "number": "1",
      "type": "sequential",
      "info": "실행 설명",
      "tasks": [
        { "name": "작업명", "agent": "main", "status": "completed" }
      ]
    }
  ],
  "skills": [],
  "artifacts": [
    { "name": "<T>_<S>.md", "type": "MD" }
  ]
}
```

## Step 4: HTML 대시보드 생성

trace.json 완성 후 `scripts/generate_html.py` 실행:

```bash
python3 scripts/generate_html.py <T>_<S>_trace.json
```

출력:
- `<T>_<S>_trace.html` - 독립 실행형 HTML 대시보드

HTML 파일은 브라우저에서 바로 열어볼 수 있으며, trace 데이터가 내장되어 있음.

## 최종 산출물

| 파일 | 설명 |
|------|------|
| `<T>_<S>_trace.json` | 실행 추적 메타데이터 (JSON) |
| `<T>_<S>_trace.html` | 시각화된 대시보드 (HTML) |
| `<T>_<S>.md` | 작업 결과물 문서 |

## 필수 규칙

1. **단일 Trace**: Run당 trace.json은 정확히 1개
2. **타임스탬프 일관성**: 모든 파일에 동일한 `<T>` 사용
3. **필수 산출물**: trace.json 1개 + trace.html 1개 + 결과물 최소 1개
4. **그룹 관계 명시**: sequential/parallel/dependency 중 선택

## 실패 조건

- trace.json 2개 이상 생성
- trace.html 미생성
- 결과물 파일 0개
- `<T>` 불일치
- 그룹 관계 누락
