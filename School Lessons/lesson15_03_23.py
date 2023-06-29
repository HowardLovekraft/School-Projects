# https://ege.sdamgia.ru/problem?id=317098
# test: r = 65, ans = 0.625

r = float(input())
ans = r - ((r - 0.37) / (21 * (0.4 / (r + 0.1))))
print(ans)


# https://math-ege.sdamgia.ru/problem?id=27983
# test: u = 180000, ans = 4.0 (4 is right too)

u = float(input())
ans = 5 * ((1 - (u**2 / (3 * 10**5)**2)) ** 0.5)
print(ans)
