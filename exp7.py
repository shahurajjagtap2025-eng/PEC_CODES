
import hashlib

# Input message
message = input("Enter a message: ")

# Generate MD5 hash
md5_hash = hashlib.md5(message.encode())

# Display the result
print("Original Message:", message)
print("MD5 Hash:", md5_hash.hexdigest())
