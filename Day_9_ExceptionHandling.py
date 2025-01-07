#Exception Handling
#what is error -> Mistakes made by programmer or system causes stop the flow of execution of program
# types of error-> 1)compile time error 2) runtime error 3) Logical error
# execution of python program -> .py->compile(convert it into bytecode file)-> .pyc-> PVM(RT) (interpreter) -> Machine code

# 1)A single try block can be followed by several exception
# 2)Multiple Except blocks can be used to handle multiple exceptions
# 3)We cannot write except blocks without a try block
# 4)We can write a try block without except blocks
# 5)else block and finally blocks are not compulsory
# 6)When there is no exception, else block is executed after try block
# 7)finally block is always executed.

# ZeroDivisionError:
# Write a program to divide two numbers. Handle the case where the denominator is zero and print an appropriate message.
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# try:
#     divide=num1/num2
#     print(f"Division is :{divide}")
# except ZeroDivisionError as Ze:
#     print(f"{Ze} is not possible")

# ValueError:
# Write a program to accept an integer from the user. Handle the case where the input is not an integer.
# try:
#     num1=int(input("Enter Any number to print: "))
# except ValueError as Ve:
#     print(Ve)
#     print(f"You cannot enter a value other than interger,Please enter a integer value")
# else:
#     sqr=num1**2
#     print(f"Square of {num1} is {sqr}") 

# FileNotFoundError:
# Write a program to open a file for reading. Handle the error if the file does not exist.
# filename=input("Enter the filename which you want to read:")
# try:
#     f=open(r"C:\Users\subod\Internship 2024-25\\"+filename+".txt",'r+')
#     data=f.write("subodh shivaji wadekar")
    
# except Exception as e:
#     print(e)
#     print("This file is not found please enter a existing file name...")


# KeyError:
# Create a dictionary and try to access a key that doesn’t exist. Handle the exception and print an error message.






# TypeError:
# Write a function that concatenates two strings. Handle the error if non-string values are passed to the function.

# IndexError:
# Write a program to access an element from a list by index. Handle the case where the index is out of range.

# AttributeError:
# Write a program to access a method that does not exist in an object. Handle the error appropriately.

# NameError:
# Write a program to use a variable that has not been declared. Handle the error with a try-except block.