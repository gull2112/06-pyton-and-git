class User:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact

    def info(self):
        print(f'가입하신 계정의 이름은 {self.name}이며, 나이는 {self.age}, 그리고 연락처는 {self.contact}입니다.')

# 사용자 정보 입력받기
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
contact = input("연락처를 입력하세요 (형식: 000-0000-0000): ")

# 사용자 객체 생성
user = User(name, age, contact)

# 사용자 정보 출력
user.info()
