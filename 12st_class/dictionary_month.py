# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담기
# 조건 : 1월 ~ 3월까지
# 조건 : 2월의 마지막은 28일로 함
# 조건 : 첫 데이터의 key는 "1월", value는 31
days={
    "1월": 31,
    "2월": 28,
    "3월": 30
}
print(days)
# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, 수작업으로 순회출력
days={
    "1월": 31,
    "2월": 28,
    "3월": 30
}
print(days["1월"])
print(days["2월"])
print(days["3월"])
# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, keys()로 key 순회출력
days={
    "1월": 31,
    "2월": 28,
    "3월": 30
}
for day in days.keys():
    print(day)
# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, keys()로 key, value 순회출력
days={
    "1월": 31,
    "2월": 28,
    "3월": 30
}
for value in days.keys():
    day = days[value]
    print(day,value)
# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, values()로 value 순회출력
days={
    "1월": 31,
    "2월": 28,
    "3월": 30
}
for value in days.values():
    print(value)
# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, items()로 key, value 순회출력
days={
    "1월": 31,
    "2월": 28,
    "3월": 30
}
for key,value in days.items():
    print(key,value)
# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, 3월 정보를 제거
days={
    "1월": 31,
    "2월": 28,
    "3월": 30
}
if "3월" in days:
    del days["3월"]
for key,value in days.items():
    print(key,value)
# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, 2월을 29일로 수정
days={
    "1월": 31,
    "2월": 28,
    "3월": 30
}
if "2월" in days:
    days["2월"] = 29
for key,value in days.items():
    print(key,value)
# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, update를 이용하여, 2월을 29일로 수정하고 4월, 5월의 정보도 추가
days={
    "1월": 31,
    "2월": 28,
    "3월": 30
}
days_2={
    "2월": 29,
    "4월": 30,
    "5월": 31
}
days.update(days_2)
print(days)
# 문제 : 영수, 영희, 철수, 민수의 나이를 딕셔너리에 담기
# 조건 : 가장 효율적인 데이터 구조를 유지해주세요.
# 조건 : 변수명을 명확하고 간결하게 지어주세요.
# 조건 : 영수 11살
# 조건 : 영희 12살
# 조건 : 철수 13살
# 조건 : 민수 14살
ages = {
    "영수":11,
    "영희":12,
    "철수":13,
    "민수":14
}
print(ages)
# 문제 : 영수, 영희, 철수, 민수의 나이를 딕셔너리에 담고, 데이터를 넣은 순서대로 순회출력
ages = {
    "영수":11,
    "영희":12,
    "철수":13,
    "민수":14
}
for name,age in ages.items():
    print("{}는 {}살이다.".format(name,age))