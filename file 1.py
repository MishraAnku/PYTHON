# For copying files/folders we have to use shutil module
import shutil

# file = open("Prac.txt","w")
# file.write("Hello World!!")
# file.close()

# file = open("Prac.txt","r")
# data = file.read()
# print(data)
# file.close()

# Copy the content from the file into another file
# shutil.copy("Prac.txt","Prac1.txt")

# Copy the entire file from one folder to another.
# shutil.copytree(r"C:\Users\SHUBHAM\Desktop\Python_File\Sh",r"C:\Users\SHUBHAM\Desktop\Python_File2\tp")

# Why we use shutil(shell utilities) instead of OS(Operating System)
# shutil is platform independent
# os operates according to your operating system.

# For removing/deleting file from a folder we need to use OS module.
# import os
# os.remove(r"C:\Users\SHUBHAM\Desktop\Python_File2\tp\pqr.txt")

# Move file from one location to another
# shutil.move(r"C:\Users\SHUBHAM\Desktop\Python_File\Sh\move.txt",r"C:\Users\SHUBHAM\Desktop\Python_File2\tp")
