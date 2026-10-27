import numpy as np

from main import index

# arr=np.array([50,20,40,10,30])
# print(np.sort(arr)[::-1])

# arr=np.array([50,20,40,10,30])
# print(np.sort(arr)[::1])

# arr=np.array([50,20,40,10,30])
# print(np.sort(arr)[0: ])

#
# arr=np.array([50,20,40,10,30])
# print(np.argsort(arr))
# index=np.argsort(arr)
# print(index)

# arr=np.diag([5,10,15])
# print(arr)
#
# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# print(np.diag(arr))
#
# arr=np.tri(2,3)
# print(arr)
# arr=np.arange(11,1,-2)
# print(arr)
#
# arr=np.linspace(1,10,6)
# print(arr)
#
# arr=np.logspace(1,3,3) #Creates numbers evenly spaced on a logarithmic scale.
# print(arr)
#
# arr = np.geomspace(1,1000,5)
# print(arr)


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


arr=np.array([10,20,30,40,50])
# print(arr[~(arr>=30) & (arr<50)])
np.random.seed(90)
print(np.random.randn(2,3))
print(np.random.random(5))


colors=["Red","Blue","Green","Black"]
print(np.random.choice(arr,3))

arr=np.array([1,2,3,4,5])
np.random.shuffle(arr)
print(arr)
print(arr[index])


arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)
# Return a new shuffled array copy
shuffled_arr = np.random.permutation(arr)
print(shuffled_arr)

# np.random.normal(mean,std,size)
# Generate 5 random numbers from a distribution with mean=0 and std=1
# samples = np.random.normal(0, 1, 5)
# print(samples)

# np.random.rand(5)
print(np.random.rand(5))


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


arr = np.array([
    [10,20,30],
    [40,50,60]
])

print(arr)

np.save("numbers1.npy", arr)
print("Array Saved")

arr1 = np.load("numbers1.npy")
print(arr1)

arr = np.array([10,20,30,40])
np.savetxt("data1.txt", arr)
print("Array Saved")
arr1 = np.loadtxt("data1.txt")
print(arr1)

arr = np.array([10,20,30,40])

np.savetxt("data1.csv", arr)
print("Array Saved")

arr1 = np.loadtxt("data1.csv")
print(arr1)

arr = np.array([10,20,30,40])

# np.genfromtxt("data2.csv", delimiter="," , filling_values=0)
# print("Array Saved")
# print(np.genfromtxt("data1.csv" , delimiter="," , missing_values="x"))
# # Load structured data safely
# data_array = np.genfromtxt("data1.csv", names=True, dtype=None, encoding="utf-8")
# print("array saved")

# np.genfromtxt("data1.csv", names = True, dtype = int , encoding="utf-8")


arr = np.array([10,20,30,40])
np.savetxt("my_data.csv", arr, delimiter=",", fmt="%d")
print(np.genfromtxt("my_data.csv"))

A = np.array([[4, 7],
              [2, 6]])
rank_A = np.linalg.matrix_rank(A)
print(rank_A)






