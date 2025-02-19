# *예외
# 이건 필수
# =>예상치 못한 상황 -> 오류
# =>두가지의 오류가 있음
# 1.SyntaxError: 문법 오류
# 2.RuntimeError: 프로그램 실행중 발생하는 오류

# 1. 문법 에러
# print("pyton!)

# 2. 런타임 에러
# print("running this line code")
# num[0]

# *예외 처리 방법
# 1. 조건문으로 처리
# 2. try except 처리

# input_num = input("Input your number")

# if input_num.isdigit():
#     input_num = int(input_num)
#     print(f"Your input number is {input_num}")
# else:
#     print("Plz input numbers only😎")

try:
    input_num = int(input("Input your number: "))
    print(f"Your input number is {input_num}")
    # =>조건문이 붙지 않음
except:
    print("Error")
finally:
    print("무조건 실행")