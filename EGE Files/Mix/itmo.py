def summy(a, b):
    if a == 0 and b == 0:
        return 0, 0
    elif a == 0 and b == 1:
        return 1, 0
    elif a == 1 and b == 0:
        return 1, 0
    elif a == 1 and b == 1:
        return 0, 1

for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                s1, c1 = summy(x1, x2)
                s2, c2 = summy(not(x1), not(x2))
                s3, c3 = summy(x3, x4)
                s4, c4 = summy(not(x3), not(x4))

                res1 = s1 or c2
                res2 = s2 and c3
                res3 = s3 or c4
                res4 = s4 and c1

                result = res1 or res2 or res3 or res4
                if not(result):
                    print(x1, x2, x3, x4, "Hooray")
                    break

