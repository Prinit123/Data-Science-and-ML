# NumPy (Numerical Python) is a powerful Python library used for numerical computing. It provides support for
# multi-dimensional arrays, mathematical functions, linear algebra, statistics, and many other operations.
# NumPy is the foundation of Data Science, Machine Learning, Artificial Intelligence, and Scientific Computing.
from unittest import result

# import  numpy  as  np
# import = Python keyword to load a library
# numpy =  The exact name of the library you want to load
# as = use for rename
# np = The short nickname (alias) you choose to use

import numpy as np
from numpy.testing import print_coercion_tables

arr=np.array([10,20,30,40])
# print(arr)


# a=np.array([1,
# b=np.array([4,5,6])
# print(a+b)
#
# print(np.__version__)
# print(arr.shape)
#
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr.shape)

arr=np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(arr.shape)
# output :- (2,2,2)
# 2 blocks (or "layers")
# 2 rows per block
# 2 columns per row
#
# arr=np.array([1,2,3,4],ndmin=5)
# print(arr.shape)
# print(arr)
#
# list=[10,20,30]
# arr=np.asarray(list)
# print(arr)
#
# a = np.array([1,2,3])
# b = np.asarray(a)
#
# print(a is b)
#
# # copy vs views
# copy = use for copy arr but if i adited first arr so not any change in second copy arr
#view = use for copy arr but if i adited first arr so change in second arr togather

# numbers=(10,20,30,40)
# arr=np.array(numbers)
# print(arr)
#
#
# marks = [
#     [90,85,88],
#     [75,80,79],
#     [95,92,98]
# ]
# arr=np.array(marks)
# print(marks)

# # Secial Array Creatio  Function

# arr=np.zeros(5)
# print(arr)
#
# arr=np.zeros((3,4))
# print(
# #
# arr=np.ones((3,4))
# print(arr)
#
# arr=np.empty((3,4))
# print(arr)

# arr=np.full((3,3),7)
# print(arr)

# diagonal
# matrix
# arr=np.eye(4)
# print(arr)
#
#
# diagonal but always in square
# arr = np.identity(3)
# print(arr)
#
# arr=np.diag([5,10,15])
# print(arr)
#
# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# print(np.diag(arr))
#
#
# arr=np.tri(3,3)
# print(arr)
#
#
# loop in numpy
# arr=np.arange(2,11,2)
# print(arr)
#
#
# arr=np.linspace(0,10,6)
# print(arr)
# arr=np.logspace(1,3,3) #Creates numbers evenly spaced on a logarithmic scale.
# print(arr)

# arr = np.geomspace(1,1000,5)
# print(arr)

# geomspace -Creates numbers spaced using a geometric progression.
# meshgrid()  - for ploating
# indices()  - for row and colum inses

# Array Attributes
arr=np.array([10,20,30,40])
print(arr.ndim)
'''
data type :-
ndim :- find dimationl matrix 1D , 2D , 3D...
shape :-  the shape attribute returns a tuple of integers that represents the number of elements along each dimension (or axis) of an array.
size :- size refers to the total number of elements contained within an array.
dtype :-  a special object that defines the exact type of data stored inside an array and how memory bytes are interpreted
itemsize :- 
ndim shape size dtype itemsize nbytes strides T flags
'''
a = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)

arr = np.array([[10,20,30],
                [40,50,60]])

#arr.strides defines how many bytes you must step in memory to reach the next element along each axis,
# while arr.T creates a transposed view of the array by swapping its dimensions and its strides without copying data
print(arr.strides)
print(arr.T)

# fllags :- flags are attributes that describe properties of an array, such as whether it is writable,
# whether its data is stored in C or Fortran order, and whether it owns its memory
# DataTypes :-



arr=np.array([10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[4])

# Negativee Indexing
print(arr[-1])
print(arr[-2])
print(arr[-3])

arr=np.array([
    [10,20,30],
    [40,50,60]
])
print(arr[0][1])
print(arr[1][2])
# print(arr[0,1])
# print(arr[1,2])

arr = np.array([10,20,30,40,50])
print(arr[arr>30])




# arr = np.array([5,12,18,25,30])
# print(arr[arr%2==0])


# 0Fancy Indexig


# arr=np.array([10,20,30,40,50])
# print(arr[[0,2,4]])
# index=[3,0,2]
# print(arr[index])
#
# # array[start:stop:step]
#
# print(arr[1:4])

# arr = np.array([
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ])
#
# print(arr[::-1,1:3])


