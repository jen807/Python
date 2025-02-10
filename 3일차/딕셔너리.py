# * 딕셔너리
# => 리스트처럼 요소를 저장하지만 키와 값으로 구분되어 사용함
# => 값을 불러올땐 대괄호를 이용하여 불러옴

# dict = {
#     # "key": "value"
#     "num_1": 10,
#     "num_2": 20,
#     "num_3": 30
# }

# print(dict["num_1"])
# print(dict["num_3"])
# print(dict["num_2"] + dict["num_3"])

user = {
    "username": "Jen",
    "profile_img": "my_face.jpg",
    "name": "jeong hyun",
    "email": "80chill@naver.com",
    "follow": ["front_end", "back_end", "data_base"]
}


print(f"아이디: {user["username"]}")
print(f"팔로우: {user["follow"]}")
print(f"팔로우: {user["follow"][1]}")

for follow in user["follow"]:
    print(follow)