---
aliases: [뷰, Vue.js, vue]
---

# Vue

> 점진적으로 도입 가능한 프론트엔드 프레임워크가 필요할 때

[[JavaScript]] [[프론트엔드 프레임워크]]다. 2014년 전 구글 개발자 Evan You가 만들었다. [[React]]보다 배우기 쉽고 [[Angular]]보다 가볍다.

"점진적 프레임워크"를 표방한다. 기존 프로젝트에 부분적으로 도입할 수 있다. 단순한 페이지에 CDN으로 추가하는 것부터 복잡한 SPA까지.

Options API와 Composition API 두 가지 스타일 지원. Vue 3부터 Composition API가 권장. [[React]] Hooks와 비슷한 느낌.

## 성능

[[React]]와 비슷하거나 약간 빠르다. 반응형 시스템이 변경 감지를 자동으로 해줘서 최적화 코드 덜 써도 됨.

Vue 3에서 크게 개선됐다. 번들 크기 줄고, 트리쉐이킹 지원.

## 생태계

[[Vue Router]], [[Pinia]](상태관리)가 공식. 생태계가 [[React]]보다는 작지만 핵심은 다 있음.

UI: [[Vuetify]], [[Element Plus]], [[PrimeVue]].

메타 프레임워크: [[Nuxt]]가 [[Next.js]] 역할.

## 주의점

**Vue 2 vs Vue 3**: Vue 2는 2023년 지원 종료. 새 프로젝트는 Vue 3로. 마이그레이션은 조금 번거로움.

**반응형 함정**: `ref`는 `.value`로 접근. 템플릿에서는 자동 언래핑. 객체는 `reactive` 쓰면 됨.

**Vuex → Pinia**: Vue 3에서는 Pinia가 공식 상태관리. Vuex보다 타입스크립트 지원 좋음.

## 주요 기능

- 반응형 데이터 바인딩
- 컴포넌트 시스템
- 디렉티브 (v-if, v-for, v-model)
- Composition API
- SFC (Single File Component)
- Teleport, Suspense

## 기타

Evan You는 전 구글 개발자다. [[Angular]]를 쓰다가 "필요한 부분만 가져온 가벼운 버전을 만들면 어떨까" 생각해서 Vue를 만들었다. 2014년 처음 공개했는데, 당시엔 개인 프로젝트였다. 지금은 풀타임으로 Vue 개발하고, 후원으로 먹고산다.

중국에서 엄청난 인기다. Alibaba, Tencent, Baidu 같은 중국 빅테크들이 Vue를 쓴다. 중국어 문서와 커뮤니티가 잘 되어 있다. 글로벌 점유율은 [[React]]에 밀리지만, 중국 시장에서는 압도적이다.

"Vue는 [[React]]와 [[Angular]]의 좋은 점을 합쳤다"는 평가가 있다. 템플릿 문법은 Angular에서, 컴포넌트 방식은 React에서 영감을 받았다. 그러면서도 더 배우기 쉽게 만들었다. "The Progressive Framework"라는 슬로건이 이걸 잘 표현한다.

Vue 3 출시(2020년)가 좀 논란이었다. Breaking Change가 많아서 마이그레이션이 쉽지 않았다. Vue 2 지원 종료가 2023년 말이어서, 많은 프로젝트가 급하게 업그레이드했다. 하지만 Vue 3의 성능 개선과 Composition API는 업그레이드할 가치가 있다는 평가.
