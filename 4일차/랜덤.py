import random as ran
from math import ceil

# print(ran.random())
# => 0~1사이의 값을 랜덤하게 반환함

# print(ceil(ran.random() * 100))

# print(ran.randrange(4, 7))
# => 랜덤한 값의 범위를 지정할 수 있음

# nums = [1,2,3,4,5,6]

# ran.shuffle(nums)
# print(nums)

# random_num = ran.choices(nums)
# =>리스트 값중 랜덤하게 하나 뽑아줌
# print(random_num)
# =>숫자만 있는게 아니라 리스트 자체를 반환해줌 숫자 하나 뽑음


# -----------------------------------------------------

menus = ["딸기", "명란크림우동", "감자탕", "쇠주", "츄르", "김밥"]

print(f"오늘의 점메추: {ran.choices(menus)}")