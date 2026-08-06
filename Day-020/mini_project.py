# -----------------------------------------
# Day 20 Mini Project — Employee Salary Management System
# -----------------------------------------


from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):

    def salary(self):
        print(f"{self.name}'s Salary = ₹80,000")


class Developer(Employee):

    def salary(self):
        print(f"{self.name}'s Salary = ₹60,000")


manager = Manager(input("Enter Manager Name: "))
developer = Developer(input("Enter Developer Name: "))

manager.salary()
developer.salary()