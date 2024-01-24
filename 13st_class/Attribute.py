# 속성
class Person:
    def __init__(self, name): # 생성자(constructor)
        self.hello = '안녕하세요'
        self.name = name
        self.age = 19

    def introduce(self):
        print("이름 : {}".format(self.name)) # 객체 내부에서 해당 객체 내부의 속성에 접근할 때 -> self. 사용
        print("나이 : {}".format(self.age))
        # print("취미 : {}".format(self.hobby))

    def Hi(self):
        print(self.hello)


chim = Person('chim') # Person 객체 생성 -> __init__메서드 (생성자) 실행
chim.introduce()

print('---')
print("이름 : {}".format(chim.name)) # 객체 외부에서 내부의 속성에 접근할 때
print("나이 : {}".format(chim.age))
# print("취미 : {}".format(chim.hobby))

poong = Person('poong')
poong.age = 20
print('---')
print("이름 : {}".format(poong.name)) # 객체 외부에서 내부의 속성에 접근할 때
print("나이 : {}".format(poong.age))
# print("취미 : {}".format(poong.hobby))

class Person:
    pass # 콜론(:) 다음의 공간을 채워야 하지만 아무런 기능이 필요없을 때

chim = Person() # 인스턴스 하나 생성
# print(chim.name) -> name 속성 없음

chim.name = 'chim' # 나중에 객체 내부에 속성을 추가한 행위
print(chim.name) # -> name 속성 존재
chim.address = '안산'
print(chim.address)

poong = Person()
poong.name = 'poong'
poong.age = 44
poong.hobby = '요리'

print("이름 : {}".format(poong.name)) # 객체 외부에서 내부의 속성에 접근할 때
print("나이 : {}".format(poong.age))
print("취미 : {}".format(poong.hobby))
# print(poong.address) -> poong에게는 없는 속성

# 비공개 속성 -> 객체 외부에서 접근 불가, 객체 내부에서만 사용 가능
class Person:
    def __init__(self, name, age, hobby, weight):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.hobby = hobby
        self.__weight = weight # 비공개 속성(_ 속성명 앞에 2개 작성)

    def diet(self, loss_weight):
        print("chim의 체중 감량 전 : {}kg".format(self.__weight))
        self.__weight -= loss_weight
        print("chim의 체중 감량 후 : {}kg".format(self.__weight))

chim = Person('chim', 42, '그림', 100)
# chim.__weight -= 20 -> 비공개 속성으로 외부 접근 불가능
chim.diet(20)