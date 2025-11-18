# for문
# - 이터러블(순회 가능한) 요소를 하나씩 꺼내서 실행 블록에 전달하는 반복문

# 리스트 반복
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"I like {fruit}")
    
# 문자열 반복
my_str = "Apple"

for char in my_str:
    print(char)

# 튜플 반복
coords = [(1,2), (10,15), (-6,8)]
# 언패킹 (구조분해 가능)
for x,y in coords:
    print(f"x좌표: {x}, y좌표: {y}")
    

# 딕셔너리 반복
person = {
    "name": "kim",
    "age": 15,
    "address": "seoul"
}

# 기본
for key in person:
    print(f"key: {key}, value: {person[key]}")
    
# value 만 가져오기
for value in person.values():
    print(f"value: {value}")

# item 가져오기
for key, value in person.items():
    print(f"key: {key}, value: {value}")


# set 반복
my_set = {1,2,3,4}

for s in my_set:
    print(s)
    
# 실습 1.
# 문제 1.
numbers = [3, 6, 1, 8, 4]
doubled = []

for number in numbers:
    doubled.append(number * 2)
print(doubled)



# 문제 2.
words = ["apple", "banana", "kiwi", "grape"]
lengths = []

for word in words:
    lengths.append(len(word))

print(lengths)


# 문제 3.
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

x_values = []
y_values = []

for x,y in coordinates:
    x_values.append(x)
    y_values.append(y)

print(f"x좌표: {x_values}")
print(f"y좌표: {y_values}")




# for문과 range()
# range 함수 : 지정된 범위의 정수 시퀀스 생성

# 기본 문법
# range(start, end, step)
# - start: 생략 가능. 기본값 0
# - end: end-1 까지 생성
# - step: 생략 가능. 기본값 1

range(1,5)

for i in range(1,5):
    print(i)
    
for i in [1,2,3,4]:
    print(i)

print("==================")

# start 생략
for i in range(10):
    print(i)
    
# 간격 (step) 지정
for i in range(0,11,2):
    print(i)

for i in range(11,0,-2):
    print(i)    

'''
# 실습 2.
# 문제 1.
num = int(input("숫자를 입력하세요:"))
sum = 0

for i in range(num + 1):
    sum += i

print(sum)


# 문제 2. 
dan = int(input("생성할 단을 입력해주세요: "))

for i in range(1, 10):
    print(f"{dan} X {i} = {dan * i}")
    
    
# 문제 3.
result = 0

for i in range(3, 101, 3):
    result += i
    
for i in range(1,101):
    if i  % 3 == 0:
        result += i
    
print("3의 배수의 합:",result)



# 문제 4.
n = int(input("숫자를 입력하세요: "))

for i in range(1, n+1):
    if i % 2 == 0 and i % 5 == 0:
        print(i)
        
'''

print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
# 루프 제어문
# - 특정 조건 하에서만 작동하도록 구현

# break : 반복을 즉시 중단
for i in range(10):
    if i == 5:
        break
    
    print(i)

print("반복 종료")


# continue : 현재 반복을 넘어감
for i in range(5):
    if i == 2:
        print("continue = 건너뜀")
        continue
    
    print(i)
    
print("반복 종료")


# pass
for i in range(10):
    pass

print("===============")
# for - else 구문
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("반복종료")
    
    
# 중첩 for문
# - 하나의 for문 안에 다른 for문이 들어있는 구조


# 이중 for문
for i in range(5):
    for j in range(5):
        print("i, j", i, j)
    print()
    
    
    
# 실습 3
# 문제 1.

for i in range(2, 10):
    print(f"[ {i}단 ]")
    for j in range(1, 10):
        print(f"{i} X {j} = {i * j}")
    print()
    

# 문제 2. 별찍기
# 왼쪽 정렬
n = int(input("몇 줄?: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
    

# 오른쪽 정렬
n = int(input("몇 줄?: "))

for i in range(1, n+1):
    # 공백 출력
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
    

#  가운데 정렬
n = int(input("몇 줄?: "))

for i in range(1, n+1):
    # 공백 출력
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
