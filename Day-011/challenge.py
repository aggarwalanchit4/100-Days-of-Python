# -----------------------------------------
# Challenge 1 – Create a Set
# -----------------------------------------

numbers = set(map(int, input("enter numbers in set: ").split()))
print(numbers)

# -----------------------------------------
# Challenge 2 – Add an Element
# -----------------------------------------

numbers = set(map(int, input("enter numbers in set: ").split()))
x = int(input("enter a number to be added to set : "))

numbers.add(x)
print(numbers)

# -----------------------------------------
# challenge 3 – Remove an Element
# -----------------------------------------

numbers = set(map(int, input("enter numbers in set: ").split()))
x = int(input("enter a number to be removed to set : "))

numbers.remove(x)

print(numbers)

# -----------------------------------------
# Challenge 4 – Union and Intersection
# -----------------------------------------

a = set(map(int, input("Enter first set: ").split()))
b = set(map(int, input("Enter second set: ").split()))

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))