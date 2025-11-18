'''
조건문
- 조건에 따라 프로그램의 실행 흐름을 분기시키는 제어문
- 조건 : 참/거짓을 구분할 수 있는 문장
'''

# 조건문의 기초 문법
# if + 조건 -> 조건이 참이면 실행

'''
a = int(input())
if a > 10:
    print("a는 10보다 커요")
print("조건문 종료")

# 들여쓰기 에러 예시
if a > 10:
    print("조건문 종료")
  
# print("a는 10보다 커요") # IndentationError

# 조건문에 실행할 코드를 작성하지 않았을 때
# pass로 해당 조건문을 넘어갈 수 있음
if a > 100:
    pass


# 실습1. ​날씨에 따른 준비물 안내
# 오늘의 날씨에 따라 필요한 준비물이 달라집니다.
# 사용자에게 오늘의 날씨를 입력받고, 그에 따라 적절한 메시지를 출력하는 프로그램을 만들어 보세요.
weather = input("비 또는 맑음을 입력해주세요: ")

# 비가 오는 경우 
# 날씨가 비 라면? → 날씨가 비와 같다
if weather == "비":
  print("우산을 챙기세요!")

# 날씨가 맑은 경우
# 날씨가 맑음 라면? → 날씨가 맑음과 같다
if weather == "맑음":
  print("선크림을 바르세요!")
'''

'''
# if - else 문
# 조건이 참일 때는 if문을 조건이 거짓일 때는 else문을 실행
# else -> ~아니라면 의 의미 -> 조건이 필요X, if문과 반드시 같이 나와야 함.
a = int(input())
if a > 10:
    print("a는 10보다 커요")
else:
    print("a는 10보다 작아요")
    


# 실습2. ​짝수 홀수 판별하기
number = int(input("정수를 입력해주세요."))

# 짝수판단
if number % 2 == 0:
  print("짝수입니다.")
else:
  print("홀수입니다.")
  

# if - elif - else 구문
# elif : else if 의 약자
# elif 에서 조건을 반드시 기록
# if 가 있어야만 사용 가능

score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
    
    
    
# 실습3. 나이에 따른 영화 관람 가능 여부
# 영화관에서는 연령에 따라 관람할 수 있는 영화가 정해져 있습니다.
# 아래의 기준에 따라 사용자의 나이를 입력 받아 관람 가능한 등급을 출력하는 프로그램을 만들어보세요.
age = int(input("나이를 입력해주세요:"))

if age >= 19:
  print("청소년 관람 불가 가능")
elif age >= 16:
  print("15세이상 관람가 가능")
elif age >= 13:
  print("12세 이상 관람가 가능")
else:
  print("전체 관람가 시청 가능")
  

# 실습4
# 조건문을 이용해서 ​초를 입력하면 시, 분, 초로 나누어 알려주는 프로그램을 만들어 봅시다.
# 변수를 만들고 정수를 입력 받아 주세요. 
# 입력 받은 변수의 값을 사용해서 변수 hour와 minute, second에 알맞은 값을 저장해 주세요.
# 조건에 따라 시, 분, 초를 적절히 출력해 주세요.

hour, minute, second = 0, 0, 0

input_second = int(input())

# 60s = 1m, 60m = 1h

minute = input_second // 60 
second = input_second % 60
hour = minute // 60
minute %= 60

if hour > 0:
    print(f"{hour}시간 {minute}분 {second}초")
elif minute > 0:
    print(f"{minute}분 {second}초")
else:
    print(f"{second}초")
'''

'''
# 중첩 조건문
# 하나의 if문 안에 또 다른 if문을 사용하는 것

username = input("관리자 아이디를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

if username == "admin":
    if password == "abcd":
        print("로그인 성공")
    else:
        print("비밀번호가 잘못됐습니다")
else:
    print("잘못된 사용자입니다")
''' 
    
# 실습 5
# 1)
money = int(input("금액을 넣어주세요: "))
item = input("김밥 / 삼각김밥 / 도시락 중 골라주세요: ")

# KIMBAB = "김밥"
# SAMKIM = "삼각김밥"
# DOSIRAK = "도시락"
# k_price, s_price, d_price = 2500, 1500, 4000

# if item == KIMBAB:
#   if money >= k_price:
#     print(f"{KIMBAB}을 구입했습니다")
#   else:
#     print("금액이 부족해요")
# elif item == SAMKIM:
#   if money >= s_price:
#     print(f"{SAMKIM}을 구입했습니다")
#   else:
#     print("금액이 부족해요")
# elif item == DOSIRAK:
#   if money >= d_price:
#     print(f"{DOSIRAK}을 구입했습니다")
#   else:
#     print("금액이 부족해요")
# else:
#   print("입력이 잘못됐습니다")


# 2) 딕셔너리 사용
prices = {
  "김밥" : 2500,
  "삼각김밥" : 1500,
  "도시락" : 4000
}

if item in prices:
  if money >= prices[item]:
    print(f"{item}을 구입했습니다.")
  else:
    print("금액이 부족해요.")
else:
  print("입력이 잘못됐습니다.")