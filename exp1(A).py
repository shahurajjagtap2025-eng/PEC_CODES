
# Program to find GCD and LCM using Euclidean Algorithm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

# Euclidean Algorithm to find GCD
while b != 0:
    a, b = b, a % b

gcd = abs(a)

# Calculate LCM
if x == 0 or y == 0:
    lcm = 0
else:
    lcm = abs(x * y) // gcd

print("GCD =", gcd)
print("LCM =", lcm)
