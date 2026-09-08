def caesar_cipher(text, shift):
    shift_amount = shift % 26
    cipher_text = ""
    for character in text:
        if character.isascii() and character.isalpha():
            base = ord('a') if character.islower() else ord('A')
            index = ord(character) - base # Numbering
            shifted = (index + shift_amount) % 26 # Shifted
            cipher_text += chr(shifted + base) # Restored
        else:
            cipher_text += character
    return cipher_text

print(caesar_cipher("Hello, World!", 8))