#List
#Lists are used to store multiple items in a single variable.

#Lists are one of 4 built-in data types in
#Python used to store collections of data,
#the other 3 are Tuple, Set, and Dictionary,
#all with different qualities and usage.
#add difrent variable.

'''
my_list=[12,23,34,"prinit"]
my_number=["prinit","jenish","mohit"]

print(my_list[1])
print(my_list[0])
print(my_list[-1])
print(my_list[0:2])
print(my_list)
print(my_number)
'''

'''
my_num=[12,23,34,54,56]
if 590 in my_num:
           print("yes this 54 in list")
else:
           print("not in list")
'''

#if change element in list
"""
list=[12,23,34,56,67,78]
list[1]=34
print(list)
"""
'''
list=[12,23,34,455,65,56,67,78,98]
list[1:3]=[21,32]
# list[1]=[10]
print(list)'''

# add any item 
'''
list=[12,23,34,56,76,89]
list.append(123)
print(list)
'''
'''
list=[12,23,34,45,56,67]
list.insert(1,143)
print(list)
'''

'''
list=["bannana","appale","chareey"]
lift=["mango","paineppale","pappya"]
list.extend(lift)
print(list)
'''

#remove in list
'''
list=[23,34,45,56,67]
list.remove(23)
print(list)
'''

#remove specified index

'''
list=[34,45,56,67,78]
list.pop(2)
del list[0]
print(list)
'''

#empty list
'''
list=[23,34,56,76]
list.clear()
print(list)
'''

#max and min
'''
list=[23,34,56,67,78]
max_list=max(list)
print(max_list)
'''
'''
list=[23,34,56,67,78]
min_list=min(list)
print(min_list)
'''
#sum of all element
'''
list=[23,34,45,56,"P"]
max_list=sum(list)

print(max_list)
'''

# List Comprehension
# Suppose you want to create a list of squares of numbers

# numbers = [1, 2, 3, 4, 5]

# squares = []

# for n in numbers:
#     squares.append(n * n)

# print(squares)

# output is :- [1, 4, 9, 16, 25]

# 2. With list comprehension
# We can write the same code in one line:

# numbers = [1, 2, 3, 4, 5]
# squares = [n * n for n in numbers]
# print(squares)
# output : -[1, 4, 9, 16, 25]