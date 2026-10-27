# what is class and object ?
# class is collection of function
# a blueprint of object

# object an instance of class


# obj.std1()
# kict.std1(obj)
# So self receives the obj.
# def std1(self):

class kict:
    def std1(self):
        print("i'm student 1")

    def std2(self):
        print("i'm student 2")


obj = kict()
obj.std1()
obj.std2()