#  Challenge 1 - Voting Eligibility
# -----------------------------------------
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# -----------------------------------------
#  Challenge 2 - Even or Odd
# -----------------------------------------
number = int(input("Enter a number: "))
if number%2 == 0:
    print(f"{number} is even")
else :
    print(f"{number} is odd")
# -----------------------------------------
#  Challenge 3 - password checker
# -----------------------------------------
password = (input("Enter a password: "))
if password == "python123" :
    print("Access Granted")
else:
    print("Access Denied")
# -----------------------------------------
#  Challenge 4 - Grade Calculator
# -----------------------------------------
marks = int(input("Enter your marks: "))
if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks < 90 :
    print("Grade B")
elif 70 <= marks < 80 :
    print("Grade C")
elif 60 <= marks < 70 :
    print("Grade D")
else :
    print("Fail")
# -----------------------------------------