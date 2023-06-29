for x in range(0, 2):
    for w in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                f = ((x <= y) <= w) or (z <= (y and w))
                if f == 0:
                    print(z, y, x, w)