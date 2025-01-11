# ANS
# 1) A
# 2) A
# 3) B
# 4) A calls the parent class methods
# 5) B Not found
# 6) A check for value equality
# 7) D All of the above
# 8) A abcdefabcdef
# 9) B [1],[1,1]
# 10) A =1
# 11) C (1) (2,3,4)
# 12) A True
# 13) B {'name': 'Alice', 'age': 26}




# 14) Create a class Vehicle with attributes like brand and speed. Derive two classes, Car and Bicycle, from Vehicle. Add an additional attribute for each (Car should have fuel_type and Bicycle should have gear_count). Instantiate both and display their information.

class Vehicle:#brand and speed
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display(self):
        print(f"Brand of vehicle is {self.brand} and speed is {self.speed} km/hr")

class Car(Vehicle): #fuel_type
    def __init__(self,brand,speed,fuel_type):
        super().__init__(brand,speed)
        self.fuel_type=fuel_type
    def display(self):
        print(f"Brand of Car is {self.brand} and speed is {self.speed} km/hr and fuel type is {self.fuel_type}")

class Bicycle(Vehicle): #gear_count
    def __init__(self,brand,speed,gear_count):
        super().__init__(brand,speed)
        self.gear_count=gear_count

    def display(self):
        print(f"Brand of Bicycle is {self.brand} and speed is {self.speed} km/hr and gear count is {self.gear_count}")

v=Vehicle("Maruti Suzuki",80)
v.display()
c=Car("Maruti Suzuki",80,"Petrol")
c.display()
b=Bicycle("Hero",20,5)
b.display()





#15)Bank 
# Write a class BankAccount with methods deposit() and withdraw(). Implement exception handling for cases when withdrawal exceeds balance, and display an appropriate error message. Ensure that all transactions are logged into a file.
import time
from logging import *


basicConfig(
    filename=r'C:\Users\subod\Internship 2024-25\Internship_Work\TransactionLog.txt',
    level=INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)

