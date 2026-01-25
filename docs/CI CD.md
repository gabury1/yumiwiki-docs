---
title: CI/CD
aliases: ["ci/cd", "ci", "cd", "지속적통합", "지속적배포", "cicd"]
---

# CI/CD

> 코드 작성부터 배포까지의 자동화 고속도로

**지속적 통합(Continuous Integration)**과 **지속적 제공/배포(Continuous Delivery/Deployment)**의 약자. 애플리케이션 개발 단계를 자동화하여 더 짧은 주기로 고객에게 서비스를 제공하는 방법론이다.

## 개념 나누기

### CI (지속적 통합)
개발자가 코드를 원격 저장소([[Git]] 등)에 푸시(Push)할 때마다 **자동으로 빌드하고 테스트**하는 과정.
- 목표: 버그를 조기에 발견하고, "내 컴퓨터에선 되는데?" 문제를 없애는 것.
- 도구: [[Jenkins]], [[GitHub Actions]], CircleCI.

### CD (지속적 제공/배포)
CI를 통과한 코드를 **자동으로 실제 서비스 환경에 릴리즈**하는 과정.
- **Continuous Delivery**: 프로덕션 배포 전까지 모든 과정을 자동화하고, 최종 배포는 사람의 승인 하에 진행.
- **Continuous Deployment**: 테스트만 통과하면 사람 개입 없이 바로 고객에게 배포.
- 도구: [[ArgoCD]](Kubernetes 전용), AWS CodeDeploy.

## Mechanism (작동 방식)

1. **Commit**: 개발자가 코드를 [[GitHub]]에 푸시한다.
2. **Trigger**: 웹훅(Webhook)이 CI 서버(예: [[GitHub Actions]])를 깨운다.
3. **Build & Test**: CI 서버가 [[Docker]] 컨테이너를 띄우고 코드를 빌드하고 테스트([[Jest]], [[JUnit]] 등)를 돌린다.
4. **Image Build**: 성공하면 실행 가능한 아티팩트(JAR 파일, Docker 이미지 등)를 만든다.
5. **Deploy**: CD 도구가 이 아티팩트를 가져와서 실제 서버([[AWS]] EC2, [[Kubernetes]] 클러스터)에 배포한다.

## 장점

- **속도**: 하루에 수십 번 배포 가능하다. 기능 출시가 빨라진다.
- **안정성**: 사람이 수동으로 배포하다가 생기는 실수(스크립트 누락 등)가 없어진다.
- **피드백**: 코드가 깨졌는지 즉시 알 수 있다.

## 주요 CI/CD 솔루션

### 1. 보편적인 도구
- [Jenkins](https://www.jenkins.io/): 가장 널리 쓰이는 오픈소스 자동화 서버. 플러그인이 풍부하고 커스터마이징이 강력하다.
- [GitHub Actions](https://github.com/features/actions): [[GitHub]] 플랫폼에 내장된 서비스. 별도 서버 구축 없이 `YAML` 파일 하나로 자동화가 가능하다.
- [GitLab CI/CD](https://about.gitlab.com/topics/ci-cd/): [[GitLab]] 저장소와 완벽하게 통합된 올인원 DevOps 도구.

### 2. GitOps 및 Kubernetes 특화 도구
- [Argo CD](https://argo.cd/): Kubernetes 환경에서의 선언적 GitOps 배포 도구.
- [Flux CD](https://fluxcd.io/): Kubernetes의 상태를 Git 저장소와 동기화해주는 GitOps 솔루션.

### 3. SaaS형 CI/CD 솔루션
- [CircleCI](https://circleci.com/): 빠른 성능과 효율적인 리소스 관리를 제공하는 클라우드 기반 서비스.
- [Travis CI](https://www.travis-ci.com/): 오픈소스 커뮤니티에서 전통적으로 많이 쓰이던 CI 도구.
- [Bitbucket Pipelines](https://atlassian.com/software/bitbucket/features/pipelines): Atlassian 제품군(Jira 등)과 연동이 뛰어난 솔루션.

### 4. 클라우드 벤더 서비스
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/): AWS 생태계 내의 빌드, 테스트, 배포를 연결하는 서비스.
- [Azure Pipelines](https://azure.microsoft.com/en-us/products/devops/pipelines): Microsoft Azure 환경에 최적화된 CI/CD 파이프라인.
- [Google Cloud Build](https://cloud.google.com/build): GCP의 서버리스 인프라에서 작동하는 빌드 서비스.

## 기타

DevOps 문화의 핵심이다. "하루에 몇 번 배포할 수 있는가?"가 엔지니어링 조직의 역량을 보여주는 지표(DORA metrics)로 쓰이기도 한다.

무중단 배포(Zero Downtime Deployment)를 위해 **[[블루-그린 배포]]**, **[[롤링 업데이트]]**, **[[카나리 배포]]** 등의 전략과 함께 쓰인다.
