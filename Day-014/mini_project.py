import random

secret = random.randint(1, 100)
attempts = 0

print("=== Number Guessing Game ===")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret:
        print("Too Low!")
    elif guess > secret:
        print("Too High!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break