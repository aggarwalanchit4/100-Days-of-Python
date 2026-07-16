# -----------------------------------------
# Day 11 - Sets
# -----------------------------------------

numbers = {10, 20, 20, 30}

print(numbers)

numbers.add(40)
print(numbers)

numbers.remove(20)
print(numbers)

numbers.discard(100)
print(numbers)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print(2 in a)
print(5 in a)