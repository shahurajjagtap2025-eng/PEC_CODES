
# Diffie-Hellman Key Exchange Algorithm

# Publicly shared values
P = 23
G = 5

# Private keys of Alice and Bob
a = 6
b = 15

# Calculate public keys
A = pow(G, a, P)
B = pow(G, b, P)

print("Alice's Public Key:", A)
print("Bob's Public Key:", B)

# Calculate shared secret keys
alice_secret = pow(B, a, P)
bob_secret = pow(A, b, P)

print("Alice's Shared Secret:", alice_secret)
print("Bob's Shared Secret:", bob_secret)

# Verify shared keys
if alice_secret == bob_secret:
    print("Shared key established successfully!")
else:
    print("Key exchange failed!")
