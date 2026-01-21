---
aliases: [포스트그레스, Postgres, postgres, 포스트그레SQL]
---

# PostgreSQL

> 복잡한 쿼리와 데이터 무결성이 중요할 때

[[오픈소스]] [[관계형 데이터베이스]]다. 1996년에 나왔고, "세계에서 가장 진보한 오픈소스 데이터베이스"를 표방한다. [[MySQL]]보다 기능이 많고 표준 SQL을 더 잘 따른다.

데이터 무결성, 복잡한 쿼리, 고급 데이터 타입이 필요하면 PostgreSQL이다. 금융, 의료, GIS 같이 데이터 정확성이 중요한 분야에서 많이 쓴다. [[Uber]], [[Instagram]], [[Spotify]], [[Discord]]가 PostgreSQL 쓴다.

[[MySQL]]보다 학습 곡선이 있다. 설정 옵션이 많고, 개념도 더 복잡하다. 하지만 제대로 쓰면 훨씬 강력하다. 스타트업은 [[MySQL]]로 시작하고 나중에 PostgreSQL로 마이그레이션하는 경우도 많다.

## 성능

쓰기 성능이 [[MySQL]]보다 좋은 경우가 많다. MVCC 구현이 더 정교해서 동시성 처리가 강하다. 복잡한 JOIN, 서브쿼리도 옵티마이저가 잘 처리한다.

[[VACUUM]]이 핵심이다. PostgreSQL은 UPDATE/DELETE해도 기존 행을 바로 안 지운다. VACUUM이 정리해준다. autovacuum 설정 잘 해야 테이블 비대화(bloat) 방지.

파티셔닝, 병렬 쿼리 지원으로 대용량 처리 가능. [[TimescaleDB]] 확장 쓰면 시계열 데이터도 빠르게 처리한다. [[Citus]]로 분산 처리도 가능.

인덱스 종류가 다양하다. B-tree 기본이고, GiST, GIN, BRIN 등 용도별 인덱스가 있다. 전문 검색은 GIN, 지리 데이터는 GiST, 대용량 테이블은 BRIN 쓴다.

## 생태계

확장(Extension) 시스템이 강력하다. [[PostGIS]]로 지리 정보 처리, [[pg_trgm]]으로 퍼지 검색, [[pgvector]]로 벡터 임베딩 저장/검색 (AI 시대에 중요). `CREATE EXTENSION` 한 줄로 설치.

JSON 지원이 우수하다. `jsonb` 타입으로 NoSQL처럼 쓸 수 있다. 인덱싱도 되고, JSON 안의 필드로 쿼리도 가능. [[MongoDB]] 대신 PostgreSQL + JSONB 쓰는 팀도 많다.

관리 도구: [[pgAdmin]] 공식 GUI, [[DBeaver]], [[DataGrip]]. CLI는 `psql`이 강력하다. [[pg_dump]], [[pg_restore]]로 백업/복원.

클라우드: [[Amazon RDS]], [[Google Cloud SQL]], [[Azure Database]], [[Supabase]], [[Neon]] 등 매니지드 옵션 많다.

## 주의점

**VACUUM 관리 필수**: autovacuum이 기본으로 켜져 있지만, 쓰기가 많은 테이블은 설정 튜닝해야 한다. `pg_stat_user_tables`에서 dead tuple 수 모니터링하자. VACUUM FULL은 락 걸리니 조심.

**커넥션 관리**: PostgreSQL은 커넥션당 프로세스를 fork한다. 커넥션 많아지면 메모리 폭발. [[PgBouncer]]나 [[Pgpool-II]] 같은 커넥션 풀러 필수. 100개 이상이면 풀러 쓰자.

**OID 래핑**: 32비트 트랜잭션 ID가 42억을 넘으면 래핑된다. VACUUM이 잘 돌아야 방지됨. 방치하면 DB가 멈춘다. `age(datfrozenxid)`로 모니터링.

**마이그레이션 주의**: `ALTER TABLE`로 컬럼 추가는 빠르지만, 타입 변경이나 NOT NULL 추가는 테이블 전체 재작성이라 오래 걸린다. [[pg_repack]]으로 무중단 처리 가능.

**인코딩**: 기본이 UTF-8이라 [[MySQL]]처럼 헷갈릴 일 없다. 다만 collation 설정에 따라 정렬 순서 다르니 `CREATE DATABASE` 할 때 확인.

**백업 전략**: `pg_dump`는 논리 백업이라 대용량에선 느리다. [[pg_basebackup]]으로 물리 백업하고, WAL 아카이빙으로 PITR 구성하자. [[Barman]], [[pgBackRest]] 같은 도구 쓰면 편함.

**읽기 복제 지연**: Streaming Replication 쓸 때 Standby가 밀릴 수 있다. `hot_standby_feedback` 켜면 좀 나아지지만 VACUUM 지연될 수 있다.

## 주요 기능

- [[ACID]] 완벽 지원, MVCC 동시성 제어
- 다양한 데이터 타입 (JSONB, Array, Range, UUID, INET 등)
- 강력한 인덱스 (B-tree, Hash, GiST, GIN, BRIN)
- CTE, 윈도우 함수, 재귀 쿼리 등 고급 SQL
- 확장 시스템 ([[PostGIS]], [[pgvector]] 등)
- 논리적 복제, 스트리밍 복제
- Row Level Security (행 단위 접근 제어)

## 기타

PostgreSQL의 역사는 1986년 버클리대 POSTGRES 프로젝트까지 거슬러 올라간다. SQL을 넣어서 PostgreSQL이 됐고, 오픈소스로 전환된 게 1996년. 거의 30년 역사다. [[MySQL]]보다 오래됐지만 대중화는 늦었다.

"코끼리" 로고가 PostgreSQL의 마스코트다. 왜 코끼리냐고 묻는 사람이 많은데, 코끼리는 기억력이 좋고 무겁지만 강하다는 의미로 골랐다고 한다. 커뮤니티에서는 코끼리를 "Slonik"이라고 부른다.

Apple이 macOS에 PostgreSQL을 기본 탑재한다. Spotlight 검색이나 Mail.app 같은 게 내부적으로 PostgreSQL을 쓴다. 일반 사용자는 모르지만 PostgreSQL이 Mac에 깔려 있다.

"PostgreSQL은 [[MongoDB]]를 죽였다"는 농담이 있다. JSONB 타입이 추가되면서 NoSQL 기능을 흡수해버렸다. 실제로 "MongoDB 대신 PostgreSQL + JSONB 쓰자"는 글이 주기적으로 올라온다. 인덱싱도 되고 트랜잭션도 되니까 PostgreSQL 쓰는 게 낫다는 주장.
