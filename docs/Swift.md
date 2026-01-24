---
title: Swift
aliases: ["swift", "스위프트", "ios"]
---

# Swift

> Apple 플랫폼 앱을 만들 때

2014년 Apple이 만든 언어다. Objective-C를 대체하기 위해 개발됐다. iOS, macOS, watchOS, tvOS 앱 개발의 표준 언어. 현대적이고 안전한 문법으로 Apple 개발 경험을 크게 개선했다.

"Fast, Safe, Expressive"를 표방한다. [[C]]/[[C++]] 수준의 성능을 내면서도 [[Python]] 같은 간결함을 추구. Apple 생태계 밖에서도 서버 사이드로 확장 중.

## 탄생 배경

Objective-C는 1980년대 언어다. C에 Smalltalk의 객체 시스템을 붙인 거라 문법이 독특하고 어려웠다. Apple 개발자들도 불만이 많았다.

Chris Lattner(LLVM 창시자)가 2010년부터 비밀리에 개발. 2014년 WWDC에서 깜짝 공개됐다. 개발자들이 환호했을 정도로 반응이 뜨거웠다.

2015년 오픈소스화. Linux 지원 추가.

## 특징

**안전한 타입 시스템**: Optional로 null 처리 강제. 타입 추론으로 간결함 유지.

**Protocol-Oriented**: 클래스 상속보다 Protocol(인터페이스) 조합 권장. Apple의 새로운 패러다임 제안.

**값 타입 중심**: struct가 class보다 권장됨. 불변성과 예측 가능성.

**클로저**: 일급 시민. 간결한 문법. Swift UI에서 많이 사용.

**메모리 관리**: ARC (Automatic Reference Counting). GC가 아니라 컴파일 타임에 해제 시점 결정. 예측 가능한 성능.

**에러 처리**: try-catch와 Result 타입. 예외를 명시적으로 처리.

## 성능

[[C]]/[[C++]]에 근접하는 성능. LLVM 기반으로 최적화 우수.

ARC라서 GC 지연 없음. 실시간 앱(게임, 오디오)에 적합.

값 타입과 인라이닝으로 힙 할당 최소화 가능.

## 생태계

**UI 프레임워크**: SwiftUI (선언적), UIKit (명령적, 레거시), AppKit (macOS)

**서버**: Vapor, Kitura, Hummingbird

**패키지**: Swift Package Manager (SPM)

**테스트**: XCTest (기본), Quick/Nimble

**IDE**: Xcode (공식), VS Code (Linux)

**앱 배포**: App Store, TestFlight

## 주의점

**Apple 종속**: 사실상 Apple 생태계 전용. Linux 지원 있지만 생태계 작음.

**ABI 안정화 역사**: Swift 5 (2019)까지 ABI가 불안정했다. 버전 올릴 때마다 호환성 문제.

**Objective-C 레거시**: 기존 iOS 코드가 Obj-C라서 interop 필요. 특히 오래된 라이브러리.

**에러 처리 번거로움**: `do-try-catch`, `guard let`, `if let` 패턴이 많아서 코드가 길어질 수 있음.

**버전 변화**: 초기엔 매 버전마다 문법이 바뀌어서 혼란. 지금은 안정화됐지만 오래된 튜토리얼 주의.

## 주요 기능

- Optional (null 안전성)
- Protocol extensions
- Generics
- Closures
- Pattern matching
- Property wrappers
- Result builders (SwiftUI용)
- async/await (Swift 5.5+)
- Actor (동시성, Swift 5.5+)

## 기타

Swift는 "빠르다"는 의미의 영어 단어다. 새 종류 이름이기도 해서 로고가 칼새(swift bird) 모양이다. Apple답게 이름도 로고도 깔끔하다.

Chris Lattner는 Swift 발표 후 Tesla, Google을 거쳐 현재는 AI 스타트업 Modular에서 Mojo 언어를 만들고 있다. 프로그래밍 언어 설계 분야의 록스타.

SwiftUI는 2019년에 나왔는데, [[React]]의 선언적 UI 패러다임을 채택했다. Apple이 React/Flutter를 벤치마킹했다는 게 보인다. 기존 UIKit과 스타일이 완전히 다르다.

"Swift를 배우면 iOS 개발자가 된다"는 말이 있다. Swift 자체보다 Apple 프레임워크(UIKit, SwiftUI, Combine 등) 학습량이 더 많다. 언어는 도구고, 생태계가 진짜 공부 대상.

