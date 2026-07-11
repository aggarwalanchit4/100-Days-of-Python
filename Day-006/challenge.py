#  Challenge 1 - Greeting Function
# -----------------------------------------

def greet():
    print("Good Morning!")

greet()
greet()
greet()

# -----------------------------------------
#  Challenge 2 – User Greeting
# -----------------------------------------

def greet(name):
    print(f"Good Morning {name}!")

name = input("Enter your name: ")

greet(name)

# -----------------------------------------
#  Challenge 3 - Calculator Function
# -----------------------------------------

def add(a, b):
    total = a + b
    print(f"Sum of {a} and {b} is {total}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add(a, b)

# -----------------------------------------
#  Challenge 4 - Area of rectangle
# -----------------------------------------
def area(l,b):
    product = l*b
    print(f"Area of rectangle is: {product} units")

l = int(input("enter length of rectangle: "))
b = int(input("enter breadth of rectange: "))

area(l,b)