for A in range(200):
    flag = True
    for x in range(150):
        for y in range(150):
            f = (2*x + y < A) or (x < y) or (21 <= x)
            if not f:
                flag = False
    if flag:
        print(A)
        break
