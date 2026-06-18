import numpy as np

# arr = np.arange(12)
# up_arr = np.reshape(arr,(3,4))           # array.reshape(new_shape)
# print(up_arr)

# arr1 = np.arange(18)
# up_arr1 = np.reshape(arr1,(2,3,3))       # np.reshape(array, new_shape)
# print(up_arr1 , np.ndim(up_arr1))


# arr = np.arange(12).reshape((3,4))
# up_arr = arr.flatten()                    # flatten()
# up_arr[0] = 100   
"""# IT DOES NOT CHANGE ORIGINAL ARRAY
 BCZ FLATTEN MAKES COPY OF ORIGINAL ARRAY 
 AND THEN WORK ON IT""" 
# print(up_arr)
# print(arr)

# arr1 = np.arange(18).reshape((2,3,3))
# up_arr1 = arr1.flatten()                  # flatten()
# print(up_arr1)


# arr = np.arange(14).reshape((7,2))
# print(arr)
# up_arr = arr.ravel()                    # ravel()
# print(up_arr)

# arr = np.arange(20).reshape((2,2,5))
# print(arr)
# up_arr = arr.ravel()                    # ravel()
# print(up_arr)
# print(arr)

# arr = np.arange(12).reshape((3,4))
# print(arr)
# up_arr = arr.T                            # Transpose --> .T
# print(up_arr)

# arr = np.arange(12).reshape((2,2,3))
# print(arr)
# up_arr = arr.T                           # Transpose
# print(up_arr)


# arr = np.arange(11)
# print(arr)
# up_arr = arr[:3]
# print(up_arr)

# arr = np.arange(16).reshape(8,2)
# print(arr)
# up_arr = arr[:,-1]
# print(up_arr)

arr = np.arange(24).reshape(3,4,2)
print(arr)
# up_arr = arr[0:3,0:2,0:3]
# print(up_arr)
print(arr[0,0,0])
print(arr[2,3,1])

