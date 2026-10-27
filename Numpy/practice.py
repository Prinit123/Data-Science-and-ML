# import numpy as np
#
# # arr = np.array([1,2,3,4,5])
# # print(arr)
# #
# # a = np.array([1,2,3,4,5])
# # b = np.array([1,2,3,4,5])
# # print(a+b)
#
# b = np.array([1, 2, 3, 4, 5])
# a = np.array([
#     [[1,2,3,4,5],
#     [5,6,7,8,9]],
#
#     [[1,2,3,4,5],
#      [5,6,7,8,9]]
# ])
# print(a+b)
# arr = np.array([1,2,3,4,5],ndmin=5)
# print(arr.shape)
# print(arr)
#
# arr = [1,2,3,4,5]
# print(arr)
# # arr = np.array([1,2,3,4,5])
# arr1 = np.asarray(arr)
# print(arr1)
# print(type(arr1))
#
#
#
# array_3d = np.array([
#     [
#         [1,2],            # Block 0 (Matrix 0),
#         [3, 4]
#     ],
#     [   [5,6],            # Block 1 (Matrix 1),
#         [7, 8]
#     ]
# ])
# arr = np.array([1,2,3,4,5])
# # print(arr[0])
# # print(arr[1])
# # print(arr[2])
#
# # print(len(arr))
#
# # for r in range(len(arr)):
# #     print(arr[r])
#
# # for r in arr:
# #     print(r)
#
# # print(array_3d.shape)
#
# arr = np.array([
#   [
#     [1,2,3,4,5],
#     [5,6,7,8,9]
# ],
#     [
#     [1,2,3,4,5],
#     [5,6,7,8,9]
# ]
# ])
# arr = np.array([
#     [1,2,3,4,5],
#     [5,6,7,8,9]
# ])
# print(arr.shape)
# # print(arr)
# # print(type(arr))
# # print(arr.size)
# # print(arr[0][0])
# # print(len(arr))
#
# for r in range(len(arr)):
#     for j in range(len(arr[r])):
#         print(arr[r][j])
#
# # What len(arr) Counts
# # 1D array in The total number of individual elements
# # in 2D array in The number of rows only
# # print(arr[0][0])
#
# #nagative Indexing
# arr = np.array([1,2,3,4,5])
# print(arr[-1])
# print(arr[-2])
#
# arr = np.array([1,2,3,4,5])
# print(arr[1:3])
#
# arr = np.array([10,20,30,40,50])
# print(arr[arr>30])
#
#


import numpy as np
from numpy import dtypes
from numpy.ma.core import ndim

# get the dimensions of an array is arr.shape
# which returns a tuple of integers representing the size of the array along each axis

arr=np.array(
    [[1,2,3],
    [4,5,6]]
)
print(arr)
print(arr.shape)

arr = np.array([[[1,2,3],[4,5,6]]])
print(arr.shape)
arr = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[1, 2, 3],
     [4, 5, 6]]
])
print(arr.shape)

arr = np.array([
[
    [[1, 2, 3],
     [4, 5, 6]],

    [[1, 2, 3],
     [4, 5, 6]]
],
[
    [[1, 2, 3],
     [4, 5, 6]],

    [[1, 2, 3],
     [4, 5, 6]]
]
])
print(arr.shape)

# convert an input to an array is np.asarray()

list=[10,20,30]
#  CORRECT: Pass the list into the function
arr=np.asarray(list)
print(arr)

tuple=(10,20,30)
arr=np.asarray(tuple)
print(arr)

# arr = np.array([1,2,3,4,5])
# arr1 = np.asarray(arr)
# print(arr1)

arr = np.array([10,20,30])
arr1 = (np.array([10,20,30]))
print(arr is arr1)



# # Secial Array Creatio  Function

# =====================================================================
# 1. CONSTANT VALUES
# =====================================================================
# zeros(): Array of 0s
arr = np.zeros((2, 3))
print("--- zeros() ---\n",arr)

# ones(): Array of 1s
arr = np.ones((3, 3),dtype=int)
print("\n--- ones() ---\n", arr)

