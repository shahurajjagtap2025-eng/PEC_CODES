#Implementation of Transposition technique (Railfence/Transposition) 

# Rail Fence Cipher Encryption and Decryption

def encrypt(text, rails):
    fence = ['' for _ in range(rails)]
    row = 0
    direction = 1

    for ch in text:
        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(fence)


def decrypt(cipher, rails):
    pattern = []
    row = 0
    direction = 1

    for _ in cipher:
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    counts = [pattern.count(r) for r in range(rails)]
    fence = []
    pos = 0

    for count in counts:
        fence.append(list(cipher[pos:pos + count]))
        pos += count

    result = ''
    indices = [0] * rails

    for r in pattern:
        result += fence[r][indices[r]]
        indices[r] += 1

    return result


message = input("Enter the message: ").replace(" ", "")
rails = int(input("Enter number of rails: "))

if rails < 2:
    print("Number of rails must be at least 2.")
else:
    cipher = encrypt(message, rails)
    print("Encrypted Message:", cipher)

    original = decrypt(cipher, rails)
    print("Decrypted Message:", original)
