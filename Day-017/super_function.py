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