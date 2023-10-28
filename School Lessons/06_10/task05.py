for kf in range(100, 1000):
    a = [int(i) for i in list(str(kf))]
    f1, f2 = a[0] + a[1], a[1] + a[2]
    num = int(str(max(f1, f2)) + str(min(f1, f2)))
    if num == 1711:
        print(kf)
        break