---
title: Django
aliases: ["django", "장고", "python django", "dj"]
---

# Django

> [[Python]]으로 빠르게 웹 서비스 만들고 싶을 때

[[Python]] 기반 [[웹 프레임워크]]다. "배터리 포함(batteries included)" 철학으로 [[ORM]], 인증, 관리자 페이지, 폼 처리, 보안 등 웹 개발에 필요한 거의 모든 게 내장되어 있다. 2005년에 나왔고, [[Python]] 웹 프레임워크 중 가장 성숙하고 안정적이다.

쇼핑몰, CMS, 관리자 페이지가 필요한 서비스라면 Django가 편하다. 모델만 정의하면 관리자 페이지가 자동으로 생성되는 게 큰 장점. Instagram, Pinterest, Disqus, Mozilla, The Washington Post 같은 서비스도 Django로 시작했다. 국내에서는 스타트업 MVP 만들 때 많이 쓴다.

[[Python]]을 이미 알고 있다면 러닝커브가 낮은 편이다. 프레임워크가 정해준 구조대로 따라가면 되니까 초보자도 접근하기 쉽다. "한 가지 방법"을 권장하는 철학이라 팀 협업 시 코드 일관성 유지하기 좋다. 반면 자유도가 낮다고 느낄 수 있다. 내 맘대로 구조 짜고 싶으면 [[Flask]]가 나을 수도 있다.

빠르게 MVP 만들어야 할 때 생산성이 좋다. 하지만 비동기 처리가 약해서 실시간 기능이 많은 서비스에는 [[FastAPI]]나 [[Node.js]]가 더 적합할 수 있다. [[마이크로서비스]] 아키텍처보다는 모놀리식에 어울린다.

## 성능

솔직히 빠른 편은 아니다. [[Python]] 자체가 인터프리터 언어라 [[Go]]나 [[Java]]보다 느리다. 초당 수천 요청 이상 처리해야 하는 서비스라면 한계가 있다. 근데 실제로 프레임워크가 병목이 되는 경우는 많지 않다. 대부분의 웹 서비스에서 병목은 DB 쿼리나 외부 API 호출이다.

동시 접속 처리는 [[Gunicorn]]이나 [[uWSGI]] 같은 WSGI 서버에 워커 여러 개 띄워서 해결한다. 보통 CPU 코어당 2~4개 워커가 적정선. 메모리는 워커당 100~300MB 정도 잡아먹는다.

Django 3.0부터 [[ASGI]] 지원해서 비동기 뷰도 쓸 수 있다. [[Uvicorn]]이나 [[Daphne]]으로 띄우면 된다. 하지만 ORM이 아직 완전한 비동기가 아니라서 `sync_to_async`로 감싸야 하고, 이러면 성능 이점이 상쇄된다. Django 5.0부터 비동기 ORM이 조금씩 추가되고 있다.

[[캐싱]]을 잘 쓰면 성능 문제 대부분 해결된다. [[Redis]]나 [[Memcached]]로 쿼리 결과 캐싱하고, 템플릿 프래그먼트 캐싱 걸면 체감 성능이 크게 좋아진다.

## 생태계

[[Django REST Framework]]로 [[REST]] API 만들기 편하다. 시리얼라이저, 뷰셋, 라우터가 잘 갖춰져 있어서 CRUD API는 거의 자동화된다. [[drf-spectacular]]로 OpenAPI 문서 자동 생성도 가능.

[[Celery]]로 백그라운드 작업 처리하고, [[Django Channels]]로 [[WebSocket]] 구현할 수 있다. [[django-allauth]]로 소셜 로그인, [[django-debug-toolbar]]로 쿼리 디버깅, [[django-extensions]]로 유틸리티 커맨드 추가하는 게 일반적이다.

PyPI에 Django 관련 패키지가 수천 개다. 인증, 결제, 이메일, 검색 같은 기능은 패키지 설치만으로 해결되는 경우가 많다. [[Wagtail]], [[django CMS]] 같은 CMS 솔루션도 있다.

한국어 자료도 많고, 입문자용 튜토리얼도 잘 되어 있다. 공식 문서가 특히 잘 작성되어 있다. 취업 시장에서 [[Spring Boot]]보다는 수요가 적지만, 스타트업이나 데이터/AI 팀에서는 여전히 인기 있다.

