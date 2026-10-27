#loop quetion  1 to 10

# Q1 - 1 to n
# n = int(input("Enter a Ending point "))

for r in range(1,n+1):
    print(r)


# Q2 n to 1
# n = int(input("Enter a Starting point "))

# for r in range(n,0,-1):
#     print(r)


# Q3 a to z
# a=65
# while(a<=90):
#     print(chr(a))
#     a+=1

# Q4 even from 1 to n
# n = int(input("Enter a Ending point "))

# for r in range(1,n+1):
#     if(r%2==0):
#         print(r)

# Q6 Sum of number from 1 to n
# 0 = 0 + 1
# 1 = 1 + 2
# 3 = 3 + 3
# 6 = 6 + 4

# n = int(input("Enter a Ending point "))
# sum = 0
# for r in range(1,n+1):
#     sum = sum + r

# print(sum)


# Q7 sum of even number from 1 to n 
# n = int(input("Enter a Ending point "))
# sum = 0
# for r in range(1,n+1):
#     if(r%2==0):
#         sum = sum + r

# print(sum)


# Q9 multiplcation table 
# n = int(input("Enter a Number to get table "))

# for r in range(1,10+1):
#     print(r,"X",n,"=",r*n)



# Q10 count digit 
# 1234/10 = 123.4
# 1234//10 = 123

# n = int(input("Enter a Number ")) #1234
# count = 0
# while(n!=0):
#     n = n // 10 #1234 123 12 1 0
#     count += 1 #0 1 2 3 4

# print("digit in number ",count)