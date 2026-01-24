---
title: Rust
aliases: ["rust", "rustlang", "러스트"]
---

# Rust

> 메모리 안전하면서도 C/C++ 수준의 성능이 필요할 때

2010년 Mozilla에서 시작된 시스템 프로그래밍 언어다. "안전하고, 빠르고, 동시성"을 목표로 한다. [[C]]/[[C++]]의 메모리 버그 없이 같은 수준의 성능을 낸다. 가비지 컬렉션 없이 메모리 안전성을 보장하는 게 핵심 혁신.

Firefox의 일부(Servo, Stylo), Linux 커널, Cloudflare, Discord, Dropbox에서 쓰인다. Stack Overflow에서 7년 연속 "가장 사랑받는 언어" 1위.

## 탄생 배경

2006년 Mozilla 직원 Graydon Hoare가 개인 프로젝트로 시작. 엘리베이터가 고장났는데 소프트웨어 버그 때문이었다. "메모리 안전한 시스템 언어"를 만들기로 했다.

2009년 Mozilla가 공식 후원. Firefox 브라우저의 성능과 보안 개선이 목적이었다. 2015년 Rust 1.0 출시.

## 특징

**소유권(Ownership)**: Rust의 핵심. 모든 값은 하나의 소유자만 가진다. 소유자가 스코프를 벗어나면 자동 해제. GC 없이 메모리 관리.

**빌림(Borrowing)**: 소유권 이전 없이 참조. 불변 참조는 여러 개, 가변 참조는 하나만. 컴파일 타임에 검증.

**수명(Lifetime)**: 참조가 유효한 범위를 명시. 댕글링 포인터 컴파일 타임에 방지.

**Zero-cost Abstractions**: 추상화 사용해도 런타임 비용 없음. [[C++]]의 철학 계승.

**패턴 매칭**: `match` 표현식. 모든 경우를 처리해야 컴파일됨. 버그 예방.

**타입 시스템**: 대수적 데이터 타입(enum), Option, Result로 null/에러 처리.

## 성능

[[C]]/[[C++]]와 동급. GC 없어서 지연 시간 예측 가능.

LLVM 백엔드 사용. 최적화 수준 높음.

추상화 비용 없음. Iterator, closure 써도 수동 루프와 같은 성능.

## 생태계

**패키지 관리**: Cargo (빌드, 의존성, 테스트, 문서 통합)

**웹**: Actix, Axum, Rocket

**비동기**: Tokio, async-std

**CLI**: clap, structopt

**WebAssembly**: Rust → Wasm 변환 쉬움

**임베디드**: no_std로 OS 없이 동작

**주요 프로젝트**: ripgrep, fd, exa, Alacritty, Deno

## 주의점

**학습 곡선**: 소유권, 빌림, 수명 개념이 처음엔 어렵다. "Rust와 싸우다"라는 표현이 있을 정도.

**컴파일 시간**: [[Go]]보다 느리다. 대규모 프로젝트에서 체감됨. 증분 컴파일로 완화.

**생태계 성숙도**: [[Python]], [[Java]]보다 라이브러리 적다. 빠르게 성장 중이지만.

**비동기 복잡성**: async/await 있지만 Pin, lifetime과 결합하면 복잡. 에러 메시지도 어렵다.

**GUI**: 아직 성숙한 GUI 프레임워크 없음. Tauri, egui 등 성장 중.

## 주요 기능

- 소유권, 빌림, 수명 (메모리 안전)
- Option, Result (null/에러 처리)
- Pattern matching (match)
- Traits (인터페이스)
- Generics (제네릭)
- Macros (메타프로그래밍)
- Cargo (패키지 관리자)
- 크로스 컴파일 지원

## 기타

Rust는 녹(rust)을 의미한다. 로고도 녹처럼 생긴 톱니바퀴. "안전하지 않은 C/C++에 녹이 슬었다"는 의미라는 설도 있고, 그냥 짧고 검색하기 쉬운 이름이라는 설도 있다.

"Rewrite it in Rust"(RIIR)라는 밈이 있다. Rust 열성 팬들이 모든 프로젝트를 Rust로 다시 쓰자고 하는 걸 비꼰 것. 실제로 coreutils, grep 등 유닉스 도구들이 Rust로 재작성되고 있다.

2023년 Linux 커널 6.1에 Rust가 공식 포함됐다. [[C]] 외 언어가 커널에 들어간 역사적 사건. 드라이버 개발에 Rust를 쓸 수 있게 됐다.

Microsoft, Google, AWS, Meta가 Rust를 적극 채택하고 있다. "메모리 안전 언어"로의 전환이 산업 트렌드가 됐고, Rust가 그 중심에 있다.

