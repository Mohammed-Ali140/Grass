
import numpy as np

# l = [1 , 2 , 3]
# print(l)

# arr = np.array(l)
# print(arr)

# l1 = [[1,2,3],[4,5,6]]
# # l1[1].remove(4)
# # l1[1].insert(0 ,100)
# print(l1)                          # 2D List

# arr = np.array(l1)
# print(arr)

# l1 = [[[1,2,3]],[[4,5,6]],[[7,8,9]]]
# print(l1)                               # 3D List

# arr = np.array(l1)
# print(arr)
# print(arr.shape)

 
# l = [1,2,3]
# lm = l * 2
# print(lm)                 # [1, 2, 3, 1, 2, 3]

# arr = np.array(l)
# arrM = arr + 2 
# print(arrM)               # [3 4 5]
# arrM = arr * 2 
# print(arrM)             # [2 4 6]



# import numpy as np
# import time

# # List
# start = time.time()
# l = [i * 2 for i in range(1000000)]
# print("List output:", time.time() - start)

# # NumPy Array
# start = time.time()
# arr = np.arange(1000000) * 2
# print("Array output:", time.time() - start)
 


# zeros array  1D
# arr = np.zeros(5)
# print(arr)

# zeros array  2D
# arr1 = np.zeros((3,4))
# print(arr1)

# ones array  1D
# arr = np.ones(5)
# print(arr)

# # ones array  2D
# arr1 = np.ones((3,4)) * 10
# print(arr1)

# # Full for 1D
# arr2 = np.full((3),5)
# print(arr2)

# # Full for 2D
# arr2 = np.full((2,3),5)
# print(arr2)

# arr = np.zeros((3,4)) 
# print(arr + 6)

# arr1 = np.full((2,2),1)
# print(arr)



# Random  for 1D 0 -> 1
# arr = np.random.random(5)
# print(arr)

# # Random  for 2D 0 -> 1
# arr = np.random.random((2,3))
# print(arr)


# arrange for 1D 
# arr = np.arange(5)
# print(arr)

# # arrange for 1D
# arr1 = np.arange(0,10,2)
# print(arr1)

# vector 1D List
# l = [1,2,3]
# print(l)

# # vector 2D Array
# arr = np.array(l)
# print(arr)

# # Matrix 1D List
# l = [[1,2,3],[4,5,6]]
# print(l)

# # Matrix 2D Array
# arr1 = np.array(l)
# print(arr1)

# # Tensor 1D List
# l = [[[1,2],[3,4]],[[5,6],[7,8]]]
# print(l)

# # Tensor 2D Array
# arr2 = np.array(l)
# print(arr2)


# Array Properties

import numpy as np

arr = np.arange(11)

print("shape:", np.shape(arr))
print("dimension:", np.ndim(arr))
print("size:", np.size(arr))
print("datatype:", arr.dtype)