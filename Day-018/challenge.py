# -----------------------------------------
# Challenge 1 — Student Property Decorator
# -----------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")

    def display(self):
        print(f"Student Name : {self.name}")
        print(f"Marks : {self.__marks}")


name = input("Enter student name: ")
marks = int(input(f"Enter marks of {name}: "))

student1 = Student(name, marks)

print("\nCurrent Details")
student1.display()

new_marks = int(input("\nEnter new marks: "))

student1.marks = new_marks

print("\nUpdated Details")
student1.display()

