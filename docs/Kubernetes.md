---
title: Kubernetes
aliases: ["k8s", "kubernetes", "쿠버네티스", "큐브"]
---

# Kubernetes

> 컨테이너를 대규모로 관리하고 오케스트레이션할 때

[[컨테이너 오케스트레이션]] 플랫폼이다. 구글이 내부에서 쓰던 Borg 시스템을 오픈소스화한 것. 2014년에 공개됐고, 현재 컨테이너 오케스트레이션의 사실상 표준.

[[Docker]]로 컨테이너 만들고, Kubernetes로 관리한다. 수십~수천 개의 컨테이너를 자동으로 배포, 스케일링, 롤링 업데이트, 복구해준다.

대규모 서비스, [[마이크로서비스]] 아키텍처에서 필수다. 하지만 소규모 프로젝트에는 오버스펙. 컨테이너 몇 개면 [[Docker Compose]]로 충분하다.

## 성능

오케스트레이션 오버헤드는 있다. Control Plane(API 서버, etcd, 스케줄러 등)이 리소스 먹음. 작은 클러스터에서는 노드의 10~20% 차지.

네트워크 오버헤드도 있다. Service, Ingress를 통한 라우팅에 약간의 지연. 하지만 수평 확장의 이점이 훨씬 크다.

Auto Scaling이 핵심. HPA(Horizontal Pod Autoscaler)로 CPU/메모리 기준 자동 스케일. VPA(Vertical)로 리소스 자동 조정. Cluster Autoscaler로 노드까지 자동 확장.

## 생태계

[[Helm]]이 패키지 매니저. 차트로 복잡한 애플리케이션 한 번에 배포. 공식 차트 저장소에 수백 개 차트.

[[Prometheus]] + [[Grafana]]로 모니터링. [[ELK Stack]]이나 [[Loki]]로 로깅. [[Istio]], [[Linkerd]]로 서비스 메시.

매니지드 서비스: [[EKS]](AWS), [[GKE]](Google), [[AKS]](Azure). 직접 설치보다 훨씬 편함. 프로덕션에서는 매니지드 추천.

## 주의점

**러닝커브 높음**: Pod, Service, Deployment, ConfigMap, Secret, Ingress... 개념이 많다. YAML 지옥. 기초부터 차근차근 배워야 함.

**YAML 관리**: 매니페스트 파일이 수십~수백 개. [[Kustomize]]나 [[Helm]]으로 관리. GitOps([[ArgoCD]], [[Flux]])로 버전 관리.

**리소스 요청/제한 설정**: requests, limits 안 하면 노드 터짐. 한 Pod이 노드 리소스 다 먹을 수 있음. 적절한 값 설정 필수.

**네트워크 정책**: 기본은 모든 Pod 간 통신 허용. NetworkPolicy로 격리해야 보안 확보.

**etcd 백업**: 클러스터 상태가 etcd에 저장됨. 정기 백업 필수. 복구 연습도 해두자.

**업그레이드 주의**: 마이너 버전 하나씩 올려야 함. 한 번에 여러 버전 점프하면 문제.

## 주요 기능

- Pod 스케줄링, 자동 복구
- Deployment로 롤링 업데이트, 롤백
- Service로 로드밸런싱
- Ingress로 외부 노출
- ConfigMap, Secret으로 설정 분리
- 수평 자동 확장 (HPA)
- 스토리지 오케스트레이션 (PV, PVC)
- 네임스페이스로 멀티테넌시

## 기타

구글이 Borg라는 내부 시스템을 10년 넘게 썼는데, 그 경험을 바탕으로 Kubernetes를 만들었다. 2014년 오픈소스로 공개했고, 2015년 CNCF(Cloud Native Computing Foundation)에 기증했다. Google, Red Hat, Microsoft, IBM 등이 같이 개발하고 있다.

이름은 그리스어로 "키잡이, 조타수"를 뜻한다. 배의 방향을 조종하는 사람. 로고의 바퀴 모양(helm)도 여기서 왔다. "K8s"라고 줄여 쓰는데, K와 s 사이에 8글자가 있어서 그렇다. i18n(internationalization), a11y(accessibility)와 같은 방식.

Kubernetes를 "쿠버네티스", "쿠버네테스", "큐버네티스" 등 다양하게 발음하는데, 공식 발음은 "쿠버네티스"에 가깝다. 영어로는 "koo-ber-net-eez". 커뮤니티에서는 그냥 "K8s" 또는 "케이에잇에스"라고 부르기도 한다.

"YAML 엔지니어" 농담이 있다. Kubernetes 쓰다 보면 YAML 파일만 수백 개 작성하게 되니까. [[Helm]], [[Kustomize]] 같은 도구가 이 문제를 완화하려고 나온 거다. 그래도 YAML 지옥에서 완전히 벗어나기는 어렵다.
