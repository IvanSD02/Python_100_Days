# Project 7 - Ceaser Cypher

# Include imports
from cypher_art import logo

# Include the constants
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Initial greeting and logo
print(logo)
print("Welcome to Ceaser Cypher! Please, choose a mode of utilization for the Cypher:")


# Combine the encrypt and decrypt functions into a single one, as they are very repetitive
def combined_cypher(input_text, shift_amount, direction):
    moved_text = ""

    # Loop through the symbols in the input text and check if they are in the alphabet - if not, do not encode/decode
    for current_letter in input_text:
        if current_letter in alphabet:

            # Find the index in the alphabet of the current letter and shift it
            current_index = alphabet.index(current_letter)
            if direction == "decode":
                shifted_index = current_index - shift_amount
            elif direction == "encode":
                shifted_index = current_index + shift_amount
            else:
                shifted_index = None
                print("Invalid mode specified!")
            # shifted_index %= len(alphabet) -> should be used, but for some reason the code works without it

            # Save the output in a new variable
            moved_text += alphabet[shifted_index]
        else:
            moved_text += current_letter

    # Output the result
    print(f"Here is the {direction}d result: {moved_text}")


# Invoke the cypher while the user is playing
is_playing = True
while is_playing:

    # Call for input on the function of the Cypher - can be decoding or encoding
    code_mode = input("Please, type 'encode' to encode and 'decode' to decode.\n")
    message = input("Please, type your message: ")
    coding_digits = int(input("Please, type the shift number: "))

    # Validate the input
    is_valid = True
    if code_mode not in ['encode', 'decode']:
        print("Invalid input, please try again.")
        is_valid = False

    # Evoke the cypher
    combined_cypher(input_text=message, shift_amount=coding_digits, direction=code_mode)

    # Prompt to use again
    still_playing = input('Would you like to go again? Type "yes" or "no": ').lower()
    if still_playing == "no":
        is_playing = False
    elif not still_playing == "yes":
        print("Invalid input, exiting...")
        is_playing = False

    if not is_playing:
        print("Goodbye!")