# arr = np.array([10,20,30,40,50])
# arr[1:4] = [100,200,300]
# print(arr)


# Array Iteration :- Array Iteration is the process of visiting each element of a NumPy array one by one.
# It is useful for processing, modifying, or displaying array elements.


# arr = np.array([10,20,30,40,50])
#
# for  i in arr:
#     print(i)
#
# arr = np.array([
#     [10,20,30],
#     [40,50,60]
# ])
#
# for row in arr:
#     for value in row:
#         print(value)
#
#
# arr=np.array([10,20,30])
#
# for index,value in np.ndenumerate(arr):
#     print(index,value)
# This code loops through a NumPy array and prints both the index and the value of each element simultaneously.
#
#
# arr = np.array([
#     [10,20],
#     [30,40]
# ])
#
# for index, value in np.ndenumerate(arr):
#     print(index, value)

#     nditer()  with  op_flags,flat,

# np.nditer()  = seperate value

# arr =np.array([34,45,56,67,69])
#
# for i in np.nditer(arr):
#     print(i,end=' ')

#with = handling file operations cleanly or if file is open for read so after crashe file is on runing in memory
# but if we use with statment so , after crash or end of read file is closed.
# with = Resource Management

#op_flags = Here is a simple example showing how op_flags is used to read
# from one array and write the results into another.
#
# a = np.array([1, 2, 3, 4])

#The code result = np.empty_like(a) creates a new NumPy array with the exact
# same shape and data type as the existing array a, but leaves its memory uninitialized
# np.zeros_like(a) or np.ones_like(a)

#np.zeros_like(a): Returns an array filled with zeros.
# np.ones_like(a): Returns an array filled with ones.
# np.full_like(a, fill_value): Returns an array filled with a custom value

# result = np.empty_like(a)
# result[0]=78
# print(result)

# ex . of To make result a view of a (so they share the exact same memory),
# you must assign it using slicing or the .view() method instead of np.empty_like(a).

#You can explicitly check if a variable is a view or a copy using
# the .base attribute or np.shares_memory()
a = np.array([1, 2, 3, 4])
a[0] = 78

# Use slicing [:] to create a view that shares the same memory
result = a[:]

# Modifying 'result' will now automatically change 'a'
result[1] = 99

print("result:", result)  # Output: [78 99  3  4]
print("a:", a)            # Output: [78 99  3  4]

#ex . 2 for cheack copy and view
# if false means not same memory share or if true so , share memory


arr = np.array([10, 20, 30, 40, 50])

# 1. Slice (View)
my_view = arr[1:4]
print(my_view.base is arr)          # Returns: True (It shares memory)
print(np.shares_memory(arr, my_view)) # Returns: True

# 2. Fancy Indexing (Copy)
my_copy = arr[[1, 2, 3]]
print(my_copy.base is arr)          # Returns: False (Independent memory)
print(np.shares_memory(arr, my_copy)) # Returns: False



# # 3. Use op_flags to define what each array does
# #    source -> ['readonly']
# # #    result -> ['writeonly']
# with np.nditer([a, result], op_flags=[['readonly'], ['writeonly']]) as it:
#     for x, y in it:
#         y[...] = x ** 2  # Square x and save it into y
#
# print("Original:", a)
# print("Squared: ", result)


# flat = The flat property in NumPy returns a 1D iterator object (numpy.flatiter) over the entire array.

#You cannot print .flat directly to see the data because it is just a memory pointer engine for loops.
# It does not create a new array or allocate a new block of memory. Instead, it lets you loop
# through or modify every single element o
# f a multidimensional array sequentially as if it were a flat, 1D array.

# arr = np.array([[10, 20],
#                 [30, 40]])
#
# print(arr.flat)
# for i in arr.flat  :
#     print(i)
#
# arr = np.array([[10,20],[30,40]])
# arr1 = arr.flatten()
# print(arr1)
#
#
# arr=np.array([
#     [10,20,30],
#     [40,50,60]
# ])
# print(arr)
# print(arr.shape)

# np.ravel()
#.flat returns a numpy.flatiter object, while ravel() returns a standard numpy.ndarray
# .flat does not allocate memory for a new array; it steps through elements one by one.
# ravel() returns a 1D view (or copy) of the array.

# ravel() creates a real, functional 1D array that you can print, slice, or perform math on.

# arr=np.array([1,2,3,4,5,6])
# print(arr)
# new_arr=arr.reshape(3,2)
# print(new_arr)

