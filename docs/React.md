---
title: React
aliases: ["react", "reactjs", "리액트"]
---

# React

> 컴포넌트 기반으로 인터랙티브한 UI 만들고 싶을 때

[[JavaScript]] UI 라이브러리다. 2013년 Facebook(현 Meta)이 만들었다. 현재 프론트엔드 생태계에서 압도적 1위.

컴포넌트 기반이다. UI를 독립적인 조각으로 나누고 조합한다. 재사용성이 좋고 유지보수가 쉽다.

[[가상 DOM]]을 써서 효율적으로 렌더링한다. 상태 변경 시 전체가 아니라 바뀐 부분만 실제 DOM에 반영.

## 성능

[[가상 DOM]] 덕에 효율적. 하지만 잘못 쓰면 느려진다. 불필요한 리렌더링 방지가 핵심. `React.memo`, `useMemo`, `useCallback` 적절히 활용.

초기 번들 크기 주의. 라이브러리 많이 넣으면 커짐. [[Code Splitting]], [[Lazy Loading]]으로 분할.

## 생태계

상태 관리: [[Redux]], [[Zustand]], [[Recoil]], [[Jotai]]. 요즘은 가벼운 Zustand 인기.

라우팅: [[React Router]]가 표준.

폼: [[React Hook Form]], [[Formik]].

UI 라이브러리: [[MUI]], [[Ant Design]], [[Chakra UI]], [[shadcn/ui]].

메타 프레임워크: [[Next.js]], [[Remix]]. SSR, 라우팅 다 해결.

## 주의점

**useEffect 무한루프**: 의존성 배열 잘못 넣으면 무한 렌더링. 빈 배열 `[]`은 마운트 시 1회만.

**상태 끌어올리기 지옥**: 깊은 컴포넌트 트리에서 props drilling 발생. Context나 상태 관리 라이브러리 필요.

**클로저 문제**: 이벤트 핸들러에서 오래된 상태값 참조. useCallback 의존성이나 함수형 업데이트로 해결.

**SEO**: CSR은 SEO 불리. [[Next.js]]로 SSR/SSG 적용.

## 주요 기능

- JSX 문법
- 함수형 컴포넌트, Hooks
- [[가상 DOM]]
- 단방향 데이터 흐름
- Context API
- Suspense, Concurrent Mode

## 기타

Facebook(현 Meta)의 Jordan Walke가 만들었다. 2011년 Facebook 뉴스피드에 처음 사용됐고, 2012년 Instagram에도 도입됐다. 2013년 JSConf에서 오픈소스로 공개했는데, 초기 반응은 회의적이었다. "HTML을 JavaScript에 넣는다고?" JSX가 너무 이상하게 보였던 거다.

라이센스 논란이 있었다. 원래 BSD + Patents 라이센스였는데, 이게 특허 조항 때문에 문제가 됐다. 2017년 [[Apache]], [[WordPress]] 같은 프로젝트들이 React 사용 중단을 검토하자, Facebook이 MIT 라이센스로 변경했다. 이후 커뮤니티가 안정됐다.

"React는 라이브러리지 프레임워크가 아니다"라는 말을 공식적으로 한다. UI만 담당하고 나머지(라우팅, 상태관리 등)는 개발자 선택이라는 뜻. 하지만 생태계가 워낙 방대해서 사실상 프레임워크처럼 쓰인다. [[Next.js]] 나오면서 "메타 프레임워크" 시대가 열렸다.

Class 컴포넌트에서 Hooks로의 전환은 React 역사의 분기점이었다. 2019년 React 16.8에서 Hooks 도입 후, 커뮤니티가 완전히 함수형으로 넘어갔다. 요즘은 Class 컴포넌트 쓰는 코드 보면 "레거시"라고 느껴진다.
