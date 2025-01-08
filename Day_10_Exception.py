
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


# AssertionError
try :
    x=-1
    y=-2
    assert x>0 and y>0,"Both numbers should be positive"
    print("Assertion passed")
except AssertionError as Ae:
    print(Ae)
else:
    print(f"Addition of {x} and {y} is {x+y}")




        