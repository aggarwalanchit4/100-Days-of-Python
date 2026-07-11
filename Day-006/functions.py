# -----------------------------------------
# Day 6 - Functions
# -----------------------------------------

def greet():
    print("Welcome to Python!")

greet()

# -----------------------------------------

def greet_user(name):
    print(f"Hello, {name}")

greet_user("Anchit")

# -----------------------------------------

def add(a, b):
    print(f"Sum = {a + b}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add(a,b)

# -----------------------------------------

def square(number):
    return number * number

result = square(5)

print("Square =", result)
# -----------------------------------------