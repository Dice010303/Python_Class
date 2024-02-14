import pandas as pd

# dictionary -> DataFrame
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)

# list -> DataFrame
df2 = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], index=[1,2,3], columns=['col1', 'col2', 'col3'])
print(df2)

# 생성된 DataFrame의 행과 열의 이름 변경
df2.index = ['row1','row2','row3'] # 행
df2.columns = ['열1','열2','열3'] # 열

# 원하는 행 또는 열의 이름 변경
df2.rename(index={'row1':'행1'}, inplace=True) # 행
df2.rename(columns={'열1':'col1'}, inplace=True) # 열
# df2.rename(columns={'열1':'col1'}, index={'row1':'행1'}, inplace=True) # 행과 열 동시
print(df2)

# DataFrame의 행과 열 삭제
# df2.drop('row3', axis=0, inplace=True) # axis = 0 => 행 삭제
df2.drop('열3', axis=1, inplace=True) # axis = 1 => 열 삭제
print(df2)