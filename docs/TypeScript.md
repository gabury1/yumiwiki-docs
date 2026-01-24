---
title: TypeScript
aliases: ["ts", "typescript", "타입스크립트", "타스"]
---

# TypeScript

> [[JavaScript]]에 타입 시스템을 얹고 싶을 때

2012년 Microsoft가 만든 [[JavaScript]]의 상위 집합(superset)이다. JavaScript에 정적 타입 시스템을 추가했다. 모든 JavaScript 코드는 유효한 TypeScript 코드다. 컴파일하면 순수 JavaScript가 나온다.

대규모 프로젝트에서 JavaScript의 타입 없음이 문제가 됐다. IDE 자동완성 안 되고, 리팩토링 무섭고, 런타임 에러 많았다. TypeScript는 이 문제를 해결한다. [[Angular]]가 공식 채택하면서 급성장했고, 현재는 [[React]], [[Vue]], [[Node.js]] 생태계 전반에서 쓰인다.

## 탄생 배경

2010년대 초, JavaScript 프로젝트 규모가 커지면서 유지보수가 힘들어졌다. Google은 Dart를 만들었고, Microsoft는 다른 접근을 택했다. JavaScript를 대체하는 게 아니라 확장하자는 거다.

Anders Hejlsberg(C#, Delphi 설계자)가 TypeScript를 이끌었다. 2012년 공개, 2014년 1.0 출시. 처음엔 "왜 굳이?"라는 반응이었는데, Angular 2가 TypeScript 기반으로 나오면서 분위기가 바뀌었다.

## 특징

**정적 타입**: 변수, 함수 인자, 반환값에 타입 지정. `let x: number = 5;`. 컴파일 시점에 타입 에러 잡는다.

**타입 추론**: 타입 명시 안 해도 대부분 추론한다. `let x = 5;`면 자동으로 `number`. 일일이 안 써도 됨.

**인터페이스/타입 별칭**: 객체 형태 정의. `interface User { name: string; age: number; }`. 코드 문서화 역할도 한다.

**제네릭**: `Array<T>`, `Promise<T>` 같은 타입 매개변수. 재사용 가능한 타입 안전 코드 작성.

**유니온/인터섹션**: `string | number` (둘 중 하나), `A & B` (둘 다 합친 것). 유연한 타입 표현.

**enum**: 열거형 지원. JavaScript에는 없는 기능.

## 성능

TypeScript는 런타임에 존재하지 않는다. 컴파일하면 타입 정보가 다 사라지고 순수 JavaScript가 된다. 런타임 성능은 JavaScript와 동일. 빌드 시간은 추가된다.

컴파일 속도가 중요해진다. 대규모 프로젝트에서 `tsc` 느리면 개발 경험 나빠진다. [[esbuild]], [[SWC]] 같은 빠른 트랜스파일러 쓰거나, 증분 컴파일 활용.

## 생태계

**컴파일러**: `tsc` (공식), [[Babel]] (타입 체크 없이 변환만), [[esbuild]], [[SWC]] (빠른 대안)

**타입 정의**: DefinitelyTyped (@types/xxx 패키지). 수천 개 라이브러리 타입 제공.

**린터/포매터**: ESLint + @typescript-eslint, Prettier

**프레임워크 지원**: [[Angular]] (기본), [[React]] (JSX + 타입), [[Vue]] 3 (완전 지원), [[NestJS]] (TypeScript 기본)

**빌드 도구**: [[Vite]], [[Webpack]], [[Rollup]] 모두 지원

## 주의점

**학습 곡선**: 타입 시스템 자체가 복잡하다. 제네릭, 조건부 타입, infer 같은 고급 기능 익히려면 시간 필요.

**`any` 남용**: 타입 정하기 귀찮으면 `any` 쓰게 되는데, 그러면 TypeScript 쓰는 의미가 없다. `strict` 모드 켜고 `any` 최소화.

**설정 복잡**: `tsconfig.json` 옵션이 많다. `strict`, `target`, `module`, `esModuleInterop` 등 이해해야 한다.

**타입 정의 누락**: 인기 없는 라이브러리는 @types가 없을 수 있다. 직접 선언해야 한다.

**빌드 시간**: 큰 프로젝트에서 `tsc` 느리다. 증분 빌드나 프로젝트 참조 활용.

**런타임 타입 검사 없음**: 컴파일 타임 검사만. API 응답 같은 외부 데이터는 [[Zod]], [[Pydantic]] 같은 런타임 검증 필요.

## 주요 기능

- 정적 타입 시스템
- 인터페이스, 타입 별칭
- 제네릭, 유니온/인터섹션 타입
- 조건부 타입, 매핑 타입
- 데코레이터 (experimental)
- JSX/TSX 지원
- JavaScript와 100% 호환

## 기타

TypeScript 창시자 Anders Hejlsberg는 프로그래밍 언어 역사에서 전설적인 인물이다. Turbo Pascal, Delphi, C# 다 이 사람 작품. TypeScript도 그의 언어 설계 철학이 담겨 있다.

"점진적 타이핑"이 TypeScript의 핵심 전략이다. JavaScript 프로젝트에 조금씩 타입을 추가할 수 있다. 한 번에 다 바꿀 필요 없이, `.js`를 `.ts`로 바꾸고 `any`로 시작해서 점진적으로 타입을 강화하면 된다.

2020년대 들어서 TypeScript가 사실상 표준이 됐다. 새 프로젝트에서 순수 JavaScript 쓰면 "왜요?"라는 질문을 받는다. npm 다운로드 순위에서도 상위권이고, 대기업 프로젝트는 거의 다 TypeScript다.

"TypeScript는 JavaScript의 미래"라는 말이 있다. TC39(JavaScript 표준화 위원회)에 TypeScript 영향을 받은 제안이 많이 올라온다. 언젠가 JavaScript 자체에 타입이 추가될 수도 있다.

