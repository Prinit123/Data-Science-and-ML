# file = open("exampale1.txt", "x")
# print("file created")

# file = open("exampale1.txt", "w")
# file.write("hello whorld 1")
# file.write("hello whorld 2")
# file.write("hello whorld 3")
# file.write("hello whorld 4")

# print("file created")

file = open("exampale1.txt","r")
# lines = file.readline()
# lines = file.readline()
# print(lines)

file = open("exampale1.txt", "r")

line = file.readline()
while line:
    print(line , end="")
    line = file.readline()  # Read the next line

file.close()  # Don't forget to close the file when done without 'with'


# print(lines)

# with open("exampale1.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)  # Outputs: ['hello whorld 1\n', 'hello whorld 2\n', ...]


# file = open("exampale1.txt", "r")
# # Read the first line
# line = file.readline()
# # Loop runs until readline() returns an empty string (end of file)
# while line:
#     print(line, end="")  # end="" prevents blank lines between outputs
#     line = file.readline()  # Fetch the next line

# file.close()
