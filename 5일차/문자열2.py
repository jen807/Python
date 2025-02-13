# text = "파이썬이 이제 조금 친해진 것 같아"
# print(text.split())
# =>문자열을 띄어쓰기 기준으로 나눠서 리스트로 반환

# print(text.find("이제"))
# =>왼쪽에서 시작하여 처음 등장하는 위치를 인덱스로 반환함

text = "코딩 개발 파이썬 프로그래밍 언어 정환쌤 굿 최고"
# for hashtag in text.split():
#     print(f"#{hashtag}")

# def hash(text):
#     hashtag = text.split()
#     for word in hashtag:
#         print(f"#{word}")

# hash(text)

# print(text.split())

# i = []

# for hashtag in text.split():
#     i.append(f"#{hashtag}")

# print(i)


def hash(text):
    hashtag = text.split()
    i = []
    for word in hashtag:
        i.append(f"#{word}")
    
    return i 

result = hash(text)

print(result)
        

