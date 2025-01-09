# #OOPS Concept
# #Method Overloading in Class Inheritance: Not Supported diectly
# # compiple time,early binding 

# Implement object class methods and its implementation
class Vehicle:
    def __init__(self, model, name, year):
        self.model = model
        self.name = name
        self.year = year

    # __str__: For user-friendly string representation
    def __str__(self):
        return f"Vehicle: {self.name} ({self.model}, {self.year})"

    # __repr__: For developer-friendly string representation
    def __repr__(self):
        return f"Vehicle(model='{self.model}', name='{self.name}', year={self.year})"

    # __eq__: For object equality comparison
    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.model == other.model and self.name == other.name and self.year == other.year
        return False

    # __hash__: To make the object hashable (needed for dictionary or set keys)
    def __hash__(self):
        return hash((self.model, self.name, self.year))

    # __len__: Example of custom len() logic (e.g., length of name string)
    def __len__(self):
        return len(self.name)

    # __del__: Called when the object is deleted
    def __del__(self):
        print(f"Vehicle {self.name} has been deleted.")

# Example usage
vehicle1 = Vehicle("BMW", "X5", 2022)
vehicle2 = Vehicle("Audi", "Q7", 2021)
vehicle3 = Vehicle("BMW", "X5", 2022)

# __str__ and __repr__
print(str(vehicle1))  # Output: Vehicle: X5 (BMW, 2022)
print(repr(vehicle1))  # Output: Vehicle(model='BMW', name='X5', year=2022)

# __eq__
print(vehicle1 == vehicle3)  # Output: True (since their attributes are the same)
print(vehicle1 == vehicle2)  # Output: False

# __hash__
vehicles = {vehicle1: "Owned", vehicle2: "Available"}
print(vehicles[vehicle1])  # Output: Owned

# __len__
print(len(vehicle1))  # Output: 2 (length of the name "X5")

# __del__
del vehicle1  # Output: Vehicle X5 has been deleted.

#Inheritance
#ENCAPSULATION by access modifiers 
class Vehicle:
    def __init__(self, model, name, year):
        self.model = model  
        self.name = name    
        self.year = year    
        self.__owner = "Subodh Wadekar"  # Private attribute notation (__ double underscore)

    def display(self):
        print(f"Vehicle Details: Model: {self.model}, Name: {self.name}, Year: {self.year}")

    # Getter for private owner attribute
    def get_owner(self):
        return self.__owner


class Car(Vehicle):
    def __init__(self, model, name, year, wheels=4, doors=4, engine_capacity=4):
        super().__init__(model, name, year)  
        self.wheels = wheels
        self.doors = doors
        self.engine_capacity = engine_capacity

    def display(self):  
        super().display()  # Call parent class display method
        print(f"Car Details: Wheels: {self.wheels}, Doors: {self.doors}, Engine Capacity: {self.engine_capacity}L")


class ElectricCar(Car):  # Derived from Car
    def __init__(self, model, name, year, battery_capacity):
        super().__init__(model, name, year)
        self.battery_capacity = battery_capacity

    def display(self):  
        super().display()  # Call parent class display method
        print(f"Electric Car Battery Capacity: {self.battery_capacity} kWh")



vehicle = Vehicle("BMW", "M5 Competition", 2007)
vehicle.display()
print(f"Owner: {vehicle.get_owner()}")  # Access private attribute via getter

car = Car("Audi", "R8", 2012)
car.display()

tesla = ElectricCar("Tesla", "Model S", 2021, 100)
tesla.display()

#Getters and setters allow indirect access to these attributes, ensuring the class encapsulates its data properly.
#Polymorphism
class Calculator:
    def add(self, num1=None, num2=None):
        if num1 != None and num2 == None:
            return num1
        elif num1 != None and num2 != None:
            return num1 + num2
        else:
            return "Invalid Input"

calc = Calculator()
print(calc.add(10))       
print(calc.add(10, 20))   


#Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Create a Rectangle object
rectangle = Rectangle(10, 5)
print(f"Area: {rectangle.area()}")  # Output: Area: 50
print(f"Perimeter: {rectangle.perimeter()}")  # Output: Perimeter: 30
