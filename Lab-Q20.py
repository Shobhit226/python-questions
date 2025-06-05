str = input("Enter a string: ")
substr = input("Enter a substring: ")

str = str.replace(" ", "").lower()
substr = substr.replace(" ", "").lower()

if substr in str:
    print("Substring is present in the given String.")

else:
    print("Substring is not present in the given String.")