# -----------------------------------------
# Day 16 Mini Project — Bank Account System
# -----------------------------------------

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount_depo):
        self.balance = self.balance + amount_depo

    def withdraw(self, amount_drawn):
        self.balance = self.balance - amount_drawn

    def display(self):
        print(f"Name of account holder is {self.name}")
        print(f"Balance of {self.name} is {self.balance}")

name = input("enter name of account holder : ")
balance = int(input("enter balance amount : "))
amount_depo = int(input("enter amount deposited : "))
amount_drawn = int(input("enter amount withdrawn : "))
customer1 = BankAccount(name , balance)
customer1.deposit(amount_depo)
customer1.withdraw(amount_drawn)
customer1.display()