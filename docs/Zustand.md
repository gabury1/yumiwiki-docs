---
title: Zustand
aliases: ["zustand", "쥬스탄드", "주스탄드", "상태관리"]
---

# Zustand (주스탄드)

> "독일어로 '상태'... 리덕스의 복잡함을 한 방에 날려준 구세주"

[[JavaScript]]와 [[React]]를 위한 가볍고 빠르며 확장 가능한 상태 관리 라이브러리다. [[Redux]]의 복잡한 보일러플레이트에 지친 개발자들이 대거 이주하고 있는 요즘 대세다.

## 왜 쓰는가? (초간단 비교)

- **Redux (공장)**: 버튼 하나 누르는데 팀장 승인(Action), 결재 문서(Reducer), 공장 가동(Store)이 다 필요하다.
- **Zustand (개인 장부)**: 그냥 장부 하나 꺼내서 바로 쓰고 덮으면 된다.

## 특징

**보일러플레이트 없음**: `dispatch`, `action`, `reducer` 같은 개념을 몰라도 된다. 그냥 훅(Hook) 하나로 끝난다.

**Context API의 해결사**: React 내장 Context API는 값이 조금만 바뀌어도 모든 하위 컴포넌트가 다시 그려지는(Re-rendering) 문제가 있지만, Zustand는 필요한 부분만 똑똑하게 다시 그린다.

**러닝 커브 0에 수렴**: React 훅을 쓸 줄 안다면 5분 만에 배울 수 있다.

## 사용 예시

```javascript
import { create } from 'zustand'

// 1. 저장소(Store) 만들기
const useStore = create((set) => ({
  bears: 0,
  increase: () => set((state) => ({ bears: state.bears + 1 })),
}))

// 2. 컴포넌트에서 쓰기
function BearCounter() {
  const bears = useStore((state) => state.bears)
  return <h1>{bears} around here ...</h1>
}
```

## 장점 vs 단점

### 장점
- **가볍다**: 용량이 엄청나게 작다.
- **선택적 구독**: 내가 필요한 상태만 골라서 감시할 수 있어 성능이 좋다.
- **리덕스 개발자 도구**: [[Redux]]와 같은 개발자 도구(Redux DevTools)를 그대로 쓸 수 있다.

### 단점
- **구조 강제 없음**: 개발자마다 짜는 방식이 달라서, 대규모 팀에서는 오히려 난맥상이 생길 수 있다. (질서가 필요함)

## 기타

1. **독일어**: Zustand는 독일어로 **'상태'**라는 뜻이다. (발음은 '주스탄드'에 가깝다)
2. **곰돌이 마스코트**: 공식 문서나 예제에 곰돌이(Bear)가 자주 등장한다. 마스코트가 귀여워서 쓰는 사람도 있다.
3. **PMNDRS 팀**: Three.js용 리액트 라이브러리를 만드는 팀에서 만들었다. 그래서 성능과 디자인 감각이 남다르다.
