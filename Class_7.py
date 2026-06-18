
# # print("Hello")
# L = [1,2,3,4,5]
# # print(L[0])
# # print(L[2])
# # print(L[-1])

# L.append(6)
# print(L)
# L.insert(3, 3.5)
# print(L)


# def name():
#     print("Hello")
# for i in range(5):
#     name()

# def Hello(x):
#     print(x)

# Hello(10)
# Hello(20)
# Hello((10, 20, 30))
# Hello({"name": "Hello", "age": 19})

# # def Hello(X):
# #     print(X[0]["name"])
# def Hello(x):
#     return x
# a = Hello(10)
# print(a)


# def Hello(x):
#     return x[2][1]
# a = Hello([10,20,[30,40]])
# print(a)

# def Hello(x,y):
#     print(x,y)
# Hello(10,20)

# def Hello(x,y):
#     print(x[1],y[1])
# Hello([10,20],[30,40])


# while loop

# # 1d
# import numpy as np
# arr = np.arange(12)
# i = 0
# while i < len(arr):
#     print(arr[i], end=" ")
#     i += 1


#2d
import numpy as np

# arr1 = np.arange(12).reshape(3,4)

# i = 0
# while i < len(arr1):
#     j = 0
#     while j < i:
#         print(arr1[j], end=" ")
#         j += 1
#     print("\n")
#     i += 1

#2d
# arr1=np.arange(12).reshape(3,4)
# i=0
# j=0
# while i<len(arr1):
#     j=0
#     while j<len(arr1[i]):
#         print(arr1[i][j],end=" ")
#         j+=1
#     print()
#     i+=1

#     arr = np.arange(12).reshape(3,4)
# i = 0
# while i < len(arr):
#     j = 0
#     while j < len(arr[i]):
#         print(arr[i][j], end=" ")
#         j += 1
#     i += 1

# arr = np.arange(24).reshape(3,4,2)
# i = 0
# while i < len(arr):
#     j = 0
#     while j < len(arr[i]):
#         k = 0
#         while k < len(arr[i][j]):
#             print(arr[i][j][k], end=" ")
#             k += 1
#         j += 1
#     i += 1


# for loop

# 1d
# import numpy as np
# arr = np.arange(12)
# for i in arr:
#     print(i, end=" ")