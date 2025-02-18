# Project 8 - Secret Auction

# Include imports
from art import logo, logo_gavel

# Initial greeting and logos
print(logo)
print(logo_gavel)
print("Welcome to the Secret Auction!")

# Initialize the bidder's data structure
bidders = {}


# Create a function to calculate the biggest bid
def calculate_biggest_bid(saved_bidders):
    # Have a variable to save the current biggest bid and the name of the bidder
    biggest_bid = 0
    biggest_bidder_name = ""
    # Loop through all the bidders' bids and save the biggest one
    for bidder in saved_bidders:
        # Overwrite the biggest bid, if the current one is bigger than the last saved
        if saved_bidders[bidder] >= biggest_bid:
            biggest_bid = saved_bidders[bidder]
            biggest_bidder_name = bidder
            
    # Another simpler way to do the above block of code would be to use the max function
    # biggest_bid = max(bidders, key=bidders.get)

    print(f"The person with the biggest bid and winner is: {biggest_bidder_name} with the bid of ${biggest_bid}!")


# While there are participants available, collect input from the users
participants_leftover = True
while participants_leftover:
    # Collect input for the bidder's name and their bid
    name = input("What is your name? ")
    bid = int(input("How much would you like to bid? $"))

    # Save the bidder's information
    bidders[name] = bid

    # Ask for other bidders
    other_bidders_response = input('Are there any other bidders? Type "yes" for yes and "no" for no.').lower()

    # Validate the input and break the cycle, if the input is not valid and also check if there are other participants
    if other_bidders_response == "no":
        participants_leftover = False
    elif not other_bidders_response  == "yes":
        print("Invalid input provided! Stopping...")
        participants_leftover = False
        break

    # If there are no other participants, exit
    if not participants_leftover:
        print("Thank you all for participating!")
        break

    # Hide the previous response with prints of a new line
    print("\n" * 100)

# Output the biggest bid
calculate_biggest_bid(bidders)




