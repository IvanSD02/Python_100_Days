# Project 6 - Hangman

# Imports
import random
from hangman_art import logo2, logo3, stages
from hangman_words import word_list # Get the list of possible words for the game

# Other constants
user_lives = 6

# Initial greeting
print("Welcome to the Hangman game!")
print(logo3)

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Output the blanks for the word
display_word = ""
for letters in chosen_word:
    display_word += "_"
print(f"Here is your word: {display_word}")

# Store the guessed letters, the stage of the hangman post and the game results
guessed_letters = []
current_stage_index = 0
game_over = False

# Loop through the word
while "_" in display_word:
    # Prompt the user to input a letter as a guess
    guessed_letter = input("What is the letter you would guess? ").lower()

    # Verify the character is not repeated
    if guessed_letter in guessed_letters:
        print("This letter was already selected, please try another one.")
        continue
    else:
        guessed_letters.append(guessed_letter)

    # Validate the input
    is_valid = True
    if not len(guessed_letter) == 1:
        print("Please insert a valid letter!")
        is_valid = False
        continue

    # Output if the guess was correct or not
    matched_word = ""
    is_letter_in_word = False
    if is_valid:
        for letter in chosen_word:
            # If the guessed letter is somewhere in the string, add it and visualize it
            if letter == guessed_letter:
                matched_word += guessed_letter
                is_letter_in_word = True
            # If the space for this letter is already guessed, do not change it
            elif letter in display_word:
                matched_word += letter
            else:
                matched_word += "_"

        # If the letter was not guessed, output the corresponding message and visualization
        if not is_letter_in_word:
            print(f"You guessed wrong! The letter '{guessed_letter}' is not in the word.")
            current_stage_index += 1
            user_lives -= 1

            # If the user has run out of lives, break the loop
            if user_lives == 0:
                game_over = True
                break
            else:
                print(f"You lost a life! {user_lives}/6 remain.")

        else:
            print("Correct! You guessed a letter!")

    # Display the results
    display_word = matched_word
    print(display_word)

    print(stages[current_stage_index])

# Print the corresponding message based on whether the player has won
if not game_over and "_" not in display_word:
    print(f'Good job, you won! The word was: "{chosen_word}"')
    print(logo2)
else:
    print(f'You lost! The word was "{chosen_word}"')
    print(stages[-1])
