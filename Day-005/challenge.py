#  Challenge 1 - Print numbers from 1 to 10
# -----------------------------------------

for i in range(1,11,1):
    print(i)

# -----------------------------------------
# Challenge 2 - Multiplication Table
# -----------------------------------------

y = int(input("enter a number: "))

for i in range(1 , 11):
    product = y*i
    print(f"{y} x {i} = {product}")

# -----------------------------------------
# Challenge 3 - Sum of Natural Numbers
# -----------------------------------------

number = int(input("Enter a number: "))
total = 0 

for i in range(number , 0 , -1):
    total = i + total

print(total)

# -----------------------------------------
# Challenge 4 - Password with 3 Attempts
# -----------------------------------------

password = input("Enter your password: ")

if password == "python123":
    print("Correct password! Entry approved.")

else:
    count = 2

    while count >= 0:
        password = input("Enter password again: ")

        if password == "python123":
            print("Correct password! Entry approved.")
            break

        count -= 1

        if count >= 0:
            print(f"Wrong password! {count + 1} attempt(s) left.")

        if count < 0:
            print("Access Denied")