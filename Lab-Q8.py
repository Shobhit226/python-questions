def swap(a, b):
    a, b = b, a
    return a, b

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before swapping: a = {a}, b = {b}")

a, b = swap(a, b)

print(f"After swapping: a = {a}, b = {b}")