# full(): Array filled with a custom constant (e.g., 7)
arr = np.full((2, 2),7)
print("\n--- full() ---\n", arr)


# =====================================================================
# 2. NUMERICAL SEQUENCES
# =====================================================================
# arange(): Sequences with a defined step size (start, stop, step)
range_arr = np.arange(10, 20, 2)
print("\n--- arange() ---\n", range_arr)


# The primary difference is that np.arange depends on step size, while np.linspace depends on the number of elements.

# linspace(): Defined number of elements evenly split between a range
linear_arr = np.linspace(1, 10, 5)
print("\n--- linspace() ---\n", linear_arr)


# =====================================================================
# 3. IDENTITY MATRICES   // # diagonal  matrix
# =====================================================================
# eye() / identity(): Diagonal 1s, others 0
# identity_matrix = np.eye(2,3)
# print("\n--- eye() ---\n", identity_matrix)

# diagonal but always in square
# identity_matrix = np.identity(2)
# print("\n--- eye() ---\n", identity_matrix)
#

# arr=np.diag([5,10,15])
# print(arr)

# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# print(np.diag(arr))

# arr=np.tri(3,3)
# print(arr)

# =====================================================================
# 4. UNINITIALIZED DATA
# =====================================================================
# empty(): Fast allocation, but contains random "garbage" memory values
# empty_arr = np.empty((2, 5))
# print("\n--- empty() ---\n", empty_arr)


# # copy vs views
# copy = use for copy arr but if i adited first arr so not any change in second copy arr
#view = use for copy arr but if i adited first arr so change in second arr togather



# loop in numpy

# arr=np.arange(2,11,2)
# print(arr)

# arr=np.linspace(0,10,6)
# print(arr)

# arr=np.logspace(1,3,3) #Creates numbers evenly spaced on a logarithmic scale .
# print(arr)

# geometric progression //   # geomspace -Creates numbers spaced using a geometric progression.
# arr = np.geomspace(1,1000,5)
# print(arr)

# generate an array representing the grid indices of a shape
# meshgrid()  - for ploating
# indices()  - for row and colum inses

# Generates row and column coordinate indexes for a 2x3 matrix

# The main difference is that np.meshgrid builds a coordinate grid out of pre-existing coo
# rdinate arrays that you provide, while np.indices builds a coordinate grid automatically based solely on a
# matrix shape size starting from zero


# (row_indices ,col_indices) = np.indices((4, 3))
#
# print("Row Indices Matrix:")
# print(row_indices)
#
# print("\nColumn Indices Matrix:")
# print(col_indices)



x_axis = np.array([0, 4, 7])
y_axis = np.array([0, 34])

# Generate coordinate grids
X, Y = np.meshgrid(x_axis, y_axis)

print("X Grid Coordinates:\n", X)
print("\nY Grid Coordinates:\n", Y)


# 1. np.meshgrid: Uses custom data values
# Useful for evaluating mathematical functions on specific coordinates

x_values = np.array([10, 20, 30])  # Custom X values
y_values = np.array([0.5, 1.5])     # Custom Y values

# X and Y elements at identical row-column indexes
# there is copy data for required
X, Y = np.meshgrid(x_values, y_values)

print("--- np.meshgrid (Custom Grid) ---")
print("X coordinates:\n", X)
print("Y coordinates:\n", Y)


# x_axis = np.array([0, 4, 7])
# y_axis = np.array([0, 34])
#
# # Generate coordinate grids
# X, Y = np.meshgrid(x_axis, y_axis)
#
# print("X Grid Coordinates:\n", X)
# print("\nY Grid Coordinates:\n", Y)


# 2. np.indices: Generates row/column array indices automatically
# Useful for image processing or pixel masking based on matrix shape

# grid_shape = (2, 3)  # Rows, Columns
# row_indices, col_indices = np.indices(grid_shape)
#
# print("\n--- np.indices (Matrix Positions) ---")
# print("Row indices (I):\n", row_indices)
# print("Column indices (J):\n", col_indices)

# (row_indices ,col_indices) = np.indices((4, 3))
#
# print("Row Indices Matrix:")
# print(row_indices)
#
# print("\nColumn Indices Matrix:")
# print(col_indices)


