def F(n):
    return 0.125 * n**2 + 3
max_i = 0
plus = 0
for i in range(60):
    dobt = F(i)
    print(i, 7*i - dobt)