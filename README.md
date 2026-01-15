# jungcollin-plugins

jungcollin의 Claude Code 플러그인 마켓플레이스입니다.

## 플러그인 목록

| 플러그인 | 설명 |
|----------|------|
| [simple-kitchen](./simple-kitchen) | 후덕죽셰프(중식)와 손종원셰프(양식)의 요리 플러그인 |
| [premium-kitchen](./premium-kitchen) | 최강록셰프(일식)와 요리괴물셰프(양식)의 프리미엄 요리 플러그인 |

## 설치

### 마켓플레이스 등록

```
/plugin marketplace add jungcollin/plugin-demo
```

### 개별 플러그인 설치

```
/plugin install simple-kitchen@jungcollin
/plugin install premium-kitchen@jungcollin
```

## 구조

```
.
├── .claude-plugin/
│   └── marketplace.json        # 마켓플레이스 설정
├── simple-kitchen/             # 심플 키친 플러그인
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── agents/                 # 후덕죽셰프, 손종원셰프
│   └── skills/                 # 중식, 웍, 양식 스킬
└── premium-kitchen/            # 프리미엄 키친 플러그인
    ├── .claude-plugin/
    │   └── plugin.json
    ├── agents/                 # 최강록셰프, 요리괴물셰프
    └── skills/                 # 일식, 양식 스킬
```

## 라이선스

MIT
