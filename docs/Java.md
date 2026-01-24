---
title: Java
aliases: ["java", "자바", "jvm"]
---

# Java

> 엔터프라이즈급 대규모 시스템을 만들 때

1995년 Sun Microsystems(현 [[Oracle]])가 만든 [[객체지향]] 언어다. "Write Once, Run Anywhere"를 표방한다. [[JVM]] 위에서 돌아가서 OS 독립적이다. 전 세계에서 가장 많이 쓰이는 언어 중 하나.

금융권, 대기업, 정부 시스템에서 압도적이다. 국내 SI 업계의 표준 언어. [[Spring Boot]]와 함께 서버 사이드 개발의 대명사다. Android 앱 개발에도 공식 언어였다(현재는 [[Kotlin]] 선호).

## 탄생 배경

1990년대 초, Sun Microsystems의 James Gosling이 가전제품용 언어로 개발했다. 원래 이름은 Oak. 가전 시장이 안 됐는데, 웹이 뜨면서 애플릿으로 방향 전환. 1995년 Java로 이름 바꾸고 공개.

"한 번 작성하면 어디서든 실행"이 혁신이었다. C/C++는 OS마다 다시 컴파일해야 했는데, Java는 바이트코드로 컴파일하고 JVM이 실행한다. 이 철학이 서버 사이드에서 빛을 발했다.

## 특징

**강력한 타입 시스템**: 모든 변수에 타입 선언 필수. 컴파일 시점에 타입 에러 잡는다. `int x = 5;`.

**객체지향**: 거의 모든 것이 클래스. 캡슐화, 상속, 다형성 철저히 적용. 원시 타입(int, boolean 등)만 예외.

**가비지 컬렉션**: 메모리 관리 자동. C/C++의 메모리 릭 문제 해결. 하지만 GC 튜닝은 고급 주제.

**예외 처리**: Checked Exception으로 예외 처리 강제. 안정성 높이지만 보일러플레이트 많다.

**멀티스레딩**: 언어 레벨에서 스레드 지원. `synchronized`, `volatile`, `java.util.concurrent` 패키지.

**풍부한 표준 라이브러리**: Collections, I/O, 네트워킹, 날짜/시간 등 웬만한 건 다 있다.

## 성능

JIT 컴파일로 꽤 빠르다. 초기엔 "Java는 느리다"였는데, HotSpot JVM 이후 많이 개선됐다. 최신 JVM은 C++에 근접하는 성능을 낸다.

GC가 변수. Stop-the-World가 발생하면 응답 지연. G1GC, ZGC, Shenandoah 같은 저지연 GC가 나왔다. 대규모 힙에서 튜닝 필수.

콜드 스타트가 문제. JVM 워밍업에 시간 걸린다. 서버리스에서 불리. [[GraalVM]] Native Image로 네이티브 컴파일하면 해결되지만 호환성 문제.

## 버전

**Java 8 (2014)**: Lambda, Stream API, Optional 도입. LTS. 아직도 가장 많이 쓰인다.

**Java 11 (2018)**: 모듈 시스템, var 지원. LTS.

**Java 17 (2021)**: Sealed class, Pattern matching 프리뷰. LTS. 현재 권장.

**Java 21 (2023)**: Virtual Thread 정식, Record pattern. LTS.

매 6개월 새 버전 나온다. LTS(Long Term Support)는 3년마다. 기업에서는 보통 LTS만 쓴다.

## 생태계

**빌드 도구**: [[Maven]], [[Gradle]]

**프레임워크**: [[Spring Boot]] (웹), [[Spring]] Framework, [[Jakarta EE]], [[Quarkus]], [[Micronaut]]

**ORM**: [[JPA]]/Hibernate, [[MyBatis]], [[jOOQ]]

**테스트**: JUnit, Mockito, AssertJ

**IDE**: IntelliJ IDEA (업계 표준), Eclipse, VS Code

**유틸리티**: [[Lombok]], [[MapStruct]], Guava

## 주의점

**보일러플레이트**: getter, setter, constructor 등 반복 코드 많다. [[Lombok]]이나 Java 14+ Record로 완화.

**Null 처리**: NullPointerException 지옥. Optional 쓰거나 @Nullable/@NonNull 애노테이션으로 방어.

**버전 파편화**: Java 8에서 못 올라가는 프로젝트 많다. 의존성 호환성 문제.

**복잡한 설정**: [[Spring Boot]]가 많이 단순화했지만, 제대로 이해하려면 학습량 많다.

**Checked Exception**: 의도는 좋은데 실무에서 try-catch 남발하게 만든다. 논쟁 대상.

## 주요 기능

- [[JVM]] 위에서 동작 (OS 독립)
- 강력한 [[객체지향]]
- Lambda, Stream API (함수형 스타일)
- Generics
- Annotation
- Reflection
- Concurrency utilities

## 기타

"Java를 만든 사람이 커피를 좋아해서 Java다"라는 설이 있다. Java는 인도네시아 섬 이름이자 커피 종류 이름이다. 원래 Oak였는데 상표 문제로 바꿨다. 회의 중에 커피 마시다가 나온 이름이라고.

James Gosling은 "Java의 아버지"로 불린다. Sun이 Oracle에 인수된 후 퇴사했다. Java 커뮤니티에서 전설적인 인물.

"Enterprise Java"라는 말이 있다. 대기업, 금융권, 정부에서 Java를 표준으로 쓰면서 생긴 문화다. 안정성, 유지보수성, 확장성을 중시한다. 반면 스타트업에서는 "Java는 무겁다"며 [[Python]], [[Node.js]]를 선호하기도.

한국 SI 업계에서 Java는 절대적이다. "자바 몇 년 하셨어요?"가 면접 첫 질문. [[Spring]] 경험 필수. 최근엔 [[Kotlin]]이 부상 중이지만, 레거시 시스템은 여전히 Java다.

