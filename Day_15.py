# def MyDecorator(func) :
#     def wrap():
#         print("Before func execution")
#         func()
#         print("After execution")
#     return wrap
    
# @MyDecorator
# def sayHello() :
#         print("Hello Python")

    
# sayHello()

# TASK: decorators with parameters



#Abstraction:
# from abc import ABC,abstractmethod
# class shape(ABC):
#     def __init__(self,color):
#         self.color=color
#     @abstractmethod
#     def calc_area(self):#to restrict this class method abstraction used due to its incomplete implementation
#         pass  
    
#     def displayColor(self):
#         print(self.color)
    
# class Rectangle(shape):
#     def __init__(self,color,l,b):
#         super().__init__(color)
#         self.l=l
#         self.b=b
#     def calc_area(self):
#         area=self.l*self.b
#         print(area)
#     def displayColor(self):
#         return super().displayColor()   


# class Circle(shape):
#     def __init__(self,color,r):
#         super().__init__(color)
#         self.pi= 3.14
#         self.r=r   
#     def calc_area(self):
#         area=self.pi**self.r
#         print(area)
        
        
# r=Rectangle("red",20,10)
# r.calc_area()
# r.displayColor()

# c=Circle("Black",2)
# c.calc_area()
# c.displayColor()

#we also can add variable in class which known as class variable 
#also accessible by invoking class no need to create and use object.
#just like static in java
#TASK:
#decorators with params
#A decorator with parameters allows you to customize the behavior of a decorator by passing arguments to it 

def greeting_decorator(func):
    def wrapper(name):
        print("Preparing to greet...")
        func(name)
        print("Greeting complete!")
    return wrapper

@greeting_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("PREC Students")

def repeat(n):  # Outer function 
    def decorator(func):  # Decorator function
        def wrapper(*args, **kwargs):  # Wrapper function
            for _ in range(n): 
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)  
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("PREC")

# #find class variable
class Car :
    wheels=4 #class variable
    def __init__(self,color):
        self.color=color
    def display(self):
        print(self.color)
        print(Car.wheels)
    wheels=5 #We can change the value of class variable
c=Car("Red")
c.display()


#static variable and method
class Bank:
    bank_name = "National Bank of India"  #class variable

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  
        self.balance = balance  

    @staticmethod
    def bank_policy():
        return "The minimum balance should be $100."

    def display_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
        print(f"Bank Name: {Bank.bank_name}")

print(Bank.bank_name)  
print(Bank.bank_policy())  

account1 = Bank("Subodh", 5000)
account2 = Bank("ssw", 3000)


account1.display_account_details()
account2.display_account_details()



# #Interface
# #total abstraction
# #python separately cannot support interface


import time
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ₹{amount}...")
        time.sleep(3)
        print("Payment completed.")

class DebitCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing debit card payment of ₹{amount}...")
        time.sleep(4)
        print("Payment completed.")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount}...")
        time.sleep(3)
        print("Payment completed.")

def make_payment():
    print("Select Payment Method:")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")

    try:
        choice = int(input("Enter your choice (1/2/3): "))
        amount = float(input("Enter the amount to pay: "))

        if choice == 1:
            payment_method = CreditCardPayment()
        elif choice == 2:
            payment_method = DebitCardPayment()
        elif choice == 3:
            payment_method = UPIPayment()
        else:
            print("Invalid choice. Please try again.")
            return

        payment_method.process_payment(amount)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

make_payment()



# #Session Example of Database Connection
from abc import ABC, abstractmethod
import time

class ConnectDB(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

class Oracle(ConnectDB):
    def connect(self):
        print(f"Connecting to Oracle DB...")
        time.sleep(2)  
        print("Successfully connected to Oracle DB.")
        # You can add actual connection code here with libraries such as cx_Oracle or SQLAlchemy
    def disconnect(self):
        print("Disconnecting from Oracle DB...")
        time.sleep(1)
        print("Successfully disconnected from Oracle DB.")
        # Actual disconnection logic would be here

class Sybase(ConnectDB):
    def connect(self):
        print(f"Connecting to Sybase DB...")
        time.sleep(2)  
        print("Successfully connected to Sybase DB.")
        # Actual connection code using libraries like PySybase or SQLAlchemy for Sybase
        
    def disconnect(self):
        print("Disconnecting from Sybase DB...")
        time.sleep(1) 
        print("Successfully disconnected from Sybase DB.")
        # Actual disconnection logic would go here

class Mongodb(ConnectDB):
    def connect(self):
        print(f"Connecting to MongoDB...")
        time.sleep(2) 
        print("Successfully connected to MongoDB.")
        # Actual connection code using PyMongo or other MongoDB client libraries

    def disconnect(self):
        print("Disconnecting from MongoDB...")
        time.sleep(1)  # Simulating a delay for disconnection
        print("Successfully disconnected from MongoDB.")
        # Actual disconnection logic would go here


# User Input for Database Choice
db = input("Enter your DB name for eg(oracle/sybase/mongoDb) : ").strip().lower()

try:
    # Checking if the class exists dynamically in the global scope
    if db.capitalize() not in globals():
        raise Exception("Database not found. Please provide a valid database name.")
except Exception as e:
    print(f"Error: {e}")
else:
    try:
        # Dynamically instantiate the class and call methods
        db_class = globals()[db.capitalize()] 
        db_instance = db_class() 
        db_instance.connect()  
        db_instance.disconnect() 
    except Exception as e:
        print(f"An error occurred while trying to connect to the database: {e}")

#The globals() method in Python is a built-in function that returns a dictionary of the current global symbol table. The global symbol table contains all the variables and functions that are defined in the global scope of the program. The keys of the dictionary are the names of the variables and functions, and the values are the corresponding objects that they refer to.
x = 5

def modify_global():
    globals()["x"] = 100  # Modifying the global variable dynamically

print(f"Before: x = {x}")
modify_global()
print(f"After: x = {x}")

# Modifying global variables using globals() can make the code harder to read and debug. 
# It is generally recommended to avoid modifying global variables directly using the globals() function


