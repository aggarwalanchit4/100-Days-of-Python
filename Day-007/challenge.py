#  Challenge 1 - Square Function
# -----------------------------------------

def square(num):
    return num * num

num = int(input("enter number: "))
result = square(num)

print("Square =", result)

# -----------------------------------------
#  Challenge 2 – Even or Odd Function
# -----------------------------------------

def even_odd(number):
    
    if number % 2 == 0 :
        return "even"
    else:
        return "odd"

number = int(input("enter a  number: "))

result = even_odd(number)

print(result)

# -----------------------------------------
#  Challenge 3 – calculator using return
# -----------------------------------------

def multiply(a, b):
    return a*b

a = int(input("enter first number: "))
b = int(input("enter second number: "))

product = multiply(a, b)
print(f"product of {a} and {b} is {product}")