# np.meshgrid is used for plotting coordinate math functions, while np.indices is used for indexing matrix cells.



# Array Attributes
'''
data type :-
ndim :- find dimationl matrix 1D , 2D , 3D...
shape :-  the shape attribute returns a tuple of integers that represents the number of elements along each dimension (or axis) of an array.
size :- size refers to the total number of elements contained within an array.
dtype :-  a special object that defines the exact type of data stored inside an array and how memory bytes are interpreted
itemsize :- 
ndim shape size dtype itemsize nbytes strides T flags
'''


# dtype defines the data type and precision of individual elements,
# while nbytes measures the total memory consumed by all elements combined

#64 bits is exactly equal to 8 bytes
# 1 byte is always equal to 8 bits

# a = np.array([
#     [[1,2],[3,4]],
#     [[5,6],[7,8]]
# ])
# a = np.array([[10, 20, 30],
#                 [40, 50, 60]])
# print(a.ndim)
# print(a.shape)
# print(a.size)
# print(a.dtype)
# print(a.itemsize)
# print(a.nbytes)

# arr.flags is a special object that displays information
# about how an array's data block is arranged and handled in your computer's memory.

'''
| Flag Name      | Short Key | Description |
| :---           | :---      | :--- |
| `C_CONTIGUOUS` | `C`       | **True** if data is stored in row-major order (standard Python/C layout). |
| `F_CONTIGUOUS` | `F`       | **True** if data is stored in column-major order (Fortran layout). |
| `WRITEABLE`    | `W`       | **True** if you can change elements. **False** if the array is read-only. |
| `ALIGNED`      | `A`       | **True** if data alignment matches hardware architecture perfectly. |
| `OWNDATA`      | `O`       | **True** if the array owns its memory block. **False** if it's a view/slice. |
'''
# Use np. when calling functions belonging to the library, and
# arr. when inspecting properties or running methods belonging to your specific dataset.

# 1. Base Array
arr = np.array([[10, 20], [30, 40]])
print("--- Base Array Flags ---")
print("Owns Data:", arr.flags.owndata)       # True
print("Writeable:", arr.flags.writeable)     # True
print("C Contiguous:", arr.flags.c_contiguous) # True

# 2. Creating a View (Slicing)
view_arr = arr[:, 1]
print("\n--- Slice/View Array Flags ---")
print("Owns Data:", view_arr.flags.owndata)  # False (it points to arr)

# 3. Transposing (Flipping layout layout)
transposed = arr.T
print("\n--- Transposed Array Flags ---")
print("C Contiguous:", transposed.flags.c_contiguous) # False
print("F Contiguous:", transposed.flags.f_contiguous) # True




# row_indices, col_indices = np.indices((3, 3))
#
# print("Row Indices Matrix:")
# print(row_indices)
#
# print("\nColumn Indices Matrix:")
# print(col_indices)

# 0Fancy Indexig
# Unlike standard slicing, fancy indexing always returns a copy of the data, not a view.


# x_axis = np.array([0, 4, 7])
# y_axis = np.array([0, 34])

# # Generate coordinate grids
# X, Y = np.meshgrid(x_axis, y_axis)

# print("X Grid Coordinates:\n", X)
# print("\nY Grid Coordinates:\n", Y)


# arr=np.array([10,20,30,40])
# print(arr.ndim)
#
# arr = np.full((3, 2),7)
# print("\n--- full() ---\n", arr)

#lecture 4

# arr = np.array([5,12,18,25,30])
# print(arr[arr%2==0])

# data extraction techniques in NumPy:

# 0Fancy Indexig
# fancy indexing allows you to grab non-consecutive elements in any arbitrary order,
# and it always returns a copy of the data rather than a view.

# # array[start:stop:step]
arr=np.array([10,20,30,40,50])
print(arr[[0,2,4]])
index=[3,0,2]
print(arr[index])


X = np.array([[1,  2,  3],
              [10, 11, 12]])

# Select row 0, row 3, and row 1
rows = X[[0, 1, 0]]


