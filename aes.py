# AES Encryption and Decryption
# Install the library first if needed:
# pip install cryptography

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = input("Enter message: ").encode()

encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted).decode()

print("\nAES Encryption and Decryption")
print("Encrypted:", encrypted.decode())
print("Decrypted:", decrypted)
