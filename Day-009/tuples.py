# -----------------------------------------
# Day 9 - tupples
# -----------------------------------------

numbers = tuple(map(int, input("enter numbers: ").split()))
print(numbers)

print(numbers[0])
print(numbers[-1])

print(numbers[1:3])

print(numbers.count(20))
print(numbers.index(30))

student = ("Anchit", 20, "CSE AI")

name, age, branch = student

print(name)
print(age)
print(branch)