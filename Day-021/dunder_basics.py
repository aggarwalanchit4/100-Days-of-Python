# -----------------------------------------
# Challenge 1 - Dunder Methods Basics
# -----------------------------------------

class Student:

    def __init__(self, name, age):
        self.name = name 
        self.age = age 
   
name = input("enter your name : ")
age = int(input("enter your age : "))
student = Student(name , age)
print(student)