# -----------------------------------------
# Day 8 - Lists
# -----------------------------------------

# Creating a List
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# -----------------------------------------
# Accessing Elements
# -----------------------------------------

print("First Element:", numbers[0])
print("Third Element:", numbers[2])

# -----------------------------------------
# Negative Indexing
# -----------------------------------------

print("Last Element:", numbers[-1])
print("Second Last Element:", numbers[-2])

# -----------------------------------------
# List Slicing
# -----------------------------------------

print("Slice (1:4):", numbers[1:4])
print("First Three:", numbers[:3])
print("From Index 2:", numbers[2:])

# -----------------------------------------
# Updating an Element
# -----------------------------------------

numbers[1] = 200
print("Updated List:", numbers)

# -----------------------------------------
# append()
# -----------------------------------------

numbers.append(60)
print("After append():", numbers)

# -----------------------------------------
# insert()
# -----------------------------------------

numbers.insert(2, 25)
print("After insert():", numbers)

# -----------------------------------------
# remove()
# -----------------------------------------

numbers.remove(25)
print("After remove():", numbers)

# -----------------------------------------
# pop()
# -----------------------------------------

numbers.pop()
print("After pop():", numbers)

# -----------------------------------------
# sort()
# -----------------------------------------

values = [40, 10, 30, 20]
values.sort()
print("Sorted List:", values)

# -----------------------------------------
# reverse()
# -----------------------------------------

values.reverse()
print("Reversed List:", values)