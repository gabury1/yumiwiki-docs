---
title: Python
aliases: ["py", "python", "파이썬"]
---

# Python

> 읽기 쉽고 빠르게 개발하고 싶을 때

1991년 Guido van Rossum이 만든 [[인터프리터]] 언어다. "코드는 시를 읽듯 읽혀야 한다"는 철학으로 설계됐다. 문법이 간결하고 직관적이라 프로그래밍 입문용으로 가장 많이 쓰인다.

웹 개발([[Django]], [[FastAPI]]), 데이터 분석([[pandas]], [[NumPy]]), [[머신러닝]]([[TensorFlow]], [[PyTorch]]), 자동화 스크립트까지 쓰이지 않는 곳이 없다. "배터리 포함(Batteries Included)" 철학으로 표준 라이브러리가 방대하다.

## 탄생 배경

1980년대 말, Guido van Rossum이 크리스마스 휴가 동안 취미로 만들기 시작했다. ABC 언어의 영향을 받았고, Unix 셸 스크립팅을 대체할 언어를 원했다. 이름은 영국 코미디 그룹 "Monty Python"에서 따왔다. 뱀과는 무관하지만 로고는 뱀이다.

1990년대에는 틈새 언어였다. 2000년대 [[Google]]이 적극 채택하면서 주목받기 시작했다. YouTube, Instagram, Dropbox가 Python으로 만들어지면서 입지가 굳어졌다. 2010년대 데이터 과학과 [[머신러닝]] 붐으로 폭발적으로 성장했다.

## 특징

**동적 타이핑**: 변수 타입을 선언 안 해도 된다. `x = 5` 하면 끝. 빠르게 프로토타입 만들 때 편하지만, 큰 프로젝트에선 버그 원인이 되기도 한다. Python 3.5부터 타입 힌트 지원.

**들여쓰기 강제**: 중괄호 대신 들여쓰기로 블록 구분. 코드가 깔끔해지지만, 탭/스페이스 섞으면 에러난다. 이거 때문에 논쟁 많다.

**가비지 컬렉션**: 메모리 관리 자동. [[레퍼런스 카운팅]]과 [[순환 참조]] 감지 방식 혼용.

**멀티 패러다임**: [[객체지향]], [[함수형]], [[절차적 프로그래밍]] 다 지원. 원하는 스타일로 짤 수 있다.

**GIL (Global Interpreter Lock)**: [[멀티스레딩]]으로 CPU 바운드 작업을 병렬화할 수 없다. 이게 Python의 가장 큰 약점. I/O 바운드는 문제없고, CPU 바운드는 [[multiprocessing]]으로 우회.

## 성능

솔직히 느리다. [[C]], [[Java]], [[Go]]보다 10~100배 느릴 수 있다. [[인터프리터]] 언어라 컴파일 언어보다 느린 건 당연하다.

하지만 개발 속도가 빠르다. 같은 기능을 [[Java]]로 100줄 짤 거 Python은 20줄로 끝난다. "컴퓨터 시간보다 개발자 시간이 비싸다"는 말이 있다. 프로토타입, MVP, 데이터 분석처럼 빠른 개발이 중요한 곳에서 Python을 선택한다.

성능이 중요한 부분은 [[C]] 확장으로 작성한다. [[NumPy]], [[pandas]]가 이렇게 만들어졌다. Python으로 인터페이스만 제공하고 내부는 C로 동작.

[[PyPy]] [[JIT]] 컴파일러를 쓰면 2~5배 빨라진다. 단, 모든 라이브러리가 호환되는 건 아니다.

## 버전

**Python 2 vs 3**: 2000년 Python 2.0, 2008년 Python 3.0 출시. Python 3는 하위 호환성을 버렸다. `print "hello"` → `print("hello")` 같은 변화. 커뮤니티가 10년 넘게 둘로 나뉘어 혼란스러웠다. 2020년 Python 2 공식 지원 종료.

**현재**: Python 3.12 (2023). 매년 10월 새 버전 출시. 3.6부터 f-string, 3.10부터 structural pattern matching 등 계속 개선되고 있다.

## 생태계

**패키지 관리**: [[pip]], [[Poetry]], [[conda]]. PyPI에 패키지 40만 개 이상.

**웹 프레임워크**: [[Django]], [[FastAPI]], [[Flask]]

**데이터 과학**: [[pandas]], [[NumPy]], [[SciPy]], [[matplotlib]], [[seaborn]]

**머신러닝/딥러닝**: [[TensorFlow]], [[PyTorch]], [[scikit-learn]], [[Keras]], [[XGBoost]]

**자동화**: [[Selenium]], [[Beautiful Soup]], [[Scrapy]]

**테스트**: [[pytest]], [[unittest]]

**비동기**: [[asyncio]], [[aiohttp]], [[Trio]]

**가상환경**: [[venv]], [[virtualenv]], [[pipenv]]

**타입 체킹**: [[mypy]], [[Pydantic]]

## 주의점

**GIL 문제**: CPU 바운드 작업은 [[multiprocessing]] 쓰거나 다른 언어 고려.

**패키지 의존성 지옥**: 패키지마다 요구하는 버전이 다르면 충돌. [[가상환경]] 필수.

**Python 2 레거시 코드**: 아직도 Python 2 코드가 많다. 마이그레이션 필요.

**들여쓰기**: 탭과 스페이스 섞으면 `TabError`. 에디터 설정 통일 필수.

**모바일 앱**: iOS/Android 네이티브 앱 개발에는 부적합. [[Kivy]] 있지만 주류 아님.

**속도**: 실시간 처리, 게임 엔진, 시스템 프로그래밍에는 느림.

## 주요 기능

- 간결하고 읽기 쉬운 문법
- 방대한 표준 라이브러리
- [[REPL]] (Read-Eval-Print Loop) 인터프리터
- [[List Comprehension]], [[Generator]], [[Decorator]]
- [[Duck Typing]], [[동적 타이핑]]
- [[Exception Handling]]
- [[Lambda 함수]], [[고차 함수]]
- [[Context Manager]] (`with` 문)

## 기타

창시자 Guido van Rossum은 커뮤니티에서 "BDFL (Benevolent Dictator For Life, 자비로운 종신 독재자)"라고 불렸다. 언어 설계 결정권을 가진 최종 권위자였다. 2018년 Python 커뮤니티 내 논쟁에 지쳐서 은퇴를 선언했다. 현재는 운영 위원회가 결정한다.

"Pythonic"이라는 말이 있다. Python다운 코드 스타일을 뜻한다. `import this` 치면 "The Zen of Python"이 나온다. "명시적이 암시적보다 낫다", "가독성이 중요하다" 같은 철학이 담겨 있다. 이게 Python 커뮤니티의 정체성이다.

`__init__`, `__str__`, `__repr__` 같은 던더(dunder, double underscore) 메서드가 많다. 처음 보면 낯설지만, 연산자 오버로딩이나 매직 메서드 구현에 쓴다. "명시적 는 것보다 매직이 낫다"는 Python의 또 다른 면이다.

Stack Overflow 2023 설문에서 "가장 원하는 언어" 1위. 배우기 쉽고, 쓸 곳 많고, 연봉도 괜찮다. 다만 "가장 무서운 언어"에도 자주 오른다. 타입 시스템 없고, 속도 느리고, GIL 때문.

[[ChatGPT]]나 [[Claude]] 같은 LLM이 Python 코드를 제일 잘 짠다. 학습 데이터에 Python 코드가 압도적으로 많아서. AI 시대에 Python의 위상은 더 올라갈 것 같다.