# arr=np.arange(1,9)
# print(arr)
# print(arr.reshape(2,2,2))
#
# arr=np.arange(12)
# print(arr.reshape(3,-1))

# arr=np.array([1,2,3,4])
# print(np.resize(arr,(3,3)))



# arr=np.array([
# [10,20],
# [30,40]
# ])
#
# print(arr.flatten())   #= work as a copy  , convert  to copy in  1d array
# # print(arr.shape)
# print(arr.ravel())      #= work as a view  ,  creates a new array object that looks at the same memory
#                                                  block as the original array without copying it
# # # raval()
#
#
# arr=np.array([
# [10,20,50],
# [30,40 ,60]
# ])
#
# print(arr.transpose())
# arr=np.array([[[1,2,3,4,5,6],
#              [1,2,3,4,5,6]]])
arr = np.array([[10,20,30],[40,50,60]])
print(arr)
result =np.swapaxes(arr,0,1)
print(result)
# result = np.moveaxis(arr,0,1)
# print((result))
# result = np.expand_dims(arr,axis=0)
# print(result.shape)
# result = np.squeeze(arr) # use gor uper dimenation than 2d not work on 2d
# print(result)



# Swapaxes()  = : Interchanges two specific axes of an array.
#                   np.swapaxes(arr, 0, 1)
#                ifs (2,6) convertor (6,2)

# moveaxis() = Moves an axis (or multiple axes) from an old position to a new position.
#                  np.moveaxis(arr, source, destination)

#expad_dims() = : Adds a new axis (dimension) of size 1 to an array at a specified position.
#                   np.expand_dims(arr, axis=0)
#                   axis=1 would insert the dimension in the middle, changing the shape to (2, 1, 6).
#                   axis=2 (or axis=-1) would insert it at the very end, changing the shape to (2, 6, 1).

# squeeze() = : Removes dimensions of size 1 from an array.
#                   Drop ALL size-1 dimensions   , result = np.squeeze(arr)
#                   Drop only a specific size-1 dimension (e.g., axis 0)  , np.squeeze(arr, axis=0)

# import numpy as np
#
# arr=np.arange(1,7)
#
# print("Original")
# print(arr)
#
# print("\nReshape")
# print(arr.reshape(2,3))
# #
# print("\nResize")
# print(np.resize(arr,(3,3)))
# #
# print("\nFlatten")
# print(arr.reshape(2,3).flatten())
# #
# print("\nRavel")
# print(arr.reshape(2,3).ravel())
#
# print("\nTranspose")
# a=np.array([[1,2,3],[4,5,6]])
# print(a.T)
# #
# print("\nExpand Dims")
# print(np.expand_dims(arr,axis=0))
#
print("\nSqueeze")
b=np.array([[[1,2,3]]])
print(np.squeeze(b))



# Joining Arrays


# concatenate()
# stack()
# vstack()
# hstack()
# dstack()
# column_stack()
# row_stack()
# block()

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


print(np.concatenate([a,b],axis=0))
print(np.stack((a,b)))
print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(np.dstack((a,b)))


'''
| Function         | Purpose                            | Result Shape                 |
| ---------------- | ---------------------------------- | ---------------------------- |
| `concatenate()`  | Join arrays along an existing axis | Depends on `axis`            |
| `stack()`        | Join arrays by creating a new axis | Dimensions increase          |
| `vstack()`       | Stack vertically (rows)            | `(rows, columns)`            |
| `hstack()`       | Stack horizontally (columns)       | Columns increase             |
| `dstack()`       | Stack along the third (depth) axis | 3D array                     |
| `column_stack()` | Convert 1D arrays into columns     | 2D array                     |
| `row_stack()`    | Stack arrays row-wise              | Same as `vstack()`           |
| `block()`        | Assemble arrays like blocks        | Flexible matrix construction |

'''

A=np.array([[1,2],
            [3,4]])

B=np.array([[5,6],
            [7,8]])

C=np.array([[9,10],
            [11,12]])

D=np.array([[13,14],
            [15,16]])

result=np.block([[A,B],[C,D]])
print(result)


# Splitting Array

#np.split(arr,indices_or_section)
#Split an array into multiple sub-arrays of equal size.

arr=np.array([10,20,30,40,50,60])
result=np.split(arr,3)
print(result)


arr = np.arange(9)
print(np.split(arr,3))

arr = np.arange(8)
print(np.split(arr,[3,5,6,10]))

#When you split a NumPy array using np.split(),
# the axis parameter controls the direction of the cut.
# axis = 1 = collum wise .
# axis = 0 = row wise .

