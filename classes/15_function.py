#what is function

# a block of code it can call mutlpies times

# pre defined
# user defined

# No parameter no return

# def add():
#     a = int(input("Enter a num A "))
#     b = int(input("Enter a num B "))
#     print(a+b)

# add()


# Yes parameter no return

# def add(a,b):
#     print(a+b)

# a = int(input("Enter a num A "))
# b = int(input("Enter a num B "))
# add(a,b)
# add(90,89)

# No parameter yes return

# def ad():
#     a = 90
#     b = 78
#     if(a>b):
#         return "A is max"

#     else:
#         return "B is max"

# sum = ad()
# print(sum)


# yes yes

def ad(a,b):

    if(a>b):
        return "A is max"

    else:
        return "B is max"


a = 90
b = 78
sum = ad(a,b)
print(sum)