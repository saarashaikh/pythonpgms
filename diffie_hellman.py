# Diffie-Hellman Key Exchange

p = 23
g = 5

private_a = 6
private_b = 15

public_a = pow(g, private_a, p)
public_b = pow(g, private_b, p)

shared_key_a = pow(public_b, private_a, p)
shared_key_b = pow(public_a, private_b, p)

print("Diffie-Hellman Key Exchange")
print("Public value of A:", public_a)
print("Public value of B:", public_b)
print("Shared key calculated by A:", shared_key_a)
print("Shared key calculated by B:", shared_key_b)
