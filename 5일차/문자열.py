# *format()
# =>format을 사용하면 중괄호 기준으로 매개변수 역할을 할 수 있음
# =>"{}" 매개변수 역할을 함

# text = "{}".format("python!!!!!!")
# print(text)

# nums = "{} {} {}".format("1","2","3")
# print(nums)

# today = "{}년 {}월 {}일".format("25","2","13")
# print(today)

# *대소문자 (upper, lower)

# text1 = "this text is changed to uppercase"
# print(text1.upper())

# text2 = "THIS TEXT IS CHANGED TO LOWERCASE"
# print(text2.lower())

text = """
                        이렇게 띄어쓰기를 하여
글을 작성하여 출력하면?
    """

# print(text)
print(text.strip())
# =>글자 양옆 공백 제거