arr = np.array([
    [10,20,30,40],
    [50,60,70,80]
])
result = np.split(arr,2,axis=1)
print(result)
arr=np.array([10,20,30,40,50])
result=np.array_split(arr,3)
print(result)
#Split array into multiple sub-arrays along the 3rd axis (depth).
# dspit
# vspilt
# hsplit()
#Split an array into multiple sub-arrays horizontally (column-wise).

'''
| Function        | Purpose                           | Example                 |
| --------------- | --------------------------------- | ----------------------- |
| `split()`       | Split into equal parts            | `np.split(arr,3)`       |
| `array_split()` | Split into equal or unequal parts | `np.array_split(arr,3)` |
| `hsplit()`      | Split columns                     | `np.hsplit(arr,2)`      |
| `vsplit()`      | Split rows                        | `np.vsplit(arr,2)`      |
| `dsplit()`      | Split depth (3D arrays)           | `np.dsplit(arr,2)`      |

'''

# Array searching
# where
# argwhere
# searchsorted
# nonzero
# extract

# Array Searching   = Best Used For                            = Output Type
# where()    = Conditional element selection or index grouping  = Tuple of coordinate arrays
# argwhere()  =  Grouping indices by individual element coordinates = 2D array of element indices
# searchsorted() = Finding insertion points in sorted arrays  =  Array of index locations
# nonzero()   = Finding indices of all non-zero elements   = Tuple of coordinate arrays
# extract()  = Filtering and returning the actual data values   = 1D array of elements


# where()
# Finds indices where a condition is true, or selects elements conditionally based on a truth mask.

# arr = np.array([10,20,30,40],ndmin=3)
# id = np.where(arr>20)
# print(arr[id])

arr = np.array([[10, 0, 30],
                [0,  40, 50]])
# id = np.where(arr>20)
# Usage 2: If true replace with 1, else replace with -1
# replaced = np.where(arr > 20, 1, -1)
# print(replaced)

# 2. argwhere()Finds indices of elements that are non-zero or match a condition, grouped by element rather than by dimension.

# id = np.argwhere(arr > 20)
# print(id)

# 3. searchsorted()Finds the indices where elements should be inserted in a pre-sorted 1D array to maintain its sorted order.
#
# arr = np.array([10, 20, 30, 40, 50])
# idx = np.searchsorted(arr, 35)
# print(idx)
# Output: 3 (because 35 fits between index 2 and index 3)

    # 4. nonzero()Returns the indices of all elements that are not equal to zero. np.nonzero(arr) is completely
# identical to np.where(arr != 0).

# idx = np.nonzero(arr)
# print(idx)
# Output: (array([0, 0, 1, 1]), array([0, 2, 1, 2]))

# 5. extract()Returns the actual data values that meet a condition, flattened into a 1D array instead of returning their index locations

condition = arr > 20
values = np.extract(condition, arr)
print(values)
# Output: [30, 40, 50]



'''
Arithmetic
Addition
Subtraction
Multiplication
Division
Floor Division
Modulus   //reminder
Power
Universal Functions (ufunc)
add()
subtract()
multiply()
divide()
power()
sqrt()
square()
abs()  1
# import numpy as np

arr = np.array([-10, -5, 0, 5, 10])
# Calculate absolute values
result = np.abs(arr)
print(result)
# Output: [10  5  0  5 10]

sign() 2

# import numpy as np
arr = np.array([-999, -5, 0, 4, 852])
# Extract the signs
result = np.sign(arr)
print(result)

16. Statistical Functions
sum()   //Adds all elements together.
mean()   //Computes the arithmetic average (Sum / Count).
median()  // Finds the middle value after sorting the data. (Handles outliers better than mean).

std() //Standard Deviation. Measures how spread out the numbers are.
var() //Variance. The average of the squared differences from the Mean (\(\tex{std}^{2}\)).

min() //Finds the smallest value.
max()  //Finds the largest value.
argmin()  

# import numpy as np
marks = np.array([45, 98, 72, 30, 85])
# Find index of lowest and highest marks
min_idx = np.argmin(marks)
max_idx = np.argmax(marks)
print(f"Lowest mark is at index {min_idx} (Value: {marks[min_idx]})")  # Index 3 (30)
print(f"Highest mark is at index {max_idx} (Value: {marks[max_idx]})") # Index 1 (98)

argmax()
percentile()
quantile()

# import numpy as np
scores = np.array([50, 60, 70, 80, 90, 100])
# Find the 75th percentile (or 0.75 quantile)
p75 = np.percentile(scores, 75)
q75 = np.quantile(scores, 0.75)
print("75th Percentile:", p75)  # Output: 87.5
print("0.75 Quantile:", q75)    # Output: 87.5 (Identical result)

average()

# import numpy as np
# Student marks: [Homework, Midterm, Final Exam]
scores = np.array([90, 80, 70])
weights = np.array([0.2, 0.3, 0.5])  # Must add up to 1.0 (or 100%)
# Weighted average calculation
final_grade = np.average(scores, weights=weights)
print("Weighted Final Grade:", final_grade)  # Output: 77.0

cov()

# import numpy as np
# Study hours vs Exam scores
study_hours = np.array([1, 2, 3, 4, 5])
exam_scores = np.array([50, 55, 70, 80, 95])
# Calculate the covariance matrix
cov_matrix = np.cov(study_hours, exam_scores)
print("Covariance Matrix:\n", cov_matrix)
# The relationship value between the two variables is at position [0, 1]
print("Direct Covariance:", cov_matrix[0, 1])  # Output: 21.25 (Positive trend)

corrcoef()
Trigonometric
sin()
cos()
tan()
arcsin()
arccos()
arctan()

# Input Values: For arcsin() and arccos(), inputs must fall strictly between -1 and 1 (otherwise NumPy returns nan). arctan() accepts any real number.

Exponential
exp()
log()
log10()
log2()
Rounding
round()
floor()
ceil()
trunc()
'''

