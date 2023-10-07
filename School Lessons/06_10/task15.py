for A in range(1000):
    flag = True
    for x in range(100):
        for y in range(100):
            f = ((2*x + 3*y) < A) or (x >= y) or (y > 24)
            if not(f):
                flag = False
    if flag:
        print(A)
        break