---
title: C Sharp
aliases: ["c#", "csharp", "씨샵", "c sharp", "net", "dotnet"]
---

# C#

> Microsoft 생태계에서 개발할 때

2000년 [[Microsoft]]가 만든 [[객체지향]] 언어다. [[Java]]에 대응하기 위해 만들어졌다. .NET 플랫폼의 핵심 언어. Windows 애플리케이션, 게임(Unity), 웹([[ASP.NET]]) 개발에 쓰인다.

문법이 [[Java]]와 비슷하지만 더 현대적인 기능이 많다. 람다, LINQ, async/await, 패턴 매칭 등을 Java보다 먼저 도입했다. Microsoft가 적극적으로 발전시켜서 기능 업데이트가 빠르다.

## 탄생 배경

1990년대 후반, [[Java]]가 인기를 끌었다. Microsoft는 J++라는 Java 확장을 만들었는데 Sun과 법적 분쟁이 생겼다. 결국 자체 언어를 만들기로 했다.

Anders Hejlsberg([[TypeScript]], Delphi 창시자)가 이끌었다. 2000년 .NET과 함께 발표. "C-like Object Oriented Language"에서 C#이 됐다. #은 음악의 샵 기호로, "C를 반음 올린 것"이라는 의미.

## 특징

**강력한 타입 시스템**: 정적 타입. `var`로 타입 추론도 가능. nullable reference types로 null 안전성 강화.

**객체지향 + 함수형**: 클래스, 인터페이스, 상속 지원. 람다, LINQ로 함수형 스타일도 가능.

**가비지 컬렉션**: .NET CLR이 메모리 관리. C/C++ 같은 수동 관리 불필요.

**async/await**: 비동기 프로그래밍 문법적으로 지원. JavaScript보다 먼저 도입.

**LINQ**: Language Integrated Query. 컬렉션, DB, XML 등에 SQL 같은 쿼리를 코드로.

**Properties**: getter/setter를 간결하게. `public string Name { get; set; }`.

## 성능

JIT 컴파일로 네이티브에 근접하는 성능. .NET Core 이후 크게 개선됐다.

AOT(Ahead-of-Time) 컴파일도 지원. Native AOT로 네이티브 바이너리 생성 가능. 서버리스에 유리.

Span<T>, Memory<T>로 저수준 메모리 최적화 가능. 게임 엔진(Unity)에서 쓸 만큼 성능 확보.

## 버전

**.NET Framework**: 원래 Windows 전용.

**.NET Core**: 2016년 크로스 플랫폼 오픈소스로 재탄생.

**.NET 5+**: Core와 Framework 통합. 현재 .NET 8 (2023).

**C# 버전**: C# 12 (2023). 매년 새 버전. primary constructors, collection expressions 등.

## 생태계

**프레임워크**: ASP.NET Core (웹), Entity Framework (ORM), WPF/WinForms (데스크톱), MAUI (모바일)

**게임**: Unity (C#이 스크립팅 언어)

**IDE**: Visual Studio (최고 지원), VS Code, Rider

**패키지**: NuGet

**클라우드**: Azure와 긴밀한 연동

## 주의점

**Windows 의존성**: 예전엔 Windows 전용이었다. .NET Core 이후 크로스 플랫폼 됐지만, 여전히 Windows에서 가장 잘 돌아간다.

**에코시스템**: Microsoft 생태계 밖에서는 인기 떨어진다. 스타트업에서는 [[Python]], [[Node.js]] 선호.

**학습 곡선**: 언어 자체는 배우기 쉬운데, .NET 생태계가 방대해서 전체 파악이 어렵다.

**Unity 특수성**: Unity에서 쓰는 C#은 .NET 본가와 버전이 다를 수 있다. Unity 전용 패턴(MonoBehaviour 등)도 있다.

## 주요 기능

- LINQ (Language Integrated Query)
- async/await 비동기
- Properties, Indexers
- Nullable reference types
- Pattern matching
- Record types (불변 데이터)
- Generics
- Extension methods

## 기타

C#의 #은 네 개의 + 기호가 합쳐진 것으로도 해석된다 (++++ 배열). 실제로는 음악의 샵 기호에서 따왔다. "C보다 반음 높다"는 의미인데, C++보다 한 단계 더 발전했다는 뉘앙스.

게임 개발에서 C#은 Unity 덕분에 엄청난 점유율을 가진다. 인디 게임의 상당수가 Unity + C# 조합. 프로그래밍 입문자가 게임 만들고 싶어서 C# 배우는 경우가 많다.

Microsoft가 오픈소스로 전환하면서 C#도 GitHub에서 개발된다. 커뮤니티 제안이 반영되고, 투명하게 진행된다. Satya Nadella 시대의 Microsoft 변화가 C#에도 영향을 줬다.

"Java vs C#" 논쟁은 오래됐다. 문법은 비슷하지만, C#이 새 기능 도입이 빠르다. Java 개발자가 C#으로 넘어오면 "왜 Java에는 이게 없어?"라고 한다는 말이 있다.

