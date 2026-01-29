---
title: Caffeine
aliases: ["caffeine cache", "카페인 캐시", "java cache"]
---

# Caffeine (카페인)

> "성능에 미친 자들을 위한 Java용 고성능 캐시 라이브러리"

Caffeine은 Java 8 이상을 위한 고성능 캐싱 라이브러리다. Google Guava 캐시의 설계를 개선하여 더 높은 적중률과 압도적인 성능을 제공한다. 현재 [[Spring Boot]]의 기본 로컬 캐시 구현체로 널리 사용된다.

## 왜 쓰는가? (강점)

- **압도적 성능**: 거의 모든 벤치마크에서 Guava, Ehcache 등을 압도한다.
- **높은 적중률**: **Window TinyLFU**라는 정교한 퇴거(Eviction) 알고리즘을 사용하여, 메모리 효율성과 적중률을 동시에 잡았다.
- **다양한 기능**: 자동 로딩, 크기 기반 만료, 시간 기반 만료, 참조 기반 만료 등 풍부한 설정을 제공한다.
- **유연한 API**: 빌더 패턴을 사용하여 복잡한 캐시 정책을 쉽게 설정할 수 있다.

## 핵심 기능

### 1. 퇴거 정책 (Eviction)
- **크기 기반**: 캐시에 저장할 최대 항목 수를 지정한다. (`maximumSize`)
- **시간 기반**: 
  - `expireAfterAccess`: 마지막 접근 후 일정 시간이 지나면 삭제.
  - `expireAfterWrite`: 생성/수정 후 일정 시간이 지나면 삭제.
- **참조 기반**: GC가 수행될 때 메모리가 부족하면 삭제되도록 설정 가능 (Weak/Soft Reference).

### 2. 자동 로딩 (Loading)
캐시에 데이터가 없을 때, 소스(DB 등)에서 데이터를 가져오는 로직을 캐시에 내장할 수 있다. (`CacheLoader`)

### 3. 통계 (Statistics)
캐시 적중률(Hit Rate), 부하 시간, 퇴거 개수 등을 추적하여 최적화에 활용할 수 있다.

## 사용 예시 (Java)

```java
Cache<String, Data> cache = Caffeine.newBuilder()
    .maximumSize(10_000)
    .expireAfterWrite(Duration.ofMinutes(5))
    .recordStats()
    .build();

// 데이터 조회 (없으면 null)
Data data = cache.getIfPresent("key");

// 데이터 조회 (없으면 생성 로직 실행)
Data data = cache.get("key", k -> loadDataFromDB(k));
```

## Spring Boot와 함께 사용하기

`application.yml` 설정만으로도 간단하게 적용할 수 있다.

```yaml
spring:
  cache:
    type: caffeine
    caffeine:
      spec: maximumSize=500,expireAfterAccess=600s
```

## 비유: 도서관의 '반납 대기대'

- **일반 캐시**: 그냥 자주 찾는 책을 앞에 두는 수준.
- **Caffeine**: 어떤 책을 사람들이 많이 찾는지, 최근에는 어떤 트렌드인지 실시간으로 분석해서 가장 효율적인 위치에 책을 배치하는 베테랑 사서와 같다.

## 연관 기술

- **[[Redis]]**: Caffeine이 로컬(In-memory) 캐시라면, Redis는 분산(Global) 캐시다. 보통 둘을 조합하여 L1/L2 캐시 구조를 만든다.
- **Guava Cache**: Caffeine의 조상 격인 라이브러리.
- **[[Spring Boot]]**: Caffeine 서비스를 가장 많이 활용하는 환경.
