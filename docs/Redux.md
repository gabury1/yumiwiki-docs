---
title: Redux
aliases: ["redux", "리덕스", "flux", "상태관리"]
---

# Redux

> 전역 상태 관리의 교과서

JavaScript 앱(주로 [[React]])을 위한 예측 가능한 상태 컨테이너. "모든 상태(State)는 하나의 저장소(Store)에 있다"는 원칙을 지킨다. Dan Abramov가 2015년에 마틀었다.

## 3가지 원칙

1. **Single Source of Truth**: 모든 상태는 하나의 Store 안에 있는 객체 트리 구조로 저장된다.
2. **State is Read-Only**: 상태를 바꾸는 유일한 방법은 Action(무슨 일이 일어났는지 설명하는 객체)을 보내는(dispatch) 것이다.
3. **Changes are made with Pure Functions**: Action을 받아서 상태를 어떻게 바꿀지는 순수 함수인 Reducer가 결정한다.

## 작동 흐름

1. UI에서 버튼 클릭 -> `dispatch(action)`
2. `Reducer`가 (기존 상태, 액션)을 받아서 -> (새로운 상태)를 리턴
3. Store가 업데이트됨 -> UI가 이를 감지(Subscribe)하고 다시 그려짐

## 장점 vs 단점

- **장점**: 흐름이 단방향(Flux 패턴)이라 예측 가능하고 디버깅(Redux DevTools)이 쉽다. 규모가 큰 프로젝트에서 질서가 잡힌다.
- **단점**: 보일러플레이트(상용구) 코드가 너무 많다. 간단한 기능 하나 넣으려는데 Action, Reducer, Type 정의까지 해야 해서 피곤하다.

## 생태계

너무 복잡해서 요즘은 [[Zustand]], [[Recoil]], [[Jotai]] 같은 가벼운 라이브러리로 많이 넘어가는 추세다. 하지만 Redux 팀도 이를 인지하고 **Redux Toolkit (RTK)**을 내놓아 코드를 획기적으로 줄였다. "RTK 쓰면 Redux도 할만하다"는 평.
