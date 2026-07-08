# Challenge 1 - Take the user's name.
# ------------------------------------------
name = input("Enter users name: ")
print("original : " ,name)
print("Length of name is :",len(name))
print("uppercase :",name.upper())
print("lowercase :",name.lower())
# ------------------------------------------
#  Challenge 2 - asks the user to enter a sentence.
# ------------------------------------------
Sentence = input("Enter a sentence: ")
print(f"Original :{Sentence}")
print(f"Length :{len(Sentence)}")
print(f"Uppercase :{Sentence.upper()}")
print(f"Lowercase :{Sentence.lower()}")
print(f"Title Case : {Sentence.title()}")
# ------------------------------------------
#  Challenge 3 -
#Takes the user's last name.
#Combines them into a full name.
# ------------------------------------------
first_name = input("Enter first name: ")
last_name  = input("Enter last name: ")
full_name  = (f"{first_name} {last_name}")
print(f"Full Name           : {full_name}")
print(f"Name uppercase      : {full_name.upper()}")
print(f"Name Lowercase      : {full_name.lower()}")
print(f"Length of full name : {len(full_name)}")
# ------------------------------------------