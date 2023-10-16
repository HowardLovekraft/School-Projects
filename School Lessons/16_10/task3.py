for A in range(1000):
    flag = True
    for m in range(500):
        for n in range(500):
            if not(
                    ( (2*m + 3*n) > 40) or ((m < A) and (n <= A))
            ):
                flag = False
    if flag == True:
        print(A)
        break