# Sorting  Array
arr=np.array([50,20,40,10,30])
print(np.sort(arr)[::-1])

print(np.argsort(arr))    # write index
index=np.argsort(arr)

print(arr[index])
# Lexsort :- lexsort() performs lexicographical sorting using multiple keys.
# key = values
name=np.array(['Ram',"Dev","Ram","Dev"])
marks=np.array([80,90,100,85])

index=np.lexsort((marks,name))

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
print(np.sort(arr,axis=0))

#While the visual array output is identical,
# the ( kind ) parameter changes the underlying algorithm,
# memory consumption, and processing speed.

arr = np.array([20,10,20,30,10])
print(np.sort(arr,kind="stable"))
np.sort(arr,kind="quicksort")
#Merge Sort is a divide and conquer algorithm based on the idea of breaking a list
np.sort(arr,kind="mergesort")
#Finally, heap sort is based on comparisons. We can say that it is an improved version of selection sort.
# It actually visualizes the array elements as heap.
#A heap is a tree-based structure
np.sort(arr,kind="heapsort")



# Filteering Arrays

arr=np.array([10,20,30,40,50])
print(arr[~(arr>=30) & (arr<50)])



'''
| Topic               | Function             | Example                      |                     |
| ------------------- | -------------------- | ---------------------------- | ------------------- |
| Sort Array          | `sort()`             | `np.sort(arr)`               |                     |
| Sort Indices        | `argsort()`          | `np.argsort(arr)`            |                     |
| Multi-key Sort      | `lexsort()`          | `np.lexsort((key2,key1))`    |                     |
| Sort Rows           | `axis=1`             | `np.sort(arr,axis=1)`        |                     |
| Sort Columns        | `axis=0`             | `np.sort(arr,axis=0)`        |                     |
| Stable Sort         | `kind="stable"`      | `np.sort(arr,kind="stable")` |                     |
| Boolean Mask        | `arr[condition]`     | `arr[arr>20]`                |                     |
| Conditional Filter  | Comparison operators | `arr[arr>=30]`               |                     |
| Logical Operations  | `&`, `               | `, `~`                       | `(arr>20)&(arr<50)` |
| Multiple Conditions | Combine filters      | `(marks>=40)&(marks<=80)`    |                     |

'''


# Broadcasting :-Broadcasting is a NumPy mechanism that allows arithmetic operations
# between arrays of different shapes without explicitly copying data.

# a=np.array([[1],[2],[3]])
# b=np.array([10,20,30])
# print(a+b)
#
# arr=np.array([10,20,30])
# print(arr+5)



# /random  Module

# # seed() :- seed() generates the same random numbers every time.
# np.random.seed(10)
# print(np.random.randn(2,3))
# # randn :-Generates random numbers from the Standard Normal Distribution.
#

#randn() :- print 0 somthing and positive and negative
# random():- print 1 to 0 print only positive

# np.random.randn   :- generates samples from a standard normal distribution (Gaussian distribution)
# with a mean of 0 and a standard deviation of 1. The values can be positive or negative,
# clustering mostly around

