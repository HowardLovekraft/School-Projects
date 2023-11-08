for A in range(200):
    flag = True
    for y in range(200):
        for x in range(200):
            if not((y + 2*x < A) or (x > 15) or (y > 30)):
                flag = False
    if flag:
        print(A)
        break