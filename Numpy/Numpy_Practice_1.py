import numpy as np

np.random.rand()

# -10 ~10 사이의 정수로 (3,4) 모양의 배열을 만들고 arr1에 저장
np.random.seed(0)
arr1 = np.random.randint(-10,11,(3,4))
print(arr1)
print("\n")
# 아래와 같은 2차원 배열을 만들고 arr2에 저장
arr2 = np.array(
    [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
)
# 1,2,3,4
# 5,6,7,8
# 9,10,11,12
# 13,14,15,16

# 1. 각 배열의 차원, 모양, 원소의 갯수를 확인
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

print("\n")

print(arr2.ndim)
print(arr2.shape)
print(arr2.size)

# 2. arr1에서 행은 모두 출력하고 열은 첫번째, 세번째만 출력
print("\n")
print(arr1[:,[0,2]])

# 3. arr2에서 아래처럼 나오게 인덱싱해주세요
# [6, 7]
# [10, 11]
print("\n")
print(arr2[1:3,1:3]) # 1번행~2번행 과 1번열~2번열 의 요소값

# 4. arr1에서 음수만 출력
print(arr1[arr1<0])

# np.where(조건,True일때 값 , False일때 값)
arr3 = np.where(arr1 < 0,arr1,0)
print(arr3)