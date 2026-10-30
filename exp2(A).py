#Implementation of following: substitution technique :(Caesar Cipher/Playfair) 

# Caesar Cipher Encryption and Decryption

def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += ch
    return result

def decrypt(text, key):
    return encrypt(text, -key)

message = input("Enter the message: ")
key = int(input("Enter the key (1-25): "))

cipher = encrypt(message, key)
print("Encrypted Message:", cipher)

original = decrypt(cipher, key)
print("Decrypted Message:", original)
