import os


f = open("demofile.txt", "r")
print(f.read())  # a read() method for reading the content of the file
f = open("demofile.txt", "r")
print(f.read(5))  # Return the 5 first characters of the file
f = open("demofile.txt", "r")
print(f.readline())  # You can return one line by using the readline() method
print(f.readline())
f = open("demofile.txt", "r")
for x in f:
    print(x)
f.close()
"""
f = open("demofile.txt", "a")
f.write("\n \n Now the file has more contact!")  # Open the file "demofile2.txt" and append content to the file
f.close()
f = open("demofile.txt", "r")  # open and read the file after the appending
print(f.read())
"""
f = open("demofile3.txt", "w")
f.write("\n \n Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
f = open("myfile.txt", "x")  # Result: a new empty file is created


if os.path.exists("myfile.txt"):  # Check if file exists, then delete it
    os.remove("myfile.txt")
else:
    print("The file does not exist")



