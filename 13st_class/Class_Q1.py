# 문제1
class Warrior:
    def __init__(self,hp,mp,defence):
        self.hp = hp
        self.mp = mp
        self.defence = defence
    def attack(self):
        print("공격")
x = Warrior(1000, 50, 30)
print(x.hp, x.mp, x.defence)

x.attack()
# 출력 : 공격