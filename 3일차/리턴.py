# def plus(a, b):
#    return a + b

# result = plus(10,20)

# print(plus(10,20))
# print(result)

# *문제

# 교통카드 프로그램 제작
# 어린이, 일반 카드로 분류
# 어린이 요금은 500원, 어른 요금은 1300원
# 매개변수에 어린이 또는 일반 , 10000 (카드요금)
# 잔액 추가

# 어린이를 매개변수로 입력시 출력결과 어린이 입니다, 500원 차감 되었습니다.
# 잔액은 ~입니다.

def card(type, left):
   card_money = {
      "어린이": 500,
      "일반": 1300
   }
   if type in card_money:
      left = left - card_money[type]
      print(f"{type}입니다, 잔액은 {left}원 입니다.")
   else:
      print("카드를 다시 한번 대주십시오")

   return left

card("어린이",10000)
card("일반",10000)
card("엥",10000)