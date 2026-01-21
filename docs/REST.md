---
aliases: [RESTful, REST API, Representational State Transfer]
---

# REST

> 웹 API를 설계하는 아키텍처 스타일

자원(Resource)을 URL로 표현하고, [[HTTP]] 메서드로 조작하는 방식을 정의한다. 2000년 로이 필딩이 박사 논문에서 제안했다.

## 탄생 배경

웹 서비스 간 통신 방식이 제각각이었다. SOAP 같은 복잡한 프로토콜 대신, [[HTTP]]의 특성을 그대로 활용하는 단순한 방식이 필요했다.

## 규정 내용

**자원(Resource)**: URL로 표현. `/users/123`은 123번 사용자.

**HTTP 메서드로 행위 표현**:
- GET /users - 목록 조회
- GET /users/123 - 상세 조회
- POST /users - 생성
- PUT /users/123 - 수정
- DELETE /users/123 - 삭제

**원칙**:
- 무상태(Stateless)
- 균일한 인터페이스
- 계층화 시스템

## 용도

웹/모바일 API의 사실상 표준. 프론트엔드와 백엔드 통신, 서비스 간 통신에 광범위하게 사용.

## 주의점

REST는 엄격한 규격이 아니라 스타일이다. "RESTful"의 정도는 다양함. 모든 원칙을 지키기 어려우면 실용적으로 타협.

## 생태계

- [[JSON]] - 데이터 포맷
- [[OpenAPI]](Swagger) - API 문서화
- [[GraphQL]] - REST 대안
- [[Django REST Framework]], [[Express]] 등 구현 프레임워크

## 기타

로이 필딩의 2000년 박사 논문에서 제안됐다. 논문 제목은 "Architectural Styles and the Design of Network-based Software Architectures". 웹의 성공 요인을 분석하고 일반화한 결과가 REST다. 필딩은 HTTP 1.0, 1.1 명세 작성에도 참여했다.

"RESTful하다"는 말의 기준이 모호하다. 필딩의 원래 정의는 매우 엄격한데, 실제로는 느슨하게 해석해서 쓴다. URL에 동사 넣으면 안 된다는 원칙도 있지만(`/getUser` 대신 `GET /users`), 실무에서는 타협하는 경우가 많다. "실용적 REST"가 주류다.

REST vs [[GraphQL]] 논쟁이 있다. REST는 여러 엔드포인트, GraphQL은 하나의 엔드포인트. REST는 Over-fetching/Under-fetching 문제가 있고, GraphQL은 캐싱이 복잡하다. 정답은 없고 상황에 맞게 선택. 요즘은 둘 다 제공하는 API도 있다.

"HATEOAS"는 REST의 마지막 제약인데, 대부분의 API가 안 지킨다. "응답에 다음 가능한 액션의 링크를 포함해야 한다"는 원칙. 구현하기 복잡하고 실익이 적다고 느껴서 무시되는 경우가 많다. 로이 필딩은 이걸 안 지키면 "진짜 REST가 아니다"라고 했지만.
