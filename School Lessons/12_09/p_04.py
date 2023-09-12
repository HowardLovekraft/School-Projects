res = []
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            s1 = a + b
            s2 = b + c
            if s2 <= s1:
                res.append(f'{s2}{s1}')
            else:
                res.append(f'{s1}{s2}')
if "1915" in res:
    print("1915 может быть")
elif "1815" in res:
    print("1815 может быть")
elif "188" in res:
    print("188 может быть")
elif "1518" in res:
    print("1518 может быть")
