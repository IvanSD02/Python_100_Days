# Project 11 - Guess The Number Game

# Include imports
import random
from art import logo

# Constants Definition
MAX_NUMBER = 100
MAX_ATTEMPTS_EASY = 10
MAX_ATTEMPTS_HARD = 5


# Functions Definition
def choose_difficulty():
    print(f"I am thinking of a number between 1 and {MAX_NUMBER}")

    # Request input for a difficulty
    difficulty = input('Choose a difficulty. Type "easy" or "hard". ').lower()

    # Validate the input and return the number of attempts based on the difficulty
    number_attempts = 0
    if difficulty == "easy":
        number_attempts = MAX_ATTEMPTS_EASY
    elif difficulty == "hard":
        number_attempts = MAX_ATTEMPTS_HARD
    else:
        print("Invalid input provided, exiting...")
        return

    return number_attempts


def choose_number():
    return random.randint(1, MAX_NUMBER)


def play_game(attempts):
    print(f"You have {attempts} to guess the number.")

    # Choose a random number
    chosen = choose_number()

    # Loop until there are no more attempts available
    while attempts > 0:
        # Prompt the user to make a guess
        guess = int(input("Make a guess. "))

        # Based on the guess decide to continue or not
        if guess > chosen:
            print("Too high.")
        elif guess < chosen:
            print("Too low.")
        else:
            print("You guessed!")
            return True

        # If we have not guessed yet, print the remaining attempts
        attempts -= 1
        print(f"You have {attempts} attempts remaining.")

    # If we have exited the loop and have not yet guessed, we have lost
    print("You lost, too bad!")
    return False


# Initial greeting
print(logo)
print("Welcome to the Number Guessing Game!")

# Choose a difficulty and validate the input
num_attempts = choose_difficulty()

# Play the game based on the chosen difficulty
play_game(attempts=num_attempts)


