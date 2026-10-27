# from abc import ABC, abstractmethod

# # 1. Inherit from ABC to make this an Abstract Class
# class Shape(ABC):
#  # 2. Decorate methods that MUST be overridden by child classes
# @abstractmethod
# def calculate_area(self):
#         pass

#     # Abstract classes can also have normal (concrete) methods
#     def print_info(self):
#         print("I am a shape.")

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         
#     # 3. The child class MUST implement the abstract method
#     def calculate_area(self):
#         return 3.14159 * (self.radius ** 2)

# class Rectangle(Shape):
#  def __init__(self, width, height):
#  self.width = width
# self.height = height

# def calculate_area(self):
#  return self.width * self.height

# # --- Testing the Abstraction ---

# # ERROR: You cannot instantiate an abstract base class directly.
# # my_shape = Shape()  # This will raise a TypeError

# # SUCCESS: You can instantiate child classes that implement the abstract methods.
# circle = Circle(5)
# rect = Rectangle(4, 6)


from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def withdraw(self):
        pass

class Bank(ATM):

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def withdraw(self):
        amount = 1000

        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Withdrawal Amount:", amount)

        if amount <= self.balance:
            self.balance -= amount
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient balance")

b = Bank("Rahul", 123456, 5000)
b.withdraw()
