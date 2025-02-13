# i = 0
# while i < 10:
#     print(i)
#     i += 1

# i = 0
# while i < 10:
#     print(f"2x{i}={2*i}")
#     i += 1

# up and down

import random
random_num = random.randrange(1,100)

playing = True
count = 0


while playing:
    input_num = int(input("숫자를 입력하세요"))
    count += 1

    if count < 5 :
        if input_num > random_num:
            print(f"DOWN!! 시도 {count}회")
        elif input_num < random_num:
            print(f"UP!! 시도 {count}회")
        elif input_num == random_num:
            playing = False
            print(f"정답!! 시도 {count}회 만에 성공")
    elif count > 4:
        playing = False
        print(f"도전 횟수 초과, 재시도 해주세요")

