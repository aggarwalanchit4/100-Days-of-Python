# -----------------------------------------
# Challenge 1 - Access List Elements
# -----------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# -----------------------------------------
# Challenge 2 - Create a List from User Input
# -----------------------------------------

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print(numbers)

# -----------------------------------------
# Challenge 3 - Append an Element
# -----------------------------------------

numbers = list(map(int, input().split()))
x = int(input("enter number to insert"))
numbers.append(x)
print(numbers)

# -----------------------------------------
# Challenge 4 – Sort a List
# -----------------------------------------

numbers = list(map(int, input().split()))
    
numbers.sort()

print(numbers)