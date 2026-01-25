---
title: Node.js
aliases: ["node", "nodejs", "node.js", "노드", "노드js"]
---

# Node.js

> JavaScript를 브라우저 밖으로 꺼내준 혁명적인 런타임

Chrome V8 엔진 기반의 [[JavaScript]] 런타임이다. Ryan Dahl이 2009년에 만들었다. **이벤트 기반**, **비동기 I/O** 모델을 사용하여 가볍고 효율적이다. 웹 서버부터 스크립팅 도구까지 광범위하게 쓰인다.

## 특징

**비동기 & 이벤트 루프**: 싱글 스레드 이벤트 루프([[Event Loop]])를 통해 [[비동기]] 작업을 처리한다. I/O 작업(파일, 네트워크)이 멈추지 않고(Non-blocking) 백그라운드에서 처리되므로, 높은 처리량(Throughput)을 감당할 수 있다.

**NPM 생태계**: 세계에서 가장 큰 패키지 저장소인 [[npm]]을 가진다. 필요한 거의 모든 라이브러리가 이미 존재한다.

**JavaScript 통일**: 프론트엔드([[React]], [[Vue]])와 백엔드([[Express]], [[NestJS]])를 같은 언어로 개발할 수 있다. "JavaScript Everywhere".

## 생태계

**프레임워크**: [[Express]](가장 대중적), [[NestJS]](엔터프라이즈급), [[Fastify]](성능 중시), [[Koa]].

**도구**: [[Webpack]], [[Vite]], [[Babel]] 등 모던 웹 개발 도구의 99%가 Node.js 위에서 돌아간다.

## 주의점

**CPU 집약적 작업**: 싱글 스레드라서 CPU를 오래 점유하는 계산(암호화, 압축 등)을 하면 전체 서버가 멈춘다(Blocking). 이런 작업은 워커 스레드나 다른 언어([[Go]], [[Rust]])로 위임해야 한다.

**에러 처리**: 콜백 헬(Callback Hell)은 `Promise`와 `async/await`로 해결됐지만, 예외 처리를 제대로 안 하면 프로세스가 툭 꺼질 수 있다. `uncaughtException` 관리가 중요.

## 기타

Ryan Dahl은 나중에 "Node.js에서 후회하는 10가지"를 발표하고 [[Deno]]라는 새로운 런타임을 만들었다(JavaScript/TypeScript 보안 런타임). 하지만 Node.js의 생태계는 여전히 압도적이다.

넷플릭스, 우버, 링크트인 등 수많은 글로벌 기업이 메인 백엔드로 사용 중이다.
