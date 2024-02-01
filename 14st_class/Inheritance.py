# 상속(inheritance) -> 물려 받다, 물려 받은 기능을 유지한 채 다른 기능을 추가

# 물려 주는 클래스 -> 부모 클래스
# 물려 받는 클래스 -> 자식 클래스
class Person:
    def hi(self):
        print('안녕')

class Student(Person):
    # def hi(self):
    #   print('안녕')

    def hi(self):  # 자식 클래스는 부모 클래스로부터 물려 받은 내용을 수정할 수 있다 -> overriding
        pass

    def study(self):
        print('공부하다')

# 자식 클래스의 메서드/속성의 개수 >= 부모 클래스의 메서드/속성의 개수
# 부모는 자식의 것 접근 불가

jin = Student()
jin.hi()

# paul = Person()
# paul.study() # 부모 클래스에는 존재하지 않는 기능

# 상속 - 포함 관계 아닐 때 할 필요 없음
class Person:
    def hi(self):
        print('안녕')

class Add_Person:
    def __init__(self):
        self.person_directory = [] # 명단에는 사람이 있다

    def add_person(self, person):
        self.person_directory.append(person)