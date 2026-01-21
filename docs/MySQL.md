---
aliases: [마이에스큐엘, mysql, MariaDB]
---

# MySQL

> 검증된 [[관계형 데이터베이스]]가 필요할 때

[[오픈소스]] [[관계형 데이터베이스]]다. 1995년에 나왔고, 세계에서 가장 많이 쓰이는 [[RDBMS]] 중 하나. 현재는 [[Oracle]]이 소유하고 있다. 포크 버전인 [[MariaDB]]도 많이 쓰인다.

웹 서비스 백엔드에서 압도적으로 많이 쓴다. [[WordPress]], [[Drupal]] 같은 CMS부터 Facebook, Twitter, YouTube까지 MySQL 기반으로 시작했다. LAMP 스택(Linux, Apache, MySQL, PHP)의 M이 이거다.

[[PostgreSQL]]보다 단순하고 빠르게 시작할 수 있다. 기본적인 CRUD 작업이라면 MySQL로 충분하다. 복잡한 쿼리, 고급 데이터 타입, 확장 기능이 필요하면 [[PostgreSQL]]을 고려하자.

## 성능

읽기 성능이 좋다. 단순한 SELECT 쿼리는 매우 빠르다. 쓰기가 많은 워크로드에서는 [[PostgreSQL]]이 더 나을 수 있다.

[[InnoDB]]가 기본 스토리지 엔진이다. 트랜잭션, 외래키, 행 수준 잠금을 지원한다. 예전에 쓰던 [[MyISAM]]은 이제 거의 안 쓴다.

인덱스 설계가 성능의 90%다. `EXPLAIN` 명령으로 실행 계획 확인하고, 슬로우 쿼리 로그 분석해서 최적화해야 한다. 커버링 인덱스, 복합 인덱스 잘 쓰면 극적인 성능 향상 가능.

커넥션 풀링 중요하다. 커넥션 하나당 메모리 수 MB 먹으니까 커넥션 수 관리해야 한다. [[ProxySQL]]이나 애플리케이션 레벨 풀링 쓰자.

## 생태계

모든 프로그래밍 언어에 드라이버가 있다. [[JDBC]], [[MySQL Connector]], [[mysqlclient]], [[mysql2]] 등. [[ORM]]도 다 지원한다. [[Sequelize]], [[TypeORM]], [[SQLAlchemy]], [[JPA]] 다 된다.

관리 도구도 많다. [[MySQL Workbench]] 공식 GUI, [[phpMyAdmin]] 웹 기반, [[DBeaver]] 범용 클라이언트. [[Percona Toolkit]]으로 운영 자동화.

클라우드에서는 [[Amazon RDS]], [[Google Cloud SQL]], [[Azure Database for MySQL]]로 매니지드 서비스 사용 가능. 운영 부담 줄이고 싶으면 이쪽으로.

[[MySQL Cluster]]로 분산 처리, [[Group Replication]]으로 고가용성 구성 가능. 하지만 설정이 복잡하다.

## 주의점

**인코딩 지옥**: `utf8`이 진짜 UTF-8이 아니다. 이모지 저장하려면 `utf8mb4` 써야 한다. 테이블 생성할 때 `CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci` 꼭 지정하자. 나중에 바꾸려면 마이그레이션 지옥이다.

**타임존 문제**: 서버 타임존, 커넥션 타임존, 컬럼 타입(DATETIME vs TIMESTAMP) 다 다르게 동작한다. UTC로 통일하고 애플리케이션에서 변환하는 게 안전하다.

**락 이슈**: InnoDB는 행 수준 잠금인데, 인덱스 안 타면 테이블 락 걸린다. 트랜잭션 길게 잡으면 데드락 발생. `SHOW ENGINE INNODB STATUS`로 락 상태 확인하자.

**대용량 데이터**: 테이블이 수억 건 넘어가면 ALTER TABLE이 몇 시간 걸린다. [[pt-online-schema-change]]나 [[gh-ost]] 써서 무중단 스키마 변경해야 한다.

**복제 지연**: Master-Slave 복제 쓸 때 슬레이브가 밀릴 수 있다. 쓰기 직후 읽기하면 데이터가 없을 수 있음. [[GTID]] 기반 복제 쓰고, Read-Your-Writes 패턴 적용하자.

**SQL 모드**: `STRICT_TRANS_TABLES` 모드 안 켜면 잘못된 데이터 들어가도 에러 안 나고 잘린다. 운영 환경에서는 strict 모드 필수.

**백업 주의**: `mysqldump`는 락 걸린다. 큰 DB는 [[Percona XtraBackup]] 쓰자. 바이너리 로그 보관해서 PITR(시점 복구) 가능하게 해두자.

## 주요 기능

- [[ACID]] 트랜잭션 지원 (InnoDB)
- [[리플리케이션]] (Master-Slave, Group Replication)
- 파티셔닝으로 대용량 테이블 관리
- 전문 검색 (Full-Text Search)
- JSON 데이터 타입 지원
- 스토어드 프로시저, 트리거, 뷰

## 기타

MySQL은 스웨덴 회사 MySQL AB에서 만들었다. 이름의 "My"는 공동 창립자의 딸 이름이라는 설이 있다. 2008년 Sun Microsystems가 인수했고, 2010년 Oracle이 Sun을 인수하면서 Oracle 소유가 됐다.

Oracle 인수 당시 오픈소스 커뮤니티가 발칵 뒤집혔다. "Oracle이 MySQL을 죽일 것"이라는 우려가 나왔고, 이게 [[MariaDB]] 포크의 계기가 됐다. MariaDB는 MySQL 원래 개발자가 만든 거라 코드베이스가 거의 같다. 실제로 많은 기업이 MariaDB로 갈아탔다.

"utf8"이 진짜 UTF-8이 아니라는 건 MySQL의 유명한 함정이다. 이모지 저장하려면 utf8mb4 써야 한다. 이거 때문에 삽질한 개발자가 한둘이 아니다. MySQL 8.0부터는 utf8mb4가 기본값이 됐다.

Facebook, Twitter, YouTube가 MySQL로 시작했다. 지금은 규모가 커져서 자체 개량 버전을 쓰지만, 초기엔 그냥 MySQL이었다. "일단 MySQL로 시작하고 나중에 고민하자"는 전략이 검증된 셈.
