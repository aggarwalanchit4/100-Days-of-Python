import calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition      :", calculator.add(num1, num2))
print("Subtraction   :", calculator.subtract(num1, num2))
print("Multiplication:", calculator.multiply(num1, num2))
print("Division      :", calculator.divide(num1, num2))


import greetings

name = input("Enter your name: ")

greetings.greet(name)
greetings.morning(name)
greetings.afternoon(name)
greetings.evening(name)
greetings.goodbye(name)