#Multiple Inheritance
# one child having multiple parents
#multiple parents are not accessible by child class
# so we use object as parent class to access the parent class B
# class A(object):
#     def __init__(self):
#         self.a='a'
#         print(f"Inside the class A:{self.a}")
#         super().__init__()
#     def display(self):
#             print(f"Inside display method of class A")
# class B(object):
#     def __init__(self):
#         self.b='b'
#         print(f"Inside the class B:{self.b}")
#         super().__init__()
#     def display(self):
#         print(f"Inside display method of class B")
# class C(A,B):
#     def __init__(self):
#       self.c='c'
#       print(f"Inside the class C:{self.c}")
#       super().__init__()
#     def display(self):
#         print(f"Inside display method of class C")
#         super().display()

# c=C()
# c.display()


# TASK
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Show_Details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):  
    def __init__(self, name, age,game):
        super().__init__(name, age,game) 
    def StudentDetails(self):
        print(f"Student Name: {self.name}, Age: {self.age} is studying")

class SportsPlayer(Person):  
    def __init__(self, name, age, game):
        super().__init__(name, age)  
        self.game = game
    def Play_sport(self):
        print(f"Player Name: {self.name}, Age: {self.age}, Game: {self.game}")

class StudentAthlete(Student, SportsPlayer): 
    def __init__(self, name, age, game):
        # SportsPlayer.__init__(self, name, age, game)
        # Student.__init__(self, name, age,game)
        super().__init__(name, age, game)

    def Show_Athlete_Details(self):
        print(f"Name: {self.name}, Age: {self.age},playing the Game: {self.game}")


s = StudentAthlete("Subodh", 22, "Cricket")
s.Show_Athlete_Details()
s.StudentDetails()
s.Play_sport()
