n  = int(input("Enter no. of terms : "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please! Enter valid no. of terms.")

else:
    print("Fibonacci Series is : ")

    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1