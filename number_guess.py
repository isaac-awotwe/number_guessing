# import packages
import random
from art import logo


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")
game_on = True

while game_on:
    guess = int(input("Make a guess: "))
    if guess != number:
        attempts-=1
        if attempts == 0:
            game_on = False
            print("You've run out of guesses. Refresh the page to run again.")
        else:
            if guess > number:
                print("Too high.")
                print("Guess again.")
            elif guess < number:
                print("Too low.")
                print("Guess again")
            print(f"You have {attempts} attempts remaining.")
    else:
        game_on = False
        print(f"You got it! The answer was {number}.")


