# file = open("file.txt", "x")
# print("FIle created successfully")


# file = open("file.txt", "w")
# file.write("Hello, this is a sample file.\n")
# file.write("This file is used for demonstrating file handling in Python.\n")
# print("FIle writed successfully")
# file.close()


# file = open("file.txt", "r")
# print(file.read())
# print(file.readline())
# This reads all remaining lines and returns them as a list of strings.
# print(file.readlines())
# file.close()

# file = open("file.txt", "a")
# file.write("This line is added using append mode.\n")
# print("FIle appended successfully")


# File Position in Python (File Handling)
# File position means the current location of the cursor inside a file where Python will read or write data.

# Two important functions
# Function	Meaning
# tell()	Returns the current position of the file cursor.
# seek()	Moves the file cursor to a specified position

# tell()
# file = open("file.txt", "r")
# print(file.tell())  # 0
# print(file.read(5))  # Hello
# print(file.tell())  # 5
# file.close()

# seek()
# file = open("file.txt", "r")
# print(file.read(5))  # Hello
# file.seek(0)
# print(file.read(5))  # Hello
# file.close()


# # if iprint only 3 lines
# # lines()

# file = open("file.txt", "r")
# lines = file.readlines()
# print(lines[0])
# print(lines[1])
# # print(lines[2])
# file.close()

# file = open("file.txt", "r")
# for i in range(3):
#     print(file.readline(), end="")
# file.close()
