with open("student.txt", "w") as file:
    file.write("Name : Anchit\n")
    file.write("Age : 19\n")
    file.write("Course : B.Tech CSE AI\n")
with open("student.txt", "a") as file:
    file.write("City : Saharanpur")
with open("student.txt", "r") as file:
    print(file.read())