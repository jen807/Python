country = {
    "kr": "한국",
    "jp": "일본",
    "us": "미국",
    "eu": "유럽",
}

find_key = input("찾을 키 명을 입력하셈!")

# *딕셔너리 키 확인 (in)
# =>딕셔너리 내부에 찾고자 하는 키가 있는지 확인

# if find_key in country:
#     print(country[find_key])
# else:
#     print("찾는 키가 없어요...🥲")

get_country = country.get(find_key)
print(get_country)