## 주의점

**N+1 쿼리 문제**: ORM 쓸 때 가장 흔한 실수. `for post in posts: print(post.author.name)` 이렇게 하면 post마다 author 쿼리가 나간다. `select_related`(FK, OneToOne)나 `prefetch_related`(M2M, 역참조)로 미리 가져와야 한다. [[django-debug-toolbar]]로 쿼리 수 꼭 확인하자.

**마이그레이션 충돌**: 여러 브랜치에서 동시에 마이그레이션 만들면 충돌난다. `makemigrations --merge`로 해결할 수 있지만, 복잡한 스키마 변경은 수동으로 마이그레이션 파일 수정해야 할 수 있다. 배포 전에 마이그레이션 squash 하는 것도 방법.

**시그널 남용**: `post_save`, `pre_delete` 같은 시그널은 편하지만 남용하면 코드 흐름 파악이 어려워진다. 어디서 뭐가 실행되는지 추적하기 힘듦. 비즈니스 로직은 가능하면 명시적으로 호출하는 게 좋다.

**settings 분리**: 로컬, 개발, 운영 환경별로 settings를 분리해야 한다. `settings/base.py`, `settings/local.py`, `settings/production.py`로 나누고 환경변수로 선택하는 게 일반적. `DEBUG=True`로 운영에 배포하면 보안 사고 난다.

**Static/Media 파일 서빙**: Django 개발 서버는 static 파일 서빙해주지만, 운영에서는 [[Nginx]]나 [[S3]]로 서빙해야 한다. `collectstatic` 돌리고 [[WhiteNoise]] 쓰거나 CDN 연결해야 한다. 이거 모르면 운영 배포에서 CSS 안 먹는다.

**테스트 DB 초기화**: 테스트마다 DB 마이그레이션 돌리면 느리다. `--keepdb` 옵션으로 테스트 DB 유지하거나, `TransactionTestCase` 대신 `TestCase` 쓰면 빠르다. pytest-django 쓰면 더 편하다.

**메모리 누수**: 대용량 QuerySet을 한 번에 메모리에 올리면 터진다. `iterator()`로 청크 단위로 가져오거나, `values()`, `values_list()`로 필요한 필드만 가져와야 한다.

## 주요 기능

- [[ORM|객체-관계 매핑]] 내장 (QuerySet API가 강력함)
- 관리자 페이지 자동 생성 (커스터마이징도 쉬움)
- [[MTV|모델-템플릿-뷰]] 패턴
- [[Migration|마이그레이션]] 자동화 (스키마 버전 관리)
- [[CSRF]] 보호, [[XSS]] 방어, SQL 인젝션 방지 등 [[보안]] 기능 내장
- Form 처리, 유효성 검사 자동화
- URL 라우팅, 미들웨어 시스템

## 기타

Django는 2005년 미국 캔자스주 신문사 Lawrence Journal-World에서 시작됐다. 뉴스 사이트를 빠르게 만들어야 했던 개발자들이 공통 코드를 프레임워크로 정리한 게 시작이었다. 이름은 재즈 기타리스트 Django Reinhardt에서 따왔다.

"배터리 포함(batteries included)"이라는 표현이 Django 철학을 잘 나타낸다. [[Flask]]는 필요한 걸 직접 고르는 "조립식"이라면, Django는 "완제품"에 가깝다. 초보자한테는 Django가 친절하지만, 숙련자는 Django가 간섭한다고 느낄 수 있다.

Instagram이 Django로 만들어졌다는 건 유명한 사실인데, 2016년 시점에 Python 2에서 Python 3로 마이그레이션했을 때 코드베이스가 수백만 줄이었다는 후기가 있다. 그 규모에서도 Django 쓸 수 있다는 증거.

한국에서는 "Django 하면 관리자 페이지"라는 인식이 강하다. 실제로 모델 정의하면 자동으로 CRUD 되는 관리자 페이지 생성은 Django의 킬러 기능이다. 스타트업이 내부 관리 도구 만들 때 Django 선택하는 이유 중 하나.
