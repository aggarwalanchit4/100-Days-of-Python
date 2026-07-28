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

# -----------------------------------------
# Challenge 3 — Overriding with Attributes
# -----------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee : {self.name}")
        print(f"Salary : {self.salary}")

class Manager(Employee):
    def display(self):
        print(f"Manager : {self.name}")
        print(f"Salary : {self.salary}")

employee_name = input("Enter employee name: ")
employee_salary = int(input("Enter employee salary: "))

manager_name = input("Enter manager name: ")
manager_salary = int(input("Enter manager salary: "))

Employee1 = Employee(employee_name , employee_salary)
Manager1 = Manager(manager_name , manager_salary)
Employee1.display()
Manager1.display()