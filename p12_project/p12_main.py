# Project 12 - Higher Or Lower Game

# Include imports
import random
from game_data import data
from art import logo, vs


# Functions definition
def compare_entries(entry1, entry2, current_score):
    # Prompt the user to compare the two
    print(f"Compare A: {entry1['name']}, a professional {entry1['description']}, from {entry1['country']}.")
    print(vs)
    print(f"Against B: {entry2['name']}, a professional {entry2['description']}, from {entry2['country']}.")

    # Save the choice between the two entries
    chosen_entry = input("Please choose between A or B: ").upper()

    # Calculate the account with more subscribers
    if entry1['follower_count'] > entry2['follower_count']:
        most_followers_entry = entry1
    else:
        most_followers_entry = entry2

    # Validate the input and return the correct entry
    if chosen_entry in ["A", "B"]:
        if most_followers_entry == entry1 and chosen_entry == "A":
            print(f"Good job! {entry1['name']} has more followers! Your score is now {current_score+1}")
        elif most_followers_entry == entry2 and chosen_entry == "B":
            print(f"Good job! {entry2['name']}has more followers! Your score is now {current_score+1}")
        else:
            print(f"Incorrect! You lose! Final score: {current_score}")
            return
    else:
        print("Invalid input provided!")
        return

    return most_followers_entry


def play_game():
    # Output the logo
    print(logo)

    # Choose two random entries to compare initially
    entry1 = random.choice(data)
    entry2 = random.choice(data)
    if entry1 == entry2:
        entry2 = random.choice(data) # TODO - make more robust

    # While the player is still guessing, keep score
    still_guessing = True
    current_score = 0
    while still_guessing:
        # Output the prompt for the user to choose between the two entries
        print("Choose - Who has more followers? 🤔")

        # Save the progress based on the chosen entry by the user
        latest_guess = compare_entries(entry1, entry2, current_score)
        if latest_guess is None:
            # If no entry was returned, then the user lost
            break
        else:
            # If an entry was returned, then it should be compared to another random entry
            current_score += 1
            entry1 = latest_guess
            entry2 = random.choice(data)


# Initial greeting
print("Welcome to the Higher Lower game! Make your best guess!")

# Play the game
play_game()