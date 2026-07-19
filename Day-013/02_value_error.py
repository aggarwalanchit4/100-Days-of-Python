try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    print(num_1 / num_2)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
