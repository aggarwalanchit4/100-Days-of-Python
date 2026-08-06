# -----------------------------------------
# Practical Example
# -----------------------------------------

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):

    def salary(self):
        print("Salary = ₹80,000")


class Developer(Employee):

    def salary(self):
        print("Salary = ₹60,000")


manager = Manager()
developer = Developer()

manager.salary()
developer.salary()