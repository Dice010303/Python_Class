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
print("\n")
f_arr = np.array([1.1,2.2,3.3])
print(f_arr)
print(f_arr.ndim)
print(f_arr.shape)
print(f_arr.size)
print(f_arr.dtype)

# 기본 배열 생성
# np.zeros((행,열)) - 요소가 모두 0
# np.ones( (행 , 열) ) - 요소가 모두 1
# ~ ~ ~ ~ ~~ ~ ~ ~ ~ ~  ~
# np.full( (행,열) , i ) - 요소가 모두 i

arr_0 = np.zeros((2,3))
print("\n요소가 모두 0인 행렬")
print(arr_0)

arr_1 = np.ones((2,3))
print("\n요소가 모두 1인 행렬")
print(arr_1)

print("\n요소가 모두 i인 행렬")
i=3
arr_i = np.full((2,3),i)
print(arr_i)

# like : ~ 처럼
print("\nshape이 어떤 배열과 동일하되 생성한 배열의 요소를 모두 0으로  채운 배열")
arr_zl = np.zeros_like(arr2)
print(arr_zl)

print("\nshape이 어떤 배열과 동일하되 생성한 배열의 요소를 모두 1로  채운 배열")
arr_ol = np.ones_like(arr1)
print(arr_ol)

print("\nshape이 어떤 배열과 동일하되 생성한 배열의 요소를 모두 임의의 어떤 수  i로  채운 배열")
arr_il = np.full_like(arr1,i) # i = 3
print(arr_il)

# 난수 행렬
print("\n난수 발생")
np.random.rand()

print("\nseed 0번")
np.random.seed(0)
rd_int = np.random.randint(-100,101,(4,4)) # 요소의 범위가 -100 ~ 100 까지 임의의 정수로 구성된 4 * 4 행렬
print(rd_int)

print("\nseed 1번")
np.random.seed(1) # 각 seed마다 고정값을 갖게 해준다 .
rd_int = np.random.randint(-100,101,(4,4)) # 요소의 범위가 -100 ~ 100 까지 임의의 정수로 구성된 4 * 4 행렬
print(rd_int)

# ndArray에서의 indexing과 slicing
print("\n리스트의 indexing")
lst = [1,2,3,4]
print(lst[0])
# print(lst[0:2])

print("\n1차원 배열의 indexing")
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(arr1[0])

print("\n1차원 배열의 slicing")
print(arr1[0:2]) # 처음부터 end(0,1,2) - 3번쨰 인덱스 전까지 출력
print(arr1[0:5:2])
print(arr1[::])
print(arr1[:]) # 같다

print("\n2차원 배열의 indexing")
arr2 = np.array(
    [[1,2,3],
    [4,5,6]]
)
print(arr2)
print("------------") # 구분선
print(arr2[0]) # 2차원의 0번째 행의 전체 요소들
print(arr2[0,0]) # 2차원의 0번째 행 0번째 열의 요소
print(arr2[0,1])
print(arr2[1,2])
print(arr2[:,:]) # 전체 행과 전체 열의 전체 요소들
print(arr2[:,1]) # 전체 행과 1번째 열의 요소들
print(arr2[0,:]) # 0번째 행과 전체 열의 요소들

# 원하는 부분만 indexing 해오기
# fancy indexing -> 원하는 인덱스를 배열로 넘기는 것
print("\n1차원 배열의 fancy indexing")
print(arr1)
print("----------") # 구분선
arr1_f = arr1[[0,2]] # 0번 인덱스와 2번 인덱스
print(arr1_f)
print(arr1_f[0])

print("\n2차원 배열의 fancy indexing")
print(arr2)
print("----------")
arr2_f = arr2[[0,1],[1,2]] # [[행],[열]] 각각
print(arr2_f)
arr2_f1 = arr2[::,[0,2]] # 전체행중 0번 열과 2번 열
print(arr2_f1)

# 논리 인덱싱
arr4 = [True,False,True,True,False]
print(arr1[arr4]) # 논리값이 True 인 인덱스만 출력
print(arr1>1)