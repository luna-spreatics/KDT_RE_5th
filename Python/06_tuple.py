'''
튜플
- 순서가 존재하는 여러 데이터의 모음
- 불변 (immutable) 자료형
'''


# ---- 튜플 생성 ----
my_tuple = (1, 2, 3, 4)
print(my_tuple) # (1, 2, 3, 4)
print(type(my_tuple)) # <class 'tuple'>

my_tuple2 = 5, 6, 7, 8
print(type(my_tuple2))

# 원소가 하나인 튜플 생성
single_el_tuple = (100,)

# 튜플 생성 함수로 생성
my_tuple2 = tuple()
print(my_tuple2)

my_tuple3 = tuple("codingon")
print(my_tuple3)

# ---- 언패킹 ----
# 시퀀스에 저장된 여러 값을 여러 변수에 나눠 저장하는 것
# 튜플, 리스트, 문자열...
apple, banana, kiwi = ("apple", "banana", "kiwi")
print(apple, banana, kiwi)

# -------------

# 불변성 (immutable)
# - 객체가 생성된 이후 내부 데이터를 변경할 수 없는 것
# my_tuple[0] = 100      # TypeError
# 삭제
# del my_tuple[1]       # TypeError
# 튜플 자체는 삭제 가능 but 원소 삭제는 불가
del my_tuple
# print(my_tuple) # NameError

# ---- 튜플 수정 ----
my_tuple4 = (10, 20, 30)
new_tuple = (100,) + my_tuple4[1:]
print("원본 튜플", my_tuple4)
print("새로운 튜플", new_tuple)

# ------------------------------------
# Step 1. 해킹된 고객 이름 복구하기
# 기존 튜플은 ("minji", 25, "Seoul")
# 이름을 "eunji"로 변경한 새 튜플을 만들어 변수 restored_user에 저장하세요.

user = ("minji", 25, "Seoul")

# 튜플은 수정 불가이므로, 슬라이싱과 결합을 사용해 새 튜플 생성
restored_user = ("eunji",) + user[1:]

# Step 2. 언패킹
# 복원된 튜플을 name, age, city로 언패킹하고 각각 출력해보세요.
name, age, city = restored_user

# Step 4. 고객 데이터 분석
# 아래 튜플에서 "minji"가 몇 번 등장하는지 count()로 구하고
# "soojin"이 처음 등장하는 인덱스를 index()로 구하세요.
users = ("minji", "eunji", "soojin", "minji", "minji")

count_minji = users.count("minji")
index_soojin = users.index("soojin")

# Step 5. 고객 리스트 정렬 (튜플은 변경하지 말고 sorted()로 리스트 형태로 출력)
sorted_users = sorted(users)

# 🔽 출력 결과 확인
print("복원된 고객 정보:", restored_user)
print(f"{name}님의 나이는 {age}세이며, 거주 도시는 {city}입니다.")
print(f"'minji'는 {count_minji}번 등장합니다.")
print(f"'soojin'은 {index_soojin}번 인덱스에 있습니다.")
print("정렬된 고객 리스트:", sorted_users)