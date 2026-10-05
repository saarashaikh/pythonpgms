# Caesar Cipher

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_cipher(message, shift)
decrypted = caesar_cipher(encrypted, -shift)

print("\nCaesar Cipher")
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
