for x in range(0, 2):
    for w in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                f = ((x <= y) <= z) or (w <= (y and z))
                if f == 0:
                    print(y, x, w, z)