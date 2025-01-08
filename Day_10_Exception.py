
# #Random Function
# # import random as r
# # print(r.randint(1,10))

# # import os
# # print(os.getcwd())

# #GENERATOR
# def mygen(x,y):
#     while x<y:
#         yield x
#         x+=1
# x=mygen(5,10)
# for i in x:
#     print(i)
  
# TASK-> What is decorators and its examples 

#try with mulitple catch(except)
#Raise Exception

  #Raise Exception
# It is user defined exception


# # AssertionError
# try :
#     x=-1
#     y=-2
#     assert x>0 and y>0,"Both numbers should be positive"
#     print("Assertion passed")
# except AssertionError as Ae:
#     print(Ae)
# else:
#     print(f"Addition of {x} and {y} is {x+y}")
# #Assert statement time consuming, 
# # only used for debugging or testing 

#Logging exception
        
import time
from logging import *

def clearLogFiles():
   with open(r'C:\Users\subod\Internship 2024-25\Internship_Work\MyLog.txt','w') as f:
      f.truncate(0)
      print("Log file is cleared")
def configLogs():
   with open(r'C:\Users\subod\Internship 2024-25\Internship_Work\MyLog.txt','a+') as f:
      pass
   basicConfig(filename=r'C:\Users\subod\Internship 2024-25\Internship_Work\MyLog.txt',level=ERROR,format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')
      
def Auth_age(age):
   if age<0:
      raise ValueError("Value cannot be negative")
   if age<18:
      raise Exception("Below 18 age not allowed")
   
clearLogFiles()
configLogs()


try:
   age=int(input("Enter your age: "))
   Auth_age(age)
except ValueError as Ve:
   print(Ve)
   error(f"{Ve} user is checking age and entered negative value",exc_info=True)
except Exception as e:
   error(e,exc_info=True)
else:
   print("Please wait for a while....\n")
   time.sleep(5)
   print("Age is verified Successfully\nAccess Granted")
finally:
   print("Code run successfully..")
   print("Code is cleared after termination")

