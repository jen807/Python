class ClassOne:
    def text_1(self):
        return "첫번째 클래스"

class ClassTwo(ClassOne):
    def text_2(self):
        return "두번째 클래스"
    
class ClassThree(ClassTwo, ClassOne):
    def text_3(self):
        return "세번째 클래스"
    
one_class = ClassOne()
print(one_class.text_1())

two_class = ClassTwo()
print(two_class.text_2())
print(one_class.text_1())

print("\n---------------\n")

three_class = ClassThree()
print(three_class.text_1())
print(three_class.text_2())
print(three_class.text_3())
