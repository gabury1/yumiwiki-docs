---
title: Nginx
aliases: ["nginx", "엔진엑스", "웹서버"]
---

# Nginx

> 고성능 웹 서버나 리버스 프록시가 필요할 때

[[웹 서버]]이자 [[리버스 프록시]]다. 2004년 러시아 개발자 Igor Sysoev가 만들었다. [[Apache]]의 C10K 문제(동시 1만 연결 처리)를 해결하려고 설계됐다.

현재 가장 많이 쓰이는 웹 서버다. 전체 웹 서버 시장의 30% 이상. Netflix, Cloudflare, WordPress.com 등 대형 서비스가 쓴다.

정적 파일 서빙, 리버스 프록시, [[로드 밸런싱]], SSL 종료, [[캐싱]] 등 여러 역할을 한다. [[Docker]] 환경에서도 필수 인프라.

## 성능

이벤트 기반 비동기 아키텍처다. [[Apache]]는 요청당 프로세스/스레드인데, Nginx는 워커 프로세스 몇 개로 수만 연결을 처리한다. 메모리 사용량이 적고 동시 접속에 강하다.

정적 파일 서빙이 엄청 빠르다. 커널 레벨 최적화(sendfile, TCP_CORK)를 활용. 동적 콘텐츠는 [[FastCGI]], [[uWSGI]], 프록시로 백엔드에 넘긴다.

적은 리소스로 많은 요청 처리 가능. 메모리 수십 MB로 초당 수만 요청 처리. 클라우드 비용 절감에 직접적으로 기여.

## 생태계

설정 파일이 직관적이다. `nginx.conf`에 서버 블록, 로케이션 블록으로 구성. 배우기 쉽고 읽기 쉽다.

모듈로 기능 확장. [[Lua]], [[GeoIP]], [[Image Filter]] 등. [[OpenResty]]는 Nginx + Lua로 웹 애플리케이션 서버 역할도 가능.

[[NGINX Plus]]가 상용 버전. 세션 지속성, 헬스체크 고급 기능, 대시보드, 기술 지원 제공. 큰 회사에서 쓴다.

[[Kubernetes]]에서 [[Ingress Controller]]로 많이 쓴다. 외부 트래픽을 클러스터 내부 서비스로 라우팅.

## 주의점

**설정 문법 실수**: 세미콜론 빠뜨리면 안 됨. `nginx -t`로 문법 검사 꼭 하고 reload. 잘못된 설정으로 reload하면 서비스 중단.

**worker_processes 설정**: 보통 CPU 코어 수로 설정. `auto`로 하면 자동 감지. worker_connections는 동시 연결 수, 보통 1024~4096.

**upstream 헬스체크**: 오픈소스 버전은 수동 헬스체크만 됨. 백엔드 죽어도 한동안 요청 보냄. [[NGINX Plus]] 쓰거나 별도 모니터링 필요.

**버퍼 설정**: 백엔드 응답이 크면 디스크에 임시 저장. proxy_buffer_size, proxy_buffers 튜닝 필요. 에러 로그에 "upstream sent too big header" 나오면 버퍼 문제.

**타임아웃 설정**: proxy_connect_timeout, proxy_read_timeout 등 제대로 설정. 백엔드 느리면 타임아웃 터짐. 너무 길게 잡으면 커넥션 물고 있음.

**로그 관리**: access_log, error_log 쌓이면 디스크 꽉 찬다. logrotate 설정 필수. 또는 syslog로 중앙 로깅.

**SSL 설정**: SSL Labs에서 A+ 받으려면 설정 신경 써야 함. ssl_protocols, ssl_ciphers, HSTS, OCSP Stapling 등. Mozilla SSL Configuration Generator 참고.

**캐시 무효화**: proxy_cache 쓸 때 캐시 갱신 전략 고민. purge 모듈 없으면 캐시 삭제 어려움.

## 주요 기능

- 정적 파일 서빙
- 리버스 프록시
- [[로드 밸런싱]] (Round Robin, Least Connections, IP Hash)
- SSL/TLS 종료
- HTTP [[캐싱]]
- Gzip 압축
- Rate Limiting
- URL Rewriting
- 가상 호스트 (Server Blocks)
- WebSocket 프록시

## 기타

Igor Sysoev는 러시아 프로그래머다. 2002년 Rambler(러시아 포털 사이트)에서 일하면서 Nginx를 만들기 시작했다. C10K 문제를 해결하는 게 목표였다. 이름 발음은 "엔진 엑스"가 공식이지만 한국에서는 "엔진엑스", "엔진X" 다 쓴다.

시장 점유율이 [[Apache]]를 추월했다. W3Techs 통계에서 Nginx가 1위를 차지하고 있다. 웹 서버 시장의 30% 이상. Netflix, Cloudflare, Dropbox, WordPress.com 같은 대형 서비스들이 Nginx를 쓴다.

Nginx Inc.라는 회사가 2011년에 설립됐다. 오픈소스 Nginx 외에 NGINX Plus라는 상용 버전을 판매한다. 2019년 F5 Networks가 6억 7천만 달러에 인수했다. 오픈소스 프로젝트는 계속 무료로 유지되고 있다.

설정 파일 문법이 독특해서 "Nginx conf 문법"이라는 게 따로 있다. 들여쓰기, 세미콜론, 중괄호 규칙이 있다. 처음 보면 낯설지만 익숙해지면 직관적이다. [[Apache]]의 .htaccess보다 깔끔하다는 평가가 많다.
