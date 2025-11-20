'''
함수 (function)
- 특정 작업을 수행하는 코드 들의 모음
- 복잡한 코드를 작은 단위로 나눌 수 있게 도와줌
- 특정한 코드들을 재사용 할 수 있게 함
'''

# 사용자 정의 함수 기본 문법
# 함수의 정의 : define의 약자로 def 사용
def 함수이름 (매개변수):
    # 실행할 코드
    print(매개변수)
    return "반환값"

# 함수의 실행(호출 call)
result = 함수이름("인자")
print(result)

# 매개 변수(Parameter): 매개 + 변수
# 매개 : 둘 사이를 연결해줌
# 함수가 실행될 때 인자로부터 입력되는 값을 함수의 코드블록으로 전달하는 역할


# 함수의 필요성 예제
a = 10
b = 20

if a > b:
    print(a - b)
else:
    print(a + b)
    
c = 30
d = 40

if c > d:
    print(c - d)
else:
    print(c + d)
    
# .....


def my_func(a,b):
    if a > b:
        return a - b
    else:
        return a + b

print(my_func(10, 20))
print(my_func(30, 40))



# 실습 1.
# 함수 이름은 calculate로 합니다.
# 매개변수는 a, b, operator 세 개입니다.
# operator는 문자열이며, 다음 중 하나입니다: "+", "-", "*", "/"
# 나눗셈은 결과를 실수(float) 로 반환합니다.
# 올바르지 않은 연산자가 들어오면 "지원하지 않는 연산입니다"라는 문자열을 반환하세요.

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return float(a / b)
    else:
        return "지원하지 않는 연산입니다"

print(calculate(20,30,"+"))
print(calculate(50,40,"-"))
print(calculate(5,4,"*"))
print(calculate(100,3,"/"))
print(calculate(1000,10000,"&"))



# 키워드 인자
# 예시 1.
print("안녕하세요", "반갑습니다!", sep="-", end= " / ")

# 예시 2.
def my_func(a, b, c=None, operator=None):
    if operator == "+":
        return a + b
    else:
        return c
    
print(my_func(10,20, operator="+"))


# 기본값 인자
# 단, 기본값 매개변수는 뒤쪽에 위치해야함
def greet(name, message="안녕하세요~!"):
    print(f"{name}님, {message}")
    
# 호출 시 인자 생략 -> 기본값 사용
greet("luna")
greet("ff", "반갑습니다!")


# 위치 가변 인자
# 여러개의 값을 유동적으로 받을 수 있음
# 값이 튜플 형태로 받아짐

def add_all(*args):
    return sum(args)

print(add_all(1,2,3,4,5))


# 키워드 가변 인자
# 여러 키워드 인자를 유동적으로 받을 수 있다
# 딕셔너리 형태로 값이 입력됨

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
print_info(name="luna", age=15, city="seoul")



# 실습 2. 가변인자 연습하기
# 문제 1. 숫자 여러 개의 평균 구하기
def average(*agrs):
  # 예외처리
  if len(agrs) == 0:
    return "입력값이 없습니다"
  return sum(agrs) / len(agrs)

print(average(1,2,3))


# 문제 2. 가장 긴 문자열 찾기
# 방법 1.
def longgest(*args):
  answer = ""
  for s in args:
    if len(s) > len(answer):
      answer = s
  return answer

print(longgest("apple","watermelon","grape","kiwi"))


# 방법 2.
def longgest2(*args):
    # 예외처리
  if len(args) == 0:
    return "입력값이 없습니다"
  return max(args, key=len)

longgest2()


# 문제 3. 사용자 정보 출력 함수
# dict.items() 활용
def print_info(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_info(name="k", age=15, city="서울", job="developer")


# 문제 4. 할인 계산기
# dict.items() 활용
def discount_price(**kwargs):
  for key, value in kwargs.items():
    discounted = value * 0.9
    print(f"{key}: 할인가 {discounted} (원가 {value})")
    
discount_price(apple=2000, watermelon=20000, chocolate=2500)




# 전역 변수 : 함수 밖에 선언된 변수
# 지역 변수 : 함수 안에 선언된 변수

# 전역변수
x = 200

# 예제
def my_func():
    # 지역변수
    x = 10
    print(x)

my_func()
print("함수 밖", x)


# 예제 2 (UnboundLocalError 에러)
x = 10

def my_func2():
    # x = 20
    # x += 5
    print("지역변수", x)

my_func2()

print("전역변수", x)


# 예제 3 (global 사용 예제)
x = 10

def my_func3():
    global x # 전역변수 사용 선언
    x += 5
    print("지역", x)

my_func3()

print("전역", x)


# 권장되는 패턴
# 부수효과(side effect)를 발생시키지 않는 함수를 위주로 프로그래밍

x = 10

def my_func4(x):
    x += 5
    return x

x = my_func4(x)

print("전역", x)
