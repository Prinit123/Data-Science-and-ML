import numpy as np

# Q1. Create a NumPy array containing numbers from 1 to 10.

arr = np.arange(1, 11)
print(arr)

# Q2. Create a 5×5 array filled with zeros.
a = np.zeros(10)
print(a)
arr = np.zeros((5,5))
print(arr)


# Q3. Create a 4×4 array filled with ones.
arr = np.ones((4,4))
print(arr)

# Q4. Create a 3×3 array filled with the value 15.

arr = np.full((3,3) ,15)
print(arr)


# Q5. Create an identity matrix of size 6×6

arr = np.eye(6,2)
a = np.identity(6)
print(a)
print(arr)

# Q6. Create a lower triangular matrix of size 5×5.

arr = np.tri(5,5)
print(arr)



# Q7. Create an array containing all even numbers from 2 to 20.

arr = np.arange(2 , 20 , 2)
print(arr)

# Q8. Create an array of 8 equally spaced numbers between 10 and 50.

arr = np.arange(10 , 50 , 8)
a = np.linspace(10,50,8)
print(a)
print(arr)

# Q9.Create an array of logarithmic values from 10¹ to 10⁴
arr = np.logspace(1,4 ,4)
# for value find
arr_number = np.log10(arr)
print(arr_number)

# Q10. Create a geometric sequence from 2 to 128 with 7 numbers

arr = np.geomspace(2,128 ,7)
print(arr)

# Level 2 (Array Attributes)

# Create a 3×4 matrix and display:
#
# Number of dimensions
# Shape
# Size
# Data type
# Item size
# Total memory used

arr = np.arange(1 , 13 ).reshape(3,4)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)
print(arr.nbytes)


# Q12.Create a 4×5 matrix and print its transpose.
arr = np.arange(1,21).reshape(4,5)
print(arr.T)

# Q13. Create a 5×5 matrix and display its memory flags
arr = np.arange(1,26).reshape(5,5)
print(arr.flags)



# Q14.Create a view and a copy of an array. Modify both and compare the original array
arr = np.array([1,2,3,4,5,6])
arr_copy = arr.copy()
arr_view = arr.view()
arr_copy[1] = 90
arr_view[0] = 78
print(arr)

# Q15. Display the strides of a 4×4 matrix.

# Definition: Strides represent the number of bytes the computer must step in memory to move to the next element a
# long each axis.The tuple (32, 8):32 (Row stride): To move from one row to the next (e.g., index [0,0] to [1,0]),
# NumPy skips 4 elements. Since each 64-bit integer takes 8 bytes, the jump is 4 × 8 = 32 bytes.8 (Column stride): To move from
# one column to the next (e.g., index [0,0] to [0,1]), NumPy skips 1 element, which takes 8 bytes.

arr = np.arange(16).reshape(4,4)
print(arr.strides)
#output ;- (32 , 8)

# Level 3 (Array Creation)

# Q16.Create a NumPy array from a Python list

list = [12,23,34,45]
arr = np.array(list)
print(arr)

# Q17.Create a NumPy array from a tuple.

tuple = (12,23,34,54)
arr = np.array(tuple)
print(arr)

# Q18.Convert the following nested list into a NumPy array.
# [
#  [5,10,15],
#  [20,25,30],
#  [35,40,45]
# ]

list =  [
 [5,10,15],
 [20,25,30],
 [35,40,45]
]
arr = np.array(list)
print(arr)

# Q19.Create a 5-dimensional array using ndmin

arr = np.array(np.arange(1,5),ndmin = 5)
print(arr)

# Q20.Use asarray() to convert a tuple into a NumPy array.

tuple = (12,23,34,45)
arr = np.asarray(tuple)
print(arr)

# Level 4 (Indexing)

# Use
# arr = np.array([5,10,15,20,25,30,35,40])

arr = np.array([5, 10, 15, 20, 25, 30, 35, 40])
print(arr[1:5])    # Index 1 up to 5 -> [10 15 20 25]
print(arr[::2])    # Every second item -> [ 5 15 25 35]
print(arr[::-1])   # Reverse the array -> [40 35 30 25 20 15 10  5]
print(arr[arr > 25])   #find max number is array as a array
print(arr[[0, 3, 4]])  # Elements at index 0, 3, and 4 -> [ 5 20 25]


# Q26.Print only even numbers using Boolean Indexing.
print(arr[arr%2==0])

# Q27.Print elements located at indices 0, 3, 5, 7 using Fancy Indexing.
index = [0,3,5,7]
print(arr[index])

# Q28.Replace the last element with 100.
arr[-1]=100
print(arr)


# Level 5 (2D Indexing)

# Use

arr = np.array([
[10,20,30],
[40,50,60],
[70,80,90]
])

print(arr[1, 2])  # Row 1, Column 2 -> 60
print(arr[0, :])  # First row    -> [10 20 30]
print(arr[:, 1])  # Second column -> [20 50 80]
print(arr[0:2, 1:3])
# Rows 0 to 1, Columns 1 to 2 -> [[20 30]
#                                [50 60]]
# fancy indexing
print(arr[[0, 2], [0, 2]])  # Corner elements (0,0) and (2,2) -> [10 90]

print(arr[1,:])
print(arr[:,0])

# Q36. Replace 50 with 500

arr[1,1] = 500;
print(arr)

# Level 6 (Slicing)

# Use
arr=np.array([10,20,30,40,50,60,70,80])

# Q37. Print elements from 20 to 60.
arr1 =arr[0:6]
print(arr1)