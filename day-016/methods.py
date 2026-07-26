# -----------------------------------------
# Challenge 1 — Create and Call a Method
# -----------------------------------------

class cars :
    def __init__(self , company , model , engine_type):
        self.company = company
        self.model = model 
        self.engine_type = engine_type

    def display(self):

        print(self.company)
        print(self.model)
        print(self.engine_type)

company = input("enter name of car company : ")
model = input("enter model name of car : ")
engine_type = input("enter type of engine : ")

cars1 = cars(company , model , engine_type)

cars1.display()

# -----------------------------------------
# Challenge 2: Method with a Parameter
# -----------------------------------------

class BankAccount :
    def __init__(self , name , balance):
        self.name = name 
        self.balance = balance

    def display(self):
        print(f"Name of account holder: {self.name}")
        print(f"Remaining  balance: {self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount

name = input("enter name of customer : ")
balance = int(input("enter reamining balance: "))
amount = int(input("enter amount deposited : "))
customer1 = BankAccount(name , balance)
customer1.deposit(amount)
customer1.display()

# -----------------------------------------
# Challenge 3 — Method That Returns a Value
# -----------------------------------------

class rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

length = int(input("enter length of rectangle: "))
width = int(input("enter width of rectangle: "))
rectangle1 = rectangle(length , width)

print(f"area of rectangle is {rectangle1.area()} ")