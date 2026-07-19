try:
    numbers = list(map(int, input("enter numbers in list : ").split()))
    divisor = int(input("Enter divisor: "))
    index = int(input("enter index: "))
    print(numbers[index] / divisor)

except ValueError:
    print("Value Error")

except ZeroDivisionError:
    print("Division by Zero")

except IndexError:
    print("Index Error")