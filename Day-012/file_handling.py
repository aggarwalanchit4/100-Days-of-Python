# -----------------------------------------
# Day 12 - File Handling
# -----------------------------------------

with open("data.txt", "w") as file:
    file.write("Hello Python")

with open("data.txt", "a") as file:
    file.write("\nWelcome")

with open("data.txt", "r") as file:
    print(file.read())