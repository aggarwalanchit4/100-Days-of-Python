# -----------------------------------------
# Challenge 1: Safe Division Using Exception Handling
# -----------------------------------------
try:
    num_1 = int(input("enter first number: "))
    num_2 = int(input("enter second number: "))
    division = num_1/num_2
    print(division)
except ZeroDivisionError:
    print("not divisible by zero")

except ValueError:
    print("Please enter valid integers.")

# -----------------------------------------
# Challenge 2: Handle Invalid Integer Input
# -----------------------------------------

try:
    num_1 = int(input("enter first number: "))
    print(f"you entered {num_1}")

except ValueError:
    print("Please enter valid integers.")

# -----------------------------------------
# Challenge 3: Open a File Safely
# -----------------------------------------

try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("file not found")


# -----------------------------------------
# Challenge 4: Simple Calculator Using Exception Handling.
# -----------------------------------------
try:
    num_1 = int(input("enter first number: "))
    num_2 = int(input("enter second number: "))
    total = num_1 + num_2
    product = num_1*num_2
    difference = num_2 - num_1
    quotient = num_1/ num_2
    print(f"The sum , product , difference and quotient of {num_1} and {num_2} are {total} , {product} , {difference} , {quotient} respectively ")
except ValueError:
    print("enter integers only")
except ZeroDivisionError:
    print("number not divisible by zero")
