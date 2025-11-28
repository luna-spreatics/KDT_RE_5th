# 파일 입출력
# - 저장장치에 저장된 파일을 읽어오거나 저장하는 작업

# 파일 열기와 닫기
# 파일 열기 : open()
# open("파일 경로", mode="r", encoding="원하는 인코딩 - utf8")
# open으로 파일을 읽으면 '파일 객체'를 반환
'''
import random
f = open("example.txt", "w", encoding="utf-8")

f.write("파이썬 파일 입출력 예제\n")
f.write("파이썬 공부!!")

# 파일 닫기 : close()
# 열린 파일을 닫아 시스템 자원을 해제함
f.close()


# 파일 읽기
# read() : 전체 내용을 한번에 읽기
f = open("example.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()


# readline() : 한 줄씩 순차적으로 읽기
f = open("example.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()

print("첫번째 줄:", line1.strip())
print("두번째 줄:", line2)
f.close()

# for문으로 읽기
f = open("example.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
f.close()


# readlines() : 모든 줄을 한번에 리스트로 읽기
f = open("example.txt", "r", encoding="utf-8")
contents = f.readlines()
print(contents)
f.close()


# tell() : 현재 읽고 있는 위치(바이트)를 반환
f = open("example.txt", "r", encoding="utf-8")
print("처음 위치:", f.tell())
f.read(5)
print("5바이트 읽은 후 위치:", f.tell())
f.close()


# seek() : 파일 포인터 위치를 이동
f = open("example.txt", "r", encoding="utf-8")
print(f.read(10))  # 10바이트를 읽기
f.seek(0)  # 파일의 맨 처음으로 이동
print(f.read())
f.close()


# a 모드 : 추가 쓰기
f = open("example.txt", "a", encoding="utf-8")
f.write("\n추가한 내용입니다.")
f.close()


# with 문
# 파일 입출력시에 자동으로 close()를 호출해주는 구문

# 파일 쓰기
with open("with_example.txt", "w", encoding="utf-8") as f1:
    f1.write("with문으로 작성한 파일이에요\n")
    f1.write("파일 입출력 완료")


# 예제 1. 파일에서 랜덤 추출
with open("words.txt", "w", encoding="utf-8") as f1:
    words = [
        "apple", "banana", "orange", "grape", "lemon",
        "peach", "melon", "cherry", "plum", "pear",
        "school", "friend", "family", "flower", "garden",
        "window", "bottle", "pencil", "summer", "winter",
        "happy", "future", "travel", "animal", "market",
        "doctor", "planet", "energy", "nature", "memory"
    ]
    for i in words:
        f1.write(i + "\n")


with open("words.txt", "r", encoding="utf-8") as f1:
    data = f1.readlines()
    for i in range(5):
        word = random.choice(data).strip()
        print(word)


# 예제2. 입력 받아 파일 쓰기
with open("with_example.txt", "a", encoding="utf-8") as f1:
    while True:
        text = input("저장할 내용을 입력해주세요(종료 : z)")
        if text == "Z" or text == "z":
            break
        f1.write(text + "\n")


# 실습 1

import os
# ------------------------------------------
# 1. 회원 3명 입력하여 파일에 저장
# ------------------------------------------
if os.path.exists("member.txt"):
    print("member.txt가 이미 존재합니다. 회원 등록을 건너뜁니다.\n")
else:
    with open("member.txt", "w", encoding="utf-8") as f:
        for i in range(3):
            name = input(f"{i+1}번째 회원의 이름: ")
            password = input(f"{i+1}번째 회원의 비밀번호: ")
            f.write(f"{name},{password}\n")
        
print("\n[회원 명부 저장 완료]\n")


# ------------------------------------------
# 2. 로그인 과정
# ------------------------------------------
input_name = input("로그인 - 이름을 입력하세요: ")
input_password = input("로그인 - 비밀번호를 입력하세요: ")

login = False
with open("member.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, password = line.strip().split(",")
        if input_name == name and input_password == password:
            login = True
            break
        

# ------------------------------------------
# 3. 로그인 성공 시 전화번호 등록/수정
# ------------------------------------------
if login:
    print("\n로그인 성공!")
    
    # 기존 전화번호 데이터 로드
    phone_data = {}
    
    if os.path.exists("member_tel.txt"):
        with open("member_tel.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, phone = line.strip().split(",")
                phone_data[name] = phone
                
    # 전화번호 입력
    new_phone = input(f"{input_name}님의 전화번호를 입력하세요: ")
    
    # 추가 또는 수정
    if input_name in phone_data:
        print("기존 전화번호 수정")
    else:
        print("전화번호 새로 추가")
    
    phone_data[input_name] = new_phone
    
    # 전화번호 파일 갱신
    with open("member_tel.txt", "w", encoding="utf-8") as f:
        for name, phone in phone_data.items():
            f.write(f"{name},{phone}\n")
            
    print("전화번호 저장 완료!")
else:
    print("\n로그인 실패!")
    
'''   

import os

print(os.getcwd())
    
# 바이너리 파일 읽기
with open('./Python/images/dog.jpg', 'rb') as f:
    img = f.read()
    print(img)
    
# 바이너리 파일 쓰기
with open("./Python/images/dog_copy.jpg", "wb") as f:
    f.write(img)
    

    
# pickle 모듈
# - 객체의 형태를 유지하면서 파일에 저장하고 불러올 수 있음

import pickle

# 리스트, 딕셔너리 파일 저장
with open('pickle.txt', 'wb') as f:
    li = ['dog', 'cat']
    dic = {1:'dog', 2: 'cat'}
    
    pickle.dump(li, f)
    pickle.dump(dic, f)
    
# 읽기
with open('pickle.txt', 'rb') as f:
    li = pickle.load(f)
    dic = pickle.load(f)
    
    print(li, dic)