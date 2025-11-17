'''
딕셔너리
- 키-값 쌍으로 묶어 데이터를 저장하는 자료형
- 키는 유일해야 함. 값은 중복 가능
- 변경 가능한 자료형
- 순서가 보장되지 않았다가 py 3.7 버전 이후 순서가 보장됨
'''

# dict 만들기
d1 = {} # 빈 dict 만들기
print(d1, type(d1)) # {} <class 'dict'>

person = {"name": "홍길동", "age" : 25}
print(person)

# dict 함수로 생성
d2 = dict()
print(d2, type(d2)) # {} <class 'dict'>

# 키가 문자열일 때 가능
movie = dict(title="int", director="nolan")
print(movie, movie["director"])

# 리스트나 튜플로 만들기
pairs = [("name", "luna"), ("age", 10), ("job", "dev")]
person2 = dict(pairs)
print(person2)

# zip 함수 활용
keys = ["title", "director", "year"]
values = ["기생충", "봉준호", "2019"]
movie2 = dict(zip(keys, values))
print(movie2)


# 키로 사용할 수 없는 자료형
# 키 - 불변 자료형만 사용해야한다
d1 = {(1,2,3): (1,2,3)} # 튜플 사용 가능
d2 = { 1 : 10 } # 숫자 사용 가능
# d3 = {[1,2,3]:"리스트 값을 키로?"} # TypeError: unhashable type: 'list'
# print(d3)



# dict 데이터 조회
print(person2["name"])
print(person2["age"])
# print(person2["city"]) # KeyError: 'city'

# get 메서드를 활용한 조회
print(person2.get("name"))
print(person2.get("email")) # None -> default
print(person2.get("email", "이메일이 존재하지 않습니다"))

# get 사용 예제
user_data = {
    "username" : "luna",
    "email" : "luna@spreatics.com",
    "password" : "1234"
}

# key = input("조회할 정보를 입력하세요(username, email, password): ")
# result = user_data.get(key, "존재하지 않는 데이터입니다.")
# print(result)


# 데이터 추가 및 수정
# 1) 기본적인 추가, 수정 방법
user_data["phone"] = "010-1234-3456"
user_data["username"] = "lunaaaaa"
print(user_data)

# 2) update 메서드 활용
user_data.update({"nickname" : "luna"})

# 키가 문자열인 경우
user_data.update(phone="010-2345-6788")

# 다른 딕셔너리 추가
extra_data = {"city": "seoul"}
user_data.update(extra_data)

print(user_data)


# 데이터 삭제
del user_data["city"]
print(user_data)

# 키로 제거
nickname = user_data.pop("nickname")
print("pop >>", user_data, nickname, sep=" /// ")

# 가장 마지막 요소 제거
phone = user_data.popitem()
print(user_data, phone, sep=" /// ")

# dict 비우기
user_data.clear()
print(user_data)

# dict 삭제하기
del user_data
# print(user_data)



# 메서드
user_data = {
    "username" : "luna",
    "email" : "luna@spreatics.com",
    "password" : "1234"
}

# keys : 모든 키를 반환
print("키" , user_data.keys()) # dict_keys(['username', 'email', 'password'])
print("키" , list(user_data.keys()))

# values : 모든 값을 반환
print("값", list(user_data.values()))

# items : 모든 키값쌍을 반환
print("쌍", list(user_data.items()))




print("==================================")

# 실습

# 문제1
# 1단계: 빈 딕셔너리 생성 : user라는 이름의 빈 딕셔너리를 생성하세요.
user = {}

# 2단계: 사용자 기본 정보 추가 
# "username": "skywalker"
# "email": "sky@example.com"
# "level": 5
# user["username"] = "skywalker"
# user["email"] = "sky@example.com"
# user["level"] = 5
user.update({
  "username": "skywalker",
  "email": "sky@example.com",
  "level": 5
})
print(user)

# 3단계: 값 읽기 - "email" 값을 변수 email_value에 저장하고 출력하세요.
email_value = user["email"]
print(email_value)

# 4단계: 값 수정 - "level" 값을 6으로 수정하세요.
user["level"] = 6

# 5단계: 안전하게 키 조회 
# 딕셔너리에 "phone" 키가 없다면 "미입력"이라는 문자열을 출력하도록 하세요.
phone = user.get("phone", "미입력")
print(phone)

# 6단계: 항목 추가 및 삭제
# update()를 사용해 "nickname": "sky" 항목을 추가하세요.
# "email" 항목을 삭제하세요.
# "signup_date" 키가 없다면 "2025-07-10"으로 추가하세요 (setdefault() 사용).
# 최종 user 딕셔너리를 출력하세요.
user.update(nickname="sky")
user.pop("email")
user.setdefault("signup_date", "2025-07-10")

print(user)


# 문제2
# 1. 빈 딕셔너리 생성
students = {}

# 2. "Alice", "Bob", "Charlie" 세 학생의 점수를 각각 85, 90, 95로 추가한다.
students.update(Alice=85, Bob=90, Charlie=95)

# 3. "David" 학생의 점수(80)를 추가한다.
students["David"] = 80

# 4. "Alice"의 점수를 88로 수정한다.
students["Alice"] = 88

# 5. "Bob"을 딕셔너리에서 삭제한다.
students.pop("Bob")

# 6. 최종 students 딕셔너리를 출력한다.
print(students)