import numpy as np

# list
lst = [1,2,3]
print(lst)
print(" ")

# ndArray 생성
arr1 = np.array([1,2,3])
print("1차원 배열")
print(arr1)
print(" ")

arr2 = np.array([
    [1,2,3],
    [4,5,6]
])
print("2차원 배열")
print(arr2)
print(" ")
arr3 = np.array(
 [
   [
     [1,2,3],
     [4,5,6]
   ],
   [
     [7,8,9],
     [10,11,12]
   ]
 ]
)

print("3차원 배열")
print(arr3)
print(" ")
# 출력시에 공백은 3차원에서의 면과 면의 공백 ?

print("ndArray의 차원 수 -> ndArray.ndim")
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

print("\n"+"ndArray의 모양 -> ndArray.shape") # 행 , 열 순
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)

print("\n"+"ndArray의 총 원소 개수 -> ndArray.size")
print(arr1.size)
print(arr2.size)
print(arr3.size)

print("\n"+"ndArray의 구성 원소 타입 -> ndArray.dtype")
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)

# 실수 요소로만 구성된 ndArray
`