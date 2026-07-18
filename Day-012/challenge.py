# -----------------------------------------
# Challenge 1 – Write to a File
# -----------------------------------------

sentence = input("write a sentence: ")
with open("data.txt", "w") as file:
    file.write(sentence)

print("data entered successfully")

# -----------------------------------------
# Challenge 2 - read a file
#  -----------------------------------------

sentence = input("write a sentence: ")
with open("data.txt", "w") as file:
    file.write(sentence)

with open("data.txt", "r") as file:   
    print(file.read())

# -----------------------------------------
# Challenge 3 – Append to a File
# ------------------------------------------
    
sentence = input("write a sentence: ")
with open("data.txt", "a") as file:   
    file.write(f"\n{sentence}")
with open("data.txt", "r") as file:   
    print(file.read())

# -----------------------------------------
# Challenge 4 — Count Characters
# ------------------------------------------

with open("data.txt", "r") as file:   
    text = file.read()
    
    count = 0 
    for char in text :
        count +=1

print(count)

# -----------------------------------------
# Challenge 5 — Count Words
# ------------------------------------------

with open("data.txt", "r") as file:   
    text = file.read()
    words = text.split()
    count = 0 
    for word in words :
        count +=1

print(count)
