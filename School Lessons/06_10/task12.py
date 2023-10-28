ans = 0
for n in range(200, 1000):
    inp = "1" * n
    while "1111" in inp:
        inp.replace("1111", "22", 1)
        if "222" in inp:
            inp.replace("222", "1", 1)
    cnt = inp.count("1")
    print(f"Единичек: {cnt}, {ans}")
    if cnt > ans:
        ans = cnt
    else:
        print(n)
        break