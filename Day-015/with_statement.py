with open("message.txt", "w") as file:
    file.write("Learning Python File Handling")

with open("message.txt", "r") as file:
    print(file.read())