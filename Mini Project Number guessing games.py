print("Mini Project Number guessing games")

import random

secret = random.randint(1,10)

while True:
    guess = int(input("Guess a Number between 1-10: "))
    if guess == secret:
        print("Correct!")
        break
    else:
        print("try again")


