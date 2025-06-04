str1 = str(input("Enter a String: "))
str2 = str(input("Enter a String: "))
str3 = str1 + str2
print("Concatenate String: ", str3)
index1 = int(input("Enter first index: "))
index2 = int(input("Enter second index: "))
print("Substring of Concatenate String from index no. ", end='')
print(index1, end='')
print(" to ", end='')
print(index2, end='')
print(" : ")
print(str3[index1: index2])

# Might be complex but i don't know any other way to write it.