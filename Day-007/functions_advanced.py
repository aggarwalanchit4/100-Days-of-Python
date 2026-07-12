# -----------------------------------------
# Day 7 - Advanced Functions
# -----------------------------------------

def square(num):
    return num * num

result = square(6)

print("Square =", result)


country = "India"

def show_country():
    print(country)

show_country()


def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Anchit")