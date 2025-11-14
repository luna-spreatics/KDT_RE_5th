'''
리스트 (List)
- 여러 값들을 순서대로 저장할 수 있는 자료형
- 인덱스(index): 각 값에 부여된 순서 (0부터 시작)
- 가변 자료형(mutable): 원소의 추가/수정/삭제 가능
'''

# 리스트 만들기
list1 = [] # 빈 리스트
list2 = ["안녕하세요", "반갑습니다"]
list3 = [10, "good", 3.14, [1,2,3,4]]

print(list1, list2, list3)

list4 = list()
list5 = list("Codingon")
print(list4, list5)


# ==============
# 인덱싱과 슬라이싱
my_list = [1,2,3,4,5]
print(my_list[0]) # 1
print(my_list[-1]) # 5
my_list[3] = -1
print(my_list)

# number = input("네 자릿수 정수를 입력하세요: ")
# 천 = number[0]
# 백 = number[1]
# 십 = number[2]
# 일 = number[3]
# print(천, 백, 십, 일)

# -----------
# 슬라이싱
my_numbers = [10,20,30,40,50,60,70,80,90,100]
print(my_numbers[1:4]) # [20, 30, 40]
print(my_numbers[3:])
print(my_numbers[:4])
my_numbers[2:4] = [300,400]
print(my_numbers)

# 실습
items = ["a", "b", "c", "d", "e"]
print("문제4", items[::-1])

data =  ["zero", "one", "two", "three", "four", "five"]
print("문제5", data[::2])

movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = ["매트릭스", "타이타닉"]
print("문제6", movies)

subjects = ["국어","수학","영어","물리","화학","생물","역사","지구과학","윤리"]
print("문제7", subjects[3:8:2])

data = ["A","B","C","D","E","F","G","H","I"]
print("문제8")
print(data[0:3][::-1], end=" ")
print(data[3:6][::-1], end=" ")
print(data[6:9][::-1])

# 인덱싱, 슬라이싱 주의 사항
my_list = [1,2,3,4]
# my_list[5] # IndexError: list index out of range

my_list = [1,2,3,4,5]
print(my_list[4:1:2]) # []
print(my_list[1:3:-1]) # []

# ==========================
# 리스트 연산 - del
my_list = [10,20,30,40,50]
del my_list[2] # 특정 요소 삭제
print(my_list)
del my_list[1:3] # 슬라이스 범위 삭제
print(my_list)
del my_list # 리스트 삭제
# print(my_list) # NameError: name 'my_list' is not defined

# 리스트 연결 - +
list1 = ["가", "나", "다"]
list2 = ["라", "마", "바"]
new_list = list1 + list2
print(list1, list2, new_list, sep=" / ")

# 리스트 반복 - *
medal = ["금", "은", "동"]
new_list = medal * 3
print(medal, new_list, sep=" / ")

# 포함 여부 (in, not in)
fruits = ["토마토", "사과", "포도", "수박", "바나나"]
print("포도" in fruits)
print("참외" not in fruits)

# 실습 1
fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
print(fruits)
result = fruits[:1] + fruits[1:]
print(result)

# 실습 2
letters = ["A", "B"]
new_letters = letters * 3
print(new_letters)
del new_letters[2]
print(new_letters)

# ==================
# 리스트 주요 메서드
# ==================

# 길이
numbers = [1,2,3,4,5]
print("1. len()", len(numbers), len("codingon"))

# 삽입
numbers.append(6)
numbers.append(7)
numbers.append(8)
print("2. append()", numbers)

numbers.insert(2, 2.5)
numbers.insert(4, 3.5)
print("3. insert()", numbers)

numbers.extend([9, 10])
print("4. extend()", numbers)

# 삭제
numbers.append(2.5)
numbers.remove(2.5)
print("5. remove()", numbers)

a = numbers.pop(1)
print("6. pop() 삭제한 요소", a)
print(numbers)
b = numbers.pop()
print("6. pop() 삭제한 요소", b)
print(numbers)

# 정렬
numbers1 = [3,2,1,4]
numbers1.sort()
print("7-1. sort()", numbers1)
numbers1.sort(reverse=True)
print("7-1. sort(reverse=True)", numbers1)

numbers2 = [50, 52, 53, 51]
new_numbers = sorted(numbers2)
new_numbers_desc = sorted(numbers2, reverse=True)
print("7-2. sorted()", numbers2, new_numbers, new_numbers_desc)

# 뒤집기
my_numbers = [100, 101, 104, 103, 102]
my_numbers.reverse()
print("8-1. reverse()", my_numbers) # [102, 103, 104, 101, 100]

my_numbers2 = list(reversed(my_numbers))
print("8-2. reversed()", my_numbers2, my_numbers)

# count, min, max, sum
numbers = [1, 2, 2, 2, 2, 3, 4, 5, 6, 7]
print("9. count()", numbers.count(2))
print("10. min/max", min(numbers), max(numbers))
print("11. sum", sum(numbers))

# 실습3 - 기차 탑승 시뮬레이션
train = []
train.append("철수")
train.append("영희")
print("1.", train)

train.extend(["민수","지훈"])
print("2.", train)

train.remove("영희")
print("3.", train)

train.insert(1,"수진")
print("4.", train)

train.remove("민수")
train.reverse()
print("5.", train)

# 문제2 - 숫자 처리 게임
cards = [5,3,7]
cards.extend([4,9])
print("1.", cards)

print("2. 가장 큰 수:", max(cards))
print("2. 가장 작은 수:", min(cards))

print("3. 총합:", sum(cards))
cards.sort()
print("4. 제거한 숫자:", cards.pop())
print("5.", cards)