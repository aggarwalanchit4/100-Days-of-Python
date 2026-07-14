# -----------------------------------------
# Challenge 1 -  Access Tuple Elements
# -----------------------------------------

games = tuple(input("enter name of games: ").split())
print(games[0])
print(games[-1])

# -----------------------------------------
# Challenge 2 – Tuple Length
# -----------------------------------------

numbers = tuple(map(int, input("enter numbers: ").split()))
print(len(numbers))

# -----------------------------------------
# Challenge 3 – Count an Element
# -----------------------------------------

numbers = tuple(map(int, input("enter numbers: ").split()))
count_num = 0
search_num = int(input("enter element to count: "))
for num in numbers:
    if num == search_num :
        count_num +=1

print(f"{search_num} appears {count_num} times .")

# -----------------------------------------
# Challenge 4 – Tupple unpacking
# -----------------------------------------

student = tuple(input("Enter data: ").split())
name , age , branch = student
print(name)
print(age)
print(branch)