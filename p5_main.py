# Project 5

# Imports
import random

# Initial greeting
print("Welcome to the PyPassword Generator!")

# Initialize constant variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Prompt the user for symbol count input and save it
num_letters = int(input("How many letters would you like in your password?\n"))
num_digits = int(input("How many digits would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

# Validate input
valid_input = True
if not num_letters >= 0:
    print("Invalid input for a number of letters!")
    valid_input = False
elif not num_digits >= 0:
    print("Invalid input for a number of digits!")
    valid_input = False
elif not num_symbols >= 0:
    print("Invalid input for a number of symbols!")
    valid_input = False

# Pick random letters, digits and symbols based on the numbers given by the user
rand_sequence = []
if valid_input:
    for letter in range(num_letters):
        rand_letter = random.choice(letters)
        rand_sequence.append(rand_letter)

    for number in range(num_digits):
        rand_num = random.choice(numbers)
        rand_sequence.append(rand_num)

    for symbol in range(num_symbols):
        rand_symbol = random.choice(symbols)
        rand_sequence.append(rand_symbol)

    # Shuffle the list to get a random sequence
    random.shuffle(rand_sequence)

    # Convert the sequence to a string for the password
    password = "".join(rand_sequence)  # As this has not been studied yet, we can also use a loop, example given below

    # Same code as above, but with a loop
    '''
    password = ""
    for symbol in rand_sequence:
        password += symbol
    '''

    # Output the new password
    print(f"Your brand new password will be: {password}")
else:
    print("Could not generate a password due to invalid input!")
