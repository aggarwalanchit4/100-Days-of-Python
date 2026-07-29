# -----------------------------------------
# Challenge 1 — Using super()
# -----------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter student course: ")

student1 = Student(name, age, course)

student1.display()

# -----------------------------------------
# Challenge 2 — super() with a Method
# -----------------------------------------

class Vehicle:
    def __init__(self , type , name , engine_type):
        self.type = type
        self.name = name
        self.engine_type = engine_type
    def display(self):
        print("This is a vehicle")

class Car(Vehicle) :
    def __init__(self, type, name, engine_type , model_name):
        super().__init__(type, name, engine_type)
        self.model_name = model_name
    def display(self):
        super().display()
        print(f"vehicle type : {self.type}")
        print(f"Name : {self.name}")
        print(f"model name :{self.model_name} ")
        print(f"engine type  : {self.engine_type}")
        
type = input("enter vehicle type : ")
name = input("enter vehicle brand name : ")
engine_type = input("enter engine type : ")
model_name = input("model name : ")
Car1 = Car(type , name , engine_type , model_name)
Car1.display()

