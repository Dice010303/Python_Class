class Person:
    def hi(self):
        print("hi")

howard = Person() # howard : 클래스 인스턴스(howard)를 사용해서 메서드 호출
howard.hi()

# 정적 메서드(static method) -> 첫번째 매개변수로 self 불필요
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

Calc.add(10, 20) # 클래스에서 바로 메서드 호출 가능
Calc.mul(10, 20)

# 클래스 메서드(class method)
class Person:
    count = 0 # 클래스 속성(공공재)

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print("사람이 총 {}명 있다.".format(cls.count))

Person.print_count()

jin = Person()
Person.print_count()

paul = Person()
Person.print_count()