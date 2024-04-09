# r -  opens file in read mode - file should be already created to open in read mode.
# w -  opens the file in write mode - if file already present, it will open it in write mode. If the file is not already present, it will create the file by itself.
# a -  opens file in write mode - If you want to have previously entered data and also enter new data, open in append mode.
# x -  create a new file for write only.
# r+ - open the file for read/write. 
# w+ - 
# a+
# x+

# Creating a file
# file = open("ABC","w")
# file.write("Hello World!!")
# print("Successfully executed")
# file.close()

# Reading the file
# file = open("ABC","r")
# data = file.read()
# print(data)
# file.close()

# Creating the file and entering input from the user.
# file = open("Demo.txt", "w")
# inputData = input("Enter the data to be inserted in file:")
# file.write(inputData)
# print("Successfully Executed")
# file.close()

# file = open("Demo.txt","r")
# data = file.read()
# print(data)
# file.close()

# Creating a file in specific location as per your requirement.
# Method 1 - using r keyword befor path - r stands for raw data
# file = open(r"D:\testPython\abc.txt", "w")
# inputData = input("Enter the data to be inserted in file:")
# file.write(inputData)
# print("Successfully Executed")
# file.close()

# Method 2 - using \\ instead of r
# file = open("D:\\testPython\\abcd.txt", "w")
# inputData = input("Enter the data to be inserted in file:")
# file.write(inputData)
# print("Successfully Executed")
# file.close()

# file = open("D:\\testPython\\abc.txt","r")
# data = file.read()
# print(data)
# file.close()

# Creating a new file and then copying content from that file into new file
# file = open("D:\\testPython\\test.txt", "w")
# inputData = input("Enter the data to be inserted in file:")
# file.write(inputData)
# file = open("D:\\testPython\\test.txt","r")
# data = file.read()
# file = open("D:\\testPython\\test1.txt","w")
# file.write(data)
# file.close()

# Reading a already created file and then copying content from that file into new file and then again reading that file.
# file = open("D:\\testPython\\test.txt","r")
# data = file.read()
# file = open("D:\\testPython\\test1.txt","w")
# file.write(data)
# file.close()
# file = open("D:\\testPython\\test1.txt","r")
# data = file.read()
# print(data)
# file.close()

# file = open("D:\\testPython\\testAppend.txt","a")
# inputData = input("Enter the data to be inserted in file:")
# file.write(inputData)
# file.close()


# file = open("D:\\testPython\\testAppend.txt","r")
# data = file.read()
# print(data)
# file.close()
