# Include the constants
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Create the encoding function - OBSOLETE
def encode(original_text, shift):
    cipher_text = ""
    for current_letter in original_text:
        if current_letter in alphabet:
            current_index = alphabet.index(current_letter)
            shifted_index = current_index + shift
            # shifted_index %= len(alphabet) -> should be used, but for some reason the code works without it
            cipher_text += alphabet[shifted_index]
        else:
            cipher_text += current_letter

    print(f"Here is the encoded result: {cipher_text}")


# Create decoding function - OBSOLETE
def decode(encoded_text, shift):
    normal_text = ""
    for current_letter in encoded_text:
        if current_letter in alphabet:
            current_index = alphabet.index(current_letter)
            shifted_index = current_index - shift
            # shifted_index %= len(alphabet) -> should be used, but for some reason the code works without it
            normal_text += alphabet[shifted_index]
        else:
            normal_text += current_letter

    print(f"Here is the decoded result: {normal_text}")


# Set called logic based on the chosen mode (encoding or decoding) - OBSOLETE
def cypher(original_text, shift, direction):
    if direction == "encode":
        encode(original_text=original_text, shift=shift)
    elif direction == "decode":
        decode(encoded_text=original_text, shift=shift)
    else:
        print("Invalid mode specified!")  # For now it is impossible to reach, but it is a good practice