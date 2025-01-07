#functions

# def funct():#funct() is known as signature
#     pass
# #def funct(name):
#function overloading is directly not possible


#default argument should be written at last end


#variable length argumets

#*args type is tuple


#for other datatypes we hsve keyword var length arg

# def numbers(**kwargs):
#     for key,values in kwargs.items() :
#         print(f"{key} ,{values}")
# numbers('name''Ssw','no':"1223345")


# def multi(*params):
#     sum=1
#     for i in params:
#         sum*=i
#     return sum
# print(multi(1,2,3,4,5,6))


#return multiple values

# def nums():
#     return 10,20
# print(nums())
#a,b=10,20 #a,b=nums(10,20)
# print(a)
# print(b)


# def tryargs(*para, **kwargs):
#     print(para)
#     print(kwargs)
# tryargs(1,2,3,4,age=25,name='subodh')
   




#   2a
# def sums(*para):
#     return sum(para)
# print(sums(10,20))


#   2b
# def string(*para):
#     return len(para)
# print(string("SSW",'abc','xyz'))


#   2c
# def numsquare(a):
#     return a*a
# print(numsquare(10))


#   3a
# def outer_fun(a):
#    def inner_fun():
#         return a**2
#    print(inner_fun())
# outer_fun(10)

#   3b
# def calculate_area(rad):
#     return  3.14*rad**2
# def calc_circumference(rad):
#     pi=3.14
#     return 2*pi*rad
# print(calc_circumference(5))
# print(calculate_area(5))

#palindrome

# def palindrome(str1):
#     revstr=str1[::-1]
#     if str1==revstr:
#         return "Palindrome"
#     else :
#         return "Not Palindrome"
# str1=input("Enter the string:")
# print(f"The string {str1} is {palindrome(str1)}")


#   4a

# def sum_all(*para):
#     return sum(para)
# print(sum_all(10,20))
#   4b
# def print_details(*args,**kwargs):
#     print("variable length argument:",args)
#     print("Keyword argument:")
#     for key,value in kwargs.items():
#         print(f"{key}:{value}") 
# print_details(1,2,3,4,5,age=25,name='subodh',address='pune')

# #   4C
# def describe_person(*args,**kwargs):
#     first_name,last_name=args
#     age=kwargs.get('age')
#     address=kwargs.get('address')
#     print(f"Hello my name is {first_name} {last_name} and currently I am {age} year old and live in {address}. ")
# describe_person('Subodh' ,'Wadekar',age=19,address='Sakur, Sangamner')
  