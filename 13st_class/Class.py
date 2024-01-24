# 객체를 이루는 요소
# 속성(attribute / property) - 체력,마력,공격력,방어력 -> 명사적 특징
# 기능(method) - 공격하다 , 방어하다 -> 동사적 특징
class Person:  # 클래스 = 객체의 설계도
    def __init__(self): #생성자(constructor)
        self.hello = "안녕하세요"
    def Hi(self):
        print(self.hello)
# Hello() -> 단독 사용은 불가능
chim = Person() # chim은 Person의 인스턴스
chim.Hi()

class Person:
    def Hello(self):
        print("hi")

    def Hi(self):
        self.Hello() # 하나의 기능에서 객체 내의 다른 기능을 실행하고 싶을 때 self 사용

chim = Person()
chim.Hi()