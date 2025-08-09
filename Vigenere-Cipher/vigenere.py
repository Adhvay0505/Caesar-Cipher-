def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def encrypted_vigenere(text, key):
    encrypted_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char

        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

def decrypted_vigenere(text, key):
    decrypted_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char

        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)


text_to_encrypt = input("ENTER THE TEXT TO ENCRYPT: ")
key = input("ENTER THE KEY: ")

encrypted_text = encrypted_vigenere(text_to_encrypt, key)
print("Encrypted text is: ",encrypted_text)

decrypted_text = decrypted_vigenere(encrypted_text, key)
print("Decrypted text is: ",decrypted_text)




