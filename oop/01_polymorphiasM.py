# overloading
# Method overloading means having multiple methods with the same name but different parameters.

# Python does not support traditional method overloading like C++ or Java.

class add2:
    def __init__(self,a):
        self.a1 = a
        print("hello : ",self.name)

    def __init__(self,a,b):
        self.a1 = a
        self.a2 = b
        print("hello : ",self.a1+self.a2)

obj = add2(3,4)



# s1 = add2(34,56)

# overriding
# Method overriding occurs when a child class provides its own implementation of a method that is already defined in the parent class.

# Method overriding means redefining a parent class method in the child class with the same method name and parameters.


# class add2:
#      def hi(self):
#         print("hello , prinit ")

# class add3(add2):
#     def hi(self):
#         print("hi ,kict ")


# obj = add3()
# obj.hi()

