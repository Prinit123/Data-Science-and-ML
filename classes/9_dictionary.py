#Python Dictionaries

#Dictionaries are used to store data values in key:value pairs.

'''
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict)
'''

# len
'''
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(len(thisdict))
'''

# enter any datatype
'''
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
'''

# remove iterm use pop
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
'''
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
'''

# add
'''
car = {"brand": "Toyota"}
# Adding multiple pairs at once
car.update({"year": 2024, "electric": False})
'''

# 2.
'''
car = {"brand": "Toyota"}
# Adding a new key-value pair
car["color"] = "Blue"
'''

# deleate value
'''
# .popitem()
car = {"brand": "Toyota", "model": "Corolla", "year": 2024}
# Removes and returns the last item added
removed_item = car.popitem()
print(removed_item)
# Output: ('year', 2024)
print(car)
# Output: {'brand': 'Toyota', 'model': 'Corolla'}
'''

# dictonery under dictunery 
'''
students = {
    "student1": {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Priya",
        "age": 21,
        "marks": 90
    }
}

print(students["student1"])
print(students["student1"]["name"])
'''