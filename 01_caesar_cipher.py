# 1. Encrypt the message “Hello world !" with the key k = 8.
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

# print(caesar_cipher("Hello, World!", 8))

# 2. Define Dn, the decryption function.
# D_n(x) = x - k mod 26
# D_n(E_n(x)) = (x + k) - k mod 26 = x mod 26 = x

# 3. Decrypt the ciphertext (without the key) : “ Znl gur sbepr or jvgu lbh !" What is the key ?
# "May the force be with you !"
def decrypt_caesar_cipher(text):
    for shift in range(26):
        plain_text = ""
        for character in text:
            if character.isascii() and character.isalpha():
                base = ord('a') if character.islower() else ord('A')
                index = ord(character) - base
                shifted = (index - shift) % 26
                plain_text += chr(shifted + base)
            else:
                plain_text += character
        print(f"Shift {shift}: {plain_text}")

decrypt_caesar_cipher("Znl gur sbepr or jvgu lbh !")

# 4. What are the limits of this encryption scheme ?
# * Small keyspace (26 keys)
# * frequency analysis
# * deterministic