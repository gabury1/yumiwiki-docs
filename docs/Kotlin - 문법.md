---
title: Kotlin - 문법
aliases: ["kotlin syntax", "코틀린 문법", "kotlin grammar"]
---

# Kotlin 문법

Kotlin의 주요 문법 요소들을 정리한 참고 문서입니다.

## 목차

- [변수와 상수](#변수와-상수)
- [기본 타입](#기본-타입)
- [함수](#함수)
- [클래스와 객체](#클래스와-객체)
- [제어 흐름](#제어-흐름)
- [Null 안전성](#null-안전성)
- [컬렉션](#컬렉션)
- [람다와 고차 함수](#람다와-고차-함수)
- [확장 함수](#확장-함수)
- [데이터 클래스](#데이터-클래스)
- [Sealed 클래스](#sealed-클래스)
- [Object와 Companion Object](#object와-companion-object)
- [인터페이스](#인터페이스)
- [제네릭](#제네릭)
- [코루틴](#코루틴)
- [스코프 함수](#스코프-함수)
- [연산자 오버로딩](#연산자-오버로딩)
- [위임](#위임)

---

## 변수와 상수

Kotlin은 변수 선언을 `var`와 `val` 두 가지로 구분한다. 이는 불변성(immutability)을 언어 차원에서 강제하는 Kotlin의 철학을 보여준다.

### var (가변 변수)

값을 바꿀 수 있는 변수다. Java의 일반 변수와 같다.

```kotlin
var name: String = "Kotlin"
name = "Java"  // 재할당 가능
```

**언제 쓸까?** 반복문의 카운터, 상태가 계속 바뀌는 UI 컴포넌트 등에서 사용한다.

### val (불변 변수)

한 번 할당하면 다시 바꿀 수 없는 변수다. Java의 `final`과 비슷하다.

```kotlin
val pi: Double = 3.14159
// pi = 3.14  // 컴파일 에러! 재할당 불가
```

**Kotlin의 권장 사항:** 가능하면 `val`을 쓰고, 꼭 필요할 때만 `var`를 쓰라. 버그가 줄어든다.

**재미있는 점:** `val`로 선언된 객체의 내부 상태는 바꿀 수 있다. 예를 들어 `val list = mutableListOf(1, 2, 3)`에서 `list.add(4)`는 가능하다. `val`은 참조를 고정할 뿐이다.

### 타입 추론

Kotlin은 똑똑해서 타입을 알아서 추론한다. 타입을 명시하지 않아도 된다.

```kotlin
val count = 10           // Int로 추론
val message = "Hello"    // String으로 추론
val price = 99.99        // Double로 추론
```

**주의:** 정수 리터럴은 기본적으로 `Int`, 소수점 리터럴은 `Double`로 추론된다. `Float`을 원하면 `99.99f`처럼 명시해야 한다.

### 지연 초기화

변수를 선언할 때 바로 초기화하지 않고 나중에 하고 싶을 때가 있다. 두 가지 방법이 있다.

```kotlin
// lateinit: var에만 사용 가능, primitive 타입 불가
lateinit var user: User

// lazy: val에만 사용 가능, 처음 접근 시 초기화
val database by lazy {
    createDatabase()
}
```

**lateinit vs lazy:**
- `lateinit`은 "나중에 내가 직접 초기화할게"라는 약속이다. Android의 `onCreate()`에서 뷰를 초기화할 때 자주 쓴다.
- `lazy`는 "처음 사용할 때 자동으로 초기화해줘"라는 의미다. 무거운 객체를 필요할 때만 만들고 싶을 때 유용하다.

**주의:** `lateinit` 변수를 초기화하기 전에 접근하면 `UninitializedPropertyAccessException`이 터진다. `::user.isInitialized`로 확인할 수 있다.

---

## 기본 타입

Kotlin은 모든 것이 객체다. Java처럼 primitive 타입과 wrapper 타입을 구분하지 않는다. 하지만 컴파일러가 알아서 최적화해서 성능 걱정은 안 해도 된다.

### 숫자 타입

```kotlin
val byte: Byte = 127
val short: Short = 32767
val int: Int = 2147483647
val long: Long = 9223372036854775807L

val float: Float = 3.14f
val double: Double = 3.141592653589793
```

**크기별 정리:**
- `Byte`: 8비트 (-128 ~ 127)
- `Short`: 16비트 (-32,768 ~ 32,767)
- `Int`: 32비트 (약 -21억 ~ 21억)
- `Long`: 64비트 (엄청 큰 수)
- `Float`: 32비트 소수
- `Double`: 64비트 소수 (더 정밀함)

**팁:** 숫자에 언더스코어를 넣어서 가독성을 높일 수 있다. `val million = 1_000_000`

### 문자와 문자열

```kotlin
val char: Char = 'A'
val string: String = "Hello, Kotlin"

// 문자열 템플릿
val name = "World"
val greeting = "Hello, $name!"
val length = "Length is ${name.length}"

// 여러 줄 문자열
val multiline = """
    첫 번째 줄
    두 번째 줄
    세 번째 줄
""".trimIndent()
```

**문자열 템플릿의 마법:** `$` 기호로 변수를 문자열 안에 바로 넣을 수 있다. Java의 `String.format()`이나 `+` 연산보다 훨씬 깔끔하다.

**여러 줄 문자열 (`"""`):** SQL 쿼리나 JSON 같은 긴 텍스트를 쓸 때 아주 편하다. 이스케이프(`\n`, `\"`)도 필요 없다.

**재미있는 점:** `trimIndent()`는 공통된 들여쓰기를 자동으로 제거해준다. 코드 포맷팅을 망치지 않으면서 깔끔한 문자열을 만들 수 있다.

### Boolean

```kotlin
val isActive: Boolean = true
val isCompleted = false
```

Java와 똑같다. `true` 또는 `false` 두 가지 값만 가능하다.

### 타입 변환

```kotlin
val num: Int = 100
val longNum: Long = num.toLong()
val doubleNum: Double = num.toDouble()
val stringNum: String = num.toString()
```

**중요:** Kotlin은 자동 타입 변환을 하지 않는다! Java에서는 `int`를 `long`에 자동으로 넣을 수 있지만, Kotlin에서는 명시적으로 `.toLong()`을 호출해야 한다.

**왜 이렇게 했을까?** 의도하지 않은 타입 변환으로 인한 버그를 방지하기 위해서다. 조금 귀찮아도 안전한 게 낫다는 철학이다.

---

## 함수

Kotlin의 함수는 일급 객체(first-class citizen)다. 변수에 저장하고, 인자로 전달하고, 반환할 수 있다.

### 기본 함수

```kotlin
fun add(a: Int, b: Int): Int {
    return a + b
}

// 단일 표현식 함수
fun multiply(a: Int, b: Int): Int = a * b

// 반환 타입 생략 (추론)
fun subtract(a: Int, b: Int) = a - b
```

**단일 표현식 함수:** 함수 본문이 한 줄이면 중괄호 없이 `=`로 바로 쓸 수 있다. 간결하고 함수형 프로그래밍 스타일이다.

**반환 타입 생략:** 단일 표현식 함수는 반환 타입을 생략할 수 있다. 컴파일러가 알아서 추론한다.

### 기본 매개변수

```kotlin
fun greet(name: String = "Guest", greeting: String = "Hello") {
    println("$greeting, $name!")
}

greet()                          // Hello, Guest!
greet("Alice")                   // Hello, Alice!
greet("Bob", "Hi")              // Hi, Bob!
greet(greeting = "Hey")         // Hey, Guest!
```

**Java와의 차이:** Java는 오버로딩으로 여러 버전의 함수를 만들어야 하지만, Kotlin은 기본값으로 한 번에 해결한다.

**명명된 인자(named arguments):** `greet(greeting = "Hey")`처럼 매개변수 이름을 명시할 수 있다. 인자가 많을 때 가독성이 좋아진다.

### 가변 인자 (vararg)

```kotlin
fun sum(vararg numbers: Int): Int {
    return numbers.sum()
}

sum(1, 2, 3, 4, 5)  // 15

// 배열을 가변 인자로 전달
val nums = intArrayOf(1, 2, 3)
sum(*nums)  // spread 연산자
```

**spread 연산자 (`*`):** 배열을 개별 인자로 펼쳐준다. Java의 `...`와 비슷하지만 사용 방식이 다르다.

**주의:** `vararg`는 함수당 하나만 쓸 수 있고, 보통 마지막 매개변수로 둔다.

### 중위 함수 (infix)

```kotlin
infix fun Int.times(str: String) = str.repeat(this)

val result = 3 times "Ha"  // "HaHaHa"
```

**언제 쓸까?** DSL(Domain Specific Language)을 만들 때 유용하다. `1 to "one"` 같은 Kotlin 표준 라이브러리도 infix를 쓴다.

**조건:** 멤버 함수이거나 확장 함수여야 하고, 매개변수가 정확히 하나여야 한다.

### 확장 함수

```kotlin
fun String.addExclamation(): String {
    return this + "!"
}

"Hello".addExclamation()  // "Hello!"
```

**마법 같은 기능:** 기존 클래스에 새로운 함수를 추가할 수 있다! `String` 클래스를 수정하지 않고도 마치 원래 있던 메서드처럼 쓸 수 있다.

**실제로는?** 컴파일 시점에 정적 함수로 변환된다. 런타임 오버헤드가 없다.

---

## 클래스와 객체

Kotlin 클래스의 가장 중요한 특징: **생성자 매개변수에 `val`/`var`를 붙이면 자동으로 프로퍼티가 된다.**

### 핵심 개념 1: val/var가 프로퍼티를 만든다

```kotlin
// val/var 없으면: 그냥 생성자 매개변수 (프로퍼티 아님)
class User(id: Int, username: String) {
    // id, username은 생성자에서만 쓸 수 있음
    // 클래스 밖에서 접근 불가!
}

val user = User(1, "alice")
// user.id  ❌ 에러! (프로퍼티가 아니라서)
// user.username  ❌ 에러!
```

```kotlin
// val/var 붙이면: 프로퍼티가 됨!
class User(val id: Int, var username: String) {
    // id, username이 자동으로 프로퍼티가 됨
}

val user = User(1, "alice")
println(user.id)  // ✅ 1 (접근 가능!)
println(user.username)  // ✅ "alice"

user.id = 2  // ❌ 에러! (val은 변경 불가)
user.username = "bob"  // ✅ OK (var는 변경 가능)
```

**이게 Kotlin의 핵심이다!** 생성자 매개변수에 `val`/`var`만 붙이면 자동으로 프로퍼티가 된다.

### 핵심 개념 2: init 블록에서 로직 수행

생성자에 로직을 넣고 싶으면 `init` 블록을 쓴다.

```kotlin
class User(val id: Int, val username: String, private var password: String) {
    
    // init: 객체 생성될 때 자동 실행
    init {
        println("User 생성됨: $username")
        
        // 유효성 검사
        require(username.isNotEmpty()) { "이름은 비어있을 수 없음" }
        require(password.length >= 8) { "비밀번호는 8자 이상" }
    }
}

// 사용
val user = User(1, "alice", "password123")
// 출력: User 생성됨: alice

val badUser = User(2, "", "short")
// 에러: 이름은 비어있을 수 없음
```

**왜 init을 쓸까?**
- 주 생성자는 매개변수만 선언 (본문 없음)
- 로직은 init 블록에 작성
- 여러 개 쓸 수 있고, 위에서 아래로 실행됨

### 핵심 개념 3: private으로 숨기기

```kotlin
class User(
    val id: Int,                    // public (기본값)
    var username: String,           // public
    private var password: String    // private (외부 접근 불가)
) {
    fun login(inputPassword: String): Boolean {
        return password == inputPassword  // 클래스 내부에서는 접근 가능
    }
}

val user = User(1, "alice", "secret123")
println(user.id)  // ✅ OK
println(user.username)  // ✅ OK
println(user.password)  // ❌ 에러! (private이라서)

user.login("secret123")  // ✅ OK (메서드로 접근)
```

### 단계별 예시: 간단 → 복잡

#### 1단계: 가장 간단한 클래스

```kotlin
class User(val id: Int, val name: String)

val user = User(1, "Alice")
println(user.id)    // 1
println(user.name)  // Alice
```

끝! 이게 전부다.

#### 2단계: 추가 프로퍼티

```kotlin
class User(val id: Int, val name: String) {
    var email: String = ""  // 추가 프로퍼티
    var age: Int = 0
}

val user = User(1, "Alice")
user.email = "alice@example.com"
user.age = 25
```

#### 3단계: init으로 검증

```kotlin
class User(val id: Int, val name: String) {
    var email: String = ""
    var age: Int = 0
    
    init {
        require(name.isNotEmpty()) { "이름 필수" }
        println("User 생성: $name")
    }
}

val user = User(1, "Alice")
// 출력: User 생성: Alice
```

#### 4단계: 메서드 추가

```kotlin
class User(val id: Int, var name: String) {
    var email: String = ""
    
    init {
        println("User 생성: $name")
    }
    
    fun updateEmail(newEmail: String) {
        email = newEmail
        println("이메일 변경: $email")
    }
    
    fun displayInfo() {
        println("ID: $id, 이름: $name, 이메일: $email")
    }
}

val user = User(1, "Alice")
user.updateEmail("alice@example.com")
user.displayInfo()
```

#### 5단계: 계산 프로퍼티

```kotlin
class User(val id: Int, val name: String) {
    var age: Int = 0
    
    // 접근할 때마다 계산
    val isAdult: Boolean
        get() = age >= 18
    
    val displayName: String
        get() = "User#$id: $name"
}

val user = User(1, "Alice")
user.age = 25

println(user.isAdult)  // true (계산됨)
println(user.displayName)  // "User#1: Alice"
```

#### 6단계: 부 생성자 (여러 방법으로 생성)

```kotlin
class User(val id: Int, val name: String) {
    var email: String = ""
    var age: Int = 0
    
    // 부 생성자: 이메일도 받기
    constructor(id: Int, name: String, email: String) : this(id, name) {
        this.email = email
    }
    
    // 부 생성자: 이메일과 나이 모두 받기
    constructor(id: Int, name: String, email: String, age: Int) : this(id, name, email) {
        this.age = age
    }
}

// 3가지 방법으로 생성 가능
val user1 = User(1, "Alice")
val user2 = User(2, "Bob", "bob@example.com")
val user3 = User(3, "Charlie", "charlie@example.com", 30)
```

**하지만 실전에서는 기본값을 쓰는 게 더 간단하다:**

```kotlin
class User(
    val id: Int,
    val name: String,
    var email: String = "",  // 기본값
    var age: Int = 0         // 기본값
)

// 같은 효과, 더 간단!
val user1 = User(1, "Alice")
val user2 = User(2, "Bob", "bob@example.com")
val user3 = User(3, "Charlie", "charlie@example.com", 30)
```

### 완전한 예시

이제 모든 개념을 합쳐보자:

```kotlin
class User(
    val id: Int,
    var username: String,
    private var password: String
) {
    // 추가 프로퍼티
    var email: String = ""
    var age: Int = 0
    
    // 초기화 로직
    init {
        require(username.isNotEmpty()) { "사용자명 필수" }
        require(password.length >= 8) { "비밀번호 8자 이상" }
        println("User 생성: $username")
    }
    
    // 계산 프로퍼티
    val isAdult: Boolean
        get() = age >= 18
    
    // 메서드
    fun login(inputPassword: String): Boolean {
        if (password == inputPassword) {
            println("$username 로그인 성공!")
            return true
        } else {
            println("비밀번호 틀림")
            return false
        }
    }
    
    fun displayInfo() {
        println("ID: $id, 이름: $username, 이메일: $email, 나이: $age")
    }
}

// 사용
fun main() {
    val user = User(1, "alice", "password123")
    user.email = "alice@example.com"
    user.age = 25
    
    println(user.isAdult)  // true
    user.login("wrongpass")  // 비밀번호 틀림
    user.login("password123")  // alice 로그인 성공!
    user.displayInfo()
}
```

**출력:**
```
User 생성: alice
true
비밀번호 틀림
alice 로그인 성공!
ID: 1, 이름: alice, 이메일: alice@example.com, 나이: 25
```

### 핵심 정리

1. **`val`/`var` 붙이면 프로퍼티** - 클래스 밖에서 접근 가능
2. **`init` 블록에 로직** - 생성 시 자동 실행
3. **`private`로 숨기기** - 외부 접근 차단
4. **계산 프로퍼티** - `get()`으로 매번 계산
5. **기본값 활용** - 부 생성자 대신 기본값 쓰기

이게 Kotlin 클래스의 전부다! 😊

---

## 제어 흐름

### if 표현식

```kotlin
// if는 표현식이므로 값을 반환
val max = if (a > b) a else b

val result = if (score >= 90) {
    "A"
} else if (score >= 80) {
    "B"
} else {
    "C"
}
```

### when 표현식

```kotlin
when (x) {
    1 -> println("One")
    2 -> println("Two")
    3, 4 -> println("Three or Four")
    in 5..10 -> println("Between 5 and 10")
    else -> println("Other")
}

// 값을 반환하는 when
val description = when (color) {
    "Red" -> "Stop"
    "Yellow" -> "Caution"
    "Green" -> "Go"
    else -> "Unknown"
}

// 조건식으로 사용
when {
    x > 0 -> println("Positive")
    x < 0 -> println("Negative")
    else -> println("Zero")
}

// 타입 체크
when (obj) {
    is String -> println("String of length ${obj.length}")
    is Int -> println("Integer: $obj")
    else -> println("Unknown type")
}
```

### for 루프

```kotlin
// 범위
for (i in 1..5) {
    println(i)  // 1, 2, 3, 4, 5
}

// until (마지막 제외)
for (i in 1 until 5) {
    println(i)  // 1, 2, 3, 4
}

// step
for (i in 0..10 step 2) {
    println(i)  // 0, 2, 4, 6, 8, 10
}

// 역순
for (i in 10 downTo 1 step 2) {
    println(i)  // 10, 8, 6, 4, 2
}

// 컬렉션 순회
val list = listOf("a", "b", "c")
for (item in list) {
    println(item)
}

// 인덱스와 함께
for ((index, value) in list.withIndex()) {
    println("$index: $value")
}
```

### while 루프

```kotlin
var x = 0
while (x < 5) {
    println(x)
    x++
}

do {
    println(x)
    x--
} while (x > 0)
```

### break와 continue

```kotlin
// 레이블 사용
outer@ for (i in 1..3) {
    for (j in 1..3) {
        if (i * j > 5) break@outer
        println("$i * $j = ${i * j}")
    }
}
```

---

## Null 안전성

Kotlin의 가장 유명한 기능 중 하나다. "10억 달러짜리 실수"라 불리는 `NullPointerException`을 컴파일 타임에 방지한다.

### Nullable 타입

```kotlin
var name: String = "Kotlin"
// name = null  // 컴파일 에러!

var nullableName: String? = "Kotlin"
nullableName = null  // OK
```

**핵심 아이디어:** 기본적으로 모든 변수는 null이 될 수 없다. null을 허용하려면 타입 뒤에 `?`를 붙여야 한다.

**왜 중요할까?** Java에서는 모든 참조 타입이 null일 수 있어서, 언제든 `NullPointerException`이 터질 수 있다. Kotlin은 이를 타입 시스템으로 해결했다.

### 안전 호출 연산자 (?.)

```kotlin
val length: Int? = nullableName?.length
// nullableName이 null이면 length도 null
```

**동작 방식:** null이 아니면 `.length`를 호출하고, null이면 그냥 null을 반환한다. if문 없이 안전하게 접근할 수 있다.

**체이닝 가능:** `user?.address?.city?.name` 이렇게 연속으로 쓸 수 있다. 중간에 하나라도 null이면 전체가 null이 된다.

### 엘비스 연산자 (?:)

```kotlin
val length: Int = nullableName?.length ?: 0
// nullableName이 null이면 0 반환
```

**이름의 유래:** `?:`를 옆으로 돌리면 엘비스 프레슬리의 헤어스타일처럼 보인다고 해서 붙여진 이름이다. 🕺

**실용적 사용:** null일 때 기본값을 제공하는 가장 간결한 방법이다. Java의 `value != null ? value : defaultValue`보다 훨씬 깔끔하다.

**응용:** `?: return`, `?: throw Exception()` 같은 패턴도 자주 쓴다.

### 단언 연산자 (!!)

```kotlin
val length: Int = nullableName!!.length
// null이면 NullPointerException 발생 (주의!)
```

**위험한 연산자:** "나는 이게 null이 아니라는 걸 확신해!"라고 컴파일러에게 말하는 것이다. 틀리면 예외가 터진다.

**언제 쓸까?** 거의 안 쓰는 게 좋다. 정말 확신할 때만 쓰고, 가능하면 `?.`나 `?:`를 쓰자.

**코드 리뷰에서:** `!!`가 많으면 코드 리뷰에서 지적받는다. Kotlin의 null 안전성을 포기하는 것이기 때문이다.

### 안전 캐스트 (as?)

```kotlin
val str: String? = obj as? String
// 캐스트 실패 시 null 반환
```

**일반 캐스트 (`as`)와의 차이:** `as`는 실패하면 `ClassCastException`을 던지지만, `as?`는 null을 반환한다.

**패턴:** `when`과 함께 쓰면 타입별로 다른 처리를 할 수 있다.

### let 함수

```kotlin
nullableName?.let {
    // nullableName이 null이 아닐 때만 실행
    println("Name is $it")
}
```

**용도:** null이 아닐 때만 특정 코드를 실행하고 싶을 때 쓴다. if문보다 간결하다.

**스코프:** `let` 블록 안에서 `it`으로 값에 접근할 수 있다. 이름을 바꾸고 싶으면 `?.let { name -> ... }` 이렇게 쓴다.

---

## 컬렉션

### List

```kotlin
// 불변 리스트
val readOnlyList = listOf(1, 2, 3, 4, 5)

// 가변 리스트
val mutableList = mutableListOf(1, 2, 3)
mutableList.add(4)
mutableList.remove(1)

// 접근
val first = readOnlyList[0]
val last = readOnlyList.last()
```

### Set

```kotlin
val readOnlySet = setOf(1, 2, 3, 3)  // 중복 제거
val mutableSet = mutableSetOf(1, 2, 3)
mutableSet.add(4)
```

### Map

```kotlin
val readOnlyMap = mapOf(
    "key1" to "value1",
    "key2" to "value2"
)

val mutableMap = mutableMapOf<String, Int>()
mutableMap["one"] = 1
mutableMap["two"] = 2

// 접근
val value = readOnlyMap["key1"]
val valueOrDefault = readOnlyMap.getOrDefault("key3", "default")

// 순회
for ((key, value) in readOnlyMap) {
    println("$key -> $value")
}
```

### 컬렉션 연산

```kotlin
val numbers = listOf(1, 2, 3, 4, 5)

// filter
val evens = numbers.filter { it % 2 == 0 }  // [2, 4]

// map
val doubled = numbers.map { it * 2 }  // [2, 4, 6, 8, 10]

// reduce
val sum = numbers.reduce { acc, n -> acc + n }  // 15

// fold
val sumWithInitial = numbers.fold(10) { acc, n -> acc + n }  // 25

// any, all, none
numbers.any { it > 3 }   // true
numbers.all { it > 0 }   // true
numbers.none { it < 0 }  // true

// find, first, last
numbers.find { it > 3 }   // 4
numbers.first { it > 3 }  // 4
numbers.last { it < 4 }   // 3

// groupBy
val grouped = numbers.groupBy { it % 2 }
// {1=[1, 3, 5], 0=[2, 4]}

// partition
val (even, odd) = numbers.partition { it % 2 == 0 }
// even=[2, 4], odd=[1, 3, 5]

// flatMap
val nested = listOf(listOf(1, 2), listOf(3, 4))
val flattened = nested.flatMap { it }  // [1, 2, 3, 4]

// distinct
val duplicates = listOf(1, 2, 2, 3, 3, 3)
val unique = duplicates.distinct()  // [1, 2, 3]

// sorted
val sorted = listOf(3, 1, 4, 1, 5).sorted()  // [1, 1, 3, 4, 5]
val sortedDesc = listOf(3, 1, 4).sortedDescending()  // [4, 3, 1]

// take, drop
numbers.take(3)  // [1, 2, 3]
numbers.drop(3)  // [4, 5]

// zip
val letters = listOf("a", "b", "c")
val zipped = numbers.zip(letters)  // [(1, a), (2, b), (3, c)]
```

### Sequence (지연 평가)

```kotlin
val sequence = sequenceOf(1, 2, 3, 4, 5)
    .filter { 
        println("Filter $it")
        it % 2 == 0 
    }
    .map { 
        println("Map $it")
        it * 2 
    }

// 여기까지는 실행 안 됨 (지연 평가)
val result = sequence.toList()  // 이제 실행됨
```

---

## 람다와 고차 함수

Kotlin은 함수형 프로그래밍을 강력하게 지원한다. 람다와 고차 함수는 그 핵심이다.

### 람다 표현식

```kotlin
// 기본 형태
val sum: (Int, Int) -> Int = { a, b -> a + b }

// 타입 추론
val multiply = { a: Int, b: Int -> a * b }

// 단일 매개변수 (it 사용)
val double: (Int) -> Int = { it * 2 }

// 여러 줄
val complexLambda = { x: Int ->
    val squared = x * x
    val doubled = x * 2
    squared + doubled  // 마지막 표현식이 반환값
}
```

**람다 문법:** `{ 매개변수 -> 본문 }` 형태다. Java의 람다보다 간결하다.

**`it` 키워드:** 매개변수가 하나일 때 이름을 생략하고 `it`으로 쓸 수 있다. `list.filter { it > 5 }` 이런 식으로.

**마지막 표현식이 반환값:** `return` 키워드 없이 마지막 줄이 자동으로 반환된다. 함수형 스타일이다.

### 고차 함수

```kotlin
// 함수를 매개변수로 받는 함수
fun operate(a: Int, b: Int, operation: (Int, Int) -> Int): Int {
    return operation(a, b)
}

val result = operate(5, 3, { a, b -> a + b })

// 후행 람다: 마지막 매개변수가 람다면 괄호 밖으로
val result2 = operate(5, 3) { a, b -> a * b }

// 함수를 반환하는 함수
fun makeMultiplier(factor: Int): (Int) -> Int {
    return { number -> number * factor }
}

val triple = makeMultiplier(3)
triple(5)  // 15
```

**고차 함수란?** 함수를 매개변수로 받거나 함수를 반환하는 함수다. 함수를 값처럼 다룬다.

**후행 람다 (trailing lambda):** Kotlin의 문법 설탕이다. 마지막 인자가 람다면 괄호 밖으로 빼낼 수 있다. `list.filter { it > 5 }`가 가능한 이유다.

**클로저 (closure):** `makeMultiplier`처럼 함수가 외부 변수(`factor`)를 캡처할 수 있다. 강력한 기능이다.

### 익명 함수

```kotlin
val sum = fun(a: Int, b: Int): Int {
    return a + b
}

// 표현식 본문
val multiply = fun(a: Int, b: Int) = a * b
```

**람다와의 차이:** 익명 함수는 `return`이 함수 자체를 종료하지만, 람다의 `return`은 바깥 함수를 종료한다. 대부분은 람다를 쓴다.

---

## 확장 함수

### 기본 확장 함수

```kotlin
fun String.removeSpaces(): String {
    return this.replace(" ", "")
}

"Hello World".removeSpaces()  // "HelloWorld"

// 확장 프로퍼티
val String.firstChar: Char
    get() = this[0]

"Kotlin".firstChar  // 'K'
```

### Nullable 수신자

```kotlin
fun String?.isNullOrEmpty(): Boolean {
    return this == null || this.isEmpty()
}

val str: String? = null
str.isNullOrEmpty()  // true
```

---

## 데이터 클래스

```kotlin
data class User(
    val name: String,
    val age: Int,
    val email: String
)

val user1 = User("Alice", 25, "alice@example.com")
val user2 = User("Alice", 25, "alice@example.com")

// 자동 생성되는 메서드들
println(user1 == user2)  // true (equals)
println(user1)           // User(name=Alice, age=25, email=alice@example.com) (toString)

// copy: 일부 프로퍼티만 변경
val user3 = user1.copy(age = 26)

// 구조 분해
val (name, age, email) = user1
println("$name is $age years old")
```

---

## Sealed 클래스

```kotlin
sealed class Result {
    data class Success(val data: String) : Result()
    data class Error(val message: String) : Result()
    object Loading : Result()
}

fun handleResult(result: Result) {
    when (result) {
        is Result.Success -> println("Data: ${result.data}")
        is Result.Error -> println("Error: ${result.message}")
        Result.Loading -> println("Loading...")
        // else 불필요 (모든 경우를 다룸)
    }
}
```

---

## Object와 Companion Object

### Object (싱글톤)

```kotlin
object DatabaseManager {
    fun connect() {
        println("Connected to database")
    }
}

DatabaseManager.connect()
```

### Companion Object

```kotlin
class MyClass {
    companion object {
        const val CONSTANT = "constant value"
        
        fun create(): MyClass {
            return MyClass()
        }
    }
}

MyClass.CONSTANT
MyClass.create()

// 이름 지정
class MyClass2 {
    companion object Factory {
        fun create() = MyClass2()
    }
}

MyClass2.Factory.create()
MyClass2.create()  // 이것도 가능
```

### Object 표현식 (익명 객체)

```kotlin
val clickListener = object : ClickListener {
    override fun onClick() {
        println("Clicked!")
    }
}
```

---

## 인터페이스

```kotlin
interface Clickable {
    fun click()  // 추상 메서드
    
    fun showOff() = println("I'm clickable!")  // 기본 구현
}

interface Focusable {
    fun focus()
    fun showOff() = println("I'm focusable!")
}

class Button : Clickable, Focusable {
    override fun click() = println("Button clicked")
    override fun focus() = println("Button focused")
    
    // 충돌 해결
    override fun showOff() {
        super<Clickable>.showOff()
        super<Focusable>.showOff()
    }
}
```

---

## 제네릭

### 제네릭 클래스

```kotlin
class Box<T>(val item: T) {
    fun get(): T = item
}

val intBox = Box(123)
val stringBox = Box("Hello")
```

### 제네릭 함수

```kotlin
fun <T> singletonList(item: T): List<T> {
    return listOf(item)
}

val list = singletonList(42)
val stringList = singletonList("Hello")
```

### 제약 조건

```kotlin
// 상한 제약
fun <T : Comparable<T>> max(a: T, b: T): T {
    return if (a > b) a else b
}

// 여러 제약
fun <T> copyWhenGreater(list: List<T>, threshold: T): List<T>
    where T : Comparable<T>, T : Number {
    return list.filter { it > threshold }
}
```

### 변성 (Variance)

```kotlin
// 공변성 (out): 생산자
interface Producer<out T> {
    fun produce(): T
}

// 반공변성 (in): 소비자
interface Consumer<in T> {
    fun consume(item: T)
}

// 사용처 변성
fun copy(from: Array<out Any>, to: Array<in Any>) {
    for (i in from.indices) {
        to[i] = from[i]
    }
}
```

### 스타 프로젝션

```kotlin
fun printList(list: List<*>) {
    for (item in list) {
        println(item)
    }
}
```

---

## 코루틴

Kotlin의 비동기 프로그래밍 솔루션이다. 콜백 지옥 없이 동기 코드처럼 비동기 코드를 작성할 수 있다.

### 기본 코루틴

```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    launch {
        delay(1000L)
        println("World!")
    }
    println("Hello")
}
```

**`launch`:** 새로운 코루틴을 시작한다. "fire and forget" 스타일이다.

**`delay`:** 스레드를 블로킹하지 않고 일시 중단한다. `Thread.sleep()`과 다르다.

**`runBlocking`:** 메인 함수를 코루틴으로 만든다. 실전에서는 잘 안 쓰고 테스트에서 주로 쓴다.

### async/await

```kotlin
suspend fun fetchUser(): User {
    delay(1000)
    return User("Alice", 25)
}

suspend fun fetchPosts(): List<Post> {
    delay(1000)
    return listOf(Post("Post 1"), Post("Post 2"))
}

fun main() = runBlocking {
    val user = async { fetchUser() }
    val posts = async { fetchPosts() }
    
    println("User: ${user.await()}")
    println("Posts: ${posts.await()}")
}
```

**`async`:** 결과를 반환하는 코루틴을 시작한다. JavaScript의 Promise와 비슷하다.

**`await()`:** 결과를 기다린다. 하지만 스레드는 블로킹하지 않는다.

**병렬 실행:** 위 코드에서 `fetchUser()`와 `fetchPosts()`는 동시에 실행된다. 총 1초만 걸린다.

### 코루틴 스코프

```kotlin
class MyViewModel : ViewModel() {
    private val viewModelScope = CoroutineScope(Dispatchers.Main)
    
    fun loadData() {
        viewModelScope.launch {
            val data = withContext(Dispatchers.IO) {
                // 백그라운드 작업
                fetchDataFromNetwork()
            }
            // UI 업데이트 (Main 스레드)
            updateUI(data)
        }
    }
}
```

**Dispatcher:** 코루틴이 어느 스레드에서 실행될지 결정한다.
- `Dispatchers.Main` - UI 스레드 (Android)
- `Dispatchers.IO` - 네트워크, 파일 I/O
- `Dispatchers.Default` - CPU 집약적 작업

**`withContext`:** 다른 Dispatcher로 전환한다. 스레드를 바꾸는 것과 비슷하지만 훨씬 가볍다.

### Flow

```kotlin
fun simpleFlow(): Flow<Int> = flow {
    for (i in 1..3) {
        delay(100)
        emit(i)
    }
}

fun main() = runBlocking {
    simpleFlow().collect { value ->
        println(value)
    }
}

// Flow 연산자
flow.map { it * 2 }
    .filter { it > 5 }
    .collect { println(it) }
```

**Flow란?** 비동기 데이터 스트림이다. RxJava의 Observable, JavaScript의 Observable과 비슷하다.

**Cold Stream:** Flow는 `collect`를 호출할 때까지 실행되지 않는다. 여러 번 collect하면 여러 번 실행된다.

**언제 쓸까?** 실시간 데이터, 검색 자동완성, 센서 데이터 등 연속적인 값을 다룰 때 쓴다.

---

## 스코프 함수

스코프 함수는 객체의 컨텍스트 내에서 코드 블록을 실행하는 함수다. 5가지가 있고, 각각 미묘하게 다르다.

**핵심 차이점:**
- **수신 객체 참조:** `this` vs `it`
- **반환 값:** 람다 결과 vs 수신 객체

### let

```kotlin
val result = "Hello".let {
    println(it)
    it.length
}  // 5

// null 체크와 함께
nullableString?.let {
    println("String is not null: $it")
}
```

**특징:**
- 수신 객체를 `it`으로 참조
- 람다의 마지막 표현식을 반환
- null 체크와 함께 쓰기 좋음

**언제 쓸까?** null이 아닐 때만 실행하고 싶을 때, 결과를 변환하고 싶을 때.

### run

```kotlin
val result = "Hello".run {
    println(this)
    length
}  // 5

// 객체 초기화
val person = Person().run {
    name = "Alice"
    age = 25
    this
}
```

**특징:**
- 수신 객체를 `this`로 참조 (생략 가능)
- 람다의 마지막 표현식을 반환
- `let`과 비슷하지만 `this`를 쓴다

**언제 쓸까?** 객체의 메서드를 여러 번 호출하면서 결과를 반환하고 싶을 때.

### with

```kotlin
val result = with("Hello") {
    println(this)
    length
}  // 5
```

**특징:**
- 확장 함수가 아님 (일반 함수)
- 수신 객체를 `this`로 참조
- 람다의 마지막 표현식을 반환

**언제 쓸까?** "이 객체로 이것저것 해라"라는 느낌. `run`과 비슷하지만 null 체크가 안 된다.

### apply

```kotlin
val person = Person().apply {
    name = "Alice"
    age = 25
}  // Person 객체 반환
```

**특징:**
- 수신 객체를 `this`로 참조
- **수신 객체 자체를 반환** (중요!)
- 객체 설정에 최적화

**언제 쓸까?** 객체를 생성하고 초기화할 때. Builder 패턴처럼 쓸 수 있다.

**재미있는 점:** Android에서 View 설정할 때 엄청 많이 쓴다. `TextView().apply { text = "Hello"; textSize = 16f }`

### also

```kotlin
val numbers = mutableListOf(1, 2, 3)
    .also { println("Before: $it") }
    .add(4)
```

**특징:**
- 수신 객체를 `it`으로 참조
- **수신 객체 자체를 반환**
- 부수 효과(side effect)를 위한 함수

**언제 쓸까?** 로깅, 디버깅, 유효성 검사 등 "이 객체로 뭔가 하되, 객체는 그대로 반환"할 때.

**정리표:**

| 함수 | 수신 객체 | 반환 값 | 주 용도 |
|------|----------|---------|---------|
| `let` | `it` | 람다 결과 | null 체크, 변환 |
| `run` | `this` | 람다 결과 | 객체 설정 + 결과 계산 |
| `with` | `this` | 람다 결과 | 여러 메서드 호출 |
| `apply` | `this` | 수신 객체 | 객체 초기화 |
| `also` | `it` | 수신 객체 | 부수 효과 (로깅 등) |

---

## 연산자 오버로딩

```kotlin
data class Point(val x: Int, val y: Int) {
    operator fun plus(other: Point) = Point(x + other.x, y + other.y)
    operator fun times(scale: Int) = Point(x * scale, y * scale)
    operator fun unaryMinus() = Point(-x, -y)
    operator fun get(index: Int) = when(index) {
        0 -> x
        1 -> y
        else -> throw IndexOutOfBoundsException()
    }
}

val p1 = Point(10, 20)
val p2 = Point(30, 40)

val sum = p1 + p2          // Point(40, 60)
val scaled = p1 * 3        // Point(30, 60)
val negated = -p1          // Point(-10, -20)
val x = p1[0]              // 10
```

---

## 위임

위임(delegation)은 상속 대신 사용할 수 있는 강력한 패턴이다. "내가 직접 하지 않고 다른 객체에게 시킨다"는 개념이다.

### 클래스 위임

```kotlin
interface Base {
    fun print()
}

class BaseImpl(val x: Int) : Base {
    override fun print() = println(x)
}

class Derived(b: Base) : Base by b

val base = BaseImpl(10)
val derived = Derived(base)
derived.print()  // 10
```

**`by` 키워드:** "이 인터페이스의 구현을 저 객체에게 위임한다"는 뜻이다.

**왜 유용할까?** 상속 없이 기능을 재사용할 수 있다. "상속보다 조합(composition over inheritance)" 원칙을 쉽게 따를 수 있다.

**실제로는?** 컴파일러가 자동으로 모든 메서드를 위임 객체로 전달하는 코드를 생성한다.

### 프로퍼티 위임

```kotlin
// lazy
val lazyValue: String by lazy {
    println("Computed!")
    "Hello"
}

// observable
var name: String by Delegates.observable("Initial") { prop, old, new ->
    println("$old -> $new")
}

// vetoable
var age: Int by Delegates.vetoable(0) { prop, old, new ->
    new >= 0  // 음수 거부
}

// 커스텀 위임
class Delegate {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): String {
        return "$thisRef, thank you for delegating '${property.name}' to me!"
    }
    
    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: String) {
        println("$value has been assigned to '${property.name}' in $thisRef.")
    }
}

class Example {
    var p: String by Delegate()
}
```

**프로퍼티 위임이란?** 프로퍼티의 get/set을 다른 객체에게 맡기는 것이다.

**표준 위임들:**
- `lazy` - 지연 초기화 (앞에서 봤음)
- `observable` - 값이 바뀔 때마다 알림
- `vetoable` - 값 변경을 거부할 수 있음
- `map` - Map에서 프로퍼티 값을 가져옴

**언제 쓸까?** 반복되는 get/set 로직을 재사용하고 싶을 때. Android의 ViewModel에서 LiveData 위임이 대표적이다.

---

## 인라인 함수

고차 함수를 쓸 때 람다가 객체로 생성되어 오버헤드가 있다. `inline`은 이를 해결한다.

```kotlin
inline fun <T> measureTime(block: () -> T): T {
    val start = System.currentTimeMillis()
    val result = block()
    val end = System.currentTimeMillis()
    println("Time: ${end - start}ms")
    return result
}

// noinline: 특정 람다를 인라인하지 않음
inline fun foo(inlined: () -> Unit, noinline notInlined: () -> Unit) {
    // ...
}

// crossinline: non-local return 방지
inline fun runInThread(crossinline block: () -> Unit) {
    thread {
        block()  // return 불가
    }
}
```

**`inline`의 동작:** 함수 호출을 함수 본문으로 대체한다. 람다도 호출 지점에 직접 삽입된다.

**장점:**
- 람다 객체 생성 오버헤드 제거
- non-local return 가능 (람다에서 바깥 함수를 return)

**단점:**
- 코드 크기 증가 (함수가 여러 곳에 복사됨)
- 큰 함수는 인라인하면 안 됨

**언제 쓸까?** 고차 함수, 특히 컬렉션 연산 같은 작은 함수에 쓴다. Kotlin 표준 라이브러리의 `map`, `filter` 등이 모두 inline이다.

**`noinline`:** 인라인 함수 안에서 특정 람다만 인라인하지 않고 싶을 때.

**`crossinline`:** 람다가 다른 컨텍스트(다른 스레드 등)에서 실행될 때, non-local return을 막기 위해 쓴다.

---

## Reified 타입 파라미터

제네릭의 타입 정보는 런타임에 지워진다(type erasure). `reified`는 이를 우회한다.

```kotlin
inline fun <reified T> isA(value: Any): Boolean {
    return value is T
}

isA<String>("Hello")  // true
isA<Int>("Hello")     // false

// 실용적인 예
inline fun <reified T> Gson.fromJson(json: String): T {
    return fromJson(json, T::class.java)
}

val user: User = gson.fromJson(jsonString)
```

**일반 제네릭의 문제:** `fun <T> isA(value: Any) = value is T` 이건 컴파일 에러다. 런타임에 `T`가 뭔지 모르기 때문이다.

**`reified`의 마법:** `inline` + `reified`를 쓰면 타입 정보가 유지된다. 런타임에 `T`가 뭔지 알 수 있다.

**조건:** 반드시 `inline` 함수여야 한다. 인라인되면서 타입 정보가 호출 지점에 직접 삽입되기 때문이다.

**실전 활용:**
- `is T` 타입 체크
- `T::class` 클래스 참조
- JSON 파싱 (`gson.fromJson<User>(json)`)
- Android의 `startActivity<MainActivity>()`

**재미있는 점:** Java에서는 불가능한 기능이다. Kotlin만의 특권이다!

---

이 문서는 Kotlin의 주요 문법 요소들을 다룹니다. 더 자세한 내용은 [Kotlin 공식 문서](https://kotlinlang.org/docs/home.html)를 참고하세요.
