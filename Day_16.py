#Task on payment gateway system credit card,paypal,google pay
# after payment user need to decide to cancel the payment if yes then display confirmation message
#Dynamic class handling
# methods are process_payment,cancel_payment

#Abstraction and Interface concepts are used


import time
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass
    

    @abstractmethod
    def cancel_payment(self):
        pass 

class Creditcard(Payment):
    def process_payment(self,amount):
        print(f"Processing the payment of total amount ₹{amount} By Credit card.....")
        time.sleep(3)
        print("Payment from Credit card is completed successfully...! ")
        
    def cancel_payment(self):
        print("To confirm again do you want to cancel the payment....")
        print("Yes or No")
        cancel=input().lower()
        if cancel=="yes":
            print("canceling payment....")
            time.sleep(3)
            print("payment is Canceled successfully")
        else:
            print("Processing wait for a moment...")
            time.sleep(3)
            print("Payment is completed successfully...!")
                
    
    
class Paypal(Payment):
    def process_payment(self,amount):
        print(f"Processing the payment of total amount ₹{amount} By PayPal.....")
        time.sleep(3)
        print("Payment from PayPal is completed successfully...! ")
        
    def cancel_payment(self):
        print("To confirm again do you want to cancel the payment....")
        print("choose :Yes or No")
        cancel=input().lower()
        if cancel=="yes":
            print("Canceling payment")
            time.sleep(3)
            print("payment is Canceled successfully")
        else:
            print("Processing wait for a moment...")
            time.sleep(3)
            print("Payment is completed successfully...!")
            
class Googlepay(Payment):
    def process_payment(self,amount):
        print(f"Processing the payment of total amount ₹{amount} by Google Pay....")
        time.sleep(3)
        print("Payment from Credit card is completed successfully...! ")
        
    def cancel_payment(self):
        print("To confirm again do you want to cancel the payment....")
        print("choose :Yes or No")
        cancel=input().lower()
        if cancel=="yes":
            print("canceling payment......")
            time.sleep(3)
            print("payment is Canceled successfully")
        else:
            print("Processing wait for a moment...")
            time.sleep(3)
            print("Payment is completed successfully...!")
        return
    

choice=input("Enter the payment method for transactions(CreditCard/PayPal/GooglePay): ").strip().lower()

try:
    if choice.capitalize() not in globals():
        raise Exception("Invalid choice, This choice of payment is not available,please try again")
except Exception as e:
    print(e)
else:
    try:
        ch_payment=globals()[choice.capitalize()]    
        payment_method=ch_payment()
        amount=int(input("Enter the amount to make payment: "))
        payment_method.process_payment(amount)
        payment_method.cancel_payment()
    except Exception as e:
        print(f"{e} Some error is occurs during payment")
        
        
            
