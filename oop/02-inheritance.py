# 🧱 Inheritance: Creating a child class that copies features from a parent class.

# allows a Child class to adopt all the attributes and methods from a Parent class


# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4.# herical
# 5. hybrid 

# single level 

# class kict:
#     def std1(self):
#         print("Im student 1")

# class kict2(kict):
#     def std2(self):
#         print("Im student 2")


# ob = kict2()
# ob.std2()
# ob.std1()


# multilevel 

# class kict:
#     def std1(self):
#         print("Im student 1")

# class kict2(kict):
#     def std2(self):
#         print("Im student 2")


# class kict3(kict2):
#     def std3(self):
#         print("Im student 3")

# ob = kict3()
# ob.std2()
# ob.std1()
# ob.std3()


# mutlplie

# class kict:
#     def std1(self):
#         print("Im student 1")

# class kict2(kict):
#     def std2(self):
#         print("Im student 2")


# class kict3(kict):
#     def std3(self):
#         print("Im student 3")

# ob = kict3()
# ob.std1()
# ob.std3()


# herical 

# class kict:
#     def std1(self):
#         print("Im student 1")

# class kict2:
#     def std2(self):
#         print("Im student 2")


# class kict3(kict,kict2):
#     def std3(self):
#         print("Im student 3")

# ob = kict3()
# ob.std1()
# ob.std3()
# ob.std2()

# hybrid 

# class kict:
#     def std1(self):
#         print("Im student 1")

# class kict2(kict):
#     def std2(self):
#         print("Im student 2")


# class kict3(kict):
#     def std3(self):
#         print("Im student 3")


# class kict4(kict2, kict3):
#     def std4(self):
#         print("Im student 4")

# ob = kict4()
# ob.std1()
# ob.std3()
# ob.std4()
# ob.std2()
