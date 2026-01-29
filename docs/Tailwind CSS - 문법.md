---
title: Tailwind CSS - 문법
aliases: ["tailwind syntax", "테일윈드 문법", "tailwind cheat sheet", "테일윈드 유틸리티"]
---

# Tailwind CSS 문법

Tailwind CSS에서 가장 자주 사용되는 유틸리티 클래스와 핵심 설정 방식을 정리한 참고 문서입니다.

## 목차

- [레이아웃 (Layout)](#레이아웃-layout)
- [간격과 크기 (Spacing & Sizing)](#간격과-크기-spacing--sizing)
- [타이포그래피 (Typography)](#타이포그래피-typography)
- [배경과 테두리 (Backgrounds & Borders)](#배경과-테두리-backgrounds--borders)
- [유연한 박스 (Flexbox & Grid)](#유연한-박스-flexbox--grid)
- [응답형 디자인 (Responsive Design)](#응답형-디자인-responsive-design)
- [상태 선택자 (States)](#상태-선택자-states)
- [다크 모드 (Dark Mode)](#다크-모드-dark-mode)
- [사용자 정의 설정 (Customization)](#사용자-정의-설정-customization)
- [지시어 (Directives)](#지시어-directives)

---

## 레이아웃 (Layout)

박스의 배치와 가시성을 조절한다.

- `block`, `inline-block`, `inline`, `flex`, `grid`, `hidden`: 디스플레이 속성
- `relative`, `absolute`, `fixed`, `sticky`: 포지션 속성
- `top-0`, `right-4`, `bottom-auto`, `inset-0`: 좌표 조절
- `z-0` ~ `z-50`: Z-index
- `overflow-auto`, `overflow-hidden`, `overflow-scroll`: 오버플로우 처리
- `visible`, `invisible`: 가시성

---

## 간격과 크기 (Spacing & Sizing)

가장 많이 쓰는 유틸리티들이다. 기본적으로 `1` 단위는 `0.25rem` (4px)이다.

### Margin (바깥 여백)
- `m-{size}`: 전체 여백 (예: `m-4`)
- `mx-{size}`: 좌우 여백
- `my-{size}`: 상하 여백
- `mt-`, `mr-`, `mb-`, `ml-`: 특정 방향 여백
- `m-auto`: 중앙 정렬

### Padding (안쪽 여백)
- `p-{size}`, `px-`, `py-`, `pt-`, `pr-`, `pb-`, `pl-`: Margin과 동일한 규칙

### Width & Height (너비와 높이)
- `w-{size}`, `h-{size}`: 고정 크기 (예: `w-64`, `h-32`)
- `w-full`, `h-full`: 100%
- `w-screen`, `h-screen`: 100vw, 100vh
- `w-min`, `w-max`, `w-fit`: 내용물에 맞춘 크기
- `min-w-0`, `max-w-7xl`: 최소/최대 너비 제한

---

## 타이포그래피 (Typography)

텍스트 스타일링의 모든 것.

- **글자 크기**: `text-xs`, `text-sm`, `text-base` (기본), `text-lg`, `text-xl`, `text-2xl` ~ `text-9xl`
- **글자 두께**: `font-thin`, `font-normal`, `font-medium`, `font-bold`, `font-black`
- **정렬**: `text-left`, `text-center`, `text-right`, `text-justify`
- **색상**: `text-white`, `text-black`, `text-gray-500`, `text-blue-600` (50~950 단계)
- **장식**: `underline`, `line-through`, `no-underline`
- **줄 간격**: `leading-none`, `leading-tight`, `leading-normal`, `leading-loose`
- **자간**: `tracking-tighter`, `tracking-normal`, `tracking-widest`

---

## 배경과 테두리 (Backgrounds & Borders)

- **배경색**: `bg-red-500`, `bg-opacity-50`, `bg-transparent`
- **테두리 두께**: `border`, `border-0`, `border-2`, `border-4`, `border-8`
- **테두리 색상**: `border-gray-300`, `border-blue-500`
- **둥근 테두리**: `rounded-none`, `rounded-sm`, `rounded`, `rounded-md`, `rounded-lg`, `rounded-xl`, `rounded-full` (원형)
- **그림자**: `shadow-sm`, `shadow`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl`, `shadow-none`

---

## 유연한 박스 (Flexbox & Grid)

현대적인 웹 레이아웃의 핵심.

### Flexbox
- `flex`: 컨테이너를 flex로 설정
- `flex-row`, `flex-col`: 방향 설정
- `justify-start`, `justify-center`, `justify-between`: 메인축 정렬
- `items-start`, `items-center`, `items-end`: 교차축 정렬
- `flex-1`, `flex-none`: 성장 비율 조절
- `gap-4`: 아이템 사이 간격

### Grid
- `grid`: 컨테이너를 grid로 설정
- `grid-cols-3`: 3열 그리드
- `col-span-2`: 2칸 차지하기
- `gap-y-8`: 세로 간격

---

## 응답형 디자인 (Responsive Design)

모바일 퍼스트(Mobile First) 전략을 사용한다. 아무 접두사가 없으면 모바일(Small)이고, 그 이상은 접두사를 붙인다.

- `sm:` (640px 이상)
- `md:` (768px 이상)
- `lg:` (1024px 이상)
- `xl:` (1280px 이상)
- `2xl:` (1536px 이상)

**사용 예시:**
```html
<div class="w-full md:w-1/2 lg:w-1/3">
  <!-- 모바일은 100%, 태블릿은 50%, 데스크탑은 33% -->
</div>
```

---

## 상태 선택자 (States)

특정 상황에서만 스타일을 적용한다.

- `hover:`: 마우스 올렸을 때
- `focus:`: 포커스 되었을 때
- `active:`: 클릭하는 순간
- `disabled:`: 비활성화 상태
- `group-hover:`: 부모(`group`)에 호버했을 때 자식 스타일 변경

**사용 예시:**
```html
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  클릭하세요
</button>
```

---

## 다크 모드 (Dark Mode)

`dark:` 접두사를 사용하여 다크 모드 전용 스타일을 지정한다.

```html
<div class="bg-white dark:bg-gray-800 text-black dark:text-white">
  밤이 되면 색이 변합니다.
</div>
```

---

## 사용자 정의 설정 (Customization)

`tailwind.config.js` 파일을 통해 프로젝트만의 색상, 폰트, 간격 등을 추가하거나 변경할 수 있다.

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'brand-blue': '#1e40af',  // 커스텀 브랜드 색상 추가
      },
      spacing: {
        '128': '32rem',           // 512px 간격 추가
      }
    }
  }
}
```

---

## 지시어 (Directives)

CSS 파일 내부에서 사용하는 특수 명령이다.

### @tailwind
Tailwind의 기본 스타일, 컴포넌트, 유틸리티를 가져온다.
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### @apply
여러 클래스를 하나의 커스텀 클래스로 묶을 때 사용한다. (HTML이 너무 지저분해질 때 유용)
```css
.btn-primary {
  @apply bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700 transition;
}
```

### @layer
특정 레이어에 스타일을 추가하여 우선순위를 조절한다.
```css
@layer components {
  .card {
    @apply border p-4 rounded shadow;
  }
}
```

---

## 꿀팁

1. **JIT 모드**: 대괄호를 사용하여 임의의 값을 즉석에서 넣을 수 있다. (예: `top-[117px]`, `bg-[#1da1f2]`, `text-[1.5rem]`)
2. **Prettier 플러그인**: `prettier-plugin-tailwindcss`를 쓰면 클래스 순서를 자동으로 정렬해준다.
3. **공식 문서**: [tailwindcss.com](https://tailwindcss.com/docs)의 검색 기능(`Ctrl + K`)은 신계 수준으로 편하다.