# ex 1
y = np.zeros(5)
target_indices = [1, 2, 4]
y[target_indices] = 99
# Returns: array([ 0., 99., 99.,  0., 99.])

# print(arr[1:4])

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

# arr[row_slice, column_slice]
# a[1:5]
print(arr[0:3,1:3])
# print(arr[::-1,1:3])

# arr = np.array([10,20,30,40,50])
# arr[1:4] = [100,200,300]
# print(arr)



# arr = np.array([10,20,30,40,50])
#
# for  i in arr:
#     print(i)

arr = np.array([
    [10,20,30],
    [40,50,60]
])

for row in arr:
    for value in row:
        print(value)

# arr=np.array([10,20,30])
#
# for index,value in np.ndenumerate(arr):
#     print(index,value)
# This code loops through a NumPy array and prints both the index and the value of each element simultaneously.
#
#


# np.nditer()

#
# arr = np.array([23,34,45,67,89])
# for i in np.nditer(arr):
#     print(i, end=' ')


a = np.array([1, 2, 3, 4])
a[0]=78
result = np.empty_like(a)
print(result)
print(np.shares_memory(a,result))


# exersize for slicing
arr = np.array([[1,2,3],
 [4,5,6],
 [7,8,9]]
)
print(arr[0])
# q3.
# print(arr[::-1])
# q4.
# print(arr[1:3])
# q5
# print(arr[::2])
# q6.
#[::2] extracts all even-indexed rows (0, 2, 4, 6...).
#[1::2] extracts all odd-indexed rows (1, 3, 5, 7...).
# [start: stop:step]
# 1 (Start): Tells NumPy to begin extracting at row index 1.
# : (Stop): Left blank, meaning it goes all the way to the end of the array.
# 2 (Step): Tells NumPy to jump forward by 2 slots each time
# print(arr[1::2])
#
# print(arr[:,::-1])
# print(arr[:,0::2])


# lecture 5

# flat =  The flat property in NumPy returns a 1D iterator object (numpy.flatiter) over the entire array.

# .flat: A NumPy-specific attribute that creates a 1D iterator over an array.
#  for loop: A built-in Python tool used to execute code repeatedly.

arr = np.array([[10,20],
               [30,40]])
print(arr.flat)
for i in arr.flat:
        print(i)

# .flatten

# arr = np.array([[10,20],[30,40]])
# arr1 = arr.flatten()
# print(arr1)


# .flat does not allocate memory for a new array; it steps through elements one by one.
# ravel() returns a 1D view (or copy) of the array.

# arr = np.array([[10,20],[30,40]])
# arr1 =arr.ravel()
# print(arr1)
# print(arr)

#The correct choice is A. ravel() returns a view that shares memory,
# while flatten() returns a distinct copy.
# The fundamental difference between these two NumPy methods
# lies in how they handle computer memory and data duplication


# arr = np.array([[10,20],[30,40]])
# print(arr.shape)
# print(arr.reshape(4,1))


# arr=np.array([1,2,3,4,5,6])
# print(arr)
# new_arr=arr.reshape(3,2)
# print(new_arr)
#
# arr = np.arange(1,9)
# print(arr)
# print(arr.reshape(2,2,2))

# We use np. because it refers to the NumPy library module,
# while arr. refers to a specific array object instance that you created

# arr = np.arange(12)
# print(arr.reshape(3,-1))
#
# arr = np.array([1,2,3,4])
# print(np.resize(arr,(3,4)))

arr=np.array([
[10,20,50],
[30,40 ,60]
])

print(arr.transpose())

# ex.1
# arr = np.array([[5, 10], [15, 20]])
# a = arr.ravel()
# b = arr.flatten()
# a[0] = 99
# b[1] = 88
# print(arr[0])

# arr = np.arange(12)

# ex2.
#A: arr.reshape(3, -1)
# B: arr.reshape(-1, 6)
# C: arr.reshape(5, -1)
# D: arr.reshape(-1, 1)

# ex3.

# lecture 6

arr=np.array([
[10,20,50],
[30,40 ,60]
])

print(arr.transpose())


