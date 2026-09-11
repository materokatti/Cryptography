# Encrypt the message : "What is your name ?"
# with the key K = "name"

def vigenere_encrypt(message, key):
    result = ""
    j = 0
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[j % len(key)]) - ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result

def vigenere_decrypt(message, key):
    result = ""
    j = 0
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[j % len(key)]) - ord('a')
            result += chr((ord(ch) - base - shift) % 26 + base)   # + => -
            j += 1
        else:
            result += ch
    return result

msg = "What is your name ?"
key = "name"

enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)

assert dec == msg
print("Round-trip test passed")