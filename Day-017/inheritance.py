# -----------------------------------------
# Challenge 1 — Basic Inheritance
# -----------------------------------------

class Animal :
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    pass
dog1 = Dog()
dog1.eat()

# -----------------------------------------
# Challenge 2 — Parent and Child Methods
# -----------------------------------------

class Vehicle :
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def Drive(self):
        print("car is driving")
    pass

Car1 = Car()

Car1.start()

Car1.Drive()

# -----------------------------------------
# Challenge 3 — Inheriting Constructor
# -----------------------------------------

class Person:
    def __init__(self , name , age):
        self.name = name 
        self.age = age 
    def display(self):
        print(f"Name of person is {self.name} ")
        print(f"Age of {self.name} is {self.age}")
class Student(Person):
    pass

name = input("enter name of student : ")
age = int(input(f" enter age of {name} : "))
Student1 = Student(name , age)
Student1.display()
