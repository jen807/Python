# *상속
# =>특정 클래스의 내용을 그대로 가져올 때 사용
# =>상속한 클래스를 부모 클래스, 상속받는 클래스를 자식 클래스

# 유저 회원가입
# =>username
# =>password
# =>name
# =>email
# =>created_at
# =>updated_at

# 컨텐츠
# =>title
# =>desc
# =>img
# =>created_at
# =>updated_at

# 댓글
# =>comment
# =>created_at
# =>updated_at

import datetime as dt

# class ParentClass:
#     def parent_text(self):
#         return "부모클래스"


# # parent = ParentClass()
# # print(parent.parent_text())

# class ChildClass(ParentClass):
#     def child_text(self):
#         return "자식클래스"
    
# class Minsu(ParentClass):
#     def minsu_text(self):
#         return "im minsu😎"
    
# child = ChildClass()
# print(child.parent_text())
# print(child.child_text())

# minsu = Minsu()
# print(minsu.minsu_text())
# print(minsu.parent_text())

# print(dt.datetime.now())

# *문제
# 회원가입 클래스를 제작하려고 하는데 이때 자동으로 회원가입 날짜를 상속 받을 수 있도록 함
# 클래스 두개 생성
# 부모 클래스에는 회원가입 날짜 출력하는 함수 제작 (datetime 모듈 사용)
# 자식 클래스 기능은 유저의 아이디, 패스워드를 입력한 값 출력

# 출력결과
# 아이디 sideway / 패스워드 123
# 회원가입 날짜: 2023-~~~~~~

class Parent:
    def date(self):
        return dt.datetime.now()
    

class Child(Parent):
    def __init__(self, id, pw):
        self.idid = id
        self.pwpw = pw

    def desc(self):
        return f"아이디: {self.idid} / 패스워드: {self.pwpw}"

id = input("아이디를 입력해주세요")
pw = input("비밀번호를 입력해주세요")

result = Child(id, pw)
print(result.desc())
print(f"회원가입 날짜: {result.date()}")