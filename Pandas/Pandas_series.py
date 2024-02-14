import pandas as pd

# dictionary -> Series
dict_data = {'a':1,'b':2,'c':3,'d':4}
sr1 = pd.Series(dict_data)
print(sr1)

# 시리즈의 index
print(sr1.index)
# 시리즈의 data
print(sr1.values)

# list -> Series
list_data = ['d','e','f']
sr2 = pd.Series(list_data)
print(sr2)

sr3 = pd.Series(list_data, index=['1','2','3'])
print(sr3)

# Series에서 원하는 부분만 보기
capital = {'Korea':'Seoul', 'USA':'washington DC', 'Japan':'Tokyo', 'Canada':'Ottawa'}
sr4 = pd.Series(capital)

print(sr4[['Korea', 'USA']])
print(sr4[[0, 3]])

# Series의 사칙연산
sr5 = pd.Series([1,2,3])
sr6 = pd.Series([4,5,6])

## 덧셈
print(sr5 + sr6)
## 곱셈
print(sr5 * sr6)
print(sr5 * 5)