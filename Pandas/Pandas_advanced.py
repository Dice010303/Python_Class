# index - row 식별하는 값
import pandas as pd
data = {
    'num':[1,2,3],
    'name':['kim','lee','park'],
    'address':['Seoul','Deajeon','Jeonju']
}
df = pd.DataFrame(data)
print(df)

# 인덱스 변경
df.index = ['1번', '2번', '3번']
df.index.values[0] = 'a'
df.index.values[1] = 'b'
print(df)

# 기존 컬럼으로 인덱스 설정하기
# df.index = df['num']
# print(df)

# 인덱스 초기화
df.reset_index() # 동일한 이름의 컬럼 -> 오류 발생

data = {
    'num':[1,2,3],
    'name':['kim','lee','park'],
    'address':['Seoul','Deajeon','Jeonju']
}
df = pd.DataFrame(data)
df.index.name = 'num'

# 컬럼 삭제
# 인덱스 초기화
df2 = df.reset_index(drop=True)
print(df)
print(df2)

df2 = df.reset_index(drop=True, inplace=True) # inplace - 원본 데이터에 적용 여부
print(df2)