
# RSA Algorithm Implementation

# Step 1: Choose two prime numbers
p = 3
q = 11

# Step 2: Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose public key e
e = 3

# Step 4: Calculate private key d
d = pow(e, -1, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))

# Step 5: Input message as a number
message = int(input("Enter message (0 to 32): "))

if 0 <= message < n:
    # Encryption
    ciphertext = pow(message, e, n)
    print("Encrypted Message:", ciphertext)

    # Decryption
    decrypted = pow(ciphertext, d, n)
    print("Decrypted Message:", decrypted)
else:
    print("Message must be between 0 and", n - 1)
