# for(let i = 0; i < 10; i++){
#     console.log(i);
# }

for num in [0,1,2,3,4]:
    print(num)

# => num에 in하겠다 []이거 안에잇는걸 순서대로

arr = [0,1,2,3,4]

for num in arr:
    print(num)

# =>이렇게 줄이는 방법이 있고

for num in range(5):
    print(num)

# => for문의 가운데라고 보면됨 range가

for num in range(5):
    print(num + 1)

#  => num에 1을 더해 0+1로 1부터 시작하게 한다

for num in range(0,10,2):
    print(num)


for num in range(1,10):
    print(f"5 x {num} = {5 * num}")