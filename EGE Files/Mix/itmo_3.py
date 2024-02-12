for N in range(0, 10):
    R = 0
    a = 1
    b = 1
    d = 0
    s = 0
    while True:
        if N > 0:
            d = N % 2
            if d == 1:
                R += b
            if d + s < 2:
                N //= 2
                s = d
            t = a
            a = b
            b = t + b
        else:
            if R >= 267:
                print(R, N)
                break
