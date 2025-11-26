# 모듈 (module)
# - 여러 기능(함수)의 묶음
# - 하나의 py파일로 여러 기능을 모아놓은 것


# 모듈 불러오기(1)
# import hello
# 모듈 불러오기(2)
import os
import sys
import time
import calendar
import datetime
import random
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

# x1, y1 = map(int, input("x1,y1을 입력해주세요.").split(","))
# # x1, y1 = int(x1), int(y1)
# x2, y2 = map(int, input("x2,y2을 입력해주세요.").split(","))

# # 피타고라스 정리: 거리 = sqrt((x2-x1)^2 + (y2-y1)^2)
# dist = round(m.sqrt(m.pow((x2-x1), 2) + m.pow((y2-y1), 2)), 2)

# print(f"두 점 사이의 거리는: {dist}")


# 📌 문제 2. 상품 나누기: 최소 공배수와 최대 공약수
a = 18
b = 24

# 최대공약수
gcd = m.gcd(a, b)

# 최소공배수
lcm = m.lcm(a, b)

print(f"최대 간식 개수: {gcd}")
print(f"최소 간식 개수: {lcm}")


print(">>>>>>>>>>>>>> random >>>>>>>>>>>>>>>>>>>>>>")
# random 모듈 : 랜덤 값(난수) 생성 시 사용


# 1. 난수 생성

# random() : 0이상 1미만의 float 난수 반환
print(random.random())

# uniform(a,b) : a이상 b이하의 실수 난수 반환
print(random.uniform(1, 10))

# randint(a,b) : a이상 b이하의 정수 난수 반환
print(random.randint(1, 100))

# randrange(start, stop, step) : 범위 안의 정수 난수 반환, 간격 지정 가능
print(random.randrange(0, 100, 5))


# 2. 랜덤 선택
fruits = ["apple", "banana", "watermelon", "grape", "orange"]

# choice(seq) : 시퀀스에서 임의의 요소 1개 반환
print(random.choice(fruits))

# choices(seq, k) : 시퀀스에서 "중복 허용" k개 요소 리스트를 반환
print(random.choices(fruits, k=2))

# 섞기
# sample(seq, k) : 시퀀스에서 "중복 없이" k개 요소 리스트를 반환
print(random.sample(fruits, k=2))

# shuffle(seq) : 시퀀스의 요소를 무작위로 섞음 -> 원본 시퀀스를 변경
numbers = [1, 2, 3, 4, 5]
print(random.shuffle(numbers))
print(numbers)


# 실습3. 로또 번호 뽑기
# 1 ~ 45사이의 정수중에서 랜덤으로 6개의 숫자를 뽑는다
# 6개의 숫자는 중복이 있어서는 x
# 오름차순으로 결과를 정렬한다!

# 1)
result = sorted(random.sample(range(1, 46), k=6))
print(result)

# 2)
lotto = []
while len(lotto) < 6:
    number = random.randint(1, 45)
    if number in lotto:
        continue

    lotto.append(number)

lotto.sort()
print(lotto)


# 실습4. 가위 바위 보 게임 만들기
# RPS = ["가위", "바위", "보"]
# win_count = 0

# while win_count < 3:
#     com_choice = random.choice(RPS)
#     user_choice = input("가위, 바위, 보 중에 골라주세요!✌️✊🤚: ")

#     print(f"유저의 선택: {user_choice}")
#     print(f"컴퓨터의 선택: {com_choice}")

#     if user_choice == com_choice:
#         print("비겼습니다")
#     elif ((user_choice == "가위" and com_choice == "보") or
#           (user_choice == "바위" and com_choice == "가위") or
#           (user_choice == "보" and com_choice == "바위")):
#         print("이겼습니다")
#         win_count += 1
#     elif user_choice in RPS:
#         print("졌습니다")
#     else:
#         print("잘못된 입력이에요")


# datetime 모듈
# 날짜와 시간의 생성, 조작, 현실 변환과 같은 시간 관련 기능을 제공

# 1. 날짜/시간 구하기
# 현재 날짜와 시간 구하기
now = datetime.datetime.now()
print(now)

# 오늘 날짜만 구하기
today = datetime.date.today()
print(today)


# 2. 날짜/시간 형식 변환
formatted = now.strftime("%Y/%m/%d %H:%M:%S")
print(formatted)

