#Tuple

#A tuple is a collection which is ordered and unchangeable.
#1.Tuples are unchangeable, meaning that we cannot change,
# add or remove items after the tuple has been created.

#2.Tuple items are ordered, unchangeable,
# and allow duplicate values.

#3.Tuple items are indexed, the first item has index [0],
# the second item has index [1] etc.

'''
list=(23,34,45,67,78)
print(list)
'''
'''
list=(23,34,45,56)
print(list[1])
'''
'''
list=(23,34,45,56,67)
print(list[:3])
'''
#if statment in list and tuple is defrent
'''
list=(23,34,45,56,56)
if 23 in list:
           print("23")
        '''

# change in tuple but tuple is unchengebale
# you first convert in list and cheange value after list change in tuple
'''
x=(23,34,45,56,67)
y=list(x)
y[1]=100
x=tuple(y)
print(x)
'''


#un pack tuple

'''
list=(23,34,45,56,65)
a,b,c,d,e=list
print(a)
'''
'''
list=("banana","appale","charry")
(b,a,c)=list
print(a)
'''

#Using Asterisk*
'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
'''

#Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


#while loop
'''
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
'''

# join tuple
'''
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
'''
