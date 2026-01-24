---
title: Kotlin
aliases: ["kotlin", "코틀린"]
---

# Kotlin

> 더 나은 [[Java]]로 개발하고 싶을 때

2011년 JetBrains가 만든 [[JVM]] 언어다. [[Java]]와 100% 호환되면서 더 간결하고 안전하다. 2017년 Google이 Android 공식 언어로 지정하면서 폭발적으로 성장했다.

"Java가 했어야 할 것들"을 다 구현했다. null 안전성, 데이터 클래스, 확장 함수, 코루틴 등. Java 개발자가 배우기 쉽고, 기존 Java 코드와 혼용 가능.

## 탄생 배경

JetBrains는 IntelliJ IDEA로 유명한 IDE 회사다. Java로 IDE를 개발하면서 Java의 한계를 느꼈다. Scala는 너무 복잡했다. "실용적인 더 나은 Java"가 필요했다.

2011년 공개, 2016년 1.0 출시. 이름은 러시아 상트페테르부르크 근처의 섬 이름. JetBrains 본사가 있는 곳과 가깝다.

## 특징

**Null 안전성**: 타입 시스템 레벨에서 null 처리. `String`은 null 불가, `String?`은 null 가능. NullPointerException 컴파일 타임에 방지.

**간결한 문법**: `data class`, `object`, `when`, `?.`, `?:`, `let` 등. 보일러플레이트 대폭 감소.

**Java 상호운용**: Java 코드를 Kotlin에서, Kotlin 코드를 Java에서 그대로 호출. 점진적 마이그레이션 가능.

**확장 함수**: 기존 클래스에 메서드 추가 (실제 수정 없이). `fun String.addExclamation() = this + "!"`.

**코루틴**: 비동기 프로그래밍을 동기 코드처럼. suspend 함수로 논블로킹 처리.

**스마트 캐스트**: 타입 체크하면 자동으로 캐스팅. `if (x is String) x.length` 가능.

## 성능

JVM에서 돌아가므로 [[Java]]와 성능 동일. 바이트코드로 컴파일되고 JIT 최적화 적용.

인라인 함수, 값 클래스(inline class)로 추가 최적화 가능.

Kotlin/Native로 네이티브 컴파일도 가능. iOS 앱, 임베디드에서 사용.

## 플랫폼

**Kotlin/JVM**: 서버, Android. 가장 많이 사용.

**Kotlin/Android**: Android 공식 언어. Jetpack Compose.

**Kotlin/JS**: JavaScript로 컴파일. 프론트엔드 개발.

**Kotlin/Native**: LLVM으로 네이티브 컴파일. iOS, 임베디드.

**Kotlin Multiplatform**: 여러 플랫폼에서 코드 공유.

## 생태계

**프레임워크**: [[Spring Boot]] (공식 지원), Ktor (Kotlin 네이티브 웹), Exposed (ORM)

**Android**: Jetpack Compose, Android KTX

**테스트**: JUnit, Kotest, MockK

**빌드**: Gradle (Kotlin DSL), Maven

**IDE**: IntelliJ IDEA (최고 지원), Android Studio

## 주의점

**빌드 시간**: Java보다 컴파일 느림. 대규모 프로젝트에서 체감. Gradle 캐싱으로 완화.

**Java와의 미묘한 차이**: 100% 호환이지만 특정 패턴에서 충돌. 애노테이션 처리, 리플렉션 등.

**학습 곡선**: Java 개발자는 쉽게 배우지만, 고급 기능(코루틴, 제네릭 변성 등)은 시간 필요.

**커뮤니티 크기**: [[Java]]보다 작다. 레퍼런스, 라이브러리가 Java 중심인 경우 많음.

**멀티플랫폼 성숙도**: Kotlin Multiplatform은 아직 발전 중. 특히 iOS 지원.

## 주요 기능

- Null 안전성 (?, ?., ?:, !!)
- Data class, Sealed class
- 확장 함수/프로퍼티
- 코루틴 (비동기)
- 위임 (by)
- DSL 빌더
- 스마트 캐스트
- when 표현식

## 기타

Google이 Android 공식 언어로 지정한 건 Java 저작권 분쟁 영향도 있다. Oracle과의 소송이 길어지면서 Java 대안이 필요했고, Kotlin이 딱 맞았다.

"Kotlin은 Java++다"라는 말이 있다. [[C++]]가 [[C]]의 확장이듯, Kotlin은 Java의 확장이라는 의미. 하지만 C++처럼 복잡해지지 않고 단순함을 유지한다.

JetBrains는 Kotlin을 자사 제품(IntelliJ, TeamCity 등) 개발에 적극 사용한다. "우리가 쓰려고 만든 언어"라서 실용성이 검증됐다.

서버 사이드에서도 Kotlin 채택이 늘고 있다. [[Spring Boot]]가 공식 지원하고, Netflix, Uber, Trello 등이 사용 중. 단순히 Android 언어가 아니라 범용 언어로 자리잡고 있다.

