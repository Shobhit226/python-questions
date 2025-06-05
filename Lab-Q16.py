char = input("Enter a single character: ")

if len(char) != 1:
    print("Enter only one character.")

elif char.isdigit():
    print("Input is a Digit.")

elif char.islower():
    print("Input is a Lowercase character.")

elif char.isupper():
    print("Input is a Uppercase character.")

else:
    print("Input is a special character.")