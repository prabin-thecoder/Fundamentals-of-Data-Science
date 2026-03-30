# Q10_game.py

import random

secret = random.randint(1, 50)
attempts = 7

for i in range(attempts):
    guess = int(input("Guess the number (1-50): "))

    if guess == secret:
        print("Correct! You win!")
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")
else:
    print("Better luck next time! The number was:", secret)