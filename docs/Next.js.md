---
aliases: [넥스트, NextJS, next.js]
---

# Next.js

> [[React]]로 풀스택 웹 애플리케이션 만들고 싶을 때

[[React]] 기반 풀스택 프레임워크다. Vercel이 만들었다. [[SSR]], [[SSG]], API 라우트까지 지원. [[React]]만으로는 어려운 것들을 해결해준다.

파일 기반 라우팅이 편하다. `pages/` 또는 `app/` 폴더 구조가 곧 URL 구조. 설정 없이 라우팅 완성.

## 성능

[[SSR]], [[SSG]]로 초기 로딩 빠르고 SEO 좋음. ISR(Incremental Static Regeneration)로 정적 + 동적 장점 결합.

Image, Font 최적화 내장. 자동 코드 스플리팅.

## 생태계

[[Vercel]]에 배포하면 최적화 자동 적용. 다른 플랫폼도 가능.

App Router(13+)가 새 패러다임. Server Components, Streaming 지원. Pages Router도 여전히 지원.

## 주의점

**App Router 러닝커브**: Server Components, 캐싱 전략 이해 필요. 기존 React 방식과 다름.

**Vercel 종속 우려**: 일부 기능은 Vercel에서 최적화. 셀프호스팅 시 제약 있을 수 있음.

**번들 크기**: 기능 많이 쓰면 커짐. 분석하고 최적화 필요.

## 주요 기능

- 파일 기반 라우팅
- SSR, SSG, ISR
- API Routes
- Server Components (App Router)
- Image, Font 최적화
- Middleware

## 기타

Vercel(원래 이름은 Zeit)의 CEO Guillermo Rauch가 만들었다. 2016년 처음 공개됐는데, [[React]]의 서버 사이드 렌더링을 쉽게 만들자는 게 목표였다. 지금은 풀스택 프레임워크로 진화했다.

"Zero Config"를 표방했다. [[Webpack]] 설정 없이 바로 쓸 수 있다는 게 큰 장점이었다. [[Create React App]]보다 기능이 많으면서 설정은 더 간단했다. 이게 대중화에 크게 기여했다.

App Router(13+)는 논란이 많았다. Server Components라는 새 패러다임을 도입했는데, 기존 [[React]] 개발자들도 헷갈려했다. "클라이언트에서 돌아가는지 서버에서 돌아가는지 헷갈린다"는 불만이 많았다. 하지만 적응하면 성능 이점이 크다.

Vercel 플랫폼과의 통합이 강하다. Next.js 자체는 오픈소스지만, Vercel에 배포하면 추가 최적화가 적용된다. 이게 "Vendor Lock-in 아니냐"는 우려도 있다. 하지만 AWS, GCP 같은 곳에도 배포할 수 있으니 큰 문제는 아니라는 반론도.
