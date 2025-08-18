# Python 기초 개념 정리

## 기본 개념

### 변수 (Variable)
- **정의**: 값을 저장하는 장소
- **메모리**: 변수에 할당되는 값은 변수에 할당된 메모리 주소에 저장됨

```python
# 예시
name = "Python"  # name 변수에 "Python" 문자열 저장
age = 25         # age 변수에 25 정수 저장
```

---

## 폰 노이만 아키텍처

**Von Neumann Architecture**는 현대 컴퓨터의 기본 구조입니다.

### 동작 원리
1. 사용자가 컴퓨터에 값을 입력하거나 프로그램을 실행
2. 해당 정보를 **메모리에 저장**
3. **CPU**가 메모리의 정보를 해석하고 계산
4. 계산된 결과값을 사용자에게 전달

```
[입력] → [메모리] → [CPU 처리] → [출력]
```

---

## Python의 특징

### Dynamic Typing (동적 타이핑)
- 코드 **실행 시점**에 데이터 타입이 결정됨
- 변수 선언 시 타입을 명시하지 않아도 됨

```python
x = 10        # 정수형으로 자동 결정
x = "Hello"   # 문자열로 타입 변경 가능
x = 3.14      # 실수형으로 타입 변경 가능
```

### 문자열 연산
- 문자열 간의 **연결(concatenation)** 가능

```python
first_name = "김"
last_name = "철수"
full_name = first_name + last_name  # "김철수"
```

### 타입 변환
- `float()`, `int()` 함수를 이용한 데이터 타입 변환 가능

```python
str_num = "123"
int_num = int(str_num)    # 문자열 → 정수: 123
float_num = float(str_num) # 문자열 → 실수: 123.0
```

---

## 연산과 할당

### 할당 연산자 (`=`)
- **좌변**: 값이 저장되는 공간(변수)
- **우변**: 해당 공간에 저장되는 값

```python
result = 10 + 20  # result 변수에 30이 저장됨
```

### Python의 연산자 특징
- C언어의 `++`, `--` 연산자가 **존재하지 않음**
- 대신 `+=`, `-=` 사용

```python
# C언어 스타일 (Python에서 사용 불가)
# count++  # 오류!

# Python 스타일
count = 0
count += 1  # count = count + 1과 동일
```

---

## 부동소수점과 반올림 오차

### 반올림 오차의 원인
컴퓨터는 숫자를 **이진수**로 저장하며, 이 과정에서 간단한 실수가 무한소수가 될 수 있습니다.

```python
# 예시: 부동소수점 연산의 오차
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 (예상: 0.3)
```

### 해결 방법
```python
import decimal

# Decimal 모듈 사용
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
result = a + b  # 정확한 0.3

# 또는 round() 함수 사용
result = round(0.1 + 0.2, 1)  # 0.3
```

---

## 이진수 시스템

### 컴퓨터의 이진수 처리
- 컴퓨터는 **반도체**로 구성
- 전류가 흐를 때: **1**
- 전류가 흐르지 않을 때: **0**

```python
# Python에서 이진수 표현
binary_num = 0b1010  # 이진수 1010 (십진수 10)
print(bin(10))       # 0b1010
```

---

## 리스트(List)

### 기본 개념
- **여러 데이터들의 집합**
- **인덱스(주소값)**를 통해 리스트 요소에 접근 가능
- 인덱스는 **0부터 시작**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # "apple" (첫 번째 요소)
print(fruits[1])  # "banana" (두 번째 요소)
```

### 슬라이싱 (Slicing)
- `[from:to]` 형태로 범위 지정
- 범위를 넘어갈 경우 **자동 조정** 기능

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])   # [2, 3, 4]
print(numbers[:3])    # [1, 2, 3] (처음부터 인덱스 2까지)
print(numbers[2:])    # [3, 4, 5] (인덱스 2부터 끝까지)
print(numbers[:])     # [1, 2, 3, 4, 5] (전체 복사)
```

### 리스트 연산
- 리스트끼리 **더할 수 있음** (concatenation)

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]
```

### 메모리 할당
- `=`은 메모리 주소에 해당 객체를 할당한다는 의미
- 리스트 복사 시 주의사항

```python
original = [1, 2, 3]
reference = original      # 같은 메모리 주소 참조
copy_list = original[:]   # 새로운 리스트 생성 (얕은 복사)

reference[0] = 99
print(original)   # [99, 2, 3] (원본도 변경됨)
print(copy_list)  # [1, 2, 3] (복사본은 변경 안됨)
```

### 2차원 리스트
- **리스트 안에 리스트**를 넣어 행렬 구현 가능

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])  # 2 (첫 번째 행, 두 번째 열)
```

### 다양한 데이터 타입
- **다양한 데이터 타입**이 하나의 리스트에 들어갈 수 있음

```python
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
```

---

## 패킹과 언패킹

### 패킹 (Packing)
- **한 번에 여러 개의 데이터**를 하나의 변수에 넣는 것

```python
numbers = 1, 2, 3, 4  # 튜플 패킹
coordinates = (10, 20)  # 좌표를 튜플로 패킹
```

### 언패킹 (Unpacking)
- **하나의 데이터 집합**을 각각의 변수로 분해하는 것

```python
# 기본 언패킹
point = (10, 20)
x, y = point  # x = 10, y = 20

# 리스트 언패킹
numbers = [1, 2, 3]
a, b, c = numbers  # a = 1, b = 2, c = 3

# 확장 언패킹 (*args)
first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5
```

---

## 📝 참고사항

이 문서는 Python 프로그래밍의 기초 개념들을 정리한 내용입니다. 
각 개념에 대한 더 자세한 정보는 [Python 공식 문서](https://docs.python.org/3/)를 참고하세요.

---

**작성일**: 2025년 8월  
**언어**: Python 3.x# Python 기초 개념 정리