# Original Array: The array arr is created with a shape of (1, 2, 6)
# .Swapping Axes: The function np.swapaxes(arr, 0, 1) interchanges the first axis (axis 0, size 1)
# with the second axis (axis 1, size 2).Resulting Shape: This shifts the array's dimensions,
# transforming the original shape from (1, 2, 6) into a new shape of (2, 1, 6)

arr=np.array([[[1,2,3,4,5,6],
             [10,20,30,40,50,60]]])
result =np.swapaxes(arr,0,1)
print(result)

arr = np.array([[10,20,30],[40,50,60]])
print(arr)

# result =np.swapaxes(arr,0,1)
# print(result)
#
# np.moveaxis(arr, source, destination)

# result = np.moveaxis(arr,0,1)
# print((result))

print(arr.shape)
result = np.expand_dims(arr,axis=0)
print(result.shape)

result = np.squeeze(arr)
print(result.shape)

# lecture 7

# Joining Arrays
#
# a = np.array([1,2,3])
# b = np.array([4,5,6])

a = np.array([[1,2,3],
             [4,5,6]])
b = np.array([[7,8,9],
             [10,11,12]])

a=np.array([1,2,3])
b=np.array([4,5,6])

print("Concatenate ")
# work as = Join a sequence of arrays along an existing axis.
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
# The rule: The arrays must have the exact same number of columns. for axis = 0
# np.concatenate((a, b), axis=0)
# The rule: The arrays must have the exact same number of rows. for axis = 1
# np.concatenate((a, b.T), axis=1)
#When you set axis=None, NumPy automatically flattens all the input arrays into flat,
#one-dimensional (1D) streams of numbers before gluing them together end-to-end.
# np.concatenate((a, b), axis=None)

#stack((a,b))
#work as = Join a sequence of arrays along a new axis.
#must be same shape in stack function
#swap shape in depending in axis
# a = np.array([[[1, 2], [3, 4]]])
# b = np.array([[[5, 6], [7, 8]]])
# c = np.stack((a,b),axis=0)
# c = np.stack((a,b),axis=1)
# c = np.stack((a,b),axis=2)
# c = np.stack((a,b),axis=-1)
# print(c)
# print(c.shape)

# vstack
#Stack arrays in sequence vertically (row wise).
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.vstack((a,b)))
#
# a = np.array([[1], [2], [3]])
# b = np.array([[4], [5], [6]])
# print(np.vstack((a,b)))

#hstack
# Stack arrays in sequence horizontally (column wise).
#use in tuple
# a = np.array((1,2,3))
# b = np.array((4,5,6))
# print(np.hstack((a,b)))
#
# a = np.array([[1],[2],[3]])
# b = np.array([[4],[5],[6]])
# print(np.hstack((a,b)))


#dstack
#Stack arrays in sequence depth wise (along third axis).
# # use in tupale
# a = np.array((1,2,3))
# b = np.array((4,5,6))
# print(np.dstack((a,b)))
#
# a = np.array([[1],[2],[3]])
# b = np.array([[4],[5],[6]])
# print(np.dstack((a,b)))

# np.column_stack()
#Stack 1-D arrays as columns into a 2-D array.
# just like with hstack
#use tuple
# a = np.array((1,2,3))
# b = np.array((4,5,6))
# np.column_stack((a,b))

#block()
# Assemble an nd-array from nested lists of blocks.

# A=np.array([[1,2],
#             [3,4]])
#
# B=np.array([[5,6],
#             [7,8]])
#
# C=np.array([[9,10],
#             [11,12]])
#
# D=np.array([[13,14],
#             [15,16]])
#
# result=np.block([[A,B],[C,D]])
# print(result)


# With a list of depth 1, block can be used as hstack
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# np.block([a, b, 10])             # hstack([a, b, 10])
#output =  ([ 1,  2,  3,  4,  5,  6, 10])
#
# A = np.ones((2, 2), int)
# B = 2 * A
# np.block([A, B])                 # hstack([A, B])
# output = ([[1, 1, 2, 2],
#        [1, 1, 2, 2]])

# With a list of depth 2, block can be used in place of vstack:
# A = np.ones((2, 2), int)
# B = 2 * A
# np.block([[A], [B]])
#  output = ([[1, 1],
#        [1, 1],
#        [2, 2],
#        [2, 2]])

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# np.block([[a], [b]])

