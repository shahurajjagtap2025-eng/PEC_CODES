#Aim
#To implement modular arithmetic operations — addition, subtraction, multiplication, and division — using Python.***

# Modular Arithmetic Operations

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
m = int(input("Enter modulus: "))

print("Addition:", (a + b) % m)
print("Subtraction:", (a - b) % m)
print("Multiplication:", (a * b) % m)

# Modular Division using modular inverse
if b % m == 0:
    print("Division is not possible")
else:
    try:
        inverse = pow(b, -1, m)
        print("Division:", (a * inverse) % m)
    except ValueError:
        print("Modular inverse does not exist")
