#OOPS Concept

class Vehicle:
    def __init__(self,model,name,year,owner):
        self.model=model
        self.name=name
        self.year=year
        #private use dbl underscore
        #protected use single underscore
        self.__owner="Subodh Wadekar"

    def display(self):
        print(f"Details:Car Model:{self.model},{self.name},{self.year},{self.owner}")
    def add(self,num1=None,num2=None):
        if num1!=None and num2== None:
            print(num1)
        if num1!=None and num2!=None:
            print(num1+num2)
    def __repr__(self):
        return f"Details:Car Model:{self.model},{self.name},{self.year}"

obj=Vehicle("BMW","M5 compitition",2007)
obj1=Vehicle("Audi","R8",2012)
obj.display()
obj1.display()
#Method Overloading: Not Supported diectly
# compiple time,early binding 
# obj.add(10,20)
# obj.add(10)
# print(obj)
# #Implement object class methods and its implementation
# print(id(obj))
# print(id(obj1))
# print(obj.owner)
#Encapsulation
#Inheritance
#types of inheritance:
#single
#only one subclass/child class
class Car(Vehicle):
    def __init__(self, model, name, year, owner):
        super().__init__(model, name, year, owner)
        self.wheels=4
        self.doors=4
        self.engineCapacity=4
    def display(self):
        print(f"Car details:{self.wheels},{self.doors},{self.engineCapacity}")
car=Car()
print(car.__owner)
car.display()
#Multilevel


#Hierarchical
#Hybrid


#multiple


