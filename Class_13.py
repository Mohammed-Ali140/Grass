
import numpy as np

#         ***** Sorting *****
# arr = np.array([10,90,330,4,60,9,5])
# print(arr)
# arr_s = np.sort(arr)
# print(arr_s)

# """ 2D
#     axis = 0 --> coloumn
#     axis = 1 --> rows 
# """
# arr = np.array([[1,5,2,3],[8,4,9,6]])
# print(arr)
# arr_s = np.sort(arr)
# print(arr_s)        # Asscending  # By Default sort by rows
# des_arr = arr_s[:,::-1]
# print(des_arr)           # Descending 

# # arr = np.array([[[11,4,2],[3,12,2][9,71,6]]])


# arr = np.array([10,90,330,4,60,9,5])
# arr_s = np.sort(arr)
# print(f"Asscending Array : {arr_s}")
# des_arr = arr_s[::-1]
# print(f"Descending Array : {des_arr}")

#        **** filter ****

# arr = np.array([10,90,333,4,67,9,5])
# print(arr)
# arr_f = arr[arr < 90]
# print(arr_f)
# arr_f = arr[arr % 2  == 0]
# print(arr_f)



#       ***** Fancy Indexing *****

# arr = np.array([1,2,13,4,7,19,5])
# print(arr)
# arr_f = arr[[0,2]]              # --> [1,13]
# print(arr_f)


# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr , arr.ndim)
# arr_f = arr[[1 ,0,2]]
# print(arr_f)


#        ***** np.where *****
# arr = np.array([1,2,130,4,70,19,5])
# print(arr)
# arr_w = np.where(arr > 40 , "True" , "False")   # condition : True_condition  : False_condition
# print(arr_w)
# arr_w = np.where(arr > 40 , arr+2 , arr-2)      # condition : True_condition  : False_condition
# print(arr_w)
# arr_w = np.where(arr > 40)      # condition : True_condition  : False_condition
# print(arr_w)
# arr_w = np.where(arr % 2 == 0)      # condition : True_condition  : False_condition
# print(arr_w)


# arr2 = np.array([[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]])

# arr_w = np.where(arr2 > 5)
# print(arr_w)
# """ (array([1, 2, 2, 2]), array([2, 0, 1, 2]))
#      ( rows , coloumn) like above condition
#      1 line means (1,2)
#                   (2,0)
#                   (2,1)
#                   (2,2)
# """


#     ***** Concatenate *****
arr1 = np.array([10,20,30])
arr2 = np.array([1,2,3])
arr1_arr2 = np.concatenate((arr1,arr2))  # Concatenate meethod
print(arr1_arr2)

# 2D
arr1 = np.array([[10,20,30],[40,50,60]])
arr2 = np.array([[1,2,3],[4,5,6]])
arr1_arr2 = np.concatenate((arr1,arr2))  # Concatenate meethod
print(arr1_arr2)    # default axis = 0 --> rows wise concatenate
arr1_arr2 = np.concatenate((arr1,arr2), axis = 1)  # Concatenate meethod
print(arr1_arr2)    # axis = 1  --> coloumn wise concatenate

"""axis = 0 --> it will concatenate it in rows
   axis = 1 --> it will concatenate it in Coloumn
"""



"""**Statistical Functions**


1. np.sum(a)
   -> Sum of all elements
 
2. np.mean(a)
   -> Average = Sum of elements / Number of elements
 
3. np.median(a)
   -> Middle value after sorting
 
4. np.min(a)
   -> Smallest value in array
 
5. np.max(a)
   -> Largest value in array
 
6. np.var(a)
   mean,difference,square,average | (sum = ddof) -> divide by array length
 
7. np.std(a)
   -> Standard Deviation = √Variance
   -> Measures spread of data
 
8. np.prod(a)
   -> Multiplication of all elements
 
9. np.cumsum(a)
   -> Cumulative (running) sum
 
10. np.cumprod(a)
    -> Cumulative (running) product
 
11. np.argmin(a)
    -> Index position of minimum value
 
12. np.argmax(a)
    -> Index position of maximum value
 
13. np.abs(a)
    -> Converts negative values to positive
    -> Absolute value (distance from zero)
 
14. np.unique(a)
    -> Returns unique values only
    -> Removes duplicates
 
15. np.percentile(a, 50)
    -> Finds percentage-based value
    -> 50th percentile = Median
 
16. np.quantile(a, 0.5)
    -> Similar to percentile
    -> 0.5 = 50%
 
17. np.ptp(a)
    -> Range = Max - Min
 
28. np.any(a)
    -> True if at least one value is True

    
 """