# 0.np.random.random :- generates numbers from a uniform distribution over
# the half-open interval [0.0, 1.0). Every number in this range has an equal chance of being selected,
# and all values are positive

# print(np.random.random(5))
#
#
# colors=["Red","Blue","Green","Black"]
# print(np.random.choice(colors,3))
#
#
# arr=np.array([1,2,3,4,5])
# np.random.shuffle(arr)
# print(arr)

# permutation()
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)
shuffled_arr = np.random.permutation(arr)
print(shuffled_arr)


# np.random.normal(mean,std,size)
# Generate 5 random numbers from a distribution with mean=0 and std=1
# The np.random.normal(loc, scale, size) function generates random numbers
# that follow a normal (bell-shaped) distribution based on three specific
# arguments:
# loc (mean): The center peak of the bell curve where most numbers will cluster.
# scale (std): The standard deviation, which controls how wide or spread out the bell curve is.
# size: The output shape (e.g., an integer for a 1D array, or a tuple like (3, 4) for a 2D matrix)
# if i put 0 to 1 so its similar to .randn
samples = np.random.normal(0, 1, (2,3))
print(samples)

# np.random.uniform(low,high,size)
# The np.random.uniform(low, high, size) function generates random floating-point numbers
# where every value within the specified range has an equally likely chance of being chosen (a uniform distribution).
# low: The lower boundary of the generation interval (inclusive). Defaults to 0.0 if omitted.
# high: The upper boundary of the generation interval (exclusive). Defaults to 1.0 if omitted.
# size: The output shape (e.g.,# np.random.binomial(n,p,size) an integer like 5, or a tuple like (2, 3) for a matrix).
# Generate 5 random floating-point numbers between 10.0 and 20.0
samples = np.random.uniform(10, 20, 5)
print(samples)




# The np.random.binomial(n, p, size) function draws random samples from a binomial distribution,
# which models the number of successes in a sequence of independent binary (yes/no)
# experiments.
# n: The number of trials per experiment (must be an integer >= 0.
# p: The probability of success on any individual trial (must be a float between 0 and 1.
# size: The output shape (e.g., an integer like 5, or a tuple like (2, 3) for a matrix).
# Simulate flipping a fair coin (p=0.5) 10 times (n=10), repeated 5 times
# samples = np.random.binomial(n=10, p=0.5, size=5)
# print(samples)


# np.random.poisson(lam,size)
# Simulate the number of events happening when the average rate (lambda) is 3.5, repeated 5 times
samples = np.random.poisson(lam=3.5, size=5)
print(samples)

# np.random.randn(size)
# print(np.random.rand(5))
# Generate 5 random floats uniformly distributed between 0.0 and 1.0

# | Function        | Purpose                          | Example                        |
# | --------------- | -------------------------------- | ------------------------------ |
# | `seed()`        | Make random results reproducible | `np.random.seed(10)`           |
# | `rand()`        | Random floats (0–1)              | `np.random.rand(2,3)`          |
# | `randn()`       | Standard normal random values    | `np.random.randn(5)`           |
# | `random()`      | Random floats (0–1)              | `np.random.random(5)`          |
# | `randint()`     | Random integers                  | `np.random.randint(1,10,5)`    |
# | `choice()`      | Random selection from data       | `np.random.choice(arr)`        |
# | `shuffle()`     | Shuffle original array           | `np.random.shuffle(arr)`       |
# | `permutation()` | Return shuffled copy             | `np.random.permutation(arr)`   |
# | `normal()`      | Normal (Gaussian) distribution   | `np.random.normal(50,10,5)`    |
# | `uniform()`     | Uniform distribution             | `np.random.uniform(10,20,5)`   |
# | `binomial()`    | Binomial distribution            | `np.random.binomial(10,0.5,5)` |
# | `poisson()`     | Poisson distribution             | `np.random.poisson(5,10)`      |



# Linear Algebra
# Matrix Creation
# Matrix Multiplication
# Dot Product
# Cross Product
# Inner Product
# Outer Product
# Inverse
# Determinant
# Eigen Values
# Eigen Vectors
# Matrix Rank
# Trace
# Matrix Power
# Solve Linear Equations
# Singular Value Decomposition (SVD)


# Here is the direct difference: a vector is a one-dimensional array of numbers representing
# a single point or direction, while a matrix is a two-dimensional grid of numbers used to
# transform vectors or store complex data.


# Linear Algebra

