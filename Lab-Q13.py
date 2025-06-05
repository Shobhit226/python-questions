def prime(n):
    for n in range(1, n):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n, end=' ')

prime(20)