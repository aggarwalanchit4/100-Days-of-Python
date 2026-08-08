# -----------------------------------------
# Challenge 1 – Implement __str__() Method
# -----------------------------------------

class Student:

```
def __init__(self, name, age):
    self.name = name 
    self.age = age 
def __str__(self):
    return f"{self.name} {self.age}"
def 
```

name = input("enter your name : ")
age = int(input("enter your age : "))
student = Student(name , age)
print(student)