# Linear Algebra is the branch of mathematics that deals with lines,
# planes, and multidimensional spaces, using vectors and matrices
# to solve equations and transform space

# A and B are sample matrices used for the demonstrations below
A = np.array([[4, 7],
              [2, 6]])

B = np.array([[1, 2],
              [3, 4]])

v = np.array([1, 2])
w = np.array([3, 4])


# Matrix Creation
# 2x3 Matrix creation
M = np.array([[1, 2, 3], [4, 5, 6]])

# # Matrix Multiplication
# # Modern python syntax (@ operator)
# # result = A @ B
# # print(result)
# # Alternative method
# # result = np.matmul(A, B)
#
# # Dot Product
# # Dot product of two vectors
# scalar_product = np.dot(v, w)
# print(scalar_product)
#
# # Cross Product
# # Cross product of two vectors
# vector_product = np.cross(v, w)
#
# # Inner Product
# # Calculates the ordinary inner product of two vectors (equivalent to a dot product for real vectors
# result = np.inner(v, w)
#
# # Outer Product
# # Computes the outer product of two vectors, creating a square matrix where # M[i, j] = v[i] * w[j].
#
# # Inverse
# #Computes the multiplicative inverse of a square matrix. Throws an error if the matrix is singular (determinant is zero)
# A_inv = np.linalg.inv(A)
#
# # Determinant
# #Computes the determinant of a square matrix to evaluate invertibility and volume scaling factors
# det_A = np.linalg.det(A)
#
# # Eigen Values  &   # Eigen Vectors
# they simplify complex matrix operations and reveal the most important physical
# or data-driven properties of a system

#Matrix Diagonalization: They are used to turn complex matrices into diagonal matrices,
# which are much easier to work with. This makes calculating high powers of matrices
# (like \(A^{100}\)) significantly faster.
# #Unpacks both the eigenvalues and corresponding normalized eigenvectors simultaneously.
# eigenvalues, eigenvectors = np.linalg.eig(A)
# # eigenvalues[i] pairs with eigenvectors[:, i]
#
# # Eigen Vectors
#
# # Matrix Rank
# #Returns the mathematical rank of a matrix using its Singular Value Decomposition (SVD) method.
# rank_A = np.linalg.matrix_rank(A)
#
# # Trace
# #Returns the sum of the elements along the main diagonal of a matrix
# trace_A = np.trace(A)
#
# # Matrix Power
# #Raises a square matrix to an integer power \(n\) by consecutive matrix multiplication.
# # Multiplies matrix A by itself 3 times (A @ A @ A)
# A_cubed = np.linalg.matrix_power(A, 3)
#
# # Solve Linear Equations
# # Solves exact linear matrix equations system \(Ax = b\) for the unknown vector \(x\).
# b = np.array([5, 8])
# x = np.linalg.solve(A, b)
#
# # Singular Value Decomposition (SVD)
#Think of any linear transformation as a multi-step physical operation on a geometric space
# (like a circle or sphere):
# #Factors a matrix into three constituent matrices:# A = U @ np.diag(S) @ Vt
# U (Left Singular Vectors):
# S (Singular Values)
# Vt (Right Singular Vectors Transposed):
# U, S, Vt = np.linalg.svd(A:)

# # S returns as a 1D array of singular values


# arr = np.array([
#     [10,20,30],
#     [40,50,60]
# ])
#
# print(arr)
#
# np.save("numbers.npy", arr)
# print("Array Saved")

arr=np.load("numbers.npy")
print(arr)
# np.savetxt()

arr=np.array([10,20,30,40])
np.savetxt("data.txt",arr)
# np.savetxt("data.csv",arr,delimiter=",")  #for save data in csv file in int form
print("Saved")
# np.loadtxt()
# np.genfromtxt(file,delimiter=",")#
#The code snippet uses np.genfromtxt() to load data from a text or CSV file into a NumPy array
# arr=np.genfromtxt("marks.csv",delimiter=",")
# arr=np.genfromtxt("marks.csv", delimiter=",", filling_values=0)
# print(arr)

'''
| Function       | Purpose                                    | Example                                      |
| -------------- | ------------------------------------------ | -------------------------------------------- |
| `save()`       | Save a NumPy array to a binary `.npy` file | `np.save("data.npy", arr)`                   |
| `load()`       | Load a `.npy` file                         | `np.load("data.npy")`                        |
| `savetxt()`    | Save an array to a text or CSV file        | `np.savetxt("data.csv", arr, delimiter=",")` |
| `loadtxt()`    | Read data from a text or CSV file          | `np.loadtxt("data.csv", delimiter=",")`      |
| `genfromtxt()` | Read files with missing values             | `np.genfromtxt("data.csv", delimiter=",")`   |
| `.csv` Files   | Store comma-separated text data            | `student.csv`                                |
| `.npy` Files   | Store binary NumPy arrays                  | `array.npy`                                  |
| `.npz` Files   | Store multiple NumPy arrays in one file    | `np.savez("data.npz", a, b)`                 |

'''


