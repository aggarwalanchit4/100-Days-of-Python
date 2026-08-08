# -----------------------------------------
# Challenge 1 – Implement __add__() Method
# -----------------------------------------

class Number:
    def __init__(self , number1):
        self.number1 = number1
    def __add__(self, other):
        return self.number1 + other.number1

number1 = int(input("enter first number : "))
number2 = int(input("enter second number : "))\
num1 = Number(number1)
num2 = Number(number2)
print(num1 + num2)