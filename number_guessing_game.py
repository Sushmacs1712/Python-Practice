import random

number = random.randint(1, 100)
attempts = 0

print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100")
        continue

    attempts += 1

    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("Congratulations! You guessed the number.")
        print("Attempts taken:", attempts)
        break