# Memory Optimization  :- Memory optimization means using NumPy arrays in a way that consumes less RAM
# and executes operations efficiently.



arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
new_arr = arr[:, ::2]
# print(arr)
# print(arr.flags)
# print(arr.flags["C_CONTIGUOUS"])
# print(new_arr.flags["C_CONTIGUOUS"])

print(arr.nbytes)

a = np.ones(1_000_000, dtype=np.float64)
b = np.ones(1_000_000, dtype=np.float32)

print(a.nbytes)
print(b.nbytes)


# Vectorization means performing an operation on an entire
# NumPy array at once instead of processing individual elements using Python loops.
# import time      #library for called time
# arr = np.arange(1_000_000)
#
# # Python loop
# start = time.perf_counter()
#
# result = []
# for x in arr:
#     result.append(x * 2)
#
# end = time.perf_counter()
#
# print("Loop Time:", end - start)
#
#
# # NumPy Vectorization
# start = time.perf_counter()
#
# result = arr * 2
#
# end = time.perf_counter()
#
# print("Vectorized Time:", end - start)




# Structured Arrays :- A Structured Array allows each array element to contain multiple named
# fields with potentially different data types.

dt=np.dtype([
    ("name", "U20"),
    ("age", "i4"),
    ("marks", "f4")
])

students=np.array([("Manav",24,90.5),
                   ("Raj",21,85.5),
                   ("Prinit",21,99.6)],dtype=dt)
print(students)


employee_type = np.dtype([
    ("id", "i4"),
    ("name", "U30"),
    ("age", "i4"),
    ("salary", "f8"),
    ("active", "?"),
    ("joining_date", "M8[D]")
])

employees = np.array([
    (101, "Amit Patel", 25, 45000.50, True, "2025-01-10"),
    (102, "Neha Shah", 28, 55000.75, True, "2024-06-15"),
    (103, "Raj Mehta", 30, 60000.00, False, "2023-08-20")
], dtype=employee_type)

print(employees)



# Masked Arrays  :- A Masked Array allows certain values to be marked as invalid, unavailable, or ignored.

marks=np.array([80,75,-1,90,-1,85])
masked_marks=np.ma.masked_equal(marks,-1)
print(masked_marks)
print(masked_marks.mean())

arr = np.ma.array([10,20,30,40,50])
result = np.ma.masked_greater(arr,30)
result = result.filled(0)
print(result)

# Date and Time

date = np.datetime64("2026-07-25")

print(date)

dates = np.array([
    "2026-07-25",
    "2026-07-26",
    "2026-07-27"
], dtype="datetime64[D]")

# np.datetime64("2026")               # Year
# np.datetime64("2026-07")            # Month
# np.datetime64("2026-07-25")         # Day
# np.datetime64("2026-07-25T10:30")   # Minute
print(dates)


# duration = dates+np.timedelta64(10, "D")
# print(duration)

'''

| Topic            | Main Purpose                     | Example                     |
| ---------------- | -------------------------------- | --------------------------- |
| Memory Layout    | Understand array storage         | `arr.flags`                 |
| Contiguous Array | Check continuous memory layout   | `arr.flags["C_CONTIGUOUS"]` |
| Memory Usage     | Find element-buffer size         | `arr.nbytes`                |
| Vectorization    | Avoid Python loops               | `arr * 2`                   |
| Structured Array | Store named heterogeneous fields | `arr["salary"]`             |
| Record Array     | Access fields using dot notation | `arr.salary`                |
| Custom dtype     | Define your own record structure | `np.dtype([...])`           |
| Masked Array     | Ignore invalid/missing data      | `ma.masked_equal()`         |
| Mask Operation   | Mask data using conditions       | `ma.masked_greater()`       |
| Fill Values      | Replace masked data              | `arr.filled(0)`             |
| `datetime64`     | Store date/time                  | `np.datetime64()`           |
| `timedelta64`    | Store duration                   | `np.timedelta64()`          |
| Date Arithmetic  | Add/subtract dates and durations | `date + duration`           |

'''


