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

value = int(input("숫자를 입력해주세요"))

for n in range(1, 10):
    print(f"{value} x {n} = {value * n}")
print(value)

# 1. 두개의 숫자를 입력해서 누가 더 큰지?
# 2. 변수로 임의의 유저 아이디와 패스워드를 저장하고 input을 통하여 입력한 아이디와 패스워드가 맞는지 확인할 수 있는 유효성 로직 구현