import time

# print("5초 뒤에 종료합니다")
# time.sleep(5)
# print("프로그램이 종료되었습니다")

# *문제
# -시간 카운트 다운
# -while을 써서

# ->1초에 한번씩 숫자가 나와야함
# 그 숫자는 5에서 1까지 줄어들어야함 -> -= 쓰겠지?

# 1초에 한번씩 print되어야함

# 저 시간들어가야하는거를 i로 넣고 i를 5라고 설정해주고 그 i가 -=되면 되겠노



i = 6
ending = True
print(f"{i-1}초 뒤에 종료합니다")

while ending:
    i -= 1
    print(f"{i}초")
    time.sleep(1)

    if i == 0:
        ending = False
        print(f"끝!!!")

# 정신차려 김정현...