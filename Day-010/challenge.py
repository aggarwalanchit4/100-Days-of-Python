# -----------------------------------------
# Challenge 1 -  Access Dictionary Values
# -----------------------------------------

student = {
    "name": "Anchit",
    "age": 20,
    "branch": "CSE AI"
}

print(student["name"])
print(student["branch"])

# -----------------------------------------
# Challenge 2 – Update Dictionary
# -----------------------------------------

student = {
    "name": "Anchit",
    "age": 20
}
student["age"] = 21
print(student)

# -----------------------------------------
# Challenge 3 – Add a New Key
# -----------------------------------------

student = {
    "name": "Anchit"
}

student["college"] = "NIET"

print(student)

# -----------------------------------------
# Challenge 4 – Display Keys, Values and Items
# -----------------------------------------

student = {
    "name": "Anchit",
    "age": 20,
    "branch": "CSE AI"
}

print(student.keys())
print(student.values())
print(student.items())