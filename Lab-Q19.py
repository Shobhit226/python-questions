str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Strings are Anagrams.")

else:
    print("Strings are not Anagrams.")

print(sorted(str1)) #for curious folks
print(sorted(str2)) #for curious folks