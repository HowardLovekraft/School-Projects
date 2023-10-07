ans = []
for i in range(245690, 245756 + 1):
    d = 2
    while d*d <= i and i%d != 0:
        d += 1
    else:
        ans.append([i - 245689, i])
for j in ans:
    print(j[0], j[1])
