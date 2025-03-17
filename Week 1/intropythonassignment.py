#Instructions:

#Basic Calculator Program

#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

print("Basic Calculator Program")
print("Type 'quit' to end")

while True:
    num1=str(input("Enter a numerical value: "))
    if num1 == "quit" :
        break
    num2=str(input("Enter another numerical value: "))
    operation=str(input("Choose an operation; +,-,*,/:  "))
    
    if operation == "+":
        print("Outcome of operation is: ",float(num1) + float(num2))
    elif operation == "*":
        print("Outcome of operation is: ",float(num1) * float(num2))
    elif operation == "/":
        print("Outcome of operation is: ",float(num1) / float(num2))    
    elif operation == "-":
        print("Outcome of operation is: ",float(num1) - (num2))
    else:
        print("Invalid Operation!!")
