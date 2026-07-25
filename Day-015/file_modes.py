with open("practice.txt", "w") as file:
    file.write("Learning Python File Handling")

with open("practice.txt", "a") as file:
    file.write("\NREACHED FILE HANDLING")
with open("practice.txt", "r") as file:
    print(file.read())
with open("newfile.txt", "x") as file:
    file.write("Hello Python")