# 상속 속성
class Person:
    def __init__(self):
        print('Person __init__ 호출')
        self.hello = '안녕'

class Student(Person):
    def __init__(self):
        print('Student __init__ 호출')
        super().__init__() # super() -> super()를 가지고 있는 클래스의 부모 클래스(Person 클래스)
        self.studyRoom = 'class C'

jin = Student()
print(jin.studyRoom)
print(jin.hello)

class Person:
    def __init__(self):
        print('Person __init__ 호출')
        self.hello = '안녕'

class Student(Person):
    pass # 자식 클래스 내에 __init__() 따로 존재하지 않으면 부모의 것을 그대로 사용한다

jin = Student()
print(jin.hello)

class Person:
    def hello(self):
        print('안녕하세요')

class Student(Person):
    def hello2(self):
        print('안녕하세요 저는 ~ 입니다')

class Office_worker(Person):
    pass

jin = Student()
jin.hello()

paul = Office_worker()
paul.hello()

# 오버라이딩(overriding)이란?
# 상속 관계에 있는 부모 클래스에서 이미 정의된 메소드를 자식 클래스에서 같은 이름을 갖는 메소드로 다시 정의

# overloading