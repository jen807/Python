
# * 중첩튜플
# tu = ((1,2,3), (4,5,6))

# print(tu[1][0])
# print(tu[0][2])

# *문제
text1 = ("튜플을", "배워요")
text2 = ("파이썬의", "오늘은")

tu = (text1, text2)

print(f"튜플의 개수는: {len(tu)}")
print(f"튜플 내용 정리: ('{text2[1]}','{text2[0]}','{text1[0]}','{text1[1]}')")
print(f"text1을 두배로 출력한 결과: {text1 *2}")