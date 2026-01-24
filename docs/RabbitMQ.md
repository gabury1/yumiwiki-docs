---
title: RabbitMQ
aliases: ["rabbitmq", "래빗엠큐", "토끼", "message queue"]
---

# RabbitMQ

> 안정적인 메시지 큐가 필요할 때

[[오픈소스]] [[메시지 브로커]]다. 2007년에 나왔고, [[Erlang]]으로 만들어졌다. [[AMQP]] 프로토콜 기반이라 다양한 언어/플랫폼에서 쓸 수 있다.

전통적인 메시지 큐 패턴에 충실하다. 프로듀서가 메시지 보내고, 큐에 쌓이고, 컨슈머가 가져간다. 메시지 전달 보장이 확실하다.

[[Kafka]]보다 단순하다. 설치도 쉽고, 관리도 쉽다. [[Docker]]로 띄우면 바로 쓸 수 있다. 처리량이 극단적으로 높지 않다면 RabbitMQ로 충분하다.

비동기 작업 처리, 서비스 간 통신, 이메일 발송, 알림 시스템 등에 많이 쓴다.

## 성능

초당 수만 건 메시지 처리 가능. [[Kafka]]보다는 적지만 대부분의 서비스에서 충분하다. 메시지가 작고 단순하면 더 빠르다.

메시지를 메모리에 저장하다가 디스크로 내린다. 영속성(durable) 설정하면 재시작해도 메시지 유지. 다만 디스크 쓰기는 성능에 영향.

클러스터링으로 고가용성 구성 가능. 미러링(Classic Mirroring)이나 Quorum Queue로 복제. 노드 하나 죽어도 서비스 유지.

메모리 관리 중요하다. 메시지가 쌓이면 메모리 압박. 기본적으로 40% 넘으면 프로듀서 블로킹. 컨슈머가 처리 못 따라가면 문제.

## 생태계

다양한 프로토콜 지원: [[AMQP]], [[MQTT]], [[STOMP]], HTTP. IoT, 웹소켓, 레거시 시스템 다 연결 가능.

관리 UI가 내장되어 있다. 15672 포트로 접속하면 큐 상태, 메시지 수, 컨슈머 상황 다 보인다. 메시지 직접 발행/조회도 가능.

[[Celery]]가 RabbitMQ를 기본 브로커로 쓴다. [[Python]] 비동기 작업 처리할 때 Celery + RabbitMQ 조합 많이 씀.

클라이언트: [[Java]]는 공식 클라이언트, [[Python]]은 [[pika]], [[Node.js]]는 [[amqplib]]. [[Spring AMQP]]로 스프링 통합.

매니지드: [[Amazon MQ]], [[CloudAMQP]]. 직접 운영해도 [[Kafka]]보다는 쉽다.

## 주의점

**Exchange와 Binding 이해**: 프로듀서는 Exchange로 보내고, Exchange가 라우팅 규칙(Binding)에 따라 큐로 전달한다. Direct, Fanout, Topic, Headers 타입이 있다. 처음엔 헷갈릴 수 있음.

**ACK 제대로 하기**: 컨슈머가 메시지 받고 ACK 안 보내면 requeue된다. 예외 터지면 ACK 안 됨. auto_ack 쓰면 편하지만 메시지 손실 가능. manual ACK 권장.

**Dead Letter Queue 설정**: 처리 실패한 메시지 버리면 안 됨. DLQ로 보내서 나중에 분석하거나 재처리. TTL, max-length 초과 메시지도 DLQ로.

**Prefetch 설정**: 컨슈머가 한 번에 가져가는 메시지 수. 너무 크면 다른 컨슈머가 놀고, 너무 작으면 왕복 오버헤드. 보통 10~100 사이로 튜닝.

**메모리 터지면 멈춤**: 메시지 쌓이면 메모리 한계 도달. `vm_memory_high_watermark` 설정 확인. 프로듀서 블로킹되면 전체 시스템 영향.

**클러스터 네트워크 파티션**: 노드 간 네트워크 끊기면 스플릿 브레인 발생 가능. `cluster_partition_handling` 설정 확인.

**Quorum Queue 사용**: 새로운 복제 방식. Classic Mirroring보다 안정적. 새 프로젝트면 Quorum Queue 쓰자.

## 주요 기능

- 다양한 Exchange 타입 (Direct, Fanout, Topic, Headers)
- 메시지 영속성 (Durable Queue, Persistent Message)
- 메시지 확인 (Publisher Confirms, Consumer ACK)
- Dead Letter Exchange
- TTL (메시지/큐 만료)
- Priority Queue
- 클러스터링, 미러링 (고가용성)
- 관리 UI 내장
- 다중 프로토콜 지원 (AMQP, MQTT, STOMP)

## 기타

RabbitMQ는 [[Erlang]]으로 만들어졌다. Erlang은 통신 시스템을 위해 설계된 언어라 고가용성, 동시성 처리가 뛰어나다. 덕분에 RabbitMQ도 안정성이 좋다. Erlang 모르는 개발자는 RabbitMQ 코드 읽기 어렵다는 게 단점이긴 하다.

2007년 Rabbit Technologies라는 회사에서 시작했다. 2010년 SpringSource에 인수됐고, 2013년 Pivotal로 넘어갔다가, 2019년 VMware가 Pivotal을 인수하면서 VMware 소유가 됐다. 회사는 여러 번 바뀌었지만 오픈소스 프로젝트는 계속 유지됐다.

관리 UI가 기본 제공되는 게 큰 장점이다. [[Kafka]]는 별도 도구 설치해야 하는데, RabbitMQ는 웹 브라우저로 바로 큐 상태를 볼 수 있다. 운영자 입장에서 편하다. 메시지 직접 발행/조회도 GUI로 가능.

[[Celery]] 기본 브로커가 RabbitMQ다. [[Python]] 개발자들은 "비동기 작업 = Celery + RabbitMQ"라는 공식에 익숙하다. [[Django]] 프로젝트에서 이메일 발송, 이미지 처리 같은 걸 백그라운드로 돌릴 때 표준 스택이다.
