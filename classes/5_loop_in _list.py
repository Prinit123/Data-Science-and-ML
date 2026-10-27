#loop in list for
'''
list=[23,34,56,67,78]
for x in list:
           if x==34:
                      print("34")
'''

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  

#while loop

# list = [23,34,45,56,7,89]
# i = 0
# while i < len(list):
#            print(list[i])
#            i=i+1
           

#comprehension in for loop


'''
squares = []
for x in range(1, 6):
    squares.append(x**2)

print(squares) # Output: [1, 4, 9, 16, 25]
'''
#after
'''
squares = [x**2 for x in range(1, 6)]

print(squares) # Output: [1, 4, 9, 16, 25]
'''
#or
'''
square = [i for i in range(0,10) if i%2==0]  # starting i or any operation compalsory ,after if is opational
print(square)
'''
'''
list=[23,34,45,67,87]
[print(x) for x in list] # output : [23,34,45,67,87]
'''

#List comprehension offers a shorter syntax when
#you want to create a new list
#based on the values of an existing list.
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
'''

#output :- ["appale","banana","mango"]
"""
The Filter:
if "a" in x apple (has "a") -> Keep
banana (has "a")->Keep
cherry (no "a")->Discard
kiwi (no "a")->Discard
mango (has "a")->Keep
"""
