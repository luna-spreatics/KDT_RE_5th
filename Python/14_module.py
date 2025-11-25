# 모듈 (module)
# - 여러 기능(함수)의 묶음
# - 하나의 py파일로 여러 기능을 모아놓은 것


# 모듈 불러오기(1)
# import hello
# 모듈 불러오기(2)
import math as m
import calc as c
from hello import greeting
# 모듈 불러오기(3)
from hello import *
# 모듈 불러오기(4)
import hello as h

# hello.greeting("lee")
greeting("kim")
introduce("sin", 20)
h.greeting("kim")


# 실습1. 계산기 모듈 만들어보기

print(c.add(3, 5))
print(c.subtract(10, 3))
print(c.multiply(2, 10))
print(c.divide(2, 0))
print(c.divide(20, 3))


# 패키지
# 모듈의 묶음
# 모듈을 폴더 단위로 묶어놓은 것

# 패키지에서 모듈 불러오기(1)
# from my_package import calc as c
# c.add(10,20)

# 패키지에서 모듈 불러오기(2)
# from my_package.calc import add
# add(10,20)


# 파이썬 표준 라이브러리

# math 모듈 : 수학적 연산에 사용되는 모듈


# 1. 올림/내림
# ceil : 올림, 소수점 지정X
print(m.ceil(3.14))

# floor : 내림, 소수점 지정X
print(m.floor(3.14))

# round : 반올림 - 내장 함수
print(round(3.141592, 2))


# 2. 제곱, 제곱근
# pow(x, y) : 제곱 - x^y
m.pow(2, 3)

# sqrt(x) : 제곱근 반환
m.sqrt(16)

# 3. 상수
# pi : 원주율
print(m.pi)

# 4. 수학 계산 편의 기능
print(m.factorial(3))

# 최대 공약수
print(m.gcd(12, 20))
# 최소 공배수
print(m.lcm(12, 20))


# 실습2.
# 📌 문제 1. 실제 거리 계산: 좌표 두 점 사이 거리 구하기

x1, y1 = map(int, input("x1,y1을 입력해주세요.").split(","))
# x1, y1 = int(x1), int(y1)
x2, y2 = map(int, input("x2,y2을 입력해주세요.").split(","))

# 피타고라스 정리: 거리 = sqrt((x2-x1)^2 + (y2-y1)^2)
dist = round(m.sqrt(m.pow((x2-x1), 2) + m.pow((y2-y1), 2)), 2)

print(f"두 점 사이의 거리는: {dist}")


# 📌 문제 2. 상품 나누기: 최소 공배수와 최대 공약수
a = 18
b = 24

# 최대공약수
gcd = m.gcd(a, b)

# 최소공배수
lcm = m.lcm(a, b)

print(f"최대 간식 개수: {gcd}")
print(f"최소 간식 개수: {lcm}")
