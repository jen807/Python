# *클래스
# 비슷한 코드가 자주 사용하게 되면 메모리 등 효율적으로 만들 수 없기 때문에
# 데이터 및 기능을 함께 묶어 새로운 객체의 형태로 만듦

# 변수 = 메모리 주소에 값이 할당

# num_1 = 0
# num_2 = 0

# def plus(a, b):
#     num_1 = a
#     num_2 = b
#     return num_1 + num_2


# def minus(a,b):
#     num_1 = a
#     num_2 = b
#     return num_1 - num_2

# plus_result = plus(1,2)
# minus_result = minus(2,1)

# print (f"덧셈결과: {plus_result}")
# print (f"뺄셈결과: {minus_result}")

# class Calc:
#     def __init__(self, a, b):
#         self.num_1 = a
#         self.num_2 = b

#     def plus(self):
#         return self.num_1 + self.num_2
    
#     def minus(self):
#         return self.num_1 - self.num_2

# input_num = Calc(2,4)
# # =>생성자 함수, 인스턴스

# print(f"덧셈 결과: {input_num.plus()}")
# print(f"뺄셈 결과: {input_num.minus()}")
# input_num = Calc(4,6)
# # =>생성자 함수, 인스턴스

# print(f"덧셈 결과: {input_num.plus()}")
# print(f"뺄셈 결과: {input_num.minus()}")


# 클래스를 만들거야 => 효율적인 함수를 만들거야

class Calc:
    def __init__(self, a, b):
        self.num_1 = a
        self.num_2 = b 
        # =>메모리에 들어갈 변수를 정의하겠다

    def plus(self):
        return self.num_1 + self.num_2
    
    def minus(self):
        return self.num_1 - self.num_2
    
    def mul(self):
        return self.num_1 * self.num_2
    
    def div(self):
        return self.num_1 / self.num_2
    
result = Calc(2,4)
print(f"덧셈: {result.plus()}")
print(f"뺄셈: {result.minus()}")
print(f"나눗셈: {result.div()}")
print(f"곱셈: {result.mul()}")


# ->클래스처음들어오는거에는무조건self를써야함
# human
# =>머리
# =>몸통
# =>팔
# =>다리

# 1번 사람의 함수
# 머리: 000
# 몸통
# 팔
# 다리

# -----------------------

# 내가 제작하는 떡볶이 (함수)
# =>떡, 고추장, 설탕... 만들어야 됨

# 밀키트(클래스)
# =>만들어야됨