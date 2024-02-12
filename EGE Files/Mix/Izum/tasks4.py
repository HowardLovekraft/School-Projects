def F(n):
    if n == 1:
        return 2
    if n > 1 and n % 3 == 0:
        return F(n-1) + F(n/3)
    elif n > 1 and n % 3 != 0:
        return F(n-1) + 1


print(F(12))