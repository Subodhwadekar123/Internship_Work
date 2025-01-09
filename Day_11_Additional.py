#Decorators
# Decorators in Python are a powerful tool that allows you to modify or extend the behavior of a function or method without changing its actual code. A decorator is essentially a function that wraps another function, adding some functionality before or after the wrapped function is executed.
# Decorators are often used in scenarios like logging, access control, performance measurement, or input validation.
# used by notation @decorator_name
# Applying the decorator
# Simple decorator function
def greeting_decorator(func):
    def wrapper(name):
        print("Preparing to greet...")
        func(name)
        print("Greeting complete!")
    return wrapper

@greeting_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("PREC")

#relationships describe the connections between classes in Object-Oriented Programming (OOP).
# to designing robust, modular, and maintainable systems.

# Types of Relationships
# Association:uses-a
# Aggregation:has-a
# Composition:contains-a
# Inheritance:is-a

# Association-> it has a "uses-a" relationship between classes.
class Student:
    def __init__(self, name):
        self.name = name

    def attend_class(self, classroom):
        print(f"{self.name} is attending {classroom.room_name} class.")

class Classroom:
    def __init__(self, room_name):
        self.room_name = room_name

# Example usage
student = Student("Subodh")
classroom = Classroom("Python-101")
student.attend_class(classroom)

# Aggregation
# Aggregation is a "has-a" relationship between classes. It represents a part-whole or a "has-a" relationship between objects. means a library has books, but the books can exist independently of the library.
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.title)

# Example usage
book1 = Book("1984")
book2 = Book("To Kill a Mockingbird")
library = Library()
library.add_book(book1)
library.add_book(book2)
library.show_books()

# Composition
# composition havea "contains-a" relationship between classes. means a car has an engine, and the engine is an essential part of the car. 
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)  # Composition

    def show_details(self):
        print(f"Car Model: {self.model}, Engine Horsepower: {self.engine.horsepower}")

# Example usage
car = Car("Tesla Model S", 670)
car.show_details()

# Inheritance
# Inheritance is an "is-a" relationship between classes. means a dog is an animal, and a cat is an animal.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Example usage
dog = Dog()
dog.speak()

# Dependency