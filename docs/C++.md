---
title: C++
aliases: ["cpp", "cplusplus", "씨플플", "c++"]
---

# C++

> 성능이 중요한 대규모 시스템을 만들 때

1983년 Bjarne Stroustrup이 Bell Labs에서 만든 언어다. [[C]]에 [[객체지향]]을 추가한 "C with Classes"로 시작했다. C의 성능을 유지하면서 대규모 프로그램을 관리하기 쉽게 하려는 목적.

게임 엔진(Unreal, Unity), 데이터베이스([[MySQL]], [[PostgreSQL]]), 브라우저(Chrome), OS 핵심 부분에서 쓰인다. 성능 크리티컬한 곳에서 여전히 1순위 선택지.

## 탄생 배경

1979년 Bjarne Stroustrup은 박사 과정에서 Simula의 객체지향 개념에 감명받았다. 하지만 Simula는 느렸다. C의 성능에 Simula의 추상화를 결합하고 싶었다.

Bell Labs에서 "C with Classes" 개발 시작. 1983년 C++로 이름 변경. `++`는 C의 증가 연산자에서 따왔다. "C의 다음 단계"라는 의미.

## 특징

**멀티 패러다임**: [[객체지향]], 제네릭(템플릿), 절차적, 함수형 스타일 다 지원. 원하는 대로 섞어 쓸 수 있다.

**C 호환**: 대부분의 C 코드가 C++에서 돌아간다. C 라이브러리 그대로 사용 가능.

**Zero-overhead 원칙**: "쓰지 않는 기능에 비용을 지불하지 않는다". 추상화해도 성능 손해 없도록 설계.

**RAII**: Resource Acquisition Is Initialization. 생성자에서 리소스 획득, 소멸자에서 해제. 메모리 릭 방지 패턴.

**템플릿 메타프로그래밍**: 컴파일 타임에 코드 생성. 매우 강력하지만 복잡.

**수동 메모리 관리**: C처럼 직접 관리하거나, 스마트 포인터(`unique_ptr`, `shared_ptr`)로 반자동화.

## 성능

C와 거의 동일한 성능. 잘 쓰면 손으로 짠 어셈블리에 근접.

추상화 비용이 거의 없다. 가상 함수 호출은 vtable 조회 한 번. 인라인 함수, 템플릿은 오버헤드 제로.

하지만 제대로 쓰기 어렵다. 잘못 쓰면 C보다 느릴 수 있다. 복사 비용, 메모리 할당 패턴 등 신경 써야 한다.

## 버전

**C++98/03**: 첫 표준. STL(Standard Template Library) 포함.

**C++11**: 현대 C++의 시작. auto, lambda, move semantics, smart pointer, range-for.

**C++14**: 작은 개선. 제네릭 람다, `make_unique`.

**C++17**: `optional`, `variant`, `filesystem`, structured bindings.

**C++20**: Concepts, Ranges, Coroutines, Modules. 대규모 업데이트.

**C++23**: 최신. `std::expected`, `std::print` 등.

C++11 이후를 "Modern C++"라고 부른다. 이전과 코딩 스타일이 많이 다르다.

## 생태계

**컴파일러**: GCC, Clang, MSVC

**빌드 도구**: CMake (사실상 표준), Meson, Bazel

**패키지 관리**: vcpkg, Conan

**테스트**: Google Test, Catch2

**주요 사용처**: Unreal Engine, Chrome, LLVM, TensorFlow(C++ 코어), Bloomberg Terminal

## 주의점

**복잡성**: 언어가 거대하다. 템플릿, 메타프로그래밍, move semantics 등 학습량 많다.

**컴파일 시간**: 템플릿 많이 쓰면 컴파일 느려진다. 헤더 인클루드 늘어나면 더 느림. 프리컴파일드 헤더, 모듈(C++20)로 완화.

**메모리 안전성**: C보다 나아졌지만 여전히 문제. use-after-free, 댕글링 포인터. 스마트 포인터 쓰더라도 raw pointer 필요한 곳 있다.

**ABI 호환성**: 컴파일러 버전, 빌드 설정 다르면 링크 안 될 수 있다.

**에러 메시지**: 템플릿 에러 메시지가 악명 높다. 수백 줄 에러에 실제 원인은 한 줄. Concepts(C++20)로 개선 중.

## 주요 기능

- 클래스, 상속, 다형성 (OOP)
- 템플릿 (제네릭)
- 스마트 포인터 (unique_ptr, shared_ptr)
- STL (vector, map, algorithm 등)
- 람다 표현식
- Move semantics, RAII
- Concepts, Ranges (C++20)

## 기타

Bjarne Stroustrup은 아직도 현역이다. 표준 위원회에서 활동하고, C++ 발전 방향을 제시한다. "C++의 아버지"로 불린다.

"C++을 완전히 아는 사람은 없다"는 농담이 있다. 언어가 워낙 크고 복잡해서 모든 기능을 다 아는 사람이 드물다는 뜻. 팀마다 쓰는 서브셋이 다르다.

게임 업계에서 C++는 절대적이다. Unreal Engine이 C++ 기반이고, 대부분의 AAA 게임이 C++로 만들어진다. 성능이 곧 경쟁력인 분야라서.

"Modern C++는 다른 언어다"라는 말이 있다. C++11 이전과 이후가 코딩 스타일이 완전히 다르다. 포인터 대신 스마트 포인터, new/delete 대신 RAII, for 대신 range-for. 레거시 코드 읽기 어려운 이유다.

