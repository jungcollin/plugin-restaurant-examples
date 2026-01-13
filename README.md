# jungcollin-plugins

jungcollin의 Claude Code 플러그인 마켓플레이스입니다.

## 플러그인 목록

| 플러그인 | 설명 |
|----------|------|
| [personal-restaurant](./personal-restaurant) | 요리 시뮬레이션. 서브에이전트와 스킬의 협업 패턴 예제 |
| [plugin-trace](./plugin-trace) | 실행 추적 시스템. JSON + HTML 대시보드로 작업 기록 |

## 설치

### 마켓플레이스 등록

```
/plugin marketplace add jungcollin/plugin-restaurant-examples
```

### 개별 플러그인 설치

```
/plugin install personal-restaurant@jungcollin
/plugin install plugin-trace@jungcollin
```

## 구조

```
.
├── .claude-plugin/
│   └── marketplace.json        # 마켓플레이스 설정
├── personal-restaurant/        # 요리 시뮬레이션 플러그인
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── agents/                 # 전문 셰프 (서브에이전트)
│   └── skills/                 # 비법 노트 (스킬)
└── plugin-trace/               # 실행 추적 플러그인
    ├── .claude-plugin/
    │   └── plugin.json
    └── skills/trace/           # trace 스킬
```

## 라이선스

MIT
