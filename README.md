# jungcollin-plugins

jungcollin의 Claude Code 플러그인 마켓플레이스입니다.

## 플러그인 목록

| 플러그인 | 설명 |
|----------|------|
| [simple-kitchen](./simple-kitchen) | 후덕죽셰프(중식)와 손종원셰프(양식)의 요리 플러그인 |

## 설치

### 마켓플레이스 등록

```
/plugin marketplace add jungcollin/plugin-demo
```

### 개별 플러그인 설치

```
/plugin install simple-kitchen@jungcollin
```

## simple-kitchen 상세

### 에이전트

| 에이전트 | 전문 분야 | 설명 |
|----------|-----------|------|
| 후덕죽셰프 | 중식 | 짜장면, 짬뽕, 탕수육 등 중화요리 전문. 화력과 웍 기술의 달인 |
| 손종원셰프 | 양식 | 스테이크, 파스타 등 서양요리 전문. 정통 프렌치 기법 |

### 스킬

| 스킬 | 설명 |
|------|------|
| common | 기본 위생 (손 씻기, 냉장/냉동 온도 관리) |
| chinese | 중식 조리법 (짜장면, 짬뽕, 탕수육) |
| wok | 웍 기술 (폭차오 300°C, 챠오 250°C) |
| western | 양식 조리법 (레어 50°C, 미디엄 60°C, 웰던 70°C) |

## 구조

```
.
├── .claude-plugin/
│   └── marketplace.json        # 마켓플레이스 설정
└── simple-kitchen/             # 심플 키친 플러그인
    ├── .claude-plugin/
    │   └── plugin.json
    ├── agents/
    │   ├── 후덕죽셰프.md       # 중식 전문 에이전트
    │   └── 손종원셰프.md       # 양식 전문 에이전트
    └── skills/
        ├── common/             # 기본 위생 스킬
        ├── chinese/            # 중식 조리법 스킬
        ├── wok/                # 웍 기술 스킬
        └── western/            # 양식 조리법 스킬
```

## 라이선스

MIT
