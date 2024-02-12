for A in range(0, 10000):
    flag = True
    for x in range(0, 100):
        t_f = int(bin(25)[2:])
        f_o = int(bin(51)[2:])
        A_b = int(bin(A)[2:])
        x_b = int(bin(x)[2:])

        tense = x_b & f_o != 0 <= (x_b & A_b == 0 <= x_b & t_f != 0)
        if not tense:
            flag = False
            break
    if flag:
        print(A)
        break