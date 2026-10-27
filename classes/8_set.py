#set
#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed
#index not fix

'''
set={34,45,56,67,89}
print(set)
'''

#duplicate not alloude
'''
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
'''
# tuples is 1 nad True is same value  means it's like duplicate
'''
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
'''

# output :-{True, 2, 'banana', 'cherry', 'apple'}

# len function

thisset = {"apple", "banana", "cherry"}
print(len(thisset))


# set can use diffrent data type
'''

set1 = {"abc", 34, True, 40, "male"}
print(set1)
'''

# type set find
'''
myset = {"apple", "banana", "cherry"}
print(type(myset))     #output :-  <class 'set'>
'''

#constructor set
'''
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
'''

#Once a set is created, you cannot change its items, but you can add new items.
'''
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
'''

#add set
'''
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
'''
'''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
'''

#remove
'''
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
'''

# for loop
'''
thisset = {"apple", "banana", "cherry"}
for x in thisset:
           print(x)
           '''

