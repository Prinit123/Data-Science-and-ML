
# Encapsulation is the process of wrapping data (variables) and methods into a single unit called a class and controlling access to that data.

# | Type      | Example           | Meaning                                  |
# | --------- | ----------------- | ---------------------------------------- |
# | Public    | `self.name`       | Accessible from anywhere                 |
# | Protected | `self._marks`     | Intended for internal use and subclasses |
# | Private   | `self.__password` | Name-mangled to discourage direct access |

# self is used to refer to the current object, and self.name is used to store data inside that object.

# why we use self.name ?
# But if you write print(k.name), Python gives an error because the object has no name attribute.

# class Student:
#     def __init__(self):
#         self.name = "Rahul"       # Public
#         self._marks = 80          # Protected (convention)
#         self.__password = "1234"  # Private (name mangling)

#     def show(self):
#         print(self.name)
#         print(self._marks)
#         print(self.__password)

# s = Student()
# s.show()

# class BankAccount:
#            def hi(self, owner, balance):
#                                  self.owner = owner
#                                  self.__balance = balance

#            # Public method to view data safely (Getter)
#            def get_balance(self):
#                                  return self.__balance

# # Usage
# account = BankAccount()
# account.hi("Alice",1000)
# # print(account.owner)
# # print(account.__balance)  # Error! Cannot access directly.
# print(account.get_balance()) # Output: 1000





# encapsulation
# public

class kict:
	def __init__(self,name):
		self.name=name
		print("Hello",name)

k=kict("heli")
print(k.name)

# protected

class Parent:
    def __init__(self):
        self._marks = 90

class Child(Parent):
    def show(self):
        print("Marks:", self._marks)

c = Child()
c.show()

# private

# class kict:
# 	def __init__(self,name,password):
# 		self._name=name
# 		self.__password=password
# 		print("Hello")
# 	def display(self):
# 		print(self.__password)
# k=kict("heli","heli1234")
# print(k._name)
# k.display()