parsed = datetime.datetime.strptime(formatted, "%Y/%m/%d %H:%M:%S")
print(parsed)


# 3. 날짜/시간 연산
dt = datetime.date(2025, 7, 7)
passed_time = today - dt
print(f"{passed_time.days}일이 지났습니다")

# 4. 요일반환 : weekday
# 0: 월요일 ~ 7: 일요일
days = ["월", "화", "수", "목", "금", "토", "일"]
day_num = today.weekday()
print(days[day_num])


# datetime 또는 date 객체에는 년/월/일 시간 등이 속성으로 들어있음
print(datetime.datetime.now().year)


# 실습 5.
# 사용자로부터 생일을 입력받음
# birth_month, birth_day = map(int, input("생일을 입력하세요.(예 03-14):").split("-"))

# # 오늘 날짜 구하기
# today = datetime.date.today()

# # 올해 생일을 date 객체로 변환
# birthday_this_year = datetime.date(today.year, birth_month, birth_day)

# # 오늘 날짜와 올해 생일을 비교
# if today > birthday_this_year:
#     # 올해 생일이 지났으면 내년으로 설정
#     birthday_next = datetime.date(today.year + 1, birth_month, birth_day)
# else:
#     # 올해로 설정
#     birthday_next = birthday_this_year

# # 남은 일수 계산
# days_left = (birthday_next - today).days

# print(f"다음 생일까지 {days_left}일이 남았어요!")


# calender 모듈
# 날짜와 달력 관련 기능을 제공


# 1. 달력 조회
print(calendar.prmonth(2025, 9))
print(calendar.prcal(2025))

# 텍스트로 값을 반환
print(calendar.month(2025, 11))

# 요일 반환
print(calendar.weekday(2025, 11, 26))


# time 모듈
# 시간의 측정, 지연, 변환과 같은 시간 관련 기능 제공


# 1. 시간 반환
# time()
# Unix 타임스탬프로 반환 (1970.1.1부터 경과 초)
print(time.time())

# ctime() : 현재 시간을 문자열로 반환
print(time.ctime())
print(time.ctime(0))  # 기준시로 반환 (1970.1.1)


# strftime() : 원하는 포맷의 문자열로 시간 객체 변환
lt = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
print(formatted)

# strptime() : 문자열을 struct_time 객체로 변환
parsed = time.strptime(formatted, "%Y-%m-%d %H:%M:%S")
print(parsed)

# 2. 시간 지연
# sleep(seconds) : 지정한 초만큼 프로그램이 일시 정지
# time.sleep(1)
# print("time sleep")


# # 시간 측정하기
# start = time.time()

# for i in range(5):
#     print(i)
#     time.sleep(1)

# end = time.time()
# print(f"수행시간 : {end - start: .2f}초")


# 실습 6. 타자연습게임
'''
words = [
    "apple", "banana", "orange", "grape", "lemon",
    "peach", "melon", "cherry", "plum", "pear",
    "school", "friend", "family", "flower", "garden",
    "window", "bottle", "pencil", "summer", "winter",
    "happy", "future", "travel", "animal", "market",
    "doctor", "planet", "energy", "nature", "memory"
]

n = 1

input("[타자 게임] 준비되면 엔터!")
start = time.time()

while n < 11:
    print(f"{n}번 문제")
    question = random.choice(words)
    print(question)

    while True:
        user_answer = input()

        if question == user_answer:
            print("통과!!")
            n += 1
            break
        else:
            print("오타! 다시 도전!")

end = time.time()
play_time = end - start
print(f"총 소요시간 : {play_time: 2f}초")
'''

# sys 모듈
# 파이썬 인터프리터와 관련된 다양한 기능 제공


# 파이썬 버전 정보
print(sys.version)

# 운영체제 정보
print(sys.platform)

# 프로그램 종료
print("프로그램 시작")
# sys.exit()  # 강제 종료
print("실행되지 않는 코드")


# os 모듈
# 운영체제와 상호작용 할 수 있도록 도와주는 기능 제공

# getcwd(): 현재 작업 디렉토리 반환
print(os.getcwd())

# listdir(): 현재 폴더 내 파일, 디렉토리 목록 반환
print(os.listdir())


# 폴더 생성
folder_name = "sample_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print(f"{folder_name} 폴더가 이미 존재합니다.")

print(os.listdir())
