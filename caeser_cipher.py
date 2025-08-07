def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result = result + chr((ord(char) + shift - 65) % 26 + 65)
        elif (char.islower()):
            result = result + chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result = result + char

    return result 

text = input("Enter the text string to be encrypted: ")
shift = int(input("Enter the shift to be applied on the string: "))

print("Text: ", text)
print("Shift: ", shift)
print("Cipher: "+encrypt(text, shift))




