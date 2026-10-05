# RSA Encryption and Decryption

p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = 3

message = 5

encrypted = pow(message, e, n)
decrypted = pow(encrypted, d, n)

print("RSA Encryption and Decryption")
print("Original message:", message)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
