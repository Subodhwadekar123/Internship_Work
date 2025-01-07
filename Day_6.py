#Lambda Function
# lambda arguments:expression
# var= lambda x:x+1  #print(x)
# print(var(1))

# add = lambda num1,num2:num1+num2
# add(2,3)


# #for conditional statements we need to write statement before the if else

# evenOdd= lambda num1: "Even" if num1%2==0 else "Odd"
# print(evenOdd(4))


# #for only expression it give boolean values
# iseven=lambda num : num%2==0 
# print(iseven(4))

# iseven =lambda x:"X is zero" if x==0 else ("x is even" if x%2==0 else "x is odd") #also can add logical operators
# print(iseven(5))

# #Map function in lambda
# #it is used for any given expression whether it having many iteration or not it will apply for all elements
# #higher order function:map()
# lst=[1,2,3,4,5]
# print(list(map(lambda x:x+1 ,lst))) #syntax map

# # function having another function
# def display(n):
#     return n*2
# lst=[1,2,3,4,5,6] 
# print(list(map(display,lst)))  #tuple,set instead of list



# def p(i):
#     return i**2
# tup= (10,20,30,40,50)
# print(list(map(p,tup)))


# def iterableSet(n1,n2):
#     return n1+n2
# lst1=[1,2,3,4,5]
# lst2=[10,11,12,13,14]
# print(tuple(map(iterableSet,lst1,lst2)))

# str=['a','b','c','d']
# print(ord('a')) #ascii value


# #filter function
# lst=[1,2,3,4,5,6,7,78,8,9,12,32,45]
# print(list(filter(lambda x:x>5,lst)))

# list(filter(lambda x:x>5 and x%2==0,lst))


# def agevalid(key,value):
#     if value > 18 :
#         print( f"{key} is Valid person for voting")
#     else :
#         print( f"{key} is Invalid person for voting")
        
# dic={'def':15,'ssw':19,'abc':21}
# agevalidity=dict(filter(lambda x:agevalid(x[0],x[1]),dic.items()))
# print(agevalidity)



tuples=[(1,3),(4,2),(2,5)]
sort=sorted(tuples,key=lambda x:x[1])
print(f"List before sorting:{tuples}")
print(f"sorted list is :{sort}")

maxi=[4,7,9,2,67,12,99]
maximum=max(maxi,key=lambda x:x)
print(f"maximum number from {maxi} is {maximum}. " )

pali=lambda x:"String is palindrome" if x==x[::-1] else "String is not palindrome"
str1=input("Enter the string in lowercase:")
print(pali(str1))


#MODULES AND PACKAGES
# import math
# print(math.sqrt(81))


