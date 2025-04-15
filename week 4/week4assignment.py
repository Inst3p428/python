#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.


"""with open("pycodes.txt", "w") as file: 
    file.write("Hello, Python!")
    

with open("pycodes.txt", "r") as file: 
    data = file.read() 
    print(data)"""
#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
UserInput=str(input("Enter file name: "))

try:
    file = open(UserInput, "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()