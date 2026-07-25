# -----------------------------------------
# Challenge 1: Write User Input to a File
# -----------------------------------------

name = input("Enter your name: ")
course = input("Enter your course: ")
with open("introduction.txt","w") as file:
    file.write(f"My name is {name}.")
    file.write(f"\nI am doing {course}.")

# -----------------------------------------
# Challenge 2: Append Data to a File
# -----------------------------------------

location = input("Enter your city: ")
with open("introduction.txt","a") as file:
    file.write(f"\nI am from {location}.")

# -----------------------------------------
# Challenge 3: Read and Display File
# -----------------------------------------

with open("introduction.txt","r") as file:
    print(file.read())

# -----------------------------------------
# Challenge 4: Count Lines in a File
# -----------------------------------------

with open("introduction.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))

# -----------------------------------------
# Challenge 5: Read a Specific Line
# -----------------------------------------

x = int(input("enter line number to read: "))
with open("introduction.txt", "r") as file:
    lines = file.readlines()
    print([lines[x-1]])

# -----------------------------------------