# plugin-trace

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://github.com/jungcollin/plugin-trace)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Claude Code 플러그인: **실행 추적(Trace) 시스템**

작업 내용을 구조화된 JSON으로 기록하고, 시각화된 HTML 대시보드로 변환합니다.

## 설치

### 방법 1: 마켓플레이스 등록 (권장)

`~/.claude/settings.json`에 마켓플레이스 추가:

```json
{
  "extraKnownMarketplaces": {
    "plugin-trace": {
      "source": {
        "source": "github",
        "repo": "jungcollin/plugin-trace"
      }
    }
  },
  "enabledPlugins": {
    "trace@plugin-trace": true
  }
}
```

### 방법 2: CLI 설치

```bash
claude /install-skill https://github.com/jungcollin/plugin-trace
```

## 사용법

```
/trace <요청>
```

예시:
```
/trace 오늘 뉴스 요약해줘
/trace 이 코드 리팩토링해줘
```

## 워크플로우

```
/trace <요청>
    ↓
1. init_trace.py → 스텁 파일 생성
    ↓
2. 작업 수행 → trace.json 완성
    ↓
3. generate_html.py → HTML 대시보드 생성
```

## 플러그인 구조

```
plugin-trace/
├── .claude-plugin/
│   └── marketplace.json      # 마켓플레이스 메타데이터
├── plugin.json               # 플러그인 정의
├── skills/
│   └── trace/
│       ├── SKILL.md          # 스킬 정의
│       ├── scripts/
│       │   ├── init_trace.py
│       │   └── generate_html.py
│       └── templates/
│           └── trace_template.html
└── README.md
```

## 스크립트

### init_trace.py
타임스탬프 기반 스텁 파일 생성

```bash
python3 skills/trace/scripts/init_trace.py "요청 요약" --output-dir ./output
```

### generate_html.py
trace.json을 HTML 대시보드로 변환

```bash
python3 skills/trace/scripts/generate_html.py <trace.json 경로>
```

## 출력 파일

| 파일 | 설명 |
|------|------|
| `<T>_<S>_trace.json` | 실행 추적 메타데이터 |
| `<T>_<S>_trace.html` | 시각화된 대시보드 |
| `<T>_<S>.md` | 작업 결과물 문서 |

> `<T>` = YYYYMMDDHHmm 형식 타임스탬프
> `<S>` = 요청 요약 (파일명용)

## 라이선스

MIT
