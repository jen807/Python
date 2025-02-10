# for i in range(1, 4):
#     print("--------")
#     print(i)
#     print("--------")

#     for n in range(4, 7):
#         print(n)

# for i in range(1, 10):
#     print(f"{i}단")

#     for n in range(1,10):
#         print(f"{i}x{n}={i*n}")

# value = int(input("숫자를 입력해주세요"))

# for n in range(1, 10):
#     print(f"{value} x {n} = {value * n}")
# print(value)

# 1. 두개의 숫자를 입력해서 누가 더 큰지?

value1 = input("첫번째 숫자를 입력해주세요")
value2 = input("두번째 숫자를 입력해주세요")

if value1 > value2:
    print(f"{value1}(이)가 {value2}보다 더 큽니다")
elif value2 > value1:
    print(f"{value2}(이)가 {value1}보다 더 큽니다")
else:
    print(f"두 숫자가 같습니다")


# 2. 변수로 임의의 유저 아이디와 패스워드를 저장하고 input을 통하여 입력한 아이디와 패스워드가 맞는지 확인할 수 있는 유효성 로직 구현

id = "30"
pw = "30"

value1 = input("아이디를 입력해주세요")
value2 = input("비밀번호를 입력해주세요")

if value1 == id and value2 == pw:
    print(f"{id}님 로그인 되셨습니다")
else:
    print(f"비밀번호나 아이디가 틀렸습니다. 다시 입력해주십시오")
