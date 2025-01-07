# def printf(str):
#     print(str)

# def add(a,b):
#     return a+b

# def add1(*args):
#     return sum(args)

# def conversion(*args):
#     return [ord(i) for i in args]

# def palindrome(str):
#     revstr=str[::-1]
#     if str==revstr:
#         return "palindrome"
#     else :
#         return "Not palindrome"
# str=input("Enter your string:")
 

def Gross(basic):
    da=basic*80/100
    hra=basic*15/100
    gross=0
    gross=basic+da+hra
    print("gross Salary:",gross)

def netsalary(basic):
   

   
    da=basic*80/100
    hra=basic*15/100
    pf=basic*12/100
    gross=basic+da+hra
    itax=gross*0.1
    netsalary=gross-pf-itax
    print("Net Salary",netsalary)

def DA(basic):
    da=basic*80/100
    print("DA",da)

def HRA(basic):
    hra=basic*15/100
    print("HRA",hra)

def PF(basic):

    pf=basic*12/100
    print("pf",pf)

def ITAX(gross):
    da=basic*80/100
    hra=basic*15/100
    gross=basic+da+hra
    itax=gross*0.1
    print("itax",itax)


if __name__=="__main__":
    # print(add(10,20))
    # print(add1(1,2,3,4,5,6))
    # print(conversion('a','b','c'))
    basic=int(input("Enter your salary:"))
    print(Gross(basic))
    print(netsalary(basic))
    print(DA(basic))
    print(HRA(basic))
    print(PF(basic))
    print(ITAX(basic))

else :
    print("This code is running in other module")