# list / dictionary
#
# 1. 공통점 -> 데이터 여러 개 묶을 때 사용
#           -> 둘 다 객체
#
# 2. 차이점
#     2-1. 리스트 장점
#     - 데이터 추가 편리(ages.append(40))
#
#     2-2. 딕셔너리 단점
#     - 데이터 추가 불편(ages["희민"]=40)
#
#     2-3. 리스트 단점
#     - 데이터 접근이 불편(print(ages[??]))
#
#     2-4. 딕셔너리 장점
#     - 데이터 접근이 편리(print(ages["병건"]))



# list
ages = [10,20,30]

# print(ages[0])  # 철수
# print(ages[1])  # 영희
# print(ages[2])  # 영수

print(ages)

for i in ages:
    print(i)

# dictionary
ages = {
    "철수" : 10,
    "영희" : 20,
    "영수" : 30
}

ages["희민"] = 40
print(ages)

# print("철수 나이 :", ages["철수"])
# print("영희 나이 :", ages["영희"])
# print("영수 나이 :", ages["영수"])
# print("희민 나이 :", ages["희민"])

print("=== v1 ===")
for name in ages:
    print(name)

print("=== v2 ===")
for name in ages:
    age = ages[name]
    print("{}의 나이 : {}".format(name, age))

print("=== v3 ===")
print("ages.keys() : ", ages.keys())
for name in ages.keys():
    age = ages[name]
    print("{}의 나이 : {}".format(name, age))

print("=== v4 ===")
print("ages.values() : ", ages.values())
for age in ages.values():
    print("나이 : {}".format(age))

print("=== v5-1 ===")
print("ages.items() : ", ages.items())
for name, age in ages.items():
    print("{}의 나이 : {}".format(name, age))

if "철수" in ages:
    del ages["철수"]

print("=== v5-2 ===")
print("ages.items() : ", ages.items())
for name, age in ages.items():
    print("{}의 나이 : {}".format(name, age))