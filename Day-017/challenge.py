# -----------------------------------------
# Challenge 1 — Employee Inheritance
# -----------------------------------------

class Employee:
    def __init__(self ,name , salary):
        self.name = name 
        self.salary = salary
    def display(self):
        print(f"Employee name : {self.name}")
        print(f"Employee salary : {self.salary}")
class Developer(Employee):
    def __init__(self , name , salary , language):
        super().__init__(name , salary )
        self.language = language
    def display(self):
        print(f"Developer language : {self.language}")
        super().display()
name_employee = input("Enter name of employee : ")
salary_employee = int(input(f"Salary of {name_employee} : "))

name_developer = input("Enter name of developer : ")
salary_developer = int(input(f"Salary of {name_developer} : "))
language = input("enter language of developer : ")

Employee1 = Employee(name_employee , salary_employee)
Developer1 = Developer(name_developer , salary_developer , language)

Employee1.display()
Developer1.display()

# -----------------------------------------
# Challenge 2 — Bank Account Inheritance
# -----------------------------------------

class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance 

    def display(self):
        print(f"Name of accountholder : {self.name}")
        print(f"Balance of {self.name} : {self.balance}")

class savingsaccount(BankAccount):
    def __init__(self, name , balance , intrest ,new_balance):
        super().__init__(name , balance)
        self.intrest = intrest
        self.new_balance = new_balance

    def display(self):
        super().display()
        print(f"intrest rate : {self.intrest}%")
        print(f"new balance : {self.new_balance}")

name = input("enter name of accountholder : ")

balance = int(input(f"enter balance of {name} : "))

intrest = int(input("enter intrest rate : "))

new_balance = (balance*intrest/100) + balance

savingsaccount1 = savingsaccount(name , balance , intrest , new_balance)

savingsaccount1.display()

# -----------------------------------------
# Challenge 3 — Gaming Character Inheritance 🎮
# -----------------------------------------

class Character:
    def __init__(self , name , health):
        self.name = name 
        self.health = health
    def display(self):
        print(f"Hi! I am {self.name}")
        print(f"My health stats are : {self.health}")
class Warrior(Character):
    def __init__(self, name, health , weapon , damage):
        super().__init__(name, health)
        self.weapon = weapon
        self.damage = damage
    def display(self):
        super().display()
        print(f"My favourite weapon is {self.weapon}")
        print(f"Damage of {self.weapon} is {self.damage}")
name_character = input("Enter name of character : ")
health_character = int(input(f"Enter health of {name_character} : "))
name_warrior = input("Enter name of warrior : ")
health_warrior = int(input(f"Enter health of {name_warrior} : "))
weapon_warrior = input(f"Enter name of {name_warrior}'s weapon : ")
damage_warrior = int(input(f"Enter damage of {weapon_warrior} : "))
Character1 = Character(name_character , health_character)
Warrior1 = Warrior(name_warrior , health_warrior , weapon_warrior , damage_warrior)
Character1.display()
Warrior1.display()