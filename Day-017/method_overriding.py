# -----------------------------------------
# Challenge 1 — Basic Method Overriding
# -----------------------------------------

class Vehicle :
    def move(self):
        print("veicle is moving")

class Car(Vehicle):
    def move(self):
        print("car is driving")

Vehicle1 = Vehicle()
Car1 = Car()
Car1.move()
Vehicle1.move()

# -----------------------------------------
# Challenge 2 — Override display()
# -----------------------------------------

class Person:
    def display(self):
        print("I am a person")

class Student(Person):
    def display(self):
        print("I am a student")

Student1 = Student()
Person1 = Person()
Person1.display()
Student1.display()
