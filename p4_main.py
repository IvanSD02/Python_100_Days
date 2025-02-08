# Project #4

# Imports
import random

# Save the Rock Paper Scissors ASCII Art

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Save the variables in a list
game_choices = [rock, paper, scissors]

# Initial greeting
print("Welcome to the Rock Paper Scissors Game!")

# Input the choice for the player
player_choice_index = int(input("What will you choose? Please type: 0 for Rock, 1 for Paper, 2 for Scissors\n"))

# Validate the input
valid_input = True
if player_choice_index == 0 or player_choice_index == 1 or player_choice_index == 2:
    player_choice = game_choices[player_choice_index]
else:
    valid_input = False
    player_choice = None

# Choose a random choice by the computer
computer_choice = random.choice(game_choices)

# Print the inputs
print("You chose:")
print(player_choice)

print("Computer chose:")
print(computer_choice)

# Determine which person wins based on the game rules
if valid_input:
    if player_choice == computer_choice:
        print("You picked the same, it is a draw!")
    else:
        if player_choice == rock:
            if computer_choice == scissors:
                print("Rock wins. Victory!")
            else:
                print("Paper wins. You lost!")
        elif player_choice == scissors:
            if computer_choice == paper:
                print("Scissors wins. Victory!")
            else:
                print("Rock wins. You lost!")
        elif player_choice == paper:
            if computer_choice == rock:
                print("Paper wins. Victory!")
            else:
                print("Scissors wins. You lost!")
else:
    print("Invalid input provided.")
