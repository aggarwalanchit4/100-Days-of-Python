# -----------------------------------------
# Day 10 - Dictionaries
# -----------------------------------------

student = {
    "name": "Anchit",
    "age": 20,
    "branch": "CSE AI"
}

print(student)

print(student["name"])
print(student["age"])

student["age"] = 21

student["college"] = "NIET"

print(student)

print(student.keys())
print(student.values())
print(student.items())

print(student.get("branch"))

student.pop("college")

print(student)