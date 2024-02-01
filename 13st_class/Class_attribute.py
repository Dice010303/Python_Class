# 클래스 속성 : __init__ 외부에 존재하는 속성
class Person:
    folder = [] # 클래스 속성 -> 클래스(설계도)에 종속 => 모든 인스턴스에서 접근 가능(공유재 성격)
    def add_file(self, file):
        Person.folder.append(file) # 클래스 속성에 접근할 경우 클래스의 이름으로 접근

jin = Person()
jin.add_file('txt')

paul = Person()
paul.add_file('png')

print(jin.folder)
print(paul.folder)

class Person:
    def __init__(self):
        self.folder = [] # 인스턴스 속성 : __init__ 실행되면서 생성되는 속성

    def add_file(self, file):
        self.folder.append(file)

jin = Person()
jin.add_file('txt')

paul = Person()
paul.add_file('png')

print(jin.folder)  # ['txt']
print(paul.folder) # ['png']

# 비공개 클래스 속성
class Person:
    __weight = 100

    def print_weight(self):
        print(Person.__weight)

jin = Person()
jin.print_weight() # "비공개" 클래스 속성을 객체 내부에서는 접근 가능
# print(jin.__weight) # -> "비공개" 클래스 속성도 외부(클래스와 위상이 동일한 구역)에서 접근 불가능