# Basic Try-Except
# try:
#     num=int(input("ENter The Number : "))
#     print(num)
# except:
#     print("Kik Locha CHa !")



# Specific Exception Handling
# try:
#     num = int(input("Enter The Number "))
#     d=10/num
#     print("ANs : ",d)
# except ValueError:
#     print("Please ENter a valid number : !")
# except ZeroDivisionError:
#     print('Cannot Divide By Zero')



# Multiple Exceptions with One Except
# try:
#     num = int(input("Enter The Number "))
#     d=10/num
#     print("ANs : ",d)
# except (ValueError,ZeroDivisionError):
#     print("Please ENter a valid number or cannot divide by zero !")



try:
    num = int(input("Enter The Number "))
    d=10/num
    print("ANs : ",d)
except (ValueError,ZeroDivisionError):
    print("Please ENter a valid number and cannot divide by zero !")
finally:
    print('Division DOne !')



# Finally Block
# try:
#     file=open('sample.txt',"r")
#     c=file.read()
#     print(c)
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("Closing The FIle ")
#     file.close()




# Custom Exception Handling
# def check_age(a):
#     if a<18:
#         raise ValueError("Age Must Be 18 or above")
#     else:
#         print("Welcome !")

# try:
#     age=int(input("Enter Your Age :"))
#     check_age(age)

# except ValueError as er:
#     print(er)