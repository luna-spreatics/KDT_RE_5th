# 사용자 입력 (input)
# - input 함수 : 콘솔을 통해 사용자로부터 문자열 형태로 입력 받음


# input 함수 사용법
# my_input = input("콘솔에 띄울 설명")
# name = input("이름을 입력하세요: ")
# print(name)

# 숫자로 활용 시 '형 변환' 필요
# a = int(input())
# b = int(input())
# print(a + b)

# c = float(input())
# d = float(input())
# print(c + d)

# 여러 자료 입력하기
# 문자열을 쪼개주는 함수 : split() 
# - 기본 구분자 : 공백
# 과일1, 과일2, 과일3 = input().split()
# print(과일1, 과일2, 과일3)

# 다른 구분자 사용
apple, banana, grape = input().split("-")
print(apple, banana, grape)
