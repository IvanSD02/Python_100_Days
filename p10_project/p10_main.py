# Project 10 - Blackjack

# Include imports
import random
from art import logo

# Constants definition
named_cards = {
    "A": 11,
    "K": 10,
    "Q": 10,
    "J": 10,
}

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "K", "Q", "J"]


# Function definitions
def convert_named_cards_to_points(deck, named_deck):
    new_deck = []
    for card in deck:
        if not type(card) == int:
            new_deck.append(named_deck[card])
        else:
            new_deck.append(card)
    return new_deck


def decide_value_of_ace(deck):
    if "A" in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return deck


def blackjack_logic(deck, named_deck):
    # Save the decks for the player and the computer separately
    player_cards = []
    computer_cards = []

    # Convert the given deck to points
    points_deck = convert_named_cards_to_points(deck, named_deck)

    # Generate two random cards for the player and one for the computer
    player_cards.append(random.choice(points_deck))
    player_cards.append(random.choice(points_deck))
    computer_first_card = random.choice(points_deck)
    computer_cards.append(computer_first_card)

    # Overwrite the ace, if needed for the player (the computer has only one card and does not need this)
    decide_value_of_ace(player_cards)

    player_score = sum(player_cards)
    computer_score = sum(computer_cards)

    # Loop, which will represent each hand and drawing of a card
    while player_score <= 21:
        # Output the initial cards
        print(f"\tYour cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"\tComputer's first card: {computer_first_card}")

        # Prepare the computer's cards - draw a second hand for the computer and overwrite the ace, if needed
        while computer_score < 17:
            # If the score is lower than 17, the computer will draw a another card
            computer_cards.append(random.choice(points_deck))
            decide_value_of_ace(computer_cards)
            computer_score = sum(computer_cards)

        # Prompt the player to choose whether to draw or not based on the previous cards
        player_choice = input("Type 'yes' to get another card, type 'no' to pass: ")

        # Validate the input and check the choice
        if player_choice == "yes":
            print("You chose to draw...")

            # Draw another card, if the player has chosen to draw and overwrite the ace, if needed
            player_cards.append(random.choice(points_deck))
            decide_value_of_ace(computer_cards)
            player_score = sum(player_cards)

        elif player_choice == "no":
            print("You chose to pass...")
            break
        else:
            print("Invalid input, exiting...")
            return

    # Show final results
    print(f"\tYour cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"\tComputer's cards: {computer_cards}, current score: {sum(computer_cards)}")

    # Decide who wins
    if player_score > 21:
        print("You went over 21! You lose :(")
    elif computer_score > 21:
        print("The opponent went over 21! You win :)")
    else:
        if player_score == computer_score:
            print("It's a draw!")
        elif player_score == 21:
            print("You got Blackjack! You win :)")
        elif computer_score == 21:
            print("The opponent got Blackjack! You lose :(")
        elif player_score > computer_score:
            print("You have the higher score, you win :)")
        else:
            print("The opponent has the higher score, you lose :(")


# Initial greeting
print("Hello, welcome to the Blackjack game!")


# Create a function for a new blackjack game
def blackjack():
    # Define a flag to verify the player is still playing
    is_playing = True

    # Loop while the player is in a game
    while is_playing:
        # Prompt the user to choose whether they would like to play
        play_choice = input('Would you like to play a game of blackjack? Type "yes" or "no". ').lower()

        # Validate the input and check the choice
        if play_choice == "no":
            print("Thanks for participating!")
            is_playing = False
            return
        elif play_choice == "yes":
            # If they are playing, output the logo and start a game
            print(logo)
            blackjack_logic(cards, named_cards)
        else:
            print("Invalid input, exiting...")
            return


blackjack()
