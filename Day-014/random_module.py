# -----------------------------------------
# Challenge 1: Random Number Generator
# -----------------------------------------

import random

a = int(input("Enter starting value: "))
b = int(input("Enter ending value: "))

print("Random Number:", random.randint(a, b))

# -----------------------------------------
# Challenge 2: Random Choice
# -----------------------------------------

fruits = list(map(str, input("enter name of fruits : ").split()))
print("Random fruit :", random.choice(fruits))