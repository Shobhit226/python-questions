for i in range(1,5):
    for j in range(i):
        print('*', end='')
    print()


print()
#another for practice
print()


for i in range(1,5):
    for j in range(4-i):
        print(" ", end='')
    
    for k in range(2 * i - 1):
        print("*", end='')
    print()