# output = ([[1, 2, 3],
#        [4, 5, 6]])
#
#
# print(np.concatenate([a,b],axis=0))
# print(np.stack((a,b)))
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# print(np.dstack((a,b)))
#
#
# # Splitting Array
#
# #np.split(arr,indices_or_sections: )
#
# arr = np.arange(9)
# print(np.split(arr,3))
#
# arr = np.arange(8)
# print(np.split(arr,[3,5,6,10]))
#
# arr = np.array([
#     [10,20,30,40],
#     [50,60,70,80]
# ])
# result = np.split(arr,2,axis=0)
# print(result)
#
# arr = np.arange(16).reshape(2,2,4)
# print(arr)
# print(np.dsplit(arr,2))
# print(np.split(arr,2))
#
# arr = np.arange(16).reshape(2,2,4)
# print(arr)
# print(np.dsplit(arr,2))
# print(np.split(arr,2))
#
# arr = np.arange(16).reshape(4,4)
# print(arr)
# print(np.hsplit(arr,2))
# print(np.array_split(arr,2))
#
# arr = np.arange(8)
# print(np.split(arr,[3,5,6,10]))
#
# arr = np.array([1,2,3,4,5])
# arr1 = arr[-1]=100
# print(arr)

# Sorting  Array
arr=np.array([50,20,40,10,30])
print(np.sort(arr))
print(np.sort(arr)[::-1])

print(np.argsort(arr))    # write index
index=np.argsort(arr)

print(arr[index])
# Lexsort :- lexsort() performs lexicographical sorting using multiple keys.
# key = values
name=np.array(['Ram',"Dev","Ram","Dev"])
marks=np.array([80,90,100,85])
#
index=np.lexsort((marks,name))
#
print(index)
print(name[index])
print(marks[index])

#axis = 0 :- work on row
#axis = 1 :- work on colume

arr = np.array([
    [30,80],
    [10,60],
    [20,70]
])
print(np.sort(arr,axis=1))

# #While the visual array output is identical,
# # the ( kind ) parameter changes the underlying algorithm,
# # memory consumption, and processing speed.
#
# arr = np.array([20,10,20,30,10])
# print(np.sort(arr,kind="stable"))
# # print(np.argsort(arr))
# np.sort(arr,kind="quicksort")
# np.sort(arr,kind="mergesort")
# np.sort(arr,kind="heapsort")

# Broadcasting :-Broadcasting is a NumPy mechanism that allows arithmetic operations
# between arrays of different shapes without explicitly copying data.

a=np.array([[1],[2],[3]])
b=np.array([10,20,30])
print(a+b)

arr=np.array([10,20,30])
print(arr+5)

M = np.array([[1, 2, 3], [4, 5, 6]])
A = np.array([[4, 7],
              [2, 6]])

B = np.array([[1, 2],
              [3, 4]])


# # Matrix Multiplication
# # Modern python syntax (@ operator)
result = A @ B
print(result)

scalar_product = np.dot(A, B)
print(scalar_product)

# v = np.array([1, 2])
# w = np.array([3, 4])
# # Cross Product
# # Cross product of two vectors
# vector_product = np.cross(v, w)
# print(vector_product)

# v = np.array([1, 2, 0])
# w = np.array([3, 4, 0])
#
# vector_product = np.cross(v, w)
# print("Cross Product (3D Vector):\n", vector_product)
#
# A = np.array([[4, 7],
#               [2, 6]])
# print(np.linalg.inv(A))

# A = np.array([[4, 7],
#               [2, 6]])
# U, S, Vt = np.linalg.svd(A)
# print(U)

arr = np.array([
    [10,20,30],
    [40,50,60]
])

print(arr)
np.save("numbers13.txt", arr)
print("Array Saved")
arr = np.load("numbers13.npy")
print(arr)

#txt
arr = np.array([
    [10,20,30],
    [40,50,60]
])
np.savetxt("numbers13.txt",arr)
arrr = np.loadtxt("numbers13.txt")
print(arrr)