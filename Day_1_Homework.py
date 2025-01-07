    #Datatypes identification
num=10
print(type(num))

name="Subodh"
print(type(name))

fnum=45.20
print(type(fnum))

#type castingtype conversion

#int()

a=int(10.5)
print(a)

b=int("1234")
print(b)

#float()
c=float(100)
print(c)

#str()
d=str("12345")
print(d)

#Boolean()
x=bool(1)
y=bool(0)
z=bool("")
print(x,y,z)

#list()
li1=list("Hello World")
li2=list((1,2,3,4))
print(li1)
print(li2)

#tuple()
tup1=tuple("Hello")
tup2=tuple([1,2,3])
print(tup1)
print(tup2)

#set()
set1 = set([1, 2, 2, 3]) 
set2 = set("hello")  
print(set1)
print(set2)

#dict()
dict1 = dict([(1, 'a'), (2, 'b')])  
dict2 = dict({'key1': 'value1', 'key2': 'value2'})  
print(dict1)
print(dict2)

#F-string
name = "Subodh"
age = 19
print(f"My name is {name} and I am {age} years old.")

pi = 3.14159
print(f"Value of pi: {pi:.2f}")  # Round to 2 decimal places

#OPERATORS
#ARITHMETIC OPERATORS 
x, y = 10, 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#COMPARISON OPERATORS
x, y = 5, 5
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#LOGICAL OPERATORS
x, y = True, False
print(x and y)
print(x or y)
print(not x)

#BITWISE OPERATORS
print("Bitwise operators")
x, y = 5, 3
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 1)
print(x >> 1)

#Assignment Operators
print("Assignment operators")
x = 5

x += 3
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 3
print(x)
x %= 2
print(x)
y=12.70
y //= 3
print(y)
y **= 2
print(y)

#Membership oprators
print("Membership Operators")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)
print(x is not y)


fruits = ['apple', 'banana']
print('apple' in fruits)
print('banana' not in fruits)
