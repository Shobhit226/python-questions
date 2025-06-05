num = [int(x) for x in input("Enter numbers with spaces: ").split()]

even_num = [x for x in num if x % 2 == 0]

print("Even numbers are: ", even_num)