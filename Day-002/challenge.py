# Challenge 1 - User Information
# ------------------------------------------
name = input("Enter your name :")
age = int(input("Enter your age : "))
height = float(input("Enter your height : "))
print("Hello,", name)
print("You are", age, "years old.")
print("You are", height, "cm tall.")

print(type(name))
print(type(age))
print(type(height))

# ------------------------------------------
# Challenge 2 - Simple Calculator
# ------------------------------------------
x = int(input("enter first number : "))
y = int(input("Enter second number :"))
total = x + y
mutiplication = x * y
subtraction  = x - y
division = x/y
average = (x + y) / 2
print(f"The sum of x and y is : {total}")
print(f"The product of x and y is : {mutiplication}")
print(f"The difference of x and y is : {subtraction}")
print(f"The quotient of x and y is : {division}")
print(f"The average of x and y is : {average}")
# ------------------------------------------