class BankAccount:
    def __init__(self, acc_number, initial_balance=0):
        self.acc_number = acc_number
        self.balance = initial_balance
        info(f"Account created with initial balance: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            error("Deposit amount must be greater than zero.")
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        info(f"Deposit: {amount}. New balance: {self.balance}")
        print(f"Successfully deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            error(f"Withdrawal amount must be greater than zero. Attempted: {amount}")
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            error(f"Insufficient balance for withdrawal. Attempted: {amount}")
            print("Insufficient balance for withdrawal.")
            return
        self.balance -= amount
        info(f"Withdraw: {amount}. Remaining balance: {self.balance}")
        print(f"Successfully withdrawn: {amount}. Remaining balance: {self.balance}")


if __name__ == "__main__":
    account = BankAccount("8767097901", 1000)  
    account.deposit(500)                       
    account.withdraw(200)                      
    account.withdraw(-100)                     

else:
    print("Bank Account transactions are done successfully")                






# #16)
# #Inheritance and Method Overriding 
# # Create a base class Shape with a method area() that calculates the area. Derive two classes, Rectangle and Circle, and override the area() method in each to calculate the area for the respective shapes. Display the areas of both shapes.

class Shape:
    def area(self,length,breadth):
        return self.length*self.breadth

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    
r=Rectangle(10,20)
print(f"Rectangle Area: {r.area()}")
c=Circle(5)
print(f"Circle Area: {c.area()}")


#17)
# Banking System Using Inheritance
# ● Create a base class BankAccount with attributes account_number, name, and balance. Add methods for deposit and withdrawal.
# ● Create a derived class SavingsAccount that limits the number of withdrawals to 3 per month.
# ● Create another derived class CurrentAccount that deducts a maintenance fee for low balances.
# ● And Log the exception to file.
# ● Write a menu-driven program to:
# ○ Create accounts.
# ○ Perform deposits and withdrawals.
# ○ Display account details.
# ○ Handle invalid operations using try-except blocks
import time
from logging import *

# Logging file creation
basicConfig(
    filename=r'C:\Users\subod\Internship 2024-25\Internship_Work\BankingLogs.txt',
    level=INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)

# Base class: BankAccount
class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        info(f"Account created: {self.account_number}, Holder: {self.name}, Initial Balance: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            error(f"Deposit failed: Invalid amount {amount} for account {self.account_number}")
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        info(f"Deposit: {amount} to account {self.account_number}. New balance: {self.balance}")
        print(f"Successfully deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            error(f"Withdrawal failed: Invalid amount {amount} for account {self.account_number}")
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            error(f"Withdrawal failed: Insufficient balance for account {self.account_number}")
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount
        info(f"Withdrawal: {amount} from account {self.account_number}. Remaining balance: {self.balance}")
        print(f"Successfully withdrawn: {amount}. Remaining balance: {self.balance}")

    def display(self):
        print("\nAccount Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        info(f"Displayed details for account {self.account_number}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, name, balance):
        super().__init__(account_number, name, balance)
        self.withdrawal_limit = 3
        self.withdrawals_this_month = 0

    def withdraw(self, amount):
        if self.withdrawals_this_month >= self.withdrawal_limit:
            warning(f"Withdrawal limit reached for account {self.account_number}")
            print("Withdrawal limit reached for this month.")
            return
        super().withdraw(amount)
        self.withdrawals_this_month += 1


class CurrentAccount(BankAccount):
    def __init__(self, account_number, name, balance):
        super().__init__(account_number, name, balance)

    def withdraw(self, amount):
        maintenance_fee = 100
        if self.balance < 500:
            if self.balance < amount + maintenance_fee:
                error(f"Withdrawal failed: Insufficient balance for account {self.account_number} after maintenance fee")
                raise ValueError("Insufficient balance to withdraw with maintenance fee.")
            self.balance -= (amount + maintenance_fee)
            info(f"Withdrawal: {amount} + maintenance fee {maintenance_fee} from account {self.account_number}. Remaining balance: {self.balance}")
        else:
            super().withdraw(amount)

# Menu
def menu():
    accounts = {}
    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Details")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                account_type = input("Enter account type (Savings/Current): ").strip().lower()
                account_number = input("Enter account number: ")
                name = input("Enter account holder's name: ")
                balance = float(input("Enter initial balance: "))

                if account_type == "savings":
                    accounts[account_number] = SavingsAccount(account_number, name, balance)
                elif account_type == "current":
                    accounts[account_number] = CurrentAccount(account_number, name, balance)
                else:
                    print("Invalid account type.")
                    warning("Attempted to create account with invalid account type.")
            elif choice == 2:
                account_number = input("Enter account number: ")
                if account_number not in accounts:
                    error(f"Account not found for deposit: {account_number}")
                    print("Account not found. Please create an account first.")
                    continue
                amount = float(input("Enter amount to deposit: "))
                accounts[account_number].deposit(amount)
            elif choice == 3:
                account_number = input("Enter account number: ")
                if account_number not in accounts:
                    error(f"Account not found for withdrawal: {account_number}")
                    print("Account not found. Please create an account first.")
                    continue
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            elif choice == 4:
                account_number = input("Enter account number: ")
                if account_number not in accounts:
                    error(f"Account not found for display: {account_number}")
                    print("Account not found. Please create an account first.")
                    continue
                accounts[account_number].display()
            elif choice == 5:
                print("Exiting Banking System....")
                info("Exited the banking system.")
                break
            else:
                print("Invalid choice. Please try again.")
                warning("Invalid menu choice selected.")
        except ValueError as e:
            print(f"Error: {e} Please enter a valid number.")
            error(f"ValueError: {e}")
        except KeyError:
            print("Account not found. Please create an account first.")
            error("KeyError: Account not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e} Please try again.")
            error(f"Unexpected error: {e}")


if __name__ == "__main__":
    menu()
