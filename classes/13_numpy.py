# NumPy in Python is a powerful open-source library used for numerical computing, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

# pip install numpy

# import numpy
# arr=numpy.array([1,2,3,4])
# print(arr)

# import numpy as am
# a=am.array([1,2,3,4])
# print(a)
# import numpy as am
# a=am.array([1,2,3,4,5])
# d=a.copy()
# print(d)

# import numpy as am
# a=am.array([[1,2,3],[4,5,6]])
# for b in range(2):
#     for c in range(3):
#         print(a[b][c],end=" ")
#     print()

# import numpy as am
# a=am.array([1,2,3,4,5,6,7,8])
# d=am.array_split(a,4)
# print(d)


# import numpy as am
# a=am.array([1,2,3,4,5,6,7,8,9,10,11,12])
# d=a.reshape(3,2,2) #split|rows|cols
# print(d)

# import numpy as am
# d=[]
# for b in range(12):
#     b=int(input("enter"))
#     d.append(b)
# a=am.array(d)
# print(a)
# d=a.reshape(3,2,2)
# print(d)

# import numpy as am
# a=am.array([1,2,3])
# b=am.array([1,2,3])
# d=am.concatenate((a,b))
# print(d)

# import numpy as A
# am=A.array([[1,2,3,4],[3,4,5,5],[6,7,8,8]])
# print(am.size)
# print(am.shape)
# print(am.ndim)

# import numpy as A
# am=A.array([[1,2,3,4],[3,4,5,5],[6,7,8,8]])
# print(A.max(am,axis=1))
# print(A.max(am,axis=0))


# import numpy as am
# a=am.array([[1,2,3,4],[3,4,5,5],[6,7,8,8]])
# print(a.T)


# import numpy as am
# a=am.array([[1,2,3,4],[3,4,5,5],[6,7,8,8]])
# print(a.diagonal())
# print(a.trace())


# import numpy as am
# a=am.array([[1,2,3],[3,4,5],[6,7,8]])
# b=am.array([[1,2,3],[3,4,5],[6,7,8]])
# print(am.add(a,b))
# print(am.subtract(a,b))
# print(am.dot(a,b))