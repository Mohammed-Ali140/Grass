import numpy 
# import numpy as np
# from numpy import arange
# from numpy import *

# n = numpy.arange(11)
# print(type(n))
# print(n)
# print(n[0])

#example   -- 2D
# n = numpy.arange(12)
# d = n.reshape(3,4)    # 3 --> Rows and 4 --> Coloumn
# print(type(d))
# print(d)

# example -- 3D
# n = numpy.arange(24).reshape(1,6,4)
# print(n)

n = numpy.arange(12).reshape(4,3)
# print(n) 
print(n[0:1])